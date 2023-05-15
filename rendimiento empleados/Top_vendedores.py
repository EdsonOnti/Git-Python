# Importamos las librerías necesarias
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Conectamos con la base de datos
conn=sqlite3.connect("Base_datos.db")
# Definimos la consulta SQL para obtener los top vendedores
querry1=('''    
SELECT LastName || " " || FirstName AS FName, ROUND(sum(dinerxproduc)) AS VOLUMEN

FROM (SELECT e.LastName,e.FirstName,od.ProductID,sum(od.Quantity)AS ProductxIDyEmploy,p.Price*(sum(od.Quantity)) AS dinerxproduc
				
FROM Employees e, Orders o 
INNER JOIN OrderDetails od ON o.EmployeeID=e.EmployeeID AND od.OrderID=o.OrderID 
INNER JOIN Products p ON p.ProductID=od.ProductID
GROUP BY od.ProductID , e.EmployeeID)
GROUP BY FName
ORDER BY VOLUMEN DESC

''')
# Ejecutamos la consulta y almacenamos el resultado en un DataFrame
resultado=pd.read_sql_query(querry1,conn)
print(resultado)

# Graficamos los datos en un diagrama de barras
ax=resultado.plot(x='FName',y='VOLUMEN',kind='bar',figsize=(7,4),color='#FFDEAD',legend=False,grid=True)
plt.title('Top vendedores')
# Cambiamos el color de las barras de los tres mejores vendedores
ax.patches[0].set_color('#7CFC00')
ax.patches[1].set_color('#7CFC00')
ax.patches[2].set_color('#7CFC00')
# Agregamos el título del gráfico, etiquetas de los ejes y rotación de las etiquetas del eje x
plt.xlabel('FNames')
plt.ylabel('VOLUMEN')
plt.xticks(rotation=45)
# Mostramos el gráfico
plt.show()





