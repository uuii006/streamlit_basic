import streamlit as st

# st.title('카운터 예제 : session_state 활용')
# count = 0
# if st.button('증가'):
#     count += 1

# st.write('count=', count)

# session_state 사용
if 'count' not in st.session_state:
    st.session_state.count = 0

def increase():
    st.session_state.count += 1
st.button('증가', on_click=increase)

def decrease():
    st.session_state.count -= 1
st.button('감소', on_click=decrease)

st.write('count=', st.session_state.count)