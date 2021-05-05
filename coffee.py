import csv
import plotly.express as px
import numpy as np

def get_data_source(data_path):
    Coffee_in_ml = []
    sleep_in_hours = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            Coffee_in_ml.append(float(row['week']))
            sleep_in_hours.append(float(row['Coffee in ml']))

    return {
        'x': Coffee_in_ml,
        'y': sleep_in_hours
    }

def find_correlation(data_source):
    correlation = np.corrcoef(data_source['x'], data_source['y'])

    print(correlation[0,1])

def setup ():
    data_path = 'coffee_c.csv'
    data_source = get_data_source(data_path)
    find_correlation(data_source)
    plotFigure(data_path)


def plotFigure (data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)

        fig = px.scatter(df, x="Coffee in ml", y='sleep in hours')
        fig.show()

setup()
