from django.contrib import admin
from .models import Member, Books, Author

# Register your models here.
admin.site.register(Member)
admin.site.register(Books)
admin.site.register(Author)