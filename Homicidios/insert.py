import sqlite3
conn=sqlite3.connect("homicidios.bd")

cursor=conn.cursor()

# SQLa="""
# create table if not exists homicidios(
# ID text,
# Año_del_hecho text,
# Sexo_de_la_victima text,
# Grupo_de_edad_de_la_victima text,
# Mes_del_hecho text,
# Dia_del_hecho text,
# Departamento_del_hecho text,
# Municipio_del_hecho text,
# Lesion_fatal_de_causa_externa text,
# Estado text);
# """
# cursor.execute(SQLa)

SQLb="""
select * from homicidios where Departamento_del_hecho='Caldas' and Municipio_del_hecho='La Dorada';
"""
cursor.execute(SQLb)


# with open("sql.sql", "r", encoding="UTF-8") as f:
#     for i in f.read().split("\n"):
#         cursor.execute(i)
#         conn.commit()

data=cursor.fetchall()
for i in data:
   print(i)