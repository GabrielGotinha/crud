import mysql.connector

conexao =  mysql.connector.connect(
    host='localhost',   
    user='root',
    password='',
    database='py',
)

cursor = conexao.cursor()

#nome = "todynho"
#valor = 2
valor = 6
nome = "todynho"

#comando = f'INSERT INTO vendas (nome, valor) VALUES ("{nome}", {valor})'
#comando = f'SELECT * FROM vendas;'
comando = f'UPDATE vendas SET valor = {valor} WHERE nome = "{nome}"'

cursor.execute(comando)
conexao.commit() # editando banco de dados
#resultado = cursor.fetchall() #ler banco de dados
#print(resultado)

cursor.close()
conexao.close()