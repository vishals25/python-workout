from flask import Flask,render_template,render_template_string
import pandas as pd
import numpy as np

app=Flask(__name__)


my_stations=pd.read_csv("data_small/stations.txt",skiprows=17)
my_stations=my_stations[['STAID','STANAME                                 ']]
my_stations['URL'] = my_stations['STAID'].apply(lambda x: f'<a href="/api/v1/{x}">/api/v1/{x}</a>')

html_table = my_stations.to_html(escape=False, index=False)



@app.route("/")

def home():
    return render_template('home.html',data=html_table)

@app.route("/api/v1/<station>/<date>/")

def about(station,date):
    df=pd.read_csv('data_small/TG_STAID'+str(station).zfill(6)+'.txt',skiprows=20,parse_dates=["    DATE"])
    temperature=df.loc[df['    DATE']==date]['   TG'].squeeze()/10
    return {'stationId':station,'Date':date,'temperature':temperature}


@app.route("/api/v1/<station>")

def station(station):
    df=pd.read_csv('data_small/TG_STAID'+str(station).zfill(6)+'.txt',skiprows=20,parse_dates=["    DATE"])
    df['   TG'] = df['   TG'].replace(-9999, np.nan)

    df = df[['    DATE', '   TG']].rename(columns={'    DATE': 'DATE', '   TG': 'TG'})
    
    # Convert the DataFrame to HTML
    html_table = df.to_html(escape=False, index=False)
    station_id = int(station)
    station_name = my_stations.loc[my_stations['STAID'] == station_id]['STANAME                                 '].squeeze()
    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>{{ station }} Data</title>
        </head>
        <body>
            <h1>Station Data for {{ station }}</h1>
            {{ table|safe }}
        </body>
        </html>
    ''', station=station_name, table=html_table)





@app.route("/api/v1/<station>/yearly/<year>")

def station_yearly(station,year):
    df=pd.read_csv('data_small/TG_STAID'+str(station).zfill(6)+'.txt',skiprows=20,parse_dates=["    DATE"])

    df['    DATE']=df['    DATE'].astype(str)

    df=df[df['    DATE'].str.startswith(year)]


    df['   TG'] = df['   TG'].replace(-9999, np.nan)

    df = df[['    DATE', '   TG']]

    html_table = df.to_html(escape=False, index=False)

    station_id = int(station)

    station_name = my_stations.loc[my_stations['STAID'] == station_id]['STANAME                                 '].squeeze()
    
    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>{{ station }} Data</title>
        </head>
        <body>
            <h1>Station Data for {{ station }}</h1>
            <h1>Station Data Year : {{ year }}</h1>
            {{ table|safe }}
        </body>
        </html>
    ''', station=station_name,year=year, table=html_table)










if __name__ == "__main__":
    app.run(debug=True)