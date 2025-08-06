import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
df = pd.read_csv("world_population.csv")

# Data Cleaning and Handling missing values
df.fillna(0, inplace=True)
print(df.info())

# ----------------------
# Analysis & Insights
# ----------------------

# Top 10 most populated countries (2022)
top_populated = df[["Country","2022 Population"]].sort_values("2022 Population", ascending=False).head(10)
print(top_populated)

# Population by Continent (2022)
population_by_continent = df.groupby("Continent")["2022 Population"].sum().sort_values(ascending=False)
print(population_by_continent)

# World Population % Share by Top 10 Countries
world_population = df[["Country", "World Population Percentage"]].sort_values("World Population Percentage", ascending=False).head(10)
print(world_population)

# Population growth trend over decades
yrs_col = [col for col in df.columns if "Population" in col and col[0:4].isdigit()]
yrs_df = df[["Country"] + yrs_col].set_index("Country")
yrs_df.columns = [int(col.split()[0]) for col in yrs_col]

top5 = df.sort_values("2022 Population", ascending=False)["Country"].head(5)
trends_over_decades = yrs_df.loc[top5]
print(trends_over_decades)

# Population Over Time (Top 15 Countries)
top15 = df.sort_values("2022 Population", ascending=False)["Country"].head(15)
population_over_time = yrs_df.loc[top15]

# ----------------------
# Visualizations
# ----------------------

sns.set_theme(style="whitegrid")

plt.figure(figsize=(10,6))
sns.barplot(data=top_populated, x="2022 Population", y="Country", palette="Blues_d", hue="Country", legend=False)
plt.title("Top 10 most populated countries (2022)")
plt.xlabel("Population")
plt.ylabel("Country")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("top_populated_country.png")
# plt.show()

plt.figure(figsize=(8,5))
plt.bar(population_by_continent.index, population_by_continent.values, color="teal")
plt.title("Total Population by Continent (2022)")
plt.xlabel("Continent")
plt.ylabel("Population")
plt.grid(axis="x")
plt.tight_layout()
plt.savefig("population_by_continent.png")
# plt.show()

plt.figure(figsize=(8,8))
plt.pie(world_population["World Population Percentage"], labels=world_population["Country"], autopct="%1.1f%%", startangle=140)
plt.title("World Population % Share by Top 10 Countries")
plt.axis("equal")
plt.tight_layout()
plt.savefig("top_world_population.png")
# plt.show()

trends_over_decades.T.plot(figsize=(12, 6), linewidth=0.7, linestyle="--", marker="o")
plt.title("Population Trend (1970–2022) - Top 5 Countries")
plt.xlabel("Year")
plt.ylabel("Population")
plt.grid(True)
plt.legend(title="Country")
plt.tight_layout()
plt.savefig("population_trends_(1970-2022).png")
# plt.show()

plt.figure(figsize=(10,8))
sns.heatmap(data=population_over_time, cmap="YlGnBu", linewidths=0.3, linecolor="gray")
plt.title("Population Heatmap (1970–2022) - Top 15 Countries")
plt.xlabel("Years")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("population_over_time.png")
# plt.show()

# Growth Rate vs Density
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x="Growth Rate", y="Density (per km²)", hue="Continent", alpha=0.8)
plt.title("Growth Rate vs Population Density (2022)")
plt.xlabel("Growth Rate")
plt.ylabel("Population Density")
plt.grid(True)
plt.tight_layout()
plt.savefig("growth_vs_density.png")
plt.show()

