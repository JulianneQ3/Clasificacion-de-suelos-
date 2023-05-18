from dash import html, dcc
import dash_bootstrap_components as dbc

#importar componentes de la parte derecha
from .graficas.curva_granulometrica import curva_granulometrica
from .graficas.cartaplasticidad import cartaplasticidad

derecha = dbc.Container(
    [
        dbc.Row(
        [
            dbc.Col(curva_granulometrica, md=12, style={'background-color':'skyblue'}),

            html.Hr(),

                html.Div(
                [
                    html.Label('pasa'),
                   
                    html.Label('abertura'),
                                      
                    html.Div(id='salidaCurvaGranulometrica')
                ]
                ),

            dbc.Col(cartaplasticidad,md=12, style={'background-color':'gray'}),

            
            html.Hr(),

            html.Div(
            [
                html.H2('Indice de plasticidad '),
                html.Label('Limite liquido '),
                dcc.Slider(
                    id='Limite_liquido',
                    min=0,
                    max=100,
                    value=55,
                    step=1,
                    marks={i: str(i) for i in range(0, 101, 10)}
                ),
                html.Label('Indice de plasticidad'),
                dcc.Slider(
                    id='Indice_plasticidad',
                    min=0,
                    max=60,
                    value=20,
                    step=1,
                    marks={i: str(i) for i in range(0, 61, 10)}
                ),

                # dcc.Input(id = 'Limite_liquido', value = 55 , type = 'number'),
                # dcc.Input(id = 'Indice_plasticidad', value = 5 , type = 'number'),
                html.Div(id='salidaCartaPlasticidad')
            ]
            ),
        ]
        )     
    ]
)