.syntax unified
.thumb

InitFlashTimer:
    push {lr}
    ldr r1, =gIntrTable + 7 * 4
    movs r0, #2
    bl SetFlashTimerIntr
    pop {r0}
    bx r0

