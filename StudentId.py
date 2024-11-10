from flask import Flask, request, render_template
import pandas as pd
import os

app = Flask(__name__)

excel_file_path = "/Users/sindongjun/Flask_py/학생이름_학번v2.csv"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        search_value = request.form['search_value']
        if os.path.exists(excel_file_path):
            df = pd.read_csv(excel_file_path)

            if '학번' not in df.columns or '성명' not in df.columns:
                result = "데이터 파일에 '학번' 또는 '성명' 열이 없습니다."
            else:
                if search_value.isdigit() and int(search_value) in df['학번'].values:
                    student_info = df[df['학번'] == int(search_value)].iloc[0]
                    result = f"{student_info['성명']} {search_value}은 납부자 입니다."
                elif search_value in df['학번'].astype(str).values:
                    student_info = df[df['학번'].astype(str) == search_value].iloc[0]
                    result = f"{student_info['성명']} {search_value}은 납부자 입니다."
                else:
                    result = f"학번 {search_value}님은 납부하지 않으셨습니다."
        else:
            result = "데이터 파일을 찾을 수 없습니다."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)


# C:/Users/C-GD/anaconda3/python.exe c:/Users/C-GD/Desktop/Flask_py-20241108T034417Z-001/Flask_py/StudentInfo/StudentId.py
