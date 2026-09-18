from flask import Flask, render_template, abort

app = Flask(__name__)

PROJECTS = {

# accident de la route -----------------------------------------------------
    "accident routier": {
                "title": "Analyse économétrique du taux d'accidents de la route en France",
                "date": "Décembre 2025",
                "summary": """
                    blabla 
                    """,
                    "summary_bottom":"""blabla """,
                "image": "img/projet6.jpg",
                "skills": ["r", "binome"],
                "comment": """L'auto-critique met toutefois en lumière la complexité inhérente 
                    l'imputation de telles bases issues d'enquêtes, particulièrement lorsque la majorité des variables sont qualitatives et possèdent de multiples modalirés.""",
                "data_origin": "INSEE",
                "data_link": "https://www.insee.fr/fr/statistiques",
                "project_file": "docs/nuitees_projet.pdf",
                "synthesis_file": "docs/nuitees_synthese.pdf"
            },

# prévision des nuitées  -----------------------------------------------------------------------------------------  
    
    "nuitees": {
        "title": "Prévision de la fréquentation touristique en France",
        "date": "Juin 2026",
        "summary": 
                        """ Cette étude a pour objectif de déterminer le meilleur modèle de prévision les plus performants
                pour anticiper la fréquentation touristique en France à court terme, mesurée par le nombre de 
                nuitées en hôtellerie sur la période 2011-2025. Elle répond à deux questions : Quel modèle 
                permet de prévoir efficacement la fréquentation touristique en France à court terme ? Dans 
                quelle mesure l’intégration de variables conjoncturelles, compétitives et comportementales 
                permet-elle d’améliorer la qualité de ces prévisions ? Sept modèles ont été estimés, répartis en 
                deux groupes : des modèles saisonniers (SARIMA, ETS, ADAM ETS ARIMA, SARIMAX) 
                et des modèles sur la tendance appliqués à la série corrigée des variations saisonnières 
                (SARIMA, ARIMAX, RLM). Après traitement des valeurs manquantes par lissage de Kalman 
                et désaisonnalisation par la méthode X13-ARIMA-SEATS, les prévisions de chaque modèle 
                sont évaluées sur l’année 2025 grâce à des indicateurs de qualité de prévision (RMSE, MAE, 
                MASE, MAPE) et au test statistique (Diebold-Mariano). 
                """,
        "summary_bottom": 
                """Les résultats montrent que les modèles 
                de prévision saisonniers SARIMA et SARIMAX surpassent le modèle naïf saisonnier. 
                Cependant, aucun modèle sur la tendance ne parvient à faire mieux que les prévisions du modèle 
                naïf simple. L’intégration de variables exogènes (Covid, Prix relatif Lags 2 et Google Trends) 
                améliore les indicateurs de qualité sans que cette amélioration soit statistiquement significative.""", 
        "image": "img/projet1.jpg",
        "skills": ["R", "R-Shiny", "Série temporelle","Prévision"],
        "comment": """
                Ce travail de recherche m'a permis de développer mes compétences techniques (R, R-Shiny) et analytiques 
                (modélisation, prévision ...). Ce fut également l'occasion de mener un projet avec des contraintes de temps et des consignes précises respectant les standards académiques.
                Ce mémoire m'a permis synthétiser mes pensées pour faire comprendre mon travail à toute personne, même non spécialiste. 
                """,
        "data_origin": "INSEE, Google Trends",
        "data_link": "https://github.com/Jules-Bstats/memoire/blob/main/data_memoire.csv",
                "project_file": "docs/nuitees_projet.pdf",
                "synthesis_file": "docs/nuitees_synthese.pdf"
    },

# POWER BI -----------------------------------------------------------------------------------------
    "dashboard": {
        "title": "Dashboard Power BI",
        "date": "Mars 2025",
        "summary": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "image": "img/projet2.jpg",
        "skills": ["powerbi", "solo"],
        "comment": "Lorem ipsum dolor sit amet. Autoévaluation : bonne prise en main de Power BI, à approfondir sur les mesures DAX complexes.",
        "data_origin": "Kaggle",
        "data_link": "https://www.kaggle.com",
                "project_file": "docs/nuitees_projet.pdf",
                "synthesis_file": "docs/nuitees_synthese.pdf"
    },

# BIOSTAT -----------------------------------------------------------------------------------------


    "Nettoyage": {
            "title": "Nettoyage de données ",
            "date": "Novembre 2025",
            "summary": """
                Dans le cadre d’un projet de biostatistique réalisé en binôme sur une enquête d'Etalab, l’objectif était d’analyser l’attractivité des métiers du numérique dans la fonction publique et de 
                maîtriser le traitement des valeurs manquantes. Pour ce faire, la base initiale a été enrichie et nettoyée sous RStudio, passant de 13 à 28 variables grâce à l'ajout de nouvelles dimensions quantitatives et qualitatives. 
                Une perte de données de 15 % a ensuite été simulée artificiellement sur plusieurs variables clés afin de tester des stratégies rigoureuses d'imputation. Le projet mobilise une panoplie de techniques comparées, allant des 
                régressions linéaires et logistiques aux approches par la médiane selon le genre et l'expérience, en passant par l'algorithme MICE (Predictive Mean Matching). 
                """,
                "summary_bottom":"""Les principaux résultats démontrent que la méthode MICE s'avère la 
                plus performante pour estimer les variables quantitatives comme les salaires, tandis que l'approche par tendances observées fonctionne mieux pour les qualitatives.  """,
            "image": "img/projet3.jpg",
            "skills": ["r", "binome"],
            "comment": """L'auto-critique met toutefois en lumière la complexité inhérente 
                l'imputation de telles bases issues d'enquêtes, particulièrement lorsque la majorité des variables sont qualitatives et possèdent de multiples modalirés.""",
            "data_origin": "INSEE",
            "data_link": "https://www.insee.fr/fr/statistiques",
                "project_file": "docs/nuitees_projet.pdf",
                "synthesis_file": "docs/nuitees_synthese.pdf"
        },


# PREVISION BROCOLI -----------------------------------------------------------------------------------------
        "brocolis": {
                "title": "Prévision du prix du brocoli aux USA",
                "date": "Septembre 2025",
                "summary": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                "image": "img/projet5.jpg",
                "skills": ["r", "binome"],
                "comment": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Autoévaluation : projet abouti, bonne maîtrise des modèles SARIMA, marge d'amélioration sur l'automatisation du pipeline.",
                "data_origin": "FED",
                "data_link": "https://www.insee.fr/fr/statistiques",
                "project_file": "docs/nuitees_projet.pdf",
                "synthesis_file": "docs/nuitees_synthese.pdf"
            },


# ANALYSE EXPLORATOIRE  -----------------------------------------------------------------------------------------
            
            "Analyse  de donnees": {
                    "title": """Analyse des inégalités entre les pays du monde à l'aide  d’indicateurs socio-économiques,
                                démographiques et sanitaires""",
                    "date": "Février 2026",
                    "summary": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                    "image": "img/projet4.jpg",
                    "skills": ["r", "binome"],
                    "comment": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Autoévaluation : projet abouti, bonne maîtrise des modèles SARIMA, marge d'amélioration sur l'automatisation du pipeline.",
                    "data_origin": "INSEE",
                    "data_link": "https://www.insee.fr/fr/statistiques",
                    "project_file": "docs/nuitees_projet.pdf",
                    "synthesis_file": "docs/nuitees_synthese.pdf"
                    
                },


# R SHINY  -----------------------------------------------------------------------------------------

            "viz memoire": {
                        "title": "Application R-Shiny : visualisation des prévisions de fréquentation touristique en France",
                        "date": "Juin2026",
                        "summary": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                        "image": "img/projet7.jpg",
                        "skills": ["r-shiny", "data-viz"],
                        "comment": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Autoévaluation : projet abouti, bonne maîtrise des modèles SARIMA, marge d'amélioration sur l'automatisation du pipeline.",
                        "data_origin": "INSEE",
                        "data_link": "https://www.insee.fr/fr/statistiques",
                        "project_file": "docs/nuitees_projet.pdf",
                        "synthesis_file": "docs/nuitees_synthese.pdf"
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