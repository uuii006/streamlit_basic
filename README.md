# streamlit_delpoy_ex
Practice deploying on Streamlit Cloud

## 환경설정
```
conda create -n streamlit_dashdb python=3.13 -y
conda activate streamlit_dashdb
pip install -r requirements.txt
```

## 필요한 라이브러리 설치
```
pip install streamlit numpy maptplotlib folium streamlit-folium pandas wordcloud sqlalchemy pymysql plotly
```

## 패키지 기록
```
pip freeze > requirements.txt
```
예시 `requirements.txt`
```
streamlit
numpy
pandas
sqlalchemy
pymysql
plotly
```

## 프로젝트 폴더 구조
```
Streamlit_Basic/
│
├─ app.py
├─ requirements.txt
├─ README.md
│
├─ data/
│  ├─ kor_news_260318-0319.xlsx
│  ├─ 경기도인구데이터.xlsx
│  └─ 경기도행정구역경계.json
│
├─ img/
│  ├─ apple.png
│  ├─ banana.png
│  └─ mango.png
│
└─ pages/
   ├─ 1_text_elements.py
   ├─ 2_data_elements.py
   ├─ 3_column_congis.py
   ├─ 4_charts.py
   ├─ 5_INput_widgets.py
   ├─ 6_Layout_sidbar.py
   ├─ 7_Layout_contaner.py
   ├─ 8_Layout_tab_etc.py
   ├─ 9_session.py
   └─ 10_caching_ex_주문관리.py
```

