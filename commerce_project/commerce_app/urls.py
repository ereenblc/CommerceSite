from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [

    # Home Page Products
    path("", views.index, name="index"), 
    path("alfa_awus/", views.alfa_awus, name="alfa_awus"), 
    path("grundig/", views.grundig, name="grundig"), 
    path("rival3/", views.rival3, name="rival3"), 
    path("airpods2/", views.airpods2, name="airpods2"), 
    path("stanley/", views.stanley, name="stanley"), 
    path("iphone13/", views.iphone13, name="iphone13"), 
    path("applewatch/", views.applewatch, name="applewatch"), 
    path("army_coat/", views.army_coat, name="army_coat"), 

    # Wifi Card Products
    path("xiaomi_mi/", views.xiaomi_mi, name="xiaomi_mi"), 
    path("alfa_uw07/", views.alfa_uw07, name="alfa_uw07"), 
    path("asus_usb/", views.asus_usb, name="asus_usb"), 
    path("tp_link/", views.tp_link, name="tp_link"), 

    # Television Products
    path("toshiba_tv/", views.toshiba_tv, name="toshiba_tv"), 
    path("samsung_tv/", views.samsung_tv, name="samsung_tv"), 
    path("philips_tv/", views.philips_tv, name="philips_tv"), 
    path("regal_tv/", views.regal_tv, name="regal_tv"),

    # PC Equipmant Products
    path("asus_mouse/", views.asus_mouse, name="asus_mouse"),
    path("logitech_keyboard/", views.logitech_keyboard, name="logitech_keyboard"),
    path("logitech_mouse/", views.logitech_mouse, name="logitech_mouse"),
    path("medusa_headset/", views.medusa_headset, name="medusa_headset"),

    # Earphones Product
    path("airpods_pro/", views.airpods_pro, name="airpods_pro"),
    path("oppo_earphones/", views.oppo_earphones, name="oppo_earphones"),
    path("huawei_earphones/", views.huawei_earphones, name="huawei_earphones"),
    path("airpods_headset/", views.airpods_headset, name="airpods_headset"),

    # Thermos Products
    path("stanley_neverleak/", views.stanley_neverleak, name="stanley_neverleak"),
    path("stanley_vacuum/", views.stanley_vacuum, name="stanley_vacuum"),
    path("stanley_food/", views.stanley_food, name="stanley_food"),
    path("stanley_mug/", views.stanley_mug, name="stanley_mug"),

    #iPhone Products
    path("iphone13_pro_1tb/", views.iphone13_pro_1tb, name="iphone13_pro_1tb"),
    path("iphone13_pro_128gb/", views.iphone13_pro_128gb, name="iphone13_pro_128gb"),
    path("iphone13_pro_256gb/", views.iphone13_pro_256gb, name="iphone13_pro_256gb"),
    path("iphone13_promax_128gb/", views.iphone13_promax_128gb, name="iphone13_promax_128gb"),

    #applewatch products
    path("applewatch_series7/", views.applewatch_series7, name="applewatch_series7"),
    path("applewatch_series8/", views.applewatch_series8, name="applewatch_series8"),
    path("xiaomi_watch/", views.xiaomi_watch, name="xiaomi_watch"),
    path("huawei_watch/", views.huawei_watch, name="huawei_watch"),

    #Coat Products
    path("north_face/", views.north_face, name="north_face"),
    path("columbia/", views.columbia, name="columbia"),
    path("jack_jones/", views.jack_jones, name="jack_jones"),
    path("nike/", views.nike, name="nike"),

    #about
    path("about/", views.about, name="about"),
    path("billing2/", views.billing2, name="billing2"),



    path("billing/", views.billing, name="billing"), 
]
