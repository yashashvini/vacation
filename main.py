__author__ = 'hemalatha_ganireddy'
from flask import Flask
app = Flask(__name__)
import os.path
import sys
import json
import datetime
from flask_cors import CORS, cross_origin
cors = CORS(app, resources={r"/": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
# try:
#     import apiai
# except ImportError:
#     sys.path.append(
#         os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
#     )
#     import apiai
# # CLIENT_ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
# client_access_token = '8bd3b6024a8e461f8e4e63c181882295'


@app.route("/")
def basic(data):
    long_weekends = {"Independence Day": "TUESDAY, JULY,2017",
    "LABOR DAY":"MONDAY, SEPTEMBER 4, 2017 ",
    "COLUMBUS DAY":"MONDAY, OCTOBER 9, 2017",
    "VETERANS DAY":"FRIDAY, NOVEMBER 10, 2017",
    "THANKSGIVING DAY":"THURSDAY, NOVEMBER 23, 2017",
    "MONDAY, DECEMBER 25, 2017":"CHRISTMAS DAY"}
    vacations_by_month = {"January": ["Caribbean","Australia","Shetland Islands","Scotland","Northern lights in Norway",
                                     "Mexico (Puerto Escondido for something lively, Mazunte, San Agustinillo and Zipolite for something a little quieter)"," Brazil",
                                     " Ethiopia", "Scotland", "Norway", "France", "Switzerland", "Austria", "The West Indies and the Caribbean", "the Dominican Republic", "South Africa"],
                          "February": ["Buenos Aires", "Argentina", "Africa", "Egypt", "South Africa", "Hawaii"],
                          "March" : ["Italy", "Asia", "America", "Cuba", "Argentina", "the Maldives"],
                          "April" : ["Crete", "Malta", "Baleric Islands", "Africa", "Amsterdam, America, Turkey, the Philippines, Japan, Australia."],
                          "May" : ["Europe,the Philippines, the Bahamas, Mexico, Australia"],
                          "June" : ["Europe", "Namibia", "Brazil", "The Caribbean", "Canada", "Cuba"],
                          "July" : ["Australia", "Europe", "Indonesia", "Peru", "Bolivia", "America"],
                          "August" : ["Europe", "South Africa", "Peru and Tibet"],
                          "September" : ["Portugal", "Croatia", "Africa", "America", "China", "Japan"],
                          "October" : ["India", "Calcutta", "Turkey", "Cyprus", "Africa", "Egypt", "South Africa", "America", "Argentina", "Japan", "Venice"],
                          "November" : ["New Zealand", "Hawaii", "Aspen", "Germany", "America", "South America", "Morocco", "Belize", "Hong Kong"],
                          "December" : ["Mexico", "Belize", "Skiing Destinations", "the Caribbean", "Cambodia", "Australia", "Iceland"]
                          }
    current_date = str(datetime.datetime.now())
    month_list = ["January","February","March","April","May","June","July","September","October","November","December"]
    if(current_date[5:6] == '0'):
        month = current_date[6:7]
    else:
        month = current_date[5:7]
    month = month_list[int(month) - 1]
    holiday_occasion = "None"
    holiday_date = "None"
    for key, value in long_weekends.items():
        if(month.upper() in value ):
            holiday_occasion = key
            holiday_date = value
            break
    vacation = vacations_by_month[month]
    return [holiday_occasion,holiday_date,vacation]

@app.route('/',methods = ['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def index():
    data = request.data
    print(data)
    output_speech = basic(data)
    return output_speech


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
