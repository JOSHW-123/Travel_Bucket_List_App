from db.run_sql import run_sql

from models.country import Country
from models.city import City

import repositories.country_repository as country_repository

        # self.name = name
        # self.geographical_area = geographical_area
        # self.population = population
        # self.language = language
        # self.currency = currency
        # self.id = id
        # self.visited = visited

def save(country):
    sql = "INSERT INTO countries (name, geographical_area, population, language, currency, visited) VALUES (%s,%s,%s,%s,%s,%s) RETURNING *"
    values = [country.name, country.geographical_area, country.population, country.language, country.currency, country.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country

# def select_all():
#     cities = []

#     sql = "SELECT * FROM cities"
#     results = run_sql(sql)

#     for row in results:
#         country = country_repository.select(row['country_id'])
#         city = City(row['name'], country, row['attractions'], row['temperature'], row['id'], row['visited'])
#         cities.append(city)
#     return cities

# def select(id):
#     city = None
#     sql = "SELECT * FROM cities WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]

#     if result is not None:
#         country = country_repository.select(result["id"])
#         city = City(result["name"], country, result["attractions"], result["temperature"], result["id"], result["visited"])
#     return city

# def delete_all():
#     sql = "DELETE FROM cities"
#     run_sql(sql)

# def delete(id):
#     sql = "DELETE FROM cities WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)

# def update(city):
#     sql = "UPDATE cities SET (name, attractions, temperature, country_id, visited) = (%s, %s, %s, %s, %s) WHERE id = %s"
#     values = [city.name, city.country, city.attractions, city.temperature, city.country.id, city.visited, city.id]
#     run_sql(sql, values)