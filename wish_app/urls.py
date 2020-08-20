from django.urls import path
from . import views, actions

urlpatterns = [
    path('', views.wish_wall),
    path('make_wish/', views.make_wish),
    path('create_wish/', actions.create_wish),
    path('edit/<int:wish_id>/', views.edit_wish),
    path('edit_wish/<int:wish_id>/', actions.edit_wish),
    path('remove/<int:wish_id>/', actions.remove_wish),
    path('granted/<int:wish_id>/', actions.grant_wish),
    path('like/<int:wish_id>/', actions.like_wish),
    path('stats/', views.stats)
]