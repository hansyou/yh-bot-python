from .eventParse import followedEventParse


# 取消关注机器人
def onBotUnfollowedTest(event, openapi):
    print("用户取消关注机器人")
    print(event)
    return 0
