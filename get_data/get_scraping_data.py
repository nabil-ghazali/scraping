import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fonction pour extraire le titre d'un livre
def extract_title(book: BeautifulSoup) -> str:
    """Extract the title of a book from a BeautifulSoup object.

    Args:
        book (BeautifulSoup): The HTML element of the book.

    Returns:
        str: The title of the book.
    """
    # On affiche le titre d'un livre
    title_book = book.find("h3").find("a")["title"]
    # print(f"Titre d'un livre : {title_book}")
    return title_book
# Fonction pour extraire le prix d'un livre
def extract_price(book: BeautifulSoup) -> str:
    """Extract the price of a book from a BeautifulSoup object.

    Args:
        book (BeautifulSoup): The HTML element of the book.

    Returns:
        str: The price of the book.
    """
    # Prix d'un livre
    price_book = book.find("div", class_="product_price").find("p").text
    # print(f"Prix d'un livre : {price_book}")
    return price_book
# Fonction pour extraire la note d'un livre
def extract_rating(book: BeautifulSoup) -> str:
    """Extract the rating of a book from a BeautifulSoup object.

    Args:
        book (BeautifulSoup): The HTML element of the book.

    Returns:
        str: The rating of the book.
    """
    # Afficher la note (rating) du premier livre
    rating_book = book.find("p", class_="star-rating")["class"][1]
    # print(f"Note d'un livre : {rating_book}")
    return rating_book
# Fonction pour extraire la disponibilité d'un livre
def extract_availability(book: BeautifulSoup) -> str:
    """Extract the availability of a book from a BeautifulSoup object.

    Args:
        book (BeautifulSoup): The HTML element of the book.

    Returns:
        str: The availability of the book.
    """
    availability_book = book.find("div", class_="product_price").find("p", class_="instock availability").text.strip()
    return availability_book

# Fonction qui combine les informations d'un livre dans un dictionnaire
def extract_book_info(book: BeautifulSoup) -> dict:
    """Extract all information of a book from a BeautifulSoup object.

    Args:
        book (BeautifulSoup): The HTML element of the book.

    Returns:
        dict: A dictionary containing the title, price, rating, and availability of the book.
    """
    book_info = {}
    # Pour chaque livre, on souhaite afficher : le prix, le titre et la disponibilité
    
    title = extract_title(book)
    price = extract_price(book)
    availability = extract_availability(book)
    rating = extract_rating(book)
    # print(f"Titre : {title}, Prix : {price}, Disponibilité : {availability}")

    book_info = {
        "title": title,
        "price": price,
        "rating": rating,
        "availability": availability
    }
    return book_info

# Fonction qui récupère le contenu HTML d'une page à partir de son url
def get_books_html(url: str) -> BeautifulSoup:
    """Fetch the HTML content of a book page.

    Args:
        url (str): The URL of the book page.

    Returns:
        BeautifulSoup: A BeautifulSoup object containing the HTML content.
    """
    # On récupère le contenu HTML d’une page
    response = requests.get(url)

    # On stocke le contenu HTML dans une variable
    html_content = response.content

    # On crée un objet BeautifulSoup pour parser le HTML
    soup = BeautifulSoup(html_content, "html.parser")

    return soup

# Parcourir les pages et récupérer les livres
def scrape_books(pages: int) -> list[dict]:
    """Scrape books from the specified number of pages.

    Args:
        pages (int): The number of pages to scrape.

    Returns:
        list: A list of dictionaries containing books information.
    """
    all_books = []

    for page in range(1, pages + 1):
        url = f"http://books.toscrape.com/catalogue/page-{page}.html"
        soup = get_books_html(url)

        books = soup.find_all("article", class_="product_pod")

        for book in books:
            data_book = extract_book_info(book)
            all_books.append(data_book)

    return all_books

# Test de la fonction scrape_books avec 50 pages
# data_books = scrape_books(5)

# # Création d'un DataFrame à partir de la liste
# df_books = pd.DataFrame(data_books)

# # Sauvegarder les données dans un fichier csv
# df_books.to_csv("books_info.csv", index=False)