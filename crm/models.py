from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ContactRecord(models.Model):
    contact_date = models.DateTimeField(auto_now_add=True)
    acquisition_method = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    communication_result = models.TextField()
    deal_closed = models.BooleanField(default=False)
    salesperson = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.contact_info} - {'Closed' if self.deal_closed else 'Open'}"

class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name="客户姓名")
    contact = models.CharField(max_length=100, verbose_name="联系方式", blank=False, unique=True)
    acquisition_method = models.CharField(max_length=100, verbose_name="获取方式", blank=True)
    description = models.TextField(verbose_name="案件描述", blank=True)
    entry_time = models.DateTimeField(default=timezone.now, verbose_name="录入时间")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="归属")
    is_closed = models.BooleanField(default=False, verbose_name="是否成单")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "客户"
        verbose_name_plural = "客户"
