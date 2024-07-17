from datetime import date, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

bus_routes_name = []
bus_route_link = []
bus_names = []
bus_type = []
departing_time = []
duration = []
reaching_time = []
star_rating = []
price = []
seat_availablity = []

count = 0

def scroll_to_bottom(driver):
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(2)  # Adjust this value based on your specific page loading time

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

driver.get('https://www.redbus.in/')
govt_bus = driver.find_elements(By.XPATH,"(//div[@class='rtcName'])") #minimum of 10 state buses
for i in range(1,11):
    scroll_button = driver.find_element(By.XPATH,"//div[@class ='scrollTopButton']")
    driver.execute_script("arguments[0].click()",scroll_button)

    g_bus = driver.find_element(By.XPATH,"(//div[@class='rtcName'])"+"["+str(i)+"]")
    driver.execute_script("arguments[0].click()",g_bus)
    # route name
    route_name = driver.find_elements(By.XPATH,"(//div[@class='route_details']/a)")
    pagination  = driver.find_elements(By.XPATH,"//div[@class='DC_117_paginationTable']/div")
   
    for r in range(len(pagination)):
       for j in range(1,11):

            try:
                page = driver.find_element(By.XPATH,"//div[@class='DC_117_paginationTable']/div"+"["+str(r+1)+"]")
                driver.execute_script("arguments[0].click()",page)
            except NoSuchElementException as e:
                print(f"Element not found - Pagination")

            try:
                element = driver.find_element(By.XPATH,"(//div[@class='route_details']/a)"+"["+str(j)+"]")
                route_txt = element.text
                href_value = element.get_attribute("href")
                driver.execute_script("arguments[0].click()",element)

            except NoSuchElementException as e:
                print(f"Element not found - routelink ")
                break

            try:
                gov_bus = driver.find_element(By.XPATH,"(//div[@class='button'])[1]")
                gov_bus.click()
            except NoSuchElementException as e:
                print(f"Element not found - 1st bus button ")

            try:
                scroll_to_bottom(driver)

                # bus name
                bus_name = driver.find_elements(By.XPATH,"(//div[@class='travels lh-24 f-bold d-color'])")
                count += len(bus_name)
                # bus type
                bus_seat_type = driver.find_elements(By.XPATH,"//div[@class='bus-type f-12 m-top-16 l-color evBus']")

                # departure time
                starting_time = driver.find_elements(By.XPATH,"//div[@class='column-three p-right-10 w-10 fl']")

                # total time
                total_time = driver.find_elements(By.XPATH,"//div[@class='dur l-color lh-24']")

                # reaching time
                arriving_time = driver.find_elements(By.XPATH,"//div[@class='column-five p-right-10 w-10 fl']")

                #rating
                rating = driver.find_elements(By.XPATH,"//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")

                # price
                cost = driver.find_elements(By.XPATH,"//div[@class='fare d-block']/span")

                # seat availablity
                seat_available = driver.find_elements(By.XPATH,"//div[@class='column-eight w-15 fl']/div[1]")

                for i in bus_name:
                    bus_names.append(i.text)

                for i in bus_seat_type:
                    bus_type.append(i.text)

                current_date = date.today()
                for i in starting_time:
                   starting_text = i.text.split('\n')[0]
                   if "Next day" in i.text:
                       departing_time.append((current_date + timedelta(days=1)).strftime('%Y-%m-%d') + " " + starting_text + ":00")
                   else:
                       departing_time.append(current_date.strftime('%Y-%m-%d') + " " + starting_text + ":00")

                for i in total_time:
                    duration.append(i.text)

                for i in arriving_time:
                   reaching_text = i.text.split('\n')[0]
                   try:
                          next_day = driver.find_element(By.XPATH, "//div[@class='next-day-dp-lbl m-top-16']")
                          if next_day.text in i.text:
                              reaching_time.append((current_date + timedelta(days=1)).strftime('%Y-%m-%d') + " " + reaching_text + ":00")
                          else:
                               reaching_time.append(current_date.strftime('%Y-%m-%d') + " " + reaching_text + ":00")

                   except NoSuchElementException:
                        reaching_time.append(current_date.strftime('%Y-%m-%d') + " " + reaching_text + ":00")

                for i in rating:
                    x = i.text
                    x = x.split('\n')[0]
                    if x == ' ':
                        star_rating.append(float(0))
                    elif x == "New":
                        star_rating.append(float(0))
                    else:
                        star_rating.append(float(x))

                for i in cost:
                    price.append(float(i.text))

                for i in seat_available:
                    i = i.text
                    i = i.split(' ')[0]
                    seat_availablity.append(int(i))

                if route_txt and href_value:
                    route_txt = [route_txt] * count
                    bus_routes_name.extend(route_txt)
                    href_value = [href_value] * count
                    bus_route_link.extend(href_value)

                count = 0

                driver.back()
                modify_button = driver.find_element(By.XPATH,"//div[@class='onward-modify-btn g-button clearfix fl']")

                if modify_button.is_displayed():
                    driver.back()

            except NoSuchElementException as e:
                print(f"Element not found - All ")
    driver.back()
