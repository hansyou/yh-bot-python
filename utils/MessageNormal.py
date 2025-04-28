from .eventParse import messageEventParse


# NormalMessage 测试用例
def onMessageNormalTest(event, openapi):
    print("根据内容回复消息")
    print(event)

    chatType, senderNickname, recvId, recvType = messageEventParse(event)

    res = openapi.sendMessage(
        recvId,
        recvType,
        "text",
        {"text": f"{recvType} 中给 {senderNickname} 的消息回复"},
    )
    print(res.content)

    content = {
        "text": "机器人批量回复普通消息",
        "buttons": [
            {
                "text": "复制内容 1",
                "actionType": 2,
                "value": "复制内容 1",
            },
            {
                "text": "复制内容 2",
                "actionType": 2,
                "value": "复制内容 2",
            },
        ],
    }

    res2 = openapi.batchSendMessage([recvId], recvType, "text", content)

    return 0
