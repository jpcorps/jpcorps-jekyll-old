import os
import shutil
import re
import urllib.parse
from datetime import datetime
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from PIL import Image

# --- 설정 ---
SOURCE_BASE_DIR = r"C:\Users\jpcor\Desktop\EGtoTS\chulin28ho\post"
GITHUB_REPO_DIR = r"D:\github\jpcorps.github.io"
POSTS_OUTPUT_DIR = os.path.join(GITHUB_REPO_DIR, "_posts")
IMAGES_OUTPUT_DIR = os.path.join(GITHUB_REPO_DIR, "assets", "images", "posts")
IMAGE_URL_PREFIX = "/assets/images/posts/"


# 1. _config.yml 완벽 복구
def fix_config():
    config_path = os.path.join(GITHUB_REPO_DIR, "_config.yml")
    content = """# The Site Configuration
theme: jekyll-theme-chirpy
lang: ko-KR
timezone: Asia/Seoul
title: "대충 살아가는 게임개발자"
tagline: "이글루스와 티스토리를 정처없이 떠돌아다니다 여기로 옮겨옴"
description: >-
  TA 대마왕의 대충 살아가는 게임개발자 블로그

url: "https://jpcorps.github.io"
github:
  username: jpcorps

social:
  name: 대마왕
  email: jpcorp@hanmail.net
  links:
    - https://github.com/jpcorps

theme_mode: light
avatar: /Face.png
toc: true

comments:
  provider: giscus
  giscus:
    repo: jpcorps/jpcorps.github.io
    repo_id: R_kgDOSOA18Q
    category: General
    category_id: DIC_kwDOSOA18c4C7-G6
    mapping: pathname
    strict: 0
    input_position: bottom
    lang: ko
    reactions_enabled: 1

paginate: 10
baseurl: ""

kramdown:
  footnote_backlink: "&#8617;&#xfe0e;"
  syntax_highlighter: rouge

collections:
  tabs:
    output: true
    sort_by: order

defaults:
  - scope:
      path: ""
      type: posts
    values:
      layout: post
      comments: true
      toc: true
      permalink: /posts/:title/
  - scope:
      path: ""
      type: tabs
    values:
      layout: page
      permalink: /:title/

jekyll-archives:
  enabled: [categories, tags]
  layouts:
    category: category
    tag: tag
  permalinks:
    tag: /tags/:name/
    category: /categories/:name/
"""
    with open(config_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("✓ _config.yml 복구 완료")


# 2. 이미지 최적화 함수
def optimize_image(source_path, target_path):
    ext = os.path.splitext(source_path)[1].lower()
    if ext == ".gif":
        try:
            shutil.copy2(source_path, target_path)
            return True
        except:
            return False
    try:
        with Image.open(source_path) as img:
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            if img.width > 1200:
                h = int((1200 / img.width) * img.height)
                img = img.resize((1200, h), Image.Resampling.LANCZOS)
            img.save(target_path, "JPEG", quality=75, optimize=True)
            return True
    except:
        try:
            shutil.copy2(source_path, target_path)
            return True
        except:
            return False


# 3. 포스트 변환 함수 (Liquid 충돌 방지 추가)
def process_file(file_path):
    filename = os.path.basename(file_path)
    folder_name = os.path.splitext(filename)[0]
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        soup = BeautifulSoup(f, "html.parser")
    title = (
        soup.find("title").text.strip() if soup.find("title") else "Untitled"
    ).replace('"', "'")
    date_tag = soup.find("span", class_="time")
    dt = (
        datetime.strptime(date_tag.text.strip(), "%Y-%m-%d %H:%M:%S")
        if date_tag
        else datetime.now()
    )
    content_div = soup.find("div", class_="content") or soup.find("body")
    if not content_div:
        return

    # 이미지 처리
    for img in content_div.find_all("img"):
        src = img.get("src", "")
        if src and not src.startswith(("http", "data:")):
            img_filename = os.path.basename(urllib.parse.unquote(src))
            local_path = os.path.join(
                os.path.dirname(file_path), folder_name, img_filename
            )
            if os.path.exists(local_path):
                ext = os.path.splitext(img_filename)[1].lower()
                new_name = f"{dt.strftime('%Y%m%d_%H%M%S')}_{os.path.splitext(img_filename)[0]}{ext if ext=='.gif' else '.jpg'}"
                if optimize_image(
                    local_path, os.path.join(IMAGES_OUTPUT_DIR, new_name)
                ):
                    img["src"] = f"{IMAGE_URL_PREFIX}{new_name}"

    # 마크다운 변환 및 Liquid 충돌 방지 ({% raw %})
    html_content = content_div.decode_contents()
    markdown_text = md(html_content, heading_style="ATX").replace("http://", "https://")

    # 핵심: 본문을 raw 태그로 감싸서 C# 코드 등의 충돌 방지
    safe_content = "{% raw %}\n" + markdown_text + "\n{% endraw %}"

    frontmatter = f"---\nlayout: post\ntitle: \"{title}\"\ndate: {dt.strftime('%Y-%m-%d %H:%M:%S')}\ncategories: [이글루스 백업, \"{dt.strftime('%Y-%m')}\"]\n---\n\n"

    out_name = f"{dt.strftime('%Y-%m-%d')}-{re.sub(r'[\\\\/*?:\"<>|]', '', title).replace(' ', '-')}.md"
    with open(os.path.join(POSTS_OUTPUT_DIR, out_name), "w", encoding="utf-8") as f:
        f.write(frontmatter + safe_content)


def main():
    fix_config()
    print("--- 6천개 글 마스터 변환 시작 ---")
    shutil.rmtree(POSTS_OUTPUT_DIR, ignore_errors=True)
    os.makedirs(POSTS_OUTPUT_DIR, exist_ok=True)

    sub_dirs = sorted(
        [
            d
            for d in os.listdir(SOURCE_BASE_DIR)
            if os.path.isdir(os.path.join(SOURCE_BASE_DIR, d))
        ]
    )
    for sub_dir in sub_dirs:
        print(f"처리 중: {sub_dir}")
        folder = os.path.join(SOURCE_BASE_DIR, sub_dir)
        for f in os.listdir(folder):
            if f.endswith(".html"):
                process_file(os.path.join(folder, f))
    print("\n✓ 모든 작업 완료! 이제 푸시하세요.")


if __name__ == "__main__":
    main()
