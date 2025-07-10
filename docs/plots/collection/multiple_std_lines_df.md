# `multiple_std_lines_df`

> Line plot with shaded confidence intervals and configurable label, color, and linestyle mappings, using a pandas DataFrame in long format.

---

## 📥 Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| data_df | pd.DataFrame | ✅ | Long-form DataFrame containing one row per point with columns for the run label, x values, y values, and standard error. |
| label_key | str | ✅ | Column name in data_df that identifies each run/series. |
| x_key | str | ❌ | Column name for x-axis values. Default: 'round_num'. |
| y_key | str | ❌ | Column name for y-axis values. Default: 'unique_scores'. |
| yerr_key | str | ❌ | Column name for standard error. Default: 'std_error'. |
| figsize | tuple | ❌ | Figure size. Default: (8, 5). |
| legend_loc | str | ❌ | Legend location. Default: 'upper left'. |
| legend_title | str | ❌ | Legend title. Default: None. |
| legend_ncol | int | ❌ | Number of columns in legend. Default: 1. |
| label_map | Dict[str, str] | ❌ | Mapping of raw labels to display names. |
| color_map | Dict[str, str] | ❌ | Mapping of raw labels to line colors. |
| style_map | Dict[str, str] | ❌ | Mapping of raw labels to line styles. |
| xlim | Tuple[float, float] | ❌ | X-axis limits. |
| ylim | Tuple[float, float] | ❌ | Y-axis limits. |
| xlabel | str | ❌ | X-axis label. |
| ylabel | str | ❌ | Y-axis label. |
| x_formatter | Callable | ❌ | Formatter for x-axis ticks. |
| y_formatter | Callable | ❌ | Formatter for y-axis ticks. |
| fontsize | int | ❌ | Base font size for axis labels, tick labels, legend, and CI shading labels. Default: 12. |
| save | str | ❌ | Base filename to save PNG and PDF. |

---

## 📦 Example Output

````{dropdown} Click to show example code
```python
# Example code for |multiple_std_lines_df| not found.
```
````

<img src="../../_static/images/plots/" alt="multiple_std_lines_df" style="max-width: 100%; width: auto; height: auto; max-height: 450px;">
