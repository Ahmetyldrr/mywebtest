from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H4('İris Dataset Deneme Grafik.'),
    dcc.Graph(id="scatter-plot"),
    html.P("Filter by petal width:"),
    dcc.RangeSlider(
        id='range-slider',
        min=0, max=2.5, step=0.1,
        marks={0: '0', 2.5: '2.5'},
        value=[0.5, 2]
    ),
])


@app.callback(
    Output("scatter-plot", "figure"), 
    Input("range-slider", "value"))
def update_bar_chart(slider_range):
    df = px.data.iris() # replace with your own data source
    low, high = slider_range
    mask = (df['petal_width'] > low) & (df['petal_width'] < high)
  
    fig = px.scatter(
        df[mask], x="sepal_width", y="sepal_length", 
        color="species", size='petal_width', 
        hover_data=['petal_length'])


  
    return fig


datam = [{

"A":1,
  "B":2,
  "C":3
  
}]

print(datam)

if __name__ == '__main__': 
    app.run_server(host='0.0.0.0',debug=True)