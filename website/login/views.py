from django.shortcuts import render
import mysql.connector as sql

em=" "
pwd=" "
def loginaction(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="ps7745ar",database="logins")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
           
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        c="select * from log where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if(t==()):
            return render(request,'error.html')
        else:
            return render(request,'welcome.html')
    return render(request,"loginup.html")
        

