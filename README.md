# 🤖 Agent Bible - AI Agent 실습 환경

패스트캠퍼스 **Agent 초격차** 강의를 위한 실습 환경입니다.

## 📋 목차

- [사전 요구사항](#사전-요구사항)
- [설치 방법](#설치-방법)
- [실습 노트북](#실습-노트북)
- [프로젝트 구조](#프로젝트-구조)
- [문제 해결](#문제-해결)

---

## 🔧 사전 요구사항

- **Python 3.10 이상**
- **OpenAI API 키** ([OpenAI Platform](https://platform.openai.com/)에서 발급)
- (선택) LangSmith API 키 - 추적 및 모니터링용

---

## 🚀 설치 방법

### 1. 저장소 클론

```bash
git clone https://github.com/HarryKane11/FC_Agent_bible.git
cd FC_Agent_bible
```

### 2. 패키지 설치 (두 가지 방법 중 선택)

#### 방법 A: ⚡ uv 사용 (권장 - 10배 이상 빠름!)

[uv](https://github.com/astral-sh/uv)는 Rust로 작성된 초고속 Python 패키지 매니저입니다.

**1) uv 설치:**
```bash
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Mac/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**2) 가상환경 생성 + 패키지 설치 (한 줄로 끝!):**
```bash
uv sync
```

**3) 가상환경 활성화:**
```bash
# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

---

#### 방법 B: 기존 pip 사용

**1) 가상환경 생성 및 활성화:**

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

**2) 패키지 설치:**
```bash
pip install -r requirements.txt
```

### 4. 환경 변수 설정

```bash
# .env.example을 .env로 복사
cp .env.example .env  # Mac/Linux
copy .env.example .env  # Windows
```

`.env` 파일을 열고 API 키를 입력하세요:

```env
OPENAI_API_KEY=sk-your-actual-api-key-here
```

### 5. Jupyter Notebook 실행

```bash
jupyter notebook
```

---

## 📚 실습 노트북

### Part 1. AI 에이전트 기초 다지기
| 위치 | 노트북 | 설명 |
|------|--------|------|
| CH03 | `CH03.02.01.Langchain으로 구현하는 Basic RAG.ipynb` | LangChain을 활용한 RAG 구현 실습 |
| CH03 | `CH03.02.02.Langgraph로 구현하는 Basic RAG.ipynb` | LangGraph를 활용한 RAG 워크플로우 실습 (Agentic RAG 포함) |

### Part 2. AI 에이전트 초간단 구현해보기
| 위치 | 노트북 | 설명 |
|------|--------|------|
| CH02 | (노코드 기반의 프레임워크, n8n) | n8n 워크플로우 실습 자료 |
| CH03 | `CH03._02.. AI 에이전트 프레임워크 Medium 버전 - OpenAI Agent SDK로 RAG 챗봇 만들어보기.ipynb` | OpenAI Agent SDK로 RAG 챗봇 구현 |
| CH04 | `CH04._02.. AI 에이전트 프레임워크 Hard 버전 - Langgraph로 웹 검색 에이전트 구현 copy.ipynb` | LangGraph로 웹 검색 에이전트 구현 |
| CH04 | `CH04._03.. AI 에이전트 프레임워크 Hard 버전 - Langgraph로 보고서 작성 에이전트 구현_test.ipynb` | LangGraph로 보고서 작성 에이전트 구현 |

### Part 3. 멀티 에이전트 구조 정복하기
| 위치 | 노트북 | 설명 |
|------|--------|------|
| CH04 | `CH02._01._ReACT 기반의 Single Agent 구현하기.ipynb` | ReACT 패턴으로 Single Agent 구현 |
| CH04 | `CH02._02._Prompt Chaining으로 더 똑똑한 답변 받기.ipynb` | Prompt Chaining 워크플로우 |
| CH04 | `CH02._03._MoA(Mixture of Agents)로 AI 답변 종합하기.ipynb` | Mixture of Agents 패턴 구현 |
| CH04 | `CH02._04._CodeAct 에이전트로 복잡한 문제 해결하기.ipynb` | CodeAct 에이전트 구현 |
| CH04 | `CH02._05._Orchestrator-Worker으로 AI 팀 만들어보기.ipynb` | Orchestrator-Worker 패턴 |
| CH04 | `CH02._06._Evaluator-optimizer으로 자율 개선 만들기.ipynb` | Evaluator-Optimizer 자율 개선 |
| CH04 | `CH02._07._Routing으로 AI 시스템 효율 끌어올리기.ipynb` | Routing 기반 효율화 |
| CH05 | `CH03._02._DeepResearch 에이전트 구현하기.ipynb` | DeepResearch 에이전트 구현 |
| CH05 | `CH03._04._DeepAgent의 To-do list 구현하기.ipynb` | DeepAgent To-do list 기능 |
| CH05 | `CH03._05._DeepAgent의 File Management 구현하기.ipynb` | DeepAgent 파일 관리 기능 |
| CH05 | `CH03._06._DeepAgent의 Sub-Agent 위임 구현하기.ipynb` | Sub-Agent 위임 구현 |
| CH05 | `CH03._07._DeepAgent 완전체 구현하기.ipynb` | DeepAgent 완전체 구현 |

### 부록. LangChain 및 LangGraph 1.0 기초
| 노트북 | 설명 |
|--------|------|
| `부록_01._LangChain과 LangGraph 소개.ipynb` | LangChain과 LangGraph 개요 |
| `부록_02._init_chat_model로 모델 초기화하기.ipynb` | `init_chat_model` 사용법 |
| `부록_03._Tool 데코레이터와 ToolRuntime.ipynb` | Tool 데코레이터 및 ToolRuntime |
| `부록_04._create_agent로 간단한 에이전트 만들기.ipynb` | `create_agent`로 에이전트 생성 |
| `부록_05._StateGraph API로 커스텀 그래프 구축하기.ipynb` | StateGraph API 활용 |
| `부록_06._Middleware로 에이전트 실행 제어하기.ipynb` | Middleware로 실행 제어 |
| `부록_07._Memory와 State 관리.ipynb` | Memory 및 State 관리 |
| `부록_08._Structured Output으로 정형 데이터 받기.ipynb` | Structured Output 활용 |
| `부록_09._Streaming으로 실시간 응답 처리하기.ipynb` | Streaming 응답 처리 |
| `부록_10._LangSmith로 Tracing과 디버깅.ipynb` | LangSmith Tracing/디버깅 |

---

## 📁 프로젝트 구조

```
FC_Agent_bible/
├── Part 1. AI 에이전트 기초 다지기/
│   └── CH03.LLM 어플리케이션의 기본, RAG/
│       ├── docs/
│       │   └── DeepSeek_OCR_paper.pdf
│       ├── CH03.02.01.Langchain으로 구현하는 Basic RAG.ipynb
│       └── CH03.02.02.Langgraph로 구현하는 Basic RAG.ipynb
├── Part 2. AI 에이전트 초간단 구현해보기/
│   ├── docs/
│   │   └── DeepSeek_OCR_paper.pdf
│   ├── CH02.노코드 기반의 프레임워크, n8n/
│   ├── CH03.에이전트 PoC 최적의 프레임워크, OpenAI Agent SDK/
│   │   └── CH03._02.. AI 에이전트 프레임워크 Medium 버전 - OpenAI Agent SDK로 RAG 챗봇 만들어보기.ipynb
│   └── CH04.프로덕션 수준의 프레임워크, Langgraph/
│       ├── CH04._02.. AI 에이전트 프레임워크 Hard 버전 - Langgraph로 웹 검색 에이전트 구현 copy.ipynb
│       └── CH04._03.. AI 에이전트 프레임워크 Hard 버전 - Langgraph로 보고서 작성 에이전트 구현_test.ipynb
├── Part 3. 멀티 에이전트 구조 정복하기/
│   ├── CH04.Langgraph 기본 워크플로우 구현/
│   │   ├── data/
│   │   │   └── netflix_titles.csv
│   │   ├── vis_result/
│   │   │   └── netflix_chart.png
│   │   ├── CH02._01._ReACT 기반의 Single Agent 구현하기.ipynb
│   │   ├── CH02._02._Prompt Chaining으로 더 똑똑한 답변 받기.ipynb
│   │   ├── CH02._03._MoA(Mixture of Agents)로 AI 답변 종합하기.ipynb
│   │   ├── CH02._04._CodeAct 에이전트로 복잡한 문제 해결하기.ipynb
│   │   ├── CH02._05._Orchestrator-Worker으로 AI 팀 만들어보기.ipynb
│   │   ├── CH02._06._Evaluator-optimizer으로 자율 개선 만들기.ipynb
│   │   └── CH02._07._Routing으로 AI 시스템 효율 끌어올리기.ipynb
│   ├── CH05.Langgraph 통한 실제 AI 에이전트 서비스 따라하기/
│   │   ├── assets/
│   │   ├── deepresearch_architecture.mmd
│   │   ├── deepresearch_architecture.png
│   │   ├── utils.py
│   │   ├── CH03._02._DeepResearch 에이전트 구현하기.ipynb
│   │   ├── CH03._04._DeepAgent의 To-do list 구현하기.ipynb
│   │   ├── CH03._05._DeepAgent의 File Management 구현하기.ipynb
│   │   ├── CH03._06._DeepAgent의 Sub-Agent 위임 구현하기.ipynb
│   │   └── CH03._07._DeepAgent 완전체 구현하기.ipynb
│   └── 부록. LangChain 및 LangGraph 1.0 기초/
│       ├── langgraph_studio_example/
│       │   ├── README.md
│       │   ├── agent.py
│       │   └── langgraph.json
│       ├── 부록_01._LangChain과 LangGraph 소개.ipynb
│       ├── 부록_02._init_chat_model로 모델 초기화하기.ipynb
│       ├── 부록_03._Tool 데코레이터와 ToolRuntime.ipynb
│       ├── 부록_04._create_agent로 간단한 에이전트 만들기.ipynb
│       ├── 부록_05._StateGraph API로 커스텀 그래프 구축하기.ipynb
│       ├── 부록_06._Middleware로 에이전트 실행 제어하기.ipynb
│       ├── 부록_07._Memory와 State 관리.ipynb
│       ├── 부록_08._Structured Output으로 정형 데이터 받기.ipynb
│       ├── 부록_09._Streaming으로 실시간 응답 처리하기.ipynb
│       └── 부록_10._LangSmith로 Tracing과 디버깅.ipynb
├── pyproject.toml                  # uv 프로젝트 설정
├── uv.lock                         # uv 의존성 잠금 파일
├── requirements.txt                # pip 패키지 의존성
├── .gitignore                      # Git 제외 파일
└── README.md                       # 프로젝트 설명
```

---

## ❗ 문제 해결

### 1. `ModuleNotFoundError` 발생 시

가상환경이 활성화되어 있는지 확인하세요:
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 2. OpenAI API 오류 발생 시

- `.env` 파일에 올바른 API 키가 입력되어 있는지 확인
- API 키에 충분한 크레딧이 있는지 확인

### 3. ChromaDB 관련 오류 발생 시

```bash
pip install --upgrade chromadb
```

---

## 📞 문의

강의 관련 문의는 패스트캠퍼스를 통해 연락해주세요.

---

**Happy Coding! 🎉**

