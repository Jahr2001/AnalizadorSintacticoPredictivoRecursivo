#alter table Usuario alter column idUsuario AUTO_INCREMENT ;
# S --> ALTER TABLE ID ALTER COLUMN ID TIPO PCOMA
# ALTER --> alter
# TABLE --> table
# COLUMN --> column
# ID --> LETRA ID
# LETRA --> a…z | A…Z
# TIPO --> TINYINT |INTEGER | VARCHAR | BLOB | DATETIME | NULL | AUTO_INCREMENT
# PCOMA --> ;

def ALTER(texto):
    if texto == "alter" or texto == "ALTER":
        return True
    return False

def TABLE(texto):
    if texto == "table" or texto =="TABLE":
        return True
    return False

def COLUMN(texto):
    if texto == 'column' or texto == "COLUMN":
        return True
    return False

def ID(texto):
    if texto.isalpha():
        return True
    return False

def TIPO(texto):
    if (texto == "TINYINT") or (texto == "INTEGER") or (texto == "VARCHAR") or (texto == "BLOB") or (texto == "DATETIME") or (texto == "NULL") or (texto == "AUTO_INCREMENT"):
        return True
    return False

def PCOMA(texto):
    if texto == ";":
        return True
    return False

def validar(cadenaTexto):
    texto = cadenaTexto.split(' ')
    if len(texto) == 8:
        alter = ALTER(texto[0])
        if alter:
            print(alter)
            table = TABLE(texto[1])
            if table:
                print(table)
                id = ID(texto[2])
                if id:
                    print(id)
                    alter = ALTER(texto[3])
                    if alter:
                        print(alter)
                        column = COLUMN(texto[4])
                        if column:
                            print(column)
                            id = ID(texto[5])
                            if id:
                                print(id)
                                tipo = TIPO(texto[6])
                                if tipo:
                                    print(tipo)
                                    pcoma = PCOMA(texto[7])
                                    if pcoma:
                                        print(pcoma)
                                        print('SENTENCIA CORRECTA')
                                        return True
    return False




# validar('alter table Usuario alter column idUsuario AUTO_INCREMENT ;')



