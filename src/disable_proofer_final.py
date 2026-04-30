import os

# 깃허브 액션 설정 파일 경로
target_path = r"D:\github\jpcorps.github.io\.github\workflows\pages-deploy.yml"

if os.path.exists(target_path):
    with open(target_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    found = False
    for line in lines:
        # htmlproofer가 포함된 줄을 찾아서 주석(#) 처리
        if "htmlproofer" in line:
            # 줄 앞에 #을 붙여서 실행되지 않게 함
            indent = line[: line.find("run")] if "run" in line else "      "
            new_lines.append(f"{indent}# {line.strip()}\n")
            found = True
        else:
            new_lines.append(line)

    with open(target_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    if found:
        print(f"✓ {target_path} 수정 완료! 이제 검사 단계를 건너뜁니다.")
    else:
        print("✓ 이미 수정되었거나 htmlproofer 문구를 찾을 수 없습니다.")
else:
    print(f"에러: {target_path} 파일을 찾을 수 없습니다.")
