from django.urls import path
from .views import login_page, register_page, home,create_battle,battle_details,minted_nft

urlpatterns = [
    path('', home, name='home'),
    path('create/', create_battle, name='create_battle'),
    path('details/<id>', battle_details, name='battle_details'),
    path('nft/', minted_nft, name='minted_nft'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
]
