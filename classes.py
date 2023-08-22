import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt
from random import randrange


class Plotter:
    """
    A class for drawing plots.
    ...
    Attributes
    ----------
    url : str
        url to pandas json file.
    Methods
    -------
    draw_plot(*args, **kwargs) -> str:
        draws a plot, saves a plot & returns an url to the plot image.
    """

    def __init__(self, url: str) -> None:
        """
        Constructs all the necessary attributes for the Plotter object.
        :param url: url to pandas json file.
        """
        try:
            self.df: pd.DataFrame = pd.read_json(url)
        except:
            print('Что-то пошло не так. Пожалуйста, проверьте ссылку.')

    def draw_plot(self, *args, **kwargs) -> str:
        """
        Draws a plot, saves a plot.
        :param args: as in pandas.DataFrame.plot().
        :param kwargs: as in pandas.DataFrame.plot().
        :return: url to the plot.
        """
        try:
            # Creating and showing a plot.
            self.df.plot(*args, **kwargs)
            fig = plt.gcf()  # keeping fig for saving into file
            plt.show()

            # Saving fig into 'plots' dir. If dir not exist: create dir.
            try:
                os.mkdir('./plots/')
            except FileExistsError:
                pass
            finally:
                # Choosing unique name for file.
                target_url: str = (f'./plots/plot_'
                                   f'{dt.now().strftime("%Y%m%d%H%M%S")}_'
                                   f'{randrange(1000)}.png')
                fig.savefig(target_url)

            # Returning url to plot image.
            return target_url
        except:
            print('Не удалось создать график.')
