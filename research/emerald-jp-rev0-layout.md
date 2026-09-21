# Emerald Japanese revision 0 layout measurement

The 16 MiB Japanese origin candidate is measured as sixteen 1 MiB regions. Region 0 is only `header-and-entry`; region 10 (`0x00a00000–0x00afffff`) is uniform `0xff` padding; all other regions remain `unclassified`. Hashes, entropy, byte counts, pointer candidates, and ARM branch-word candidates are search evidence rather than semantic boundaries. No ROM bytes are stored and the release remains a `candidate`.
