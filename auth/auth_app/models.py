from django.db import models


class User(models.Model):
    phone = models.CharField(max_length=20)
    invite_code = models.CharField(max_length=6, blank=True, null=False)
    invited_users = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(default=False)


class UseInviteCode(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    who_used_code = models.CharField(null=True, max_length=(13))
