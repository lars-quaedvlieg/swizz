# `general_bar_plot`

> General bar plot comparing multiple metrics for each category with consistent colors, hatching, and customizable font sizes.

---

## 📥 Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| df | pd.DataFrame | ✅ | DataFrame containing the category column and one or more metric columns. |
| category_column | str | ✅ | Column name for the x-axis categories (e.g., 'Group', 'Condition'). |
| figsize | tuple | ❌ | Figure size. Default: (12, 7). |
| xlabel | str | ❌ | Label for x-axis. |
| ylabel | str | ❌ | Label for y-axis. |
| title | str | ❌ | Title of the plot. |
| legend_loc | str | ❌ | Legend location. Default: 'upper right'. |
| bar_width | float | ❌ | Width of bars. Default: 0.25. |
| color_map | Dict[str, str] | ❌ | Map from metric name to color. |
| style_map | Dict[str, str] | ❌ | Map from metric name to hatch style. |
| fontsize | float | ❌ | Base font size for axis labels, tick labels, title, legend, and annotations. Default: 12. |
| save | str | ❌ | Base filename to save PNG and PDF. |
| ax | matplotlib.axes.Axes | ❌ | Optional matplotlib Axes object. |

---

## 📦 Example Output

````{dropdown} Click to show example code
```python
# Example code for |general_bar_plot| not found.
```
````

<img src="../../_static/images/plots/" alt="general_bar_plot" style="max-width: 100%; width: auto; height: auto; max-height: 450px;">
