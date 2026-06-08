# 🛠️ Assignment: Construire une API REST avec FastAPI

## 🎯 Objectifs d'apprentissage

- Comprendre la structure d'une API FastAPI
- Implémenter des endpoints RESTful (GET, POST, PUT, DELETE)
- Valider les entrées et sorties avec Pydantic
- Exposer et tester la documentation OpenAPI automatique

## 🧰 Pré-requis

- Python 3.8+
- `pip` installé
- Connaissances de base en Python et en HTTP

## Description

Dans cet exercice vous construirez une API pour gérer une collection d'items (CRUD). L'API doit permettre de lister, récupérer, créer, mettre à jour et supprimer des items.

## Tâches

1. Lire et exécuter le code fourni dans `starter-code.py`.
2. Implémenter (ou améliorer) les endpoints suivants :
   - `GET /items` — lister tous les items
   - `GET /items/{item_id}` — récupérer un item par id
   - `POST /items` — créer un nouvel item
   - `PUT /items/{item_id}` — mettre à jour un item
   - `DELETE /items/{item_id}` — supprimer un item
3. Utiliser Pydantic pour définir des schémas clairs pour les requêtes et réponses.
4. Gérer les erreurs avec des codes HTTP appropriés (`404`, `400`, etc.).
5. Ajouter des tests manuels avec `curl` ou `httpie` et vérifier `/docs`.

## Exigences détaillées

- Le champ `id` doit être unique pour chaque item.
- Les champs `name` (str) et `price` (float) sont obligatoires.
- `description` est optionnel.
- `POST /items` doit renvoyer `201 Created` et l'objet créé.
- `DELETE /items/{item_id}` doit renvoyer `204 No Content` en cas de succès.

## Critères de réussite

- Tous les endpoints fonctionnent comme spécifié.
- Les données sont validées par Pydantic.
- La documentation OpenAPI est accessible via `/docs`.
- Le code est lisible et bien structuré.

## Comment exécuter

1. Installer les dépendances :

```
pip install -r requirements.txt
```

2. Lancer le serveur :

```
uvicorn starter-code:app --reload
```

3. Ouvrir la documentation interactive : http://127.0.0.1:8000/docs

## Soumission

Fournir :

- Un lien vers votre dépôt contenant le dossier `fastapi-rest-apis`.
- Une brève description des choix réalisés (format POST auto-assignation d'ID, validations, etc.).

## Extensions (optionnel)

- Implémenter la pagination pour `GET /items`.
- Ajouter recherche par nom (`/items?name=...`).
- Persister les données dans une base légère (SQLite).
