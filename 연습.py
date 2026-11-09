import streamlit as st
# python -m streamlit run 연습.py
st.title("💗공주들의 추억사이트💗")

이름 = st.text_input("이름을 입력하세요")

if st.button("클릭"):
    st.write(이름, "공주 환영해♥️ 아래는 우리들의 추억장소야!구경해🐾")

st.image("KakaoTalk_20261109_165537369.png",width=300)
st.image("야외 그릴 테이블의 따뜻한 밤 모임.png",width=300)
st.image("따뜻한 방의 애니메이션 신부 셀피.png",width=300)

질문 = st.text_input("사진 어때?")
if st.button("클릭!"):
    st.write(질문,"'(이)라구? 헐 감동이야!! 나두 그렇게 생각해🩵")

질문2 = st.text_input("앞으로도 같이 추억 많이 쌓을거징?")
if st.button("클릭!!"):
    st.write("소연 AI 답변:ㅎ.ㅎ나도 네 의견이랑 똑같이 생각헤💖")


질문3 = st.text_input("소연 AI 답변:마지막으로 4명 단톡에 후기 카톡남겨줘👻")



if st.button("클릭!!!"):
    st.write("소연 AI 답변:","조금 더 업그레이드 됏었으면 하는것도 카톡으로 남겨줘!")



st.write("그럼 곤쥬들 다음에 또 봐~👋🏻💌")