    .syntax unified
    .thumb

SetTrainerId:
    strb r0, [r1]
    lsrs r2, r0, #8
    strb r2, [r1, #1]
    lsrs r2, r0, #16
    strb r2, [r1, #2]
    lsrs r0, r0, #24
    strb r0, [r1, #3]
    bx lr

GetTrainerId:
    adds r2, r0, #0
    ldrb r0, [r2, #3]
    lsls r0, r0, #24
    ldrb r1, [r2, #2]
    lsls r1, r1, #16
    orrs r0, r1
    ldrb r1, [r2, #1]
    lsls r1, r1, #8
    orrs r0, r1
    ldrb r1, [r2]
    orrs r0, r1
    bx lr

CopyTrainerId:
    push {r4, lr}
    adds r4, r0, #0
    adds r3, r1, #0
    movs r2, #0
.copy_loop:
    adds r0, r4, r2
    adds r1, r3, r2
    ldrb r1, [r1]
    strb r1, [r0]
    adds r2, #1
    cmp r2, #3
    ble .copy_loop
    pop {r4}
    pop {r0}
    bx r0
