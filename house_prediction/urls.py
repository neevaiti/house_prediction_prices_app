from django.contrib import admin
from django.urls import path
from house_price import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estimation/', views.estimation),
    path('votre-prix/', views.estimate, name="votre-prix")
]
