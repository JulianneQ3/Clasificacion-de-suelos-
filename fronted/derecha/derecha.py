from dash import html, dcc
import dash_bootstrap_components as dbc

#importar componentes de la parte derecha
from .graficas.curva_granulometrica import *
from .graficas.cartaplasticidad import cartaplasticidad
from backend.curva_granulometrica import *

derecha = dbc.Container(
    [
        dbc.Row(
        [
            dbc.Col(curva_granulometrica, md=12, style={'background-color':'skyblue'}),

            html.Div([
                html.Img(id='graph-image'),
                dcc.Interval(id='interval', interval=5000, n_intervals=0)
            ]),

            dbc.Col(cartaplasticidad,md=12, style={'background-color':'gray'}),

            
            html.Hr(),

            html.Div(
                html.Div([
                html.Div(id='editing-prune-data-output', style={'margin-top': '20px'}),
            ], style={'width': '50%', 'display': 'inline-block', 'vertical-align': 'top'}),
            
            ),
        ]
        )     
    ]
)