from dash import html, dcc
import dash_bootstrap_components as dbc


#import fronted
from fronted.navegador.navegador import navegador
from fronted.derecha.derecha import derecha
from fronted.izquierda.izquierda import izquierda

layout = dbc.Container(
    [
        dbc.Row(
        [
            dbc.Col(navegador, md=12, style={'background-color':'red'}),
            dbc.Col(izquierda, md=6, style={'background-color':'blue'}),
            dbc.Col(derecha, md=6, style={'background-color':'green'}),
        ]
        )
    ]
)