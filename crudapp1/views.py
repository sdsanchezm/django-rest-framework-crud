from django.shortcuts import render


# Create your views here.

def test1(request):
	return render(request, "crudapp1/test1.html")