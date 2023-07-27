from django.contrib import admin
from .models import score1,score2,score3,score4,payment3,payment4



@admin.register(score1)
class score1Admin(admin.ModelAdmin):
    list_display = ("id", "user_name", "score","date_created")
    list_filter = ("user_name", "score","date_created")
    search_fields=['user_name','score']
    def has_delete_permission(self, request):
        # Disable delete
        return False
    def has_add_permission(self,request):
        return False

@admin.register(score2)
class score2Admin(admin.ModelAdmin):
    list_display = ("id", "user_name", "score","date_created")
    list_filter = ("user_name", "score","date_created")
    search_fields=['user_name','score']
    def has_delete_permission(self, request):
        # Disable delete
        return False
    def has_add_permission(self,request):
        return False

@admin.register(score3)
class score3Admin(admin.ModelAdmin):
    list_display = ("id", "user_name", "score","date_created")
    list_filter = ("user_name", "score","date_created")
    search_fields=['user_name','score']
    def has_delete_permission(self, request):
        # Disable delete
        return False
    def has_add_permission(self,request):
        return False


@admin.register(score4)
class score4Admin(admin.ModelAdmin):
    list_display = ("id", "user_name", "score","date_created")
    list_filter = ("user_name", "score","date_created")
    search_fields=['user_name','score']
    def has_delete_permission(self, request):
        # Disable delete
        return False
    def has_add_permission(self,request):
        return False

@admin.register(payment3)
class payment3Admin(admin.ModelAdmin):
    list_display=("id","user_name","pay","amount","date_created")
    list_filter=("user_name","date_created")
    search_fields=['user_name']
    def has_delete_permission(self,request):
        return False
    def has_add_permission(self,request):
        return False
@admin.register(payment4)
class payment4Admin(admin.ModelAdmin):
    list_display=("id","user_name","pay","amount","date_created")
    list_filter=("user_name","date_created")
    search_fields=['user_name']
    def has_delete_permission(self,request):
        return False
    def has_add_permission(self,request):
        return False