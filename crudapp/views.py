from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentForm
from .models import Student

# Create your views here.
def add_show(request):
    """" This function will add new data and show all data"""
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            pwd = fm.cleaned_data['password']
            res = Student(name=nm,email=email,password=pwd)
            # fm.save()      #save data in db
            res.save()    #save data in db using cleand_data method
            fm = StudentForm()  #after adding data in db show blank form
    else:
        fm = StudentForm()
    stud = Student.objects.all()


    return render(request,'crudapp/addandshow.html',{'form':fm,'std':stud})

def delete_data(request,id):
    """This function will delet data"""    
    if request.method == "POST":
        pi = Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update_data(request,id):
    """This function will update data"""
    if request.method == "POST":
        pi = Student.objects.get(pk=id)
        fm=StudentForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Student.objects.get(pk=id)
        fm = StudentForm(instance=pi)
    return render(request,'crudapp/update.html' ,{'form':fm})




