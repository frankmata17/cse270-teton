# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

MAGIC_PASSWORD = "CSE270Rocks!"

headers = {
    "Cross-Origin-Opener-Policy": "unsafe-none",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers":
        "Origin, X-Requested-With, Content-Type, Accept",
}


def index(request):
    print(request.GET.get("password"))
    password = request.GET.get("password")
    username = request.GET.get("username")

    if password == MAGIC_PASSWORD or (
        username == "admin" and password == "qwerty"
    ):
        return HttpResponse(headers=headers)
    else:
        return HttpResponse(status=401, headers=headers)


def ingest(request):
    print(request.GET)
    return HttpResponse(headers=headers)
