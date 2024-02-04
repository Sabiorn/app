from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('create-order/', views.create_order, name='create_order'),
]


'''
path('create-order/', views.create_order, name='create_order'):
Определение маршрута для создания заказа. Когда пользователь обращается к create_order/,
вызывается функция views.create_order. name='create_order' задает уникальное имя для этого маршрута
в пределах пространства имен orders.

<a href="{% url 'orders:create_order' %}">Создать заказ</a>
url = reverse('orders:create_order')

'''