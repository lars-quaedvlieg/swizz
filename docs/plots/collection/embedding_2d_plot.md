# `embedding_2d_plot`

> Plot a 2D embedding (e.g., t-SNE, PCA, UMAP) colored by categorical groups or continuous values, with optional density contours, legends, and colorbars.

---

## 📥 Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| df | pd.DataFrame | ✅ | DataFrame containing at least 'x', 'y', and the hue column. |
| font_family | str | ❌ | Font family for title, legend, and colorbar. Default: 'Times New Roman'. |
| title | str | ❌ | Title for the plot. Default: None. |
| mode | str | ❌ | Plotting mode: 'categorical' or 'continuous'. Default: 'categorical'. |
| hue_column | str | ❌ | Column name for coloring points. Must be provided. |
| palette | List[str] | ❌ | List of colors for categorical groups. If None, uses seaborn 'tab20' palette. |
| cmap_continuous | str | ❌ | Matplotlib colormap name for continuous values. Default: 'viridis'. |
| display_legend | bool | ❌ | Whether to display the legend (categorical mode only). Default: False. |
| legend_loc | str | ❌ | Legend location if displayed. Default: 'lower right'. |
| display_cbar | bool | ❌ | Whether to display the colorbar (continuous mode only). Default: False. |
| cbar_loc | str | ❌ | Colorbar inset location if displayed. Default: 'lower right'. |
| show_density | bool | ❌ | Whether to overlay density contours (continuous mode only). Default: False. |
| density_column | str | ❌ | Column to use for density grouping. Default: 'island' if exists. |
| density_alpha | float | ❌ | Transparency for density contours. Default: 0.5. |
| figsize | tuple | ❌ | Figure size in inches. Default: (8, 8). |
| s | int | ❌ | Marker size for scatter points. Default: 40. |
| alpha | float | ❌ | Transparency for scatter points. Default: 0.9. |
| edgecolor | str | ❌ | Edge color for scatter points. Default: 'white'. |
| linewidth | float | ❌ | Edge line width for scatter points. Default: 0.3. |
| fontsize | float | ❌ | Base font size for title, legend texts, and colorbar labels. Default: 12. |
| save | str | ❌ | Base filename to save PNG and PDF versions if provided. |

---

## 📦 Example Output

````{dropdown} Click to show example code
```python
# Example code for |embedding_2d_plot| not found.
```
````

<img src="../../_static/images/plots/" alt="embedding_2d_plot" style="max-width: 100%; width: auto; height: auto; max-height: 450px;">
