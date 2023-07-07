import streamlit as st
import requests
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns
import os
# from pydantic import BaseModel, Field

url = os.environ.get('API_URI') + '/predict'


def clear_page():
    # pyautogui.hotkey("ctrl","F5")
    pass

st.title('Wingman prediction')

data_ready = False
resp_data = None

prediction = None
# st.divider()

input_file = st.file_uploader("Upload a CSV file", type=(['csv']), accept_multiple_files=False, on_change=clear_page)

if input_file is not None:

    # To read file as bytes:
    bytes_data = input_file.getvalue()

    # print(bytes_data)

    var_s = bytes_data.decode('utf-8')

    var_s = var_s.strip('\n')
    var_s = var_s.strip('\r')

    data = var_s.split('\n')

    data = [x.strip('\r') for x in data]



    data_keys = data[0].split(',')
    data_numeric = data[1].split(',')

    data = {
        'field_names': data_keys[1:],
        'values': data_numeric[1:]
    }

    # st.write(data)
    # print(data)

else:
    data_ready = False
    resp_data = None

st.button('Reset', on_click=clear_page)




if st.button('Make prediction', disabled=input_file is None):
    response = requests.post(url, json=data)


    with st.spinner('Making prediction...'):
        time.sleep(3)


    resp_data = response.json()

    # st.write(resp_data)


    st.text('Prediction : ' + resp_data['prediction'])


    subcat_legend = {
        1: "Handling",
        2: "Systems",
        3: "Structural",
        4: "Propeller",
        5: "Power Plant",
        6: "Oper/Perf/Capability",
        7: "Fluids / Misc Hardware"
    }

    subcat_labels = [val for key, val in subcat_legend.items()]

    st.text('Probability of each subcategory')

    proba = resp_data['proba']

    plt.pie(
        proba[0],
        labels=subcat_labels,
        explode=(0, 0, 0, 0, 0, 0, 0),
        autopct='%1.1f%%',
        startangle=90,
        pctdistance=1.15,
        labeldistance=1.3,
        colors=sns.color_palette("Accent", 7)
        )

    center_circle = plt.Circle((0, 0), 0.75, fc='white')
    prob_fig = plt.gcf()
    prob_fig.gca().add_artist(center_circle)

    plt.axis('equal')

    st.pyplot(prob_fig)
