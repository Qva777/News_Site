from django.db import models
from django.urls import reverse

from django.contrib.auth.models import UserManager, AbstractUser, User
from django.db import models


# class NewsRate(models.TextChoices):
#     """ Choice mark for news """
#     FINE = (1, "Fine")
#     MEDIUM = (2, "Not bab")
#     BAD = (3, "Bad")


class News(models.Model):
    """ Model news in database """
    title = models.CharField(max_length=150, verbose_name='Name')
    content = models.TextField(blank=True, verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Photo', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Is Published')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Category')
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Name')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']



class UserNewsRelation(models.Model):
    Choise = {(1, "Fine"),
              (2, "Not bab"),
              (3, "Bad")
              }
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(News, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    in_bookmarks = models.BooleanField(default=False)
    rate = models.PositiveIntegerField(choices=Choise)

    def __str__(self):
        return f'{self.user.username}: {self.book.title} Rate - {self.rate}'