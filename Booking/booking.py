from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import Booking.constants as const
from lxml import etree
from datetime import datetime
from Booking.function import month_to_number
from Booking.booking_filtration import Booking_Filtration
from prettytable import PrettyTable,ALL

class Booking():
    
    def __init__(self):
        options = ChromeOptions()
        options.add_experimental_option("detach", True)
        service = webdriver.ChromeService(executable_path = '/usr/bin/chromedriver')
        self.options = options
        self.service =service
        super(Booking,self).__init__()
    
    def __enter__(self, teardown =False):
        driver = webdriver.Chrome(service=self.service, options = self.options)
        self.driver = driver
        self.teardown = teardown
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.teardown:
            self.driver.quit()
    
    def land_first_page(self):
        self.driver.get(const.Base_Url)
        sleep(5)
        
    
    def Shut_down_ad(self):
        self.driver.implicitly_wait(50)
        Shut_down_but = self.driver.find_elements(By.XPATH,'/html/body/div[21]/div/div/div/div[1]/div[1]/div/button')
        Shut_down_but[0].click()
        
    def Change_currency(self, currency):
        self.driver.implicitly_wait(50)
        currency_element = self.driver.find_element(By.CSS_SELECTOR, '#b2indexPage > div:nth-child(4) > div > div > header > nav.c20fd9b542 > div.c624d7469d.f034cf5568.dab7c5c6fa.c62ffa0b45.a3214e5942 > span:nth-child(1) > button')
        currency_element.click()
        page_source = BeautifulSoup(self.driver.page_source,'html.parser')
        dom = etree.HTML(str(page_source))
        try:
            for row in range(1,15):
                for column in range(1,5):
                    dom_1 = dom.xpath(f'/html/body/div[21]/div/div/div/div/div[2]/div/div[3]/div/div/div/ul[{row}]/li[{column}]/button/div/div[1]/span/div')
                    dom_2 = dom_1[0].text
                    if dom_2 == currency:
                        select_currency = self.driver.find_element(By.XPATH,f'/html/body/div[21]/div/div/div/div/div[2]/div/div[3]/div/div/div/ul[{row}]/li[{column}]/button')
                        select_currency.click()
                        sleep(2)
                        break
                    else:
                        continue
        except Exception as e:
            print(f"Erro {e}")
        
        
    def select_place(self, place):
        self.driver.implicitly_wait(50)
        search_field = self.driver.find_element(By.NAME, 'ss') 
        #search_field.clear()
        search_field.send_keys(place)
        sleep(2)
        
    def Select_Sdate_Edate(self, check_in_date, check_out_date):
        self.driver.implicitly_wait(50)
        # click the date but
        date_button = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/form/div[1]/div[2]/div/div/button[1]')
        date_button.click()
        
        current_date = datetime.now().date()
        
        # month and year to compare with user input if it greater click the next button on calendar
        date_compare = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/form/div[1]/div[2]/div/div[2]/div/nav/div[2]/div/div[1]/div/div[2]/h3')
        date_compare.text
    
        date_compare_year = date_compare.text.split()[1]
        date_compare_month = month_to_number(date_compare.text.split()[0])
        
        
        year_user_out = str(check_out_date).split("-")[0]
        month_user_out = str(check_out_date).split("-")[1]
        
        year_user_in = str(check_in_date).split("-")[0]
        month_user_in = str(check_in_date).split("-")[1]
        
        if check_in_date < str(current_date) or check_out_date < str(current_date):
            
            print("Error")
            
        elif check_in_date == str(current_date):
            self.driver.implicitly_wait(50)
            check_in_element = self.driver.find_element(By.CSS_SELECTOR,f'span[data-date="{check_in_date}"]')     
            check_in_element.click()
            if year_user_out == date_compare_year:
               
                if month_user_out <= date_compare_month:
                    self.driver.implicitly_wait(50)
                    check_out_element = self.driver.find_element(By.CSS_SELECTOR, f'span[data-date="{check_out_date}"]')
                    check_out_element.click()
                   
                    
                else:
                   
                    number_of_click = int(month_user_out) - int(date_compare_month)
                    if number_of_click == 1:
                        self.driver.implicitly_wait(50)
                        next_button = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/form/div[1]/div[2]/div/div[2]/div/nav/div[2]/div/div[1]/button')
                        next_button.click()
                        
                        check_out_element = self.driver.find_element(By.CSS_SELECTOR, f'span[data-date="{check_out_date}"]')
                        check_out_element.click()
                       
                    else:
                        self.driver.implicitly_wait(50)
                        next_button = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/form/div[1]/div[2]/div/div[2]/div/nav/div[2]/div/div[1]/button')
                        next_button.click()
                        
                        for _ in range(0, number_of_click-1):
                            self.driver.implicitly_wait(50)
                            next_button = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/form/div[1]/div[2]/div/div[2]/div/nav/div[2]/div/div[1]/button[2]')
                            next_button.click()
                        self.driver.implicitly_wait(50)   
                        check_out_element = self.driver.find_element(By.CSS_SELECTOR, f'span[data-date="{check_out_date}"]')
                        check_out_element.click()
                     
                        
                    
                    
                        
        else:
            if year_user_in == date_compare_year:
                if month_user_in <= date_compare_month:
                    self.driver.implicitly_wait(50)
                    check_in_element = self.driver.find_element(By.CSS_SELECTOR,f'span[data-date="{check_in_date}"]')
                    check_in_element.click()
                    
                    if year_user_out == date_compare_year:
                       
                        if month_user_out <= date_compare_month:
                            self.driver.implicitly_wait(50)
                            check_out_element = self.driver.find_element(By.CSS_SELECTOR, f'span[data-date="{check_out_date}"]')
                            check_out_element.click()
                           
                            
                        else:
                           
                            number_of_click = int(month_user_out) - int(date_compare_month)
                            if number_of_click == 1:
                                self.driver.implicitly_wait(50)
                                next_button = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/form/div[1]/div[2]/div/div[2]/div/nav/div[2]/div/div[1]/button')
                                next_button.click()
                                self.driver.implicitly_wait(50)
                                check_out_element = self.driver.find_element(By.CSS_SELECTOR, f'span[data-date="{check_out_date}"]')
                                check_out_element.click()
                              
                            else:
                                self.driver.implicitly_wait(50)
                                next_button = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/form/div[1]/div[2]/div/div[2]/div/nav/div[2]/div/div[1]/button')
                                next_button.click()
                                
                                for _ in range(0, number_of_click-1):
                                    self.driver.implicitly_wait(50)
                                    next_button = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/form/div[1]/div[2]/div/div[2]/div/nav/div[2]/div/div[1]/button[2]')
                                    next_button.click()
                                self.driver.implicitly_wait(50)  
                                check_out_element = self.driver.find_element(By.CSS_SELECTOR, f'span[data-date="{check_out_date}"]')
                                check_out_element.click()
                                
                else:
                    number_of_click = int(month_user_in) - int(date_compare_month)
                    
                    #--------------------------------------------------------------
                    # doan code nay de xu ly ngay check in, neu thang check in lon hon trong calendar thi bam nut di chuyen de sang cac thang sau
                    if number_of_click == 1:
                        self.driver.implicitly_wait(50)
                        next_button = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/form/div[1]/div[2]/div/div[2]/div/nav/div[2]/div/div[1]/button')
                        next_button.click()
                        check_in_element = self.driver.find_element(By.CSS_SELECTOR,f'span[data-date="{check_in_date}"]')
                        check_in_element.click()
                        
                        date_compare = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/form/div[1]/div[2]/div/div[2]/div/nav/div[2]/div/div[1]/div/div[2]/h3')
                        date_compare.text
                       
    
                        date_compare_year = date_compare.text.split()[1]
                        date_compare_month = month_to_number(date_compare.text.split()[0])
                        
                        if year_user_out == date_compare_year:
                           
                            if month_user_out <= date_compare_month:
                                self.driver.implicitly_wait(50)
                                check_out_element = self.driver.find_element(By.CSS_SELECTOR, f'span[data-date="{check_out_date}"]')
                                check_out_element.click()
                                
                                
                            else:
                               
                                number_of_click = int(month_user_out) - int(date_compare_month)
                                
                                for _ in range(0, number_of_click):
                                    self.driver.implicitly_wait(50)
                                    next_button = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/form/div[1]/div[2]/div/div[2]/div/nav/div[2]/div/div[1]/button[2]')
                                    next_button.click()
                                self.driver.implicitly_wait(50)   
                                check_out_element = self.driver.find_element(By.CSS_SELECTOR, f'span[data-date="{check_out_date}"]')
                                check_out_element.click()
                               
                        
                    else:
                        self.driver.implicitly_wait(50)
                        next_button = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/form/div[1]/div[2]/div/div[2]/div/nav/div[2]/div/div[1]/button')
                        next_button.click()
                        
                        for _ in range(0, number_of_click-1):
                            self.driver.implicitly_wait(50)
                            next_button = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/form/div[1]/div[2]/div/div[2]/div/nav/div[2]/div/div[1]/button[2]')
                            next_button.click()
                        self.driver.implicitly_wait(50)    
                        check_in_element = self.driver.find_element(By.CSS_SELECTOR,f'span[data-date="{check_in_date}"]')
                        check_in_element.click()
                        
                        date_compare = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/form/div[1]/div[2]/div/div[2]/div/nav/div[2]/div/div[1]/div/div[2]/h3')
                        date_compare.text
    
                        date_compare_year = date_compare.text.split()[1]
                        date_compare_month = month_to_number(date_compare.text.split()[0])
                        
                    #---------------------------------------------------------------------    
                    # doan code nay de xu ly ngay check out
                        if year_user_out == date_compare_year:
                            
                            if month_user_out <= date_compare_month:
                                self.driver.implicitly_wait(50)
                                check_out_element = self.driver.find_element(By.CSS_SELECTOR, f'span[data-date="{check_out_date}"]')
                                check_out_element.click()
                               
                                
                            else:
                                
                                number_of_click = int(month_user_out) - int(date_compare_month)
                                for _ in range(0, number_of_click):
                                    self.driver.implicitly_wait(50)
                                    next_button = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/form/div[1]/div[2]/div/div[2]/div/nav/div[2]/div/div[1]/button[2]')
                                    next_button.click()
                                self.driver.implicitly_wait(50)
                                check_out_element = self.driver.find_element(By.CSS_SELECTOR, f'span[data-date="{check_out_date}"]')
                                check_out_element.click()
                               
                    #---------------------------------------------------------- 
                        
            
    def select_number_of_people(self, people_number = None):
        self.driver.implicitly_wait(50)
        selection_element = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/form/div[1]/div[3]/div/button')
        selection_element.click()
            
        while True:
            decrease_adults_element = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/form/div[1]/div[3]/div/div/div/div/div[1]/div[2]/button[1]')
            decrease_adults_element.click()
            #If the value of adults reaches 1, then we should get out
            #of the while loop
            adults_value_element = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/form/div[1]/div[3]/div/div/div/div/div[1]/div[2]/span')

            

            if int(adults_value_element.text) == 1:
                break

        increase_button_element = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/form/div[1]/div[3]/div/div/div/div/div[1]/div[2]/button[2]')

        for _ in range(people_number - 1):
            increase_button_element.click()
        
    def click_search(self):
        self.driver.implicitly_wait(50)
        search_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/form/div[1]/div[4]/button')
        search_button.click()
        sleep(5)
        
    def apply_filtration(self):
        filtration = Booking_Filtration(driver = self.driver)
        filtration.apply_star_rating(2,4,5)
        sleep(5)
        filtration.sort_price_lowest_first()
        sleep(3)
        
    def report_result(self):
        
        collection = []
      
        hotel_title = self.driver.find_elements(By.CSS_SELECTOR, '[data-testid="title"]')
        for i in range(len(hotel_title)):
            
            hotel_price = self.driver.find_elements(By.CSS_SELECTOR,'[data-testid="price-and-discounted-price"]')
            
            hotel_score = self.driver.find_elements(By.CSS_SELECTOR,'[data-testid="review-score"]')
            try:
                hotel_score_eddit = hotel_score[i].text
            except:
                hotel_score_eddit = None
                
            collection.append([hotel_title[i].text,hotel_price[i].text,hotel_score_eddit])
            
        table = PrettyTable(field_names = ['Hotel Name','Hotel Price', "Hotel "])
        table.add_rows(collection)
        table.hrules =ALL
        print(table)