#importing necessary modules
from DataLoader import DataLoader
from Preprocessing import Preprocessing
from Visualization import Visualization
from ModelTester import ModelTester
from Evaluation import Evaluation
from FileManager import FileManager

def main():
    print("\n=== PROJET L3 ISEI ===")

    # 1. Charger les données
    loader = DataLoader("diabetes_binary_health_indicators_BRFSS2015.csv")
    
    # Réduire à 1% des donnée
    loader.data = loader.data.sample(frac=0.01, random_state=42) 
    print(f"Données réduites à 1%: {len(loader.data)} lignes") 
    
    X, y = loader.extraire_variables("Diabetes_Status")

    # 2. Prétraitement
    prep = Preprocessing(X, y)
    prep.traiter_valeurs_manquantes()
    X_train, X_test, y_train, y_test = prep.separer_donnees() 

    # 3. Visualisation
    visu = Visualization(loader.data)
    visu.distribution_age()
    visu.distribution_bmi()
    visu.repartition_diabete()
    visu.relation_age_bmi()

    # 4. Modèles
    tester = ModelTester(X_train, y_train, X_test, y_test)
    models = tester.entrainer_models()

    # 5. Évaluation
    eval = Evaluation(models, X_test, y_test)
    resultats = eval.evaluer()
    classement = eval.classement()
    
    # KNN
    eval.afficher_graphe_knn()

    # 6. Sauvegarde fichiers
    fm = FileManager()
    fm.sauvegarder(resultats)
    fm.lire()

# 7. Fin du programme
if __name__ == "__main__":
    main()
