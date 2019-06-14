from django.urls import path
from . import views

urlpatterns=[

    path('CookingApp/', views.index, name='index'),

    path('Recipes/', views.getRecipes, name='recipes'),

    path('recipedetails/<int:id>/', views.recipeDetails, name='recipedetails'),

    path('newRecipe/', views.newRecipe, name='newrecipe'),

    path('newReview/', views.newReview, name='newreview'),

    path('loginmessage/', views.loginmessage, name='loginmessage'),

    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),



]