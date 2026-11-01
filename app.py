from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    df = pd.read_csv('/app/data/train_small.csv')
    rows = len(df)
    cols = len(df.columns)
    return f"""
    <html>
        <body>
            <h1>TP04 - Docker Web App</h1>
            <h2>Analyse réussie !</h2>
            <p>Nombre de lignes : {rows}</p>
            <p>Nombre de colonnes : {cols}</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)