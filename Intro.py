import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from plotly.subplots import make_subplots


def set_custom_css(): #사이트 전체 css 적용(건들지 마셈!)
    st.set_page_config(page_title="강서구 교통안전 빅데이터", page_icon="🔍", layout="wide")

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
    st.title("강서구 어린이 교통환경 빅데이터")
    st.subheader('by childrensave.co.kr')

def col1_about():
    st.markdown('''<h5> 해당 페이지는 어린이 교통환경에 대한 시각화 자료를 나타낸 페이지입니다.</h5>''', unsafe_allow_html=True)
	
    image_link1 = "https://imgur.com/tO3wtE3.png"
    st.markdown('''
    <div style="display: flex; align-items: center;"><img src="{}" style="height: 150px; width:50px; margin-right:5px; margin-bottom:10px;"><h5>In the Data tab on the left, you can see map visualization data, chart data, and data tables for each category. You can view it.</h5>
    '''.format(image_link1), unsafe_allow_html=True)
    image_link2 = "https://imgur.com/muedAfS.png"
    st.markdown('''
    <div style="display: flex; align-items: center;"><img src="{}" style="height: 150px; width:50px; margin-right:5px; margin-bottom:10px;"><h5>Each category is divided into CCTV, traffic volume, child traffic accidents, location of elementary, middle, and high schools, and location of child protection zone. It is divided.</h5>
    '''.format(image_link2), unsafe_allow_html=True)
	
def col2_about():
    st.header("페이지 구성 목적")
    
    image_path1 = "https://ifh.cc/g/zCYynK.png"
    st.markdown(f'<div style="display: flex; align-items: center;"><img src="{image_path1}" style="width:50px; margin-right:5px; margin-bottom:10px;"><h5> 누구나 One-click으로 쉽게 접근할 수 있도록 구성</h5>', unsafe_allow_html=True)
    
    
    image_path2 = "https://ifh.cc/g/JmsXp7.png"
    st.markdown(f'<div style="display: flex; align-items: center;"><img src="{image_path2}" style="width:50px; margin-right:5px; margin-bottom:10px;"><h5> 관련 있는 항목을 한 화면에 보여주어 자료 간 상관성을 확인할 수 있도록 구성</h5>', unsafe_allow_html=True)

    
    image_path3 = "https://ifh.cc/g/GXP5Nz.png"
    st.markdown(f'<div style="display: flex; align-items: center;"><img src="{image_path3}" style="width:50px; margin-right:5px; margin-bottom:10px;"><h5> 사용자가 원하는 자료만 확인할 수 있는 친사용자 환경을 구성</h5>', unsafe_allow_html=True)

def col3_about():
    st.divider()
    imgPath1 = "https://i.imgur.com/giJzGgl.png"
    st.markdown(f'<div style="display: flex; align-items: center;"><img src="{imgPath1}" style="width: 300px; height:80px; margin-right:20px; margin-bottom:20px;">', unsafe_allow_html=True)
    imgPath2 = "https://i.ibb.co/0FdxyNz/geopandas-logo-web.png"
    st.markdown(f'<div style="display: flex; align-items: center;"><img src="{imgPath2}" style="width: 300px; height:80px; margin-right:20px; margin-bottom:20px;">', unsafe_allow_html=True)
    imgPath3 = "https://i.ibb.co/hcPGx3Q/Num-Py-logo.png"
    st.markdown(f'<div style="display: flex; align-items: center;"><img src="{imgPath3}" style="width: 300px; height:80px; margin-right:20px; margin-bottom:20px;">', unsafe_allow_html=True)

def col4_about():
    st.divider()
    imgPath1 = "https://i.ibb.co/G0CMx3g/python-logo.png"
    st.markdown(f'<div style="display: flex; align-items: center;"><img src="{imgPath1}" style="width: 300px; height:80px; margin-right:20px; margin-bottom:20px;">', unsafe_allow_html=True)
    imgPath2 = "https://i.ibb.co/K7hJ1F4/Plotly-logo.png"
    st.markdown(f'<div style="display: flex; align-items: center;"><img src="{imgPath2}" style="width: 300px; height:80px; margin-right:20px; margin-bottom:20px;">', unsafe_allow_html=True)
    imgPath3 = "https://i.imgur.com/63k4cx2.png"
    st.markdown(f'<div style="display: flex; align-items: center;"><img src="{imgPath3}" style="width: 300px; height:80px; margin-right:20px; margin-bottom:20px;">', unsafe_allow_html=True)

def col5_about():
    st.divider()
    imgPath1 = "https://i.ibb.co/Rcqwp6T/css3-logo.png"
    st.markdown(f'<div style="display: flex; align-items: center;"><img src="{imgPath1}" style="width: 150px; height:80px; margin-right:20px; margin-bottom:20px;">', unsafe_allow_html=True)
    imgPath2 = "https://i.ibb.co/jv1hy3v/vs.png" 
    st.markdown(f'<div style="display: flex; align-items: center;"><img src="{imgPath2}" style="width: 120px; height:80px; margin-right:20px; margin-bottom:20px;">', unsafe_allow_html=True)
    imgPath3 = "https://i.imgur.com/6lxguoP.png" 
    st.markdown(f'<div style="display: flex; align-items: center;"><img src="{imgPath3}" style="width: 120px; height:80px; margin-right:20px; margin-bottom:20px;">', unsafe_allow_html=True)


set_custom_css()
     

main_header()

st.divider()

col1, empty , col2 = st.columns([1, 0.1,0.9])
col3 ,col4, col5=st.columns(3)

with col1:
    col1_about()

with empty:
    pass

with col2:
    col2_about()


st.divider()
