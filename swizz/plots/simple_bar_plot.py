from swizz.plots._registry import register_plot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import colors as mcolors

@register_plot(
    name="general_bar_plot",
    description="General bar plot comparing multiple metrics for each category with consistent colors, hatching, and customizable font sizes.",
    args=[
        {"name": "df", "type": "pd.DataFrame", "required": True,
         "description": "DataFrame containing the category column and one or more metric columns."},
        {"name": "category_column", "type": "str", "required": True,
         "description": "Column name for the x-axis categories (e.g., 'Group', 'Condition')."},
        {"name": "figsize", "type": "tuple", "required": False, "description": "Figure size. Default: (12, 7)."},
        {"name": "xlabel", "type": "str", "required": False, "description": "Label for x-axis."},
        {"name": "ylabel", "type": "str", "required": False, "description": "Label for y-axis."},
        {"name": "title", "type": "str", "required": False, "description": "Title of the plot."},
        {"name": "legend_loc", "type": "str", "required": False, "description": "Legend location. Default: 'upper right'."},
        {"name": "bar_width", "type": "float", "required": False, "description": "Width of bars. Default: 0.25."},
        {"name": "color_map", "type": "Dict[str, str]", "required": False, "description": "Map from metric name to color."},
        {"name": "style_map", "type": "Dict[str, str]", "required": False, "description": "Map from metric name to hatch style."},
        {"name": "fontsize", "type": "float", "required": False,
         "description": "Base font size for axis labels, tick labels, title, legend, and annotations. Default: 12."},
        {"name": "save", "type": "str", "required": False, "description": "Base filename to save PNG and PDF."},
        {"name": "ax", "type": "matplotlib.axes.Axes", "required": False, "description": "Optional matplotlib Axes object."},
    ],
)
def plot(
    df,
    category_column,
    figsize=(12, 7),
    xlabel=None,
    ylabel=None,
    title=None,
    legend_loc="upper right",
    bar_width=0.25,
    color_map=None,
    style_map=None,
    fontsize=12,
    save=None,
    ax=None,
):
    # Validate DataFrame and inputs
    if not isinstance(df, pd.DataFrame):
        raise TypeError("`df` must be a pandas DataFrame.")
    if category_column not in df.columns:
        raise ValueError(f"`category_column` '{category_column}' not found in DataFrame.")

    categories = df[category_column].tolist()
    metric_columns = [col for col in df.columns if col != category_column]
    indices = np.arange(len(categories))

    # Default color and style maps
    if not color_map:
        color_map = {metric: None for metric in metric_columns}
    if not style_map:
        style_map = {metric: '/' for metric in metric_columns}

    # Create figure/axis
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig = ax.figure

    # Plot bars
    for i, metric in enumerate(metric_columns):
        values = df[metric].values
        positions = indices + (i - len(metric_columns)/2) * bar_width
        color = color_map.get(metric)
        hatch = style_map.get(metric, '/')

        bars = ax.bar(
            positions, values, bar_width,
            label=metric, color=color, linewidth=1, hatch=hatch
        )
        max_val = values.max() if values.size else 0
        # Annotate bars
        for rect in bars:
            face_rgba = mcolors.to_rgba(rect.get_facecolor(), alpha=1.0)
            edge_col = mcolors.to_hex([min(1, c*0.6) for c in face_rgba[:3]])
            rect.set_edgecolor(edge_col)
            height = rect.get_height()
            x = rect.get_x() + rect.get_width()/2
            y = height
            ax.text(
                x, y + max_val*0.01,
                f"{height:.1f}",
                ha='center', va='bottom',
                color=edge_col, fontweight='bold',
                fontsize=fontsize
            )
            ax.plot([x, x], [y, y + max_val*0.01], lw=1.5, color=edge_col)

    # Axis labels and ticks
    ax.set_xticks(indices)
    ax.set_xticklabels(categories, fontsize=fontsize)
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=fontsize)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=fontsize)

    # Title
    if title:
        ax.set_title(title, fontsize=fontsize)

    # Legend
    if legend_loc:
        leg = ax.legend(loc=legend_loc, fontsize=fontsize)
        for text in leg.get_texts():
            text.set_fontsize(fontsize)

    plt.tight_layout()

    # Save
    if save:
        fig.savefig(f"{save}.png", dpi=300, bbox_inches='tight')
        fig.savefig(f"{save}.pdf", dpi=300, bbox_inches='tight')

    return fig, ax
