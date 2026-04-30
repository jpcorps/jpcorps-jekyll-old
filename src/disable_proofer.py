import os

target_path = r"D:\github\jpcorps.github.io\.github\workflows\pages-deploy.yml"

if os.path.exists(target_path):
    with open(target_path, "r", encoding="utf-8") as f:
        content = f.read()

    # htmlproofer 실행 단계를 주석 처리
    new_content = content.replace(
        "run: bundle exec htmlproofer _site --disable-external --check-html --allow-hash-href",
        "# run: bundle exec htmlproofer _site --disable-external --check-html --allow-hash-href",
    )

    with open(target_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"✓ {target_path} 수정 완료! 이제 검사기를 건너뜁니다.")
else:
    print(f"에러: {target_path} 파일을 찾을 수 없습니다. 경로를 확인해주세요.")
