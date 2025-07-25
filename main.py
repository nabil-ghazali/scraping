from pipelines.pipeline_scraping import run_scrapping

def main():
    print("Bienvenue dans l'application de scraping!")
    number_pages = int(input("Compien de pages voulez vous scrapez : "))
    try:
        run_scrapping(number_pages)
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
if __name__ == "__main__":
    main()
   