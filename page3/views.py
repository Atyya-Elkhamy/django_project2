from django.shortcuts import render,redirect
from . forms import DepForm


def store_page3_data(request):
    if request.method == 'POST':
        form = DepForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("page3")
        else:
            return render(request,"page3/departments.html",{"form":form})
    form = DepForm()
    return render(request,'page3/departments.html',{"form":form})
    





    return render(request,'page3/departments.html')

# Create your views here.
