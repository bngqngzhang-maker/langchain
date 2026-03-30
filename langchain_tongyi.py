# langchain_tongyi.py
from dotenv import load_dotenv
from langchain_community.llms import Tongyi

load_dotenv()  # 👈 关键！加载 .env 文件

model = Tongyi(model="qwen-max")
question = input("""请输入问题：""")

# response = model.invoke(question)#一次性返回所有结果
# print(response)
response = model.stream(question)#逐行返回结果
for chunk in response:
    print(chunk,end="",flush=True)#flush=True 保证输出
