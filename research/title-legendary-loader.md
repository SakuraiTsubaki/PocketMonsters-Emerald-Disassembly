# Title-screen Rayquaza loader provenance

The Japanese, English, German, French, Italian, and Spanish asset reports were traced back into their complete retail ROMs. In every release the Rayquaza LZ77 stream has exactly one stored GBA pointer and exactly one direct Thumb literal-load consumer. The following instruction sequence loads destination `0x06008000` and calls the release-local LZ77 VRAM routine.

This connects the existing compressed-range digest, decoded 4bpp digest, and PNG to its runtime use in state 1 of `CB2_InitTitleScreen`. Names and semantics are corroborated by `pret/pokeemerald` commit `fe1d8e51b265851676b65885818b1f5f62586135`, `src/title_screen.c`. Local ROM offsets and hashes remain authoritative, and no ROM instruction or asset bytes are published.
