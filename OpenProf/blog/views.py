from django.shortcuts import render, get_object_or_404
from .forms import CommentForm,ProfForm
from .models import Article,Comment

def accueil(request):
    """
    Affiche les 5 derniers articles du blog. Nous n'avons pas encore
    vu comment faire de la pagination, donc on ne donne pas la
    possibilité de lire les articles plus vieux via l'accueil pour
    le moment.
    """
    articles = Article.objects.filter(is_visible=True).order_by('-date')[:4]
    for article in articles:
        article.getNbrComment()
    return render(request, 'blog/accueil.html', {'articles': articles})
    
    
def accueil(request):
    """
    Affiche les 5 derniers articles du blog. Nous n'avons pas encore
    vu comment faire de la pagination, donc on ne donne pas la
    possibilité de lire les articles plus vieux via l'accueil pour
    le moment.
    """
    articles = Article.objects.filter(is_visible=True).order_by('-date')[:4]
    for article in articles:
        article.getNbrComment()
    return render(request, 'blog/accueil.html', {'articles': articles})

def prof_add(request):
    if request.method=="POST":
        form = ProfForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blog')
    form = ProfForm()
    return render(request, 'blog/prof_add.html', locals())

def lire_article(request, slug):
    """
    Affiche un article complet, sélectionné en fonction du slug
    fourni en paramètre
    """
    article = get_object_or_404(Article, slug=slug)
    comments=Comment.objects.filter(articleRef=article)
    donnees_comm={'articleRef':article}
    form1 = CommentForm(request.POST or donnees_comm)
    form1.articleRef = article
    if form1.is_valid():
        form1.save(commit=False)
        form1.articleRef = article
        form1.save()
        envoi = True

    return render(request, 'blog/lire_article.html', {'article': article,'comments': comments,'form1':form1})