
from Booking.booking import Booking
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

with Booking() as bot:
    
    try:
        bot.land_first_page()
        bot.Shut_down_ad()
        bot.Change_currency(currency='AUD')
        bot.select_place("ThaiLan")
        #bot.select_place(input("Where you want to go ?"))
        # bot.Select_Sdate_Edate(check_in_date=input("What is the check in date ?"),
        #                     check_out_date=input("What is the check out date ?"))
        
        bot.Select_Sdate_Edate('2024-05-23','2024-05-29')
        #bot.select_number_of_people(int(input("How many people ?")))
        bot.select_number_of_people(5)
        bot.click_search()
        bot.apply_filtration()
        bot.report_result()
    except Exception as e:
        raise