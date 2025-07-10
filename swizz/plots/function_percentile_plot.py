from swizz.plots._registry import register_plot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

@register_plot(
    name="function_percentile_plot",
    description="Plot any function curve across x-values, grouped by a variable (e.g., scale), with percentile annotations and optional formula text, with customizable font sizes.",
    args=[
        {"name": "df", "type": "pd.DataFrame", "required": True, "description": "DataFrame containing 'x', 'y', and 'group' columns."},
        {"name": "xlabel", "type": "str", "required": False, "description": "Label for the x-axis. Default: 'X'."},
        {"name": "ylabel", "type": "str", "required": False, "description": "Label for the y-axis. Default: 'Y'."},
        {"name": "title", "type": "str", "required": False, "description": "Title for the plot. Default: 'Function Curve with Percentile Labels'."},
        {"name": "legend_title", "type": "str", "required": False, "description": "Title of the legend. Default: None."},
        {"name": "func_loc", "type": "str", "required": False, "description": "The location of the function text (if not None). Default: 'top left'."},
        {"name": "legend_loc", "type": "str", "required": False, "description": "The location of the legend (if not None). Default: 'lower right'."},
        {"name": "cmap", "type": "str", "required": False, "description": "The color map of the lines. Default: 'viridis'."},
        {"name": "hline_at", "type": "float", "required": False, "description": "Draw a horizontal line at this y-value. Default: None."},
        {"name": "function_str", "type": "str", "required": False, "description": "Optional LaTeX string to annotate function formula."},
        {"name": "function_str_coords", "type": "Tuple[float, float]", "required": False, "description": "Coordinates for the function string annotation in Axes coordinates. Default: (0.05, 0.96)."},
        {"name": "function_font_size", "type": "int", "required": False, "description": "Font size for function string annotation. Default: 13."},
        {"name": "numbers_font_size", "type": "int", "required": False, "description": "Font size for percentile number annotations. Default: 11."},
        {"name": "figsize", "type": "tuple", "required": False, "description": "Figure size. Default: (10, 6)."},
        {"name": "min_label_val", "type": "float", "required": False, "description": "Minimum y-value to annotate labels. Default: -inf."},
        {"name": "max_label_val", "type": "float", "required": False, "description": "Maximum y-value to annotate labels. Default: inf."},
        {"name": "percentiles", "type": "List[int]", "required": False, "description": "Percentiles to compute for labels. Default: [0,10,...,95]."},
        {"name": "fontsize", "type": "int", "required": False, "description": "Base font size for axis labels, tick labels, title, and legend. Default: 12."},
        {"name": "save", "type": "str", "required": False, "description": "Base filename to save PNG and PDF if provided."},
    ],
)

def plot(
    df: pd.DataFrame,
    xlabel: str = "X",
    ylabel: str = "Y",
    title: str = "Function Curve with Percentile Labels",
    legend_title: str = None,
    func_loc: str = "top left",
    legend_loc: str = "lower right",
    cmap: str = "viridis",
    hline_at: float = None,
    function_str: str = None,
    function_str_coords: tuple = (0.05, 0.96),
    function_font_size: int = 13,
    numbers_font_size: int = 11,
    figsize: tuple = (10, 6),
    min_label_val: float = -np.inf,
    max_label_val: float = np.inf,
    percentiles: list = None,
    fontsize: int = 12,
    save: str = None,
    ax=None,
):
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig = ax.figure

    if percentiles is None:
        percentiles = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95]

    groups = df['group'].unique()
    colormap = plt.get_cmap(cmap)
    colors = colormap(np.linspace(0, 1, len(groups)))

    x_ticks = []

    for color, group in zip(colors, groups):
        df_group = df[df['group'] == group].sort_values('x')
        x_vals = df_group['x'].values
        y_vals = df_group['y'].values

        ax.plot(x_vals, y_vals, label=f'{group}', color=color)

        current_percentiles = np.percentile(y_vals, percentiles)
        for y_val in sorted(current_percentiles):
            idx = np.abs(y_vals - y_val).argmin()
            x_at = x_vals[idx]
            y_at = y_vals[idx]
            if min_label_val <= y_at <= max_label_val:
                ax.text(x_at, y_at - 0.03, f'{y_at:.2f}',
                        ha='center', va='bottom', fontsize=numbers_font_size, color=color)
            if group == groups[0]:
                x_ticks.append(x_at)

    ax.set_xticks(x_ticks)
    ax.set_xticklabels([f'{int(x)}' for x in x_ticks], fontsize=fontsize)

    if hline_at is not None:
        ax.axhline(y=hline_at, color='black', linewidth=2.5, linestyle='-', alpha=0.2)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.xaxis.label.set_size(fontsize)
    ax.yaxis.label.set_size(fontsize)

    if title:
        ax.set_title(title, fontsize=fontsize)

    ax.grid(True, axis='y')

    if legend_title is not None:
        legend = ax.legend(title=legend_title, loc=legend_loc,
                           fontsize=fontsize, title_fontsize=fontsize)
        for text in legend.get_texts():
            text.set_fontsize(fontsize)

    if function_str:
        ver, hor = func_loc.split()
        ax.text(function_str_coords[0], function_str_coords[1], function_str,
                transform=ax.transAxes,
                fontsize=function_font_size,
                va=ver, ha=hor)

    plt.tight_layout()

    if save:
        fig.savefig(f"{save}.png", dpi=300, bbox_inches="tight")
        fig.savefig(f"{save}.pdf", dpi=300, bbox_inches="tight")

    return fig, ax
