import sys
from pathlib import Path

import argparse


def touch_recursive(path: Path):
    if path.is_dir():
        for p in path.iterdir():
            touch_recursive(p)
    else:
        path.touch()


parser = argparse.ArgumentParser()
parser.add_argument('path', type=Path, help='Path to the directory to touch')
args = parser.parse_args()


if __name__ == '__main__':
    touch_recursive(args.path)
