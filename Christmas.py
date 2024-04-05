import pygame
from random import randint
#მიქსერის შემოტანა
from pygame import mixer

#ფაიგეიმის ინიციაცია
pygame.init()
clock = pygame.time.Clock()
fps = 30


#მიქსერის ინიციაცია
mixer.init()
#მუსიკის ატვირთვა
mixer.music.load("background.mp3")
#მუსიკის დაკვრა (ლუფით)
mixer.music.play(-1)
#ხმის დაწევა
mixer.music.set_volume(0.5)

#ეკრანის ზომები
width = 800
height = 600
#ეკრანის შექმნა
screen = pygame.display.set_mode((width, height))



#საჭირო სურათების ატვირთვა, ზომის ცვლილება და ფერების განსაზღვრა
icon = pygame.image.load("animation1.png")

background = pygame.image.load("background.jpg")
#ფონის სურათის ზომის შეცვლა
background = pygame.transform.scale(background, (width, height))

snow_image = pygame.image.load("snowflake.png")
snow_image = pygame.transform.scale(snow_image, (50, 50))

#ანიმაციის სურათების სახელების სია
animation_image_names = ["animation1.png", "animation2.png"]
#ანიმაციის სურათების სია
animation_images = []
for name in animation_image_names:
    #ანიმაციის სურათების სახელის მიხედვით ატვირთვა
    load_animation = pygame.image.load(name)
    #სასურველი ზომის მინიჭება
    scaled_animation = pygame.transform.scale(load_animation, (200, 200))
    #ანიმაციის სურათების სიაში დამატება
    animation_images.append(scaled_animation)

red = (255, 50, 50)
yellow = (255, 255, 50)
color = yellow
#ფონტის შემოტანა წარწერისთვის
font = pygame.font.Font("font.ttf", 120)

#ფანჯარაზე წარწერის ცვლილება
pygame.display.set_caption("Merry Christmas")

#ფანჯარაზე სურათის შეცვლა
pygame.display.set_icon(icon)


#ფიფქის კლასი
class SnowFlake(pygame.sprite.Sprite):
    def __init__(self, image, h, v):
        super().__init__()
        #ფიფქის სურათის შენახვა
        self.image = image
        #ფიფქის სურათის ზომის მართკუთხედის შექმნა
        self.rect = self.image.get_rect()
        #მართკუთხედის ცენტრის შემთხვევით ლოკაციაზე განთავსება
        self.rect.center = [randint(-1000, width + 1000), randint(-500, -25)]

        self.speed_h = h
        self.speed_v = v

    def update(self):
        #ფიფქის ვერტიკალური და ჰორიზონტალური მოძრაობა
        self.rect.y += self.speed_v
        self.rect.x += self.speed_h
        #ფიფქის განადგურება როდესაც ეკრანს გაცდება
        if self.rect.y > height or self.rect.y < -1000:
            self.kill()



#მთავარი ანიმაციის კლასი
class ChristmasAnimation:
    def __init__(self, images_list, loc_x, loc_y):
        #ანიმაციის სიის გადაცემა
        self.images = images_list
        #ანიმაციის პირველი სურათის შენახვა
        self.image = images_list[0]
        #შენახული სურათის ზომის მართკუთხედის შექმნა
        self.rect = self.image.get_rect()
        #მართკუთხედის ცენტრის კონკრეტულ ლოკაციაზე განთავსება
        self.rect.center = [loc_x, loc_y]
        self.i = 0

    #სურათის დახატვის ფუნქცია
    def draw(self):
        global counter
        #ეკრანზე სურათის დახატვა
        screen.blit(self.image, self.rect)
        #სურათის დროგამოშვებით ცვლილება
        if counter == 0:
            print(self.i)
            if self.i < len(self.images) - 1:
                self.i += 1
            else:
                self.i = 0
            #სურათის ცვლილება
            self.image = self.images[self.i]




# ობიექტის შექმნა მთავარი კლასისგან
anime = ChristmasAnimation(animation_images, width/2, height/2)

#ფიფქებისთვის ჯგუფის შექმნა
snow_group = pygame.sprite.Group()

#მთვლელის მიხედვით თოვლის ფიფქების ავტომატური გენერირების ფუნქცია (მინიმალურ და მაქსიმალურ ფიფქების რაოდენობას ვაწვდით)
counter = 0
def create_snow(mn, mx):
    if counter == 0:
        for _ in range(randint(mn, mx)):
            #ახალი ფიფქის შექმნა
            flake = SnowFlake(snow_image, 15, 30)
            #ახალი ფიფქის ფიფქების ჯგუფში ჩამატება
            snow_group.add(flake)

    #ფიფქების ჯგუფის დახატვა და განახლება
    snow_group.draw(screen)
    snow_group.update()


#მესიჯის გამოტანის ფუნქცია
def message(color, font):
    #ტექსტის ფონტის მეშვეობით დარენდერება
    rendered_text = font.render("Happy New Year!", False, color)
    #ტექსტისთვის მართკუთხედის შექმნა
    text_rect = rendered_text.get_rect()
    #მართკუთხედის ცენტრის ლოკაციის შერჩევა
    text_rect.center = [width/2, 150]
    #წარწერის ეკრანზე გამოტანა
    screen.blit(rendered_text, text_rect)

#მთავარი ციკლის შექმნა
run = True
while run:
    #ციკლის სიჩქარის დარეგულირება
    clock.tick(fps)
    #მთვლელის კონტროლი (15 იტერაცია _ ნახევარი წამია, რადგან fps 30ია მითითებული, ანუ კოდი წამში 30ჯერ ეშვება)
    counter += 1
    #ყოველ ნახევარ წამში მთვლელი ისევ ნულს უტოლდება და წარწერის ფერი ამ დროს იცვლება
    if counter > 15:
        counter = 0
        if color == red:
            color = yellow
        else:
            color = red


    #ფონის ფერის ჩასხმა
    # screen.fill(red)
    #ფონის სურათის დადება
    screen.blit(background, (0, 0))
    #მესიჯის გამოტანის ფუნქციის გამოძახება
    message(color, font)
    #ობიექტის დახატვა
    anime.draw()
    #თოვლის შექმნის ფუნქციის გამოძახება
    create_snow(10, 30)
    #კოდის გათიშვა
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #ეკრანის განახლება
    pygame.display.update()