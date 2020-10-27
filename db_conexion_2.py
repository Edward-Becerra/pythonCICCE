import pymysql # importe de la libreria pymysql
def saludar(nombre):
    print("Bienvenido ", nombre)

db = pymysql.connect("localhost", "root", "", "colegio")# conexion a la DB pymysql.connect es una instancia del objeto db
cursor = db.cursor()# crear el cursor
sql = "SELECT * FROM estudiantes;"# consulta almacenada en consulta 
cursor.execute(sql) # enviar la consulta
registros = cursor.fetchall() # metodo devolver todo 
nombres=[]
for registro in registros:
    nombres.append(registro[1])
db.close()# cerrar la conexion a la base de datos 
for nombre in nombres:
    saludar(nombre)