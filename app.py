import dash
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


#import fronted
from fronted.main import layout

#import backend
from backend.cartaplasticidad import cartaPlasticidad
from fronted.izquierda.izquierda import *
from backend.curva_granulometrica import *
from fronted.derecha.derecha import *

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

#
app.layout = layout

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Actualizar la imagen en intervalos regulares
@app.callback(
    dash.dependencies.Output('graph-image', 'src'),
    dash.dependencies.Input('interval', 'n_intervals')
)
def update_graph_image(n):
    return 'data:image/png;base64,{}'.format(image_base64)


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#calculamos la carta de plasticidad
@app.callback(Output('editing-prune-data-output', 'children'),
              Input('editing-columns', 'data'))
def display_output(columns):
    pruned_columns = []
    for i in range(500):  # Iterar sobre todas las columnas dinámicas
        pruned_column = []
        for row in columns:
            if row.get(i) != '':
                pruned_column.append(row.get('ensayo-{}'.format(i)))
        pruned_columns.append(pruned_column)
    
    limite_liquido = []
    indice_plasticidad = []
    
    for column in pruned_columns:
        if len(column) >= 9:
            limite = column[8]
            indice = column[9]
            
            if limite is not None and limite != 'None':
                limite = int(limite.strip("'"))
                limite_liquido.append(limite)
    
            if indice is not None and indice != 'None':
                indice = int(indice.strip("'"))
                indice_plasticidad.append(indice)
    
    encoded_image = cartaPlasticidad(limite_liquido, indice_plasticidad)
    image_element = html.Img(src="data:image2/png;base64,{}".format(encoded_image))
    
    return html.Div([image_element], style={'text-align': 'center'})

if __name__ == '__main__':
    app.run_server(debug=True)
