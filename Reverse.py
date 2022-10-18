from functools import cache
import ReverseVideo
import ReverseAudio
import ReverseSync
import argparse
import os


def process(project: str, ext_v: str, ext_a: str, ext_av: str, ext_seg: str):
    ReverseAudio.process(project, ext_a)
    ReverseVideo.process(project, ext_v, ext_seg)
    ReverseSync.process(project, ext_v, ext_a, ext_av)
    os.remove(ReverseVideo.path_rv(project, ext_v))
    return True


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("project", type=str)
    args.add_argument("ext_v", type=str, default="v.mp4", nargs="?")
    args.add_argument("ext_a", type=str, default="a.mp3", nargs="?")
    args.add_argument("ext_av", type=str, default="av.mp4", nargs="?")
    args.add_argument("ext_seg", type=str, default="t.ts", nargs="?")
    process(**args.parse_args().__dict__)
