from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import time
from dotenv import load_dotenv
load_dotenv()
import os


# ChatOpenAI model 초기화
llm = init_chat_model(model="gpt-4o-mini", model_provider="openai", api_key=os.getenv("OPENAI_API_KEY"))

# ChatPromptTemplate 초기화
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}")
])

# StrOutputParser 초기화
output_parser = StrOutputParser()

# LLM Chain 구성
chain = prompt | llm | output_parser

# 제목
st.title("인공지능 시인")

# 시 주제 입력 필드
content = st.text_input("시 주제를 입력해주세요")
st.write("시의 주제는 " + content)

# 시 작성 버튼
if st.button("시 작성 요청하기"):
    with st.spinner("시를 작성중입니다...", show_time=True):
        time.sleep(5)
        result = chain.invoke({"input": content + "에 대한 시를 써줘"})
        st.write(result)