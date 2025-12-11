import matplotlib.pyplot as plt
import os

class Visualization:
    def __init__(self, data):
        self.data = data
        self.figures_dir = 'figures'
        if not os.path.exists(self.figures_dir):
            os.makedirs(self.figures_dir)
    
    def distribution_age(self):
        plt.figure(figsize=(8, 5))
        plt.hist(self.data['Age'], bins=20, color='skyblue') 
        plt.xlabel('Âge')
        plt.ylabel('Fréquence')
        plt.title('Distribution de l\'âge')
        plt.show()
        plt.savefig(os.path.join(self.figures_dir, 'distribution_age.png'))
        plt.close()
    
    def distribution_bmi(self):
        plt.figure(figsize=(8, 5))
        plt.hist(self.data['BMI'], bins=20, color='lightcoral')
        plt.xlabel('IMC (BMI)')
        plt.ylabel('Fréquence')
        plt.title('Distribution de l\'IMC')
        plt.show()
        plt.savefig(os.path.join(self.figures_dir, 'distribution_bmi.png'))
        plt.close()
    
    def repartition_diabete(self):
        plt.figure(figsize=(6, 6))
        counts = self.data['Diabetes_Status'].value_counts()
        labels = counts.index.tolist()
        plt.pie(counts, labels=labels, autopct='%1.1f%%', colors=['lightgreen', 'salmon', 'orange'])
        plt.title('Répartition diabétique / non diabétique')
        plt.show()
        plt.savefig(os.path.join(self.figures_dir, 'repartition_diabete.png'))
        plt.close()
    
    def relation_age_bmi(self):
        plt.figure(figsize=(8, 5))
        plt.scatter(self.data['Age'], self.data['BMI'], alpha=0.3)
        plt.xlabel('Âge')
        plt.ylabel('IMC (BMI)')
        plt.title('Relation entre âge et IMC')
        plt.show()
        plt.savefig(os.path.join(self.figures_dir, 'relation_age_bmi.png'))
        plt.close()
