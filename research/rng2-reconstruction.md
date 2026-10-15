# Emerald SeedRng2 and Random2

All six catalogued official languages were SHA-256 gated and independently scanned for the structurally adjacent secondary RNG pair. `Random2` follows `SeedRng2` and its literal pool, and both refer to the same `gRng2Value`; this relationship distinguishes the pair from unrelated short compiler patterns.

Japanese uses `SeedRng2=$0806f094`, `Random2=$0806f0a4`, and `gRng2Value=$03005ae4`. English, German, and Italian use `$0806f610`/`$0806f620`; French and Spanish use `$0806f60c`/`$0806f61c`. All international builds use state `$03005d84`. Every build applies `state = 1103515245 * state + 24691`, returns bits 31..16, and keeps this state independent from primary `Random`.

Naming and semantics are corroborated by `pret/pokeemerald@731ad5bfd6e6f265508d0efcca0ba42f9dcf5881`, `src/random.c`. Reports retain addresses, code hashes, constants, and state without ROM bytes.
