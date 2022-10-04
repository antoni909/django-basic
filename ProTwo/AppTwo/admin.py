from django.contrib import admin
from .models import Page, Topic, WebPage, User

# Register your models here.
admin.site.register(User)
admin.site.register(Page)
admin.site.register(Topic)
admin.site.register(WebPage)
# admin.site.register(AccessRecord)