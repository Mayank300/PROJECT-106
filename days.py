import csv
import plotly.express as px
import numpy as np

def get_data_source(data_path):
    Roll_No = []
    Marks_In_Percentage = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            Roll_No.append(int(row['Roll No']))
            Marks_In_Percentage.append(float(row['Marks In Percentage']))

    return {
        'x': Roll_No,
        'y': Marks_In_Percentage
    }

def find_correlation(data_source):
    correlation = np.corrcoef(data_source['x'], data_source['y'])

    print(correlation[0,1])

def setup ():
    data_path = 'days.csv'
    data_source = get_data_source(data_path)
    find_correlation(data_source)
    plotFigure(data_path)


def plotFigure (data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)

        fig = px.scatter(df, x="Marks In Percentage", y='Days Present')
        fig.show()

setup()
