import requests
from github import Github
import urllib.request

"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("imgtest.html", user_image= "https://www4b.wolframalpha.com/Calculate/MSP/MSP5343175c3he563612h1300001f2dc5bhge4412f4?MSPStoreType=image/gif&amp;s=41")

if __name__ == "__main__":
    app.run()

"""

# 9U487H-VALXT3HLLQ -- wolfram Appid
# call to get all awards from a certain year
resp = requests.get(
    "https://api.wolframalpha.com/v2/query?input=Academy+award+2019&podstate=Result__More&podstate=Result__More&includepodid=Result&format=plaintext&output=JSON&appid=9U487H-VALXT3HLLQ"
).json()
# print(resp['queryresult']['pods'][0]['subpods'][0]['plaintext'])
# print(resp)

resp = requests.get(
    "https://api.wolframalpha.com/v2/query?input=best+actor&format=plaintext&output=JSON&appid=9U487H-VALXT3HLLQ"
).json()


print(resp)
# print(resp["queryresult"]["pods"][1]["subpods"][0]["plaintext"])
# print(resp)

# call to get awards & other info by searching an actor
# 3 actors will be Rami Malek, Mahershala Ali, Olivia Colman
# returns basic info of Rami Malek -- name, DOB (age), POB
actor1 = requests.get(
    "https://api.wolframalpha.com/v2/query?input=rami+malek&includepodid=BasicInformation:PeopleData&format=plaintext&output=JSON&appid=9U487H-VALXT3HLLQ"
).json()
print(actor1["queryresult"]["pods"][0]["subpods"][0]["plaintext"])

# returns address of jpg of Rami Malek
actor1pic = requests.get(
    "https://api.wolframalpha.com/v2/query?input=rami+malek&includepodid=Image:PeopleData&format=plaintext&output=JSON&appid=9U487H-VALXT3HLLQ"
).json()

# print(actor1pic['queryresult']['pods'][0]['subpods'][0]['imagesource'])
url = actor1pic["queryresult"]["pods"][0]["subpods"][0]["imagesource"]
print(url)
urllib.request.urlretrieve(
    "https://commons.wikimedia.org/wiki/File:SXSW_2016_-_Rami_Malek_(25138464364)_(cropped_2).jpg",
    "mehershala.jpg",
)

# returns all awards Rami Malek has won of been nomiated for -- award name, year (age), movie
actor1awards = requests.get(
    "https://api.wolframalpha.com/v2/query?input=rami+malek&includepodid=CrossPeopleData:AcademyAwardData&format=plaintext&output=JSON&appid=9U487H-VALXT3HLLQ"
).json()
print(actor1awards["queryresult"]["pods"][0]["subpods"][0]["plaintext"])

# returns list of movies Rami Malek has been in
actor1movies = requests.get(
    "https://api.wolframalpha.com/v2/query?input=rami+malek&includepodid=NotableFilms:PeopleData&format=plaintext&output=JSON&appid=9U487H-VALXT3HLLQ"
).json()
print(actor1movies["queryresult"]["pods"][0]["subpods"][0]["plaintext"])

# returns bio of Rami Malek
actor1bio = requests.get(
    "https://api.wolframalpha.com/v2/query?input=rami+malek&includepodid=WikipediaSummary:PeopleData&format=plaintext&output=JSON&appid=9U487H-VALXT3HLLQ"
).json()
print(actor1bio["queryresult"]["pods"][0]["subpods"][0]["plaintext"])

# use movie list from wolfram to get movie name and search it in new api
movlist = resp["queryresult"]["pods"][0]["subpods"][0]["plaintext"]
movie = movlist.splitlines()
mov = movie[0].split(" | ")
# mov has award name and winner in indexes 0 & 1 respectively, now using search for ease of access

# using omdb api
search = "Green Book"
res = requests.get("http://www.omdbapi.com/?apikey=82ddccc8&?t=Green+Book")
# print(res.json())


# using username and password
# g = Github("austin.blanchard@utexas.edu", "G00seman$")
# or using an access token
g = Github("42fecb005a67ca016a3ef08fc8935d3281269912")
# Github Enterprise with custom hostname
# g = Github(base_url="https://{databaseApp}/api/v3", login_or_token="42fecb005a67ca016a3ef08fc8935d3281269912")

repo = g.get_repo("SahilAshar/EE461L-DatabaseApp")
# contents = repo.get_clones_traffic()
contents = repo.get_clones_traffic()
# print(contents)

# 42fecb005a67ca016a3ef08fc8935d3281269912 -- github pers access token
# res = requests.get('https://api.github.com/repos/:ablanchard10/:EE461L-DatabaseApp/stats/contributors')
# print(res.content)
