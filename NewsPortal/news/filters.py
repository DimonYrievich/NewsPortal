# В fields содержится словарь настройки самих фильтров. Ключами являются названия полей модели, а значениями выступают списки
# операторов фильтрации. Именно те, которые мы можем указать при составлении запроса.
# Например, Product.objects.filter(price__gt=10)
# Список операторов можно посмотреть по ссылке:	https://docs.djangoproject.com/en/4.0/ref/models/querysets/#field-lookups
# По настройке внешнего вида фильтров и способа фильтрации см.  ниже с применением ModelChoiceFilter

from django_filters import FilterSet, ModelChoiceFilter, DateFilter
from .models import Post, Category, Author
import django.forms

# Создаем свой набор фильтров для модели Post
# FilterSet, который мы наследуем, должен чем-то напомнить знакомые нам Django дженерики.
# ModelChoiceFilter - это выбор модели фильтра (как он будет выглядеть)

class PostFilter(FilterSet):
    category = ModelChoiceFilter(
            field_name='categories',
            queryset=Category.objects.all(),
            label='Категория',
            empty_label='----------------'
        )
    author = ModelChoiceFilter(
        field_name='author',
        queryset=Author.objects.all(),
        label='Автор',
        empty_label='---------------------'
    )
# Далее кусок кода для фильтрации по дате, но я его не включил в проект
#    posting_time = DateFilter(
#        lookup_expr='gte',
#        widget=django.forms.DateInput(
#            attrs={
#                'type': 'date'
#            }
#        ))

    class Meta:
        # В Meta классе мы должны указать Django модель, в которой будем фильтровать записи.
        model = Post
        # В fields мы описываем по каким полям модели будет производиться фильтрация.
        fields = {
            # поиск по категориям
            #'author': ['exact'],
            # поиск по авторам
            #'categories': ['exact'],
        }
