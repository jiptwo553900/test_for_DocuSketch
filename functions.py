from classes import Plotter


def draw_plots(url: str) -> list[str]:
    """
    Draws some plots and saves them as images.
    :param url: url to pandas json file.
    :return: list of urls to plot images.
    """
    # Creating Plotter class instance.
    myplot: Plotter = Plotter(url)

    path: str
    paths: list[str] = []

    # Creating Plot 0.
    path = myplot.draw_plot('gt_corners', 'rb_corners',
                            kind='scatter', title='Plot 0')
    paths.append(path)

    # Creating Plot 1.
    myplot.df = myplot.df.sort_values(by=['floor_mean', 'ceiling_mean'])
    path = myplot.draw_plot('name', ['mean', 'min', 'max'],
                            kind='line', rot=5, fontsize=4, title='Plot 1')
    paths.append(path)

    # Creating Plot 2.
    path = myplot.draw_plot('floor_mean', 'ceiling_mean',
                            kind='scatter', title='Plot 2')
    paths.append(path)

    # Creating Plot 3.
    path = myplot.draw_plot('ceiling_max', 'ceiling_min',
                            kind='scatter', color='red', title='Plot 3')
    paths.append(path)

    # Creating Plot 4.
    path = myplot.draw_plot('floor_max', 'floor_min',
                            kind='scatter', title='Plot 4')
    paths.append(path)

    # Creating Plot 5.
    path = myplot.draw_plot(y='floor_mean', kind='hist', title='Plot 5')
    paths.append(path)

    return paths
