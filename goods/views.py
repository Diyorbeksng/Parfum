from django.shortcuts import render



def catalog(request):
    return render(request, 'goods/catalog.html')


def filter(request):
    return render(request, 'goods/filter.html')

def product(request):
    return render(request, 'goods/product.html')
#fsdfedgdrgergergre
