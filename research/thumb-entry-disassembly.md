# Japanese Thumb entry reachable disassembly

Starting at the proven Thumb transition target `0x080003a4`, conservative control-flow traversal records 124 reachable halfwords, 14 direct CFG edges, and 29 BL call sites. BL targets are recorded without following callees, and unreachable gaps are represented by explicit `.org` directives in the source.

The source halfwords in ascending address order have canonical SHA-256 `5e8d14c7c584a1bc4dc445bf5afb5ec5c4c0d375da3fc7aa15d5c9ac47fe0dd2`. No return is reachable in this graph, so this is documented as a non-returning bootstrap path rather than a complete function boundary. Every emitted `.hword` is checked against its original little-endian ROM bytes.

