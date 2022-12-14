from django.views.generic.list import ListView   #добавил .list , согласно документации в Django
from .models import Post

class ListPost(ListView):           # Создаем свой класс, который наследуется от ListView
    model = Post                    # Указываем модель, объекты которой мы будем выводить
    post_title = 'title'            # Поле, которое будет использоваться для сортировки объектов (необязательно)
    post_template = 'posts.html'     # Указываем имя шаблона, в котором будут все инструкции о том, как именно пользователю должны быть показаны наши объекты
    context_object_name = 'posts'   # Имя списка, в котором будут лежать все объекты. Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.