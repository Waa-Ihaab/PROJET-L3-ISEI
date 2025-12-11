import pandas as pd


class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.data = None 
        self.X = None
        self.y = None 
        self.charger_csv()
    
    def charger_csv(self):
        try:
            self.data = pd.read_csv(self.filename)
            print(f"Fichier '{self.filename}' chargé avec succès")
            self.afficher_dimensions()
        except FileNotFoundError:
            print("Erreur fichier introuvable.")
    
    def afficher_dimensions(self):
        if self.data is not None: 
            lignes, colonnes = self.data.shape 
            print(f"Nombre de lignes: {lignes}")
            print(f"Nombre de colonnes: {colonnes}")
            return lignes, colonnes
        return None, None
    
    def extraire_variables(self, colonne_cible):
        if self.data is not None:
            if colonne_cible not in self.data.columns:
                print(f"Erreur: La colonne '{colonne_cible}' n'existe pas")
                print(f"Colonnes disponibles: {list(self.data.columns)}")
                return None, None
            
            self.y = self.data[colonne_cible]
            self.X = self.data.drop(columns=[colonne_cible])
            
            print(f"✓ Variables extraites:")
            print(f"  - X: {self.X.shape[1]} colonnes")
            print(f"  - y: {colonne_cible}")
            
            return self.X, self.y
        return None, None
