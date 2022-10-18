import argparse
from functools import cache
import os
from subprocess import check_output


def process(path: str, start: float = 0):
    path = os.path.realpath(path)
    f = check_output(
        f'ffplay -ss {start} -i "{path}" -hide_banner 2>&1',
        shell=True,
    )
    b = f.rfind(b"\r", 0, -9)
    e = f.find(b" ", b + 3)
    return float(f[b:e])


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("path", type=str)
    args.add_argument("start", type=float, default=0, nargs="?")
    print(process(**args.parse_args().__dict__))
