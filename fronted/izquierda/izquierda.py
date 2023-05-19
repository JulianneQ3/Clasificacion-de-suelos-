from dash import html, dcc
import dash_bootstrap_components as dbc

#importar componentes de la parte derecha
from backend.tablatamices import table

izquierda = dbc.Container(
    [
         dbc.Row(
        [
            dbc.Col('De acuerdo a la cantidad de ensayos realizados en laboratorio, agregue la cantidad de columnas necesarias. Luego ingrese los porcentajes pasa. Recuerde que este código clasifica suelos finos por tanto, debe ingresar también el límite líquido y el indice de plasticidad.', md=12, style={'background-color':'brown'}),
            dbc.Col(table,md=12, style={'background-color':'white'}),
            dbc.Col('conclusiones',md=12, style={'background-color':'orange'})
        ]
        )  
    ]
)