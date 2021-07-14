from db.run_sql import run_sql

from models.country import Country
from models.city import City

import repositories.country_repository as country_repository

# def cities(country):
#     cities = []

#     sql = "SELECT * FROM cities WHERE country_id = %s"
#     values = [country.id]
#     results = run_sql(sql, values)

#     for row in results:
#         city = City(row["name"], row["country"], row["attractions"], row["temperature"], row["id"], row["visited"])
#         cities.append(city)
#     return cities

    # self.name = name
    #     self.country = country
    #     self.attractions = attractions
    #     self.temperature = temperature
    #     self.id = id
    #     self.visited = visited

def save(country):
    sql = "INSERT INTO countries (name, geographical_area, population, language, currency, visited) VALUES (%s,%s,%s,%s,%s,%s) RETURNING *"
    values = [country.name, country.geographical_area, country.population, country.language, country.currency, country.visited]
    results = run_sql(sql, values)
    id = results[0]["id"]
    country.id = id
    return country

def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row["name"], row["geographical_area"], row["population"], row["language"], row["currency"], row["visited"], row["id"])
        countries.append(country)
    return countries

def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = Country(result["name"], result["geographical_area"], result["population"], result["language"], result["currency"],  result["visited"], result["id"])

    return country

def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(country):
    sql = "UPDATE countries SET (name, geographical_area, population, language, currency, visited) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [country.name, country.geographical_area, country.population, country.language, country.currency, country.visited, country.id]
    print(values)
    run_sql(sql, values)


    # self.name = name
        # self.geographical_area = geographical_area
        # self.population = population
        # self.language = language
        # self.currency = currency
        # self.id = id
        # self.visited = visited