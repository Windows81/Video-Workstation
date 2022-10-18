import argparse
from functools import cache
import SelectTime
import os


@cache
def path_dir(project: str):
    root = os.path.dirname(__file__)
    return os.path.join(root, project)


@cache
def path_t(project: str):
    d = path_dir(project)
    return os.path.join(d, f".concat")


@cache
def path_v(project: str, ext_v: str):
    d = path_dir(project)
    return os.path.join(d, f".{ext_v}")


def process(project: str, ext_v: str):
    t = path_t(project)
    v = path_v(project, ext_v)
    os.system(f"ffmpeg -f concat -safe 0 -i {t} -c copy {v} -stats -loglevel error -y")


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("project", type=str)
    args.add_argument("ext_v", type=str, default="v.mp4", nargs="?")
    process(**args.parse_args().__dict__)
