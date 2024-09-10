from django.urls import path
from goods import views

app_name = 'goods'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('filter/', views.filter, name='filter'),
    path('product/', views.product, name='product'),
    

]
