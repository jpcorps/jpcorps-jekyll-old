import os

posts_dir = r"D:\github\jpcorps.github.io\_posts"
files = [f for f in os.listdir(posts_dir) if f.endswith(".md")]

if files:
    target_file = os.path.join(posts_dir, files[0])
    print(f"파일 진단 중: {files[0]}")
    with open(target_file, "r", encoding="utf-8") as f:
        lines = f.readlines()[:10]
        for i, line in enumerate(lines):
            print(f"Line {i+1}: |{line.strip()}|")
else:
    print("파일이 없습니다.")
