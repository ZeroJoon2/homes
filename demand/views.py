from django.shortcuts import render, redirect
from users.models import tbUsers
from .models import tbDemands
# Create your views here.

# def demand_detail(request, id):
#     print_id = tbDemands.objects.get(id = id)
#     print(print_id)
#     context = {
#         'post_title' : id
#     }
#     return  context



def demand_view(request):
    user_email = request.session.get('user_email')
    if user_email:
        user = tbUsers.objects.get(email = user_email)
        print('hello~')
        print_id = tbDemands.objects.all()
        context = {
            'user' : user,
            'print_id' : print_id,
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
            house_type_code = request.POST.get('house_type_code')
            print(f'''request.POST.get('house_type_code') : {request.POST.get('house_type_code')}''')
            house_transaction_code = request.POST.get('house_transaction_code')
            house_location_code = request.POST.get('house_location_code')
            house_min_price = request.POST.get('house_min_price')
            house_max_price = request.POST.get('house_max_price')
            print(f'request.FILES : {request.FILES}')
            image1 = request.FILES['image1']
            image2 = request.FILES['image2']
            image3 = request.FILES['image3']
            print(f'house_type_code : {house_type_code}')
            print(f'house_transaction_code : {house_transaction_code}')
            print(f'house_location_code : {house_location_code}')
            print(f'house_min_price : {house_min_price}')
            print(f'house_max_price : {house_max_price}')
            tbDemands.objects.create(
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
            print('good')

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