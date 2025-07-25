from process_data.process_scraping_data import  convert_types
from get_data.get_scraping_data import  scrape_books
from database.insert_data import create_BDD
import pandas as pd
import os


def run_scrapping (int):
    print("Lancement du scraping")
    books_scraped = scrape_books(int)
    df = pd.DataFrame(books_scraped)
    df_cleaned = convert_types(df)
    print(f"Données nettoyées : {len(df_cleaned)}" )
    print("Sauvegarde des données en cours ...")
    os.makedirs("data", exist_ok=True) #crée le dossier s'il n'existe pas
    raw_csv_path = "data/data_scraping.csv"
    df_cleaned.to_csv(raw_csv_path)
    print(f"Données sauvegardés dans : {raw_csv_path}")
    print(f"Insertion des données en base de données")
    create_BDD(df_books=raw_csv_path)