import requests
import pandas as pd
url ="https://data.gov.sg/api/action/datastore_search?resource_id=f9dbfc75-a2dc-42af-9f50-425e4107ae84&q=2019"
result = requests.get(url).json()
# Try out the following codes
# Try to understand the result and figure out how is the data stored in json
print(result.keys()) #level_1
print(result['result'].keys)
print(result['result']['records'])

df = pd.DataFrame(result['result']['records'])
print(df.level_2)

print(df[df.level_1=='Total Residents'])
