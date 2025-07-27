# Import des fonctions principales de scraping et de l'API
from pipelines.pipeline_scraping import run_scrapping
from api_pipeline.pipeline_api import run_api_pipeline

def main():
    """
    Fonction principale qui orchestre l'exécution du scraping de livres et de la récupération de données depuis l'API Google Books.
    
    Étapes :
    1. Demande à l'utilisateur combien de pages il souhaite scraper.
    2. Lance le pipeline de scraping local avec le nombre de pages spécifié.
    3. Lance ensuite le pipeline de récupération de données depuis l'API Google Books.
    4. Gère les erreurs potentielles dans chaque étape.
    """
    
    print("Bienvenue dans l'application de scraping!")
    
    # Demande à l'utilisateur le nombre de pages à scraper
    number_pages = int(input("Combien de pages voulez-vous scraper : "))
    
    # Étape 1 : Lancer le scraping local
    try:
        run_scrapping(number_pages)
    except Exception as e:
        print(f"Une erreur est survenue pendant le scraping : {e}")

    # Étape 2 : Lancer la récupération de données via l'API Google Books
    print("Nous allons maintenant importer des données à partir de l'API Google : ")
    try:
        run_api_pipeline(number_pages)
    except Exception as e:
        print(f"Une erreur est survenue pendant l'appel à l'API : {e}")

# Point d'entrée du script
if __name__ == "__main__":
    main()
