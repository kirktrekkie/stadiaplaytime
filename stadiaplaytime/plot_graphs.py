from matplotlib import pyplot as plt


def make_graph_total_time(games_list):
    x = []
    y = []
    pie_names = []
    pie_times = []
    total_time = 1
    rest = 0

    for game in games_list:
        if game['name'] == 'Total':
            total_time = game['total_seconds']

    for game in games_list:
        if game['name'] != 'Total':
            x.append(game['name'])
            y.append(game['total_seconds']/3600)
            if game['total_seconds'] / total_time > 0.01:
                pie_names.append(game['name'])
                pie_times.append(game['total_seconds']/3600)
            else:
                rest += game['total_seconds']/3600
    pie_names.append("Rest")
    pie_times.append(rest)

    make_bar_graph(x, y)
    make_pie_graph(pie_times, pie_names)


def make_bar_graph(x, y):
    width = 10 + len(x) / 5
    plt.figure(figsize=(width,10))
    plt.bar(x ,y)
    plt.gcf().subplots_adjust(bottom=0.30)
    plt.xticks(rotation=90)
    plt.ylabel('Hours')
    plt.xlabel('Games')
    plt.title('Total time per game')

    plt.savefig('stadiaplaytime/static/total_time.png')


def make_pie_graph(times, game_names):
    plt.figure(figsize=(12,12))
    plt.pie(times, labels=game_names, autopct='%.2f%%')
    plt.savefig('stadiaplaytime/static/pie_graph.png')


if __name__ == '__main__':
    games_list = [{'name': 'Risk of Rain 2', 'total': '25:02:38', 'average': '00:57:47', 'total_seconds': 90158}, {'name': 'Farming Simulator 19', 'total': '2:19:22', 'average': '00:34:50', 'total_seconds': 8362}, {'name': 'Thumper', 'total': '0:59:29', 'average': '00:29:44', 'total_seconds': 3569}, {'name': 'Get Packed', 'total': '0:20:07', 'average': '00:20:07', 'total_seconds': 1207}, {'name': 'Stacks On Stacks (On Stacks)', 'total': '0:07:30', 'average': '00:07:30', 'total_seconds': 450}]
    make_graph_total_time(games_list)
    print("Done!")