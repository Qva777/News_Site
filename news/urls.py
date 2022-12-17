from .views import *
from django.urls import path
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(HomeNews.as_view()), name='home'),
    # Login | Logout
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    # View
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),

    path("search/", SearchResultsView.as_view(), name="search_results"),
]
