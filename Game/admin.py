from django.contrib import admin
# Register your models here.
from .models import Game

class CustomGameAdmin(admin.ModelAdmin):
    model = Game
    list_display = ['Game', 'player', 'Consel', 'Discription']
    fieldsets= (
        ('Owner',{
            'fields':('Game','player', 
            )}
        ),
        ('Game info',{
            'fields':('Consel','Discription',
            )}
        )
    )

    
admin.site.register(Game, CustomGameAdmin)