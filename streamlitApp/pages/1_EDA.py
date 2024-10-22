import streamlit as st

st.set_page_config(layout="wide")


markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""
st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)



st.title("EDA")
st.markdown('''
            - Identify keywords in course titles using a **WordCloud**
            - Calculate the summary statistics and visualizations of the online course content dataset
            - Determine **popular course genres**
            - Calculate the summary statistics and create visualizations of the online course **enrollment** dataset
            - Identify courses with the greatest number of enrolled students
            
            - Prepare data for more analysis
            - BoW
            ''')



