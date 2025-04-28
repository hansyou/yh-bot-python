from .eventParse import groupEventParse


# 用户入群
def onGroupJoinTest(event, openapi):
    print("新用户加入群")
    print(event)

    chatType, senderNickname, recvId, recvType = groupEventParse(event)

    res = openapi.sendMessage(
        recvId,
        recvType,
        "text",
        {"text": f"欢迎 {senderNickname} 入群"},
    )
    print(res.content)

    return 0
