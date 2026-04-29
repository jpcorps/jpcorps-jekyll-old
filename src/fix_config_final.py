import os

config_path = r"D:\github\jpcorps.github.io\_config.yml"

# 완벽하게 복구 및 설정된 전체 내용
full_config = """# The Site Configuration

# Import the theme
theme: jekyll-theme-chirpy

lang: ko-KR
timezone: Asia/Seoul

title: 대충 살아가는 게임개발자
tagline: 이글루스와 티스토리를 정처없이 떠돌아다니다 여기로 옮겨옴
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

webmaster_verifications:
  google:
  bing:
  alexa:
  yandex:
  baidu:
  facebook:

analytics:
  google:
    id:
  goatcounter:
    id:
  umami:
    id:
    domain:
  matomo:
    id:
    domain:
  cloudflare:
    id:
  fathom:
    id:

pageviews:
  provider:

theme_mode: # [light | dark]

cdn:
avatar: /Face.png
social_preview_image:
toc: true

comments:
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
    reactions_enabled: 1

assets:
  self_host:
    enabled:
    env:

pwa:
  enabled: true
  cache:
    enabled: true
    deny_paths:

paginate: 10
baseurl: ""

kramdown:
  footnote_backlink: "&#8617;&#xfe0e;"
  syntax_highlighter: rouge
  syntax_highlighter_opts:
    css_class: highlight
    span:
      line_numbers: false
    block:
      line_numbers: true
      start_line: 1

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
      path: _drafts
    values:
      comments: false
  - scope:
      path: ""
      type: tabs
    values:
      layout: page
      permalink: /:title/

sass:
  style: compressed

compress_html:
  clippings: all
  comments: all
  endings: all
  profile: false
  blanklines: false
  ignore:
    envs: [development]

exclude:
  - "*.gem"
  - "*.gemspec"
  - docs
  - tools
  - README.md
  - LICENSE
  - purgecss.js
  - "*.config.js"
  - "package*.json"

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
    f.write(full_config)

print(f"완료! {config_path} 파일을 완벽하게 복구 및 수정했습니다.")
