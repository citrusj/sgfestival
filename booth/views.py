from django.shortcuts import render
from django.shortcuts import get_object_or_404 
from .models import Booth, Photo


def booth_list(request):
    booths = Booth.objects.filter(checkbooth="madang")
    
    return render(request, 'booth/booth.html', {'booths': booths})

def flee_list(request):
    
    flees = Booth.objects.filter(checkbooth="flee")
    
    return render(request, 'booth/booth.html', {'flees': flees})


def booth_detail(request, index):
    booth = get_object_or_404(Booth, pk=index)  #booth꺼랑 flee쪽 다 포함임
    photos = Photo.objects.filter(booth=booth)

    # try:
    # # ip주소와 게시글 번호로 기록을 조회함
    #     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    #     if x_forwarded_for:
    #         ip = x_forwarded_for.split(',')[0]
    #     else:
    #         ip = request.META.get('REMOTE_ADDR')
    #     hits = HitCount.objects.update_or_create(ip=ip, booth=booth)
    # except Exception as e:
    #     # 처음 게시글을 조회한 경우엔 조회 기록이 없음
    #     print(e)
        
    return render(request, 'booth/booth_detail.html', {'booth':booth , 'photos': photos })


# Create your views here.



