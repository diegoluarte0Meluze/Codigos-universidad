import numpy as np
import matplotlib.pyplot as mlp

v_i = np.array([1.0730,1.5370,2.0350,2.5550,3.0840,3.5200,4.0200,4.52000,5.0600,5.5200,6.0300,6.5100,7.0400,7.500,8.000,8.5000,9.0000,9.5000,10.000])#voltaje inicial
print('voltaje inicial o inducido:')
print(v_i)
a = np.array([3.07,3.07,2.97,3.16,3.16,3.15,3.15,3.15,3.16,3.15,3.15,3.15,3.15,3.15,3.15,3.16,3.15,3.15,3.15]) #amperaje
print('Amperaje:')
print(a)
vf=np.array([0.32,0.31,0.33,0.32,0.35,0.36,0.35,0.34,0.32,0.38,0.33,0.30,0.34,0.28,0.34,0.29,0.38,0.28,0.36]) #voltaje final
print('Voltaje final:')
print(vf)
z = np.array([0.04,0.04,0.06,0.05,0.05,0.04,0.03,0.03,0.04,0.06,0.05,0.05,0.04,0.08,0.05,0.07,0.05,0.07,0.05]) #errores voltaje
print('Errores de cada medicion del voltaje:')
print(z)
w = np.array([0.07,0.07,0.17,0.04,0.03,0.04,0.04,0.03,0.04,0.03,0.04,0.04,0.04,0.03,0.05,0.07,0.05,0.07,0.05]) #errores amperaje
print('Errores de cad medicion del amperaje:')
print(w)
def f(x,y):  #funcion Resistencia
    return x/y

def g(x,y,z,w): #errores de las resistencias en particular
    return (x/y**2)*w+(1/y)*z

R= f(vf,a)
print('Resistencia resultante para cada voltaje:')
print(R)

errores = g(vf,a,z,w)
print('Errores de cada resistencia de forma individual:')
print(errores)

ww = 1/(errores**2)

pol = np.polyfit(v_i,R,1,w=1/errores**2)
a0 = pol[0]
a1 = pol[1]

def j(x,y):
    return x - y
residuos = j(a1,R)

Rp = 0.10543130990415336

st1=np.sum((R-0.105)**2)
sr1=np.sum((R-Rp)**2)
r_cuadrado1 = 1-(sr1/st1)
print('coeficiente de determinación usando un promedio preeliminar')
print (r_cuadrado1)

st2=np.sum((R-0.105)**2)
sr2=np.sum((R-v_i*a0-a1)**2)
r_cuadrado2 = 1-(sr2/st2)
print('coeficiente de determinacion usando el ajuste de polyfit:')
print (r_cuadrado2)


print('Valor de la resistencia según el ajuste:')
print(a1)

      

mlp.plot(v_i,R,'.')
mlp.hlines(a1,xmin=v_i[0],xmax=v_i[-1])
mlp.show()
mlp.plot(v_i,residuos,'o')
mlp.show()

