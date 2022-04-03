#Dado el sistema de masas presentado en la figura, realizar un programa en lenguaje de programación Python compuesto por una clase que tenga los siguientes métodos: 
#1. calcular_movimiento(), que dado un ángulo θ, un coeficiente de rozamiento µ y una masa m1; genere una lista cuyos elementos sean listas de dos elementos que contengan en el primer valor la masa m2 y en el segundo valor la dirección de movimiento de m2. El valor de la masa m2 inicia en 0 kg y debe aumentar en 0.5Kg hasta que m2 empiece a caer. 
#2. calcular_angulo(), que dada una masa m1, una masa m2 y un coeficiente de rozamiento µ; retorne el valor del ángulo en que el sistema estaría en equilibrio. Si con los valores dados el sistema no entra en equilibrio para ningún ángulo entonces la función retorna el valor de -1. Los valores del ángulo deben variar desde 10 a 85 grados. 
import math 

def calcular_movimiento(angulo,coef_roza,masa1):
    
    datos=[]
    subdatos=[]
    subiendo="subiendo"
    bajando="bajando"
    masa2=0
    booleanoprueba=True
    valor=angulo*math.pi/180
    valor2=masa1*((math.sin(valor))-(coef_roza*math.cos(valor)))
    
    while booleanoprueba:
        if masa2<valor:
            subdatos.append(masa2)
            subdatos.append(subiendo)
        else:
            subdatos.append(masa2)
            subdatos.append(bajando)      
        datos.append(subdatos)
        subdatos=[]
        if masa2>valor2:
            booleanoprueba=False
        masa2+=0.5
    return datos
            
            

    
def calcular_angulo(coef_roza,masa1,masa2):
    resp=-1
    valor=10
    valorfinal=0
    
    for i in range (75):
        valorfinal=round(masa1*9.8*(coef_roza*math.cos(math.radians(i+valor))-math.sin(math.radians(i+valor)))+masa2*9.8)
        if valorfinal==0:
             resp=i+valor
             break
    return resp


class main:
    angulo=0
    coef_razo=0
    masa1=0
    print(calcular_movimiento(55,0.15,6))
    print(calcular_angulo(0.15,6,4.5))