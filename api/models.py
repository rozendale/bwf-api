from django.db import models
from django.contrib.auth.models import User


def upload_path_handler(instance, filename):
    return f"avatars/{instance.user.id}/{filename}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_path_handler, blank=True)
    is_premium = models.BooleanField(default=False)
    bio = models.CharField(default="", blank=True, max_length=256)


class Groupa(models.Model):
    name = models.CharField(max_length=32, null=False, unique=False)
    location = models.CharField(max_length=32, null=False, unique=False)
    description = models.CharField(max_length=256, null=False, unique=False)

    class Meta:
        unique_together = ('name', 'location',)


class Event(models.Model):
    team1 = models.CharField(max_length=32, blank=False)
    team2 = models.CharField(max_length=32, blank=False)
    time = models.DateTimeField(null=False, blank=False)
    score1 = models.IntegerField(null=True, blank=True)
    score2 = models.IntegerField(null=True, blank=True)
    group = models.ForeignKey(to=Groupa, related_name='events', on_delete=models.CASCADE)


class Member(models.Model):
    group = models.ForeignKey(to=Groupa, related_name='members', on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, related_name='members_of', on_delete=models.CASCADE)
    admin = models.BooleanField(default=False)

    class Meta:
        unique_together = (('user', 'group'),)
        index_together = (('user', 'group'),)


class Comment(models.Model):
    group = models.ForeignKey(to=Groupa, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, related_name='user_comments', on_delete=models.CASCADE)
    description = models.CharField(max_length=256, null=False, unique=False)
    time = models.DateTimeField(auto_now_add=True)

# hours:
# 20220212 20:20 - 21:30 = Section1
# at admin.py with @admin.register(admin.ModelAdmin) I learned to override the default admin view. I also worked with Postman again
# 20220213 07:20 - 09:09 = Video 6-12
# 20220221 09:00 - 10:30 = At video 21 there is a nice thing I learned about related_name in models.py and add this as field in serializers
# 20210221 17:55 = 19:00 = I must learn "MUI5 (Material UI) Crash Course"

