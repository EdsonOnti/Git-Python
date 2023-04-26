#cantidad de segundos dado un tiempo en horas, min y segundos

def segundos(n=None):
    if n is None:
        n=int(input('Tienpos a ingresar: '))
    list=[]
    for i in range (n):
        h=int(input("Ingresa las horas del tiempo "+str(i+1) +":  "))
        m=int(input("Ingresa los minutosdel tiempo "+str(i+1) +":  "))
        s=int(input("Ingresa los segundosdel tiempo "+str(i+1) +":  "))
        print('El '+ str(i+1)+'°'+ ' tiempo en segundos es: '+str(3600*h + 60*m + s)) 
        r=(3600*h + 60*m + s) 
        list.append(r)
    return list



def h_m_s(n=None):
    if n is None:
        n=int(input("Introduce los segundo: "))
    h=int(n/3600)
    m=int((n%3600)/60)
    s=(n%3600)%60
    return (h,m,s)
#print(h_m_s(10801))

#Leer dos tiempos en hms y sumarlas , devolverlas en hms

def sum2tiempos():
    print('Ingresa solo 2 tiempos a calcular')
    t1,t2=segundos(2)
    r_seg=t1+t2
    r_horas=h_m_s(r_seg)
    return r_horas
#print(sum2tiempos())


def palindromo(str=None):
    if str is None:
        str=(input('Escribe una palabra para verificar'))
    n=(len(str))
    str1=''
    lista=[]
    for i in range (n):
        r=str[(n-1)-i]
        lista.append(r)
    for letra in lista:
        str1 += letra 
    if str1 == str:
        print(f'{str} Es un palindromo')
    else: 
        print(f'{str} No es palindromo')
#(palindromo('coloco'))


def max_producto(lista=None):
    if lista is None:
        lista=[]
        for i in range(4):
            n=int(input('Ingresa el '+str(i+1)+'° numero:'))
            lista.append(n)
    n1,n2,n3,n4=lista
    resulta=max(n1*n2,n1*n3,n1*n4,n2*n3,n2*n4,n3*n4)
    return resulta


def max_producto1(lista=None):
    if lista is None:
        while True:
            n=input('Escribe aqui 4 digitos separados por un espacio')
            lista=[int(num) for num in n.split()]
            if len(lista)==4:
                break
            else:
                print('Escribe 4 digitos separados por espacio')
    max_producto=max([lista[i]*lista[j]for i in range(len(lista)) for j in range(i,len(lista)) if j>i])
    return max_producto
print(max_producto1())
        