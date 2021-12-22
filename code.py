import pandas as pd , plotly.figure_factory as ff;
df = pd.read_csv("data.csv")
data = df["Avg Rating"].tolist()
fig = ff.create_distplot([data],["Avg Rating"])
fig.show()