from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.utils.crypto import get_random_string
from django.conf import settings

def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

# 인증 코드 전송 뷰
def send_verification_code(request):
    if request.method == "POST":
        email = request.POST.get("email")
        verification_code = get_random_string(length=6, allowed_chars="1234567890")
        request.session["verification_code"] = (
            verification_code  # 인증 코드를 세션에 저장
        )
        request.session["email"] = email

        # 이메일 전송
        send_mail(
            "Your Verification Code",
            f"Your verification code is {verification_code}",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        # 이메일 주소를 템플릿으로 전달
        return render(request, "signup.html", {"email": email})
    return JsonResponse({"error": "Invalid request method."}, status=400)

# 인증 코드 확인 뷰
def verify_code(request):
    if request.method == "POST":
        email = request.session.get("email")  # Retrieve email from session
        entered_code = request.POST.get("verification_code")
        stored_code = request.session.get("verification_code")

        if entered_code == stored_code:
            # Verification successful
            return render(request, "signup.html", {"verification_successful": True, "email": email})
        else:
            # Verification failed
            return render(request, "signup.html", {"verification_failed": True, "email": email})

    return JsonResponse({"error": "Invalid request method."}, status=400)

def complete_registration(request):
    if request.method =='POST':
        print('hi')
        return render(request, 'next.html')
    return render(request, 'next.html')