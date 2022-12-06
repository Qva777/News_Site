from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),

    path('register/', register, name='register'),
    path('login/', login, name='login'),


    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),

    path('news/add_news/', CreateNews.as_view(), name='add_news'),

]
