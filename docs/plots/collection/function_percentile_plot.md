# `function_percentile_plot`

> Plot any function curve across x-values, grouped by a variable (e.g., scale), with percentile annotations and optional formula text, with customizable font sizes.

---

## 📥 Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| df | pd.DataFrame | ✅ | DataFrame containing 'x', 'y', and 'group' columns. |
| xlabel | str | ❌ | Label for the x-axis. Default: 'X'. |
| ylabel | str | ❌ | Label for the y-axis. Default: 'Y'. |
| title | str | ❌ | Title for the plot. Default: 'Function Curve with Percentile Labels'. |
| legend_title | str | ❌ | Title of the legend. Default: None. |
| func_loc | str | ❌ | The location of the function text (if not None). Default: 'top left'. |
| legend_loc | str | ❌ | The location of the legend (if not None). Default: 'lower right'. |
| cmap | str | ❌ | The color map of the lines. Default: 'viridis'. |
| hline_at | float | ❌ | Draw a horizontal line at this y-value. Default: None. |
| function_str | str | ❌ | Optional LaTeX string to annotate function formula. |
| function_str_coords | Tuple[float, float] | ❌ | Coordinates for the function string annotation in Axes coordinates. Default: (0.05, 0.96). |
| function_font_size | int | ❌ | Font size for function string annotation. Default: 13. |
| numbers_font_size | int | ❌ | Font size for percentile number annotations. Default: 11. |
| figsize | tuple | ❌ | Figure size. Default: (10, 6). |
| min_label_val | float | ❌ | Minimum y-value to annotate labels. Default: -inf. |
| max_label_val | float | ❌ | Maximum y-value to annotate labels. Default: inf. |
| percentiles | List[int] | ❌ | Percentiles to compute for labels. Default: [0,10,...,95]. |
| fontsize | int | ❌ | Base font size for axis labels, tick labels, title, and legend. Default: 12. |
| save | str | ❌ | Base filename to save PNG and PDF if provided. |

---

## 📦 Example Output

````{dropdown} Click to show example code
```python
# Example code for |function_percentile_plot| not found.
```
````

<img src="../../_static/images/plots/" alt="function_percentile_plot" style="max-width: 100%; width: auto; height: auto; max-height: 450px;">
