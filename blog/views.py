from django.shortcuts import render
from .models import Post


def index_page(request):
    posts = Post.objects.all()
    ctx = {"posts": posts}
    return render(request, "index.html", ctx)

def calc_page(request):
    a = request.POST.get("a")
    b = request.POST.get("b")

    try:
        sum = int(a) + int(b)
    except:
        sum = "error"

    ctx = {"t_sum": sum, "a": a, "b": b}
    return render(request, "calc.html", ctx)


def add(request):
    return render(request, "add.html")


def subtract(request):
    a = request.POST.get("a")
    b = request.POST.get("b")

    try:
        difference = int(a) - int(b)
    except:
        difference = "error"

    ctx = {"t_difference": difference, "a": a, "b": b}
    return render(request, "subtract.html", ctx)


def multiply(request):
    a = request.POST.get("a")
    b = request.POST.get("b")

    try:
        multiply = int(a) * int(b)
    except:
        multiply = "error"

    ctx = {"t_multiply": multiply, "a": a, "b": b}
    return render(request, "multiply.html", ctx)

def divide(request):
    a = request.POST.get("a")
    b = request.POST.get("b")

    try:
        divide = int(a) / int(b)
    except:
        divide = "error"

    ctx = {"t_divide": divide, "a": a, "b": b}
    return render(request, "divide.html", ctx)

    