import pandas as pd

class Graph:

    def __init__(self):
        pass

    def get_nodes(self, df):
        labels = pd.concat([df['From'], df['To']])
        labels = labels.unique()
        
        nodes = pd.DataFrame(columns=['id', 'label', 'shape', 'size'])
        nodes['id'] = range(1, 1+len(labels))
        nodes['label'] = labels
        nodes['shape'] = 'dot'
        nodes['size'] = 1

        #nodes.to_csv('nodes.csv', index=False)
        #display(nodes)
        return nodes

    def get_edges(self, df, node_df):
        edges = pd.DataFrame()
        edges['source'] = df['From'].map(node_df.set_index('label')['id'].to_dict())
        edges['target'] = df['To'].map(node_df.set_index('label')['id'].to_dict())
        #print(df)
        
        #edges = df[['Source', 'Target']]
        #edges['Type'] = 'Directed'
        edges['Weight'] = 1

        return edges


    def graph(self):
        main_df = pd.read_csv('data/connections.csv')
        nodes_df = self.get_nodes(main_df)
        nodes_df.to_json('data/nodes.json', orient='records', lines=True)

        edges_df = self.get_edges(main_df, nodes_df)
        edges_df.to_json('data/edges.json', orient='records', lines=True)

    