import requests

query = input("iTunes Cover Downloader\n\nEnter album name: ")
response = requests.get("https://itunes.apple.com/search?entity=album&limit=1&term=" + query, allow_redirects = True)

json = response.json()['results'][0]

imageLink = json['artworkUrl100'].replace("100x100bb.jpg", "600x600bb.jpg")
imageName = json['collectionName'] + ".jpg"
imageFile = requests.get(imageLink)

with open(imageName, 'wb') as file:
	file.write(imageFile.content)
	
print("Downloaded as " + imageName)
