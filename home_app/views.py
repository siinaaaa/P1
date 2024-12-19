from django.contrib.auth import authenticate
from .models import Product, Order, Contact
from auth_app.models import ImageProcessing
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    products = Product.objects.all()
    order = Product.objects.raw('select * from modshopdb.home_app_product order by price DESC')
    return render(request, 'home_app/index.html', {'products': products, 'recent': order})


def detail(request, pk):
    instance = get_object_or_404(Product, id=pk)
    return render(request, 'home_app/detail.html', {'product': instance})


def add_to_cart(request, pk):
    if request.method == 'POST':
        product = Product.objects.get(id=pk)

        quantity, color, size = request.POST.get('quantity'), request.POST.get('color'), request.POST.get('size')
        product_exist = Order.objects.filter(username=request.user, color=color, size=size,
                                             product_name=product.name).exists()
        instance = Order.objects.filter(username=request.user, color=color, size=size,
                                        product_name=product.name)
        print(request.user)

        if product_exist:
            print('ok')
            for order in instance:
                order.quantity += int(quantity)
                print('test2')
                order.total_price += int(quantity) * int(product.price)
                order.save()

        else:
            print('no')

            new_instance = Order.objects.create(username=request.user, color=color, size=size,
                                                product_name=product.name,
                                                quantity=int(quantity), price=int(product.price))
            print('test')
            new_instance.total_price += (int(quantity) * int(new_instance.price))
            new_instance.save()

        products = Order.objects.filter(username=request.user)
        total_prices = 0
        for order in products:
            total_prices += order.total_price

        return render(request, 'home_app/cart.html', {'products': products, 'total': total_prices})
    products = Order.objects.filter(username=request.user)
    total_prices = 0
    for order in products:
        total_prices += order.total_price

    return render(request, 'home_app/cart.html', {'products': products, 'total': total_prices})


def delete(request, pk):
    Order.objects.get(id=pk).delete()
    products = Order.objects.filter(username=request.user)
    total_prices = 0
    for order in products:
        total_prices += order.total_price
    return render(request, 'home_app/cart.html', {'products': products, 'total': total_prices})


def women_category(request):
    search_products = Product.objects.filter(category__name='women')
    products = Product.objects.all()
    order = Product.objects.raw('select * from modshopdb.home_app_product order by price DESC')
    return render(request, 'home_app/index.html', {'products': products, 'recent': order, 'search': search_products})


def sport_category(request):
    search_products = Product.objects.filter(category__name='sport')
    products = Product.objects.all()
    order = Product.objects.raw('select * from modshopdb.home_app_product order by price DESC')
    return render(request, 'home_app/index.html', {'products': products, 'recent': order, 'search': search_products})


def search(request):
    name = request.GET.get('search')
    print(name)
    search_products = Product.objects.raw('select * from modshopdb.home_app_product where name LIKE %s', [f'%{name}%'])
    products = Product.objects.all()
    order = Product.objects.raw('select * from modshopdb.home_app_product order by price DESC')
    return render(request, 'home_app/index.html', {'products': products, 'recent': order, 'search': search_products})


def send_msg(request):
    if request.method == 'POST':
        name, subj, msg, email = request.POST.get('name'), request.POST.get('subj'), request.POST.get(
            'msg'), request.POST.get('email')
        Contact.objects.create(name=name, subj=subj, msg=msg, email=email)
        return render(request, 'home_app/contact.html')

    return render(request, 'home_app/contact.html')


def show_cart(request):
    products = Order.objects.filter(username=request.user)
    total_prices = 0
    for order in products:
        total_prices += order.total_price
    return render(request, 'home_app/cart.html', {'products': products, 'total': total_prices})


def all_products(request):
    colors, sizes, min_price, max_price = request.GET.getlist('color'), request.GET.getlist('size'), request.GET.get(
        'min'), request.GET.get('max')

    products = Product.objects.all()
    if colors:
        products = products.filter(colors__color__in=colors).distinct()
    if sizes:
        products = products.filter(size__size__in=sizes).distinct()
    if max_price and min_price:
        max = int(max_price)
        min = int(min_price)
        products = products.raw('select * from modshopdb.home_app_product where price > %s and price < %s',
                                [min, max])
    paginator = Paginator(products, 1)
    page = request.GET.get('page')
    obj = paginator.get_page(page)

    return render(request, 'home_app/shop.html', {'products': obj})
