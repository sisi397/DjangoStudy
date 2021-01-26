from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.


def index (request):
	return render(request, "a.html")

def gu(req):
    num = req.GET.get('num','')
    return HttpResponse(f"<h1> gugu : {num_gugu(num)} </h1>")

def num_gugu(num):
    str = ""
    for i in range(9):
        str += f"{int(num)} * {i+1} = {int(num) * (i+1)} <br>"
    return str
