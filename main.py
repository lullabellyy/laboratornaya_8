import PIL
from PIL import Image, ImageDraw, ImageFont


def zadanie_1():
    print("задание 1")
    filename = "G:\lab\pichpn.jpg"
    with Image.open(filename) as img:
        img.load()
    img.show()
    img_crop1 = img.crop((50, 150, 900, 1000))
    img_crop1.show()
    img.save("croppic1.jpg")


def zadanie_2():
    print("задание2")

    cards = {'С днем рождения,': 'G:\lab\piccake.jpg', 'С новым годом,': 'G:\lab\pichpn.jpg', 'С пасхой': 'G:\lab\picp.jpg'}
    print(*cards.keys())
    cap = input("Введите праздник - ")
    if "С днем рождения" in cap:
        filename = "G:\lab\piccake.jpg"
        with Image.open(filename) as img:
            img.load()
            img.show()
    if "С новым годом" in cap:
        filename = "G:\lab\pichpn.jpg"
        with Image.open(filename) as img:
            img.load()
            img.show()
    if "С пасхой" in cap:
        filename = "G:\lab\picp.jpg"
        with Image.open(filename) as img:
            img.load()
            img.show()

def zadanie_3():
    print("задание3")
    i = Image.open('G:\lab\pichpn.jpg')
    name = input("Введите имя получателя - ")
    font = ImageFont.truetype("G:\lab/arial_bold.ttf", 35)
    d = ImageDraw.Draw(i)
    d.text((100, 100), name + ", поздравляю!", font=font, fill='blue')
    i.show()
    i.save(name + "_postcard.png")

zadanie_1(), zadanie_2(), zadanie_3()


