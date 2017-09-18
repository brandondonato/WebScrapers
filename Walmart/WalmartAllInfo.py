import urllib
from urllib import urlopen
import string
from bs4 import BeautifulSoup
import os.path
import datetime
groceries='''applesauce
almond joy
apple cider vinegar
apple juice
baking soda
bagged popcorn
ham (cold cuts)
turkey (cold cuts)
almond milk
apples
artichoke
arugula
asparagus
avocado
bagels (Thomas' Bagels plain)
banana
barbecue sauce
beets
berries
black beans
Black beans (canned)
black olives
black pepper
black tea (tea bags)
brown rice
brown sugar 
brownie mix
cake mix
canned corn
canned pineapple
Canned tuna
canned/jarred mushrooms
canola oil
carrots
cashews
cheerios
Cheez-it
cherries
chicken breast
chicken broth
chicken noodle soup
chickpeas/garbanzo beans
chocolate chips
chocolate syrup
coconut flakes
coconut oil
coffee beans
coffee creamer
coke 
condensed milk
cooking spray
corn
cranberry juice
crunchy taco shells
crushed red pepper
cucumber
distilled white vinegar
Entenmann's Donuts Pop'ems Glazed Donut Holes
extra virgin olive oil
fig newtons
flour (all-purpose)
flour tortillas
frosted flakes
frosting
frozen berries
frozen fish
frozen pizza
frozen soup
frozen waffles
fruit snacks
fruity pebbles
garlic powder
gatorade
ginger ale
graham crackers
granola bars
grapefruit
grapes
greek yogurt (chobani)
green tea (tea bags)
ground beef
ground cinnamon 
ground coffee
gummy bears
Hershely's milk chocolate bar
honey
honey bunches of oats
hot sauce
hummus 
ice cream
iceberg lettuce 
iced tea powder
instant coffee
Instant noodles (ramen) 
Jelly/jam
k-cups
kale
ketchup
Lay's chips
lemons
lime
M&M's
Macaroni & Cheese
mango
maple syrup
marinara sauce
marshmallow
mayonnaise
meat sauce
mustard
nutella
oatmeal
olive oil spray
olives
orange
oreos
pancake mix
peaches
peanut butter
peanuts
pears
penne pasta
pepsi
pickles
pie crust
pinto beans
pistachios
pita 
plums
popcorn kernals
pretzels
Pringles
pudding
quinoa
raisin bran
raisins
ranch dressing
Ravioli
reese's puffs
relish
rice cakes
Rice Krispies Treats
ritz crackers
romaine lettuce
Rotini pasta
salt
sardines
sea salt
Skittles
sliced peaches
smoked paprika
soy sauce
Spaghetti
sparkling water/seltzer/club soda
spinach
steak sauce
stevia
sugar (white pure-cane)
sweet peas
thousand island dressing
tofu
tomato
tomato paste
tomato soup
trail mix
trident gum
vegetable oil
vodka sauce
walnuts
water bottles
watermelon
white rice
wrigley gum
yogurt (Yoplait)
coffee filters
food storage bags
laundry detergent
mouth wash
razor blade refills 
toothpaste'''
#create list from input string
groceryList=string.split(groceries, "\n")
time = datetime.datetime.now()
currentMonth = str(time.month)
currentDay = str(time.day)
currentYear = str(time.year)
currentHour = str(time.hour)
currentMinute = str(time.minute)
with open("walmart.txt", "a") as myfile:
    myfile.write("Today's date is: "+currentMonth+"/"+currentDay+\
        "/"+currentYear+"\t"+"The time is: "+currentHour+":"+currentMinute+"\n\n\n\n")
    myfile.close()
for item in groceryList:
    print (item)
    #open the webpage on walmart website
    content=urlopen("http://www.walmart.com/search/?query="+item)
    #feed html code into beautiful soup module
    sourceCode=BeautifulSoup(content.read(),"html.parser")
    #this next line makes sure your computer doesnt crash because Eytan wants to go shopping for 200 items at the same time
    content.close()
    #try:
    temp=sourceCode.find_all("a",{"class":"js-product-title"})
    for sale in temp:
        try:
            product=sale.get_text()
            price=sale.parent.next_sibling.next_sibling.div.get_text()
            if 'In stores only' in sale.parent.next_sibling.next_sibling.div.get_text():
                break
            with open("walmart.txt", "a") as myfile:
                myfile.write(product.encode('utf-8')+'\t'+ price.encode('utf-8') + '\n')
                continue
        except TypeError:
            with open("walmart.txt", "a") as myfile:
                myfile.write(item+'\t'+'Item not there'+'\n')
                continue
        except AttributeError:
            with open("walmart.txt", "a") as myfile:
                myfile.write(item+'\t'+'Item not there'+'\n')
                continue
with open("walmart.txt", "a") as myfile:
    myfile.write("\n\n")
    myfile.close()
#   #price=string.replace(temp2,"\xa2","cents")

#include what to do if there is a space in the url you are trying to hit