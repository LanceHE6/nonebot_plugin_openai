## 介绍

一款基于API的openAI相关的nonebot插件



##  功能

ChatGPT对话(触发对话10分钟内 支持连续对话 3072token内)

实现内置人格功能

基于DalL.E的AI绘图



## 配置

使用前须在bot的.env配置文件中添加以下变量:

```
# ChatGPT相关
CHATGPT_API_KEY=""  # api key sk-xxxxxx
CHATGPT_ENABLE_PROXY=false  # 是否启用代理
CHATGPT_PROXY=""  # 代理地址 https://example.com
CHATGPT_TIMEOUT=600  # 定时清理用户会话 xx秒
CHATGPT_PERSONALITY=""  # 人格描述
```



## 指令

@bot ——与bot对话

/重置聊天——清除当前聊天token

/dall ——dall绘图