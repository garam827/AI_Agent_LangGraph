from session import conn


def query_db(query: str) -> list:
    """데이터베이스에 쿼리를 실행하고 결과를 반환합니다.

    Args:
        query (str): 실행할 SQL 쿼리

    Returns:
        list: 결과 행 목록 (레코드 형태)
    """

    print("데이터 조회중...", end="")

    try:
        with conn.cursor() as cursor:
            cursor.execute(query)

            # 열 이름을 가져옵니다.
            rows = cursor.fetchall()

            # 결과를 딕셔너리 형태로 변환합니다.
            columns = [col[0] for col in cursor.description]

            result = [dict(zip(columns, row)) for row in rows]
    except Exception as e:
        result = []
    print("완료", end="\n")
    return result