from flask import Flask, request, jsonify,render_template
import pandas as pd

app =Flask(__name__)


df1 = pd.read_csv("data_small\stations.txt", skiprows=17)
df1=df1[['STAID','STANAME                                 ']]


@app.route("/")
def home():
    return render_template("home.html",data=df1.to_html()
                           )

@app.route("/api/v1/<station>/<date>")
def about(station,date):
    print("station:",station)
    print("date:",date)
    filename = 'data_small\TG_STAID'+str(station).zfill(6)+'.txt'
    df = pd.read_csv(filename, skiprows=20,  parse_dates=["    DATE"])

    temperature = df.loc[df['    DATE']==date]['   TG'].squeeze() / 10
    print(temperature)
    return {"station":station,
            "date":date,
            "temperature":temperature}

if __name__ == "__main__":

    app.run(debug=True)