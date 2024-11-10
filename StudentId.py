from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# 학생 이름과 학번 CSV 파일 로드
df = pd.read_csv("학생이름_학번v2.csv")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        search_value = request.form.get("search_value")
        # 학번을 이용하여 검색
        if search_value.isdigit():
            found = df[df['학번'] == int(search_value)]
        else:
            found = df[df['이름'] == search_value]

        if not found.empty:
            result = f"학번: {found.iloc[0]['학번']}, 이름: {found.iloc[0]['이름']}, 납부 여부: {found.iloc[0]['납부여부']}"
        else:
            result = "해당 정보를 찾을 수 없습니다."

    return render_template("index.html", result=result)

# Lambda로 실행할 수 있도록 설정
if __name__ == "__main__":
    app.run(debug=True)


# C:/Users/C-GD/anaconda3/python.exe c:/Users/C-GD/Desktop/Flask_py-20241108T034417Z-001/Flask_py/StudentInfo/StudentId.py
