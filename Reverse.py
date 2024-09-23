from functools import cache
import ReverseVideo
import ReverseAudio
import ReverseSync
import argparse
import os


def process(project: str, ext_v: str, ext_a: str, ext_av: str, ext_seg: str, encode_twice: bool, ff_args: str = ''):
    ReverseVideo.process(project, ext_v, ext_seg, ff_args=ff_args, encode_twice=encode_twice)
    ReverseAudio.process(project, ext_a, ff_args=ff_args)
    ReverseSync.process(project, ext_v, ext_a, ext_av, ff_args=ff_args)
    os.remove(ReverseVideo.path_rv(project, ext_v))


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("project", type=str)
    args.add_argument("ext_v", type=str, default="v.mp4", nargs="?")
    args.add_argument("ext_a", type=str, default="a.mp3", nargs="?")
    args.add_argument("ext_av", type=str, default="av.mp4", nargs="?")
    args.add_argument("ext_seg", type=str, default="t.ts", nargs="?")
    args.add_argument("ff_args", type=str, default="", nargs="?")
    args.add_argument("--encode_twice", action="store_true")
    process(**args.parse_args().__dict__)
