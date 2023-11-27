import streamlit as st


def set_custom_css():
    st.set_page_config(page_title="강서구 교통환경 시각화", page_icon="🚌", layout="wide")

    with open("./style.css", "r") as f:
        css_content = f.read()

    st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)   

def main_header():
    pass

def col1_about():
    st.header("Creator")
    st.divider()
    img_path = "https://i.ibb.co/br83bJr/about.png"
    st.markdown(f'<div style="display: flex; align-items: center;"><img src="{img_path}" style="width: 702px; margin-right:20px">', unsafe_allow_html=True)
    

def col2_about():
    st.header("Source")
    st.divider()
    
    col2_centered_html = """
        <div style="display: flex; flex-direction: column; align-items: left;">
            <p style="font-size: 20px;"><strong><교통량></strong></p>
            <p style="font-size: 15px;">2022.04 서울시 시계 지점별 교통량 통계</p>
            <p style="font-size: 15px;">2022.04 서울시 도심 지점별 교통량 통계</p>
            <p style="font-size: 15px;">2022.04 서울시 교량 지점별 교통량 통계</p>
            <p style="font-size: 15px;">2022.04 서울시 간선도로 지점별 교통량 통계</p>
            <br>
            <p style="font-size: 20px;"><strong><교통사고></strong></p>
            <p style="font-size: 15px;">2022.02 경찰청 전국 교통사고 다발지역 표준 데이터</p>
            <br>
            <p style="font-size: 20px;"><strong><학교 정보></strong></p>
            <p style="font-size: 15px;">2023.11 서울시교육청 학교 기본 정보</p>
            <p style="font-size: 15px;"><strong><CCTV 설치 수량></strong></p>
            <p style="font-size: 15px;">2023.08 서울시 자치구 목적별 CCTV 설치 수량</p>
            <br>
            <p style="font-size: 20px;"><strong><어린이 보호구역 위치></strong></p>
            <p style="font-size: 15px;">2022.05 서울특별시, 어린이 보호구역 위치</p>
        </div>
    """
    st.markdown(col2_centered_html, unsafe_allow_html=True)


set_custom_css()


col1, col2 , col3= st.columns([1,0.1,0.9])

with col1:
    col1_about()


with col2:
    pass
 

with col3:
    col2_about()

st.divider()
