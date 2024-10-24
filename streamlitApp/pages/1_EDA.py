import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

st.set_page_config()


# BAR SIDE

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""
st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

# INTRODUDCTION

st.title("EDA")
st.markdown('''
            eda
            ''')

# LOAD DATA

course_df = pd.read_csv('../data/course.csv')
ratings_df = pd.read_csv('../data/ratings.csv')

#=============================== WORD CLOUD
st.header('WordCloud')

with st.expander("See code"):
    code = '''
    titles = " ".join(title for title in course_df['TITLE'].astype(str))
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(stopwords=stopwords, 
                        background_color="green", 
                        width=800, 
                        height=400)
    wordcloud.generate(titles)
    '''
    st.code(code, language="python")

st.image("../data/wordcloud.png")


#=================================== Courses Genrer
st.header('Courses Genres')
expander = st.expander("See explanation")

with st.expander('See code'):
    code='''
    import plotly.express as px
    dummy = course_df[course_df.columns[3:]].sum(axis=0).sort_values(ascending=False)
    dummy = pd.DataFrame({'gender': dummy.index, 'count':dummy.values})
    fig = px.bar(dummy, x='gender', y='count')
    '''
    st.code(code, language='python')
    
import plotly.express as px
dummy = course_df[course_df.columns[3:]].sum(axis=0).sort_values(ascending=False)
dummy = pd.DataFrame({'gender': dummy.index, 'count':dummy.values})
fig = px.bar(dummy, x='gender', y='count')
st.plotly_chart(fig)

#==================================  COURSE ENROLLMENTS
dummy = ratings_df.groupby(by='user').size().to_frame(name='enrolls').reset_index()
fig =  px.histogram(
                dummy,
                x='enrolls',
                marginal="box",
                #nbins=int((dummy.max()-dummy.min())/int(np.log2(dummy.shape[0]+1)))
                )
st.header('Course enrollments')
with st.expander('See code'):
    st.code('''
            dummy = ratings_df.groupby(by='user').size().to_frame(name='enrolls').reset_index()
            fig =  px.histogram(
                            dummy,
                            x='enrolls',
                            marginal="box",
                            #nbins=int((dummy.max()-dummy.min())/int(np.log2(dummy.shape[0]+1)))
                            )
            ''', language='python')
st.plotly_chart(fig)
        


# ====================================  TOP POPULAR COURSES
st.header('Top popular courses')

order_by = st.selectbox('order by:', ('rating','size'))
number = st.number_input(
    "number of columns showed", value=20, placeholder="Type a number...", max_value=20
)

with st.expander('See code'):
    st.code(
        '''
        dummy = ratings_df.groupby(by=['item']).agg({'item':'size', 'rating':'mean'}).rename(columns={'item':'size'}).reset_index()
        dummy = dummy.rename(columns={'item':'COURSE_ID'})
        dummy = pd.merge(
                        left = dummy,
                        right = course_df[['COURSE_ID','TITLE']],
                        on = 'COURSE_ID', 
                        how='left'
                        )
        st.dataframe(dummy.sort_values(by=order_by, ascending=False).reset_index(drop=True).head(number))
        fig = px.bar(dummy.sort_values(by='size', ascending=False).reset_index(drop=True).head(number), x='TITLE', y=order_by,text_auto='.2s')
        st.plotly_chart(fig)
        ''',
        language='python'
    )

dummy = ratings_df.groupby(by=['item']).agg({'item':'size', 'rating':'mean'}).rename(columns={'item':'size'}).reset_index()
dummy = dummy.rename(columns={'item':'COURSE_ID'})
dummy = pd.merge(
                left = dummy,
                right = course_df[['COURSE_ID','TITLE']],
                on = 'COURSE_ID', 
                how='left'
                )

st.dataframe(dummy.sort_values(by=order_by, ascending=False).reset_index(drop=True).head(number))
fig = px.bar(dummy.sort_values(by='size', ascending=False).reset_index(drop=True).head(number), x='TITLE', y=order_by,text_auto='.2s')
st.plotly_chart(fig)



