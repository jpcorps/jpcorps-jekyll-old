import os

config_path = r"D:\github\jpcorps.github.io\_config.yml"

# 새로 넣을 giscus 설정 내용
new_comments_section = """comments:
  # Global switch for the post-comment system. Keeping it empty means disabled.
  provider: giscus
  # The provider options are as follows:
  disqus:
    shortname: 
  utterances:
    repo: 
    issue_term: 
  # Giscus options › https://giscus.app
  giscus:
    repo: jpcorps/jpcorps.github.io
    repo_id: R_kgDOSOA18Q
    category: General
    category_id: DIC_kwDOSOA18c4C7-G6
    mapping: pathname
    strict: 0
    input_position: bottom
    lang: ko
    reactions_enabled: 1"""

if os.path.exists(config_path):
    with open(config_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 기존 comments: 섹션을 찾아서 교체 (정규표현식 사용)
    import re

    # comments: 부터 다음 빈 줄이나 파일 끝까지를 찾아서 교체
    new_content = re.sub(
        r"comments:.*?(?=\n\n|\Z)", new_comments_section, content, flags=re.DOTALL
    )

    with open(config_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"성공! {config_path} 파일이 업데이트되었습니다.")
else:
    print(f"에러: {config_path} 파일을 찾을 수 없습니다.")
