import streamlit as st
import requests
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns
# import pyautogui

def clear_page():
    # pyautogui.hotkey("ctrl","F5")
    pass

st.title('Wingman prediction')

# st.divider()

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

    # creating a dictionary with keys and values
    for index, key in enumerate(data_keys):
        data_obj[key] = [data_numeric[index]]



    df = pd.DataFrame(data_obj)

    df


def predict():
    with loading:
        time.sleep(3)
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


# ADV
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

# Placeholder till the actual proba is returned from the api call
proba = [[
    0.68633303,
    15.64000318,
    2.4907375 ,
    2.78677454,
    16.5781061 ,
    53.05815674,
    8.75988892
    ]]

plt.pie(
    proba[0],
    labels=subcat_labels,
    explode=(0, 0, 0, 0, 0, 0.05, 0),
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
