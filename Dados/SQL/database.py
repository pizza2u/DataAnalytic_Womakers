import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('CREATE TABLE gerentes(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefon INT')
#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefon TO telefone')

#cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')

#cursor.execute('DROP TABLE produtos')

#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(1,"Carol","Rua Silvino Lopes","Carolnet@gmail.com",41995146523)')
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(2,"Rodrigo","Rua Edson Ramalho","rodrinet@gmail.com",41995145423)')
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(3,"Ricardo","Rua Primeiro de Maio","ricardnet@gmail.com",41994536523)')
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(4,"Bia","Rua Sei não","bianet@gmail.com",41995454523)')

#cursor.execute('INSERT INTO gerentes(id,nome,endereco,email) VALUES(8,"Cinthia","Paraiba","cinet@gmail.com")')


#cursor.execute('DELETE FROM usuario where id=4')

#cursor.execute('SELECT * FROM usuario')
#vi = cursor.execute('SELECT nome,email FROM usuario')
#vi = cursor.execute('SELECT * FROM usuario WHERE id>2')
#for usuario in vi:
 #   print(usuario)

#cursor.execute('UPDATE usuario SET endereco="Sao Paulo" WHERE nome="Ricardo"')

#ORDER BY E DESC

#vi = cursor.execute('SELECT * FROM usuario ORDER BY nome DESC')

#LIMIT E DISTINCT
#vi = cursor.execute('SELECT * FROM usuario LIMIT 2')
#vi = cursor.execute(' SELECT DISTINCT * FROM usuario')


# GROUP BY e HAVING
#vi = cursor.execute('SELECT nome FROM usuario GROUP BY nome')
#vi = cursor.execute('SELECT nome FROM usuario GROUP BY nome HAVING id>2')

#JOIN
# INNER JOIN
#vi = cursor.execute('SELECT * FROM usuario INNER JOIN gerentes ON usuario.id = gerentes.id')

# LEFT JOIN
#vi = cursor.execute('SELECT * FROM usuario LEFT JOIN gerentes ON usuario.id = gerentes.id')

# RIGHT JOIN
#vi = cursor.execute('SELECT * FROM usuario RIGHT JOIN gerentes ON usuario.id = gerentes.id')

# FULL JOIN
#vi = cursor.execute('SELECT * FROM usuario FULL JOIN gerentes ON usuario.id = gerentes.id')

#SUB CONSULTAS
vi = cursor.execute('SELECT * FROM usuario WHERE nome in (SELECT nome FROM gerentes)')
for usuario in vi:
    print(usuario)

conexao.commit()
conexao.close