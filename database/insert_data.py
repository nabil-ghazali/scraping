import sqlite3
import pandas as pd
import sqlite3
import pandas as pd

# Lire les données du fichier

# df_books = pd.read_csv("/home/nabil_simplon/scraping-1/get_data/books_info.csv")

def create_BDD (df_books= "data/data_scraping.csv", db_path = "data/book_store.db") -> None:
    df_books = pd.read_csv(df_books)

    # Création de la BDD et insertion des données
    connection = sqlite3.connect(db_path)
    # vérifier la bonne création de la base de données
    print(connection.total_changes)
    # structurer votre base de données, Cursor permet alors d’envoyer des commandes SQL à votre base de données.
    cursor = connection.cursor()

    if 'Unnamed: 0' in df_books.columns:
        df_books = df_books.drop(columns=['Unnamed: 0'])

    # df_books = pd.read_csv("books_info.csv")
    df_books.to_sql(
        name= 'book',
        con=connection,
        if_exists='append',
        index=True,
        index_label='book_id'
    )

    # Compter le nombre de livre dans la BDD
    cursor.execute("SELECT COUNT(book_id) FROM book")
    resultat = cursor.fetchone()
    print(f"Le nombre de livres : {resultat[0]}")


    connection.commit()
    connection.close()