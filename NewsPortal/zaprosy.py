>>> #Создать двух пользователей
>>> User.objects.create_user('Иванов Иван Иванович')
<User: Иванов Иван Иванович>
>>> User.objects.create_user('Халитов Руслан Рустамович')
<User: Халитов Руслан Рустамович>
>>>
>>> #Создать два объекта модели Author
>>> author5 = Author(user_id=5)
>>> author6 = Author(user_id=6)
>>> author6.save()
>>> author5.save()
>>>
>>> #Добавить 4 категории в модель Category
>>> category1 = Category(name_of_category = 'Спорт')
>>> category1.save()
>>> category2 = Category(name_of_category = 'Политика')
>>> category2.save()
>>> category3 = Category(name_of_category = 'Образование')
>>> category3.save()
>>> category4 = Category(name_of_category = 'Погода')
>>> category4.save()
>>>
>>> #Добавить 2 статьи и 1 новость.
>>> post1 = Post.objects.create(author = author5, topic = 'Влияние санкций на уровень образования', text_of_topic = 'Влияние санкций на уровень образования в учебных заведениях пока не представляется возможным. Вот такие пироги!')
>>> post1.save()
>>> post2 = Post.objects.create(author = author6, topic = 'Обзор на Hogwarts Legacy', text_of_topic = 'Еще не поиграл, но уже очень нравится. 10 из 10')
>>> post2.save()
>>> post3 = Post.objects.create(author = author6, topic = 'Зима никак не уходит', text_of_topic = 'Уже середина марта, а в Санкт-Петербурге зима продолжает царствовать. Столбики термометра не поднимаются выше 0 градусов, и выпадает
тонна снега. Раудет только одно,наконец-то увеличилась продолжительность светлого времени суток. Надеюсь в апреле зима отступит и передаст брозды правления весне', var = 'Статья')
>>> post3.save()
>>> Post.objects.all()
<QuerySet [<Post: Post object (4)>, <Post: Post object (5)>, <Post: Post object (6)>]>
>>>
>>> #Присвоить им категории
>>> PostCategory.objects.create(category_id = 6, post_id = 4)
<PostCategory: PostCategory object (6)>
>>> PostCategory.objects.create(category_id = 7, post_id = 4)
<PostCategory: PostCategory object (7)>
>>> PostCategory.objects.create(category_id = 5, post_id = 5)
<PostCategory: PostCategory object (8)>
>>> PostCategory.objects.create(category_id = 8, post_id = 6)
<PostCategory: PostCategory object (9)>
>>>
>>> #Создать как минимум 4 комментария к разным объектам модели Post
>>> Comment.objects.create(text_of_comment = "Информативно. Пироги без начинки. Не понравилось.", post_id = 4, user_id = 6)
<Comment: Comment object (5)>
>>> Comment.objects.create(text_of_comment = "Жду-не дождусь твой новый обзор. Твой пост не относится к категории Спорт", post_id = 4, user_id = 6)
<Comment: Comment object (6)>
>>> Comment.objects.create(text_of_comment = "Вторую половину марта синоптики обещают тепловй", post_id = 6, user_id = 5)
<Comment: Comment object (7)>
>>> Comment.objects.create(text_of_comment = "Будем надеяться", post_id = 6, user_id = 6)
<Comment: Comment object (8)>
>>>
>>> #Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов
>>> Post1_l = Post.objects.all()[0]
>>> Post1_l.like()
>>> Post1_l.like()
>>> Post1_l.like()
>>> Post1_l.like()
>>> Post1_l.like()
>>> Post1_l1 = Post.objects.all()[1]
>>> Post1_l1.like()
>>> Post1_l1.like()
>>> Post1_l1.like()
>>> Post1_l1.like()
>>> Post1_l1.like()
>>> Post1_l1.like()
>>> Post1_l1.like()
>>> Post1_l1.like()
>>> Post1_l1.like()
>>> Post1_l1.dislike()
>>> Post1_l1.dislike()
>>> Post1_l1.dislike()
>>>
>>> Post1_l1.dislike()
>>> Post1_l11 = Post.objects.all()[2]
>>> Post1_l11.like()
>>> Post1_l11.like()
>>> Post1_l11.like()
>>>
>>> Post1_l11.like()
>>> Post1_l11.like()
>>> Post1_l11.like()
>>> Post1_l11.like()
>>> Post1_l11.like()
>>> comment1 = Comment.objects.all()[0]
>>> comment2 = Comment.objects.all()[1]
>>> comment3 = Comment.objects.all()[2]
>>> comment4 = Comment.objects.all()[3]
>>> comment1.like()
>>> comment1.like()
>>> comment1.like()
>>> comment1.like()
>>> comment1.like()
>>> comment1.like()
>>> comment1.like()
>>> comment1.like()
>>> comment1.like()
>>> comment1.like()
>>> comment2.like()
>>> comment3.like()
>>> comment3.like()
>>> comment3.like()
>>> comment3.like()
>>> comment3.like()
>>> comment3.like()
>>> comment3.like()
>>> comment3.like()
>>> comment4.like()
>>> comment4.like()
>>> comment4.like()
>>> comment3.dislike()
>>>
>>> #Обновить рейтинги пользователей
>>> Author5 = Author.objects.all()[0]
>>> Author6 = Author.objects.all()[1]
>>> Author5.update_rating()
>>> Author6.update_rating()
>>>
>>> #Вывести username и рейтинг лучшего пользователя
>>> Author.objects.order_by('rate_of_author').last().user
<User: Халитов Руслан Рустамович>
>>> Author.objects.order_by('rate_of_author').last().rate_of_author
63
>>>
>>> #Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
>>> Post.objects.order_by('time_post').first().time_post - Дата добавления
  File "<console>", line 1
    Post.objects.order_by('time_post').first().time_post - Дата добавления
                                                                ^
SyntaxError: invalid syntax
>>> Post.objects.order_by('datetime_of_post').first().datetime_of_post
datetime.datetime(2023, 3, 12, 19, 40, 38, 21052, tzinfo=datetime.timezone.utc)
>>> Post.objects.order_by('rate_of_post').first().author.user.username
'Иванов Иван Иванович'
>>> Post.objects.order_by('rate_of_post').first().rate_of_post
5
>>> Post.objects.order_by('topic').first().topic
'Влияние санкций на уровень образования'

>>> previewtoppost = Post.objects.all()[2]
>>> previewtoppost.preview()
