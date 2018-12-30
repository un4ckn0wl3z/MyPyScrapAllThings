from selenium import webdriver
from selenium.webdriver.firefox.options import Options



def get_upcoming_events(url):
    options = Options()
    options.set_headless(True)
    driver = webdriver.Firefox(options=options)
    driver.get(url)

    events = driver.find_elements_by_xpath('//ul[contains(@class, "list-recent-events")]/li')

    for event in events:
        event_details = dict()
        event_details['name'] = event.find_element_by_xpath('h3[@class="event-title"]/a').text
        event_details['location'] = event.find_element_by_xpath('p/span[@class="event-location"]').text
        event_details['time'] = event.find_element_by_xpath('p/time').text
        print(event_details)

    driver.close()

get_upcoming_events('https://www.python.org/events/python-events/')
