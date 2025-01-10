from django.db import models

class TestA1(models.Model):
    chinese = models.CharField(max_length=200)
    english = models.CharField(max_length=200)
    cur_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'testa1'
        ordering = ['-cur_date']  # 按创建时间倒序排列
