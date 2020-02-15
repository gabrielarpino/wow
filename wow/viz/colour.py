import seaborn as sns
import matplotlib.pyplot as plt
import random

# TODO: Random colour palette

# sns.set_palette("husl")
# "RdBu_r"
# "coolwarm"
# "BrBG"
# "GnBu_d"
# {‘sequential’, ‘diverging’, ‘qualitative’}
# sns.choose_colorbrewer_palette('seq', as_cmap=True)

# sns.set_palette(sns.choose_colorbrewer_palette('seq'))
flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]

PAL_list = [
                sns.cubehelix_palette(4),
                sns.color_palette("cubehelix", 4),
                sns.cubehelix_palette(4, start=.5, rot=-.75),
                flatui,
                sns.color_palette("RdBu_r", 4),
                sns.color_palette("coolwarm", 4),
                sns.diverging_palette(220, 20, n=4),
                sns.diverging_palette(255, 133, l=60, n=4, center="dark")]


# sns.set_palette(flatui)
#
# sns.set_palette(sns.diverging_palette(220, 20, n=7))
# sns.palplot(sns.diverging_palette(255, 133, l=60, n=7, center="dark"))

PAL = random.choice(PAL_list)
