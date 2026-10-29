.syntax unified
.thumb

SetDefaultFontsPointer:
    push {lr}
    ldr r0, =sFontInfos
    bl SetFontsPointer
    pop {r0}
    bx r0

