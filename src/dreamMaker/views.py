from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
<<<<<<< HEAD
    user = request.user
    hello = 'Hello world'

    context = {
        'user':user,
        'hello': hello,
    }
    return render(request, 'main/home.html',context)
=======
	return render (request,'main/home.html')
>>>>>>> d5302132746921ea390fb3826529e2359b21a372
