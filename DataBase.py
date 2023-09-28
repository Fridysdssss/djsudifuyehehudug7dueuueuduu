import sqlite3 as sq
import Config as cfg

conn=sq.connect('DataBase.DB',check_same_thread=False)
cur=conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS user(
            ID INT,
            Balance INT
)''')

#Есть ли юзер  в базе данных None=Нету Не None=Есть
def usersID(message):
    userID=cur.execute(f'SELECT ID FROM user WHERE ID={message.from_user.id}').fetchone()
    return userID

def Balance(message):
    if usersID(message)==None:
        print(1)
        cur.execute(f'INSERT INTO user(id,balance) VALUES ({message.from_user.id},{cfg.default_valute})')
        conn.commit()
        Balancs=cfg.default_valute
        return Balancs
    else:
        print(2)
        Balances=cur.execute(f'SELECT Balance FROM user WHERE ID={message.from_user.id}').fetchone()[0]
        print(Balances)
        return Balances
    
def give(message):
    cur.execute(f'UPDATE user SET Balance={int(str(message.text).split()[2])} WHERE id={int(str(message.text).split()[1])}')
    conn.commit()