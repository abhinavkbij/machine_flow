import pandas as pd  
import json  
  
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv')  
  
with open('boston.json', 'w') as f:  
    f.write(df.to_json(orient='records'))