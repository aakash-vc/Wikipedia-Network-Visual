import pandas as pd
import networkx as nx
from pyvis.network import Network


class Process:

    def __init__(self):
        pass

    def get_connections(self, lst):
        res = []
        for i in range(len(lst)-1):
            res.append([lst[i].split('/')[-1].replace('_', " "), lst[i+1].split('/')[-1].replace('_', " ")])

        df =  pd.DataFrame(res, columns=['From', 'To'])
        df['Weight'] = 1
        return df

    def merge_dataframes(self, df):
        old_df = pd.read_csv('data/connections.csv')
        new_df = pd.concat([old_df, df])

        df = new_df.drop_duplicates(subset=['From', 'To'], keep='last')
        #df = df.sort_values(by='From', ignore_index=True)

        return df

    def get_graph(self, df, physics):
        Graph = nx.from_pandas_edgelist(df, 'From', 'To', 'Weight')
        wiki_net = Network(height='600px', width='100%', font_color='black')
        wiki_net.force_atlas_2based()

        if physics:
            wiki_net.show_buttons(filter_=['physics'])

        wiki_net.from_nx(Graph)
        
        path = 'html-files'
        wiki_net.save_graph(f'{path}/wiki_graph.html')
        HtmlFile = open(f'{path}/wiki_graph.html', 'r', encoding='utf-8')

        return HtmlFile

    def clean(self):
        open('data/connections.csv', 'w').close()