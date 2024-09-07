import sys
from pathlib import Path

project_root: Path = Path(__file__).resolve().parent
src_dir: Path = project_root.parent / "src"
# `src`ディレクトリのパスを追加
sys.path.insert(0, str(src_dir))
