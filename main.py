# This is a sample Python script.
from termcolor import colored, cprint
import csv

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

recommend_restaurant_name = ""
cache_file_name = "restaurant.csv"


def print_ask_name():
    cprint('안녕하세요 저는 Roboter 입니다. 당신의 이름은 무엇인가요?', "green")  # Press Ctrl+F8 to toggle the breakpoint.


def input_name():
    return input()


def check_is_exist_recommend_restaurant():
    with open(cache_file_name, "r") as f:
        f.readline()


def print_ask_favorite_restaurant(name):
    cprint(f"{name}씨, 좋아하는 레스토랑의 이름은 무엇인가요?", "green")  # Press Ctrl+F8 to toggle the breakpoint.


def input_favorite_restaurant():
    favorite_restaurant_name = input()
    with open(cache_file_name, "w+", newline="") as f:
        fieldnames = ["NAME", "COUNT"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'NAME': favorite_restaurant_name, 'COUNT': 1})
    return favorite_restaurant_name


def print_ask_recommend_restaurant():
    pass


def input_recommend_restaurant():
    pass


def process():
    while True:
        print_ask_name()
        name = input_name()
        print_ask_favorite_restaurant(name)
        input_favorite_restaurant()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    process()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
