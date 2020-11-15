from matplotlib import pyplot as plt


def make_graph_total_time(games_list):
    x = []
    y = []

    for game in games_list:
        x.append(game['name'])
        y.append(game['total_seconds']/3600)

    plt.figure(figsize=(15,10))
    plt.bar(x ,y)
    plt.gcf().subplots_adjust(bottom=0.30)
    plt.xticks(rotation=45)
    plt.ylabel('Hours')
    plt.xlabel('Games')
    plt.title('Total time per game')

    plt.savefig('total_time.png')


if __name__ == '__main__':
    games_list = [{'name': 'Risk of Rain 2', 'total': '25:02:38', 'average': '00:57:47', 'total_seconds': 90158}, {'name': 'Farming Simulator 19', 'total': '2:19:22', 'average': '00:34:50', 'total_seconds': 8362}, {'name': 'Thumper', 'total': '0:59:29', 'average': '00:29:44', 'total_seconds': 3569}, {'name': 'Get Packed', 'total': '0:20:07', 'average': '00:20:07', 'total_seconds': 1207}, {'name': 'Stacks On Stacks (On Stacks)', 'total': '0:07:30', 'average': '00:07:30', 'total_seconds': 450}]
    make_graph_total_time(games_list)
    print("Done!")