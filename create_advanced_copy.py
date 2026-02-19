# -*- coding: utf-8 -*-
"""创建高级版副本的脚本"""
import os
import shutil
from pathlib import Path

SRC = Path(__file__).parent
DST = SRC.parent / "滚动字幕_高级版"
EXCLUDE = {'build', 'dist', '__pycache__', '.cursor', '.git', 'logs'}

def should_copy(rel_parts) -> bool:
    for part in rel_parts:
        if part in EXCLUDE:
            return False
    return True

def main():
    if DST.exists():
        shutil.rmtree(DST)
    DST.mkdir(parents=True, exist_ok=True)
    for root, dirs, files in os.walk(SRC):
        dirs[:] = [d for d in dirs if d not in EXCLUDE]
        root_path = Path(root)
        try:
            rel = root_path.relative_to(SRC)
        except ValueError:
            continue
        if not should_copy(rel.parts):
            continue
        dest_dir = DST / rel
        dest_dir.mkdir(parents=True, exist_ok=True)
        for f in files:
            if f == 'create_advanced_copy.py':
                continue
            src_file = root_path / f
            dst_file = dest_dir / f
            shutil.copy2(src_file, dst_file)
    print(f"已复制到: {DST}")

if __name__ == '__main__':
    main()
