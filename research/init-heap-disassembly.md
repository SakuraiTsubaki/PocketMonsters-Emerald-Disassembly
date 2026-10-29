# Emerald InitHeap disassembly

`bpe-j-rev0-retail` is the Japanese origin reference. All 6 cataloged releases (Japanese, English, German, French, Italian, Spanish) preserve the 18-byte arena bootstrap that stores the heap start and size before calling PutFirstMemBlockHeader. The family-specific boot order uses 2 call(s) after ResetBgs. Maps retain addresses and hashes without ROM bytes.
