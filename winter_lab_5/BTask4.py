import urllib


zip_code = input("Enter zip code: ")
url = "http://www.uszip.com/zip/"
conn = urllib.urlopen(url +  str(zip_code))
town_match_pattern = "<h2><strong>"
population_match_pattern = "<dt>Total population</dt><dd>"


town_name = ""
for line in conn:
    town_index_start = line.find(town_match_pattern)
    if town_index_start != -1:
        line_words = line.split("strong>")
        town_name = line_words[1]
        print(town_name)
    elif line.find(population_match_pattern) != -1:
        print(line.split(population_match_pattern)[1])

