import requests 

# Extraction
api_url = "https://hugovk.github.io/top-pypi-packages/top-pypi-packages-30-days.min.json"
r = requests.get(api_url , auth=('Safiyya Asma', 'My First API usage'))\

print( r.status_code)

# data to dictionary object
raw_data = r.json()

# Transformation

package_list = []
package_downloads = []

for i in raw_data['rows']:
    package_downloads.append(i['download_count'])
    package_list.append(i['project'])

#Data Loading
f = open("package_data.csv", "w")
f.write("Package Name, Downloads\n")

for idx, package in enumerate(package_list):
    row = f"{package}, {package_downloads[idx]}\n"
    f.write(row)

f.close()