; Emerald independent secondary RNG stream.
SeedRng2::
    lsls r0, r0, 16
    lsrs r0, r0, 16
    ldr r1, =gRng2Value
    str r0, [r1]
    bx lr

Random2::
    ldr r2, =gRng2Value
    ldr r1, [r2]
    ldr r0, =1103515245
    muls r0, r1
    ldr r1, =24691
    adds r0, r0, r1
    str r0, [r2]
    lsrs r0, r0, 16
    bx lr
