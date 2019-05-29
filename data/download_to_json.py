import pandas as pd  
import json  
  
df = pd.read_csv('C:/Users/abhin/Documents/predicting_house_prices/kc_house_data.csv')  
  
with open('kc_house_data.json', 'w') as f:  
    f.write(df.to_json(orient='records'))