import urllib.request
import json
import requests

def nowviewer (user):
    now = count(user,"now")
    return now

def totalviewer (user):
    total = count(user,"total")
    return total

def count (user,mode):
    movie1 = urllib.request.Request("https://frontendapi.twitcasting.tv/users/" + user + "/latest-movie")
    with urllib.request.urlopen(movie1) as res:
        userjson = json.loads(res.read())
        movie = userjson["movie"]["id"]
        status = userjson["movie"]["is_on_live"]
        if status == True:        
            tttto = "https://twitcasting.tv/happytoken.php"
            res = requests.post(tttto,data={"movie_id":movie})
            tokenjson = json.loads(res.text)
            token = tokenjson["token"]
            url = "https://frontendapi.twitcasting.tv/movies/" + str(movie) + "/status/viewer?token=" + token
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req) as res:
                body = res.read()
                j1 = json.loads(body)
                movie = j1["movie"]
                view = movie["viewers"]
                now = view["current"]
                total = view["total"]
                if mode == "now":
                    return now
                elif mode == "total":
                    return total