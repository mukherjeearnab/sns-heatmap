import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()
plt.rcParams["font.family"] = "Times New Roman"

df = pd.DataFrame({'Anomalies': ['Redundancy', 'Conflict', 'Incomplete', 'Cyclic Rule Redundancy'],
                   'University': [15, 15, 13, 1],
                   'Hospital': [15, 15, 5, 1],
                   'Demo': [15, 15, 13, 1],
                   'Continue': [15, 15, 5, 1],
                   'Conference-6': [15, 15, 5, 1],
                   'Conference-5': [15, 15, 5, 1],
                   'Conference-3': [15, 15, 5, 1],
                   'Bank': [15, 15, 12, 1]})

df = df.set_index(['Anomalies'])

print(df)


plt.figure(figsize=(12, 1.7))
# fig = plt.figure()
# fig.tight_layout()

ax = sns.heatmap(data=df, annot=True, cmap="crest")

ax.set(xlabel="Benchmark Policy", ylabel="Anomaly")
ax.margins(x=0)

plt.tight_layout(pad=0)

# ax1 = sns.heatmap()

# plt.show()

# sns.plt.show()

# plt.subplots_adjust(top=0.947,
#                     bottom=0.242,
#                     left=0.171,
#                     right=1,
#                     hspace=0,
#                     wspace=0)

# plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)


plt.savefig('test.pdf', bbox_inches='tight')
