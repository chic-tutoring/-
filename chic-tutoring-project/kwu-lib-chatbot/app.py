import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="KW-LIBRARY 챗봇",
    page_icon="📚",
    layout="centered"
)

# 상단 제목
st.title("📚 광운대학교 도서관 Q&A 챗봇")

# 설명 텍스트
st.markdown("""
안녕하세요! 도서관 이용에 대해 궁금한 점을 질문해주세요.  
아래 입력창에 자유롭게 입력하시면 관련 정보를 알려드립니다.  
""")

# 사용자 입력 받기
question = st.text_input("❓ 궁금한 점을 입력하세요", placeholder="예: 연체료는 얼마인가요?")

# 답변 처리 로직
def get_answer(q: str) -> str:
    q = q.lower()
    if "연체료" in q or "벌금" in q:
        return "📌 연체료는 1일당 100원이며, 최대 5,000원까지 부과됩니다."
    elif "자리" in q or "예약" in q:
        return "🪑 자리 예약은 오전 9시부터 도서관 앱 또는 홈페이지를 통해 가능합니다."
    elif "도서" in q and "반납" in q:
        return "📖 도서는 반납 예정일까지 반납하지 않으면 연체료가 부과됩니다."
    else:
        return "😢 죄송합니다. 해당 질문에 대한 답변이 아직 준비되지 않았습니다."

# 답변 출력
if question:
    answer = get_answer(question)
    st.markdown("---")
    st.subheader("💬 챗봇의 답변:")
    st.success(answer)
