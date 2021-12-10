travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


def add_new_country(country_name, visit_number, city_name):
    new_entry = {"country": country_name, "visits": visit_number, "cities": city_name}
    travel_log.append(new_entry)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
