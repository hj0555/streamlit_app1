import streamlit as st
import pandas as pd

st.title("lab1")
url = "https://github.com/myoh0623/dataset/blob/main/student-mat.csv"
df = pd.read_csv(url)

# 성별 평균 성적 비교(G3 컬럼은 성적을 나타낸다)
st.subheader("1. 성별에 따른 평균 최종 성적 (G3 컬럼)")
gender_score = df.groupby("sex")["G3"].mean()

st.bar_chart(gender_score)

# 공부 시간별 평균성ㅈ적을 bar chart로 study time 컬럼으로 group by
st.subheader("2. 공부 시간별 평균 성적")
study_score = df.groupby("studytime")["G3"].mean()

# walc 주말알콜섭취 에 따른 평균 성적을 bar chart로
st.subheader("2. 주말 알콜 섭취에 따른 평균 성적")
walc_score = df.groupby("Walc")["G3"].mean()