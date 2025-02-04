from django.shortcuts import render , redirect
from . forms import EmpForm


def store_page1_data(request):
    if request.method == "POST":
        form = EmpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("page1")
        else:
            return render(request, "page1/emps.html", {"form": form})
    form = EmpForm()
    return render(request, "page1/emps.html", {"form": form})

# Create your views here.
