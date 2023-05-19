import dash
from dash import dcc, html, Input, Output
import dash_table

app = dash.Dash(__name__)

# Define una lista vacía para almacenar los datos ingresados
datos = []

# Define la tabla inicial con una columna vacía
tabla = dash_table.DataTable(
    id='tabla-dinamica',
    columns=[{'name': '', 'id': 'columna'}],
    data=[{'columna': ''}],
    editable=True
)

# Define el layout de la aplicación
app.layout = html.Div([
    html.H1('Tabla Dinámica'),
    tabla,
])

# Define la función de callback para capturar los cambios en la tabla
@app.callback(
    Output('tabla-dinamica', 'data'),
    Input('tabla-dinamica', 'data_timestamp'),
    Input('tabla-dinamica', 'data'),
)
def actualizar_tabla(timestamp, data):
    global datos

    # Comprueba si se han realizado cambios en la tabla
    if timestamp is not None:
        # Obtiene los valores ingresados por el usuario en la última columna
        nueva_columna = [row['columna'] for row in data]

        # Agrega los nuevos valores a la lista de datos
        datos.append(nueva_columna)

    return data

if __name__ == '__main__':
    app.run_server(debug=True)