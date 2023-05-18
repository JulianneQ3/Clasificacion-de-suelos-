#Importación de paquetes

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path as mpath
from scipy.interpolate import interp1d
import io
import base64

pasa=[100, 95, 84, 65, 45, 25, 10, 0]

tamiz=['4.75','2','0.850','0.425','0.250','0.150','0.075','Fondo']
abertura = [4.75,2,0.850,0.425,0.250,0.150,0.075,0]


def curva_granulometrica():

    #Calcular D60 D30 D10

    #Se grafica la línea de la granulometría
    plt.figure(figsize=(14, 4)) 
    plt.plot(abertura,pasa,linestyle='-', marker='o', color='k', fillstyle='none',label='Data') 
    f = interp1d(pasa, abertura)
    #valores de entrada
    y1_coord = 60
    y2_coord = 30
    y3_coord = 10
    #Realiza interpolación
    x1_coord = f(y1_coord)
    x2_coord = f(y2_coord)
    x3_coord = f(y3_coord)
    #Solo toma dos decimales
    x1_formatted = '{:.2f}'.format(x1_coord)
    x2_formatted = '{:.2f}'.format(x2_coord)
    x3_formatted = '{:.2f}'.format(x3_coord)

    #------------------------------------------------------------

    #Los ubica en el plano
    plt.scatter(x1_coord, y1_coord, marker='s', s=50, color='k', label='D60='+x1_formatted)
    plt.scatter(x2_coord, y2_coord, marker='<', s=50, color='k', label='D30='+x2_formatted)
    plt.scatter(x3_coord, y3_coord, marker='>', s=50, color='k', label='D10='+x3_formatted)

    #Grafica
    plt.title("",fontsize=10)
    plt.xlabel('Diámetro (mm)')
    plt.ylabel('Porcentaje pasa acumulado (%)')
    plt.title('Curva granulométrica')
    plt.legend() 
    plt.xscale("log")
    plt.xlim(0.075,4.75)
    plt.ylim(0,100) 
    plt.grid(color='k',lw='0.1',ls='-')

    #se agregan más grillas
    ax1 = plt.gca()
    ax1.invert_xaxis()

    # Agregar el segundo eje x para los nombres de los tamices
    ax2 = ax1.twiny()
    ax2.set_xscale('log')
    ax2.set_xticks(abertura)
    ax2.set_xticklabels(tamiz, rotation=90, fontsize=8)

    # Agregar linas de los tamices
    ax2.set_xlabel('Tamices')
    ax2.set_xlim(0.075,4.75)
    ax2.invert_xaxis()

    #agregamos nombre lineas verticales
    L_No10 = ([4.75,4.75]) 
    L_No20 = ([2,2]) 
    L_No40 = ([0.850,0.850]) 
    L_No60 = ([0.425,0.425])
    L_No140 = ([0.106,0.106])  
    L_rango = ([0,100])

    #se indicca en el plot la ubicación de estas líneas
    plt.plot(L_No10, L_rango, color='grey', lw='0.8', ls='--')
    plt.plot(L_No20, L_rango, color='grey', lw='0.8', ls='--') 
    plt.plot(L_No40, L_rango, color='grey', lw='0.8', ls='--')
    plt.plot(L_No60, L_rango, color='grey', lw='0.8', ls='--')
    plt.plot(L_No140, L_rango, color='grey', lw='0.8', ls='--')

    #se agrega textos
    plt.text(4.75, 2, 'Grava(Fina)', fontsize=8, rotation=90)
    plt.text(1.95, 2, 'Arena(Gruesa)', fontsize=8, rotation=90)
    plt.text(0.415, 2, 'Arena(Mediana)', fontsize=8, rotation=90)
    plt.text(0.075, 2, 'Arena(Fina)', fontsize=8, rotation=90)

    x_values = [4, 3, 2, 1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.09, 0.08]
    for x in x_values:
        plt.axvline(x=x, color='grey', ls='-', lw='0.3')

    # Guardar la figura en un objeto BytesIO

    fig_buffer_ = io.BytesIO()
    plt.savefig(fig_buffer_, format='png')
    plt.close()

    fig_buffer_.seek(0)

    encoded_image_ = base64.b64encode(fig_buffer_.getvalue()).decode()

    # Crear la figura HTML con Dash
    return encoded_image_
