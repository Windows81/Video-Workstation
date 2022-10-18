import argparse
import os
from subprocess import check_output


def process(path: str, min_score: float = 11):
    path = os.path.realpath(path)
    o = check_output(
        f'ffmpeg -i "{path}" -vf scdet={min_score}:1,'
        + "metadata=mode=print:key=lavfi.scd.score:"
        + "file=- -f null -loglevel 0 -"
    )
    return [
        {"pts": float(pts[pts.find("pts_time") + 9 :]), "score": float(scr[17:])}
        for pts, scr in zip(o[0::2], o[1::2])
    ]


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("path", type=str)
    args.add_argument("min_score", type=float, default=11, nargs="?")
    print(process(**args.parse_args().__dict__))
