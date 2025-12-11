from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import os

class Evaluation:
    def __init__(self, models, X_test, y_test):
        self.models = models
        self.X_test = X_test
        self.y_test = y_test
        self.resultats = {}

    def evaluer(self):
        print("\n=== Évaluation des modèles ===")
        for nom, model in self.models.items():
            predictions = model.predict(self.X_test)

            acc = accuracy_score(self.y_test, predictions)
            cm = confusion_matrix(self.y_test, predictions)
            report = classification_report(self.y_test, predictions)

            self.resultats[nom] = {
                "accuracy": acc,
                "confusion_matrix": cm,
                "classification_report": report
            }

            print(f"\n----- {nom} -----")
            print(f"Accuracy = {acc:.4f}")
            print("Matrice de confusion :\n", cm)
            print("Rapport :\n", report)

        return self.resultats
    
    def classement(self):
        print("\n=== Classement des modèles ===")
        sorted_models = sorted(
            self.resultats.items(),
            key=lambda x: x[1]['accuracy'],
            reverse=True
        )
        
        for i, (nom, metrics) in enumerate(sorted_models, start=1):
            print(f"{i}. {nom} → Accuracy: {metrics['accuracy']:.4f}")
        
        return sorted_models
    
    def afficher_graphe_knn(self):
        if 'KNN' not in self.resultats:
            print("Erreur: Le modèle KNN n'a pas été évalué.")
            return
        
        print("\n=== Génération du graphique pour KNN ===")
        
        # Créer le dossier figures s'il n'existe pas
        if not os.path.exists('figures'):
            os.makedirs('figures')
        
        # Récupérer la matrice de confusion de KNN
        cm = self.resultats['KNN']['confusion_matrix']
        acc = self.resultats['KNN']['accuracy']
        
        # Créer le graphique
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                    xticklabels=['Non-diabétique', 'Diabétique'],
                    yticklabels=['Non-diabétique', 'Diabétique'])
        plt.title(f'Matrice de Confusion - KNN\nAccuracy: {acc:.4f}')
        plt.ylabel('Vraie classe')
        plt.xlabel('Classe prédite')
        plt.tight_layout()
        
        # Sauvegarder
        filepath = 'figures/knn_confusion_matrix.png'
        plt.savefig(filepath)
        print(f"✓ Graphique sauvegardé: {filepath}")
        plt.show()

