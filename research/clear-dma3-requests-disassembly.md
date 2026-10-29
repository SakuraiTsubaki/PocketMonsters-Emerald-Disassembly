# Emerald ClearDma3Requests disassembly

`bpe-j-rev0-retail` is the Japanese origin reference. All 6 cataloged releases (Japanese, English, German, French, Italian, Spanish) resolve the boot call immediately after InitMapMusic and preserve the same 42-byte routine: lock the manager, reset the cursor, clear size/source/destination in 128 sixteen-byte requests, then unlock. Maps retain addresses, structure and hashes without ROM bytes.
