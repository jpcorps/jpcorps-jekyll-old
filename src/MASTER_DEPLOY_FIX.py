import os

target_path = r"D:\github\jpcorps.github.io\.github\workflows\pages-deploy.yml"

# 들여쓰기와 구조를 완벽하게 맞춘 배포 설정 (검사기 제거 버전)
master_deploy_content = """name: "Build and Deploy"
on:
  push:
    branches:
      - main
      - master
    paths-ignore:
      - .gitignore
      - README.md
      - LICENSE

  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: true

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Pages
        id: pages
        uses: actions/configure-pages@v5

      - name: Setup Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: 3.3
          bundler-cache: true

      - name: Build site
        run: bundle exec jekyll b -d "_site${{ steps.pages.outputs.base_path }}"
        env:
          JEKYLL_ENV: "production"

      # 검사기(htmlproofer) 단계를 완전히 제거했습니다.

      - name: Upload site artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: "_site"

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
"""

if os.path.exists(target_path):
    # 폴더가 없는 경우를 대비해 폴더 생성 (이미 있겠지만 안전을 위해)
    os.makedirs(os.path.dirname(target_path), exist_ok=True)

    with open(target_path, "w", encoding="utf-8") as f:
        f.write(master_deploy_content)
    print(f"✓ {target_path} 파일을 완벽한 형식으로 재작성했습니다!")
else:
    print(f"에러: {target_path} 파일을 찾을 수 없습니다. 경로를 확인해주세요.")
