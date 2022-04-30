from django.shortcuts import render
import mysql.connector as sql
fn=" "
ln=" "
# Create your views here.
s=" "
em=" "
pwd=" "
def signaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="ps7745ar",database="logins")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="firstname":
                fn=value
            if key=="lastname":
                ln=value
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        c="insert into log Values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
        cursor.execute(c)
        m.commit()
    return render(request,"signup.html")
        