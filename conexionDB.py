import pymysql # importe de la libreria pymysql
db = pymysql.connect("localhost", "root", "", "colegio")# conexion a la DB pymysql.connect es una instancia del objeto db
cursor = db.cursor()# crear el cursor
consulta = ("INSERT INTO estudiantes VALUES(10105555,'PEPITO','PEREZ',11, 7);")# consulta almacenada en consulta 
print(consulta)# impresion de la consulta 
cursor.execute(consulta) # guardar la consulta
db.commit()# enviar la , se ejecuta la consulta 
db.close()# cerrar la conexion a la base de datos 