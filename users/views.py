from django.shortcuts import render, redirect
from users.models import tbUsers
from django.contrib.auth import authenticate, login


# Create your views here.
def register_user(request):
    if request.method == "POST":
        email = request.session.get("email")
        password = request.POST.get("password")
        nickname = request.POST.get("nickname")
        if email and password and nickname:
            try:
                tbUsers.objects.create(
                    email=email, password=password, nickname=nickname
                )
                return render(request, "login.html")
            except:
                context = {"error_message": "이미 등록되있는디요"}
                return render(request, "error.html", context)
    return render(request, "login.html")


def login_check(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = tbUsers.objects.get(email=email)
        try:
            if password == user.password:
                print("hello")
                request.session["user_email"] = user.email  # user의 id를 세션에 저장
                return render(request, "select.html", {"user": user})

            else:
                print("bye")
                return render(request, "login.html")
        except Exception as e:
            print("except", e)
            return render(request, "index.html")

    return render(request, "login.html")
