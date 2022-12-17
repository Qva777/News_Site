from .utils import MyMixin
from .models import News, Category
from django.contrib import messages
from django.contrib.auth import login, logout

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .forms import UserRegisterForm, UserLoginForm


def register(request):
    """ Method which registering a user """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You have successfully registered!')
            return redirect('home')
        else:
            messages.error(request, 'Error')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {"form": form})


def user_login(request):
    """ Method which login a user """
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {"form": form})


def user_logout(request):
    """ Method which logout a user """
    logout(request)
    return redirect('home')


class HomeNews(MyMixin, ListView):
    """ Additional context for news list """
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        """ Changed context title """
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Main page')
        return context

    def get_queryset(self):
        """ Return news which published """
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(MyMixin, ListView):
    """ Additional context for news category """
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        """ Changed context title's category """
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
        return context

    def get_queryset(self):
        """ Return category which published"""
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewNews(DetailView):
    """ Detail view  news 'read more' """
    model = News
    context_object_name = 'news_item'


class SearchResultsView(ListView):
    """ Return news queryset by title """
    model = News
    template_name = 'news/search_results.html'

    def get_queryset(self):
        """ Search by title """
        query = self.request.GET.get("q")
        object_list = News.objects.filter(title__icontains=query)
        return object_list
