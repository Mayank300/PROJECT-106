import csv
import plotly.express as px
import numpy as np

def get_data_source(data_path):
    ice_cream_sales = []
    cold_drink_sales = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            ice_cream_sales.append(float(row['Temperature']))
            cold_drink_sales.append(float(row['Ice-cream Sales( ₹ )']))

    return {
        'x': ice_cream_sales,
        'y': cold_drink_sales
    }

def find_correlation(data_source):
    correlation = np.corrcoef(data_source['x'], data_source['y'])

    print(correlation[0,1])

def setup ():
    data_path = 'data.csv'
    data_source = get_data_source(data_path)
    find_correlation(data_source)
    plotFigure(data_path)


def plotFigure (data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)

        fig = px.scatter(df, x="Ice-cream Sales( ₹ )", y='Cold drink sales( ₹ )')
        fig.show()

setup()
