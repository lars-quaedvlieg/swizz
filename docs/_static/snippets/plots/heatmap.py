import pandas as pd
import matplotlib.pyplot as plt
from swizz import plot

# 1) Create the exact DataFrame from your example image
data = pd.DataFrame({
    10: {6:  0.93,  9: 0.86, 12: 0.86},
    20: {6:  0.92,  9: 0.88, 12: 0.86},
    50: {6:  0.92,  9: 0.90, 12: 0.75},
    100:{6:  0.75,  9: 0.90, 12: 0.78},
})
data.index.name = "Radius"
data.columns.name = "Team Reward"

# 2) Plot with annotations, custom colormap, cbar label, axis labels, and save output
fig, ax = plot(
    "heatmap",
    data=data,
    figsize=(7, 5),
    cmap="Blues",
    vmin=0.70,
    vmax=0.95,
    annot=True,
    fmt=".2f",
    cbar=True,
    cbar_title="Lone Wolf Rate",
    save="lone_wolf_rate_heatmap",
    x_category="Team Reward",
    y_category="Radius",
)

# 3) Show the figure
plt.show()
