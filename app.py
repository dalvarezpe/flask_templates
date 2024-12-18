from flask import Flask
from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
#rom importlib_resources import path
from importlib.metadata import distribution, PackageNotFoundError

# Crear instancia Flask
server = Flask(__name__)

# Crear instancia Dash
app = Dash(__name__, server=server, url_base_pathname='/dashboard/')

# Datos ficticios basados en gapminder
data = {
    "Country": ["Argentina", "Brazil", "Chile", "Colombia", "Peru"] * 20,
    "Year": list(range(2000, 2020)) * 5,
    "Population": [40 + i * 0.5 for i in range(100)],
    "GDP": [10_000 + i * 100 for i in range(100)],
    "Life Expectancy": [70 + i * 0.1 for i in range(100)],
}
df = pd.DataFrame(data)

# Gráfico 1: Población a través de los años
fig1 = px.line(
    df,
    x="Year",
    y="Population",
    color="Country",
    title="Población a través de los años",
    template="plotly_white",
)

# Gráfico 2: PIB por país
fig2 = px.bar(
    df[df["Year"] == 2019],
    x="Country",
    y="GDP",
    title="PIB por país en 2019",
    template="plotly_white",
    color="GDP",
    color_continuous_scale="Blues",
)

# Gráfico 3: Esperanza de vida por país
fig3 = px.scatter(
    df,
    x="GDP",
    y="Life Expectancy",
    size="Population",
    color="Country",
    title="Esperanza de vida vs. PIB",
    template="plotly_white",
    hover_name="Country",
    log_x=True,
    size_max=60,
)

# Diseño de Dash
app.layout = html.Div(
    [
        html.H1("Dashboard de Gapminder", style={"textAlign": "center"}),
        html.Div(
            [
                dcc.Graph(figure=fig1, style={"width": "48%", "display": "inline-block"}),
                dcc.Graph(figure=fig2, style={"width": "48%", "display": "inline-block"}),
            ]
        ),
        dcc.Graph(figure=fig3, style={"marginTop": "20px"}),
    ],
    style={"padding": "20px"},
)

# Ruta de Flask
@server.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask + Dash</title>
    </head>
    <body>
        <div style="text-align: center; margin-top: 50px;">
            <h1>Bienvenido a la aplicación Flask + Dash</h1>
            <p><a href="/dashboard/">Ir al Dashboard</a></p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run_server(debug=True)
