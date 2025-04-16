# %% [markdown]
# ---
# title: Goalkeepers and their heights
# author: Cameron West and Stéphane Guillou
# date: today
# warning: false
# error: false
# format: dashboard
# image: tb.png
# ---

# %%
import pandas as pd
df = pd.read_csv("../../data_sources/Players2024.csv")

# Remove missing position
df = df[df["positions"] != "Missing"]

# Ensure reasonable heights
df = df[df["height_cm"] > 100]

#%% [markdown]
"""
## Row {height = 10%}
**[Download the code for this dashboard](../example_project.zip)**
"""

# %% [markdown]
"""
## Figures {height=70%}
"""

# %%
#| title: Goalkeepers tend to be taller
#| fig-alt: "A scatterplot of the relationsip between height and position."
import seaborn as sns
import matplotlib.pyplot as plt
sns.catplot(data = df, x = "positions", y = "height_cm", kind = "box")
_ = plt.xlabel("Position")
_ = plt.ylabel("Height (cm)")
_ = plt.savefig("tb.png")
plt.show()

# %%
#| title: Age vs Height
import plotly.express as px
#px.scatter(data_frame = df, x = "Age", y = "height_cm")
px.scatter(data_frame = df, x = "age", y = "height_cm", color = "positions",
           facet_col = "positions", facet_col_wrap = 2, hover_name = "name",
           hover_data = "nationality", labels = {"height_cm": "Height (cm)",
                                                 "positions": "Position"})



# %% [markdown]
"""
## Table
"""

# %%
#| title: A glimpse at the dataset
df.head(10)




















