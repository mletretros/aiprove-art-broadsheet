# AIProve — broadsheet poster

An entry for the `make-art-aiprove` bounty: give AIProve a face, in the
"broadsheet meets terminal" register the brief asks for.

Everything on the page is drawn by `poster.py` using Pillow primitives —
no stock art, no image model, no borrowed plate. The guilloche bands, the
seal rings, the gear teeth, the paper grain, the vignette and the phosphor
terminal are all computed from math in that one file.

## Output

| file | what it is |
|---|---|
| `out/poster.png` | 2000×2800 poster, the main entry |
| `out/mark.png` | 1600×1600 square mark (the bay window version) |

## Reproduce

```bash
pip install pillow          # only dependency
python3 poster.py           # writes out/poster.png + out/mark.png (~5s)
python3 preview.py out/poster.png 90   # coarse ASCII proof, layout QA
```

## Concept

- **Masthead** — the wordmark set in DejaVu Serif Bold with hand tracking,
  over a double rule and a pair of parametric guilloche bands, the way a
  Victorian financial page opens.
- **Terminal** — the only glowing element on the page. A real bounty board
  listing is rendered in monospace phosphor green, with a scanline overlay
  and a blurred glow pass. It is the product, so it sits in the optical
  centre.
- **Body** — two justified serif columns that state the offer plainly:
  free to enter, judged in the open, paid in stock.
- **Seal** — three modulated rings, 64 gear teeth, a stamped checkmark and
  circular set type ("VERIFIED IN THE OPEN" / "SETTLED IN STOCK"). This is
  the mascot: proof itself, struck as a medal.
- **Paper** — noise-based grain, faint foxing stains, soft vignette, so the
  plate reads as print rather than as a screenshot.

## Layout rules the generator enforces

- Border is drawn first, all content is measured against the inner margin.
- The copy block reports its own bottom edge; the seal is placed below it
  and the script asserts the seal cannot collide with the footer.
- Body columns wrap by measured text length, not by character count.

## Licence

CC0 — do what you like with it.
