travel_log = {
  "Africa": 
  {
    "cities_visited": ["Kinshasa", "Abidjan", "Dakar", "Johannesbourg", "Douala", "Zanzibar"], 
  "citiesTo_visit": ["Brazza", "Kigali", "Cap Town"],
  "time": 17
  },

  "Europe": 
  {
    "cities_visited": ["Lille", "Paris", "Rome", "Bruxelles", "Berlin"], 
  "citiesTo_visit": ["Lyon", "Viennes", "Luxembourg", "Liege"] },
  "time": 15,

  "Asie": 
  {
    "cities_visited": ["Tokyo", "Seoul", "Shanghai"],
  "citiesTo_visit": ["Dubai", "New Delhi", "Bombay"],
  "time": 12  
  },
  "Oceanie":
  {
    "cities_visited": ["Wellington", "Sidney","Canberra"],
    "citiesTo_visit": ["Adelaide", "Suva", "Melbourne", "Papeete"],
    "time": 7
  }

}

print(travel_log)

# fuction to add more countries into the dictionary

def add_new_visit(cities_visited, citiesTo_visit, time):
  new_travel = {}
  new_travel["city"] = cities_visited
  new_travel["toVisit"] = citiesTo_visit
  new_travel["number"] = time
  travel_log.append(new_travel)


add_new_visit(["Moscou","Roma","London"], ["Venise", "Strasbourg"], 6)

print(travel_log)