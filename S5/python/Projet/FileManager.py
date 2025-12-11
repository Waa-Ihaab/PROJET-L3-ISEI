class FileManager:
    def __init__(self, filename="resultats.txt"):
        self.filename = filename

    def sauvegarder(self, data):
        with open(self.filename, "w", encoding="utf-8") as f: 
            for nom, info in data.items():
                f.write(f"=== {nom} ===\n")
                f.write(f"Accuracy: {info['accuracy']}\n")
                f.write("Matrice de confusion:\n")
                f.write(str(info['confusion_matrix']) + "\n")
                f.write("Rapport de classification:\n")
                f.write(info['classification_report'] + "\n\n")

        print(f"\nRésultats sauvegardés dans {self.filename}")

    def lire(self):
        print(f"\n=== Contenu de {self.filename} ===")
        with open(self.filename, "r", encoding="utf-8") as f:
            print(f.read())
