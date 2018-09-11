from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=20)
    category_en = models.CharField(max_length=20)
    category_image = models.CharField(max_length=300)

    def __str__(self):
        return self.category


class Post(models.Model):
    page_title = models.CharField(max_length=60)
    page_desc = models.CharField(max_length=160)
    page_keywords = models.CharField(max_length=100)

    title = models.CharField(max_length=300)
    desc = models.TextField(blank=True)
    img = models.CharField(max_length=300, blank=True)
    img_alt = models.CharField(max_length=100, blank=True)
    vid = models.CharField(max_length=300, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Section(models.Model):
    title = models.CharField(max_length=300, blank=True)
    desc = models.TextField(blank=True)
    img = models.CharField(max_length=300, blank=True)
    img_alt = models.CharField(max_length=100, blank=True)
    vid = models.CharField(max_length=300, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
