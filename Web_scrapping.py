import requests
from bs4 import BeautifulSoup
import pandas as pd

def start():
    price = []
    model = []
    link = []
    rating = []
    performance = []
    img = []
    spec = []
    camera = []
    display = []
    battery = []
    design = []
  

    for i in range(45):
        print(i)
        url = "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&q=mobile&otracker=categorytree&page=" + str(i)
        response = requests.get(url)
        print(response)
        soup = BeautifulSoup(response.content, "html.parser")
        cost = soup.find_all("div", {"class": "_30jeq3 _1_WHN1"})
        reference = soup.find_all("a", {"class": "_1fQZEK"})
        name = soup.find_all("div", {"class": "_4rR01T"})
        images = soup.find_all("img", {"loading": "eager"})

        for i in cost:
            a = i.text
            b = a.split('₹')
            d = b[1].split(',')
            c = ''
            for i in range(len(d)):
                c = c + d[i]
            price.append(int(c))

        for i in name:
            model.append(i.text)

        for i in reference:
            link.append("https://www.flipkart.com"
                        + i.get('href'))

        for i in images:
            img.append(i.get('src'))
    print(cost, name, reference)
    for i in range(len(link)):
        phone_url = link[i]
        content = requests.get(phone_url)
        soup = BeautifulSoup(content.content, "html.parser")
        rating_ = soup.find_all("text", {"class": "_2Ix0io"})
        overall = soup.find("div", {"class": "_2d4LTz"})
        specification = soup.find_all("li", {"class": "_21Ahn-"})
        rating2 = []
        temp = []

        for i in rating_:
            print(i)
            a = i.text
            rating2.append(float(i.text))
        rating.append(rating2)

        for i in specification:
            temp.append(i.text + "\n")
        spec.append(temp)
        del temp

        if overall == None or rating2 == []:
            pass
        else:
            performance.append(float(overall.text))
        del rating2

    temp = []
    z = 0
    for i in range(len(rating)):
        if (len(rating[i]) == 0):
            temp.append(i-z)
            z = z+1

    for i in temp:
        del rating[i]
        del price[i]
        del img[i]
        del link[i]
        del model[i]
        del spec[i]

    del temp
    print(rating)
    for i in range(len(rating)):
        if len(rating[i]) == 4:  
            camera.append(rating[i][0])
            battery.append(rating[i][1])
            display.append(rating[i][2])
            design.append(rating[i][3])
        else: 
            del price[i]
            del img[i]
            del link[i]
            del model[i]
            del spec[i]
            del performance[i]
    print(len(model))
    print(len(price))
    print(len(link))
    print(len(img))
    print(len(camera))
    print(len(design))  
    print(len(display))
    print(len(battery))
    print(len(spec))
    print(len(performance))

    data_set = {"model": model, "price": price, "specification": spec, "display": display, "camera": camera,
                "performace": performance, "battery": battery, "design": design, "url": link, "image": img}
    data = pd.DataFrame(data_set)
    
    data.to_csv("test11.csv", index=False)
    print(data)


start()

