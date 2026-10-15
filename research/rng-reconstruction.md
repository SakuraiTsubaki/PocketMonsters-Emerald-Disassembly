# Emerald Random and SeedRng

All six catalogued Emerald languages were SHA-256 gated and searched independently. Each ROM contains exactly one extended RNG pair. `Random` has hash `7a127cd9fb3c422f84c3834409ec9e04057ef5680c16b22fb68dd9e9a9fee63e`; `SeedRng` has `a15ae683e626610da45d5a377c6d80212c0757411d25d272c3ebf48533b11c0a`.

Japanese uses `Random=$0806F050`, `gRngValue=$03005AE0`, `sRandCount=$02024664`, `sUnknown=$02024660`. Global releases relocate the pair near `$0806F5C8`/`$0806F5CC` and states to `$03005D80`, `$020249C0`, `$020249BC`. The base recurrence is unchanged, while `Random` increments the counter and `SeedRng` clears the auxiliary byte.

Naming is corroborated by `pret/pokeemerald@731ad5bfd6e6f265508d0efcca0ba42f9dcf5881`, `src/random.c`. Reports publish no ROM bytes.
