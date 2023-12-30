from datetime import date
from rcci_playground.scraper.scraper import scrape
from rcci_playground.modeller.modeller import model

def main():
    print('rcci_playground main')
    price = scrape()
    today = date.today()
    model(price=price, date=today)
    pass

if __name__ == "__main__":
    main()
