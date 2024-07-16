import requests

def fetch_covid_data(region):
  API_URL = f"https://disease.sh/v3/covid-19/countries/{region}"
  response = make_api_call(API_URL)

  if response.status_code == 200:
      return response.json()
  else:
      return f"Error fetching data: {response.status_code}"

def make_api_call(url):
  headers = {"Accept": "application/json"}
  return requests.get(url, headers=headers)

def display_statistics(data):
  print(f"COVID-19 Statistics for {data['country']}:")
  print(f"Total Cases: {data['cases']}")
  print(f"Total Recoveries: {data['recovered']}")
  print(f"Total Deaths: {data['deaths']}")

def main():
  region = input("Enter the region (country, state, or city): ")
  covid_data = fetch_covid_data(region)

  if isinstance(covid_data, dict):
      display_statistics(covid_data)
  else:
      print(covid_data)

if __name__ == "__main__":
  main()