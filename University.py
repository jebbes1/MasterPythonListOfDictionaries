universities = [
    {"University name": "University of Demacia", "Location": "123 Academy Lane, Demacia City, Valoran, 45678", "Established": "2009", "Number of students": 15000, "University Type": "Private"},
    {"University name": "University of Noxus", "Location": "456 Conqueror's Way, Noxus City, Runeterra, 12345", "Established": "2005", "Number of students": 18000, "University Type": "Private"},
    {"University name": "University of Ionia", "Location": "789 Harmony Path, Ionia Village, Runeterra, 67890", "Established": "2007", "Number of students": 12000, "University Type": "Public"},
    {"University name": "University of Targon", "Location": " 321 Celestial Way, Targon Peaks, Runeterra, 13579", "Established": "2002", "Number of students": 21000, "University Type": "Private"},
    {"University name": "University of Shurima", "Location": "987 Sun Disk Road, Shurima Desert, Runeterra, 24680, Runeterra, 13579", "Established": "2002", "Number of students": 9500, "University Type": "Private"},
]

for university in universities:
    print(f"University Name: {university["University name"]} | Location: {university["Location"]} | Established: {university["Established"]} | Number of students: {university["Number of students"]} | University Type: {university["University Type"]}")
