from fastapi import FastAPI
import csv
import datetime

def parse(file):
    with open(file, newline="") as f:
        data = csv.DictReader(f)
        data = list(data)

        result = []
        for row in data:
            row = dict((k.lower(), v.lower()) for k, v in row.items())
            result.append(row)

        return result

data = parse("./sports/data.csv")

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello world!"}

@app.get("/results")
async def results():
    return {"results": data}

