import requests
import bs4

result = requests.get("https://www.videoschool.com/photography/")

soup = bs4.BeautifulSoup(result.text, "html.parser")


"""central_block = soup.select(".fusion-text.fusion-text-1 h1  ")

for h in central_block:
    print(h.getText())"""

images = soup.select(".img-responsive")[0]["src"]

print(images)

images1 = requests.get(images)

f = open("my_image.jpg", "wb")
f.write(images1.content)
f.close()
