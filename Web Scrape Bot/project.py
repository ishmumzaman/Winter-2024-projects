import bs4
import requests

#URL without page number
basic_url = "http://books.toscrape.com/catalogue/page-{}.html"

#List of 4 or 5 star titles
high_rated_titles = []

#Iterate pages
for page in range(1, 51):

    #Create soup on each page
    url_page = basic_url.format(page)
    result = requests.get(url_page)
    soup = bs4.BeautifulSoup(result.text, "html.parser")

    #Select data of books
    books = soup.select(".product_pod")

    #Iterate books
    for book in books:

    #Check if they are 4 or 5 stars books
        if len(book.select(".star-rating.Four")) != 0  or len(book.select(".star-rating.Five")) != 0:

            #Store title in variable
            book_title = book.select("a")[1]["title"]

            #Add books to list
            high_rated_titles.append(book_title)

#Show 4 or 5 stars books
for b in high_rated_titles:
    print(b)

"""results = requests.get(basic_url.format("1"))

soup = bs4.BeautifulSoup(results.text, "html.parser")

books = (soup.select(".product_pod"))

example = books[0].select("a")[1]["title"]
print(example)"""





"""for p in range(1,11):
    print(basic_url.format(p))"""