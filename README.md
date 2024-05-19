In [4]: models.Animal.objects.all()
Out[4]: <QuerySet [<Animal: Зебра>, <Animal: Акула>, <Animal: Хамелион>, <Animal: Бенгальский тигр>, <Animal: Корелла>]>

In [5]: list(models.Animal.objects.all())
Out[5]:
[<Animal: Зебра>,
 <Animal: Акула>,
 <Animal: Хамелион>,
 <Animal: Бенгальский тигр>,
 <Animal: Корелла>]

In [6]: models.Sot.objects.first()
Out[6]: <Sot: Иван Иванов>

In [7]: models.Sot.objects.last()
Out[7]: <Sot: Георгий Родионов>

In [8]: models.Sot.objects.count()
Out[8]: 4

In [9]: models.Sot.objects.order_by('last_name')
Out[9]: <QuerySet [<Sot: Александр Александров>, <Sot: Иван Иванов>, <Sot: Петр Петров>, <Sot: Георгий Родионов>]>

In [10]: models.Sot.objects.order_by('-last_name')
Out[10]: <QuerySet [<Sot: Георгий Родионов>, <Sot: Петр Петров>, <Sot: Иван Иванов>, <Sot: Александр Александров>]>

In [11]: models.Animal.objects.filter(name__contains='a') #Тут английска А
Out[11]: <QuerySet []>

In [12]: models.Animal.objects.filter(name__contains='а')
Out[12]: <QuerySet [<Animal: Зебра>, <Animal: Акула>, <Animal: Хамелион>, <Animal: Бенгальский тигр>, <Animal: Корелла>]>

In [13]: models.Sot.objects.filter(salary__gt=100000)
Out[13]: <QuerySet []>

In [14]: models.Sot.objects.filter(salary__gt=20000)
Out[14]: <QuerySet [<Sot: Петр Петров>, <Sot: Александр Александров>, <Sot: Георгий Родионов>]>

In [15]: models.Sot.objects.filter(salary__gt=80000)
Out[15]: <QuerySet [<Sot: Петр Петров>, <Sot: Александр Александров>]>

In [23]: models.Sot.objects.exclude(first_name__contains='П')
Out[23]: <QuerySet [<Sot: Иван Иванов>, <Sot: Александр Александров>, <Sot: Георгий Родионов>]>

In [24]: models.Sot.objects.values('first_name','last_name')
Out[24]: <QuerySet [{'first_name': 'Иван', 'last_name': 'Иванов'}, {'first_name': 'Петр', 'last_name': 'Петров'}, {'first_name': 'Александр', 'last_name': 'Александров'}, {'first_name': 'Георгий', 'last_name': 'Родионов'}]>

In [25]: models.Sot.objects.dates('date_of_birth','day')
Out[25]: <QuerySet [datetime.date(1999, 5, 19), datetime.date(2024, 5, 1), datetime.date(2024, 5, 18), datetime.date(2024, 5, 19)]>

In [27]: models.Sot.objects.filter(id=2).values('first_name','last_name')
Out[27]: <QuerySet [{'first_name': 'Петр', 'last_name': 'Петров'}]>

In [28]: models.Matematic.objects.filter(id__gt=3).delete()
Out[28]: (3, {'core.Matematic': 3})

In [29]: models.Matematic.objects.filter(id__gt=3).delete()
Out[29]: (0, {})

In [30]: models.Matematic.objects.filter(id=1).update(long_text='Заменяем длинный текст')
Out[30]: 0

In [36]: models.Matematic.objects.create(name='Текст', long_text='Длинный текст. Честно тут очень длинный текст')
Out[36]: <Matematic: тскеТ>

In [37]: models.Sot.objects.filter(salary__lt=100000)
Out[37]: <QuerySet [<Sot: Иван Иванов>, <Sot: Георгий Родионов>]>

In [38]: models.Sot.objects.filter(salary__lte=100000)
Out[38]: <QuerySet [<Sot: Иван Иванов>, <Sot: Петр Петров>, <Sot: Александр Александров>, <Sot: Георгий Родионов>]>

In [39]: models.Animal.objects.filter(id=6).update(is_rare=True)
Out[39]: 0

In [40]: models.Animal.objects.filter(id=2).update(is_rare=True)
Out[40]: 1

