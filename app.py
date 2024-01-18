from flask import (Flask, render_template, make_response, url_for, request,
                   redirect, flash, session, send_from_directory, jsonify)
from werkzeug.utils import secure_filename
app = Flask(__name__)

# one or the other of these. Defaults to MySQL (PyMySQL)
# change comment characters to switch to SQLite

import cs304dbi as dbi
# import cs304dbi_sqlite3 as dbi

import secrets

app.secret_key = 'your secret here'
# replace that with a random key
app.secret_key = secrets.token_hex()

# This gets us better error messages for certain common request errors
app.config['TRAP_BAD_REQUEST_ERRORS'] = True

@app.route('/')
def index():
    return render_template('list-all.html',users = users,page_title='test')

@app.route('/quiz/', methods=['GET','POST'])
def quiz():
    conn = dbi.connect()
    if request.method == "GET":
        return render_template('quiz.html',page_title='form')
    # if post, then they submitted form data, and we want to enter that
    elif request.method == "POST":
        return render_template('quiz.html',page_title='form')
    return print("shouldnt get here")

@app.route('/all-users/')
def list_all():
    conn = dbi.connect()
    curs = dbi.dict_cursor(conn)
    
    # Select * here as all columns are needed for rendering
    curs.execute(
        """
        select username, descrip, contact, classyear, bedtime, waketime, cleanliness, activity, dorm
        from roommate
        """
    )
    users = curs.fetchall()
    return render_template('list-all.html', users = users, page_title='List All')

if __name__ == '__main__':
    import sys, os
    if len(sys.argv) > 1:
        # arg, if any, is the desired port number
        port = int(sys.argv[1])
        assert(port>1024)
    else:
        port = os.getuid()
    # set this local variable to 'wmdb' or your personal or team db
    db_to_use = 'je100_db' 
    print('will connect to {}'.format(db_to_use))
    dbi.conf(db_to_use)
    app.debug = True
    app.run('0.0.0.0',port)
