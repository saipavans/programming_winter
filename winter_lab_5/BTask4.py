import urllib3


#zip_code = input("Enter zip code: ")
zip_code = "02492"
http = urllib3.PoolManager()
url = "http://www.uszip.com/zip/"
result = http.request("GET", url +  str(zip_code))
data_str = str(result.data)
filtered_data = data_str.split("is the zip code for")[1].split("strong")[1].split(" ")[0]

print("TOWN NAME:",filtered_data[1:-1])