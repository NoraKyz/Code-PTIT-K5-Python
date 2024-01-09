import print_functions as pf

# 7.1
def display_message():
    print("I am learning about functions in Python.")

display_message()

# 7.2
def favourite_book(title):
    print("One of my favourite books is " + title + ".")

favourite_book("Alice in Wonderland")

# 7.3
def make_shirt(size, message):
    print(f"Size: {size}\nMessage: {message}")

make_shirt("M", "Hello World!")
make_shirt(message="Hello World!", size="M")

# 7.4
def make_shirt(size = "L", message = "I love Python"):
    print(f"Size: {size}\nMessage: {message}")

make_shirt()
make_shirt("M")
make_shirt("M", "Hello World!")

# 7.5
def description_city(city, country = "Viet Nam"):
    print(city + " is in " + country)

description_city("Ha Noi")
description_city("Ho Chi Minh")
description_city("LonDon", "England")

# 7.6
def city_name(city, country):
    return city + ", " + country

print(city_name("Ha Noi", "Viet Nam"))
print(city_name("Ho Chi Minh", "Viet Nam"))
print(city_name("LonDon", "England"))

# 7.7
def make_album(artist, title, number_of_songs = None):
    album = {
        "artist": artist,
        "title": title
    }
    if number_of_songs:
        album["number_of_songs"] = number_of_songs
    return album

print(make_album("Taylor Swift", "Red"))
print(make_album("Jack", "5 cu"))
print(make_album("Son Tung", "Lac Troi"))
print(make_album("Taylor Swift", "Red", 16))

# 7.9
messages = [
    "Hello",
    "How are you?",
    "Bye"
]
def show_messages(messages):
    for message in messages:
        print(message)

show_messages(messages)

# 7.10
sent_messages = []
def send_message(message):
    show_messages([message]) 
    sent_messages.append(message)

send_message("Long")
for message in sent_messages:
    print(message)

# 7.11
def send_messages(messages):
    for message in messages:
        send_message(message)

send_message(messages)
for message in sent_messages:
    print(message)

# 7.12
def sandwich(*items):
    print("You ordered a sandwich with:")
    for item in items:
        print("- " + item)

sandwich("beef", "cheese", "tomato")
sandwich("beef", "cheese")
sandwich("beef")

# 7.13
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Le Quy', 'Long', location='HaNoi',field='physics')
print(user_profile)

# 7.14
def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

# 7.15
# In printing_models.py

# 7.16
import funtions
from funtions import isPrime
from funtions import isPrime as ip
import funtions as f
from funtions import *

