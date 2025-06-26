import streamlit as st
import pandas as pd

st.title("lab1")
url = "https://raw.githubusercontent.com/myoh0623/dataset/refs/heads/main/student-mat.csv"
df = pd.read_csv(url)

# 성별 평균 성적 비교(G3 컬럼은 성적을 나타낸다)
st.subheader("1. 성별에 따른 평균 최종 성적 (G3 컬럼)")
gender_score = df.groupby("sex")["G3"].mean()

st.bar_chart(gender_score)


# 공부 시간별 평균 성적 을 bar chart로 studytime 컬럼으로 groupby 
st.subheader("2. 공부 시간별 평균 최종 성적 (G3 컬럼)")
study_time_avg = df.groupby("studytime")["G3"].mean()

st.bar_chart(study_time_avg)

# walc(주말 알콜 섭취) 에 따른 평균 성적 을 bar chart로
st.subheader("3. Walc(주말 알콜 섭취) 에 따른 평균 성적")
walc_time_avg = df.groupby("Walc")["G3"].mean()

st.bar_chart(walc_time_avg)