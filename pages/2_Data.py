import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time
from streamlit_option_menu import option_menu
from plotly.subplots import make_subplots

def sidebar(): 
    with st.sidebar:
        selected = option_menu("데이터", ["cctv", "교통량", "어린이 사고","어린이 보호구역","초/중/고 위치"], 
        icons=['bi bi-camera-video-fill', 'bi bi-car-front-fill','bi bi-bandaid-fill','bi bi-sign-stop-fill','bi bi-hospital-fill'],
        menu_icon="bi bi-bar-chart-line-fill", 
        default_index=0,
        styles = {
        "container": {"padding": "4!important"},
        "icon": {"color": "white", "font-size": "25px"},
        "nav-link": {"font-size": "16px", 
                    "text-align": "left", 
                    "margin":"0px", 
                    "--hover-color": "#feefc6"
                    },
        "nav-link-selected": {"background-color": "#fccf55",
                                "color": "#0b1e33"}
        } )

    return selected    

def main_header(): 
    st.title("강서구 어린이 교통환경 데이터 시각화")
    st.subheader("3조🦷틀딱코딩단")

def load_folium_map(selected_page):
    if selected_page == "cctv": 
        st.markdown(
                    """
                    <style>
                    width:50px; 
                    margin-right:5px;
                    margin-bottom:10px;">
                    </style>
                    <h5> 강서구 CCTV 설치 현황 -색이 진할수록 cctv가 설치된 밀도가 높습니다.</h5>
                    """
                    , 
                    unsafe_allow_html=True)
        html_file_path = "./html/cctv_final.html"
    elif selected_page == "교통량":
        st.markdown(
                    """
                    <style>
                    width:50px; 
                    margin-right:5px;
                    margin-bottom:10px;">
                    </style>
                    <h5> 강서구 교통량 현황 -원의 크기가 클수록 교통량이 많습니다.</h5>
                    """
                    , 
                    unsafe_allow_html=True)
        html_file_path = "./html/traffic_final.html"
    elif selected_page == "어린이 사고":
        st.markdown(
                    """
                    <style>
                    width:50px; 
                    margin-right:5px;
                    margin-bottom:10px;">
                    </style>
                    <h5> 강서구 어린이 교통사고 현황 -마우스 오버시 상세 사고 현황을 볼 수 있습니다.</h5>
                    """
                    , 
                    unsafe_allow_html=True)
        html_file_path = "./html/accident_final.html"
    elif selected_page == "어린이 보호구역":
        st.markdown(
                    """
                    <style>
                    width:50px; 
                    margin-right:5px;
                    margin-bottom:10px;">
                    </style>
                    <h5> 강서구 어린이 보호구역 위치 현황 </h5>
                    """
                    , 
                    unsafe_allow_html=True)
        html_file_path = "./html/childrenArea_final.html"
    elif selected_page == "초/중/고 위치":
        st.markdown(
                    """
                    <style>
                    width:50px; 
                    margin-right:5px;
                    margin-bottom:10px;">
                    </style>
                    <h5> 강서구 초/중/고 위치 현황 -마우스 오버 시 학교 명을 볼 수 있습니다. </h5>
                    """
                    , 
                    unsafe_allow_html=True)
        html_file_path = "./html/school_final.html"     
    else:
        # 지도가 선택되지 않은 경우의 기본값
        html_file_path = ""

    # 선택한 인덱스에 따라 Folfum 지도를 표시
    if html_file_path:
        with open(html_file_path, "r", encoding="utf-8") as file:
            folium_html_content = file.read()
            st.components.v1.html(folium_html_content, scrolling=True)
            
    else:
        st.warning("지도를 선택해주세요.")
    
