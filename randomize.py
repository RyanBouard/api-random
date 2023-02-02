import random
from flask import Flask, request

app = Flask(__name__)
@app.route("/myMath/randomize", methods=["GET"])
def randomize():
    lower_bound = int(request.args.get("lower_bound", 10))
    upper_bound = int(request.args.get("upper_bound", 999))
    random_number = random.randint(lower_bound, upper_bound)
    return {"result": random_number}
app.run()
