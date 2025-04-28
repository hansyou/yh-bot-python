from .eventParse import groupEventParse


# 用户退群
def onGroupLeaveTest(event, openapi):
    print("有用户退出群")
    print(event)

    return 0
