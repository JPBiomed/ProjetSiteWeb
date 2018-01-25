from django.db import models

class Prof(models.Model):
    prenom = models.CharField(max_length=42)
    nom = models.CharField(max_length=42)
    slug = models.SlugField()
    description = models.TextField(null=True)
    competence_phys = models.BooleanField(verbose_name="Compétent en physique",default=False)
    competence_chim = models.BooleanField(verbose_name="Compétent en chimie",default=False)
    competence_math = models.BooleanField(verbose_name="Compétent en maths",default=False)
    profession = models.ForeignKey('Profession',on_delete=models.DO_NOTHING)

class Profession(models.Model):
    titre = models.CharField(max_length=100)

    def __str__(self):
        return self.titre

class Annonce(models.Model):
    prenom = models.CharField(max_length=42)
    slug = models.SlugField()
    description = models.TextField(null=True)
    date = models.DateTimeField(verbose_name="Date de parution",auto_now_add=True, auto_now=False)
    niveauScolaire = models.ForeignKey('NiveauScolaire',on_delete=models.DO_NOTHING)
    besoin_phys = models.BooleanField(verbose_name="Compétent en physique",default=False)
    besoin_chim = models.BooleanField(verbose_name="Compétent en chimie",default=False)
    besoin_math = models.BooleanField(verbose_name="Compétent en maths",default=False)
    
class NiveauScolaire(models.Model):
    titre = models.CharField(max_length=100)
    annee = models.IntegerField()

    def __str__(self):
        return self.titre

class Article(models.Model):
    titre = models.CharField(max_length=100)
    slug = models.SlugField()
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(verbose_name="Date de parution",auto_now_add=True, auto_now=False)
    is_visible = models.BooleanField(verbose_name="Article publié ?",default=False)
    categorie = models.ForeignKey('Categorie',on_delete=models.DO_NOTHING)
    nbrComment=models.IntegerField(null=True)

    def __str__(self):
        return self.titre

    def getNbrComment(self):
        self.nbrComment= len(Comment.objects.filter(articleRef=self))
    # En cas de besoin, vous êtes autorisé à rajouter des méthodes ou
    # propriétés dans ce modèle.


class Categorie(models.Model):
    titre = models.CharField(max_length=100)

    def __str__(self):
        return self.titre


class Comment(models.Model):
    auteur = models.CharField(max_length=42)
    email=models.EmailField()
    contenu = models.TextField(null=True)
    date = models.DateTimeField(verbose_name="Date de parution", auto_now_add=True, auto_now=False)
    articleRef = models.ForeignKey('Article', on_delete=models.DO_NOTHING,)
    is_visible = models.BooleanField(verbose_name="Visible", default=True)