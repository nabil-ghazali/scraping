import pandas as pd


# Lire les données du fichier
# df_books = pd.read_csv("/home/nabil_simplon/scraping-1/get_data/books_info.csv")

# Fonction pour convertir la valeur de availability en booléen
def convert_availability(value : str) -> bool:
    """Convert the availability value to a boolean.

    Args:
        value (str): The availability status of the book.

    Returns:
        bool: True if the book is available, False otherwise.
    """
    
    if isinstance(value , str) and "in stock" in value.lower().strip():
        return True
    else:
        return False

# Fonction convert_types qui s'occupe de la conversion des données du dataframe
def convert_types(df_books: pd.DataFrame) -> pd.DataFrame:
    """Convert the types of the DataFrame columns to appropriate types.

    Args:
        df_books (pd.DataFrame): The DataFrame containing book data.

    Returns:
        pd.DataFrame: The DataFrame with converted types.
    """
    # Vérification des types de données
    print(df_books.dtypes)

    # Conversion de title en chaîne de caractères
    df_books["title"] = df_books["title"].astype(str)
    # # Convertir la colonne price en type décimal
    df_books["price"] = df_books["price"].str.replace('£', '').astype(float)
    print(df_books["price"].head())

    # # Valeurs possibles de la colonne availability
    # # Afficher les valeurs uniques
    print(df_books['availability'].unique())

    # # Convertir la colonne availability en booléen (True/False)
    df_books["availability"] = df_books["availability"].apply(convert_availability)
    print(df_books['availability'].head())
        
    # Affiche les valeurs uniques originales avant mapping
    print(df_books["rating"].unique())

    # # Convertir la colonne _rating_ en chiffre en utilisant un dictionnaire `rating_map` et la méthode [_map_]
    # Dictionnaire associant les notes au format initial et les valeurs numérique
    ratings_map = {
        'Zero': 0,
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    # df_books["rating"] = df_books["rating"].astype(str).str.strip().str.capitalize()

    df_books["rating"] = df_books["rating"].map(ratings_map)
    print(df_books["rating"].value_counts(dropna=False))

    return df_books