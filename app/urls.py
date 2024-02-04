
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from app import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls", namespace="main")),
    path("catalog/", include("goods.urls", namespace="catalog")),
    path("user/", include("users.urls", namespace="user")),
    path("cart/", include("carts.urls", namespace="cart")),
    path("orders/", include("orders.urls", namespace="orders")),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""
orders/': Указывает префикс URL-пути, который будет обрабатываться этим маршрутом.
 все URL-пути, начинающиеся с 'orders/' будут переданы в обработку приложению, связанному с 'orders.urls'.

include('orders.urls', namespace='orders'): Используется для включения URL-маршрутов из другого приложения.
 orders.urls представляет собой модуль с URL-маршрутами для управления заказами. namespace='orders' 
 добавляет пространство имен "orders" для этих URL-путей, что полезно, когда есть несколько приложений с
   одинаковыми именами URL.

Таким образом, этот код создает префикс 'orders/' для всех URL-путей, определенных в файле orders.urls,
 и предоставляет пространство имен "orders" для удобства их использования и отделения их от URL-путей других частей
приложения.

"""
