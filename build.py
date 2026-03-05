import subprocess
from pathlib import Path

UFO = Path(__file__).parent / "ZephyrSansSprite.ufo"
OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)

subprocess.run([
    "fontmake",
    "-u", str(UFO),
    "-o", "ttf", "otf",
    "--output-dir", str(OUT),
    "--no-production-names",
], check=True)
