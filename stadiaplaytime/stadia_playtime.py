import json
from time import gmtime, strftime


def list_game_time(uploaded_file):
    with open(uploaded_file) as game_history_file:
        data = json.load(game_history_file)
        games = data.get('gamerHistory').get('applications')

        games = convert_string_to_int(games)
        print(games)
        games.sort(key=get_total_time, reverse=True)

        total_time = 0

        new_list = []
        for game in games:
            name = game['applicationName']
            time_seconds = game['totalTimePlayed']
            avg_time_seconds = game['averageTimePlayedPerSession']

            total_time += time_seconds

            # time = strftime("%w days %H:%M:%S", gmtime(time_seconds))
            avg_time = strftime("%H:%M:%S", gmtime(avg_time_seconds))

            #game_string = (f'{name}: Total: {calc_hours(time_seconds)}, Average: {avg_time}')
            game_dict = {"name" : name,
                         "total" : calc_hours(time_seconds),
                         "average" : avg_time}

            new_list.append(game_dict)

        #total = (f'Total: {calc_hours(total_time)}')
        total = {"name" : "Total",
                 "total" : calc_hours(total_time),
                 "average" : ""}
        new_list.append(total)

    return new_list


def convert_string_to_int(games):
    for game in games:
        game['totalTimePlayed'] = int(game['totalTimePlayed'].replace('s', ''))
        game['averageTimePlayedPerSession'] = int(game['averageTimePlayedPerSession'].replace('s', ''))

    return games


def get_total_time(game):
    return game['totalTimePlayed']


def calc_hours(input_time):
    seconds = int(input_time % 60)
    input_time = (input_time - seconds) / 60
    minutes = int(input_time % 60)
    input_time = (input_time - minutes) / 60
    hours = int(input_time)
    if seconds < 10:
        seconds = f'0{seconds}'
    if minutes < 10:
        minutes = f'0{minutes}'
    return f'{hours}:{minutes}:{seconds}'


if __name__ == '__main__':
    list_game_time()