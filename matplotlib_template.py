import matplotlib

font = {"size": 12}
matplotlib.rc("font", **font)
matplotlib.rcParams["axes.spines.left"] = True
matplotlib.rcParams["axes.spines.right"] = False
matplotlib.rcParams["axes.spines.top"] = False
matplotlib.rcParams["axes.spines.bottom"] = False


VERY_DARK_VIOLET = "#1e1332"
LIGHT_MAGENTA = "#e7d4e8"
VIOLET = "#af8dc3"
DARK_MAGENTA = "#762a83"

LIGHT_LIME_GREEN = "#d9f0d3"
LIME_GREEN = "#7fbf7b"

YELLOW_POLKA_DOT = "#fdb863"
ORANGE = "#e66101"

COLUMN_WIDTH = 6.3
ONE_COLUMN_FIGURE_SIZE = (COLUMN_WIDTH / 2, 2)
TWO_COLUMN_FIGURE_SIZE = (COLUMN_WIDTH, 2)
