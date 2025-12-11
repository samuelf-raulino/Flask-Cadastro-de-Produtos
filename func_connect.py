import sqlite3

DB = "database.db"

def inserir_camiseta(nome, tamanho, cor, modelo):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    sql = "INSERT INTO camiseta (nome, tamanho, cor, modelo) VALUES (?, ?, ?, ?)"
    cursor.execute(sql, (nome, tamanho, cor, modelo))
    conn.commit()
    cursor.close()
    conn.close()
    print("camiseta inserida")


def retornar_camiseta(id=0):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    if id == 0:
        cursor.execute("SELECT * FROM camiseta")
    else:
        cursor.execute("SELECT * FROM camiseta WHERE id = ?", (id,))

    resultado = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultado


def editar_camiseta(nome, tamanho, cor, modelo, id):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE camiseta SET nome=?, tamanho=?, cor=?, modelo=? WHERE id=?",
        (nome, tamanho, cor, modelo, id)
    )
    conn.commit()
    cursor.close()
    conn.close()

def deletar_camiseta(id):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM camiseta WHERE id = ?",(id,))
    conn.commit()
    cursor.close()
    conn.close()
deletar_camiseta(1)