# -*- coding = utf-8 -*-
# @File:OpenAI.py
# @Author:Hycer_Lance
# @Time:2023/7/27 13:52
# @Software:PyCharm

from nonebot import on_message, on_command
from nonebot.rule import *
from nonebot.adapters.onebot.v11 import GroupMessageEvent, MessageSegment

from .SessionManager import Session, SessionManager

chat = on_message(rule=to_me(), priority=2, block=True)
rm_session = on_command("rm_session", aliases={"清除会话记录", "清除聊天记录", "重置聊天", "重置聊天记录"}, priority=2,
                        block=True)

session_manager = SessionManager()


@chat.handle()
async def reply(event: GroupMessageEvent):
    uid = event.get_user_id()
    # 判断当前用户会话是否存在
    if not await session_manager.is_session_exist(uid):
        # 不存在则添加进会话管理中
        await session_manager.add_session(uid, Session())
        session = await session_manager.get_session(uid)
    else:
        session = await session_manager.get_session(uid)

    user_content = str(event.get_message())
    await session.add_user_content(user_content)
    response = await session.get_response()
    await chat.finish(GroupAndGuildMessageSegment.at(event) + response)


@rm_session.handle()
async def _(event: GroupMessageEvent):
    uid = event.get_user_id()
    if not await session_manager.is_session_exist(uid):
        await rm_session.finish("你还没有和我聊过天哦")
    await session_manager.remove_session(uid)
    await rm_session.finish(MessageSegment.at(uid) + "聊天已重置")
