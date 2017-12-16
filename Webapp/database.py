import sqlite3

conn = None

def open_database(path):
    global conn
    conn = sqlite3.connect(path)

def get_task_list(status):
    c = conn.cursor()
    c.execute("SELECT id, task, CASE WHEN status = 1 THEN 'Open' ELSE 'Closed' END FROM todo WHERE status LIKE ?",(status,))
    result = c.fetchall()
    c.close()
    return result

def new_task(new):
    c = conn.cursor()
    c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new, 1))
    new_id = c.lastrowid
    conn.commit()
    c.close()
    return new_id

def search_task(item, status):
    c = conn.cursor()
    item = "%" + item + "%"
    c.execute("SELECT id, task, CASE WHEN status = 1 THEN 'Open' ELSE 'Closed' END FROM todo WHERE task LIKE ? AND status LIKE ?", (str(item),status))
    result = c.fetchall()
    c.close()
    return result

def get_task(id):
    c = conn.cursor()
    c.execute("SELECT id,task,status FROM todo WHERE id LIKE ?", (str(id),))
    result = c.fetchone()
    c.close()
    return result

def update_task(task_edit, task_status, task_id):
    c = conn.cursor()
    c.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (task_edit, task_status, task_id))
    conn.commit()
    c.close()

def delete_task(id):
    c = conn.cursor()
    c.execute("DELETE FROM todo WHERE id = ?", (str(id),))
    conn.commit()
    c.close()