import requests

response = requests.get('https://api.flickr.com/services/rest/?method=flickr.favorites.getPublicList&api_key=5e726571cb05962eebdd2232c6fcebb2&user_id=99806945@N03')

outfile = open('flickFave.txt','w')
outfile.write(response.text)


#response = requests.get('https://lefty.io/_api/v1/search?from=0&q="hiking"&size20&sort=4&colors=maroon&cats=outdoor&client_id=6b5c93079db0adb5cc4685e5af5e2cf&client_secret=284a6d2c4e8028a687c3ccd249cbb12')

# https://lefty.io/_api/v1/search?from=0&q="hiking"&size20&sort=4&colors=maroon&cats=outdoor&client_id=6b5c93079db0adb5cc4685e5af5e2cf&client_secret=284a6d2c4e8028a687c3ccd249cbb12







 
    

