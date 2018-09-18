from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
import nmap
import subprocess
import networkx
import plotly.plotly as py
import plotly.graph_objs as go
import networkx as nx

class DeviceManager(Screen):

    def get_neighbors(self):
        output = subprocess.Popen(["nmap", "-sP", "192.168.0.*"], stdout=subprocess.PIPE)
        netView = output.stdout.read().decode('utf-8')
        macs = []
        ips = []
        for line in netView.split('\n'):
            if 'MAC Address' in line:
                mac = line.split(': ', 1)[1]
                mac = mac.split('\r', 1)[0]
                macs.append(mac)
        print(macs)
        for mac in macs:
            self.topology.add_widget(Label(text="MAC: " + mac))

        for line in netView.split('\n'):
            if 'Nmap scan report' in line:
                ip = line.split('r ', 1)[1]
                ip = ip.split('\r', 1)[0]
                ips.append(ip)
        print(ips)
        for ip in ips:
            self.topology.add_widget(Label(text="IP: " + ip))


        #Create network topology
        G = nx.random_geometric_graph(len(ips), 0.125)
        pos = nx.get_node_attributes(G, 'pos')

        dmin = 1
        ncenter = 0
        for n in pos:
            x,y=pos[n]
            d=(x-0.5)**2+(y-0.5)**2
            if d<dmin:
                ncenter=n
                dmin=d

        p = nx.single_source_shortest_path_length(G,ncenter)

        edge_trace = go.Scatter(
            x=[],
            y=[],
            line=dict(width=0.5, color='#888'),
            hoverinfo='none',
            mode='lines')

        for edge in G.edges():
            x0, y0 = G.node[edge[0]]['pos']
            x1, y1 = G.node[edge[1]]['pos']
            edge_trace['x'] += tuple([x0, x1, None])
            edge_trace['y'] += tuple([y0, y1, None])

        node_trace = go.Scatter(
            x=[],
            y=[],
            text=[],
            mode='markers',
            hoverinfo='text',
            marker=dict(
                showscale=True,
                colorscale='YLGnBu',
                reversescale=True,
                color=[],
                size=10,
                colorbar=dict(
                    thickness=15,
                    title='Your Home Network',
                    xanchor='left',
                    titleside='right',
                ),
            line=dict(width=2)))

        for node in G.nodes():
            x, y = G.node[node]['pos']
            node_trace['x'] += tuple([x])
            node_trace['y'] += tuple([y])

        for node, adjacencies in enumerate(G.adjacency()):
            node_trace['marker']['color']+=tuple([len(adjacencies[1])])
            node_info = '# of connections: ' + str(len(adjacencies[1]))
            node_trace['text']+=tuple([node_info])

        fig = go.Figure(data=[edge_trace, node_trace],
                        layout=go.Layout(
                            title='<br>Your Home Network',
                            titlefont=dict(size=16),
                            showlegend=False,
                            hovermode='closest',
                            margin=dict(b=20,l=5,t=40),
                            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

        py.plot(fig, filename='networkx')