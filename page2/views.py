from django.shortcuts import render,redirect
from . forms import PageForm

def store_page2_data(request):
    if request.method == "POST":
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page2')
        else:
            return render(request,'page2/project.html',{"form":form})
    form = PageForm()
    return render(request,'page2/project.html',{"form":form})
    






    return render(request,'page2/project.html')

# Create your views here.
