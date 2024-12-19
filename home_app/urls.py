from django.urls import path
from . import views

app_name = 'home_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('detail<int:pk>', views.detail, name='detail'),
    path('addtocart<int:pk>', views.add_to_cart, name='addtocart'),
    path('deletefromcart<int:pk>', views.delete, name='deletefromcart'),
    path('womencategory', views.women_category, name='womencategory'),
    path('search', views.search, name='search'),
    path('sportcategory', views.sport_category, name='sportcategory'),
    path('sendmsg', views.send_msg, name='sendmsg'),
    path('showcart', views.show_cart,name='showcart'),
    path('showall', views.all_products,name='all_products')

]
