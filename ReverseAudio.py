import argparse
from functools import cache
import os


@cache
def path_dir(project: str):
    root = os.path.dirname(__file__)
    return os.path.join(root, project)


@cache
def path_a(project: str, ext_a: str):
    d = path_dir(project)
    return os.path.join(d, f".{ext_a}")


@cache
def path_ra(project: str, ext_a: str):
    d = path_dir(project)
    return os.path.join(d, f".r.{ext_a}")


def process(project: str, ext_a: str):
    a = path_a(project, ext_a)
    ra = path_ra(project, ext_a)
    if not os.path.exists(a):
        return None
    os.system(f"ffmpeg -vn -i {a} -af areverse -loglevel panic {ra} -n")
    return ra


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("project", type=str)
    args.add_argument("ext_a", type=str, default="a.mp3", nargs="?")
    process(**args.parse_args().__dict__)
