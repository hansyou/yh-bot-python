# 由于不同的 POST 获取到的结构不同，因此要将不同类型分开
# 消息类型
def messageEventParse(event):
    # 初始化一些必要信息
    chatType = event["chat"]["chatType"]
    senderNickname = event["sender"]["senderNickname"]

    # 首先确定是群消息还是用户消息
    match chatType:
        # 用户：userID
        case "bot":
            recvId = event["sender"]["senderId"]
            recvType = "user"
        # 群：groupID
        case "group":
            recvId = event["chat"]["chatId"]
            recvType = "group"

    return chatType, senderNickname, recvId, recvType


# 关注机器人，与加入群聊的 event 结构类似
def followedEventParse(event):
    
    print(event)

    chatType = event["chatType"]
    recvId = event["userId"]
    recvType = "user" if chatType == "bot" else "group"
    senderNickname = event["nickname"]

    return chatType, senderNickname, recvId, recvType

# 加入群，指向 followedEventParse 函数
groupEventParse = followedEventParse