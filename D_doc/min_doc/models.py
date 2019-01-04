import uuid
from django.db import models
# from django.contrib.auth.models import User

class Client(models.Model):
    STATUS_CHOICE = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    uuid = models.CharField(unique=True, default=uuid.uuid4, max_length=255, editable=False)
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    email = models.EmailField()
    status = models.CharField('Status',max_length=32, default='Active', choices=STATUS_CHOICE)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField('Date Joined', auto_now_add=True)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        db_table = "Clients"

    def __str__(self):
        return self.username


class Category(models.Model):
    STATUS_CHOICE = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    uuid = models.CharField(unique=True, default=uuid.uuid4, max_length=255, editable=False)
    name = models.CharField(max_length=128)
    status = models.CharField(max_length=32, default=STATUS_CHOICE[0][0], choices=STATUS_CHOICE)
    is_permission = models.BooleanField("Permission", default=True)
    create_time = models.DateTimeField('Create Time', auto_now_add=True)
    modify_time = models.DateTimeField('Modify Time', auto_now_add=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = "categories"


class Book(models.Model):
    STATUS_CHOICE = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    EDITOR_CHOICE = (
    	('edit.md', 'edit.md'),
    	('wangEdit', 'wangEdit'),
    )
    uuid = models.CharField(unique=True, default=uuid.uuid4, max_length=255, editable=False)
    name = models.CharField(max_length=128)
    user = models.ForeignKey(Client, blank=False, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, blank=True, on_delete=models.DO_NOTHING)
    is_open = models.BooleanField('Is Open', default=True)
    is_release = models.BooleanField('Is Release', default=True)
    is_permission = models.BooleanField('Is Permission', default=True)
    status = models.CharField(max_length=32, default=STATUS_CHOICE[0][0], choices=STATUS_CHOICE)
    editor = models.CharField(max_length=32, default=STATUS_CHOICE[1][1], choices=EDITOR_CHOICE)
    description = models.TextField('Description', blank=True, null=True)
    create_time = models.DateTimeField('Create Time', auto_now_add=True)
    modify_time = models.DateTimeField('Modify Time', auto_now_add=True)
    version = models.CharField('Version', max_length=32)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        db_table = "books"

    def __str__(self):
        return self.name


class Document(models.Model):
    STATUS_CHOICE = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    EDITOR_CHOICE = (
    	('edit.md', 'edit.md'),
    	('wangEdit', 'wangEdit'),
    )
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    user = models.ForeignKey(Client, blank=False, on_delete=models.DO_NOTHING)
    book = models.ForeignKey(Book, blank=False, on_delete=models.DO_NOTHING)
    str_id = models.IntegerField()
    sort_id = models.IntegerField()
    content = models.TextField('Article content', blank=True, null=True)
    markdown = models.TextField('Content of Markdown', blank=True, null=True)
    html = models.TextField('Content of Html', blank=True, null=True)
    version = models.CharField('Version', max_length=128)
    is_open = models.BooleanField('Is Open', default=True)
    is_release = models.BooleanField('Is Release', default=True)
    create_time = models.DateTimeField('Create Time', auto_now_add=True)
    modify_time = models.DateTimeField('Modify Time', auto_now_add=True)

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"
        db_table = "documents"

    def __str__(self):
        return self.name




