# 인공지능 시인 (AI Poetry Application)

## 프로젝트 개요

이 프로젝트는 LangChain과 OpenAI API를 활용하여 한국어 시를 자동으로 생성하는 Streamlit 기반 웹 애플리케이션입니다.

## 주요 기능

- 사용자가 입력한 주제에 대한 한국어 시 자동 생성
- OpenAI API 키를 사이드바에서 안전하게 입력 (password 타입)
- 실시간 시 생성 및 결과 표시
- 사용자 친화적인 에러 핸들링

## 기술 스택

- **Python**: 주요 프로그래밍 언어
- **Streamlit**: 웹 인터페이스 구현
- **LangChain**: LLM 체인 구성 및 관리
- **OpenAI API**: GPT-4o-mini 모델을 사용한 시 생성

## 파일 구조

```
project/
│
├── app.py              # 메인 애플리케이션 파일
└── requirements.txt    # 의존성 패키지 목록
```

## 설치 방법

### 1. 필요한 패키지 설치

```bash
pip install -r requirements.txt
```

### 2. 추가 필수 패키지

requirements.txt에 포함된 패키지:
- `python-dotenv==1.0.0`: 환경 변수 관리
- `openai>=1.0.0`: OpenAI API 클라이언트
- `langchain>=0.1.0`: LangChain 프레임워크

**주의**: `streamlit`과 `langchain_core`, `langchain_openai` 등도 필요하므로 추가 설치가 필요할 수 있습니다.

```bash
pip install streamlit langchain-openai langchain-core
```

## 사용 방법

### 1. 애플리케이션 실행

```bash
streamlit run app.py
```

### 2. 사용 절차

1. 웹 브라우저에서 애플리케이션이 자동으로 열립니다
2. **사이드바**에서 OpenAI API 키를 입력합니다 (sk-로 시작)
3. **메인 화면**에서 시의 주제를 입력합니다
4. **"시 작성 요청하기"** 버튼을 클릭합니다
5. 생성된 시를 확인합니다

## 코드 구조 설명

### app.py

#### 1. 라이브러리 임포트

```python
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
```

#### 2. 사이드바 - API 키 입력

- `st.sidebar`를 사용하여 설정 영역 구성
- `type="password"`로 API 키를 안전하게 입력받음
- API 키 입력 상태에 따른 피드백 제공

#### 3. 메인 화면 - 시 주제 입력

- `st.text_input()`으로 시의 주제 입력받기
- 버튼 클릭 시 시 생성 프로세스 시작

#### 4. 시 생성 프로세스

**유효성 검사**:
- API 키 입력 여부 확인
- 주제 입력 여부 확인

**LangChain 파이프라인 구성**:

```python
# 1. LLM 초기화
llm = init_chat_model("gpt-4o-mini", model_provider="openai")

# 2. 프롬프트 템플릿 생성
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that writes beautiful Korean poetry."),
    ("user", "{input}")
])

# 3. 체인 구성 (프롬프트 | LLM | 파서)
chain = prompt | llm | output_parser

# 4. 실행
result = chain.invoke({"input": f"{content}에 대한 아름다운 시를 써 줘"})
```

#### 5. 결과 표시

- 마크다운 형식으로 결과 출력
- 주제와 생성된 시를 구분하여 표시

#### 6. 에러 핸들링

- 일반적인 예외 처리
- API 관련 오류에 대한 특별 처리

## 주요 특징

### 1. 안전한 API 키 관리

- 패스워드 타입 입력 필드 사용
- 환경 변수를 통한 API 키 설정
- 키 노출 방지

### 2. 사용자 경험 (UX)

- 명확한 에러 메시지
- 로딩 스피너 (`st.spinner()`)
- 입력 상태에 따른 실시간 피드백

### 3. LangChain 활용

- `init_chat_model()`을 통한 모델 초기화
- 파이프 연산자 (`|`)를 사용한 직관적인 체인 구성
- `StrOutputParser()`를 통한 출력 파싱

## 개선 가능한 점

### 1. requirements.txt 보완

현재 requirements.txt에 누락된 패키지:
```
streamlit
langchain-openai
langchain-core
```

### 2. 환경 변수 파일 사용

`.env` 파일을 사용하여 API 키를 더 안전하게 관리:

```python
from dotenv import load_dotenv
load_dotenv()
```

### 3. 추가 기능 제안

- 시의 길이 조절 옵션
- 시의 스타일 선택 (현대시, 고전시 등)
- 생성된 시 저장 기능
- 히스토리 기능
- 다양한 LLM 모델 선택 옵션

### 4. 에러 처리 강화

- 네트워크 오류 처리
- API 요청 제한 처리
- 더 구체적인 에러 메시지

## OpenAI API 키 발급 방법

1. [OpenAI 웹사이트](https://platform.openai.com/) 접속
2. 계정 생성 또는 로그인
3. API Keys 섹션으로 이동
4. "Create new secret key" 클릭
5. 생성된 키를 안전하게 보관

**주의**: API 사용에는 비용이 발생할 수 있습니다.

## 라이선스 및 주의사항

- OpenAI API 사용 약관을 준수해야 합니다
- API 키는 절대 공개 저장소에 커밋하지 마세요
- `.gitignore`에 `.env` 파일을 추가하세요

## 문제 해결 (Troubleshooting)

### 1. API 키 오류

```
오류: API 키가 올바르지 않거나 권한이 없습니다
해결: API 키를 확인하고 OpenAI 계정에 크레딧이 있는지 확인하세요
```

### 2. 패키지 임포트 오류

```
오류: ModuleNotFoundError
해결: pip install -r requirements.txt 및 누락된 패키지 설치
```

### 3. Streamlit 실행 오류

```
오류: streamlit: command not found
해결: pip install streamlit
```

## 참고 자료

- [Streamlit 공식 문서](https://docs.streamlit.io/)
- [LangChain 공식 문서](https://python.langchain.com/)
- [OpenAI API 문서](https://platform.openai.com/docs/)

---

**작성일**: 2025년 11월 18일  
**버전**: 1.0  
**작성자**: AI Poetry Application Team
