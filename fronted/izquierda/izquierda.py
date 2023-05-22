import dash_bootstrap_components as dbc
from dash import ctx, no_update
from dash import Dash, dash_table, dcc, html
from dash.dependencies import Input, Output, State
import pandas as pd
from backend.cartaplasticidad import cartaPlasticidad


product_data = {
    "tamiz": ["Num_4", "Num_8", "Num_10", "Num_20", "Num_40", "Num_100", "Num_200", "FONDO", "LIMITE LIQUIDO", "INDICE DE PLASTICIDAD"],
}

df_product = pd.DataFrame(product_data)


diseno = html.Div([
    html.Div([
        dcc.Input(
            id='editing-columns-name',
            placeholder='Enter a column name...',
            value='',
            style={'padding': 10}
        ),
        html.Button('Add Column', id='editing-columns-button', n_clicks=0)
    ], style={'height': 50}),

    html.Div([
        html.Div(
            dash_table.DataTable(
                id='editing-columns',
                columns=[{
                    'name': 'Tamiz',
                    'id': 'tamiz',
                    'editable': False,
                    'renamable': False
                }] + [{
                    'name': 'Ensayo {}'.format(i),
                    'id': 'ensayo-{}'.format(i),
                    'deletable': True,
                    'renamable': True
                } for i in range(0, 50)],
                data=df_product.to_dict("records"),
                editable=True,
            ),
            style={'overflowX': 'auto', 'maxWidth': '100%'}
        )
    ], style={'width': '100%', 'float': 'left'}),

    html.Div(id='editing-prune-data-output', style={'width': '100%', 'float': 'right'}),

    html.Div(style={'clear': 'both'}),

    html.Hr(),
    html.Hr(),
    html.Hr(),

    # Elemento para mostrar el diccionario de la columna 3
    html.Div(id='column-3-data'),
])

izquierda = dbc.Container(
    [
         dbc.Row(
        [
            dbc.Col('De acuerdo a la cantidad de ensayos realizados en laboratorio, agregue la cantidad de columnas necesarias. Luego ingrese los porcentajes pasa. Recuerde que este código clasifica suelos finos por tanto, debe ingresar también el límite líquido y el indice de plasticidad.', md=12, style={'background-color':'brown'}),
            dbc.Col(diseno,md=12, style={'background-color':'white'}),
            dbc.Col('conclusiones',md=12, style={'background-color':'orange'})
        ]
        )  
    ]
)







