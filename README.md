# PocketMonsters-Emerald-Disassembly

Disassembly and reconstruction project for Pokémon Emerald, preserving regional and language variants as reproducible source, data, graphics, text, audio, maps, and scripts. ROM binaries are not included.

## Goal

Reconstruct each supported Pokémon Emerald release from repository source and extracted/recovered assets, without requiring a committed or bundled base ROM. Local reference ROMs may be used during reverse-engineering and verification, but they are never committed.

Target workflow:

```text
repository source + assets + tools
              ↓
             build
              ↓
        reconstructed ROM
              ↓
byte/hash verification against reference ROM
```

## Reference set

The current reference set covers Japanese, English, French, German, Italian, and Spanish releases. Exact hashes and GBA header metadata are recorded in `manifests/roms.json`.

The two currently supplied English files, `(U)` and `(USA, Europe)`, are byte-identical and share the same hashes.

## Repository policy

- ROM binaries are never committed.
- Disassembly/decompilation source, scripts, documentation, manifests, extracted/recovered graphics, text, audio, maps, data, and verification outputs are repository material.
- Human-readable/editable source forms are preferred over opaque binary blobs whenever practical.
- Sprite and graphics work should include viewable image assets such as PNG files alongside conversion metadata.
- Every reconstructed target must eventually be verified byte-for-byte or by exact cryptographic hash against its reference ROM.

## Planned layout

```text
asm/          low-level assembly and unresolved code/data
src/          reconstructed C source where applicable
include/      headers and declarations
constants/    symbolic IDs and constants
data/         structured game data
graphics/     sprites, tiles, palettes, UI and other graphics
text/         game text and text metadata
sound/        music, SFX, cries, samples and sound tables
maps/         maps, layouts, events and map scripts
tools/        extraction, conversion, build and verification tools
manifests/    reference ROM metadata and reconstruction manifests
docs/         reverse-engineering notes and project documentation
tests/        regression and reproducibility tests
build/        generated output (ignored by Git)
```

## Status

Bootstrap phase. Reference ROM identities have been recorded and the reconstruction policy/tooling skeleton is being established before bank/region-by-region extraction begins.
