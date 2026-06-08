# Building REST APIs with FastAPI

## Objectifs d'apprentissage

- Comprendre les concepts de base de FastAPI
- Créer des endpoints RESTful (GET, POST, PUT, DELETE)
- Valider les requêtes et réponses avec Pydantic
- Lancer et tester l'application localement avec Uvicorn

## Pré-requis

- Python 3.8+
- Connaissances de base en Python et HTTP

## Description

Dans cet exercice, vous allez construire une API REST simple pour gérer une collection d'items. Vous implémenterez les opérations CRUD suivantes :

- Lister tous les items
- Récupérer un item par son identifiant
- Créer un nouvel item
- Mettre à jour un item existant
- Supprimer un item

## Tâches

1. Exécuter l'application fournie dans `starter-code.py`.
2. Compléter les endpoints manquants si nécessaire.
3. Ajouter la validation Pydantic pour les schémas de requête et de réponse.
4. Tester l'API avec `curl`, `httpie` ou l'interface interactive fournie par FastAPI (`/docs`).

## Exécution

Installer les dépendances :

```
pip install -r requirements.txt
```

Lancer le serveur :

```
uvicorn starter-code:app --reload
```

Accéder à la documentation interactive : http://127.0.0.1:8000/docs

## Critères de réussite

- Endpoints CRUD fonctionnels
- Validation des données en entrée
- Documentation OpenAPI accessible via `/docs`

## Soumission

Fournir un lien vers votre dépôt ou zipper le dossier de l'exercice et le soumettre selon les consignes du cours.
