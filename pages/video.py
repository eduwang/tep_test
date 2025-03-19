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

# 미리 지정된 유튜브 영상 URL
youtube_url = "https://youtu.be/RuLtMcxXRoM"  # 원하는 유튜브 링크로 변경

def get_embed_url(youtube_url):
    # 유튜브 URL을 embed 가능한 URL로 변환
    if "watch?v=" in youtube_url:
        video_id = youtube_url.split("watch?v=")[-1]
    elif "youtu.be/" in youtube_url:
        video_id = youtube_url.split("youtu.be/")[-1]
    else:
        return None
    return f"https://www.youtube.com/embed/{video_id}"

# 페이지 제목
st.title("사전 영상 시청")

# 유튜브 영상 표시
embed_url = get_embed_url(youtube_url)
if embed_url:
    st.video(embed_url)  # 유튜브 영상 재생
else:
    st.error("유효한 유튜브 링크를 확인하세요!")

if st.button("가상 대화 입력 페이지로 이동", use_container_width=True):
    st.switch_page("pages/app.py")  # 사이드바 없이 페이지 전환 가능!

# 푸터 추가
st.markdown("---")  # 가독성을 위한 구분선
st.markdown("© 2024 MyApp | Developed by [Your Name](https://yourwebsite.com)")