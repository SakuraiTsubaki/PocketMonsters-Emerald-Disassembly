# Name Tables

This directory contains the fixed-width Pokémon species-name and move-name tables recovered directly from the verified Emerald reference ROMs.

Each source file is UTF-8 text in the form:

```text
NNN<TAB>decoded name
```

The numeric index is the original internal ROM table index and is intentionally preserved.

## Table geometry

| Release family | Species records | Species width | Move records | Move width |
| --- | ---: | ---: | ---: | ---: |
| JPN | 412 | 6 bytes | 355 | 8 bytes |
| ENG/FRA/DEU/ITA/ESP | 412 | 11 bytes | 355 | 13 bytes |

The western widths correspond to `POKEMON_NAME_LENGTH + 1` and `MOVE_NAME_LENGTH + 1`; the final byte is the string terminator. The Japanese build uses shorter fixed-width records, which is also reflected by the language-dependent name-length values in its Game Freak ROM metadata header.

## Internal species numbering

- index `0` is the null/unknown entry
- indices `1-251` are Generation I-II species
- indices `252-276` are the unused old-Unown placeholder slots and decode as `?`
- index `277` resumes with Treecko / キモリ
- index `411` is Chimecho / チリーン

These are internal Generation III species IDs, not National Pokédex numbers.

## Verification

`tools/extract_name_tables.py` regenerates the committed files from local reference ROMs only after checking each ROM SHA-1 against `manifests/roms.json`.

Across the six unique release payloads:

- 6 × 412 = 2,472 species-name records decoded
- 6 × 355 = 2,130 move-name records decoded
- 4,602 total records decoded
- undefined character codes: 0
- records missing the expected EOS terminator: 0

`summary.csv` records each release's ROM root, record count, record width and validation totals.

The two supplied English ROM files are byte-identical; `ENG_USA_EUR` is the canonical committed English table and `ENG_U` is its alias.
