from flask import Flask, request
from yunhu.subscription import Subscription
from yunhu.openapi import Openapi
from utils import (
    BotFollowed,
    BotUnfollowed,
    GroupJoin,
    GroupLeave,
    ButtonReportInline,
    MessageInstruction,
    MessageNormal,
)

# 内网穿透一定要选用海外节点
app = Flask(__name__)
sub = Subscription()
openapi = Openapi("your api")


# api 调用
@app.route("/sub", methods=["POST", "GET"])
def subRoute():
    match request.method:
        case "POST":
            print("POST")
            sub.listen(request)
            return "success"
        # 网页端可测试服务器是否正常
        case "GET":
            return "连接通畅"
        case _:
            return "failed"


# 机器人根据内容回复消息
@sub.onMessageNormal
def onMessageNormalHander(event):
    # 这里写与用户交流的逻辑
    return MessageNormal.onMessageNormalTest(event=event, openapi=openapi)


# 接收到指令时触发
@sub.onMessageInstruction
def onMessageInstructionHandler(event):
    return MessageInstruction.onMessageInstructionTest(event=event, openapi=openapi)


# 进入群的时候，触发
@sub.onGroupJoin
def onGroupJoinHandler(event):
    return GroupJoin.onGroupJoinTest(event=event, openapi=openapi)


# 离开群的时候触发
@sub.onGroupLeave
def onGroupLeaveHandler(event):
    return GroupLeave.onGroupLeaveTest(event=event, openapi=openapi)


# 关注机器人触发
@sub.onBotFollowed
def onBotFollowedHandler(event):
    return BotFollowed.onBotFollowedTest(event=event, openapi=openapi)


# 取关机器人触发
@sub.onBotUnfollowed
def onBotUnfollowedHandler(event):
    return BotUnfollowed.onBotUnfollowedTest(event=event, openapi=openapi)


# 机器人设置消息事件
@sub.onButtonReportInline
def onButtonReportInlineHandler(event):
    return ButtonReportInline.onButtonReportInlineTest(event=event, openapi=openapi)


if __name__ == "__main__":
    app.run("0.0.0.0", 7888)
    # app.run("0.0.0.0", 8857)
