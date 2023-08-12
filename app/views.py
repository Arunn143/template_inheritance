from django.shortcuts import render

# Create your views here.

def parents_mdb4(request):
    return render(request,'parents_mdb4.html')


def child(request):
    return render(request,'child.html')