from flask import Flask
import random
app = Flask(__name__)
@app.route('/')
def index():
 statuses=[200,500]
 x=random.choice(statuses)
 if x == 200:
 return "200 ok"
 elif x == 500:
 return "500 error"
if __name__ == "__main__":
app.run(host="0.0.0.0",port=5000)