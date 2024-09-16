from fastapi import FastAPI
import uvicorn
import sklearn
import numpy as np
import pandas as pd
import pickle
import json 
from pydantic import BaseModel


app=FastAPI()

class inputvar(BaseModel):
    age: float
    sex:float
    bmi: float
    bp: float
    s1: float
    s2: float
    s3:float
    s4: float
    s5: float
    s6: float

## load the model from disk

regmodel= pickle.load(open('regmodel.pkl','rb'))
scaler= pickle.load(open('scaling.pkl','rb'))


@app.get('/')
def index():
    return{'message': 'Hello, world'}

@app.post('/predict')
def prediction(Data: inputvar):
    data=pd.json_normalize(Data.dict())
    data= scaler.transform(data)
    predicted=regmodel.predict(data)

    return f"The diabete progression prediction is {predicted}"





if __name__=='__main__':
    uvicorn.run(app)