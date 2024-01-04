from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import path
from members.data import test_fun
from members.models import Member
from django.contrib import messages

def members(request):
    print(f"req=={request.POST}")
    if request.method == "POST":
        print(f"got pos req")
        Member.objects.create(firstname=request.POST.get('firstname'), lastname=request.POST.get('lastname'))
    return render(request, 'first.html')


# def show(request):
#     print(f"req=={request.POST}")
#     if request.method=="POST":
#         print(f"got pos req")
#         Member.firstname=request.post.get('firstname')
#         Member.lastname = request.post.get('lastname')
#         Member.objects.create(firstname=request.post.get('firstname'), lastname=request.post.get('lastname'))
#         return HttpResponse("Hello world!")
#     else:
#         return HttpResponse("Not Working")


def mymembers2(request):
    # need to use filter
    # mymembers = Member.objects.values()
    # mymembers = Member.objects.filter(testfield=12).latest('testfield')
    # mymembers = Member.objects.filter(id).order_by('-id')[0]
     # mymembers = Member.objects.latest('id')
    mymembers = Member.objects.all().values()
    context = {
        'mymembers': mymembers,
    }
    return render(request, 'second.html', context)
