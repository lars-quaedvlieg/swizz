import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.cm as cm

from swizz.plots._registry import register_plot

@register_plot(
    name="multiple_std_lines_df",
    description=(
        "Line plot with shaded confidence intervals and configurable label, color, "
        "and linestyle mappings, using a pandas DataFrame in long format."    ),
    args=[
        {"name": "data_df", "type": "pd.DataFrame", "required": True,
         "description": (
             "Long-form DataFrame containing one row per point with columns for the run label, "
             "x values, y values, and standard error."
         )},
        {"name": "label_key", "type": "str", "required": True,
         "description": "Column name in data_df that identifies each run/series."},
        {"name": "x_key", "type": "str", "required": False,
         "description": "Column name for x-axis values. Default: 'round_num'."},
        {"name": "y_key", "type": "str", "required": False,
         "description": "Column name for y-axis values. Default: 'unique_scores'."},
        {"name": "yerr_key", "type": "str", "required": False,
         "description": "Column name for standard error. Default: 'std_error'."},
        {"name": "figsize", "type": "tuple", "required": False,
         "description": "Figure size. Default: (8, 5)."},
        {"name": "legend_loc", "type": "str", "required": False,
         "description": "Legend location. Default: 'upper left'."},
        {"name": "legend_title", "type": "str", "required": False,
         "description": "Legend title. Default: None."},
        {"name": "legend_ncol", "type": "int", "required": False,
         "description": "Number of columns in legend. Default: 1."},
        {"name": "label_map", "type": "Dict[str, str]", "required": False,
         "description": "Mapping of raw labels to display names."},
        {"name": "color_map", "type": "Dict[str, str]", "required": False,
         "description": "Mapping of raw labels to line colors."},
        {"name": "style_map", "type": "Dict[str, str]", "required": False,
         "description": "Mapping of raw labels to line styles."},
        {"name": "xlim", "type": "Tuple[float, float]", "required": False,
         "description": "X-axis limits."},
        {"name": "ylim", "type": "Tuple[float, float]", "required": False,
         "description": "Y-axis limits."},
        {"name": "xlabel", "type": "str", "required": False,
         "description": "X-axis label."},
        {"name": "ylabel", "type": "str", "required": False,
         "description": "Y-axis label."},
        {"name": "x_formatter", "type": "Callable", "required": False,
         "description": "Formatter for x-axis ticks."},
        {"name": "y_formatter", "type": "Callable", "required": False,
         "description": "Formatter for y-axis ticks."},
        {"name": "fontsize", "type": "int", "required": False,
         "description": "Base font size for axis labels, tick labels, legend, and CI shading labels. Default: 12."},
        {"name": "save", "type": "str", "required": False,
         "description": "Base filename to save PNG and PDF."},
    ],
)

def plot(
    data_df: pd.DataFrame,
    label_key: str,
    x_key: str = "round_num",
    y_key: str = "unique_scores",
    yerr_key: str = "std_error",
    figsize: tuple = (8, 5),
    legend_loc: str = "upper left",
    legend_title: str = None,
    legend_ncol: int = 1,
    label_map: dict = None,
    color_map: dict = None,
    style_map: dict = None,
    xlim: tuple = None,
    ylim: tuple = None,
    xlabel: str = None,
    ylabel: str = None,
    x_formatter=None,
    y_formatter=None,
    fontsize: int = 12,
    save: str = None,
    ax=None,
):
    # Setup figure
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig = ax.figure

    # Ensure label ordering type
    try:
        data_df[label_key] = data_df[label_key].astype(int)
    except Exception:
        try:
            data_df[label_key] = data_df[label_key].astype(float)
        except Exception:
            pass

    # Default color mapping
    if color_map is None:
        uniq = data_df[label_key].unique()
        cmap = cm.get_cmap('viridis')
        positions = np.linspace(0,1,len(uniq))
        color_map = {lab: cmap(pos) for lab,pos in zip(uniq,positions)}

    # Plot each series with CI
    for lab, grp in sorted(data_df.groupby(label_key), key=lambda x: x[0]):
        name = label_map.get(lab, lab) if label_map else lab
        clr = color_map.get(lab)
        ls = style_map.get(lab, 'solid') if style_map else 'solid'

        x = grp[x_key].values
        y = grp[y_key].values
        yerr = grp[yerr_key].values

        line, = ax.plot(x, y, label=name, color=clr, linestyle=ls)
        fill_clr = clr if clr is not None else line.get_color()
        ax.fill_between(x, y - yerr, y + yerr, color=fill_clr, alpha=0.2)

    # Legend
    if legend_loc:
        leg = ax.legend(loc=legend_loc, title=legend_title, ncol=legend_ncol)
        leg.set_title(leg.get_title().get_text(), prop={'size':fontsize})
        for txt in leg.get_texts(): txt.set_fontsize(fontsize)

    # Formatters
    if x_formatter:
        ax.xaxis.set_major_formatter(mtick.FuncFormatter(x_formatter))
    if y_formatter:
        ax.yaxis.set_major_formatter(mtick.FuncFormatter(y_formatter))

    # Axis labels and ticks
    if xlabel: ax.set_xlabel(xlabel, fontsize=fontsize)
    if ylabel: ax.set_ylabel(ylabel, fontsize=fontsize)
    if xlim: ax.set_xlim(xlim)
    if ylim: ax.set_ylim(ylim)
    ax.tick_params(axis='both', labelsize=fontsize)

    # Save
    if save:
        fig.savefig(f"{save}.png", dpi=300, bbox_inches='tight')
        fig.savefig(f"{save}.pdf", dpi=300, bbox_inches='tight')

    return fig, ax
