import pandas as pd
datos = pd.read_csv("homicidios.csv")

# sql_insert="create table if not exists homicidios(\n"

# for i in datos.columns:
#     sql_insert=sql_insert+i+" text,\n"
# sql_insert=sql_insert[0:-2]
# sql_insert=sql_insert+");"  

# print(sql_insert)

sql_datos_cabecera="insert into homicidios ("
for i in datos.columns:
    sql_datos_cabecera = sql_datos_cabecera + i + ","

sql_datos_cabecera = sql_datos_cabecera[0:-1]

sql_datos_cabecera = sql_datos_cabecera + ") VALUES ("


def return_insert(values):
    txt_data = ""
    for i in values:
        if str(i) == "nan":
            txt_data = txt_data + "\'\',"
        else:
            txt_data = txt_data + "\'" + str(i) + "\'," 

    return txt_data


SQL_FINAL = ""
for indice, fila in datos.iterrows():
    txt = return_insert(fila.values)
    txt = txt[0:-1]

    SQL_FINAL = SQL_FINAL + sql_datos_cabecera + txt + ");\n"


with open("sql.sql", "w", encoding="UTF-8") as f:
    f.write(SQL_FINAL)