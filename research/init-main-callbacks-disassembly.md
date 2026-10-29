# Emerald InitMainCallbacks disassembly

`bpe-j-rev0-retail` is the Japanese origin reference. All 6 cataloged releases (Japanese, English, German, French, Italian, Spanish) independently resolve the direct boot call immediately after CheckForFlashMemory and preserve the family-specific `emerald-storage` structure. The routine clears callback state, installs the copyright-screen callback through SetMainCallback2, and performs the profile-specific pointer initialization. Maps publish structure and hashes, never ROM bytes or halfwords.