def plotly(selected_page):
    if selected_page == "cctv":
            st.markdown(
                    """
                    <h5> 강서구 목적별 CCTV 설치 수량 </h5>
                    <style>
                    width:50px; 
                    margin-right:5px;
                    margin-bottom:10px;">
                    </style>
                    """
                    , 
                    unsafe_allow_html=True)
            line_counter = 0
            fieldName = []
            cctvList = []
            with open('./csv/test1.csv', 'r', encoding='utf8') as cd:
                while 1:
                    data = cd.readline()
                    if not data:
                        break
                    if line_counter == 0:
                        fieldName = data.split(",")
                    else:
                        cctvList = data.split(",")
                    line_counter += 1
            data = {'Category': fieldName[2:], 'Value': cctvList[2:]}
            df = pd.DataFrame(data)

            fig = px.pie(df, values='Value', names='Category',hole=0.4
                            ,color_discrete_sequence=['#F7A41E','#FCBB51','#FADE64','#FFF2A1','#FFF9D0'])  
            fig.update_layout(width=1200, height=380,margin=dict(t=50,b=0,l=0,r=0))

            st.plotly_chart(fig,use_container_width=True)


    elif selected_page == "교통량":
            st.markdown(
                    """
                    <h5> 2022 강서구 교통량의 평균 </h5>
                    <style>
                    width:50px; 
                    margin-right:5px;
                    margin-bottom:10px;">
                    </style>
                    """
                    , 
                    unsafe_allow_html=True)
            part1=[]
            count1=[]
            lineCounter=0

            with open('./csv/trafficTotal.csv','r',encoding='utf8')as csvList:
                while 1:
                    data=csvList.readline()
                    if not data:break
                    if lineCounter == 0:
                        part1=data.split(",")

                    else:
                        count1.append(data.split(","))

                    lineCounter+=1

            part2=[]
            count2=[]
            lineCounter=0

            with open('./csv/trafficGangseo.csv','r',encoding='utf8')as csvList1:
                while 1:
                    data=csvList1.readline()
                    if not data:break
                    if lineCounter == 0:
                        part2=data.split(",")

                    else:
                        count2.append(data.split(","))

                    lineCounter+=1

            chart1=[]
            chart2=[]
            i=0

            count1 = [item for sublist in count1 for item in sublist]
            chart1=count1[0::2]
            count1=[float(i) for i in count1[1::2]]

            count2 = [item for sublist in count2 for item in sublist]
            chart2 = count2[0::2]
            count2=[float(i) for i in count2[1::2]]

            fig2=go.Figure()
                        
            fig2.add_trace(go.Bar(x=chart1,y=count1,name='서울시 교통량 평균',marker_color='#FFA617'))
            fig2.add_trace(go.Bar(x=chart1,y=count2,name='강서구 교통량 평균',marker_color='#FADE64'))
            fig2.update_layout(xaxis_title='구분',yaxis_title='교통량의 통계',barmode='group')
            fig2.update_layout(width=1200, height=380,margin=dict(t=50,b=0,l=0,r=0))
            fig2.update_layout(legend=dict(traceorder='normal', orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1))
            st.plotly_chart(fig2,use_container_width=True)

    elif selected_page == "어린이 사고":
            st.markdown(
                    """
                    <h5> 강서구 어린이 교통사고 연도별 통계 </h5>
                    <style>
                    width:50px; 
                    margin-right:5px;
                    margin-bottom:10px;">
                    </style>
                    """
                    , 
                    unsafe_allow_html=True)
            years=[]
            counts=[]
            lineCounter=0
            with open('./csv/childrenAccidentBar.csv','r',encoding='utf8')as csvList:
                while 1:
                    data=csvList.readline()
                    if not data:break
                    if lineCounter == 0:
                        years=data.split(",")
                    else:
                        counts=data.split(",")
                    
                    lineCounter+=1
            
            years = [int(i) for i in years[1:]]
            counts = [int(i) for i in counts[1:]]
            
            colors=['#F7A41E','#FCBB51','#FADE64','#FFF2A1','#FFF9D0']
            df= pd.DataFrame({'Category':years,'Value':counts,'Years':colors})

            fig3=px.bar(df,x='Category',y='Value',color='Years',color_discrete_sequence=colors,text='Value')

            fig3.update_layout(
                xaxis_title='연도',
                yaxis_title='교통사고 수',
                legend_title='연도 구분')
            fig3.update_layout(legend=dict(traceorder='normal', orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1))
            fig3.update_traces(textposition='outside', textfont=dict(color='black'))
            fig3.update_layout(width=1200, height=380,margin=dict(t=50,b=0,l=0,r=0))
            fig3.data[0].name = '2018'
            fig3.data[1].name = '2019'
            fig3.data[2].name = '2020'
            fig3.data[3].name = '2021'
            fig3.data[4].name = '2022'

            st.plotly_chart(fig3,use_container_width=True)

    elif selected_page == "어린이 보호구역":
            st.markdown(
                    """
                    <h5> 강서구 청소년 비율 및 어린이보호구역 </h5>
                    <style>
                    width:50px; 
                    margin-right:5px;
                    margin-bottom:10px;">
                    </style>
                    """
                    , 
                    unsafe_allow_html=True)
            part1 = []
            count1 = []
            line_counter = 0

            with open('./csv/gs_ChildrenTotal.csv', 'r', encoding='utf-8') as csv_list:
                while 1:
                    data = csv_list.readline()
                    if not data:break
                    if line_counter == 0:
                        part1 = data.split(",")
                    else:
                        count1.append(data.split(","))

                    line_counter += 1

            part2=[]
            count2=[]
            line_counter = 0
            with open('./csv/gs_ChildrenSafetyzone.csv', 'r', encoding='utf-8') as csv_list_1:
                while 1:
                    data=csv_list_1.readline()
                    if not data:break
                    if line_counter ==0:
                        part2=data.split(",")
                    else :
                        count2.append(data.split(","))

                    line_counter +=1

            number1 = []
            number2 = []
            year = []
            count1 = [item for sublist in count1 for item in sublist]
            count2 = [item for sublist in count2 for item in sublist]

            number1 = count1[1::2]
            number2 = count2[1::2]
            year = count1[0::2]

            number1 = [int(i) for i in number1[:]]
            number2 = [int(i) for i in number2[:]]
            year = [int(i) for i in year[:]]

            df = pd.DataFrame({'Year': year, 'YouthRatio': number1})
            df1 = pd.DataFrame({'Year': year, 'ChildProtectionArea': number2})

            fig = make_subplots(specs=[[{"secondary_y":True}]])

            fig.add_trace(go.Bar(x=df['Year'], y=df['YouthRatio'], name='청소년 비율',  width=0.7, marker_color='#FFF9D0'), secondary_y=False)
            fig.add_trace(go.Scatter(x=df1['Year'], y=df1['ChildProtectionArea'], mode='lines+markers', name='어린이 보호구역', marker=dict(color='#FFA10A', size=20, symbol='circle'),line=dict(width=4)),secondary_y=True)

            fig.update_layout(
                xaxis_title='연도',
                yaxis_title='비율 또는 면적'
            )
            fig.update_layout(width=680, height=380,margin=dict(t=50,b=0,l=0,r=0))
            fig.update_layout(legend=dict(traceorder='normal', orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1))
            fig.update_yaxes(title_text="강서구 거주 인구 중 청소년 비율(%)", secondary_y=False, range=[min(number1)-10, max(number1)+10])
            fig.update_yaxes(title_text="어린이 보호구역(개)", secondary_y=True, range=[70, 120])
            st.plotly_chart(fig,use_container_width=True)

    elif selected_page == "초/중/고 위치":
            st.markdown(
                    """
                    <style>
                    width:50px; 
                    margin-right:5px;
                    margin-bottom:10px;">
                    </style>
                    <h5> 강서구 내 학교 종류별 숫자 </h5>
                    """
                    , 
                    unsafe_allow_html=True)
            data = pd.read_csv('./csv/school.csv',encoding='utf-8',engine='python')

            i=0
            schoolType=[]

            for i in range(len(data)):
                schoolType+=[data.loc[i, '학교종류명']]

            i=0
            element=[]
            middle=[]
            high=[]
            etcs=[]
            colors = ['#FFA617','#FFB43B','#FAE173','#FCF4BD']
            for i in range(len(schoolType)):
                if schoolType[i]=='초등학교':
                    element+=[schoolType[i]]
                elif schoolType[i]=='중학교':
                    middle+=[schoolType[i]]
                elif schoolType[i]=='고등학교':
                    high+=[schoolType[i]]
                else:
                    etcs+=[schoolType[i]]
            
            SchoolType=['초등학교','중학교','고등학교','특수/기타']
            DataSet=[len(element),len(middle),len(high),len(etcs)]
            df= pd.DataFrame({'Category':SchoolType,'Value':DataSet,'Colors':colors})

            fig=px.bar(df,x='Category',y='Value',color='Colors', color_discrete_sequence=colors,text='Value')
            fig.update_layout(width=1200, height=380,margin=dict(t=50,b=0,l=0,r=0))
            fig.update_layout(
                xaxis_title='학교 구분',
                yaxis_title='학교 수',
                legend_title='학교 구분'
                )
            fig.data[0].name = '초등학교'
            fig.data[1].name = '중학교'
            fig.data[2].name = '고등학교'
            fig.data[3].name = '특수/기타학교'
            fig.update_traces(textposition='outside', textfont=dict(color='black'))
            fig.update_layout(legend=dict(traceorder='normal', orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1))
            st.plotly_chart(fig,use_container_width=True)
            
