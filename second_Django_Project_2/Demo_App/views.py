from django.shortcuts import render,redirect
from django.http import HttpResponse
from Demo_App.models import Student
from Demo_App.comman_methods import *
from json import dumps


# Create your views here.
def HomePage(request):
    return render(request,"Demo_App/Home.html")

def DemoPage(request):
    details={'firstName':'Likhith',
             'lastname':'Palukuru'}
    return render(request,"Demo_App/Test.html",{'firstname':'Likhith','lastname':'Palukuru'})

def LoginPage(request):
    msg="<h1 style="+"color:red;text-align:center;"+"> This is a Login Page </h1>" 
    return HttpResponse(msg)

def indexing(request):
    person= {'firstname': 'Likhith', 'lastname': 'Palukuru'}
    item_list = {"Chocolate": 4, "Pen": 10, "Pencil": 3}
    order_number= "000132342"
    context= {
        'person': person,
        'item_list': item_list,
        'order_number': order_number,
        }
    return render(request, 'test.html', context)

def TemplateTest(request):
    first_name='Likhith'
    last_name='Palukuru'
    std_list=Student.objects.all()
    fullname="{} {}".format(first_name, last_name)
    names=['likhith','Nayeen','Venkatesh']
    data={'size':std_list,'names':names,'std_list':std_list}
    return render(request,"Demo_App/Wish.html",context=data)

def BasePage(request):
    count=request.session.get('count',0)
    newcount=count+1
   # request.session['count']=newcount
    return render(request,"Demo_App/base.html",{'count':newcount})

def registerPage(request):
    msg=''
    mark=''
    if request.method=="POST":
        serialNumber=request.POST['sno']
        if len(serialNumber)==0:
            msg="The Serial Number Can't be Empty."
            mark='error' 
            return render(request,"Demo_App/CURD.html",{'msg':msg,'mark':mark})
            exit()
        
        print('this is Student Number :'+serialNumber)
        name=request.POST['sname']
        if len(name)==0:
            msg=" The Student Name Can't be Empty."
            mark='error' 
            return render(request,"Demo_App/CURD.html",{'msg':msg,'mark':mark})
            exit()
        
        print('this is name :'+name)
        address=request.POST['saddress']
        if len(address)==0:
            msg=" The Student Address Can't be Empty."
            mark='error' 
            return render(request,"Demo_App/CURD.html",{'msg':msg,'mark':mark})
            exit()
        
        print('this is address :'+address)
        obj=Student.objects.create(sno=serialNumber,sname=name,saddr=address)
        msg=name+" Student Registered Successfully....!"
        mark='sucess'
        obj.save()
    return render(request,"Demo_App/CURD.html",{'msg':msg,'mark':mark})

def deleterec(request,id):
    stdobj=Student.objects.get(id=id)
    stdobj.delete()
    print(id)
    return redirect('/testapp/template')

def updatepage(request,id):
    stdobj=Student.objects.get(id=id)
    data={'stddata':stdobj}
    if request.method=="POST":
        serialNumber=request.POST['sno']
        name=request.POST['sname']
        address=request.POST['saddress']
        stdobj.sno=serialNumber
        stdobj.sname=name
        stdobj.saddr=address
        stdobj.save()
        Stdall=Student.objects.all()
        return redirect('/testapp/template')
    return render(request,"Demo_App/Update.html",context=data)

def loginform(request):
    return render(request,"Demo_App/Login.html")









