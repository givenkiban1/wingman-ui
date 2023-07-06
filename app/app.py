import streamlit as st
import requests
import pandas as pd
import time
import pyautogui

def clear_page():
    pyautogui.hotkey("ctrl","F5")

st.title('Wingman prediction')

st.divider()

# st.snow()

input_file = st.file_uploader("Upload a CSV file", type=(['csv']), accept_multiple_files=False, on_change=clear_page)

if input_file is not None:
    # To read file as bytes:
    bytes_data = input_file.getvalue()

    # print(bytes_data)

    var_s = bytes_data.decode('utf-8')

    var_s = var_s.strip('\n')

    data = var_s.split('\n')

    data_obj = {}
    data_keys = data[0].split(',')
    data_numeric = data[1].split(',')

    for index, key in enumerate(data_keys):
        data_obj[key] = [data_numeric[index]]



    df = pd.DataFrame(data_obj)

    df


def predict():
    with loading:
        time.sleep(5)
    st.success('Done!')


st.button('Make prediction', disabled=input_file is None, on_click=predict)


loading = st.spinner('Making prediction...')

st.button('Reset', on_click=clear_page)

# param1 = st.slider('Select a number', 1, 15, 3)

# param2 = st.slider('Select another number', 1, 15, 3)

# url = os.environ.get('API_URI') + '/predict'

# params = {
#     'feature1': param1,  # 0 for Sunday, 1 for Monday, ...
#     'feature2': param2
# }
# response = requests.get(url, params=params)

# st.text(response.json())
