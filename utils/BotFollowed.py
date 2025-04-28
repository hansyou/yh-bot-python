from .eventParse import followedEventParse


def onBotFollowedTest(event, openapi):
    print("用户关注机器人")
    print(event)

    chatType, senderNickname, recvId, recvType = followedEventParse(event)

    res = openapi.sendMessage(
        recvId,
        recvType,
        "text",
        {"text": f"感谢 {senderNickname} 关注"},
    )
    print(res.content)

    return 0
