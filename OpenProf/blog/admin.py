from django.contrib import admin
from random import choice
from .models import Article, Categorie, Comment,Prof,Profession,Annonce,NiveauScolaire

class ProfAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'profession', 'competence_phys','competence_chim','competence_math', )
    list_filter = ('profession', )
    search_fields = ('profession', 'competence_phys','competence_chim','competence_math', )
    prepopulated_fields = {'slug': ('prenom','nom' )}

class AnnonceAdmin(admin.ModelAdmin):
    list_display = ('prenom','niveauScolaire', 'besoin_phys','besoin_chim','besoin_math', )
    list_filter = ('date', )
    search_fields = ('profession', 'besoin_phys','besoin_chim','besoin_math', )
    prepopulated_fields = {'slug': ('prenom','niveauScolaire' )}


    
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'categorie', 'date', 'is_visible', )
    list_filter = ('categorie', )
    search_fields = ('title', 'auteur', )

    prepopulated_fields = {'slug': ('titre', )}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('auteur', 'date','articleRef', 'is_visible', )
    list_filter = ('articleRef', )
    search_fields = ('auteur','contenu', )



admin.site.register(Prof, ProfAdmin)
admin.site.register(Annonce, AnnonceAdmin)
admin.site.register(Profession)
admin.site.register(NiveauScolaire)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Categorie)
admin.site.register(Comment,CommentAdmin)