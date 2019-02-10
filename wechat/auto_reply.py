#在这里新建你的自动回复规则 word为关键词 probability为回复内容出现概率 partial为部分匹配 whole为完全匹配 区分大小写
reply_data = {
    "subscribe": {
        "content": "欢迎使用XPuzzle后台系统！这是一个为了文字解谜游戏搭建的公众号后台，正在建设当中~"
    },
    "keyword": [
        {
            "word": "XP",
            "type": "partial",
            "content": [
                {
                    "probability": 0.8,
                    "text": "XP说这句话出现的概率是0.8"
                },
                {
                    "probability": 0.2,
                    "text": "XP说这句话出现的概率是0.2"
                }
            ]
        },{
            "word": "17",
            "type": "whole",
            "content": [
                {
                    "probability": 1,
                    "text": "小十七天下第一可爱！"
                }
            ]
        }
    ]
}
