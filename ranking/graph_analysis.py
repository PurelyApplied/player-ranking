import logging

import matplotlib.pyplot as plt
from networkx import Graph


def detect_component_sizes(g: Graph):
    """Flaw: currently coloring edges, it looks like."""
    logging.info("Attempting a recursive coloring...")

    def bleed(current, _colors):
        for n, _ in g.edges():
            if _colors[n] is None:
                _colors[n] = current
                bleed(current, _colors)

    colors = {k: None for k in g.edges()}
    current_color = 0
    for seed in list(colors.keys()):
        # print("try seed:", seed)
        if colors[seed] is None:
            colors[seed] = current_color
            bleed(current_color, colors)
            current_color += 1
    return colors, current_color


def draw_deg_dist(d, log_x=True, log_y=True):
    # These are the worst variable names.
    xs = sorted(d.keys())
    ys = [d[x] for x in xs]
    if log_x and log_y:
        plt.loglog(xs, ys)
    elif log_x:
        plt.semilogx(xs, ys)
    elif log_y:
        plt.semilogy(xs, ys)
    else:
        plt.plot(xs, ys)
    plt.title("Degree distribution")
    plt.show()
