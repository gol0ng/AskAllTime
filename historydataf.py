import sqlite3
from datetime import datetime
import pytz

def now_time():
    # 获取当前UTC时间
    utc_now = datetime.now(pytz.utc)

    # 选择时区，例如 'Asia/Shanghai' 代表中国上海时区
    timezone = pytz.timezone('Asia/Shanghai')

    # 将UTC时间转换为指定时区的时间
    local_time = utc_now.astimezone(timezone)
    return local_time.strftime("%Y-%m-%d %H:%M:%S")




# 连接到SQLite数据库（如果数据库不存在，则会自动创建）
conn = sqlite3.connect('askalltime.db')

# 创建一个游标对象
cursor = conn.cursor()
# 创建一个表
cursor.execute('''CREATE TABLE IF NOT EXISTS history
                  (id INTEGER PRIMARY KEY, question TEXT, answer TEXT, time TIMESTAMP)''')
# 关闭连接
conn.close()

def add_history(question, answer):
    conn = sqlite3.connect('askalltime.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO history (question, answer, time) VALUES (?, ?, ?)", (question, answer,now_time()))
    conn.commit()
    last_id = cursor.lastrowid
    conn.close()
    return last_id

def get_history():
    # 连接到SQLite数据库（如果数据库不存在，则会自动创建）
    conn = sqlite3.connect('askalltime.db')

    # 创建一个游标对象
    cursor = conn.cursor()
    # 查询数据
    cursor.execute("SELECT * FROM history ORDER BY time DESC ")
    rows = cursor.fetchall()
    items = []
    for row in rows:
        id = row[0]
        question = row[1][:10]
        answer = row[2][:20]
        time = row[3]
        item = {'question': question, 'answer': answer, 'time': time,'id':id}
        items.append(item)
    # 关闭连接
    conn.close()
    return items

def history_detail(hid:int):
    # 连接到SQLite数据库（如果数据库不存在，则会自动创建）
    conn = sqlite3.connect('askalltime.db')
    # 创建一个游标对象
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history WHERE id=?", (hid,))
    row = cursor.fetchone()
    if row:
        question = row[1]
        answer = row[2]
        time = row
        return {'question': question, 'answer': answer, 'time': time}
    return None



