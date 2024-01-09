from scrape import scrape_all
from constants import BASE_URL, course_abbreviations, credit_hour
from process_data import process_data

for course in course_abbreviations:
    complete_url = BASE_URL.replace("NDX", f"{course}")
    print(f'\nComplete URL: {complete_url}')

    #scrape the data from webpage
    data = scrape_all(complete_url, course)

    #process data
    processed_data = process_data(data, credit_hour).get_result()

    for result in processed_data:
        print(result)
