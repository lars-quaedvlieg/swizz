# `general_horizontal_bar_plot`

> Horizontal bar plot comparing metrics for each category, with optional group-based coloring and legends.

---

## 📥 Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| df | pd.DataFrame | ✅ | DataFrame with category_column and metric columns. |
| category_column | str | ✅ | Column used for y-axis labels. |
| category_group_key | str | ❌ | Column used for group labels (used for colour and legend). |
| group_color_map | Dict[str, str] | ❌ | Mapping of group label → colour. |
| figsize | tuple | ❌ | Figure size. Default: (12, 7). |
| xlabel | str | ❌ | Label for x-axis. |
| ylabel | str | ❌ | Label for y-axis. |
| title | str | ❌ | Title of the plot. |
| legend_loc | str | ❌ | Legend location. Default: 'upper right'. |
| bar_height | float | ❌ | Height of the bars. Default: 0.35. |
| color_map | Dict[str, str] | ❌ | Mapping of metrics to colours. |
| style_map | Dict[str, str] | ❌ | Mapping of metrics to hatch styles. |
| put_legend | bool | ❌ | Whether to display a legend. Default: True. |
| fontsize | float | ❌ | Base font size for axis labels, tick labels, title, legend, and annotations. Default: 12. |
| save | str | ❌ | Filename base to save PNG and PDF. |
| ax | matplotlib.axes.Axes | ❌ | Optional matplotlib Axes object. |

---

## 📦 Example Output

````{dropdown} Click to show example code
```python
import pandas as pd
import matplotlib.pyplot as plt
from swizz import plot

# 1) Prepare the data as a DataFrame
df = pd.DataFrame({
    "Category": ["64", "128", "256", "512", "1024", "2048", "0.95", "0.99", "0.995"],
    "rate": [0.7835051, 0.8800000, 0.9368421,
             0.8913044, 0.8800000, 0.8736842,
             0.8297873, 0.8800000, 0.7234042],
    "Group": ["Hidden size", "Hidden size", "Hidden size", "Batch size", "Batch size", "Batch size", "Discount factor", "Discount factor", "Discount factor"],
})

# 3) Assign one color per group
group_color_map = {
    "Discount factor": "#41047F",
    "Batch size":      "#7464AE",
    "Hidden size":     "#A3A1CB",
}

# 4) Plot using the new function
fig, ax = plot(
    "general_horizontal_bar_plot",
    df=df,
    category_column="Category",
    category_group_key="Group",
    group_color_map=group_color_map,
    xlabel="Lone-wolf capture rate",
    ylabel="",
    title="",
    bar_height=0.4,
    style_map={"rate": ""},
    put_legend=True,
    save="general_barh_plot",
    legend_loc="upper left",
)

plt.show()

```
````

<img src="../../_static/images/plots/general_barh_plot.png" alt="general_horizontal_bar_plot" style="max-width: 100%; width: auto; height: auto; max-height: 450px;">
