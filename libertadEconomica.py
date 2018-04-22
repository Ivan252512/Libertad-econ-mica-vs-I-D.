import numpy as np
import csv
import math
import matplotlib.pyplot as plt

'''Convierte un csv en un array.'''
def csvToArray(csvNombre):
    array=[]
    with open(csvNombre, newline='') as File:
        for row in csv.reader(File):
            array.append(np.asarray(row))
    return np.asarray(array)

PIB=csvToArray("Datos/API_NY.GDP.PCAP.PP.CD_DS2_en_csv_v2.csv")
iMasD=csvToArray("Datos/API_GB.XPD.RSDV.GD.ZS_DS2_en_csv_v2.csv")
libertadEconomica=csvToArray("Datos/index2014_data.csv")

'''Limpia los datos de iMasD, regresa un arreglo con el nombre de cada país y
el valor de inversión en porcentaje del PIB de cada país.'''
def paisesIMasDLimpios(iMasD):
    paisesIMasD2014=[]
    for i in range(len(iMasD)-5):
        if (iMasD[i+5][59]!=''):
            paisesIMasD2014.append([iMasD[i+5][0],iMasD[i+5][59]])
    return np.array(paisesIMasD2014)

'''Limpia los datos de iMasD, regresa un arreglo con el nombre de cada país y
el valor del PIB de cada país.'''
def paisesPIBPerCapitaLimpios(PIB):
    paisesPIB=[]
    for i in range(len(PIB)-5):
        if(PIB[i+5][59]!=''):
            paisesPIB.append([PIB[i+5][0],PIB[i+5][59]])
    return np.array(paisesPIB)

'''Limpia los datos de iMasD, regresa un arreglo con el nombre de cada país y
el valor del índice de libertad económica de cada país.'''
def paisesLibertadEconomicaLimpios(libertadEconomica):
    paisesLibertadEconomica2014=[]
    for i in libertadEconomica[1:]:
        if (i[6]!='N/A'):
            paisesLibertadEconomica2014.append([i[1],i[6]])
    return paisesLibertadEconomica2014

'''Compara el nombre del país entre los arreglos que recibe, sí el nombre está
en los tres arreglos, agrega el nombre del país, el valor de su iMásD per cápita
y su índice de libertad económica, regresa estos tres parámetros.'''
def comparaPorNombre(paisesIMasD,paisesLibertadEconomica,paisesPIB):
    nombre=[]
    iMasD=[]
    libertad=[]
    for i in paisesIMasD:
        for j in paisesLibertadEconomica:
            for h in paisesPIB:
                if(i[0]==j[0]==h[0]):
                    #Agrega el nombre
                    nombre.append(i[0])
                    #Multiplica el porcentaje de inversión del PIB en iMasD por
                    # el PIB per capita por 100, agregando el iMasD per capita.
                    iMasD.append(float(i[1])*float(h[1])/100)
                    #Agrega el valor del índice de libertad económica.
                    libertad.append(float(j[1]))
                    break
    return nombre,iMasD,libertad

paises=comparaPorNombre(paisesIMasDLimpios(iMasD),
      paisesLibertadEconomicaLimpios(libertadEconomica),
      paisesPIBPerCapitaLimpios(PIB))

#Gráfica.
fig=plt.figure(figsize=(15,7.5))
ax = fig.add_subplot(111)
plt.scatter(paises[2],paises[1])
#Etiqueta los puntos con los nombres su respectivo país.
for i in range(len(paises[0])):
    ax.annotate(paises[0][i], xy=(paises[2][i],paises[1][i]),
                xytext=(paises[2][i],paises[1][i]),
                arrowprops=dict(facecolor='black'),
                )
#Etiqueta a México.
plt.scatter(paises[2][42],paises[1][42],color='red',label='Mexico')
ax.annotate(paises[0][42], xy=(paises[2][42],paises[1][42]),
            xytext=(paises[2][42],paises[1][42]),
            arrowprops=dict(facecolor='red'),
            )
plt.legend(loc=2)
plt.title('Research and development expenditure '+
          'vs  Index of economic freedom 2014')
plt.xlabel(' Index of economic freedom [0-100]')
plt.ylabel('Research and development expenditure per capita [$USD]')
plt.savefig('i+d',dpi=400)


#Gráfica HD.
fig=plt.figure(figsize=(40,20))
ax = fig.add_subplot(111)
plt.scatter(paises[2],paises[1])
#Etiqueta los puntos con los nombres su respectivo país.
for i in range(len(paises[0])):
    ax.annotate(paises[0][i], xy=(paises[2][i],paises[1][i]),
                xytext=(paises[2][i],paises[1][i]),
                arrowprops=dict(facecolor='black'),
                )
#Etiqueta a México.
plt.scatter(paises[2][42],paises[1][42],color='red',label='Mexico')
ax.annotate(paises[0][42], xy=(paises[2][42],paises[1][42]),
            xytext=(paises[2][42],paises[1][42]),
            arrowprops=dict(facecolor='red'),
            )
plt.legend(loc=2)
plt.title('Research and development expenditure '+
          'vs  Index of economic freedom 2014')
plt.xlabel(' Index of economic freedom [0-100]')
plt.ylabel('Research and development expenditure per capita [$USD]')
plt.savefig('i+dHD',dpi=400)
