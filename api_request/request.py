import sqlite3

import pandas as pd

def insert_data_to_bdd(df_new_books):
    import sqlite3
    import pandas as pd

    # Lecture du fichier CSV existant (facultatif si tu ne l’utilises pas plus bas)
    df_books = pd.read_csv("data/data_scraping.csv")
    start_index = len(df_books)
    print(f"Nombre de livres dans le CSV : {start_index}")

    # Connexion à la base SQLite
    connection = sqlite3.connect("data/book_store.db")
    cursor = connection.cursor()

    # Obtenir le dernier book_id
    cursor.execute("SELECT MAX(book_id) FROM book")
    last_id = cursor.fetchone()[0]
    if last_id is None:
        last_id = 0

    print(f"Dernier book_id existant : {last_id}")

    # Vérifier que le DataFrame à insérer est non vide
    if df_new_books.empty:
        print("Aucune donnée à insérer.")
        connection.close()
        return

    # Générer les nouveaux ID à partir de last_id
    df_new_books = df_new_books.copy()
    df_new_books.insert(0, "book_id", range(last_id + 1, last_id + 1 + len(df_new_books)))

    # Afficher un aperçu pour debug
    print("Extrait des données à insérer :")
    print(df_new_books.head())

    # Insérer dans la base
    df_new_books.to_sql(
        name='book',
        con=connection,
        if_exists='append',
        index=False
    )

    # Vérification post-insertion
    cursor.execute("SELECT COUNT(*) FROM book")
    print("Total de livres dans la base :", cursor.fetchone()[0])

    connection.commit()
    connection.close()
