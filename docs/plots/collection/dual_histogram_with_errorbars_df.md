# `dual_histogram_with_errorbars_df`

> Plot main model and baseline histograms with mean frequencies and standard error bars, using a pandas DataFrame in long format.

---

## 📥 Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| data_df | pd.DataFrame | ✅ | Long-form DataFrame containing one row per sample with columns for the dataset label, seed, and score. |
| label_key | str | ✅ | Column name in data_df that identifies the dataset (main or baseline). |
| seed_key | str | ✅ | Column name identifying the random seed for each sample. |
| score_key | str | ✅ | Column name containing the score values. |
| main_label | str | ❌ | Value in label_key that denotes the main model. If not provided, first label is used. |
| baseline_labels | List[str] | ❌ | List of baseline labels; default is all labels except main_label. |
| baseline_colors | List[str] | ❌ | Colors for each baseline label. Default palette is used. |
| main_color | str | ❌ | Color for the main model. Default: '#4C72B0'. |
| num_bins | int | ❌ | Number of histogram bins. Default: 50. |
| xlabel | str | ❌ | Label for the x-axis. Default: 'Score'. |
| ylabel | str | ❌ | Label for the y-axis. Default: 'Average Frequency'. |
| title | str | ❌ | Plot title. Default: None. |
| figsize | tuple | ❌ | Figure size. Default: (8, 5). |
| save | str | ❌ | Base path to save PNG and PDF if provided. |
| fontsize | float | ❌ | Base font size for annotations, ticks, labels, title, and legend. |

---

## 📦 Example Output

````{dropdown} Click to show example code
```python
# Example code for |dual_histogram_with_errorbars_df| not found.
```
````

<img src="../../_static/images/plots/" alt="dual_histogram_with_errorbars_df" style="max-width: 100%; width: auto; height: auto; max-height: 450px;">
