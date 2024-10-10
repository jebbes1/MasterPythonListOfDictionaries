restaurants = [
    {"Restaurant name": "Sands of Flavor", "Cuisine Type": "Middle Eastern", "Location": "789 Oasis Drive, Shurima Desert, Runeterra", "Restaurant Owner": "Omah D. Azir", "Average Price Range": "$15-35 per person"},
    {"Restaurant name": "The Iron Fork", "Cuisine Type": "Rustic European", "Location": "456 Warpath Lane, Noxus City, Runeterra", "Restaurant Owner": "Dar D. Ius", "Average Price Range": "$20-$50 per person"},
    {"Restaurant name": "Valor's Bounty", "Cuisine Type": "Traditional American", "Location": "123 Honor Road, Demacia City, Runeterra", "Restaurant Owner": "Garen D. Crownguard", "Average Price Range": "$10-$25 per person"},
    {"Restaurant name": "Serenity Garden", "Cuisine Type": "Asian Fusion", "Location": "234 Tranquil Path, Ionia Village, Runeterra", "Restaurant Owner": "Karma I. Ionian", "Average Price Range": "$12-$30 per person"},
    {"Restaurant name": "Celestial Cuisine", "Cuisine Type": "Mediterranean", "Location": "321 Starfall Avenue, Targon Peaks, Runeterra", "Restaurant Owner": "Tar G. On", "Average Price Range": "$18-$40 per person"}
]

for restaurant in restaurants:
    print(f"Restaurant Name: {restaurant["Restaurant name"]} | Cuisine Type: {restaurant["Cuisine Type"]} | Location: {restaurant["Location"]} | Restaurant Owner: {restaurant["Restaurant Owner"]} | Average Price Range: {restaurant["Average Price Range"]}")