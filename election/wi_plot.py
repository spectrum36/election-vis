import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv("state_ENR_president.csv", dtype={'jurisdiction_name': "string"})

wi_df = df[df['state'] == 'WI']

pivot_df = wi_df.pivot(index='time',columns="candidate", values="votes")

pivot_df = pivot_df.drop(columns=["Kennedy", "Oliver", "Stein", "West"])

pivot_df.index = pd.to_datetime(pivot_df.index, format="mixed")

date = pd.to_datetime('2024-11-07')

pivot_df = pivot_df.loc[(pivot_df.index < date)]

pivot_df.plot(kind="line", color=["blue", "red"])
plt.xlabel("time")
plt.ylabel("votes")

plt.ticklabel_format(axis='y', style='plain')

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%m-%d %H:%M"))
plt.gcf().set_figwidth(12)
plt.gcf().set_figheight(8)

#plt.show()
plt.savefig("plot.png")
