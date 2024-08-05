from langchain.chains import ConversationChain
from langchain_core.prompts import MessagesPlaceholder
from langchain_wenxin import ChatWenxin
from langchain.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory


def get_chat_response(prompt, memory):
    model = ChatWenxin(model="ernie-speed-128k", baidu_api_key="Idvexi7giPhjajeswlwjz7uC"
                       ,baidu_secret_key="XVpmwFYDs4rXFdjgAvv9Hz7ewyhNCNlP")
    prompt_template=ChatPromptTemplate.from_messages(
        [("system", f"你是一个非常暴躁的繁體中文智能助手。最重要的一點是無論如何只能使用繁體中文回覆。然後遇到數學問題時先乘除後加減，一步一步思考完成。在回覆訊息最後要加上憤怒的語氣和表情符號，並且訊息長度限制在100個字以內。"),
         MessagesPlaceholder(variable_name="history"),
         ("human", "{input}")
         ]
    )

    chain = ConversationChain(llm=model, memory=memory,prompt=prompt_template)

    response = chain.invoke({"input":prompt})
    return response["response"]

#memory = ConversationBufferMemory(return_messages=True)

#print(get_chat_response("牛顿提出过哪些知名的定律？", memory))
#print(get_chat_response("我上一个问题是什么？", memory))
