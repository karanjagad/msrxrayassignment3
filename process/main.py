import pandas as pd

repos = pd.read_csv("repositories_with_dependencies.csv", header=0)

# convert dependencies string to list
for i in range(len(repos)):
    a = repos["dependencies"][i]
    a = a.replace("[", "")
    a = a.replace("]", "")
    a = a.split(",")
    repos["dependencies"][i] = a

a = repos["dependencies"][0:]
a = list(a)

random_list = a
frequency = {}

for random_list in a:
    # iterating over the list
    for item in random_list:
        # checking the element in dictionary
        if item in frequency:
            # incrementing the counr
            frequency[item] += 1
        else:
            # initializing the count
            frequency[item] = 1

b = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
b[:10]
df_top = pd.DataFrame(b[:168], columns=["api", "count"])  # threshhold >90
total_count = df_top["count"].sum()

temp_list = []
for i in range(len(df_top)):
    api_a = list(df_top.iloc[i])
    for j in range(len(df_top)):
        if i != j:
            api_b = list(df_top.iloc[j])
            count_both = 0
            for k in range(len(a)):
                if df_top["api"][i] in a[k] and df_top["api"][j] in a[k]:
                    count_both += 1

            api_a_name = api_a[0]
            api_b_name = api_b[0]
            api_a_count = api_a[1]
            api_b_count = api_b[1]

            t = [
                api_a_name,
                api_b_name,
                api_a_count,
                api_b_count,
                count_both,
                (count_both / api_a_count),
                (count_both / api_b_count),
                (api_a_count / total_count),
                (api_b_count / total_count),
                (count_both / total_count),
            ]
            temp_list.append(t)

implies_df = pd.DataFrame(
    temp_list,
    columns=[
        "api_a",
        "api_b",
        "count_a",
        "count_b",
        "count_pair",
        "pom(a)",
        "pom(b)",
        "p(a)",
        "p(b)",
        "p(c_pair)",
    ],
)
implies_df["p(a)*p(b)"] = implies_df["p(a)"] * implies_df["p(b)"]
implies_df["Percentage difference"] = 1 - (
    implies_df["p(a)*p(b)"] / implies_df["count_pair"]
)

# generate csv from dataframe implies_df
implies_df.to_csv("../data/output/mcr_assignment3_analyse.csv")
