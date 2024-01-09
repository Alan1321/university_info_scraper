from scrape import scrape_all
from constants import BASE_URL, course_abbreviations
from process_data import process_data

for course in course_abbreviations:
    complete_url = f"{BASE_URL}{course}"
    print(f'\nComplete URL: {complete_url}')

    #scrape the data from webpage
    data = scrape_all(complete_url, course)

    #process data
    processed_data = process_data(data, '1.0').get_result()

    for result in processed_data:
        print(result)
