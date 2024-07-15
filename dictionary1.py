data = [{"id":101,"name":"rahul","grade":"A+"},
        {"id":102,"name":"rahul","grade":"B"},
        {"id":103,"name":"ram","grade":"A"}
        ]

for i in data:
    print(i["id"],i["name"],i["grade"])

import pandas as pd
df=pd.DataFrame(data)
print(df)
