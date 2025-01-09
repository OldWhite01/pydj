from django.db import models

class TUser(models.Model):
    user_name = models.CharField(max_length=50, unique=True, db_column='user_name')
    user_pass = models.CharField(max_length=100, db_column='user_pass')
    user_email = models.EmailField(unique=True, db_column='user_email')
    create_time = models.DateTimeField(auto_now_add=True, db_column='create_time')
    modify_time = models.DateTimeField(null=True, blank=True, db_column='modify_time')

    class Meta:
        db_table = 't_user1'
