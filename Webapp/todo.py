import sqlite3
from bottle import get, post, run, debug, template, request, redirect, get, static_file
import database

LOCAL = (__name__ == "__main__")

if LOCAL:
    VIEWS = "."
else:
    VIEWS = ""

@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='./static/')

@get('/')
@get('/todo')
def todo():
    result = database.get_task_list(1)
    res_closed = database.get_task_list(0)
    output = template('make_table', rows=result, closed=res_closed)
    return output

@post('/new')
def new_item():
    new = request.POST.task.strip()
    database.new_task(new)
    return redirect("/")

@post('/search')
def search_item():
    item = request.POST.searchtxt.strip()
    result = database.search_task(item, 1)
    res_closed = database.search_task(item, 0)
    if not result:
        output = template('make_table', rows=result, closed=res_closed)
        return output
    else:
        output = template('make_table', rows=result, closed=res_closed)
        return output
        #return 'Task ID: '+str(result[0][0])+'and Task: '+str(result[0][1])

@get('/edit/<no:int>')
def edit_item(no):
    cur_data = database.get_task(no)
    return template('edit_task', old=cur_data, no=no)

@post('/edit/<no:int>')
def edit_item(no):
    edit = request.POST.task.strip()
    status = request.POST.status.strip()
    if status == 'Open':
        status = 1
    else:
        status = 0
    database.update_task(edit, status, no)
    return redirect("/")

@get('/delete/<id:int>')
def delete_item(id):
    database.delete_task(id)    
    return redirect("/")

if __name__ == "__main__":
    database.open_database("todo.db")
    debug(True)
    run(host="0.0.0.0", port=8080, reloader=True)
else:
    database.open_database("todo.db")
    application = default_app()