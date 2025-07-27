from api_get_data import get_data_api as gda
from api_process_data import process_data as prd
from api_request import request as rq

def run_api_pipeline(url='https://www.googleapis.com/books/v1/volumes'):
    """
    Pipeline complète d'extraction, transformation et chargement (ETL) des données depuis l'API Google Books.

    Étapes :
    1. Appelle la fonction `get_data()` pour récupérer les données depuis l’API.
    2. Transforme les données JSON en DataFrame avec `data_to_dataframe()`.
    3. Filtre et nettoie les données avec `filter_data()`.
    4. Insère les données filtrées dans la base de données SQLite.

    Paramètres
    ----------
    url : str, optionnel
        L’URL de l’API Google Books (par défaut : endpoint standard de recherche de livres).

    Retour
    ------
    None
    """

    # 1. Récupération des données brutes depuis l’API
    data_books = gda.get_data()

    # 2. Conversion des données JSON en DataFrame pandas
    df_books = gda.data_to_dataframe(data_books)

    # 3. Filtrage des données (suppression des livres sans titre/prix/note, par exemple)
    df_filtered = prd.filter_data(df_books)

    # 4. Insertion dans la base de données
    rq.insert_data_to_bdd(df_filtered)
