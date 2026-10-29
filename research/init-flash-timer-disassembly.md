# Emerald InitFlashTimer disassembly

`bpe-j-rev0-retail` is the Japanese origin reference. All 6 cataloged releases (Japanese, English, German, French, Italian, Spanish) independently trace the InitFlashTimer call and preserve the `slot-address` operand form for interrupt-table slot 7. The routine selects timer 2 and calls SetFlashTimerIntr. Per-release maps publish addresses, structure and hashes, never ROM bytes or halfwords.
