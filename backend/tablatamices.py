from dash import Dash, dash_table, html, Input, Output, ctx, no_update
import pandas as pd

product_data = {
    "tamiz": ["4", "8", "10", "20", "40", "100", "200", "FONDO", "LIMITE LIQUIDO", "INDICE DE PLASTICIDAD"],
}

new_column = {"1": [0], "2": [0], "3": [0]}

df_product = pd.DataFrame(product_data)
df_new_column = pd.DataFrame(new_column)

app = Dash(__name__)

title = html.H4("Granulometría", style={"textAlign": "center", "margin": 30})
add_button = html.Button("Agregar ensayo", n_clicks=0, id="add-btn")

table = dash_table.DataTable(
    id="table",
    columns=[
        {
            "name": "Tamiz",
            "id": "tamiz",
            "editable": False,
        },
        *[
            {
                "name": col,
                "id": col,
                "type": "numeric",
                "format": {"specifier": ",.0f"},
                "editable": True,
                "on_change": {"failure": "default"},
                "validation": {"default": 0},
            }
            for col in df_new_column.columns
        ],
    ],
    data=df_product.to_dict("records"),
    row_deletable=False,
)

app.layout = html.Div([title, add_button, table], style={"margin": 30})


