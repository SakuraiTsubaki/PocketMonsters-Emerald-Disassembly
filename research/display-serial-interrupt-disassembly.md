# Pokemon Emerald display and serial interrupt disassembly

`bpe-j-rev0-retail` is the Japanese origin reference. All 6 cataloged releases (Japanese, English, German, French, Italian, Spanish) contain exactly one HBlank, VCount and Serial handler matching the `emerald` profile. VCount invokes the optional callback and m4aSoundVSync. Each handler sets both INTR_CHECK and gMain.intrCheck. Per-release evidence preserves ranges, hashes, validated literals and call order without ROM bytes or instruction halfwords.
