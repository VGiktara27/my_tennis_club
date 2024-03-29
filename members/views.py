from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import path
from members.data import test_fun
from members.models import Member
from members.models import Author
from django.contrib import messages
from members.models import Books
from members.models import Lent
from django.db.models import Count

def members(request):
    print(f"req=={request}")
    if request.method == "POST":
        print(f"req.post=={request.POST}")
        Member.objects.create(firstname=request.POST.get('firstname'), lastname=request.POST.get('lastname'),
                              phone_number=request.POST.get('phone_number'),
                              Member_id=int(request.POST.get('member_id')),
                              email=request.POST.get('email'))
        return HttpResponse("Data Saved")

        mymembers = Member.objects.all().values()
        context = {'mymembers': mymembers}
        return render(request, 'second.html', context)

    return render(request, 'first.html')


def lentz(request):
    print(f"req=={request}")

    books3 = Member.objects.all().values()
    books4 = Books.objects.all().values()
    context = {'books': books3, 'book2s': books4}
    return render(request, 'MemberBooks', context)


def author(request):
    print(f"req=={request}")
    if request.method == "POST":
        print(f"req.post=={request.POST}")
        Author.objects.create(firstname=request.POST.get('firstname'), lastname=request.POST.get('lastname'),
                              phone_number=request.POST.get('phone_number'),
                              author_id=int(request.POST.get('author_id')),
                              email=request.POST.get('email'))

        mymembers2 = Author.objects.all().values()
        context = {'mymembers': mymembers2}
        return render(request, 'second.html', context)

    return render(request, 'author.html')


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

def book(request):
    print(f"req=={request}")
    if request.method == "POST":
        print(f"req.post=={request.POST}")
        print(f"req.post=={type(request.POST.get('author_id'))}")
        member_inst = Author.objects.get(author_id=int(request.POST.get('author_id')))
        Books.objects.create(author_id=member_inst, authorname=request.POST.get('author_name'),
                             publication_name=request.POST.get('publication_name'),
                             book_id=int(request.POST.get('book_id')),
                             bookname=request.POST.get('book_name'))
        return HttpResponse("Data Saved")

    books3 = Author.objects.all().values()
    print("bookss", type(books3))
    context = {'books': books3}
    return render(request, 'third.html', context)


def mymembers2(request):
    # need to use filter
    # mymembers = Member.objects.values()
    # mymembers = Member.objects.filter(testfield=12).latest('testfield')
    # mymembers = Member.objects.filter(id).order_by('-id')[0]
    # mymembers = Member.objects.latest('id')
    mymembers = Author.objects.all().values()
    context = {'mymembers': mymembers}
    return render(request, 'second.html', context)


def listsofbooks(request):

    if request.method =="POST":
        print(f"req.post=={request.POST}")
        member_inst = Author.objects.get(author_id=int(request.POST.get('author_id')))
        mydata = Books.objects.filter(author_id=member_inst).values()
        books3 = Author.objects.all().values()
        context={'mymembers':mydata,
                 'books':books3
                 }
        return render(request,'ListofBooks.html',context)
    books3 = Author.objects.all().values()
    # print("bookss", type(books3))
    context = {'books': books3}
    return render(request, 'ListofBooks.html',context)

def listsofauthors(request):

    books3 = Author.objects.all().values()
    # print("bookss", type(books3))
    context = {'books': books3}
    return render(request, 'ListofAuthor.html',context)


def members(request):
    print(f"req=={request}")
    if request.method == "POST":
        print(f"req.post=={request.POST}")
        Member.objects.create(firstname=request.POST.get('firstname'), lastname=request.POST.get('lastname'),
                              phone_number=request.POST.get('phone_number'),
                              Member_id=int(request.POST.get('member_id')),
                              email=request.POST.get('email'))
        return HttpResponse("Data Saved")

        mymembers = Member.objects.all().values()
        context = {'mymembers': mymembers}
        return render(request, 'second.html', context)

    return render(request, 'first.html')


def charts(request):
    bookid_set = Books.objects.values('author_id').annotate(book_count=Count('book_id'))
    bookid_list=list(bookid_set)

    auth_list=[items['author_id'] for items in bookid_list]
    value_list=[items['book_count'] for items in bookid_list]

    print(f' auth_list---{ auth_list}')
    print(f' value_list---{value_list}')

    context={'auth_list':auth_list,'value_list':value_list}
    print(context)
    return render(request, 'Charts.html',context)
