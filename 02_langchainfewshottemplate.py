from langchain_core.prompts import FewShotPromptTemplate,PromptTemplate
from langchain_community.llms import Tongyi
from dotenv import load_dotenv
load_dotenv()
example_prompt = PromptTemplate.from_template("单词：{word},反义词：{antonym}")

example_data = [
    {"word":"中国", "antonym":"外国"},
    {"word":"大","antonym":"小"}
]
# FewshotPromptTemplate(
#     example_prompt=None, #示例数据的模板
#     examples = None,#示例的数据（用来注入动态数组的），list内嵌字典
#     prefix=None,#示例之前的描述
#     suffix=None,#示例之后的描述
#     input_variables=[],#输入变量
# )
few_shot_template = FewShotPromptTemplate(
    example_prompt=example_prompt,#示例数据的模板
    examples = example_data,#示例的数据（用来注入动态数组的），list内嵌字典
    prefix="输入一个单词，输出它的反义词。示例如下：",
    suffix="基于前面的示例告诉我，{input_word}的反义词是？",
    input_variables=["input_word"]#输入变量,
)
model = Tongyi(model="qwen-max")
prompt_text = few_shot_template.format(input_word=input("请输入一个单词："))
print(model.invoke(prompt_text))