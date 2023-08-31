from functools import cache
import argparse
import math
import os


@cache
def path_dir(project: str):
    root = os.path.dirname(__file__)
    return os.path.join(root, project)


@cache
def get_lang(project: str, lang: str = None):
    d = path_dir(project)
    if lang != None:
        return f".{lang}"
    # Find first usable subtitle track.
    for rf in os.listdir(d):
        if rf.endswith(".srt") and not rf.endswith(".r.srt"):
            return rf[:-4]


@cache
def path_read(project: str, lang: str = None):
    d = path_dir(project)
    l = get_lang(project, lang)
    return os.path.join(d, f"{l}.srt")


@cache
def path_write(project: str, lang: str = None):
    d = path_dir(project)
    l = get_lang(project, lang)
    return os.path.join(d, f"{l}.r.srt")


def get_time(v: str):
    if len(v) == 9:
        v = "00:" + v
    h = int(v[:-10])
    m = int(v[-9:-7])
    s = int(v[-6:-4])
    l = int(v[-3:])
    return 1e3 * (60 * (60 * h + m) + s) + l


def do_line(v: str, index, offset: int, mult: float = 1):
    t = v.split("\n")
    t[0] = str(index)
    a = []
    for v in t[1].split(" --> "):
        r = max(mult * (offset - get_time(v)), 0)
        H = math.floor(r / 3600000)
        M = math.floor(r / 60000 % 60)
        S = math.floor(r / 1000 % 60)
        L = math.floor(r % 1000)
        a.append(f"{H:02d}:{M:02d}:{S:02d},{L:03d}")

    a.reverse()
    t[1] = " --> ".join(a)
    return "\n".join(t)


def process(project: str, offset: float = 0, mult: float = 1, lang: str = None):
    rp = path_read(project, lang)
    wp = path_write(project, lang)
    if not os.path.exists(rp):
        return False
    rf = open(rp, "r", encoding="UTF-8")
    wf = open(wp, "w", encoding="UTF-8")
    t = rf.readlines()
    lt = [""]
    c = 1
    for l in t:
        if l.strip(" \t\ufeff\n") == str(c):
            c += 1
            lt[0] = lt[0].strip()
            lt.insert(0, "0\n")
            continue
        lt[0] += l

    lt.pop()
    msb = lt[0].index(" --> ")
    mse = lt[0].index("\n", msb)
    ms = get_time(lt[0][msb + 5: mse]) + offset * 1e3

    a = []
    for i, l in enumerate(lt, 1):
        a.append(f"{do_line(l, i, ms,mult)}\n\n")
    wf.writelines(a)
    rf.close()
    wf.close()
    return True


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("project", type=str)
    args.add_argument("offset", type=float, default=0, nargs="?")
    args.add_argument("mult", type=float, default=1, nargs="?")
    args.add_argument("lang", type=str, default=None, nargs="?")
    process(**args.parse_args().__dict__)
