import pandas as pd
from sklearn.model_selection import train_test_split

class Preprocessing: 
    def __init__(self, X, y):
        self.X = X  
        self.y = y 
        self.X_train = None 
        self.X_test = None   
        self.y_train = None  
        self.y_test = None  
    
    def traiter_valeurs_manquantes(self): 
        valeurs_manquantes = self.X.isnull().sum().sum() 
        print(f"Total: {valeurs_manquantes}")
        
        if valeurs_manquantes > 0:
            self.X = self.X.dropna()#dropna() method from pandas library removes missing values from DataFrame
            self.y = self.y[self.X.index]#align y with X after dropping rows using the index of X
    
    def separer_donnees(self):
        #train_test_split imported from sklearn.model_selection take in arguments X, y, test_size and random_state
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

        print(f"Train: {len(self.X_train)} (80%)")
        print(f"Test: {len(self.X_test)} (20%)")

        return self.X_train, self.X_test, self.y_train, self.y_test
    