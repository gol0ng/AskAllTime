import sqlite3

# 连接到SQLite数据库（如果数据库不存在，则会自动创建）
conn = sqlite3.connect('askalltime.db')

# 创建一个游标对象
cursor = conn.cursor()
# 创建一个表
cursor.execute('''CREATE TABLE IF NOT EXISTS ai
                  (id INTEGER PRIMARY KEY, model_nickname TEXT, model_name TEXT, url TEXT,APIkey TEXT, prompt TEXT, is_deleted INTEGER DEFAULT 0, is_default INTEGER DEFAULT 0)''')
# 关闭连接
conn.close()



def delete_model(id):
    # 连接到SQLite数据库（如果数据库不存在，则会自动创建）
    conn = sqlite3.connect('askalltime.db',detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    # 创建一个游标对象
    cursor = conn.cursor()
    cursor.execute("UPDATE ai SET is_deleted=1 WHERE id=?",(id,))
    # 提交事务
    conn.commit()
    # 关闭连接
    conn.close()

def update_model(model_nickname,model_name,url,APIkey,prompt,id):
    # 连接到SQLite数据库（如果数据库不存在，则会自动创建）
    conn = sqlite3.connect('askalltime.db',detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    # 创建一个游标对象
    cursor = conn.cursor()
    cursor.execute("UPDATE ai SET model_nickname=?, model_name=?, url=?, APIkey=?, prompt=? WHERE id=?",(model_nickname,model_name,url,APIkey,prompt,id))
    # 提交事务
    conn.commit()
    # 关闭连接
    conn.close()
def get_default_model():
    # 连接到SQLite数据库（如果数据库不存在，则会自动创建）
    conn = sqlite3.connect('askalltime.db',detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)

    # 创建一个游标对象
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ai WHERE is_default = 1")
    row = cursor.fetchone()
    # 关闭连接
    conn.close()
    return row
def has_available_model():
    # 连接到SQLite数据库（如果数据库不存在，则会自动创建）
    conn = sqlite3.connect('askalltime.db',detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    # 创建一个游标对象
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ai WHERE is_deleted=0")
    rows = cursor.fetchall()
    # 关闭连接
    conn.close()
    if rows:
        return True
    else:
        return False


def set_default_model(id):
    conn = None
    try:
        # 连接到SQLite数据库
        conn = sqlite3.connect('askalltime.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cursor = conn.cursor()

        # 开始事务
        conn.execute("BEGIN")

        # 将所有记录的is_default设置为0
        cursor.execute("UPDATE ai SET is_default=0")
        print(f"Updated all records to is_default=0, rows affected: {cursor.rowcount}")

        # 将特定模型的is_default设置为1
        cursor.execute("UPDATE ai SET is_default=1 WHERE id=?", (id,))
        print(f"Set is_default=1 for model '{id}', rows affected: {cursor.rowcount}")

        # 提交事务
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        if conn:
            # 如果出现错误，回滚事务
            conn.rollback()
    finally:
        # 关闭连接
        if conn:
            conn.close()
def add_model(model_nickname,model_name,url,APIkey,prompt=""):
    # 连接到SQLite数据库（如果数据库不存在，则会自动创建）
    conn = sqlite3.connect('askalltime.db',detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    # 创建一个游标对象
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ai (model_nickname,model_name,url,APIkey,prompt) VALUES (?,?,?,?,?)",(model_nickname,model_name,url,APIkey,prompt))
    # 提交事务
    conn.commit()
    # 关闭连接
    conn.close()
    last_id = cursor.lastrowid
    set_default_model(last_id)
def has_default_model():
    # 连接到SQLite数据库（如果数据库不存在，则会自动创建）
    conn = sqlite3.connect('askalltime.db',detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    # 创建一个游标对象
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ai WHERE is_default=1")
    row = cursor.fetchone()
    # 关闭连接
    conn.close()
    if row:
        return True
    else:
        return False

def get_models_list():
    # 连接到SQLite数据库（如果数据库不存在，则会自动创建）
    conn = sqlite3.connect('askalltime.db',detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    # 创建一个游标对象
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ai WHERE is_deleted=0")
    rows = cursor.fetchall()
    items = []
    for row in rows:
        model_nickname = row[1]
        model_name = row[2]
        url = row[3]
        APIkey = row[4]
        prompt = row[5][:10]
        is_dedefault = row[7]
        id = row[0]
        item = {'model_nickname': model_nickname, 'model_name': model_name, 'url': url, 'APIkey': APIkey, 'prompt': prompt, 'is_default': is_dedefault, 'id':id}
        items.append(item)
    # 关闭连接
    conn.close()
    return items

def get_model(id):
    # 连接到SQLite数据库（如果数据库不存在，则会自动创建）
    conn = sqlite3.connect('askalltime.db',detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    # 创建一个游标对象
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ai WHERE id=?",(id,))
    row = cursor.fetchone()
    model_nickname = row[1]
    model_name = row[2]
    url = row[3]
    APIkey = row[4]
    prompt = row[5][:10]
    is_dedefault = row[7]
    id = row[0]
    item = {'model_nickname': model_nickname, 'model_name': model_name, 'url': url, 'APIkey': APIkey, 'prompt': prompt,
            'is_default': is_dedefault, 'id': id}
    # 关闭连接
    conn.close()
    return item

