.syntax unified
.thumb

InitMainCallbacks:
    push {lr}
    ldr r2, =gMain
    movs r0, #0
    str r0, [r2, #0x20]
    ldr r1, =gTrainerHillVBlankCounter
    str r0, [r1]
    str r0, [r2, #0x24]
    str r0, [r2]
    ldr r0, =CB2_InitCopyrightScreenAfterBootup
    bl SetMainCallback2
    ldr r1, =gSaveBlock2Ptr
    ldr r0, =gSaveblock2
    str r0, [r1]
    ldr r1, =gPokemonStoragePtr
    ldr r0, =gPokemonStorage
    str r0, [r1]
    pop {r0}
    bx r0

