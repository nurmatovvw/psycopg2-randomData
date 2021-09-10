import psycopg2 as psy
import random as rd
from datas import *
# num = rd.randint(0, 10)
# print (num)
# password = input('Password for data base: ')
Connection = psy.connect(
    database = 'citizens',
    user = 'postgres',
    password = 'kh01052006',
    host = 'localhost',
    port = '5432'
)

cursor = Connection.cursor()

password = []
emails = []
phone_numbers = []
addresses = []
followers = tuple(rd.randint(1, 1000)for i in range(500))
# print (followers)

for name in logins:
    email = name + domains[rd.randint(0, len (domains)-1)]
    emails.append(email)
# print (emails)

# for i in range(500):
#     pswrd = ''
#     for p in range(rd.randint(8, 15)):
#         pswrd += pswd_symbols[rd.randint(0, len(pswd_symbols)-1)]
#         if len(pswrd)>=8:
#             password.append(pswrd)
#         else:
#             continue
# print (password)


for i in range(500):
    pswrd = ''
    for p in range(rd.randint(8, 15)):
        pswrd += pswd_symbols[rd.randint(0, len(pswd_symbols)-1)]
    password.append(pswrd)

# print (password)



code = ('75','13','55','77','70','84','45','99',)
for num in range(5000):
    number = '+996' + str(code[rd.randint(0, len (code)-1)]) + str(rd.randint(0, 9)) + str(rd.randint(111111, 999999))
    phone_numbers.append(number)
# print (phone_numbers)


for i in range(5000):
    address = streets[rd.randint(0, len(streets)-1)] + " " + str(rd.randint(0, 500))
    addresses.append(address)
# print (addresses)

cursor.execute("""CREATE TABLE users(user_id SERIAL PRIMARY KEY,login VARCHAR(20) NOT NULL,password VARCHAR(100) NOT NULL,
email VARCHAR(100) NOT NULL,
phone_number VARCHAR(20) NOT NULL,
country VARCHAR(50) NOT NULL,
address VARCHAR(50) NOT NULL,
profession VARCHAR(50) NOT NULL,
followers INT NOT NULL
)""")

query = '''insert into users (login, password, email, phone_number, country, address, profession, follower) values '''
for i in range (10000):
    query += f'''(
        '{logins[rd.randint(0, len(logins)-1)]}',
        '{password[rd.randint(0, len(password)-1)]}',
        '{emails[rd.randint(0, len(emails)-1)]}',
        '{phone_numbers[rd.randint(0, len(phone_numbers)-1)]}',
        '{countries[rd.randint(0, len(countries)-1)]}',
        '{addresses[rd.randint(0, len(addresses)-1)]}',
        '{professions[rd.randint(0, len(professions)-1)]}', 
        '{followers[rd.randint(0, len(followers)-1)]}'
    ),'''

sql_query = query[:-1]+';'

cursor.execute(sql_query)
Connection.commit()
cursor.close()
Connection.close()