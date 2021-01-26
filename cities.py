travel_time = [
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
{
  "country": "Congo RD",
  "visits": 9,
  "cities": ["Kinshasa", "Boma", "Matadi", "Goma", "Lomami", "Mbandaka"]
},

]

def adding_new_cities(name, visit_count, visited):
  new_travel = {}
  new_travel["country"] = name
  new_travel["visit_count"] = visit_count
  new_travel["visited"] = visited
  travel_time.append(new_travel)

adding_new_cities("South Africa", 4, ["Durban", "Cap Town", "Johannesbourg", "Sun Cities"])

print(adding_new_cities)