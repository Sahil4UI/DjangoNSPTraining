data = [{"id":101,"name":"rahul","grade":"A+"},
        {"id":102,"name":"rahul","grade":"B"},
        {"id":103,"name":"ram","grade":"A"},
        {"id":103,"name":"sam","grade":"A"},
        {"id":103,"name":"ram","grade":"A"},
        {"id":103,"name":"ram","grade":"A"},
        {"id":103,"name":"ram","grade":"A"},
        {"id":105,"name":"ram","grade":"A"},
        ]

for i in data:
    print(i["id"],i["name"],i["grade"])

import pandas as pd
df=pd.DataFrame(data=data)
# print(df.head())
# print(df.tail(8))
# df.dropna(inplace=True)
print(df)
df = df.drop_duplicates()
x = pd.value_counts(df["name"]=="ram")
print(x)
print(help(pd))