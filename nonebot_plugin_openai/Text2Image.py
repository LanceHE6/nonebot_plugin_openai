# -*- coding = utf-8 -*-
# @File:Text2Image.py
# @Author:Hycer_Lance
# @Time:2023/7/27 14:05
# @Software:PyCharm

from nonebot import on_command
from nonebot.params import Arg

from pathlib import Path
import os

from .DallE import AIDraw
from nonebot.adapters.onebot.v11 import GroupMessageEvent, MessageSegment

ai_draw_comm = on_command("chatgpt绘图", aliases={"chatgpt作画", "dall", "chatgpt作图"}, priority=2, block=True)


@ai_draw_comm.got("prompt", prompt="请发送作画描述")
async def _(event: GroupMessageEvent, prompt=Arg("prompt")):
    uid = event.get_user_id()
    ai_draw = AIDraw(prompt)
    await ai_draw_comm.send("开始作画，请稍等...")
    img_url = await ai_draw.get_image()
    if isinstance(img_url, Path):
        await ai_draw_comm.send(
            MessageSegment.at(uid) + MessageSegment.image(img_url))
        os.remove(img_url)
        await ai_draw_comm.finish()
    else:
        await ai_draw_comm.finish(MessageSegment.at(uid) + img_url)
