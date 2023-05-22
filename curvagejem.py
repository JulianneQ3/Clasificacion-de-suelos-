import dash
import dash_html_components as html
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Definir los datos de entrada y realizar la interpolación
abertura = [0.075, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 4.75]
pasa = [0, 8, 20, 45, 65, 80, 90, 95, 98, 100, 100, 100]

f = interp1d(pasa, abertura)

y1_coord = 60
y2_coord = 30
y3_coord = 10

x1_coord = f(y1_coord)
x2_coord = f(y2_coord)
x3_coord = f(y3_coord)

x1_formatted = '{:.2f}'.format(x1_coord)
x2_formatted = '{:.2f}'.format(x2_coord)
x3_formatted = '{:.2f}'.format(x3_coord)

# Crear la figura y agregar los elementos gráficos
fig, ax = plt.subplots(figsize=(14, 4))

ax.plot(abertura, pasa, linestyle='-', marker='o', color='k', fillstyle='none', label='Data')

ax.scatter(x1_coord, y1_coord, marker='s', s=50, color='k', label='D60=' + x1_formatted)
ax.scatter(x2_coord, y2_coord, marker='<', s=50, color='k', label='D30=' + x2_formatted)
ax.scatter(x3_coord, y3_coord, marker='>', s=50, color='k', label='D10=' + x3_formatted)

ax.set_xlabel('Diámetro (mm)')
ax.set_ylabel('Porcentaje pasa acumulado (%)')
ax.set_title('Curva Granulométrica')
ax.legend()
ax.set_xscale("log")
ax.set_xlim(0.075, 4.75)
ax.set_ylim(0, 100)
ax.grid(color='k', lw='0.1', ls='--')

# Convertir la figura en una imagen HTML
import io
import base64
buffer = io.BytesIO()
plt.savefig(buffer, format='png')
plt.close(fig)
buffer.seek(0)
image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

# Crear la aplicación Dash y definir el layout
app = dash.Dash(__name__)
app.layout = html.Div([
    html.Img(src='data:image/png;base64,{}'.format(image_base64))
])

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)

