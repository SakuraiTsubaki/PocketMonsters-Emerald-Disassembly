# Emerald MultiBoot BIOS stub

emerald-jp-rev0 is the Japanese origin reference. All 6 cataloged releases (Japanese, English, German, French, Italian, Spanish) verify the six-byte MultiBoot wrapper at +8 from LZ77UnCompVram. It fixes r1 to mode 1, invokes BIOS SWI 0x25, and returns the result in r0. Pinned libagbsyscall sources corroborate the symbol and calling convention. No ROM bytes are published.
