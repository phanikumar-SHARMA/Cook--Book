from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ensure this line is present
    path('add/', views.add_recipe, name='add_recipe'),
    path('store/', views.food_store, name='food_store'),
    path('about/',views.about,name = "about"),
    path('explore/',views.explore,name = "explore"),
    path('like/<int:recipe_id>/', views.like_recipe, name='like_recipe'),
]