# Emerald Japanese title-screen Rayquaza tiles

The Japanese revision-0 candidate (`BPEJ`, ROM SHA-256
`33f5610b9186b4add09fef68895deb00f552b997b3d133b5a961e5123506343c`)
contains a GBA BIOS-LZ77 stream at `0x519AB4`.

Decompression produces 8,192 bytes (256 GBA 4bpp tiles), SHA-256
`2d5bd462bb787ec8b28022fe3c2e98b28db7ed3bea69a59e1e46a3bd8f035667`.
An independent 8x8-tile-order conversion of `pret/pokeemerald`'s indexed
`graphics/title_screen/rayquaza.png` has exactly the same digest.

`graphics/title/rayquaza.png` is a deterministic 2x tile-sheet rendering
with the public `rayquaza_and_clouds.pal` palette. It is not a composed
screenshot. The manifest records ROM, compressed stream, decoded tiles,
reference source, palette, and output hashes without publishing ROM bytes.

The match verifies this asset correspondence only and does not change the
overall release candidate status.

## Whole-ROM discovery evidence

A bounded scan of the complete 16 MiB Japanese ROM found 70 valid BIOS-LZ77
streams with an 8,192-byte decoded length, representing 69 distinct decoded
hashes. The Rayquaza digest occurs exactly once, at the already established
`0x519AB4` source offset, and its compressed hash also matches the extraction
report. `analysis/emerald-jp-rev0-lz77-8192-scan.json` preserves the complete
offset/length/hash index without publishing compressed or decoded ROM bytes.
