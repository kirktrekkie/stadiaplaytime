from random import randint
from matplotlib import pyplot as plt
from datetime import datetime
import numpy as np
import matplotlib.dates as mdates


def make_graph_total_time(games_list):
    long_name = []
    playtime_hours = []
    latest_play = []
    pie_names = []
    pie_times = []
    total_time = 1
    rest = 0

    for game in games_list:
        if game['name'] == 'Total':
            total_time = game['total_seconds']

    for game in games_list:
        if game['name'] != 'Total':
            long_name.append(shorten_name_if_needed(game['name']))
            playtime_hours.append(game['total_seconds']/3600)
            latest_play.append(game['last_played_date'])
            if game['total_seconds'] / total_time > 0.01:
                pie_names.append(shorten_name_if_needed(game['name'], 28))
                pie_times.append(game['total_seconds']/3600)
            else:
                rest += game['total_seconds']/3600
    pie_names.append("Rest")
    pie_times.append(rest)

    file_number = randint(10000, 99999)

    make_bar_graph(long_name, playtime_hours, file_number)
    make_pie_graph(pie_times, pie_names, file_number)
    make_timeline(latest_play, long_name, file_number)

    return file_number


def make_bar_graph(x, y, file_number):
    width = 10 + len(x) / 5
    plt.figure(figsize=(width,10))
    plt.bar(x ,y)
    plt.gcf().subplots_adjust(bottom=0.30)
    plt.xticks(rotation=90)
    plt.ylabel('Hours')
    plt.xlabel('Games')
    plt.title('Total time per game')

    plt.savefig(f'stadiaplaytime/static/total_time_{file_number}.png')


def make_pie_graph(times, game_names, file_number):
    plt.figure(figsize=(12,12))
    plt.pie(times, labels=game_names, autopct='%.2f%%')
    plt.savefig(f'stadiaplaytime/static/pie_graph_{file_number}.png')


def make_timeline(dates, game_names, file_number):
    dates = [datetime.strptime(d.split('T')[0], "%Y-%m-%d") for d in dates]
    level_range = int(len(game_names) / 2)
    level_values = [i for i in range(level_range * -1,level_range)]
    level_values.remove(0)
    levels = np.tile(level_values,
                     int(np.ceil(len(dates) / 6)))[:len(dates)]

    fig, ax = plt.subplots(figsize=(12, 10), constrained_layout=True)
    ax.set(title="Latest time you played a game")

    markerline, stemline, baseline = ax.stem(dates, levels,
                                             linefmt="C3-", basefmt="k-",
                                             use_line_collection=True)

    plt.setp(markerline, mec="k", mfc="w", zorder=3)

    # Shift the markers to the baseline by replacing the y-data by zeros.
    markerline.set_ydata(np.zeros(len(dates)))

    # annotate lines
    vert = np.array(['top', 'bottom'])[(levels > 0).astype(int)]
    for d, l, r, va in zip(dates, levels, game_names, vert):
        ax.annotate(r, xy=(d, l), xytext=(-3, np.sign(l) * 3),
                    textcoords="offset points", va=va, ha="right")

    # format xaxis with 4 month intervals
    ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval=1))
    ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%b %Y"))
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

    # remove y axis and spines
    ax.get_yaxis().set_visible(False)
    for spine in ["left", "top", "right"]:
        ax.spines[spine].set_visible(False)

    ax.margins(y=0.1)
    plt.savefig(f'stadiaplaytime/static/time_line_{file_number}.png')


def shorten_name_if_needed(name, max_len=33):
    if len(name) < max_len:
        return name
    else:
        return '{}...'.format(name[0:max_len - 3])


if __name__ == '__main__':
    games_list = [{'name': 'Risk of Rain 2', 'total': '25:02:38', 'average': '00:57:47', 'total_seconds': 90158}, {'name': 'Farming Simulator 19', 'total': '2:19:22', 'average': '00:34:50', 'total_seconds': 8362}, {'name': 'Thumper', 'total': '0:59:29', 'average': '00:29:44', 'total_seconds': 3569}, {'name': 'Get Packed', 'total': '0:20:07', 'average': '00:20:07', 'total_seconds': 1207}, {'name': 'Stacks On Stacks (On Stacks)', 'total': '0:07:30', 'average': '00:07:30', 'total_seconds': 450}]
    make_graph_total_time(games_list)
    print("Done!")