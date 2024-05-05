from django.contrib import admin
from .models import ChatConversation , newsletter
# Register your models here.

admin.site.register(ChatConversation)

class ChatConversationAdmin(admin.ModelAdmin):
    list_display = ('session_id', 'bot_message', 'user_message', 'timestamp')
    list_filter = ['timestamp']
    search_fields = ['session_id', 'bot_message', 'user_message']

admin.site.register(newsletter)
class newsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'timestamp')