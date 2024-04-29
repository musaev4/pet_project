from django.contrib import admin
from .models import NFT, Collection, Transaction, Tag, Review

@admin.register(NFT)
class NFTAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'created_at']
    search_fields = ['title', 'owner__username']
    list_filter = ['created_at']

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner']
    search_fields = ['title', 'owner__username']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'nft', 'amount', 'created_at']
    search_fields = ['sender__username', 'receiver__username', 'nft__title']
    list_filter = ['created_at']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'nft', 'rating', 'created_at']
    search_fields = ['user__username', 'nft__title']
    list_filter = ['created_at']

