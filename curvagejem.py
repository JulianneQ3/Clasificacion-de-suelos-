import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
from scipy.interpolate import interp1d
from dash import html

# Datos de ejemplo
abertura = [0.075, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 4.75]
pasa = [0, 8, 20, 45, 65, 80, 90, 95, 98, 100, 100, 100]
tamiz = ['No.200', 'No.70', 'No.40', 'No.30', 'No.25', 'No.20', 'No.16', 'No.14', 'No.12', 'No.10', 'No.4', '3"', '2"', '1 1/2"', '1"']

# Realiza interpolación
f = interp1d(pasa, abertura)
y_coords = [60, 30, 10]
x_coords = [float('{:.2f}'.format(f(y))) for y in y_coords]

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    fluid=True,
    children=[
        html.H1("Curva granulométrica"),
        dbc.Row(
            [
                dbc.Col(
                    dbc.FormGroup(
                        [
                            dbc.Label("D60"),
                            dbc.Input(
                                id="d60",
                                type="number",
                                value=y_coords[0],
                                min=0,
                                max=100,
                                step=1,
                            ),
                        ]
                    ),
                    width=4,
                ),
                dbc.Col(
                    dbc.FormGroup(
                        [
                            dbc.Label("D30"),
                            dbc.Input(
                                id="d30",
                                type="number",
                                value=y_coords[1],
                                min=0,
                                max=100,
                                step=1,
                            ),
                        ]
                    ),
                    width=4,
                ),
                dbc.Col(
                    dbc.FormGroup(
                        [
                            dbc.Label("D10"),
                            dbc.Input(
                                id="d10",
                                type="number",
                                value=y_coords[2],
                                min=0,
                                max=100,
                                step=1,
                            ),
                        ]
                    ),
                    width=4,
                ),
            ],
            align="center",
            style={"margin-bottom": "20px"},
        ),
        dbc.Row(
            dbc.Col(
                dcc.Graph(id="granulometry-graph"),
                width={"size": 10, "offset": 1},
            ),
        ),
    ],
)


@app.callback(
    dash.dependencies.Output("granulometry-graph", "figure"),
    [
        dash.dependencies.Input("d60", "value"),
        dash.dependencies.Input("d30", "value"),
        dash.dependencies.Input("d10", "value"),
    ],
)
def update_graph(d60, d30, d10):
    y_coords = [d60, d30, d10]
    x_coords = [float('{:.2f}'.format(f(y))) for y in y_coords]

    trace_d60 = {
        "x": x_coords[0],
        "y": y_coords[0],
        "mode": "markers",
        "marker": {"symbol": "square", "size": 10},
        "name": "D60",
    }
    trace_d30 = {
    "x": x_coords[1],
    "y": y_coords[1],
    "mode": "markers",
    "marker": {"symbol": "triangle-left", "size": 10},
    "name": "D30",
    }
    trace_d10 = {
        "x": x_coords[2],
        "y": y_coords[2],
        "mode": "markers",
        "marker": {"symbol": "triangle-right", "size": 10},
        "name": "D10",
    }

    return {
        "data": [
            {"x": abertura, "y": pasa, "mode": "lines+markers", "name": "Data"},
            trace_d60,
            trace_d30,
            trace_d10,
        ],
        "layout": {
            "title": "",
            "xaxis": {"type": "log", "title": "Diámetro (mm)"},
            "yaxis": {"title": "Porcentaje pasa acumulado (%)"},
            "legend": {"x": 1, "y": 1},
            "hovermode": "closest",
            "width": 800,
            "height": 400,
            "margin": {"l": 50, "r": 20, "t": 70, "b": 50},
            "plot_bgcolor": "#f9f9f9",
            "paper_bgcolor": "#f9f9f9",
            "grid": {"color": "lightgray", "dash": "solid"},
        },
    }


if __name__ == "__main__":
    app.run_server(debug=True)

