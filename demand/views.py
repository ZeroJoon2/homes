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
            )
            print('good')
            return redirect('demand_view')
        return render(request,'demand_add.html')
    else:
        print('?')        
    return render(request,'login.html')