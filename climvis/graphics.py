import matplotlib.pyplot as plt


def plot_annual_cycle(df, filepath=None):
    """Plot the annual cycle of precipitation and temperature.

    This function takes a DataFrame containing monthly average precipitation
    and temperature data and generates a bar plot showing the annual cycle
    of precipitation and a line plot showing the temperature.
    The plot can be saved to a file if a filepath is provided.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing the monthly average precipitation and temperature
        data. The DataFrame is expected to have the following columns:
            'grid_point_elevation', 'pre', 'tmp', 'lon', and 'lat'.
    filepath : str, optional
        The filepath to save the plot image. If not specified, the plot will
        not be saved. Default is None.

    Returns
    -------
    The generated matplotlib Figure object representing the plot.
    """
    z = df.grid_point_elevation
    df = df.loc['1981':'2010']
    df = df.groupby(df.index.month).mean()
    df.index = list('JFMAMJJASOND')

    f, ax = plt.subplots(figsize=(6, 4))

    df['pre'].plot(ax=ax, kind='bar', color='C0', label='Precipitation', rot=0)
    ax.set_ylabel('Precipitation (mm mth$^{-1}$)', color='C0')
    ax.tick_params('y', colors='C0')
    ax.set_xlabel('Month')
    ax = ax.twinx()
    df['tmp'].plot(ax=ax, color='C3', label='Temperature')
    ax.set_ylabel('Temperature (°C)', color='C3')
    ax.tick_params('y', colors='C3')
    title = 'Climate diagram at location ({}°, {}°)\nElevation: {} m a.s.l'
    plt.title(title.format(df.lon[0], df.lat[0], int(z)),
              loc='left')
    plt.tight_layout()

    if filepath is not None:
        plt.savefig(filepath, dpi=150)
        plt.close()

    return f
