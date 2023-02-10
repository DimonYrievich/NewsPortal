
from django.urls import reverse_lazy
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post, Author
from .filters import PostFilter
from .forms import PostForm


class PostsList(ListView):          # ПРЕДСТАВЛЕНИЕ. Создаем свой класс, который наследуется от ListView (для отображения списка)
    model = Post                    # Указываем модель, объекты которой мы будем выводить
    post_title = 'title'            # Поле, которое будет использоваться для сортировки объектов (необязательно)
    template_name = 'posts.html'    # Указываем имя шаблона, в котором будут все инструкции о том, как именно пользователю должны быть показаны наши объекты
    context_object_name = 'posts'   # Имя списка, в котором будут лежать все объекты. Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    paginate_by = 8                 # ПАГИНАЦИЯ. Так мы можем указать количество записей на web-странице + нужно внести изменения в шаблоне HTML

   # Переопределяем функцию получения списка постов
    def get_queryset(self):
       # Получаем обычный запрос
       queryset = super().get_queryset()
       # Используем наш класс фильтрации.
       # self.request.GET содержит объект QueryDict, который мы рассматривали в этом юните ранее.
       # Сохраняем нашу фильтрацию в объекте класса,
       # чтобы потом добавить в контекст и использовать в шаблоне.
       self.filterset = PostFilter(self.request.GET, queryset)
       # Возвращаем из функции отфильтрованный список товаров
       return self.filterset.qs

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       # Добавляем в контекст объект фильтрации.
       context['filterset'] = self.filterset
       return context


class PostDetail(DetailView):          #ПРЕДСТАВЛЕНИЕ Создаем свой класс, который наследуется от DetailView (для отображения одного экземпляра таблицы из БД)
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostSearch(ListView):            #ПРЕДСТАВЛЕНИЕ Для возможности искать новости по определённым критериям
    model = Post
    ordering = '-posting_time'
    template_name = 'post_search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostCreate(CreateView, PermissionRequiredMixin):   #ПРЕДСТАВЛЕНИЕ Добавляем новое представление для создания постов.
    form_class = PostForm                                # Указываем нашу разработанную форму
    model = Post                                         # Указываем модель
    template_name = 'post_edit.html'                     # и новый шаблон, в котором используется форма.
    permission_required = ('news.add_post',
                           'news.delete_post',
                           'news.view_post',
                           'news.change_post',)          #добавил, но под??? см.ниже ПРЕДСТАВЛЕНИЕ: Ограничения и права доступа пользователя
    success_url = reverse_lazy('post_list')              #добавил

#    def form_valid(self, form):
#        post = form.save(commit=False)
#        post.choice_field = 'news'      # либо 'post' либо 'posts' ?????????????????????????
#        post.author = Author.objects.get(user=self.request.user)
#        return super().form_valid(form)


class PostUpdate(UpdateView):                           #ПРЕДСТАВЛЕНИЕ Добавляем еще одно представление для изменения публикации.
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    success_url = reverse_lazy('post_list')             # либо ('news_list') либо ('posts_list') ?????????????????????


class PostDelete(DeleteView):                           #ПРЕДСТАВЛЕНИЕ удаляющее публикацию.
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')             # либо ('news_list') либо ('posts_list'), но вроде бы всё правильно


class ArticlesPost(ListView):                           #ПРЕДСТАВЛЕНИЕ
    model = Post
    template_name = 'articles.html'
    context_object_name = 'articles'

class NewsPost(ListView):                               #ПРЕДСТАВЛЕНИЕ
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'


class NewsCreate(CreateView, PermissionRequiredMixin):  #ПРЕДСТАВЛЕНИЕ
    form_class = PostForm
    model = Post
    permission_required = ('news.add_post',
                           'news.delete_post',
                           'news.view_post',
                           'news.change_post',)
    template_name = 'post_edit.html'
    success_url = reverse_lazy('news_list')

#    def form_valid(self, form):
#        post = form.save(commit=False)
#        post.choice_field = 'news'
#        post.author = Author.objects.get(user=self.request.user)
#        return super().form_valid(form)


class ArticleCreate(CreateView, PermissionRequiredMixin):   #ПРЕДСТАВЛЕНИЕ
    form_class = PostForm
    model = Post
    permission_required = ('news.add_post',
                           'news.delete_post',
                           'news.view_post',
                           'news.change_post',)
    template_name = 'post_edit.html'
    success_url = reverse_lazy('news_list')

#    def form_valid(self, form):
#        post = form.save(commit=False)
#        post.choice_field = 'article'
#        post.author = Author.objects.get(user=self.request.user)
#        return super().form_valid(form)


#class MyView(PermissionRequiredMixin, CreateView):
#    permission_required = ('<app>.<action>_<model>',
#                           '<app>.<action>_<model>')
#ЭТОТ КУСОК ДОЛЖЕН БЫТЬ ЛИБО ЗДЕСЬ, ЛИБО в sing\views.py НЕ ПОНЯТНО!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class EditPost(PermissionRequiredMixin, CreateView):    # ПРЕДСТАВЛЕНИЕ: Ограничения и права доступа пользователя
    permission_required = ('news.add_post',
                           'news.delete_post',
                           'news.view_post',
                           'news.change_post',)