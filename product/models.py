from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    cid = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=255, null=False, blank=True)
    category = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.slug = slugify(self, Category)
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    fid = models.AutoField(primary_key=True, null=False, blank=True)
    product = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, db_column='category')


class Comment(models.Model):
    co_id = models.AutoField(primary_key=True, null=False, blank=True)
    comment_user = models.CharField(max_length=255)
    comment = models.CharField(max_length=500)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)


class Feedback(models.Model):
    fe_id = models.AutoField(primary_key=True, null=False, blank=True)
    comment_user = models.CharField(max_length=255)
    fe_comment = models.CharField(max_length=500)
    feedback = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
