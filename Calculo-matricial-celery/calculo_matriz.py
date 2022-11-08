from calc_config import app
import math

@app.task
def raiz(x):
    return math.sqrt(x)

@app.task
def pot(x):
    return x**x

@app.task
def log(x):
    return math.log10(x)

if __name__ == "__main__":

    app.start()

