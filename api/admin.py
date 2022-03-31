from django.contrib import admin
from .models import *


@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    fields = ('user', 'image', 'is_premium', 'bio')
    list_display = ('id', 'user', 'is_premium', 'image')


@admin.register(Groupa)
class GroupAdmin(admin.ModelAdmin):
    fields = ('name', 'location', 'description')
    list_display = ('id', 'name', 'location', 'description')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ('team1', 'team2', 'time', 'score1', 'score2', 'group')
    list_display = ('id', 'team1', 'team2', 'time', 'score1', 'score2', 'group')


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    fields = ('user', 'group', 'admin')
    list_display = ('id', 'user', 'group', 'admin')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ('user', 'group', 'description')
    list_display = ('id', 'user', 'group', 'description', 'time')


