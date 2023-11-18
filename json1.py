import json
from pygal.i18n import COUNTRIES

filename = 'population.json'
with open(filename) as f:
    pop_data = json.load(f)

# get population value for a specific year entered by the user
user_year = input('Please enter year: \n')
user_year_found = False

for pop_dict in pop_data:
    try:
        if pop_dict['Year'] == user_year:
            country_name = pop_dict['Country Name']
            country_code = pop_dict['Country Code']
            year = pop_dict['Year']
            population = int(float(pop_dict['Value']))

            print(f"""\n
            Country: {country_name}
            Population: {population:,}
            Country Code: {country_code}
            Year: {year}""")

            user_year_found = True  # Mark that the year was found
    except (KeyError, TypeError, ValueError):
        pass

# Print a message if the year was not found
if not user_year_found:
    print(f'{user_year} details are not available yet. Try another year.')
