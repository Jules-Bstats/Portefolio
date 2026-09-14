from flask import Flask, render_template, abort

app = Flask(__name__)

PROJECTS = {
    "nuitees": {
        "title": "Prévision de la fréquentation touristique en France",
        "date": "juin 2026",
        "summary": """ Cette étude a pour objectif de déterminer le meilleur modèle de prévision les plus performants pour anticiper la fréquentation touristique en France à court terme, mesurée par le nombre de  nuitées en hôtellerie sur la période 2011-2025. Elle répond à deux questions : Quel modèle \n 
permet de prévoir efficacement la fréquentation touristique en France à court terme ? Dans 
quelle mesure l’intégration de variables conjoncturelles, compétitives et comportementales 
permet-elle d’améliorer la qualité de ces prévisions ? Sept modèles ont été estimés, répartis en 
et des modèles sur la tendance appliqués à la série corrigée des variations saisonnières 
(SARIMA, ARIMAX, RLM). Après traitement des valeurs manquantes par lissage de Kalman 
et désaisonnalisation par la méthode X13-ARIMA-SEATS, les prévisions de chaque modèle 
sont évaluées sur l’année 2025 grâce à des indicateurs de qualité de prévision (RMSE, MAE, 
MASE, MAPE) et au test statistique (Diebold-Mariano). Les résultats montrent que les modèles 
de prévision saisonniers SARIMA et SARIMAX surpassent le modèle naïf saisonnier. 
Cependant, aucun modèle sur la tendance ne parvient à faire mieux que les prévisions du modèle 
naïf simple. L’intégration de variables exogènes (Covid, Prix relatif Lags 2 et Google Trends) 
améliore les indicateurs de qualité sans que cette amélioration soit statistiquement significative.""",
        
        "image": "img/projet1.jpg",
        "skills": ["r", "binome"],
        "comment": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Autoévaluation : projet abouti, bonne maîtrise des modèles SARIMA, marge d'amélioration sur l'automatisation du pipeline.",
        "data_origin": "INSEE",
        "data_source": "Fréquentation touristique départementale",
        "data_link": "https://www.insee.fr/fr/statistiques"
    },
    "dashboard": {
        "title": "Dashboard Power BI",
        "date": "Mars 2025",
        "summary": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "image": "img/projet2.jpg",
        "skills": ["powerbi", "solo"],
        "comment": "Lorem ipsum dolor sit amet. Autoévaluation : bonne prise en main de Power BI, à approfondir sur les mesures DAX complexes.",
        "data_origin": "Kaggle",
        "data_source": "Retail Sales Dataset",
        "data_link": "https://www.kaggle.com"
    },
    "Nettoyage": {
            "title": "Nettoyage de données ",
            "date": "Septembre 2025",
            "summary": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
            "image": "img/projet1.jpg",
            "skills": ["r", "binome"],
            "comment": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Autoévaluation : projet abouti, bonne maîtrise des modèles SARIMA, marge d'amélioration sur l'automatisation du pipeline.",
            "data_origin": "INSEE",
            "data_source": "Data",
            "data_link": "https://www.insee.fr/fr/statistiques"
        },
        "brocolis": {
                "title": "Prévision du prix du brocoli aux USA",
                "date": "Septembre 2025",
                "summary": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                "image": "img/projet5.jpg",
                "skills": ["r", "binome"],
                "comment": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Autoévaluation : projet abouti, bonne maîtrise des modèles SARIMA, marge d'amélioration sur l'automatisation du pipeline.",
                "data_origin": "FED",
                "data_source": "Brocolis price",
                "data_link": "https://www.insee.fr/fr/statistiques"
            },
            "Analyse2": {
                    "title": "Analyse",
                    "date": "Septembre 2026",
                    "summary": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                    "image": "img/projet4.jpg",
                    "skills": ["r", "binome"],
                    "comment": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Autoévaluation : projet abouti, bonne maîtrise des modèles SARIMA, marge d'amélioration sur l'automatisation du pipeline.",
                    "data_origin": "INSEE",
                    "data_source": "Kaggle",
                    "data_link": "https://www.insee.fr/fr/statistiques"
                }
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projets")
def projets():
    return render_template("projets.html")

@app.route("/projets/<slug>")
def projet_detail(slug):
    project = PROJECTS.get(slug)
    if project is None:
        abort(404)
    return render_template("projet_detail.html", project=project, slug=slug)

@app.route('/stage')
def stage():
    return render_template('stage.html')

@app.route("/a-propos")
def a_propos():
    return render_template("a_propos.html")

if __name__ == "__main__":
    app.run(debug=True)