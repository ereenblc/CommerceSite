from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

# Home Page Products
def index(request):
    return render(request, "base.html")

def alfa_awus(request):
    return render(request, "commerce_app/alfa_awus.html")

def xiaomi_mi(request):
    return render(request, "commerce_app/xiaomi_mi.html")

def grundig(request):
    return render(request, "commerce_app/grundig.html")

def rival3(request):
    return render(request, "commerce_app/rival3.html")

def airpods2(request):
    return render(request, "commerce_app/airpods2.html")

def stanley(request):
    return render(request, "commerce_app/stanley.html")

def iphone13(request):
    return render(request, "commerce_app/iphone13.html")

def applewatch(request):
    return render(request, "commerce_app/applewatch.html")

def army_coat(request):
    return render(request, "commerce_app/army_coat.html")

def billing(request):
    return render(request, "commerce_app/billing.html")

# Wifi Card Products
def alfa_uw07(request):
    return render(request, "commerce_app/alfa_uw07.html")

def asus_usb(request):
    return render(request, "commerce_app/asus_usb.html")

def tp_link(request):
    return render(request, "commerce_app/tp_link.html")

# Television Products
def toshiba_tv(request):
    return render(request, "commerce_app/toshiba_tv.html")

def samsung_tv(request):
    return render(request, "commerce_app/samsung_tv.html")

def philips_tv(request):
    return render(request, "commerce_app/philips_tv.html")

def regal_tv(request):
    return render(request, "commerce_app/regal_tv.html")

# PC Equipmants 
def asus_mouse(request):
    return render(request, "commerce_app/asus_mouse.html")

def logitech_keyboard(request):
    return render(request, "commerce_app/logitech_keyboard.html")

def logitech_mouse(request):
    return render(request, "commerce_app/logitech_mouse.html")

def medusa_headset(request):
    return render(request, "commerce_app/medusa_headset.html")

# Earphones Products
def airpods_pro(request):
    return render(request, "commerce_app/airpods_pro.html")

def oppo_earphones(request):
    return render(request, "commerce_app/oppo_earphones.html")

def huawei_earphones(request):
    return render(request, "commerce_app/huawei_earphones.html")

def airpods_headset(request):
    return render(request, "commerce_app/airpods_headset.html")

# Thermos Products
def stanley_neverleak(request):
    return render(request, "commerce_app/stanley_neverleak.html")

def stanley_vacuum(request):
    return render(request, "commerce_app/stanley_vacuum.html")

def stanley_mug(request):
    return render(request, "commerce_app/stanley_mug.html")

def stanley_food(request):
    return render(request, "commerce_app/stanley_food.html")

#iPhone Products
def iphone13_pro_1tb(request):
    return render(request, "commerce_app/iphone13_pro_1tb.html")

def iphone13_promax_128gb(request):
    return render(request, "commerce_app/iphone13_promax_128gb.html")

def iphone13_pro_128gb(request):
    return render(request, "commerce_app/iphone13_pro_128gb.html")

def iphone13_pro_256gb(request):
    return render(request, "commerce_app/iphone13_pro_256gb.html")

#applewatch products
def applewatch_series8(request):
    return render(request, "commerce_app/applewatch_series8.html")

def applewatch_series7(request):
    return render(request, "commerce_app/applewatch_series7.html")

def xiaomi_watch(request):
    return render(request, "commerce_app/xiaomi_watch.html")

def huawei_watch(request):
    return render(request, "commerce_app/huawei_watch.html")

#coat products
def north_face(request):
    return render(request, "commerce_app/north_face.html")

def columbia(request):
    return render(request, "commerce_app/columbia.html")

def nike(request):
    return render(request, "commerce_app/nike.html")

def jack_jones(request):
    return render(request, "commerce_app/jack_jones.html")

#about
def about(request):
    return render(request, "commerce_app/about.html")


def billing2(request):
    return render(request, "commerce_app/billing2.html")