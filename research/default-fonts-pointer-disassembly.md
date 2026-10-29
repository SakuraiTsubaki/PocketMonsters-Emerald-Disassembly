# Emerald SetDefaultFontsPointer disassembly

`bpe-j-rev0-retail` is the Japanese origin reference. All 6 cataloged releases (Japanese, English, German, French, Italian, Spanish) preserve the 12-byte wrapper that loads `sFontInfos` and calls SetFontsPointer. Family-specific boot ordering around InitHeap is independently checked. Maps publish only addresses, structure and hashes, never ROM bytes or instruction halfwords.