def dataframe(selected_page):
    if selected_page=="cctv":
        refined_data = pd.read_csv('./csv/cctvFinal.csv')
        df=pd.DataFrame(refined_data)
        st.dataframe(df,width=1200,height=283)
    elif selected_page=="교통량":
        refined_data = pd.read_csv('./csv/trafficSeoulGangseo.csv')
        df=pd.DataFrame(refined_data)
        st.dataframe(df,width=1200,height=283)   
    elif selected_page =="어린이 사고":
        count=[]
        with open('./csv/childrenAccidentBar_df.csv', 'r', encoding='utf-8') as csvList:
            while 1:
                data=csvList.readline()
                if not data:break
                count.append(data.split(","))
        count = [item for sublist in count for item in sublist]
        col = count[0:2]
        year= count[2::2]
        count = count[3::2]

        df=pd.DataFrame({'사고 연도':year,'사고 수':count})
        df['사고 연도'] = df['사고 연도'].str.replace(',', '').astype(str)
        df['사고 수'] = df['사고 수'].str.replace(',', '').astype(float)
        st.dataframe(df,width=1200,height=283)

    elif selected_page =="어린이 보호구역":
        count=[]
        with open('./csv/gs_ChildrenTotal_df.csv', 'r', encoding='utf-8') as csvList:
            while 1:
                data=csvList.readline()
                if not data:break
                count.append(data.split(","))
        count = [item for sublist in count for item in sublist]
        col = count[0:3]
        year= count[3::3]
        count2=count[4::3]
        count = count[5::3]

        df=pd.DataFrame({'연도 구분':year,'거주 청소년 비율':count2,'어린이 보호구역 수':count})
        df['연도 구분'] = df['연도 구분'].str.replace(',', '').astype(str)
        df['어린이 보호구역 수'] = df['어린이 보호구역 수'].str.replace(',', '').astype(float)
        df['거주 청소년 비율'] = df['거주 청소년 비율'].str.replace(',', '').astype(float)
        st.dataframe(df,width=1200,height=283)
        
    elif selected_page =="초/중/고 위치":
        refined_data = pd.read_csv('./csv/schoole_count.csv')
        df=pd.DataFrame(refined_data)
        st.dataframe(df,width=1200,height=283)

