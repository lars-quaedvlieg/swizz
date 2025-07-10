# `percentile_curve_plot`

> Plot scores ranked by percentile with optional normalization, reference lines, highlighting, and customizable font sizes.

---

## 📥 Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| scores | Union[pd.Series, pd.DataFrame] | ✅ | Scores as a pandas Series or single-column DataFrame. |
| column | str | ❌ | Column name if `scores` is a multi-column DataFrame. |
| normalize_scores | bool | ❌ | Normalize scores to [0,1]. Default: True. |
| normalize_percentiles | bool | ❌ | Normalize percentiles to [0,1]. Default: True. |
| horizontal_markers | List[Tuple[float,str]] | ❌ | List of (y_value, label) for horizontal lines. |
| vertical_markers | List[Tuple[float,str]] | ❌ | List of (x_value, label) for vertical lines. |
| highlight_top_n | int | ❌ | Number of top scores to shade. Default: None. |
| highlight_color | str | ❌ | Color for highlight region. Default: '#c8e6c9'. |
| highlight_label | str | ❌ | Text label in highlight. Default: None. |
| highlight_label_color | str | ❌ | Color of highlight label text. Default: 'green'. |
| highlight_label_font_size | int | ❌ | Font size for highlight label text. Default: fontsize. |
| vertical_label_offset | float | ❌ | Offset above vertical marker. Default: 0.02. |
| xlabel | str | ❌ | X-axis label. Default: 'Percentile'. |
| ylabel | str | ❌ | Y-axis label. Default: 'Score'. |
| title | str | ❌ | Plot title. Default: None. |
| font_family | str | ❌ | Font family. Default: 'Times New Roman'. |
| fontsize | int | ❌ | Base font size for ticks, labels, title, and marker text. Default: 14. |
| figsize | tuple | ❌ | Figure size. Default: (8, 5). |
| save | str | ❌ | Base filename to save PNG/PDF if provided. |

---

## 📦 Example Output

````{dropdown} Click to show example code
```python
# Example code for |percentile_curve_plot| not found.
```
````

<img src="../../_static/images/plots/" alt="percentile_curve_plot" style="max-width: 100%; width: auto; height: auto; max-height: 450px;">
