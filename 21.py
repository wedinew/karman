import requests
from bs4 import BeautifulSoup
import socket
import pickle
url='https://magadan.kinoafisha.info/afisha/schedule/?'
request=requests.get(url).text
soup=BeautifulSoup(request)
parser=soup.find('div',class_='showtimes showtimes-align bottom40').find_all('div',class_='films_right')
par1=soup.find_all('div',class_='showtimes_frame')

def par():
    for i in parser:
        urls=i.find('a').get('href')
        fil_url=urls.replace('//','')
        http='https://'
        rop=http+fil_url
        film_urls=requests.get(rop).text
        film_soup=BeautifulSoup(film_urls)
        par_film=film_soup.find_all('div',class_='grid_cell10')
        par_film2=film_soup.find_all('div',class_='showtimes_frame')
        par_film3=film_soup.find_all('div',class_='showtimes_item showtimes_item-border fav fav-theater')
        par_film4=film_soup.find_all('div',class_='grid')
        for y in par_film4:
            try:
                img_=y.find('a',class_='movieInfo_posterLink').get('href')
                img.append(img_)
            except AttributeError:
                pass
        for x in par_film:

            try:
                name=x.find('div',class_='movieInfo_main grid_cell8').find('h1').text
                name_fil=name.replace('\t','').replace('\n','')
                name_fil2=name_fil[:len(name_fil)-6]
                kino_name.append(name_fil2)
            except AttributeError:
                pass
            try:
                usa=x.find('div',class_='movieInfo_par').text
                usa2=usa.replace('  ','\n').replace('\t','\n')
                info.append(usa2)
            except AttributeError:
                pass
            try:
                reje_=x.find('p',class_='movieInfo_par').text
                reje_1=reje_.replace('\n',' ').replace('\t','')
                reje_2=reje_1[1:]
                reje.append((reje_2))
            except AttributeError:
                t32=0
                t32+=1
                if t32==2:
                    reje.append('Режиссер: None')
                    t32=0
                if t32==2:
                    t32-=2
            try:
                opis_=x.find('div',id='movieInfo-desc').text
                opis_fil=x.find('div',id='movieInfo-desc').find('div',class_='moreBox js-active').text

                filtr=opis_.replace(opis_fil,'')
                opis.append(filtr)
            except AttributeError:
                pass

            try:
                genre_=x.find('div',class_='movieInfo_genre').text
                genre_1=genre_.replace('\t','').replace('\n',' ').replace('    ','').replace('р:','р: ')
                genre.append(genre_1)
            except AttributeError:
                pass

    for i in par1:
        k=i.find_all('div',class_='showtimes_item showtimes_item-border fav fav-theater')
        print('----------------------------------------------------------')
        rex=str(p).replace('[','').replace(']','').replace('\'','').replace(':,',':')
        xx.append(rex)
        p.clear()
        for u in k:
            gg=u.find_all('a',class_='session2')
            gg1=u.find('span').text
            p.append('..'+gg1+':')
            for i in gg:
                try:
                    ss.clear()
                    r1=i.find('span',class_='session2_price').text
                    r2=r1.replace(' ₽',' руб|')
                    ss.append(r2)
                except AttributeError:
                    pass
                try:
                    try:
                        rr=i.find('span',class_='session2_time').text
                        rrr=rr+'-'+ss[0]
                        p.append(rrr)
                    except IndexError:
                        rrr1=rr+'-'+'000'
                        p.append(rrr1)

                except AttributeError:
                    pass
ss=[]
p=[]
xx=[]



kino_name=[]
info=[]
genre=[]
reje=[]
opis=[]
mani=[]
img=[]
par()
xx.pop(0)

print(len(kino_name))
print(len(info))
print(len(img))
print(len(genre))
print(len(opis))

rex1=str(p).replace('[','').replace(']','').replace('\'','').replace(':,',':')
xx.append(rex1)

print(xx)


sock=socket.socket()
sock.bind(('',8080))
sock.listen()
while 1==1:
    conn, addr=sock.accept()
    data_1=pickle.dumps(kino_name)
    data_2=pickle.dumps(info)
    data_3=pickle.dumps(genre)
    data_4=pickle.dumps(reje)
    data_5=pickle.dumps(opis)
    data_6=pickle.dumps(xx)
    data_7=pickle.dumps(img)
    conn.send(data_1)
    conn.send(data_2)
    conn.send(data_3)
    conn.send(data_4)
    conn.send(data_5)
    conn.send(data_6)
    conn.send(data_7)
