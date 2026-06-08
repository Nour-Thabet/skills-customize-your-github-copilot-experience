# 📘 Assignment: Jeu Python modulaire

## 🎯 Objectif

Concevoir et développer un petit jeu en Python organisé en modules réutilisables. Les étudiant·e·s apprendront à structurer un projet, écrire du code testable et collaborer via Git (branches, revues). Ce projet s'étend sur plusieurs semaines et se fait en binômes ou petits groupes.

## 📝 Tasks

### 🛠️ Concevoir l'architecture du jeu

#### Description
Définir les modules principaux (moteur de jeu, entités/joueurs, utils) et leur API minimale.

#### Requirements
Completed program should:

- Décrire les modules et les interfaces dans un court document (README ou diagramme simple).
- Fournir un point d'entrée `starter-code.py` qui montre comment les modules interagissent.

### 🛠️ Implémenter le moteur de jeu et les entités

#### Description
Implémenter une boucle de jeu simple, une classe `Player` et au moins un type d'entité (ex. `Enemy`).

#### Requirements
Completed program should:

- Avoir une classe `Game` qui gère les entités et une méthode `step()` qui avance l'état.
- Avoir une classe `Player` avec au moins une méthode `add_score(amount)` et un attribut `score`.
- Fournir une démonstration simple exécutable (`python starter-code.py`).

### 🛠️ Tests et qualité

#### Description
Écrire des tests unitaires `pytest` qui valident le comportement des composants principaux.

#### Requirements
Completed program should:

- Contenir des tests automatisés couvrant l'ajout de joueurs, l'incrément de score et l'avancée de la boucle de jeu.
- Pouvoir exécuter les tests localement via `pytest`.

### 🛠️ Collaboration et livraison

#### Description
Travailler en binôme, utiliser des branches Git, ouvrir une Pull Request et inclure une courte note sur la division du travail.

#### Requirements
Completed program should:

- Avoir un fichier `README.md` (celui-ci) décrivant la structure et les consignes.
- Inclure un fichier `requirements.txt` listant les dépendances (si nécessaire).

## Ressources et critères d'évaluation

- Code propre, modules bien séparés, tests passant.
- Document succinct expliquant l'architecture et les choix.
