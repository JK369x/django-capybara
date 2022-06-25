from django.urls import path
from .views import * #.views คือ folderเดียวกัน


urlpatterns = [
    path('', Home ,name = 'home-page'),
    path('service/', Service, name = 'service'),
    path('contact/', Contact, name = 'contact'),
    path('account/', Account, name = 'account'), #acc หน้าใช้ url webApp acc หลังใช้ใน base.html
    path('register/', Register, name = 'register-page'),
]