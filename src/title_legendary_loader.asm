; Verified CB2_InitTitleScreen state-1 statement for every documented locale.
; Per-ROM instruction and literal offsets are recorded in analysis/*-title-rayquaza-load.json.

LoadTitleScreenRayquazaTiles::
    ldr r0, =TitleScreenRayquazaTiles
    ldr r1, =$06008000
    bl LZ77UnCompVram
