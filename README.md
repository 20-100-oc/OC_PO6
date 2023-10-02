# Projet: Améliorez le produit IA de votre start-up

## Contexte
Avis Restau, une startup qui met en relation des clients et des restaurants, cherche à réaliser une étude de faisabilité sur une nouvelle fonctionnalité.
L'entreprise souhaite que les utilisateurs de leur plateforme puissent poster leurs avis ou commentaires sur leurs expériences, ainsi que les photos prises dans le restaurant. 
Cela donnerait à Avis Restau l'occasion de détecter les sujets d'insatisfaction des clients à travers les commentaires. 
Elle voit aussi la possibilité de labélliser automatiquement les photos postées dans différentes catégories (nourriture, menu, intérieur du restaurant, extérieur du restaurant).
Le but est de réaliser une étude préliminaire pour estimer s'il est pertinent d'investir plus avant dans la réalisation de cette idée.

## Objectifs
- Pour les commentaires :
  - prétraitement des commentaires négatifs
  - réduction de dimension et modélisation (LDA)
  - visualisation des mots-clés et interprétation des sujets d'insatisfaction 
- Pour les photos :
  - modélisation : algorithme d'extraction de features et réseau de neurones avec transfer learning
  - algorithme de réduction de dimension pour simplifier les résultats en sortie de modèle
  - clustering des catégories et création de visualisations pour estimer la qualité d'une potentielle classification
- Déterminer la faisabilité de la nouvelle fonctionnalité (pour les commentaires et les photos)
- Présenter les résultats à travers une page web
- Mettre en place un système de récolte de nouvelles données pour l'entraînement des potentiels futurs modèles (dataset Yelp)

## Livrables
- Notebook de traitement des avis clients
- Notebook de traitement des photos
- Notebook de récolte de données avec l'API Yelp
- Page web de présentation synthétique des résultats
- Présentation PowerPoint

## Outils
- Python
- Git / Github
- Jupyter notebook / Python IDE
- PowerPoint
- Streamlit
  
### Python : libraires additionnelles
- numpy
- matplotlib
- pandas
- seaborn
- sklearn
- tensorflow
- Pillow
- pyLDAvis
- gensim
- wordcloud
- contractions
- nltk
- streamlit
- yelpapi