from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os

st.title("인공지능 시인")

# 사이드바에서 API 키 입력
with st.sidebar:
    st.header("설정")
    api_key = st.text_input("OpenAI API Key를 입력하세요:", type="password", help="sk-로 시작하는 OpenAI API 키를 입력하세요.")
    
    if api_key:
        st.success("API 키가 입력되었습니다.")
    else:
        st.warning("API 키를 입력해주세요.")

# 메인 화면
content = st.text_input("시의 주제를 입력하세요.")

if st.button("시 작성 요청하기"):
    if not api_key:
        st.error("먼저 사이드바에서 OpenAI API 키를 입력해주세요.")
    elif not content:
        st.error("시의 주제를 입력해주세요.")
    else:
        try:
            # 환경 변수에 API 키 설정
            os.environ['OPENAI_API_KEY'] = api_key
            
            with st.spinner("시를 작성하는 중입니다..."):
                # ChatOpenAI 초기화 (API 키가 환경변수에서 자동으로 읽힘)
                llm = init_chat_model("gpt-4o-mini", model_provider="openai")
                
                # 프롬프트 템플릿 생성
                prompt = ChatPromptTemplate.from_messages([
                    ("system", "You are a helpful assistant that writes beautiful Korean poetry."),
                    ("user", "{input}")
                ])
                
                # 체인 생성
                output_parser = StrOutputParser()
                chain = prompt | llm | output_parser
                
                # 시 생성 요청
                result = chain.invoke({"input": f"{content}에 대한 아름다운 시를 써 줘"})
                
                # 결과 출력
                st.markdown("### 생성된 시")
                st.markdown(f"**주제: {content}**")
                st.markdown("---")
                st.write(result)
                
        except Exception as e:
            st.error(f"오류가 발생했습니다: {str(e)}")
            if "api" in str(e).lower() or "key" in str(e).lower():
                st.error("API 키가 올바르지 않거나 권한이 없습니다. API 키를 확인해주세요.")