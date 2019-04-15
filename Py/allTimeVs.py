# For each of the matches in history, update win/loss record and GS/GC. At end, make table and output

import pandas as pd


data = pd.read_csv("../data-raw/belgium.csv")
data = data[["Date","home","visitor","hgoal","vgoal","result"]]
result_table = pd.DataFrame(columns=["Team","games", "GS", "GA", "points"])
result_table.set_index("Team", inplace=True, drop= False)

print(result_table.head())

for index, row in data.iterrows():
    if row["home"] not in result_table["Team"]:
        result_table = result_table.append({"Team": row["home"], "games": 0, "GS": 0, "GA": 0, "points": 0},
                                           ignore_index=True)
    # result_table.[row["home"]] = 1 + result_table['games'][row["home"]]
    result_table.loc[row["home"], 'games'] = 1
    # update values based on gamen for home
    if row["visitor"] not in result_table["Team"]:
        result_table = result_table.append({"Team": row["visitor"], "games": 0, "GS": 0, "GA": 0, "points": 0},
                                           ignore_index=True)
    # update values based on game for visitor





print(result_table.head())
