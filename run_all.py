from pathlib import Path
from subprocess import run, PIPE

IMAGES_LIB = Path.cwd() / "testing_images"
PROG_LOC = Path.cwd() / "src" / "main.py"
PY_PATH = Path.cwd() / ".venv" / "Scripts" / "python.exe"
OUT_FILE = Path.cwd() / "out.txt"

all_images = IMAGES_LIB.glob("**/*")

res = ""

for img in all_images:
    if img.is_dir(): continue
    output = run([str(PY_PATH), str(PROG_LOC), "-i", str(img)], stdout=PIPE)
    x = str(img.relative_to(Path.cwd()))
    x += output.stdout.decode() + ("-" * 50) + "\n"
    res += x
    print(x)

OUT_FILE.write_text(res)
