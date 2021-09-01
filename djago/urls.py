from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('compte/nouveau', views.inscription, name='inscription'),
    path('compte/connexion', views.connexion, name='connexion'),
    path('search/<int:id_projet>', views.chercher_projet, name='searchProjet'),
    path('search/<int:budget>/<str:statut>', views.lister_projets, name='listeProjet'),
    path('search/<int:budget>/', views.lister_projets, name='listeProjet'),
    path("newProjet", views.creerProjet, name="nouveauProjet")
]