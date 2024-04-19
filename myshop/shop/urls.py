from django.urls import path
from .views import home, add_item, update_item

urlpatterns = [
    path('', home, name='home'),
    path('add_item/', add_item, name='add_item'),
    path('update_item/', update_item, name='update_item'),
]
