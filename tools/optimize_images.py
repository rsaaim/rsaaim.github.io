"""Make a compressed .webp copy of every raster image the built pages reference.
Originals stay untouched; build.py swaps references to the .webp when it exists."""
import os, re, sys
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX_EDGE, QUALITY = 1800, 76

def referenced():
    out = set()
    for d, _, fs in os.walk(ROOT):
        if "/tools" in d or "/.git" in d:
            continue
        for f in fs:
            if f.endswith(".html"):
                for m in re.findall(r'(?:\.\./)?(assets/img/[^"\'\s)]+\.(?:jpe?g|png))', open(os.path.join(d, f)).read(), re.I):
                    out.add(m)
    return sorted(out)

def main():
    before = after = 0
    for rel in referenced():
        src = os.path.join(ROOT, rel)
        if not os.path.exists(src):
            continue
        dst = os.path.splitext(src)[0] + ".webp"
        im = ImageOps.exif_transpose(Image.open(src))
        if im.mode not in ("RGB", "RGBA"):
            im = im.convert("RGBA" if "transparency" in im.info or im.mode in ("LA", "P") else "RGB")
        im.thumbnail((MAX_EDGE, MAX_EDGE), Image.LANCZOS)
        lossless = rel.lower().endswith(".png") and min(im.size) < 400  # logos / small graphics
        im.save(dst, "WEBP", quality=QUALITY, method=6, lossless=lossless)
        if os.path.getsize(dst) > 0.9 * os.path.getsize(src):
            os.remove(dst)  # not worth it; keep serving the original
            before += os.path.getsize(src); after += os.path.getsize(src)
            continue
        before += os.path.getsize(src); after += os.path.getsize(dst)
    print(f"{before/1e6:.1f} MB -> {after/1e6:.1f} MB")

if __name__ == "__main__":
    main()
