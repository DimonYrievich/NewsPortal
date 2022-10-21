#1.Создать двух пользователей (с помощью метода User.objects.create_user('username')):

from django.contrib.auth.models import User

user_1 = User.objects.create_user(username='Daria Gusina', password='322223')
user_2 = User.objects.create_user(username='Dmitriy Kubik', email='dmitriy@mail.ru')
user_3 = User.objects.create_user(username='Yana Yana')

##################################################################################################################################
#2.Создать три объекта модели Author, связанные с пользователями (привязка пользователя к автору).

from news.models import Author

author_1 = Author.objects.create(name_author=User.objects.get(username='Dmitriy Kubik')) #!!!Почему-то в БД создается
author_2 = Author.objects.create(name_author=User.objects.get(username='Daria Gusina'))  #поле name_author_id вместо
author_3 = Author.objects.create(name_author=User.objects.get(id=10))                    #name_author!!! Возможно, нужен
                                                                                         #другой метод (вместо get)
##################################################################################################################################
#3.Добавить 4 категории в модель Category.

from news.models import Category

category_1 = Category.objects.create(name_category='Спорт')
category_2 = Category.objects.create(name_category='Политика')
category_3 = Category.objects.create(name_category='Образование')
category_4 = Category.objects.create(name_category='Технологии')
category_5 = Category.objects.create(name_category='Кино')

#################################################################################################################################################
# 4. Создание постов

from news.models import Post

post_1 = Post.objects.create(author = Author.objects.get(name_author=9), title='Южная Корея', text="«Было решено»", article_or_news ='new')
post_2 = Post.objects.create(author = Author.objects.get(pk=1), title='Тест', text="«Привет!»", article_or_news ='art')
post_3 = Post.objects.create(author=Author.objects.get(pk=1), title='Южная Корея ввела санкции против КНДР', text="Южная Корея вводит собственные санкции против 15 физических лиц и 16 организаций из КНДР, связанных с недавними пусками ракет. Об этом сообщает агентство Yonhap со ссылкой на Министерство иностранных дел. "
                                                                                                        "«Было решено ввести дополнительные санкции против 15 физических лиц и 16 организаций Северной Кореи, которые способствовали развитию ракетно-ядерной программы Северной Кореи или уклонению от санкций», — сообщили в южнокорейском внешнеполитическом ведомстве. "
                                                                                                        "6 октября КНДР запустила две баллистические ракеты в сторону Японского моря. Этот пуск стал шестым за неделю. Власти страны назвали это ответом на учения США и Южной Кореи. "
                                                                                                        "9 сентября КНДР официально провозгласила себя ядерным государством. По новому законодательству, правом на любые решения единолично обладает лидер страны Ким Чен Ын. Декрет также закрепляет за КНДР право нанесения превентивного ядерного удара по противнику.", article_or_news ='new')
post_4 = Post.objects.create(author=Author.objects.get(pk=2), title='Евлоев снялся с боя UFC против Митчелла', text="Российский боец смешанных единоборств (ММА) Мовсар Евлоев снялся с поединка в полулегкой весовой категории против американца Брайса Митчелла на турнире Абсолютного бойцовского чемпионата (UFC), сообщает MMA Junkie. "
                                                                                                                    "Евлоев должен был встретиться с Митчеллом в главном бою вечера на турнире UFC Fight Night 214 в Лас-Вегасе (США) 5 ноября. Поединок был согласован в прошлом месяце. "
                                                                                                                    "За свою профессиональную карьеру 28-летний Евлоев не потерпел ни одного поражения в ММА при 16 победах. У 28-летнего Митчелла 15 побед и также ни одного поражения. Митчелл и Евлоев занимают девятое и десятое места в рейтинге UFC в полулегком весе соответственно.", article_or_news = 'new')
