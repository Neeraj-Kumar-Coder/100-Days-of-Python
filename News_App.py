import requests

API_KEY = "b6c492dd282d458e83fa9ece22361081"
categories = ["business", "entertainment", "general",
              "health", "science", "sports", "technology"]

countries = ["in", "us"]

print("Select the category you want the headlines for:")
for index, category in enumerate(categories):
    print(f"{index + 1}. {category}")

category_choice = input("Which category you choose (1-7): ")

if (not category_choice.isnumeric() or int(category_choice) < 1 or int(category_choice) > len(categories)):
    exit(
        f"Please enter a valid input between 1 and {len(categories)} (inclusive)")

category_choice = int(category_choice)
category_choice -= 1

for index, country in enumerate(countries):
    print(f"{index + 1}. {country}")

country_choice = input("Which country news you want to see: ")

if (not country_choice.isnumeric() or int(country_choice) < 1 or int(country_choice) > len(countries)):
    exit(
        f"Please enter a valid input between 1 and {len(countries)} (inclusive)")

country_choice = int(country_choice)
country_choice -= 1


URL = f"https://newsapi.org/v2/top-headlines?country={countries[country_choice]}&category={categories[category_choice]}&apiKey={API_KEY}"
response = requests.get(URL).json()

print(end="\n")
print(
    f" TOP HEADLINES FROM {categories[category_choice].upper()} OF {countries[country_choice].upper()} ".center(70, "*"))

articles = response["articles"]
for index, article in enumerate(articles):
    print(
        f"\n{index + 1}. {article['title']}\n->{article['description']}\n->Published at: {article['publishedAt']}")
