from functools import cache
import argparse
import os


@cache
def path_dir(project: str) -> str:
    root = os.path.dirname(__file__)
    return os.path.join(root, project)


@cache
def path_txt(project: str) -> str:
    d = path_dir(project)
    return os.path.join(d, f".txt")


@cache
def path_v(project: str, ext_v: str) -> str:
    d = path_dir(project)
    return os.path.join(d, f".{ext_v}")


@cache
def path_rv(project: str, ext_v: str) -> str:
    d = path_dir(project)
    return os.path.join(d, f".r.{ext_v}")


def process(project: str, ext_v: str, ext_seg: str, encode_twice: bool = False, ff_args: str = '') -> bool:
    ext_vid_l = ext_v.lower()
    ext_seg_l = ext_seg.lower()
    if ext_vid_l.endswith("mp4") and ext_seg_l.endswith("webm"):
        ext_seg = f"{ext_seg[:-4]}ts"
    elif ext_vid_l.lower().endswith("webm") and ext_seg_l.endswith("ts"):
        ext_seg = f"{ext_seg[:-2]}webm"

    d = path_dir(project)
    t = path_txt(project)
    v = path_v(project, ext_v)
    rv = path_rv(project, ext_v)

    if os.path.exists(rv):
        return True

    for (dur, e) in [
        ("69.0", encode_twice),
        ("69.0", not encode_twice),
        ("127.1", False),
    ]:
        os.system(' '.join([
            f'ffmpeg -an -i "{v}" -f segment -hls_segment_type fmp4 -loglevel warning',
            '-q 1 ' if e else '-vcodec copy ',
            f'-segment_time {dur} -map 0 "{d}/%d.{ext_seg}" -n',
        ]))
        f = open(t, "w")
        l = 0
        while os.path.exists(os.path.join(d, f"{l}.{ext_seg}")):
            l += 1

        for c in range(l, 0, -1):
            i = os.path.join(d, f"{c - 1}")
            f.write(f"file {repr(f'{i}.r.{ext_seg}')}\n")
            if os.path.exists(f"{i}.r.{ext_seg}"):
                continue
            os.system(
                f"ffmpeg -i {i}.{ext_seg} -vf reverse {ff_args} "
                + f"-q 7 -loglevel error -dn -an {i}.r.{ext_seg} -n",
            )

        f.close()
        success = True
        for c in range(l):
            p = os.path.join(d, f"{c}.r.{ext_seg}")
            if not os.path.exists(p) or os.path.getsize(p) < 666:
                print(f"Unable to reverse segment file at index {c}.")
                success = False
                break

        if success:
            os.system(
                f'ffmpeg -loglevel panic -safe 0 -f concat -i "%s" -vcodec copy "%s"' %
                (t, rv,)
            )
        # os.remove(t)

        for c in range(l):
            p = os.path.join(d, f"{c}.{ext_seg}")
            rp = os.path.join(d, f"{c}.r.{ext_seg}")
            if os.path.exists(p):
                os.remove(p)
            if os.path.exists(rp):
                os.remove(rp)

        if os.path.exists(rv):
            break
    return True


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("project", type=str)
    args.add_argument("ext_v", type=str, default="v.mp4", nargs="?")
    args.add_argument("ext_seg", type=str, default="t.ts", nargs="?")
    args.add_argument("ff_args", type=str, default="", nargs="?")
    args.add_argument("--encode_twice", action="store_true")
    process(**args.parse_args().__dict__)
