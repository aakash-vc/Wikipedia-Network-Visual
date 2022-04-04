import os
import streamlit as st
import streamlit.components.v1 as components
from googlesearch import search
from scripts import Crawl,Process

def display():
    st.title('Wiki Connect')
    topic = st.text_input('Enter Topic Name or Wikipedia URL')
    physics = st.checkbox('Add physics interavtivity')

    if not topic == '':
        if not topic.startswith('https://'):
            query = 'wikipedia ' + topic

            for i in search(query, num=1, stop=1):
                topic = i
        
        print(f'URL: {topic}')
        lst = Crawl().input_url(topic)
        df = Process().get_connections(lst)

        if not os.stat('data/connections.csv').st_size == 0:
            df = Process().merge_dataframes(df)
        df.to_csv('data/connections.csv', index=False)

        HtmlFile = Process().get_graph(df, physics)

        components.html(HtmlFile.read(), height=1200, width=1000)

    #if st.button('Clear Data'):
        #Process().clean()

if __name__ == '__main__':
    display()

