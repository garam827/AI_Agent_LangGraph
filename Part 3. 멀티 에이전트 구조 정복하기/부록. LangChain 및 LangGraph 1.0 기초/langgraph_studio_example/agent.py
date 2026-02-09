"""LangGraph Studio Web Search Agent with Middleware

create_agent와 SummarizationMiddleware를 사용한 웹 검색 에이전트 예제입니다.
- Exa API를 활용한 실시간 웹 검색
- 대화 요약 Middleware (긴 대화 자동 요약)

사용법:
1. 환경 변수 설정 (.env 파일에 EXA_API_KEY 추가)
2. `langgraph dev` 명령어로 개발 서버 시작
3. LangGraph Studio에서 http://127.0.0.1:2024 연결
"""

import os
from datetime import datetime
from typing import Optional

from dotenv import load_dotenv
from exa_py import Exa

from langchain_core.tools import tool
from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware

# 환경 변수 로드
load_dotenv()


# ============================================================
# 1. Exa 클라이언트 설정
# ============================================================
def get_exa_client() -> Optional[Exa]:
    """Exa 클라이언트 반환 (API 키가 없으면 None)"""
    api_key = os.getenv("EXA_API_KEY")
    if api_key:
        return Exa(api_key=api_key)
    return None


# ============================================================
# 2. 도구 정의
# ============================================================
@tool
def search_web(query: str, num_results: int = 5) -> str:
    """Search the web for current information using Exa API.

    Use this tool when you need to find up-to-date information,
    news, or facts that might not be in your training data.

    Args:
        query: The search query to look up
        num_results: Number of results to return (default: 5)

    Returns:
        Search results with titles, URLs, and content snippets
    """
    client = get_exa_client()

    if not client:
        return "Error: EXA_API_KEY is not set. Please add it to your .env file."

    try:
        results = client.search_and_contents(
            query=query,
            type="auto",
            num_results=num_results,
            text={"max_characters": 2000},
        )

        if not results.results:
            return f"No results found for: {query}"

        output = f"Search results for '{query}':\n\n"
        for i, result in enumerate(results.results, 1):
            output += f"{i}. **{result.title}**\n"
            output += f"   URL: {result.url}\n"
            if result.text:
                snippet = result.text[:2000] + "..." if len(result.text) > 2000 else result.text
                output += f"   {snippet}\n"
            output += "\n"

        return output

    except Exception as e:
        return f"Search error: {str(e)}"


@tool
def search_news(query: str, days: int = 7) -> str:
    """Search for recent news articles using Exa API.

    Use this tool specifically for finding recent news and current events.
    Query needs to be specific and recent and in English.

    Args:
        query: The news topic to search for
        days: How many days back to search (default: 7)

    Returns:
        Recent news articles with titles, URLs, and summaries
    """
    client = get_exa_client()

    if not client:
        return "Error: EXA_API_KEY is not set. Please add it to your .env file."

    try:
        from datetime import timedelta

        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)

        results = client.search_and_contents(
            query=query,
            type="auto",
            num_results=5,
            start_published_date=start_date.strftime("%Y-%m-%d"),
            text={"max_characters": 2000},
        )

        if not results.results:
            return f"No recent news found for: {query}"

        output = f"Recent news about '{query}' (last {days} days):\n\n"
        for i, result in enumerate(results.results, 1):
            output += f"{i}. **{result.title}**\n"
            output += f"   URL: {result.url}\n"
            if hasattr(result, 'published_date') and result.published_date:
                output += f"   Published: {result.published_date}\n"
            if result.text:
                snippet = result.text[:2000] + "..." if len(result.text) > 2000 else result.text
                output += f"   {snippet}\n"
            output += "\n"

        return output

    except Exception as e:
        return f"News search error: {str(e)}"


@tool
def get_page_content(url: str) -> str:
    """Get the full content of a specific webpage using Exa API.

    Use this tool when you need to read the detailed content of a specific URL.

    Args:
        url: The URL of the page to read

    Returns:
        The main text content of the webpage
    """
    client = get_exa_client()

    if not client:
        return "Error: EXA_API_KEY is not set. Please add it to your .env file."

    try:
        results = client.get_contents(
            url,
            text={"max_characters": 2000},
        )

        if not results.results:
            return f"Could not retrieve content from: {url}"

        result = results.results[0]
        output = f"Content from: {result.url}\n"
        output += f"Title: {result.title}\n\n"
        output += result.text if result.text else "No text content available."

        return output

    except Exception as e:
        return f"Error getting page content: {str(e)}"


@tool
def get_current_time() -> str:
    """Get the current date and time.

    Returns:
        Current date and time in a readable format
    """
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S (%A)")


# 도구 리스트
tools = [search_web, search_news, get_page_content, get_current_time]


# ============================================================
# 3. 시스템 프롬프트
# ============================================================
SYSTEM_PROMPT = """You are a helpful web research assistant powered by Exa search.

Your capabilities:
- search_web: Search the internet for any information
- search_news: Find recent news articles (specify days parameter for time range)
- get_page_content: Read the full content of a specific URL
- get_current_time: Get the current date and time

Guidelines:
1. Always use search tools when asked about current events, recent information, or facts you're unsure about.
2. For news queries, use search_news for better results on recent events.
3. If a search result looks promising but needs more detail, use get_page_content to read the full article.
4. Cite your sources by including URLs when providing information from searches.
5. If EXA_API_KEY is not set, inform the user they need to add it to the .env file.

Respond in Korean when the user writes in Korean, otherwise respond in English."""


# ============================================================
# 4. 에이전트 생성 (LangGraph Studio용)
# ============================================================
# create_agent를 사용하여 에이전트 생성
# SummarizationMiddleware: 토큰 4000개 초과 시 자동 요약, 최근 20개 메시지 유지
graph = create_agent(
    model="gpt-4.1-mini",
    tools=tools,
    system_prompt=SYSTEM_PROMPT,
    middleware=[
        SummarizationMiddleware(
            model="gpt-4.1-mini",
            trigger=("tokens", 4000),
            keep=("messages", 20),
        ),
    ],
)


# ============================================================
# 5. 로컬 테스트용 코드
# ============================================================
if __name__ == "__main__":
    from langchain_core.messages import HumanMessage

    print("=" * 60)
    print("Web Search Agent with SummarizationMiddleware Test")
    print("=" * 60)

    # EXA_API_KEY 확인
    if not os.getenv("EXA_API_KEY"):
        print("\n⚠️  Warning: EXA_API_KEY is not set!")
        print("Add it to your .env file to enable web search.")
        print("Get your API key at: https://exa.ai\n")

    # 테스트 쿼리
    test_queries = [
        "What time is it now?",
        "Search for the latest news about AI agents",
        "What is LangGraph and how does it work?",
    ]

    for query in test_queries:
        print(f"\n🔍 Query: {query}")
        print("-" * 40)

        result = graph.invoke({
            "messages": [HumanMessage(content=query)]
        })

        # 마지막 AI 메시지 출력
        last_message = result["messages"][-1]
        content = last_message.content if last_message.content else "[No content]"
        print(f"🤖 Response:\n{content[:800]}...")
        print("=" * 60)
