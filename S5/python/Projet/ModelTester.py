from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

class ModelTester:
    def __init__(self, X_train, y_train, X_test, y_test):
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test
        self.models = {
            "KNN": KNeighborsClassifier(),
            "Logistic Regression": LogisticRegression(), 
            "Decision Tree": DecisionTreeClassifier(),
            "SVM": SVC()
        }
        self.trained_models = {}

    def entrainer_models(self):
        print("\n=== Entraînement des modèles ===")
        for nom, model in self.models.items():
            model.fit(self.X_train, self.y_train)
            self.trained_models[nom] = model
            print(f"{nom} entraîné avec succès")
        
        return self.trained_models
