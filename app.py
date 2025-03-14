import streamlit as st
from PIL import Image
from openai import OpenAI

#ChatGPT 세팅
api_key = st.secrets["openai"]["api_key"]
client = OpenAI(api_key=api_key)  # OpenAI API 키를 여기에 입력하세요!


# 페이지 설정 - wide 레이아웃 적용
st.set_page_config(
    layout="wide",
    page_title="교사교육용 챗봇 프로토타입",  # 🔹 웹페이지 브라우저 탭에 표시되는 제목
    )

# 기존 데이터 저장 공간 설정
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "image_description" not in st.session_state:
    st.session_state.image_description = ""  # 이미지 설명 저장 공간
if "feedback" not in st.session_state:
    st.session_state.feedback = ""  # ChatGPT의 피드백 저장 공간
if "character_input" not in st.session_state:
    st.session_state.character_input = ""  # 등장인물 입력 저장 공간
if "dialogue_input" not in st.session_state:
    st.session_state.dialogue_input = ""  # 대화 입력 저장 공간



# 이미지 목록 준비
image_files = ["Imgs/test_1.png", "Imgs/test_2.png", "Imgs/test_3.png"]
images = [Image.open(img) for img in image_files] 

# 화면을 좌우로 분할
left_col, right_col = st.columns([10, 10])

# 좌측에 이미지 표시
with left_col:
    st.header("문제 상황")
    # 숫자 버튼 (1, 2, 3) 만들기
    image_index = st.radio(f"총 {len(images)}장의 그림이 있습니다.", range(1, len(images) + 1), horizontal=True) - 1

    # 선택된 이미지 표시
    st.image(images[image_index], use_container_width=True)

    # 이미지 설명 입력 (보이지 않지만, 데이터로 저장됨)
    image_description = "이 이미지는 수학에 어려움을 겪는 학생A의 상황입니다."  # 예제 설명 (실제 설명을 적어주세요)
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
        character = st.text_input("등장인물", placeholder="예: 학생A, 교사, 학생B")
        
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
    st.subheader("작성한 대화 내용")
    if st.session_state.chat_history:
        for character, dialogue in st.session_state.chat_history:
            col1, col2 = st.columns([1, 3])
            with col1:
                st.markdown(f"**{character}**")
            with col2:
                st.markdown(dialogue)
    else:
        st.info("아직 대화가 없습니다. 대화를 입력해보세요!")

    # 🔹 제출 버튼 추가 (ChatGPT API 요청)
    if st.button("제출하고 피드백 받기"):
        with st.spinner("분석 중..."):
            # ChatGPT에 보낼 메시지 구성
            prompt = """
            당신은 교사교육 전문가 입니다. 주어진 이미지 설명과 대화 내용을 분석하고, 교사교육 전문가의 관점에서 피드백을 해줘
            피드백은 다음 기준을 따라야 합니다:
            1. 학생이 어려워하는 개념을 구체적으로 지적하기
            2. 개선 방법을 단계별로 제공하기
            3. 교사가 어떤 방식으로 지도하면 좋을지 조언하기
            """
            messages = [
                {"role": "system", "content": prompt},
                {"role": "user", "content": f"이미지 설명: {st.session_state.image_description}"},
            ]
            for char, text in st.session_state.chat_history:
                messages.append({"role": "user", "content": f"{char}: {text}"})

            # OpenAI API 호출
            response = client.chat.completions.create(
                model="gpt-4",
                messages=messages
            )

            # 결과 저장 및 표시
            st.session_state.feedback = response.choices[0].message.content
            st.success("피드백을 받았습니다!")

# 전체 너비를 차지하는 피드백 영역 (새로운 row 추가)
st.markdown("---")  # 가독성을 위한 구분선 추가
st.header("피드백")
if st.session_state.feedback:
    st.markdown(st.session_state.feedback)
else:
    st.info("아직 피드백이 없습니다. '제출하고 피드백 받기' 버튼을 눌러주세요!")