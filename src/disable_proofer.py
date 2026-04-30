import os

target_path = r"D:\github\jpcorps.github.io\.github\workflows\pages-deploy.yml"

if os.path.exists(target_path):
    with open(target_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        # htmlproofer가 들어간 줄은 무조건 주석(#) 처리합니다.
        if "htmlproofer" in line:
            # 이미 주석 처리되어 있지 않다면 앞에 # 추가
            clean_line = line.lstrip()
            if not clean_line.startswith("#"):
                new_lines.append("      # " + clean_line)
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    with open(target_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print(f"✓ {target_path} 강제 주석 처리 완료!")
else:
    print("파일을 찾을 수 없습니다.")
