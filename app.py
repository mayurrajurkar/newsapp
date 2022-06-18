from flask import Flask ,render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=02766462b0cc42ce92cbd5189ba44e38" 
    r = requests.get(url).json()

    cases = {
        'article' : r['articles']
    }
    return render_template("index.html",case = cases)
if __name__ == "__main__":
     app.run(debug = True)