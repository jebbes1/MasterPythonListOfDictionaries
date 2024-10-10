books = [
    {"Title": "Darkness Hour", "Author": "Aatrox D. Darkness", "Publication Year": "1998", "ISBN": 978-3-16-148410-0, "Genre": "Thriller, Mystery"},
    {"Title": "Lightness Hour", "Author": "Kyle D. Light", "Publication Year": "1991", "ISBN": 978-0-7432-7356-5, "Genre": "Romantic, Drama"},
    {"Title": "Happiest of my life", "Author": "Teemo D. Veli", "Publication Year": "2010", "ISBN": 978-0-452-28423-4, "Genre": "Adventure, Drama"},
    {"Title": "Monster of Demacia", "Author": "Fiddle D. Stick", "Publication Year": "1999", "ISBN": 978-1-4516-7321-8, "Genre": "Horror, Myster, Thriller"},
    {"Title": "Void Century", "Author": "Kass D. Adin", "Publication Year": "1942", "ISBN": 978-3-16-148410-0, "Genre": "Adventure, Mystery, Thriller, Horror"},
]

for book in books:
    print(f"Title Name: {book["Title"]} | Author: {book["Author"]} | Publication Year: {book["Publication Year"]} | ISGN: {book["ISBN"]} | Genre: {book["Genre"]}" )