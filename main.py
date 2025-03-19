import streamlit as st

# 페이지 전체 너비로 설정
st.set_page_config(
    layout="centered",
    page_title="교사교육용 챗봇 프로토타입",  # 🔹 웹페이지 브라우저 탭에 표시되는 제목
    )

# 🔥 CSS를 사용하여 사이드바 및 네비게이션 완전 제거
hide_sidebar = """
    <style>
        [data-testid="stSidebar"] {display: none !important;}
        [data-testid="stSidebarNav"] {display: none !important;}
    </style>
"""
st.markdown(hide_sidebar, unsafe_allow_html=True)


st.title("메인 페이지")
st.write("우리 프로그램에 대한 설명.")

if st.button("수업 영상 시청", use_container_width=True):
    st.switch_page("pages/video.py")  # 사이드바 없이 페이지 전환 가능!


# 푸터 추가
st.markdown("---")  # 가독성을 위한 구분선
st.markdown("© 2024 MyApp | Developed by [Your Name](https://yourwebsite.com)")