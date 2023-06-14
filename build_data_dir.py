from pathlib import Path
import zipfile

CUR_DIR = Path.cwd()
OUT_DIR = CUR_DIR / "data"
ZIP_FILES = CUR_DIR.glob("*.zip")

OUT_DIR.mkdir(exist_ok=True)

for source in ZIP_FILES:
    ext_path = OUT_DIR / source.name.split(".")[0]
    ext_path.mkdir(exist_ok=True)

    with zipfile.ZipFile(source, "r") as ref:
        ref.extractall(ext_path)

    for unrelated in ext_path.glob("*.svg"):
        unrelated.unlink()
