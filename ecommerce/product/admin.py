from django.contrib import admin

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'creation', 'price')
    search_fields = ('title', 'price')
    ordering = ('-creation',)
    readonly_fields = ('creation',)
    
    def save_model(self, request, obj):
        obj.responsible = request.user
        obj.save()
