import csv
import plotly.express as px
import numpy as np

def get_data_source(data_path):
    tv_size = []
    tv_time = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            tv_size.append(float(row['Size of TV']))
            tv_time.append(float(row['	Average time spent watching TV in a week (hours)']))

    return {
        'x': tv_size,
        'y': tv_time
    }

def find_correlation(data_source):
    correlation = np.corrcoef(data_source['x'], data_source['y'])

    print(correlation[0,1])

def setup ():
    data_path = 'tvTime.csv'
    data_source = get_data_source(data_path)
    find_correlation(data_source)
    plotFigure(data_path)


def plotFigure (data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)

        fig = px.scatter(df, x="Size of TV", y='	Average time spent watching TV in a week (hours)')
        fig.show()

setup()
