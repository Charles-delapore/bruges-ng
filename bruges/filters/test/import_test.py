"""Regression test: importing bruges must not require matplotlib."""

import subprocess
import sys
from pathlib import Path


def test_import_without_matplotlib():
    root = Path(__file__).resolve().parents[3]
    code = "import sys; sys.modules['matplotlib'] = None; import bruges"
    subprocess.run([sys.executable, "-c", code], cwd=root, check=True)
