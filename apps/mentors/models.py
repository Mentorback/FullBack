from django.db import models
from apps.users.models import User
from django.contrib.postgres.fields import ArrayField
from django.conf import settings


class WorkTimes(models.Model):
    daystart = models.CharField(verbose_name='По будням с', max_length=20)
    dayend = models.CharField(verbose_name='до', max_length=20)
    weekends = models.CharField(verbose_name='По выходным с', max_length=20)
    weekende = models.CharField(verbose_name='до', max_length=20)

    def __str__(self):
        return f'daystart: {self.daystart}' \
               f'dayend: {self.dayend}' \
               f'weekends: {self.weekends}' \
               f'weekende: {self.weekende}'

    class Meta:
        verbose_name = 'График работы'
        verbose_name_plural = 'График работы'


class Mentor(models.Model):
    LANGUAGE_CHOICES = (
        ('Русский', 'Русский'),
        ('Кыргызский', 'Кыргызский')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False, blank=True)
    image = models.ImageField(verbose_name='Фото', blank=True, upload_to='mentors/', default='mentors/default.jpg')
    name = models.CharField(verbose_name='Имя', max_length=15)
    about = models.TextField(verbose_name='О себе')
    tel = models.URLField(verbose_name='Телеграм')
    course = models.CharField(verbose_name='Направление', max_length=255)
    month = models.CharField(verbose_name='Месяц', max_length=255)
    language = ArrayField(models.CharField(max_length=20, choices=LANGUAGE_CHOICES), verbose_name='Язык')
    skils = ArrayField(models.CharField(max_length=25), verbose_name='Скиллы',)
    worktimes = models.ForeignKey(WorkTimes, on_delete=models.CASCADE, verbose_name='График работы')
    time_create = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, null=True)
    time_update = models.DateTimeField(verbose_name='Дата обновления', auto_now=True, null=True)
    likes = models.ManyToManyField(User, blank=True, related_name='likes', verbose_name='Лайки')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes', verbose_name='Дизлайки')

    @property
    def like(self):
        return self.likes.count()

    @property
    def dislike(self):
        return self.dislikes.count()

    class Meta:
        verbose_name = 'Ментор'
        verbose_name_plural = 'Менторы'

    def __str__(self):
        return f'{self.name}'


class FavoriteMentor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Избранный ментор'
        verbose_name_plural = 'Избранные менторы'


class MentorReview(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='review')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def user_name(self):
        return self.user.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
