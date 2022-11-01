from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrapemars

app = Flask(__name__)


mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def home():
    
    scrp = mongo.db.scrp.find_one()
    if scrp:
        return render_template("index.html", scrp = scrp)
    else:
        #return "<html> <head> <body> <h1> No data found! Please run IP + '/scrape' </h1> </body> </head> </html>"
        return redirect("/scrape") 


@app.route("/scrape")
def scraper():
    scrp_db= mongo.db.scrp
    scrp_scrape = scrapemars.scrape()
    print(f'My data is: \n {scrp_scrape}')

    scrp_db.update_many({},{"$set":scrp_scrape},upsert=True)
   
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)



