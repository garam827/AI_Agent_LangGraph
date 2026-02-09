# LangGraph Studio Web Search Agent

Exa API를 활용한 웹 검색 에이전트 예제입니다. `create_agent`를 사용하여 구현되었습니다.

## 파일 구조

```text
langgraph_studio_example/
├── agent.py          # 웹 검색 에이전트 코드
├── langgraph.json    # LangGraph Studio 설정
├── .env.example      # 환경 변수 예시
└── README.md         # 이 파일
```

## 설정 방법

### 1. 환경 변수 설정

```bash
# .env.example을 복사하여 .env 파일 생성
cp .env.example .env   # Mac/Linux
copy .env.example .env # Windows
```

`.env` 파일에 API 키 설정:

```env
# 필수
OPENAI_API_KEY=sk-...
EXA_API_KEY=...        # https://exa.ai 에서 발급

# 선택 (LangSmith 트레이싱)
LANGSMITH_API_KEY=lsv2_...
LANGSMITH_TRACING=true
```

> **주의**: Windows에서 `.env` 파일에 한글 주석이 있으면 인코딩 오류가 발생할 수 있습니다. 영문 주석만 사용하세요.

### 2. 의존성 설치

```bash
# 프로젝트 루트에서 실행

# uv 사용 (권장)
uv sync --link-mode=copy  # Windows OneDrive 환경

# 또는 pip 사용
pip install -r requirements.txt

# LangGraph CLI 설치 (in-memory 서버 포함)
pip install -U "langgraph-cli[inmem]"
```

## 실행 방법

### LangGraph Studio 실행

```bash
# 이 폴더로 이동
cd "Part 3. 멀티 에이전트 구조 정복하기/부록. LangChain 및 LangGraph 1.0 기초/langgraph_studio_example"

# 개발 서버 시작
langgraph dev
```

서버가 시작되면 출력되는 URL로 LangGraph Studio 접속:

```text
🚀 API: http://127.0.0.1:2024
🎨 Studio UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
```

### 로컬 테스트 (CLI)

```bash
python agent.py
```

## 에이전트 기능

이 에이전트는 Exa API를 사용하여 실시간 웹 검색을 수행합니다:

| 도구 | 설명 |
| ---- | ---- |
| `search_web` | 웹 검색 (neural search) |
| `search_news` | 최근 뉴스 검색 (날짜 필터링 지원) |
| `get_page_content` | 특정 URL의 전체 내용 읽기 |
| `get_current_time` | 현재 날짜와 시간 조회 |

## 예시 쿼리

- "AI 에이전트 최신 뉴스 검색해줘"
- "LangGraph가 뭐야? 검색해서 알려줘"
- "오늘 테슬라 관련 뉴스 알려줘"
- "What are the latest developments in AI agents?"
- "Search for LangChain vs LangGraph comparison"

## LangGraph Studio 기능

1. **그래프 시각화**: ReAct 에이전트의 노드/엣지 구조 확인
2. **단계별 실행**: 각 도구 호출의 입출력 확인
3. **스레드 관리**: 대화 히스토리 관리 (자동 persistence)
4. **디버깅**: 브레이크포인트 설정 및 상태 검사

## 문제 해결

### `langgraph` 명령어를 찾을 수 없음

```bash
pip install -U "langgraph-cli[inmem]"
```

### Windows 인코딩 오류 (UnicodeDecodeError)

`.env` 파일에 한글이 포함되어 있으면 오류가 발생합니다. 영문만 사용하세요:

```env
# Good
OPENAI_API_KEY=sk-...

# Bad (causes error on Windows)
# OpenAI API 키 (필수)
OPENAI_API_KEY=sk-...
```

### Custom checkpointer 오류

LangGraph Studio는 자체 persistence를 제공하므로, `agent.py`에서 `checkpointer`를 제거해야 합니다:

```python
# Good - Studio용
graph = create_react_agent(model=model, tools=tools)

# Bad - Studio에서 오류 발생
graph = create_react_agent(model=model, tools=tools, checkpointer=memory)
```

### Safari에서 접속 불가

Safari는 localhost 연결을 차단할 수 있습니다:

```bash
langgraph dev --tunnel
```

### EXA_API_KEY 오류

Exa API 키가 없으면 검색 기능이 작동하지 않습니다:

1. <https://exa.ai> 에서 API 키 발급
2. `.env` 파일에 `EXA_API_KEY=...` 추가
