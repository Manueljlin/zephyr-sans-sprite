import subprocess
import sys
from pathlib import Path

UFO = Path(__file__).parent / "ZephyrSansSprite.ufo"
OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)

fontmake = Path(sys.executable).parent / "fontmake"

subprocess.run([
    str(fontmake),
    "-u", str(UFO),
    "-o", "ttf", "otf",
    "--output-dir", str(OUT),
    "--no-production-names",
], check=True)
