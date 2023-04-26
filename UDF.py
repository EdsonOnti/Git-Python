# Siempre para trabajar con sql se importan estas 2 librerias

import sqlite3
import pandas as pd

#Para trabajar la udf con sqlite3 , tenemos que definirlas en python y despues conectarlas a sql
square=lambda n: n*n

#En lugar de abrir y cerrar los conn/cursor, optimizaremos con: "whit"
with sqlite3.connect("db_northwind.db") as conn: #Conectamos la base (esta en la misma carpeta) y generamos la variable conn
#Conectamos la funcion antes ya creada en python , con la variable de coneccion
    conn.create_function('square',1,square) #parametors("nombre"/#parametros/"funcion en py")
#Conectamos un cursor para poder hacer querrys en python de sql 
    cursor=conn.cursor()
#Empezamos a hacer transacciones con el cursor ya conectado( El begin, ya viene implicito)
    cursor.execute('''
       SELECT *,square(price) FROM Products            
                   
                   '''
        )
#Guardamos los resultados de la transaccion(En este caso es una simple consulta, con una aplicacion de funcion)
    results=cursor.fetchall()
#Lo transformamos en Data Frame, para poder visualizarlo mejor e imprimimos
    result_df=pd.DataFrame(results)
    
    
print(result_df)
#Si queremos que todo se ejecute sin tener cambios, escribimos el commit(Solo si estamos 100% seguros)



#conn=sqlite3.connect("db_northwind.db")
#conn.create_function('square',1,square)

#cursor=conn.cursor()
#cursor.execute(
#'''SELECT * FROM Products'''
#)
#results=cursor.fetchall()
#results_df=pd.DataFrame(results)

#cursor.close()
#conn.close()

#print(results_df)



