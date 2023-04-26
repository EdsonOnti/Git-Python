import sqlite3 
import pandas as pd
import matplotlib.pyplot as plt

#Top 10 productos mas vendidos

conn=sqlite3.connect('db_northwind.db')

querry=('''
    SELECT ProductName, SUM(Price * Quantity) AS Revanue
    FROM OrderDetails od 
    JOIN Products p ON od.ProductID=p.ProductID 
    GROUP BY p.ProductID
    ORDER BY Revanue DESC
    LIMIT 10
    ''')

result=pd.read_sql_query(querry,conn)
print(result)

ax=result.plot(x='ProductName',y='Revanue',kind='bar',color='r', figsize=[7,3],legend=False, grid=True)
plt.title('Top 10 productos')
ax.patches[0].set_color('green')
plt.xlabel('ProductName')
plt.ylabel('Revanue')
plt.tick_params(axis='x', which='major', labelsize=8)
plt.xticks(rotation=45)
plt.show()

