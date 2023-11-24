import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from plotly.subplots import make_subplots


def set_custom_css(): #사이트 전체 css 적용(건들지 마셈!)
    st.set_page_config(page_title="강서구 교통환경 시각화", page_icon="🚌", layout="wide")

    with open("./style.css", "r") as f:
        css_content = f.read()

    st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
    video_html = """
		<style>
        
		#myVideo {
		  position: fixed;
		  right: 0;
		  bottom: 0;
		  min-width: 100%; 
		  min-height: 100%;
		}

		.content {
		  position: fixed;
		  bottom: 0;
		  background: rgba(0, 0, 0, 0.5);
		  color: #f1f1f1;
		  width: 100%;
		  padding: 20px;
		}
    

		</style>	
		<video autoplay muted loop id="myVideo">
		  <source src="https://i.imgur.com/EYTsgNh.mp4")>
		</video>
        """

    st.markdown(video_html, unsafe_allow_html=True)

    

def main_header():
    st.title("아이의 아이에 의한 아이를 위한 교통환경 시각화 대시보드")
    st.subheader('"I want safe"')

def col1_component():
    st.header("개요")
    project_description = """<h5>
    현대인은 자동차가 많은 현대 사회에서 살아가면서
    직간접적으로 교통사고 위험을
    경험하는 경우가 많이 있습니다.
    특히 영유아, 어린이 같은 사회적 약자의 경우
    교통사고 발생 시 더 큰 피해를 입게 됩니다.

    이러한 어린이 교통사고 피해를 막기 위해
    어린이 당사자보다는 아동의 학부모에게
    통학로 등의 교통안전을 위해 정보를 제공하는 것이
    이번 프로젝트의 1차 목표입니다.</h5>
    """
    st.markdown(    '''<h5>현대인은 자동차가 많은 현대 사회에서 살아가면서
    직간접적으로 교통사고 위험을
    경험하는 경우가 많이 있습니다.
    특히 영유아, 어린이 같은 사회적 약자의 경우
    교통사고 발생 시 더 큰 피해를 입게 됩니다.
                </h5>\n\n''', unsafe_allow_html=True)
    st.markdown(    '''<h5>            
    이러한 어린이 교통사고 피해를 막기 위해
    어린이 당사자보다는 아동의 학부모에게
    통학로 등의 교통안전을 위해 정보를 제공하는 것이
    이번 프로젝트의 1차 목표입니다.</h5>''', unsafe_allow_html=True)

def col2_component():
    st.header("대시보드를 제작한 이유")
    
    image_path1 = "https://ifh.cc/g/zCYynK.png"
    st.markdown(f'<div style="display: flex; align-items: center;"><img src="{image_path1}" style="width:50px; margin-right:5px; margin-bottom:10px;"><h5> 누구나 One-click으로 쉽게 접근할 수 있도록 구성</h5>', unsafe_allow_html=True)
    
    
    image_path2 = "https://ifh.cc/g/JmsXp7.png"
    st.markdown(f'<div style="display: flex; align-items: center;"><img src="{image_path2}" style="width:50px; margin-right:5px; margin-bottom:10px;"><h5> 관련 있는 항목을 한 화면에 보여주어 자료 간 상관성을 확인할 수 있도록 구성</h5>', unsafe_allow_html=True)

    
    image_path3 = "https://ifh.cc/g/GXP5Nz.png"
    st.markdown(f'<div style="display: flex; align-items: center;"><img src="{image_path3}" style="width:50px; margin-right:5px; margin-bottom:10px;"><h5> 사용자가 원하는 자료만 확인할 수 있는 친사용자 환경을 구성</h5>', unsafe_allow_html=True)

def col3_component():
    st.divider()
    imgPath1 = "https://i.ibb.co/RQ9chgx/streamlit-logo.png"
    st.markdown(f'<div style="display: flex; align-items: center;"><img src="{imgPath1}" style="width: 300px; height:80px; margin-right:20px">', unsafe_allow_html=True)
    imgPath2 = "https://i.ibb.co/0FdxyNz/geopandas-logo-web.png"
    st.markdown(f'<div style="display: flex; align-items: center;"><img src="{imgPath2}" style="width: 300px; height:80px; margin-right:20px">', unsafe_allow_html=True)
    imgPath3 = "https://i.ibb.co/hcPGx3Q/Num-Py-logo.png"
    st.markdown(f'<div style="display: flex; align-items: center;"><img src="{imgPath3}" style="width: 300px; height:80px; margin-right:20px">', unsafe_allow_html=True)

def col4_component():
    st.divider()
    imgPath1 = "https://i.ibb.co/G0CMx3g/python-logo.png"
    st.markdown(f'<div style="display: flex; align-items: center;"><img src="{imgPath1}" style="width: 300px; height:80px; margin-right:20px">', unsafe_allow_html=True)
    imgPath2 = "https://i.ibb.co/K7hJ1F4/Plotly-logo.png"
    st.markdown(f'<div style="display: flex; align-items: center;"><img src="{imgPath2}" style="width: 300px; height:80px; margin-right:20px">', unsafe_allow_html=True)
    imgPath3 = "https://i.ibb.co/Rcqwp6T/css3-logo.png"
    st.markdown(f'<div style="display: flex; align-items: center;"><img src="{imgPath3}" style="width: 300px; height:80px; margin-right:20px">', unsafe_allow_html=True)

def col5_component():
    st.divider()
    imgPath1 = "https://i.ibb.co/K5ZfSL0/folium-logo-removebg-preview.png"
    st.markdown(f'<div style="display: flex; align-items: center;"><img src="{imgPath1}" style="width: 300px; height:80px; margin-right:20px">', unsafe_allow_html=True)
    imgPath2 = "https://i.ibb.co/mh70rm9/Imgur-logo.png" 
    st.markdown(f'<div style="display: flex; align-items: center;"><img src="{imgPath2}" style="width: 300px; height:80px; margin-right:20px">', unsafe_allow_html=True)
    imgPath3 = "https://i.ibb.co/qBds4Lb/json-logo.png" 
    st.markdown(f'<div style="display: flex; align-items: center;"><img src="{imgPath3}" style="width: 300px; height:80px; margin-right:20px">', unsafe_allow_html=True)

set_custom_css()
     

main_header()

st.divider()

col1, empty , col2 = st.columns([1, 0.1,0.9])
col3 ,col4, col5=st.columns(3)

with col1:
    col1_component()

with empty:
    pass

with col2:
    col2_component()

with col3:
    col3_component()

with col4:
    col4_component()

with col5:
    col5_component()
st.divider()
