import streamlit as st
from PIL import Image
from openai import OpenAI


# 페이지 설정 - wide 레이아웃 적용
st.set_page_config(layout="wide")

# 기존 데이터 저장 공간 설정
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "image_description" not in st.session_state:
    st.session_state.image_description = ""  # 이미지 설명 저장 공간

# 화면을 좌우로 분할
left_col, right_col = st.columns([10, 10])

# 좌측에 이미지 표시
with left_col:
    st.header("이미지 섹션")
    image = Image.open("Imgs/test_1.png")  # 이미지 파일 이름을 여기에 적어주세요.
    st.image(image, use_container_width=True)

    # 이미지 설명 입력 (보이지 않지만, 데이터로 저장됨)
    image_description = "이 이미지는 한 남성이 공원에서 산책하는 모습을 담고 있습니다."  # 예제 설명 (실제 설명을 적어주세요)
    st.session_state.image_description = image_description

# 우측: 대화 입력 섹션
with right_col:
    st.header("대화 시나리오 작성")

    # 기존 대화 내용을 저장할 공간
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # 가로 병렬 배치: 등장인물 입력과 대화 입력
    col1, col2 = st.columns([1, 3])
    
    with col1:
        character = st.text_input("등장인물", placeholder="예: 주인공, 친구, 선생님")
        
    with col2:
        user_input = st.text_input("대화", placeholder="대화를 입력하세요")

    # 전송 버튼 클릭 시 대화 추가
    if st.button("대화 추가"):
        if character and user_input:
            # 대화 형식으로 저장
            st.session_state.chat_history.append((character, user_input))
            st.success("대화가 추가되었습니다.")
        else:
            st.warning("등장인물과 대화를 모두 입력해주세요!")

    # 대화 내용 출력 (등장인물과 대화를 가로로 나란히)
    st.subheader("대화 내용")
    if st.session_state.chat_history:
        for character, dialogue in st.session_state.chat_history:
            col1, col2 = st.columns([1, 3])
            with col1:
                st.markdown(f"**{character}**")
            with col2:
                st.markdown(dialogue)
    else:
        st.info("아직 대화가 없습니다. 대화를 입력해보세요!")