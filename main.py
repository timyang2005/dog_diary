from astrbot.api.all import *

@register("dog_diary", "Your Name", "舔狗日记插件", "1.0.0")
class DogDiaryPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @command("舔狗日记")
    async def dog_diary(self, event: AstrMessageEvent):
        '''舔狗日记指令'''
        try:
            # 调用接口
            response = requests.get("https://api.oick.cn/api/dog")
            response.raise_for_status()  # 检查请求是否成功
            data = response.text

            # 发送结果
            yield event.plain_result(data)

        except Exception as e:
            yield event.plain_result(f"获取舔狗日记失败：{str(e)}")
