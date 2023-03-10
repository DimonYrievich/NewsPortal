
from django.urls import path
from .views import PostsList, \
    PostDetail, \
    PostCreate, \
    PostUpdate, \
    PostDelete, \
    PostSearch, \
    CategoryListView, \
    subscribe, \
    NewsCreate, \
    ArticleCreate, \
    NewsList, \
    ArticlesList, \
    ContactsList                # Импортируем все созданные нами представления

urlpatterns = [
    path('', PostsList.as_view(), name='posts'),   # Путь ко всем постам останется пустым, т.к. все последующие пути должны прикрепляться к 'cheburashka/'
    path('<int:pk>', PostDetail.as_view(), name='post'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('news/', NewsList.as_view(), name='news_list'),
    path('articles/', ArticlesList.as_view(), name='articles_list'),
    path('contacts/', ContactsList.as_view(), name='contacts_list'),
    #path('news/create/', NewsCreate.as_view(), name='news_create'),
    #path('articles/create/', ArticleCreate.as_view(), name='articles_create'),
    #path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('categories/<int:pk>/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe/', subscribe, name='subscribe'),
    ]

	# path — означает путь.
	# Т.к. наше объявленное представление является классом, а Django ожидает функцию, нам надо представить этот класс в виде view.
	# Для этого вызываем метод as_view.
    # pk — это первичный ключ публикации, который будет выводиться у нас в шаблон
    # int — указывает на то, что принимаются только целочисленные значения