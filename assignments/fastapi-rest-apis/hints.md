# 💡 Indices pour l'exercice FastAPI

- Utilisez Pydantic pour définir des modèles de requête et de réponse.
- Pour retourner `204 No Content`, ne renvoyez pas de corps (utiliser `return` sans valeur).
- Exemple CURL pour créer un item :

```
curl -s -X POST http://127.0.0.1:8000/items \
  -H "Content-Type: application/json" \
  -d '{"id": 2, "name": "Nouvel item", "price": 12.5}'
```

- Pour assigner un `id` côté serveur, acceptez un modèle sans `id` pour `POST` puis générez un nouvel `id`.
- Tester l'API via l'interface interactive : `http://127.0.0.1:8000/docs`.