def set_custom_css(): #사이트 전체 css 적용(건들지 마셈!)
    st.set_page_config(page_title="강서구 교통환경 시각화", page_icon="🚌", layout="wide")

    with open("./style.css", "r") as f:
        css_content = f.read()

    st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
    st.markdown(''' <style> 
@import url("https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@700&display=swap"); 
div[class^='block-container'] { padding-top: 0px; }

[data-testid="stSidebarNav"] {
    font-family:'IBM Plex Sans KR', sans-serif;
    font-size: 20px;
    background-image: url(https://i.imgur.com/SKTE40H.png);
    background-repeat: no-repeat;
    background-position: 45px 45px;
    background-size:auto;
    padding-top: 185px;
    margin-top: auto;

}
[data-testid="stSidebarNav"]::before {
    content: "Created by ©HFCREW";
    margin-left: 117px;
    margin-top: 0px;
    background-position: 100px 100px;
    font-size: 10px;
    position: relative;
    top: 88px;
}

[data-testid='stIFrame'] {
                width:100%;
                height:680px;
                object-fit: contain;
}

@media (max-width: 400px) {
[data-testid='stIFrame']  {
    height: 350px;
  }
}


 </style>''', unsafe_allow_html=True)
# 사용자 지정 CSS 설정 적용
set_custom_css()

selected_page = sidebar()


main_header()
st.divider()


col1, col2_and_col3 = st.columns([1.0, 0.8])  
with col1:  
    load_folium_map(selected_page)

    
with col2_and_col3: 
    plotly(selected_page)

    dataframe(selected_page)

