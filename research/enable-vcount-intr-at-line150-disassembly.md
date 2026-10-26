# Pokemon Emerald EnableVCountIntrAtLine150 disassembly

The Japanese release `bpe-j-rev0-retail` is the origin reference. Independent ROM scanning found exactly one matching 40-byte Thumb routine in every one of the 6 cataloged releases (Japanese, English, German, French, Italian, Spanish). Ruby and Sapphire were checked separately and do not contain this routine shape.

The assembly preserves the low DISPSTAT byte, installs VCount line 150 and its enable bit, then enables interrupt flag 0x0004. Per-release CFGs omit raw instruction halfwords; maps retain only locations, hashes, constants and call targets. Names are corroborated by `pret/pokeemerald` at `731ad5bfd6e6f265508d0efcca0ba42f9dcf5881`, `src/main.c`.
