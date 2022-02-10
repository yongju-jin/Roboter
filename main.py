# This is a sample Python script.
from termcolor import colored, cprint
import csv

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

cache_file_name = "restaurant.csv"


def init_favorite_restaurant_name():
    with open(cache_file_name, "w", newline="") as f:
        fieldnames = ["NAME", "COUNT"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()


def get_exist_favorite_restaurants():
    favorite_restaurants = []
    with open(cache_file_name, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            favorite_restaurants.append(row['NAME'])
    return favorite_restaurants


def add_favorite_restaurant(restaurant):
    with open(cache_file_name, "r+", newline="") as f:
        fieldnames = ["NAME", "COUNT"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        reader = csv.DictReader(f)
        for row in reader:
            if restaurant == row['NAME']:
                row['COUNT'] = int(row['COUNT']) + 1
            writer.writerow(row)
        else:
            writer.writerow({'NAME': restaurant, 'COUNT': 1})


def process():
    init_favorite_restaurant_name()
    while True:
        cprint('안녕하세요 저는 Roboter 입니다. 당신의 이름은 무엇인가요?', "green")  # Press Ctrl+F8 to toggle the breakpoint.
        name = input()
        favorite_restaurants = get_exist_favorite_restaurants()
        for restaurant in favorite_restaurants:
            cprint(f"추천드리는 레스토랑은 {restaurant} 입니다.\n 이 레스토랑을 좋아하세요?[Yes/No]",
                   "green")  # Press Ctrl+F8 to toggle the breakpoint.
            take_recommend = input()
            if take_recommend == "Yes":
                add_favorite_restaurant(restaurant)
                break
        else:
            cprint(f"{name}씨, 좋아하는 레스토랑의 이름은 무엇인가요?", "green")  # Press Ctrl+F8 to toggle the breakpoint.
            favorite_restaurant_name = input()
            add_favorite_restaurant(favorite_restaurant_name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    process()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
