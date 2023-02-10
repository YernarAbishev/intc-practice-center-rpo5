from django.db import models
from datetime import datetime

class Job(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    company = models.CharField("Компания", max_length=255)
    logo = models.CharField("Логотип компании (Ссылка на изображение)", max_length=500)
    postDate = models.DateTimeField("Дата и время публикации", default=datetime.now)
    isActive = models.BooleanField("Активная/В архиве", default=True)
    description = models.TextField("Описание вакансии")
    linkJob = models.CharField("Ссылка на вакансию", max_length=500)

    def __str__(self):
        return f"{self.title} - {self.company} - {self.postDate}"

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"


class Practice(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    company = models.CharField("Компания", max_length=255)
    logo = models.CharField("Логотип компании (Ссылка на изображение)", max_length=500)
    postDate = models.DateTimeField("Дата и время публикации", default=datetime.now)
    isActive = models.BooleanField("Активная/В архиве", default=True)
    description = models.TextField("Описание вакансии")
    linkCompany = models.CharField("Ссылка на сайт компании", max_length=500)

    def __str__(self):
        return f"{self.title} - {self.company} - {self.postDate}"

    class Meta:
        verbose_name = "Производственная практика"
        verbose_name_plural = "Производственные практики"