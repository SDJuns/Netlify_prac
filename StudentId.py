import pandas as pd
import streamlit as st

# CSV 파일 경로
CSV_FILE_PATH = 'csvfolder/data'

# 데이터 불러오기
def load_data(file_path):
    return pd.read_csv(file_path)

# 학회비 납부 여부 확인 함수
def check_fee_status(student_id, data):
    result = data[data['학번'].astype(int) == int(student_id)]
    if not result.empty:
        return f"{student_id}님은 납부하셨습니다."
    else:
        return "학회비를 납부하지 않았습니다."

# Streamlit 앱 시작
st.title('학회비 납부 여부 확인 프로그램')

# 학번 입력 받기
student_id = st.text_input('학번을 입력하세요:')

if st.button('확인하기'):
    if student_id:
        data = load_data(CSV_FILE_PATH)
        status = check_fee_status(student_id, data)
        st.write(status)
    else:
        st.write("학번을 입력해주세요.")
# C:/Users/C-GD/anaconda3/python.exe c:/Users/C-GD/Desktop/Flask_py-20241108T034417Z-001/Flask_py/StudentInfo/StudentId.py
