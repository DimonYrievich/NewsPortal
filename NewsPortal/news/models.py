from django.db import models
from django.contrib.auth.models import User    #Встроенная модель пользователей User
from django.db.models import Sum

#############################################################################################################

class Author(models.Model):
    name_author = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.PROTECT)        #cвязь «один к одному» с встроенной моделью User
    rating = models.IntegerField(default = 0)

# !!!Далее будет украденный кусок кода, который немного изменен и в котором я так ничего толком и не понял!!!

    def update_rating(self):
        a = Post.objects.filter(id_author=self.id).aggregate(Sum('rating'))['rating__sum'] * 3
        b = Comment.objects.filter(id_user=self.id_user).aggregate(Sum('rating_comment'))['rating_comment__sum']
        c = Post.objects.filter(id_author=self.id).values('id')
        d = 0
        for i in c:
            com = Comment.objects.filter(id_post=i['id']).aggregate(Sum('rating_comment'))['rating_comment__sum']
            if com != None:
                d += com
        self.rating = a + b + d
        self.save()

#############################################################################################################

sport = 'sp'
politics = 'pol'
education = 'ed'
technology = 'tech'
movie = 'mov'

POSITIONS = [
    (sport, 'Спорт'),
    (politics, 'Политика'),
    (education, 'Образование'),
    (technology, 'Технологии'),
    (movie, 'Кино')
]

class Category(models.Model):
    name_category = models.CharField(max_length=30, choices = POSITIONS, default = technology, unique = True)

###############################################################################################################

article = 'art'
news = 'new'

PUBLICATION = [
    (article, 'Статья'),
    (news, 'Новость')
]

class Post(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    article_or_news = models.CharField(max_length=30, choices = PUBLICATION, default = news)
    title = models.CharField(max_length=30)
    text = models.TextField()
    rating = models.IntegerField(default = 0)

    author = models.ForeignKey('Author', on_delete=models.CASCADE)  #связь «один ко многим» с моделью Author

    categories = models.ManyToManyField('Category', through = 'PostCategory')  #связь «многие ко многим» с моделью Category
                                                                               # (с дополнительной моделью PostCategory);
    def preview(self):                    # Метод preview() модели Post, который возвращает начало статьи (предварительный
        return self.text[0:125] + "..."                     # просмотр) длиной 124 символа и добавляет многоточие в конце.

    @property
    def rating_post(self):
        return self.rating

    @rating_post.setter
    def rating_post(self, value):
        self.rating = int(value) if value >= 0 else 0
        self.save()

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

###############################################################################################################
                                            #Промежуточная таблица
class PostCategory(models.Model):
    post = models.ForeignKey("Post", on_delete=models.PROTECT)
    category = models.ForeignKey("Category", on_delete=models.PROTECT)

###############################################################################################################

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)      #связь «один ко многим» с моделью Post
    user = models.ForeignKey(User, on_delete=models.PROTECT)        #связь «один ко многим» со встроенной моделью User
    text_comment = models.CharField(max_length=500)                 #текст комментария
    time_in_comment = models.DateTimeField(auto_now_add=True)       #дата и время создания комментария
    rating_comment = models.IntegerField(default = 0)               #рейтинг комментария

    @property
    def comment_rating(self):
        return self.rating_comment

    @comment_rating.setter
    def comment_rating(self, value):
        self.rating_comment = int(value) if value >= 0 else 0
        self.save()

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -= 1
        self.save()

################################################################################################################
                                        # Это Проект News Portal
#Что в нём должно быть?

#1.Модель Author
#        Модель, содержащая объекты всех авторов.
#        Имеет следующие поля:
#            - cвязь «один к одному» с встроенной моделью пользователей User;
#            - рейтинг пользователя. Ниже будет дано описание того, как этот рейтинг можно посчитать.
#2.Модель Category
#        Категории новостей/статей — темы, которые они отражают (спорт, политика, образование и т. д.).
#        Имеет единственное поле: название категории. Поле должно быть уникальным (в определении поля необходимо
#        написать параметр unique = True).
#3.Модель Post
#        Эта модель должна содержать в себе статьи и новости, которые создают пользователи. Каждый объект может иметь
#        одну или несколько категорий.
#        Соответственно, модель должна включать следующие поля:
#            - связь «один ко многим» с моделью Author;
#            - поле с выбором — «статья» или «новость»;
#            - автоматически добавляемая дата и время создания;
#            - связь «многие ко многим» с моделью Category (с дополнительной моделью PostCategory);
#            - заголовок статьи/новости;
#            - текст статьи/новости;
#            - рейтинг статьи/новости.
#4.Модель PostCategory
#        Промежуточная модель для связи «многие ко многим»:
#            - связь «один ко многим» с моделью Post;
#            - связь «один ко многим» с моделью Category.
#5.Модель Comment
#        Под каждой новостью/статьёй можно оставлять комментарии, поэтому необходимо организовать их способ хранения тоже.
#        Модель будет иметь следующие поля:
#            - связь «один ко многим» с моделью Post;
#            - связь «один ко многим» со встроенной моделью User (комментарии может оставить любой пользователь, необязательно автор);
#            - текст комментария;
#            - дата и время создания комментария;
#            - рейтинг комментария.

#Эти модели должны также реализовать методы:

#1.Методы like() и dislike() в моделях Comment и Post, которые увеличивают/уменьшают рейтинг на единицу.
#2.Метод preview() модели Post, который возвращает начало статьи (предварительный просмотр) длиной 124 символа и
#  добавляет многоточие в конце.
#3.Метод update_rating() модели Author, который обновляет рейтинг пользователя, переданный в аргумент этого метода.
#  Он состоит из следующего:
#    - суммарный рейтинг каждой статьи автора умножается на 3;
#    - суммарный рейтинг всех комментариев автора;
#    - суммарный рейтинг всех комментариев к статьям автора.