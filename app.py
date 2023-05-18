import dash
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import math
import time
from dash import Dash

#import fronted
from fronted.main import layout

#import backend
from backend.cartaplasticidad import cartaPlasticidad
from backend.tablatamices import *

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

#
app.layout = layout

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#desarrollamos la tabla de tamices

@app.callback(
    Output("table", "columns"),
    Output("table", "data"),
    Input("add-btn", "n_clicks"),
    prevent_initial_call=True,
)

def add_column(n_clicks):
    if n_clicks > 0:
        df_product.insert(len(df_product.columns), str(n_clicks), 0)
        return (
            [
                {"name": "Tamiz", "id": "tamiz", "editable": False},
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
                    for col in df_product.columns[1:]
                ],
            ],
            df_product.to_dict("records"),
        )

    return no_update
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#calculamos la curva granulométrica
@app.callback(
    Output('salidaCurvaGranulometrica', 'children'),
    Input('pasa', 'value'),
    Input('abertura', 'value')
)

def curvaGranulometrica():
    #retrasar la página un segundo
    # time.sleep(1)
    encoded_image_ = curvaGranulometrica()

    image_element = html.Img(src="data:image/png;base64,{}".format(encoded_image_))
 
    return html.Div([image_element])



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#calculamos la carta de plasticidad
@app.callback(
    Output('salidaCartaPlasticidad', 'children'),
    Input('Limite_liquido', 'value'),
    Input('Indice_plasticidad', 'value')
)

def cartaPlasticidadDash(Limite_liquido, Indice_plasticidad):
    #retrasar la página un segundo
    # time.sleep(1)
    encoded_image, messages = cartaPlasticidad(Limite_liquido, Indice_plasticidad)

    image_element = html.Img(src="data:image/png;base64,{}".format(encoded_image))
    messages_element = html.Label(messages)

    return html.Div([image_element, messages_element])


if __name__ == '__main__':
    app.run_server(debug=True)
