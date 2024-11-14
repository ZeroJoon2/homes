from django.shortcuts import render, redirect
from django.conf import settings
from django.db.models import Count
from users.models import tbUsers
from .models import tbDemands
from io import BytesIO
import base64
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import os
# Create your views here.

# def demand_detail(request, id):
#     print_id = tbDemands.objects.get(id = id)
#     print(print_id)
#     context = {
#         'post_title' : id
#     }
#     return  context

# def just_do_it():
#     font_path = 'C:/Users/YJ/Desktop/국비교육/python/web/django_proj/homes/static/fonts/NotoSansKR-Black.ttf'
#     font_name = font_manager.FontProperties(fname = font_path).get_name()
#     rc('font', family = font_name)
#     pass

font_path = os.path.join(settings.BASE_DIR, 'static', 'fonts', 'NotoSansKR-Black.ttf')
font_name = font_manager.FontProperties(fname = font_path).get_name()
rc('font', family = font_name)
def chart():
    data = sorted(tbDemands.objects.values('house_location_name').annotate(count = Count('house_location_name')), key = lambda x: x['count'], reverse=True)
    x_field = [i['house_location_name'] for i in data]
    y_field = [i['count'] for i in data]
    plt.figure(layout = 'constrained') #layout으로 크기 자동 조절된다고 함
    plt.bar(x_field, y_field, edgecolor = 'black', color = 'tab:pink')
    plt.title('자치구별 수요')
    plt.xticks(rotation = 90)
    plt.yticks(range(min(y_field),max(y_field)+1))
    plt.ylim(bottom = 0)
    plt.xlabel('서울 자치구')
    plt.ylabel('수요')

    buffer = BytesIO()
    plt.savefig(buffer, format = 'png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode()
    buffer.close()
    return image_base64


def demand_view(request):
    #just_do_it()
    # 함수 호출할까 했지만, 페이지 렌더링 될때마다 이러면 성능에 안좋을거 같아, 전역변수로 가져가기
    user_email = request.session.get('user_email')
    if user_email:
        user = tbUsers.objects.get(email = user_email)
        print('hello~')
        print_id = tbDemands.objects.all()
        image_base64 = chart()
        context = {
            'user' : user,
            'print_id' : print_id,
            'chart' : image_base64,
        }

        return render(request, 'demand_view.html', context)
    else:
        print('?')        
        return render(request,'login.html')
    
def demand_add(request):
    user_email = request.session.get('user_email')
    if user_email:
        user = tbUsers.objects.get(email = request.session.get('user_email'))
        if request.method == 'POST':
            email = tbUsers.objects.get(email = request.session.get('user_email'))

            print(f'''request.session.get('user_email') : {request.session.get('user_email')}''')        
            post_title = request.POST.get('post_title')
            house_type_code = int(request.POST.get('house_type_code'))
            print(f'''request.POST.get('house_type_code') : {request.POST.get('house_type_code')}''')
            house_transaction_code = int(request.POST.get('house_transaction_code'))
            house_location_code = int(request.POST.get('house_location_code'))
            house_min_price = request.POST.get('house_min_price')
            house_max_price = request.POST.get('house_max_price')
            print(f'request.FILES : {request.FILES}')
            image1 = request.FILES.get('image1')
            image2 = request.FILES.get('image2')
            image3 = request.FILES.get('image3')
            print(f'house_type_code : {house_type_code}')
            print(f'house_transaction_code : {house_transaction_code}')
            print(f'house_location_code : {house_location_code}')
            print(f'house_min_price : {house_min_price}')
            print(f'house_max_price : {house_max_price}')




            new_row = tbDemands.objects.create(
                email = email,
                post_title = post_title,
                house_type_code = house_type_code,
                house_transaction_code = house_transaction_code,
                house_location_code = house_location_code,
                house_min_price = house_min_price,
                house_max_price = house_max_price,
                image1 = image1,
                image2 = image2,
                image3 = image3,
            )
            new_row.save()
            print('DB에 저장합니다이')

            return redirect('demand_view')
        context = {
            'user' : user,
        }
        return render(request,'demand_add.html',context)
    else:
        print('?')        
    return render(request,'login.html')


def demand_detail(request, post_id):
    user_email = request.session.get('user_email')
    user = tbUsers.objects.get(email = user_email)
    post_index = [num+1 for num, i in enumerate(tbDemands.objects.all())]
    print(post_id)
    try:
        print('good~')
        
        post_id = tbDemands.objects.get(id = post_id)
        last_id = tbDemands.objects.last().id
        value_post_title = post_id.post_title
        value_house_type_code = post_id.house_type_code
        value_house_transaction_code = post_id.house_transaction_code
        value_house_location_code = post_id.house_location_code
        value_house_min_price = post_id.house_min_price
        value_house_max_price = post_id.house_max_price
        value_house_max_price = post_id.house_max_price
        print(post_id.image1.url)
        print(post_id.image2.url)
        print(post_id.image3.url)

        context = {
            'user' : user,
            'post_index' : post_index,
            'post_id' : post_id,
            'last_id' : last_id,
            'value_post_title' : value_post_title,
            'value_house_type_code' : value_house_type_code,
            'value_house_transaction_code' : value_house_transaction_code,
            'value_house_location_code' : value_house_location_code,
            'value_house_min_price' : value_house_min_price,
            'value_house_max_price' : value_house_max_price,

        }
        print(context)
        return render(request, 'demand_detail.html', context)
    except Exception as e:
        context = {
            'e' : e
            }
        return print(context)

