from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Tongyi
from dotenv import load_dotenv
load_dotenv()
prompt_template = PromptTemplate.from_template(
    "简单回答我的问题，尽量20get字以内: {question}"
)
# prompt_text = prompt_template.format(question="如何使用 LangChain？")
# model = Tongyi(model="qwen-max")

# res = model.invoke(prompt_text)
# print(res)

model = Tongyi(model="qwen-max")
chain = prompt_template | model

res = chain.invoke({"question": "如何使用 LangChain？"})
print(res)