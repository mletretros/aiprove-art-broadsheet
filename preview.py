#!/usr/bin/env python3
"""Coarse ASCII proof of a rendered page, for layout QA without a vision model."""
import sys
from PIL import Image, ImageOps

RAMP = "@%#*+=-:. "


def preview(path, cols=76):
    im = Image.open(path).convert("L")
    w, h = im.size
    rows = max(1, int(cols * (h / w) * 0.46))
    im = im.resize((cols, rows), Image.LANCZOS)
    im = ImageOps.autocontrast(im)
    px = im.load()
    out = []
    for y in range(rows):
        line = ""
        for x in range(cols):
            v = px[x, y]
            line += RAMP[min(len(RAMP) - 1, v * len(RAMP) // 256)]
        out.append(line)
    return "\n".join(out)


if __name__ == "__main__":
    print(preview(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 76))
