
from django.shortcuts import render, redirect, get_object_or_404
from .models import PropertyListing
from django.contrib import messages
from django.db.models import Count
from users.models import tbUsers
from supply.models import tbSupply
from supply.forms import PropertyListingForm
from django.conf import settings
from django.core.files.storage import default_storage
from django.urls import reverse
from io import BytesIO
import base64
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import os
def index_view(request):
    print('index_view')
    user_email = request.session.get('user_email')
    user = tbUsers.objects.get(email = user_email)
    context = {
        'user' : user

    }
    return render(request, 'supply/supply.html', context)

# def index(request):
#     return render(request, 'supply.html')

        # print(f'user_email : {user_email}')
        # print(f'post_title : {post_title}')
        # print(f'house_type_code : {house_type_code}')
        # print(f'house_transaction_code : {house_transaction_code}')
        # print(f'house_location_code : {house_location_code}')
        # if form.is_valid():
        #     # 로그인한 사용자의 정보로 매물 등록
        #     property_listing = form.save(commit=False)
        #     property_listing.user = request.user  # 로그인한 사용자 설정
        #     property_listing.save()
        #     messages.success(request, '매물이 성공적으로 등록되었습니다.')
        #     return redirect('my_list')  # 등록 후 메인 페이지로 이동


font_path = os.path.join(settings.BASE_DIR, 'static', 'fonts', 'NotoSansKR-Black.ttf')
font_name = font_manager.FontProperties(fname = font_path).get_name()
rc('font', family = font_name)
def chart():
    data = sorted(tbSupply.objects.values('house_location_name').annotate(count = Count('house_location_name')), key = lambda x: x['count'], reverse=True)
    x_field = [i['house_location_name'] for i in data]
    y_field = [i['count'] for i in data]
    plt.figure(layout = 'constrained') #layout으로 크기 자동 조절된다고 함
    plt.bar(x_field, y_field, edgecolor = 'black', color = 'tab:pink')
    plt.title('자치구별 공급')
    plt.xticks(rotation = 90)
    plt.yticks(range(0,max(y_field)+1,10))
    plt.ylim(bottom = 0)
    plt.xlabel('서울 자치구')
    plt.ylabel('공급')

    buffer = BytesIO()
    plt.savefig(buffer, format = 'png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode()
    buffer.close()
    return image_base64

    
def supply_view(request):
    user_email = request.session['user_email'] 
    user = tbUsers.objects.get(email = user_email)
    context = {
        'user' : user,
    }
    print(user_email)
    print(user)
    if user_email is not None:
        print('user_email is not None')
        #form = PropertyListingForm(request.POST, request.FILES)
        print('good')
        if request.method == 'POST':
            email = tbUsers.objects.get(email = request.session.get('user_email'))
            post_title = request.POST.get('post_title')
            house_type_code = int(request.POST.get('house_type_code'))
            house_transaction_code = int(request.POST.get('house_transaction_code'))
            house_location_code = int(request.POST.get('house_location_code'))
            
            new_row = tbSupply.objects.create(
                email = email,
                post_title = post_title,
                house_type_code = house_type_code,
                house_transaction_code = house_transaction_code,
                house_location_code = house_location_code,
            )
            post_id = new_row.id
            new_row.save()
            context = {
                'user' : user,
                'post_id' : post_id
            }
            print(new_row.id)
            print('DB에 저장합니다이')
            # post_id를 포함하여 URL로 리다이렉트
            return redirect(reverse('supply_add_detail', args=[post_id]),context)

        return render(request, 'listings/supply_add.html', context)
    else:
        return render(request, 'login.html')


# views.py
def supply_add_detail(request, post_id): 
    user_email = request.session['user_email']
    user = tbUsers.objects.get(email = user_email)
    post_id = tbSupply.objects.get(id = post_id)
    
    print(f'{user}')
    print(f'{post_id}')
    context = {
    'user' : user,
    'post_id' : post_id,
    'image_range': range(1, 8),  # 이미지 업로드용 숫자 리스트 전달
    }  
    if request.method == 'POST':
        # 폼에서 전송된 데이터를 받아옴
        address = request.POST.get('address')
        width = request.POST.get('width')
        height = request.POST.get('height')
        price = request.POST.get('price')
        rooms = request.POST.get('rooms')
        bath = request.POST.get('bath')
        is_park = request.POST.get('is_park')
        age = request.POST.get('age')
        owner_fee = request.POST.get('owner_fee')
        surround = request.POST.get('surround')
        etc = request.POST.get('etc')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        image4 = request.FILES.get('image4')
        image5 = request.FILES.get('image5')
        image6 = request.FILES.get('image6')
        image7 = request.FILES.get('image7')
        print(image1)
        print(image2)
        print(image3)
        print(image4)
        print(image5)
        print(image6)
        print(image7)

        PropertyListing.objects.create(
            address = address,
            width = width,
            height = height,
            price = price,
            rooms = rooms,
            bath = bath,
            is_park = is_park,
            age = age,
            owner_fee = owner_fee,
            surround = surround,
            etc = etc,
            email = user,
            list_id = post_id,
            image1 = image1,
            image2 = image2,
            image3 = image3,
            image4 = image4,
            image5 = image5,
            image6 = image6,
            image7 = image7,
        )
        print('세부 목록도 저장합니다.')
        context = {
            'user' : user,
        }
        return redirect('all_listings')

    return render(request, 'listings/supply_add_detail.html', context)

#내 매물 목록 페이지 
def my_listings_only_view(request):
    user_email = request.session.get('user_email')
    user = tbUsers.objects.get(email = user_email)
    print(f'{user_email}')
    print(f'여기 : {user_email}')
    if user_email == user.email:
        print('통과')
        # 현재 로그인한 사용자의 매물만 필터링하여 가져옵니다.
        my_listings = tbSupply.objects.filter(email=user_email).values('id', 'post_title')
        
        context = {
            'my_listings': my_listings,
            'user': user
        }
        print(f'my_listings : {my_listings}')
        return render(request, 'supply/my_list_only.html', context)



def property_register(request):
    if request.method == 'POST':
        house_type = request.POST.get('house_type')
        transaction_type = request.POST.get('transaction_type')
        
        property_listing = PropertyListing.objects.create(
            house_type=house_type,
            transaction_type=transaction_type,
        )
        
        return redirect('listing_detail', pk=property_listing.pk)

    return render(request, 'supply.html')



#내 매물 페이지 뷰 
def my_list_view(request):
    user_email = request.session['user_email'] 
    user = tbUsers.objects.get(email = user_email)

    if request.method == "POST":
        # 로그인한 사용자만 자신의 매물을 볼 수 있도록 필터링
        listings = PropertyListing.objects.filter(user=request.user)
        context = {
        'listings': listings,
        'user' : user

         }
    return render(request, 'listings/my_list.html', context)


def listing_list_view(request):
    listings = PropertyListing.objects.filter(user=request.user)  # 로그인한 사용자만 필터링
    return render(request, 'listings/my_list.html', {'listings': listings})

# 매물 상세 페이지 뷰
def listing_detail_view(request, post_id):
    user_email = request.session['user_email'] 
    user = tbUsers.objects.get(email = user_email)
    listings = tbSupply.objects.get(id = post_id)
    listing = PropertyListing.objects.get(list_id = post_id)
    print(f'post_id : {post_id}')
    
    image_range = range(1,8)
    context = {
        'user' : user,
        'listings' : listings,
        'listing' : listing,
        'image_range' : image_range

    }
    return render(request, 'listings/all_listings_detail.html', context)


# 매물 수정 뷰 함수
def listing_update_view(request, id):
    listing = get_object_or_404(PropertyListing, id=id)

    if request.method == 'POST':
        form = PropertyListingForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listing_detail', id=listing.id)
        else:
            # form이 유효하지 않을 경우, 오류를 디버그하기 위해 출력
            print(form.errors)
    else:
        form = PropertyListingForm(instance=listing)

    return render(request, 'listings/listing_update.html', {'form': form, 'listing': listing})

# 매물 삭제 뷰 함수
def listing_delete_view(request, id):
    listing = get_object_or_404(PropertyListing, id=id)

    if request.method == 'POST':
        listing.delete()
        return redirect('my_list')

    return render(request, 'listings/listing_confirm_delete.html', {'listing': listing})

# 모든 매물 보기 뷰
def all_listings_view(request):
    user_email = request.session['user_email'] 
    user = tbUsers.objects.get(email = user_email)
    listings = tbSupply.objects.all()
    image_base64 = chart()
    context = {
        'listings': listings,
        'user' : user,
        'chart' : image_base64,
    }
    return render(request, 'listings/all_listings.html',context)
    
def supply_add(request):
    if request.method == 'POST':
        house_type = request.POST.get('house_type')
        transaction_type = request.POST.get('transaction_type')
        print(house_type, transaction_type)
        return render(request, 'listings/my_list.html')