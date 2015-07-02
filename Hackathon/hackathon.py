from wsgiref.simple_server import make_server
import sqlite3

def createtable():
    conn = sqlite3.connect("gymregister.sqlite")
    cursor = conn.cursor()
    cursor.execute("create table student_count (studentname text, studentid text, classid text)") #execute the create table query
    conn.commit()
    conn.close()

def getdata():
    conn = sqlite3.connect("gymregister.sqlite")
    cursor = conn.cursor()
    result = cursor.execute("select * from student_count")
    datalist = result.fetchall()
    conn.commit()
    conn.close()
    return datalist

def insertmethod(studentname, studentid, classid):
    #print(country)
    conn = sqlite3.connect("gymregister.sqlite")
    cursor = conn.cursor()
    cursor.execute("insert into student_count(studentname, studentid, classid) values(?,?,?)", (studentname, studentid, classid))
    conn.commit()
    conn.close()

def get_form_vals(post_str):
    form_vals = {item.split("=")[0]: item.split("=")[1] for item in post_str.decode().split("&")}
    return form_vals
def hello_world_app(environ, start_response):
    #print("ENVIRON:", environ)
    message=""
    status = '200 OK'
    headers = [('Content-type', 'html; charset=utf-8')]
    start_response(status, headers)
    if(environ['REQUEST_METHOD'] == 'POST'):
        #createtable()
        request_body_size = int(environ['CONTENT_LENGTH'])
        request_body = environ['wsgi.input'].read(request_body_size)
        form_vals = get_form_vals(request_body)

            
        for item in form_vals.keys():
            if item == "studentname":
                studentname = form_vals[item]
            elif item == "studentid":
                studentid = form_vals[item]
            elif item == "classid":
                classid = form_vals[item]

        try:
            if (studentname==None or studentid==None or classid==None):
                raise Exception("")
            elif (studentname=="" or studentid=="" or classid==""):
                raise Exception("")
            else:
                insertmethod(studentname, studentid, classid)
          
        except Exception as e:
            message += "<br><font color=red>Please input completely!</font>"                
    message += "<br/><h1>People in the GYM!</h1><br/>"
    message += '''<img src="https://upload.wikimedia.org/wikipedia/commons/0/06/Yoga_Class_at_a_Gym.JPG" alt="Gym" style="width:304px;height:228px;">'''
    message += "<h1>Welcome to the GYM! Please register here for participation!</h1>"
    message += "<form method='POST'><br>StudentName:<input type=text name='studentname'>"
    message += "<br><br>StudentID:<input type=text name='studentid'>"
    message += "<br><br>ClassID:<input type=text name='classid'>"
    message += "<br><br><input type='submit' name='Submit' ></form>"

    message += "<h1>Registed People</h1>"
    datalist = getdata()
    message += "<table border=1>"
    message +="<tr><td><b>StudentName</b></td><td><b>StudentID</b></td><td><b>ClassID</b></td></tr>"
    for value in datalist:
        message +="<tr><td>"+value[0]+"</td><td>"+value[1]+"</td><td>"+value[2]+"</td></tr>"
    message += "</table>"    
    return[bytes(message,'utf-8')]
httpd = make_server('', 8000, hello_world_app)
print("Serving on port 8000...")
httpd.serve_forever()














