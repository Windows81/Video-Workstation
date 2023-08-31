from functools import cache
import ReverseSubtitle
import argparse
import os


@cache
def path_dir(project: str):
    root = os.path.dirname(__file__)
    return os.path.join(root, project)


@cache
def path_rav(project: str, ext_av: str):
    return os.path.join(path_dir(project), f".r.{ext_av}")


@cache
def path_rv(project: str, ext_v: str):
    return os.path.join(path_dir(project), f".r.{ext_v}")


@cache
def path_ra(project: str, ext_a: str):
    return os.path.join(path_dir(project), f".r.{ext_a}")


def process(project: str, ext_v: str, ext_a: str, ext_av: str, ff_args: str = ''):
    rv = path_rv(project, ext_v)
    ra = path_ra(project, ext_a)
    rav = path_rav(project, ext_av)
    if not os.path.exists(ra) or not os.path.exists(rv):
        return False

    while (o := input("Enter AV offset (q to finalise): ")) != "q":
        os.system(f'ffmpeg -i {rv} -itsoffset "{o}" -i {ra} -codec copy {rav} -y')
        os.system(f"vlc {rav}")

    rs = ReverseSubtitle.path_write(project)
    if ReverseSubtitle.process(project):
        while (o := input("Enter subtitle offset (q to finalise): ")) != "q":
            ReverseSubtitle.process(project, float(o))
            os.system(f"vlc {rav} --sub-file={rs}")
    return True


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("project", type=str)
    args.add_argument("ext_v", type=str, default="v.mp4", nargs="?")
    args.add_argument("ext_a", type=str, default="a.aac", nargs="?")
    args.add_argument("ext_av", type=str, default="av.mp4", nargs="?")
    process(**args.parse_args().__dict__)
