from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatTongyi(model="qwen3-max")

# 完整形式
# message = [
#     SystemMessage(content="你是一位诗人"),
#     HumanMessage(content="讲一个冷笑话")]

#简写形式
message = [
    ("system","你是一位诗人"),
    ("human","讲一个冷笑话"),
    ("assistant","12345,上山打老虎"),
    ("human","按照刚才的对话格式，讲一个冷笑话"),
]
response = model.stream(input=message)
for chunk in response:
    print(chunk.content, end="")