Post.objects.create(author=Author.objects.get(name_author=10), title="«Шантарам»: какой получилась экранизация одного из главных романов XXI века", text="14 октября на Apple TV+ стартует сериал «Шантарам» — почти такой же внушительный, как оригинальный роман Грегори Дэвида Робертса. Экранизировать монументальное произведение пытались "
                                                                                                                                                        "последние 20 лет, но только сейчас литературный источник сумел обрести свою киношную плоть. Кинокритик «Пампарам.Ru» Yana Yana рассказывает, какой получилась экранизация бестселлера — "
                                                                                                                                                        "и стоила ли она всех ожиданий.", article_or_news = 'article')

##################################################################################################################################################
# 5. Присваивание поста к категории

from news.models import PostCategory
from news.models import Post
from news.models import Category

PostCategory.objects.create(post = Post.objects.get(pk=1), category = Category.objects.get(name_category = 'Политика'))
PostCategory.objects.create(post = Post.objects.get(pk=2), category = Category.objects.get(name_category = 'Образование'))
PostCategory.objects.create(post = Post.objects.get(pk=3), category = Category.objects.get(name_category = 'Политика'))
PostCategory.objects.create(post = Post.objects.get(pk=4), category = Category.objects.get(name_category = 'Спорт'))
PostCategory.objects.create(post = Post.objects.get(pk=5), category = Category.objects.get(name_category = 'Кино'))

#################################################################################################################################################
# 6. Написание комментариев

from news.models import Comment
from django.contrib.auth.models import User
from news.models import Post

comment_1 = Comment.objects.create(post = Post.objects.get(pk=1), user = User.objects.get(username = 'Daria Gusina'), text_comment = 'Так и не понятно, что было решено...')
Comment.objects.create(post = Post.objects.get(pk=2), user = User.objects.get(id=9), text_comment = 'Это тестовый пост, не обращайте на него внимание.')
comment_3 = Comment.objects.create(post = Post.objects.get(pk=3), user = User.objects.get(username = 'Daria Gusina'), text_comment = 'Теперь всё понятно! Всем пи..ц!:)')
comment_4 = Comment.objects.create(post = Post.objects.get(pk=4), user = User.objects.get(username = 'Yana Yana'), text_comment = 'Разжирел! Вот и пришлось сняться с поединка')
Comment.objects.create(post = Post.objects.get(pk=5), user = User.objects.get(username = 'Dmitriy Kubik'), text_comment = 'Рекомендасьён к просмотру')

#################################################################################################################################################
# 7. Применение методов лайк/дизлайк

from news.models import Post
from news.models import Comment

Comment.objects.get(pk=1).like()
Comment.objects.get(pk=3).like()
Comment.objects.get(pk=5).like()
Comment.objects.get(pk=5).like()
Comment.objects.get(pk=4).like()
Comment.objects.get(pk=4).like()
Comment.objects.get(pk=4).dislike()
Post.objects.get(pk=3).like()
Post.objects.get(pk=4).like()
Post.objects.get(pk=3).like()
Post.objects.get(pk=4).like()
Post.objects.get(pk=5).like()
Post.objects.get(pk=5).like()
Post.objects.get(pk=5).like()
Post.objects.get(pk=3).dislike()
Post.objects.get(pk=4).dislike()

###################################################################################################################################################
# 8. Обновление рейтинга пользователей

from news.models import Author

Author.objects.get(pk=1).update_rating()
Author.objects.get(pk=2).update_rating()
Author.objects.get(pk=3).update_rating()

#####################################################################################################################################
# 9. Вывести username и рейтинг лучшего пользователя (не проверял!!!!!!!!!!!!)

Author.objects.all().order_by('-_rating').values('user', '_rating')[0]

# 10. Вывести дату добавления, автора, рейтинг, заголовок и превью лучшей статьи (не проверял!!!!!!!!!!!!!!!)

Post.objects.all().order_by('-_rating').values('pub_time', 'author', '_rating', 'title')[0]
best_post = Post.objects.all().order_by('-_rating')[0]
best_post.preview()

# 11. Вывести все комментарии к этой статье (не проверял!!!!!!!!!!!!!!!!!!!!)

Comment.objects.filter(post = best_post).values('pub_time', 'user', '_rating', 'text')


