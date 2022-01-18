import dash
import dash_html_components as html
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px


############# RUN APP
app = dash.Dash(__name__,title='DataTown',update_title='Cargando...')
server = app.server


# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# Main
if __name__ == "__main__":
    app.run_server(debug=True)