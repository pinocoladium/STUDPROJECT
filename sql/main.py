import psycopg2

name_base = input('Enter your database_name: ')
name = input('Enter your user_name: ')
pas = input('Enter your password: ')

with psycopg2.connect(database=name_base, user=name, password=pas) as conn:
    with conn.cursor() as cur:

        def table_creat(cursor):
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Client (
	        client_id SERIAL PRIMARY KEY,
	        email VARCHAR(40) UNIQUE,
            name VARCHAR(40) NOT NULL,
            surname VARCHAR(40)
            );
            CREATE TABLE IF NOT EXISTS Phone_client (
	        id SERIAL PRIMARY KEY,
	        client_id INTEGER REFERENCES Client(client_id),
	        phone_number VARCHAR(11)
            );
            """)
            conn.commit()
            return 
        
        def table_drop(cursor):
            cursor.execute("""
            DROP TABLE Phone_client;
            DROP TABLE Client;
            """)
            conn.commit()
            return 

        def add_new_client(cursor, email:str, name: str, surname=None, ph_number=None):
            cursor.execute("""SELECT client_id FROM Client WHERE email = %s;""" , (email,))
            check = cursor.fetchone()
            if check == None:
                sql_insert = """INSERT INTO Client (email, name, surname) VALUES(%s, %s, %s);"""
                var = (email, name, surname)
                cursor.execute(sql_insert, var)
                conn.commit()
                if ph_number != None:
                    cursor.execute("""SELECT client_id FROM Client WHERE email = %s;""" , (email,))
                    client_id = [x[0] for x in cursor.fetchall()][0]
                    sql_insert_2 = """INSERT INTO Phone_client (client_id, phone_number) VALUES(%s, %s);"""
                    var_2 = (client_id, ph_number)
                    cursor.execute(sql_insert_2, var_2)
                    conn.commit()
                    return
            else:
                print('The specified client already exists')
                return 

        def add_ph_number_client(cursor, email:str, ph_number):
            cursor.execute("""SELECT client_id FROM Client WHERE email = %s;""" , (email,))
            client_id = [x[0] for x in cursor.fetchall()][0]
            sql_insert = """INSERT INTO Phone_client (client_id, phone_number) VALUES(%s, %s);"""
            var = (client_id, ph_number)
            cursor.execute(sql_insert, var)
            conn.commit()
            return

        def change_info(cursor, old_email: str, new_email=None, new_name=None, new_surname=None, new_ph_number=None):
            cursor.execute("""SELECT client_id FROM Client WHERE email = %s;""" , (old_email,))
            client_id = [x[0] for x in cursor.fetchall()][0]
            if new_email != None:
                cursor.execute("""UPDATE Client SET email=%s WHERE client_id=%s;""", (new_email, client_id))
                conn.commit()
            if new_name != None:
                cursor.execute("""UPDATE Client SET name=%s WHERE client_id=%s;""", (new_name, client_id))
                conn.commit()
            if new_surname != None:
                cursor.execute("""UPDATE Client SET surname=%s WHERE client_id=%s;""", (new_surname, client_id))
                conn.commit()
            if new_ph_number != None:
                cursor.execute("""UPDATE Phone_client SET phone_number=%s WHERE client_id=%s;""", (new_ph_number, client_id))
                conn.commit()
            conn.commit()
            return

        def del_ph_number(cursor, email:str):
            cursor.execute("""SELECT client_id FROM Client WHERE email = %s;""" , (email,))
            client_id = [x[0] for x in cursor.fetchall()][0]
            cursor.execute("""SELECT client_id FROM Phone_client WHERE client_id = %s;""" , (client_id,))
            client_id_2 = [x[0] for x in cursor.fetchall()][0]
            if client_id == client_id_2:
                cursor.execute("""DELETE FROM Phone_client WHERE client_id = %s;""", (client_id,))
                conn.commit()
            return

        def del_client(cursor, email:str):
            cursor.execute("""SELECT client_id FROM Client WHERE email = %s;""" , (email,))
            check = cursor.fetchone()
            if check != None:
                cursor.execute("""SELECT client_id FROM Client WHERE email = %s;""" , (email,))
                client_id = [x[0] for x in cursor.fetchall()][0]
                cursor.execute("""SELECT client_id FROM Phone_client WHERE client_id = %s;""" , (client_id,))
                client_id_2 = [x[0] for x in cursor.fetchall()][0]
                if client_id == client_id_2:
                    cursor.execute("""DELETE FROM Phone_client WHERE client_id = %s;""", (client_id,))
                    conn.commit()
                cursor.execute("""DELETE FROM Client WHERE client_id = %s;""", (client_id,))
                conn.commit()
                return
            else:
                print('The specified client does not exist')
                return

        def search_client(cursor, email=None, name=None, surname=None, ph_number=None):
            if email == None and name == None and surname == None and ph_number == None:
                print('Search information required. Enter data in the client')
                return
            elif email != None:
                cursor.execute("""SELECT c.client_id, email, name, surname, phone_number FROM Client c JOIN \
                Phone_client pc ON c.client_id = pc.client_id WHERE email = %s;""" , (email,))
                client_info = cursor.fetchone()
                print(client_info)
                return
            elif surname != None:
                cursor.execute("""SELECT c.client_id, email, name, surname, phone_number FROM Client c JOIN \
                Phone_client pc ON c.client_id = pc.client_id WHERE surname = %s;""" , (surname,))
                client_info = cursor.fetchone()
                print(client_info)
                return
            elif name != None:
                cursor.execute("""SELECT c.client_id, email, name, surname, phone_number FROM Client c JOIN \
                Phone_client pc ON c.client_id = pc.client_id WHERE name = %s;""" , (name,))
                client_info = cursor.fetchone()
                print(client_info)
                return
            elif ph_number != None:
                cursor.execute("""SELECT c.client_id, email, name, surname, phone_number FROM Client c JOIN \
                Phone_client pc ON c.client_id = pc.client_id WHERE phone_number = %s;""" , (ph_number,))
                client_info = cursor.fetchone()
                print(client_info)
                return

        # result = table_creat(cur)
        # result2 = table_drop(cur)
        # result3 = add_new_client(cur, 'frtyueo@bk.ru', 'Jack')
        # result4 = add_ph_number_client(cur, 'frtyueo@bk.ru', '89222654789')
        # result5 = change_info(cur, 'frtyueo@bk.ru', new_ph_number='89222654790', new_surname='Plint')
        # result5 = del_ph_number(cur, 'frtyueo@bk.ru')
        # result6 = del_client(cur, 'frtyueo@bk.ru')
        # result7 = search_client(cur, email='frtyueo@bk.ru')
        # result8 = search_client(cur, name='Jack')
        # result9 = search_client(cur, surname='Plint')
        # result10 = search_client(cur, ph_number='89222654790')

conn.close()