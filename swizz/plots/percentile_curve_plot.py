from swizz.plots._registry import register_plot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

@register_plot(
    name="percentile_curve_plot",
    description="Plot scores ranked by percentile with optional normalization, reference lines, highlighting, and customizable font sizes.",
    args=[
        {"name": "scores", "type": "Union[pd.Series, pd.DataFrame]", "required": True,
         "description": "Scores as a pandas Series or single-column DataFrame."},
        {"name": "column", "type": "str", "required": False,
         "description": "Column name if `scores` is a multi-column DataFrame."},
        {"name": "normalize_scores", "type": "bool", "required": False,
         "description": "Normalize scores to [0,1]. Default: True."},
        {"name": "normalize_percentiles", "type": "bool", "required": False,
         "description": "Normalize percentiles to [0,1]. Default: True."},
        {"name": "horizontal_markers", "type": "List[Tuple[float,str]]", "required": False,
         "description": "List of (y_value, label) for horizontal lines."},
        {"name": "vertical_markers", "type": "List[Tuple[float,str]]", "required": False,
         "description": "List of (x_value, label) for vertical lines."},
        {"name": "highlight_top_n", "type": "int", "required": False,
         "description": "Number of top scores to shade. Default: None."},
        {"name": "highlight_color", "type": "str", "required": False,
         "description": "Color for highlight region. Default: '#c8e6c9'."},
        {"name": "highlight_label", "type": "str", "required": False,
         "description": "Text label in highlight. Default: None."},
        {"name": "highlight_label_color", "type": "str", "required": False,
         "description": "Color of highlight label text. Default: 'green'."},
        {"name": "highlight_label_font_size", "type": "int", "required": False,
         "description": "Font size for highlight label text. Default: fontsize."},
        {"name": "vertical_label_offset", "type": "float", "required": False,
         "description": "Offset above vertical marker. Default: 0.02."},
        {"name": "xlabel", "type": "str", "required": False,
         "description": "X-axis label. Default: 'Percentile'."},
        {"name": "ylabel", "type": "str", "required": False,
         "description": "Y-axis label. Default: 'Score'."},
        {"name": "title", "type": "str", "required": False,
         "description": "Plot title. Default: None."},
        {"name": "font_family", "type": "str", "required": False,
         "description": "Font family. Default: 'Times New Roman'."},
        {"name": "fontsize", "type": "int", "required": False,
         "description": "Base font size for ticks, labels, title, and marker text. Default: 14."},
        {"name": "figsize", "type": "tuple", "required": False,
         "description": "Figure size. Default: (8, 5)."},
        {"name": "save", "type": "str", "required": False,
         "description": "Base filename to save PNG/PDF if provided."},
    ],
)

def plot(
    scores,
    column=None,
    normalize_scores=True,
    normalize_percentiles=True,
    horizontal_markers=None,
    vertical_markers=None,
    highlight_top_n=None,
    highlight_color="#c8e6c9",
    highlight_label=None,
    highlight_label_color="green",
    highlight_label_font_size=None,
    vertical_label_offset=0.02,
    xlabel="Percentile",
    ylabel="Score",
    title=None,
    font_family="Times New Roman",
    fontsize=14,
    figsize=(8, 5),
    save=None,
    ax=None,
):
    # Handle DataFrame input
    if isinstance(scores, pd.DataFrame):
        if column is None:
            if scores.shape[1] != 1:
                raise ValueError("Specify `column` for multi-column DataFrames.")
            column = scores.columns[0]
        scores = scores[column]
    if not isinstance(scores, pd.Series):
        raise TypeError("`scores` must be a pandas Series or single-column DataFrame.")

    # Setup axis
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig = ax.figure

    # Sort and normalize
    vals = np.sort(scores.values)
    pct = np.linspace(0, 1, len(vals))
    if not normalize_percentiles:
        pct = np.arange(len(vals)) / (len(vals) - 1)
    if normalize_scores:
        mn, mx = vals.min(), vals.max()
        vals = (vals - mn) / (mx - mn) if mx != mn else np.zeros_like(vals)

    # Highlight top region
    if highlight_top_n and highlight_top_n > 0:
        n = min(highlight_top_n, len(vals))
        start = 1 - n / len(vals)
        ax.axvspan(start, 1, color=highlight_color, alpha=0.5, zorder=0)
        if highlight_label:
            fs_label = highlight_label_font_size or fontsize
            ax.text((start + 1) / 2, 0.02, highlight_label,
                    fontsize=fs_label, fontfamily=font_family,
                    color=highlight_label_color, ha='center', va='bottom')

    # Plot curve
    ax.plot(pct, vals, color='black', linewidth=2)

    # Reference lines
    if horizontal_markers:
        for y, lbl in horizontal_markers:
            ax.axhline(y=y, color='gray', linestyle='--', linewidth=1.5)
            ax.text(0.01, y, lbl,
                    fontsize=fontsize - 2, fontfamily=font_family,
                    va='bottom', ha='left', color='gray')
    if vertical_markers:
        for x, lbl in vertical_markers:
            idx = np.argmin(np.abs(pct - x))
            y = vals[idx]
            ax.plot([x, x], [0, y], color='gray', linestyle='--', linewidth=1.5)
            ax.text(x, y + vertical_label_offset, lbl,
                    fontsize=fontsize - 2, fontfamily=font_family,
                    va='bottom', ha='center', color='gray')

    # Axis labels and ticks
    ax.set_xlabel(xlabel, fontsize=fontsize, fontfamily=font_family)
    ax.set_ylabel(ylabel, fontsize=fontsize, fontfamily=font_family)
    ax.tick_params(axis='both', labelsize=fontsize)

    # Percentile/score tick formatting
    if normalize_percentiles:
        ticks = np.linspace(0, 1, 6)
        ax.set_xticks(ticks)
        ax.set_xticklabels([f"{int(t*100)}%" for t in ticks], fontsize=fontsize)
    if normalize_scores:
        ticks = np.linspace(0, 1, 6)
        ax.set_yticks(ticks)
        ax.set_yticklabels([f"{int(t*100)}%" for t in ticks], fontsize=fontsize)

    # Title
    if title:
        ax.set_title(title, fontsize=fontsize + 2, fontfamily=font_family)

    plt.tight_layout()
    if save:
        plt.savefig(f"{save}.png", dpi=300, bbox_inches='tight')
        plt.savefig(f"{save}.pdf", dpi=300, bbox_inches='tight')

    return fig, ax
