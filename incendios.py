import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets


#S--> árboles sanos, Q--> árboles quemados, I--> árboles incendiados, alpha --> probabilidad de que un arbol incendiado queme a uno sano, beta --> probabilidad de que el fuego se disipe o no se traspase.


def parametros(viento = 0.2,distancia =0.2,n=100,Si=99,Qi=0,Ii=1,totaltime=400):
    
    num_steps=1600
    h=totaltime/num_steps #pasos para método de Euler ancho de intervalos para dividir el eje x

    S=np.zeros([num_steps+1,1])
    Q=np.zeros([num_steps+1,1])
    I=np.zeros([num_steps+1,1])

    t=np.linspace(0, totaltime, num_steps+1)

#condiciones iniciales 
    
    S[0]=Si
    Q[0]=Qi
    I[0]=Ii
    #Constantes de proporcionalidad
    alpha = viento/distancia
    beta = distancia/viento
    
    for i in range(num_steps):
        F=np.array([[-(alpha/n)*S[i]*I[i]],[(beta/n)*I[i]*(Q[i]+I[i])],[((alpha/n)*S[i]*I[i])-((beta/n)*I[i]*(Q[i]+I[i]))]], dtype="float")
    
        S[i+1]= S[i] + h * F[0]
        Q[i+1]= Q[i] + h * F[1]
        I[i+1]= I[i] + h * F[2]

    #Graficando las soluciones
    plt.figure(figsize=(12,8))
    plt.style.use('fivethirtyeight')
    
    plt.plot(t,S, label="Árboles sanos")
    plt.plot(t,Q, label="Árboles quemados")
    plt.plot(t,I, label="Árboles incendiandose")
    
    plt.title("Modelo de propagación de incendios")
    
    plt.xlabel('Tiempo [horas]')
    plt.ylabel('Número de árboles')
    plt.legend(loc='upper left')

#Widget interactivo    
print('Para la simulación, debemos considerar que:')
print('a =', chr(945) , '=' , 'Tasa de propagación del incendio o rapidez de propagación')
print('b =', chr(946) , '=' , 'Tasa de probabilidad de un árbol de no quemarse el entrar en contacto con un incendiado')
print('n = Número de árboles en total')
print('Si = Árboles sanos iniciales')
print('Qi = Árboles quemados iniciales')
print('ii = Árboles incendiandose iniciales')
print('tsim = Tiempo final de la simulación [Horas]')    
print('Al momento de modificar los parámetros, hay que tener en cuenta la igualdad (I0+S0+E0=n) para que nuestra simulación tenga sentido.')
widgets.interact(parametros,viento=(0,1,0.01),distancia=(0,1,0.01),n=(1,100,100),Si=(0,100,1),Qi=(0,100,1),Ii=(0,100,1),totaltime=widgets.Play(min=1,max=100))
