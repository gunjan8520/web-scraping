import requests
from bs4 import BeautifulSoup
def start(l, m, p1, p2, p3):
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
    final_price = []
    final_model = []
    final_link = []
    final_camera = []
    final_img = []
    final_display = []
    final_design = []
    final_battery = []
    final_performance = []
    final_spec = []


    

    for i in range(45):
            print(i)
            url = "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&page=" + \
                str(i)
            response = requests.get(url)
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

    for i in range(len(price)):
            phone_url = link[i]
            content = requests.get(phone_url)
            soup = BeautifulSoup(content.content, "html.parser")
            rating_ = soup.find_all("text", {"class": "_2Ix0io"})
            overall = soup.find_all("div", {"class": "_2d4LTz"})
            specification = soup.find_all("li", {"class": "_21Ahn-"})
            rating2 = []
            temp = []
            for i in rating_:
                rating2.append(float(i.text))
            rating.append(rating2)
            del rating2

            for i in specification:
                temp.append(i.text + "\n")
            spec.append(temp)
            del temp

            for i in overall:
                performance.append(float(i.text))

    for i in range(len(rating)):
            camera.append(rating[i][0])
            battery.append(rating[i][1])
            display.append(rating[i][2])
            design.append(rating[i][3])
    del rating


  
    minimum = l
    maximum = m
    priority1 = p1
    priority2 = p2
    priority3 = p3
    for i in range(len(price)):
            if (price[i] >= minimum and price[i] <= maximum):
                final_link.append(link[i])
                final_price.append(price[i])
                final_img.append(img[i])
                final_model.append(model[i])
                final_camera.append(camera[i])
                final_design.append(design[i])
                final_battery.append(battery[i])
                final_display.append(display[i])
                final_spec.append(spec[i])
                final_performance.append(performance[i])

    length = len(final_camera)

    if priority1 == "Camera":
            x = max(final_camera)
            for i in range(len(final_camera)):
                if final_camera[i] >= x-0.3:
                    final_link.append(final_link[i])
                    final_price.append(final_price[i])
                    final_img.append(final_img[i])
                    final_model.append(final_model[i])
                    final_camera.append(final_camera[i])
                    final_design.append(final_design[i])
                    final_battery.append(final_battery[i])
                    final_display.append(final_display[i])
                    final_spec.append(final_spec[i])
                    final_performance.append(final_performance[i])

    elif priority1 == "Performance":
            x = max(final_performance)
            for i in range(len(final_performance)):
                if final_performance[i] >= x-0.3:
                    final_link.append(final_link[i])
                    final_price.append(final_price[i])
                    final_img.append(final_img[i])
                    final_model.append(final_model[i])
                    final_camera.append(final_camera[i])
                    final_design.append(final_design[i])
                    final_battery.append(final_battery[i])
                    final_display.append(final_display[i])
                    final_spec.append(final_spec[i])
                    final_performance.append(final_performance[i])

    else:
            x = max(final_battery)
            for i in range(len(final_battery)):
                if final_battery[i] >= x-0.3:
                    final_link.append(final_link[i])
                    final_price.append(final_price[i])
                    final_img.append(final_img[i])
                    final_model.append(final_model[i])
                    final_camera.append(final_camera[i])
                    final_design.append(final_design[i])
                    final_battery.append(final_battery[i])
                    final_display.append(final_display[i])
                    final_spec.append(final_spec[i])
                    final_performance.append(final_performance[i])

    for i in range(length):
            del final_camera[0]
            del final_performance[0]
            del final_battery[0]
            del final_display[0]
            del final_design[0]
            del final_price[0]
            del final_model[0]
            del final_link[0]
            del final_img[0]
            del final_spec[0]

    length = len(final_camera
                    )
    if priority2 == "Camera":
            x = max(final_camera)
            for i in range(len(final_camera)):
                if final_camera[i] >= x-0.3:
                    final_link.append(final_link[i])
                    final_price.append(final_price[i])
                    final_img.append(final_img[i])
                    final_model.append(final_model[i])
                    final_camera.append(final_camera[i])
                    final_design.append(final_design[i])
                    final_battery.append(final_battery[i])
                    final_display.append(final_display[i])
                    final_spec.append(final_spec[i])
                    final_performance.append(final_performance[i])

    elif priority2 == "Performance":
            x = max(final_performance)
            for i in range(len(final_performance)):
                if final_performance[i] >= x-0.3:
                    final_link.append(final_link[i])
                    final_price.append(final_price[i])
                    final_img.append(final_img[i])
                    final_model.append(final_model[i])
                    final_camera.append(final_camera[i])
                    final_design.append(final_design[i])
                    final_battery.append(final_battery[i])
                    final_display.append(final_display[i])
                    final_spec.append(final_spec[i])
                    final_performance.append(final_performance[i])

    else:
            x = max(final_battery)
            for i in range(len(final_battery)):
                if final_battery[i] >= x-0.3:
                    final_link.append(final_link[i])
                    final_price.append(final_price[i])
                    final_img.append(final_img[i])
                    final_model.append(final_model[i])
                    final_camera.append(final_camera[i])
                    final_design.append(final_design[i])
                    final_battery.append(final_battery[i])
                    final_display.append(final_display[i])
                    final_spec.append(final_spec[i])
                    final_performance.append(final_performance[i])

    for i in range(length):
            del final_camera[0]
            del final_performance[0]
            del final_battery[0]
            del final_display[0]
            del final_design[0]
            del final_price[0]
            del final_model[0]
            del final_link[0]
            del final_img[0]
            del final_spec[0]

    length = len(final_camera
                    )
    if priority3 == "Camera":
            x = max(final_camera)
            for i in range(len(final_camera)):
                if final_camera[i] >= x-0.3:
                    final_link.append(final_link[i])
                    final_price.append(final_price[i])
                    final_img.append(final_img[i])
                    final_model.append(final_model[i])
                    final_camera.append(final_camera[i])
                    final_design.append(final_design[i])
                    final_battery.append(final_battery[i])
                    final_display.append(final_display[i])
                    final_spec.append(final_spec[i])
                    final_performance.append(final_performance[i])

    elif priority3 == "Performance":
            x = max(final_performance)
            for i in range(len(final_performance)):
                if final_performance[i] >= x-0.3:
                    final_link.append(final_link[i])
                    final_price.append(final_price[i])
                    final_img.append(final_img[i])
                    final_model.append(final_model[i])
                    final_camera.append(final_camera[i])
                    final_design.append(final_design[i])
                    final_battery.append(final_battery[i])
                    final_display.append(final_display[i])
                    final_spec.append(final_spec[i])
                    final_performance.append(final_performance[i])

    else:
            x = max(final_battery)
            for i in range(len(final_battery)):
                if final_battery[i] >= x-0.3:
                    final_link.append(final_link[i])
                    final_price.append(final_price[i])
                    final_img.append(final_img[i])
                    final_model.append(final_model[i])
                    final_camera.append(final_camera[i])
                    final_design.append(final_design[i])
                    final_battery.append(final_battery[i])
                    final_display.append(final_display[i])
                    final_spec.append(final_spec[i])
                    final_performance.append(final_performance[i])

    for i in range(length):
            del final_camera[0]
            del final_performance[0]
            del final_battery[0]
            del final_display[0]
            del final_design[0]
            del final_price[0]
            del final_model[0]
            del final_link[0]
            del final_img[0]
            del final_spec[0]
    final = []
    final.append(final_model)
    final.append(final_spec)
    final.append(final_img)
    final.append(final_link)
    return final



print(start(5000,10000,"Performance","Camera","Battery"))