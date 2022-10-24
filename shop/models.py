# from mongoengine import Document
# from mongoengine import *
# from django.db import models

# Create your models here.
# class Good(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self) -> str:
#         return self.name
# class History(EmbeddedDocument):
#     name = StringField(max_length=255)
#     quantity = IntField()
#     time = DateField()

# class GoodsAndHistory(Document):
#     goods_name = StringField(max_length=255)
#     history = ListField(EmbeddedDocumentField(History))
    
#     def __str__(self) -> str:
#         return self.name



# class Order(models.Model):
#     purchase_name = models.CharField(max_length=255)
#     quantity = models.IntegerField()
#     create_time = models.DateTimeField(auto_now_add=True)
#     good = models.ForeignKey(Good, on_delete=models.PROTECT)

