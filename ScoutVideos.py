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


def process(project: str):
    d = path_dir(project)
    t = path_t(project)
    if not os.path.exists(d):
        os.mkdir(d)

    with open(t, "w") as f:
        while True:
            v = input("Video Path: ")
            if v == "q":
                break
            elif v != "":
                r2 = 0
                p = os.path.realpath(v)
            print("Input Time: ", end="")
            r1 = SelectTime.process(p, r2)
            print(r1)
            print("Output Time: ", end="")
            r2 = SelectTime.process(p, r1)
            print(r2)
            f.writelines(
                [
                    f"file {repr(p)}",
                    f"inpoint {r1}",
                    f"outpoint {r2}",
                ]
            )


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("project", type=str)
    process(**args.parse_args().__dict__)
