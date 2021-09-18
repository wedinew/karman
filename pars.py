import requests
from bs4 import BeautifulSoup
import urllib
import os
import datetime
test=[]
action = []
content = {'боевик':dict(film_name=[],film_janr=[],film_year=[]),
           'комедия':dict(film_name=[],film_janr=[],film_year=[]),
           'вестерн':dict(film_name=[],film_janr=[],film_year=[]),
           'детектив':dict(film_name=[],film_janr=[],film_year=[]),
           'детский':dict(film_name=[],film_janr=[],film_year=[]),
           'фэнтези':dict(film_name=[],film_janr=[],film_year=[])
}
def films():
    g=0
    while g!=10:
        if g==0:
            url= "https://www.kinoafisha.info/rating/movies/"
        if g!=0:
            url="https://www.kinoafisha.info/rating/movies/?page="+str(g)

        res = requests.get(url)
        soup = BeautifulSoup(res.text,"html")

        for n in soup.find_all("div",class_="movieList_item movieItem movieItem-rating movieItem-position"):
            janr=n.find('span',class_='movieItem_genres').text
            jpan_filtr=""
            for x in janr:
                if x ==",":
                    break
                jpan_filtr+=x

            name_film = n.find("span", class_="movieItem_title").text
            filtr = name_film.replace('»',')').replace('«','(').replace(':',';').replace("?","+").replace('"',')').replace('/','99')
            img_pars=n.find("source",type="image/jpeg")

            year=n.find('span',class_='movieItem_year').text
            try:
                content[jpan_filtr]['film_name'].append(filtr)
                content[jpan_filtr]['film_year'].append(year)
                content[jpan_filtr]['film_janr'].append(janr)
            except:
                pass
            img_url = img_pars.get('srcset')
            if os.path.isfile(filtr+".jpg")==False:
                p = requests.get(img_url)
                out = open(filtr+".jpg", "wb")
                out.write(p.content)
                out.close()
            if os.path.isfile(filtr+".jpg")==True:
                pass
        g+=1
    return content
