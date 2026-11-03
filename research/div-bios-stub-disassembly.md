# Emerald Div BIOS stub

emerald-jp-rev0 is the Japanese origin reference. All 6 cataloged releases (Japanese, English, German, French, Italian, Spanish) verify the Div wrapper at -4 from LZ77UnCompVram. It invokes BIOS SWI 0x06 and exposes quotient, remainder, and absolute quotient results in r0, r1, and r3. Pinned libagbsyscall source corroborates the symbol and calling convention. No ROM bytes are published.
