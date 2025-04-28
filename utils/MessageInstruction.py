from .eventParse import messageEventParse


# NormalInstruction 测试用例
def onMessageInstructionTest(event, openapi):
    print("根据指令回复消息")
    print(event)

    chatType, senderNickname, recvId, recvType = messageEventParse(event)

    # 根据指令回复
    commandID = event["message"]["commandId"]
    match commandID:
        # 根据指令触发回复
        case 1359:
            res = openapi.sendMessage(
                recvId,
                recvType,
                "text",
                {"text": f"指令 {commandID} 触发的 {recvType} 消息回复"},
            )

    return 0
