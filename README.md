# 🏥 Projet L3 ISEI - Analyse et Prédiction du Diabète

## 📋 Description du Projet

Ce projet de Machine Learning vise à analyser et prédire le statut diabétique des patients en utilisant des données de santé provenant du BRFSS 2015 (Behavioral Risk Factor Surveillance System). Le projet implémente et compare plusieurs algorithmes de classification pour identifier les meilleurs modèles de prédiction.

## 🎯 Objectifs

- Charger et prétraiter des données médicales massives
- Visualiser les distributions et relations entre variables de santé
- Entraîner et comparer 4 algorithmes de Machine Learning
- Évaluer les performances avec des métriques détaillées
- Sauvegarder les résultats pour analyse

## 🛠️ Technologies Utilisées

- **Python 3.x**
- **Pandas** - Manipulation de données
- **Scikit-learn** - Algorithmes de Machine Learning
- **Matplotlib/Seaborn** - Visualisations
- **NumPy** - Calculs numériques

## 📊 Algorithmes Implémentés

1. **K-Nearest Neighbors (KNN)** - Classification par voisinage
2. **Régression Logistique** - Modèle linéaire probabiliste
3. **Arbre de Décision** - Modèle basé sur des règles
4. **SVM (Support Vector Machine)** - Classification par hyperplan

## 🗂️ Structure du Projet

```
Projet/
│
├── main.py                    # Point d'entrée principal
├── DataLoader.py              # Chargement des données CSV
├── Preprocessing.py           # Nettoyage et préparation des données
├── Visualization.py           # Génération des graphiques
├── ModelTester.py             # Entraînement des modèles
├── Evaluation.py              # Évaluation et métriques
├── FileManager.py             # Sauvegarde des résultats
├── diabetes_binary_health_indicators_BRFSS2015.csv
├── resultats.txt              # Résultats des évaluations
└── figures/                   # Visualisations générées
```

## 🚀 Installation et Utilisation

### Prérequis
```bash
pip install pandas scikit-learn matplotlib seaborn numpy
```

### Exécution
```bash
python main.py
```

## 📊 Dataset

**Source:** BRFSS 2015 - Behavioral Risk Factor Surveillance System

Le dataset contient des indicateurs de santé binaires incluant:
- Statut diabétique
- Âge
- IMC (Indice de Masse Corporelle)
- Pression artérielle
- Cholestérol
- Activité physique
- Consommation de fruits et légumes
- Et bien d'autres variables de santé

**Note:** Le projet utilise 1% du dataset complet pour optimiser les temps de calcul.

## 📝 Fonctionnalités

### 1. Chargement des Données
- Import du CSV
- Réduction à 1% pour performance
- Extraction des variables cibles

### 2. Prétraitement
- Traitement des valeurs manquantes
- Séparation train/test
- Normalisation des données

### 3. Visualisation
- Distribution des variables clés
- Graphiques de corrélation
- Matrices de confusion

### 4. Modélisation
- Entraînement de 4 algorithmes
- Prédictions sur données de test
- Comparaison des performances

### 5. Évaluation
- Précision (Accuracy)
- Rapport de classification
- Matrice de confusion
- Classement des modèles

### 6. Sauvegarde
- Export des résultats en fichier texte
- Graphiques PNG dans `/figures`

## 📊 Résultats

Les résultats détaillés de chaque modèle (précision, recall, f1-score) sont automatiquement sauvegardés dans `resultats.txt` après chaque exécution.



*Développé dans le cadre du cursus L3 ISEI - Python*
