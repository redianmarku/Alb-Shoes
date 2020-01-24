from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'kreu'

urlpatterns = [
    path('', views.kryefaqja, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('produkte/', views.produkte, name='produkte'),
    path('kategorite/', views.kategorite, name='kategorite'),
    path('shporta/', views.shporta, name='shporta'),
    path('pagesa/', views.pagesa, name='pagesa'),
    path('kontakt/', views.kontakt, name='kontakt'),
    path('fshij/<int:produkt_id>', views.fshij, name='fshij'),
    path('shto_shport/<int:produkt_id>', views.shto_shport, name='shto')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
