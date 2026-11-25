.syntax unified
.thumb

.global AgbMain

.type AgbMain, %function
AgbMain:
    @ Structural reconstruction; per-release maps preserve conditional edges.
    bl RegisterRamReset
    bl InitGpuRegManager
    bl InitKeys
    bl InitIntrHandlers
    bl m4aSoundInit
    bl EnableVCountIntrAtLine150
    bl InitRFU
    bl RtcInit
    bl CheckForFlashMemory
    bl InitMainCallbacks
    bl InitMapMusic
    bl ClearDma3Requests
    bl ResetBgs
    bl SetDefaultFontsPointer
    bl InitHeap
    bl SetMainCallback2
    bl ReadKeys
    bl rfu_REQ_stopMode
    bl rfu_waitREQComplete
    bl DoSoftReset
    bl Overworld_SendKeysToLinkIsRunning
    bl UpdateLinkAndCallCallbacks
    bl UpdateLinkAndCallCallbacks
    bl Overworld_RecvKeysFromLinkIsRunning
    bl ClearSpriteCopyRequests
    bl UpdateLinkAndCallCallbacks
    bl PlayTimeCounter_Update
    bl MapMusicMain
    bl WaitForVBlank
.Lemerald_retail_loop:
    b .Lemerald_retail_loop
.size AgbMain, . - AgbMain
