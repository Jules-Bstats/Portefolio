from flask import Flask, render_template, abort

app = Flask(__name__)

PROJECTS = {

# accident de la route -----------------------------------------------------
    "accident routier": {
                "title": "Analyse économétrique du taux d'accidents de la route en France",
                "date": "Décembre 2025",
                "summary": """
                    Ce projet d'économétrie cherche à expliquer les fortes disparités départementales du taux d'accidents mortels en France métropolitaine
                    pour l'année 2023, afin d'orienter les politiques publiques territoriales. La problématique consiste à identifier les facteurs structurels 
                    (géographiques, démographiques, météorologiques et liés aux infrastructures) qui influencent ce taux, au-delà des comportements individuels des conducteurs. 
                    Pour ce faire, nous avons constitué une base de données de 19 variables (en excluant les piétons et les territoires d'outre-mer). Nous avons ensuite fait une régression 
                    via la méthode d'estimation des Moindres Carrés Ordinaires (MCO) pour construire notre modèle explicatif final.
                    """,
                    "summary_bottom":"""Le modèle final explique environ 63 % de la variabilité de la mortalité routière interdépartementale et offre une très bonne précision 
                    de prévision (RMSE de 0,052). L'analyse démontre qu'une pluviométrie abondante et un fort dénivelé géographique augmentent significativement le taux d'accidents 
                    mortels. Au contraire, une plus grande densité d'autoroutes et de routes départementales permet de faire baisser cette mortalité. Enfin, la proportion d'hommes 
                    au sein d'un département n'a statistiquement aucun impact significatif sur ces disparités. """,
                "image": "img/projet6.jpg",
                "skills": ["R", "MCO", "Économétrie Quantitative"],
                "comment": """Le choix de l'échelle départementale crée un biais de variables omises majeur, car il empêche d'intégrer les comportements individuels qui sont les causes 
                premières des accidents (vitesse, alcool, stupéfiants). Ensuite, pour contourner de forts problèmes de multicolinéarité, nous avons simplement exclu de nombreuses 
                variables de leur base, amputant ainsi l'analyse d'informations utiles, ce qui n'est pas l'idéal. De plus, la forme log-linéaire du modèle conduit à des interprétations irréalistes d'un point de 
                vue pratique (comme une baisse de 99,5 % de la mortalité si l'on ajoute 1 km d'autoroute par km carré). Enfin, le modèle souffre d'un fort risque de surajustement (overfitting) 
                aux données spécifiques de 2023 et élude complètement le problème d'endogénéité des infrastructures routières, faute d'avoir trouvé des variables instrumentales adéquates. """,
                "data_origin": "INSEE, Data.gouv.fr, Météo France",
                "data_file": "data/base_mortalite_routiere.csv",
                "project_file": "docs/projet_accident.pdf",
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
        "skills": ["R", "R-Shiny", "Série Temporelle","Prévision"],
        "comment": """
                Ce travail de recherche m'a permis de développer mes compétences techniques (R, R-Shiny) et analytiques 
                (modélisation, prévision ...). Ce fut également l'occasion de mener un projet avec des contraintes de temps et des consignes précises respectant les standards académiques.
                Ce mémoire m'a permis synthétiser mes pensées pour faire comprendre mon travail à toute personne, même non spécialiste. 
                """,
        "data_origin": "INSEE, Google Trends",
        "data_file": "data/data_memoire.csv",
                "project_file": "docs/memoire.pdf",
                "synthesis_file": "docs/note_synthese_memoire.pdf"
    },

# POWER BI -----------------------------------------------------------------------------------------
    "dashboard": {
        "title": "Dashboard Power BI",
        "date": "Mars 2025",
        "summary": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "image": "img/projet2.jpg",
        "skills": ["PowerBI", "Data-Viz", "DAX"],
        "comment": "Lorem ipsum dolor sit amet. Autoévaluation : bonne prise en main de Power BI, à approfondir sur les mesures DAX complexes.",
        "data_origin": "Simulation de données via IA générative",
                "project_link": "https://app.powerbi.com/links/rLNg-HaM9c?ctid=3e08a669-4292-42cb-aaff-083b43a0d551&pbi_source=linkShare",
                "synthesis_file": "docs/note_synthese_bi.pdf"
    },

# BIOSTAT -----------------------------------------------------------------------------------------


    "Nettoyage": {
            "title": "Analyse de l'attractivité du numérique dans la fonction publiquue : nettoyage et imputation de valeurs manquantes",
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
            "skills": ["R", "Imputation", "Nettoyage", "Analyse Exploratoire"],
            "comment": """L'auto-critique met toutefois en lumière la complexité inhérente 
                l'imputation de telles bases issues d'enquêtes, particulièrement lorsque la majorité des variables sont qualitatives et possèdent de multiples modalirés.""",
            "data_origin": "Etalab",
            "data_link": "https://www.data.gouv.fr/datasets/sondage-metiers-du-numerique-et-service-public-1",
                "project_file": "docs/biostat.pdf"        
                },


# PREVISION BROCOLI -----------------------------------------------------------------------------------------
        "brocolis": {
                "title": "Prévision du prix du brocoli aux USA",
                "date": "Septembre 2025",
                "summary": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                "image": "img/projet5.jpg",
                "skills": ["R", "Prévision", "Série temporelle"],
                "comment": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Autoévaluation : projet abouti, bonne maîtrise des modèles SARIMA, marge d'amélioration sur l'automatisation du pipeline.",
                "data_origin": "FED",
                "data_file": "data/base_brocoli.csv",
                "project_file": "docs/brocoli.pdf"
            },


# ANALYSE EXPLORATOIRE  -----------------------------------------------------------------------------------------
            
            "Analyse  de donnees": {
                    "title": """Analyse des inégalités entre les pays du monde à l'aide  d’indicateurs socio-économiques,
                                démographiques et sanitaires""",
                    "date": "Février 2026",
                    "summary": """ Ce projet d'analyse de données vise à étudier les inégalités macroéconomiques, sanitaires et démographiques entre 167 pays, à partir d'une base de données Kaggle enrichie de deux variables 
                    qualitatives représentant le niveau de développement et la région géographique. La démarche méthodologique s'appuie d'abord sur des analyses descriptives univariées et bivariées utilisant des matrices de 
                    corrélation de Spearman, des analyses de variance (ANOVA) et des tests du Khi-2. Les auteurs utilisent ensuite des méthodes d'analyse multidimensionnelle, plus précisément une Analyse Factorielle des Correspondances
                      (AFC) et une Analyse en Composantes Principales (ACP) suivie d'une classification, pour modéliser la structure globale des disparités mondiales. """,
                      "summary_bottom":"""Les résultats démontrent une polarisation extrême des conditions de vie à l'échelle mondiale, l'espérance de vie étant très fortement corrélée de manière positive au revenu et de manière négative 
                      à la mortalité infantile ou à la fécondité. L'AFC met en évidence une structure hiérarchisée opposant diamétralement l'Afrique sous-développée à l'Europe développée, avec l'Amérique et l'Asie dans des positions de 
                      transition. L'ACP et la classification finale confirment cette fracture structurelle en regroupant les nations en trois profils distincts, séparant très nettement les pays européens riches à forte qualité de vie, 
                      les nations américaines aux revenus intermédiaires, et les pays africains pauvres caractérisés par de fortes contraintes sanitaires et démographiques. """,
                    "image": "img/projet4.jpg",
                    "skills": ["R", "ACP", "Clustering", "Analyse Exploratoire"],
                    "comment": """L'étude présente toutefois plusieurs limites méthodologiques, notamment la suppression arbitraire des variables liées aux importations et aux dépenses de santé pour forcer la pertinence de l'ACP, ce qui 
                    ampute le modèle d'informations socio-économiques potentiellement révélatrices. De plus, la gestion des valeurs extrêmes reste discutable car si le Luxembourg a été retiré de l'analyse principale pour éviter d'écraser 
                    es résultats, d'autres pays aux revenus atypiques comme Singapour ou le Qatar ont été conservés, ce qui rend l'interprétation du deuxième axe de l'ACP particulièrement confuse et contre-intuitive selon les auteurs eux-mêmes. 
                    Enfin, l'utilisation d'un nombre aussi restreint d'indicateurs limite structurellement la capacité du modèle"
                    final à capter l'entière complexité des inégalités de développement dans le monde. """,
                    "data_origin": "Kaggle",
                    "data_link": "https://www.kaggle.com/code/leilahasan/pca-unsupervised-dimensionality-reduction-techniq",
                    "project_file": "docs/analyse_explo.pdf"
                   
                    
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