from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrapemars

app = Flask(__name__)


mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
@app.route("/")
def home():

    scraped = mongo.db.Scraping.find_one()

    return render_template("index.html", scrp = scraped)

@app.route("/scrape")
def scraper():
    
    scraped_data = scrapemars.scrape()
    mongo.db.Scraping.update_many({},{"$set":scraped_data},upsert=True)
   
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)



