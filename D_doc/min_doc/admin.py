from django.contrib import admin
from .models import Client, Category, Book, Document

admin.site.register(Client)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Document)
