import sqlite3
from flask import Flask,request,render_template,url_for

app = Flask(__name__)

# con = sqlite3.connect('database.db')
# con.execute('create table student(name text,addr text,city text,pin text)')
# con.close()

@app.route('/')
def hello_world():
    return "hello world"

@app.route('/creat')
def create_student():
    return render_template('student.html')

@app.route('/addstudent',methods = ['POST','GET'])
def add_student():
    try:
        nm = request.form['nm']
        addr = request.form['addr']
        city = request.form['city']
        pin = request.form['pin']
        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute('insert into student (name, addr, city, pin) values (?, ?, ?, ?)', (nm, addr, city, pin))
            cur.close()
            con.commit()
            msg = "创建数据成功"
    except:
        con.rollback()
        msg="操作失败"
    finally:
        return render_template("result.html",msg = msg)
    con.close()

@app.route('/show')
def show_student():
    con = sqlite3.connect("database.db")
    con.row_factory=sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from student")
    rows = cur.fetchall()
    return render_template("show.html",rows=rows)

if __name__=='__main__':
     app.run(debug=True)