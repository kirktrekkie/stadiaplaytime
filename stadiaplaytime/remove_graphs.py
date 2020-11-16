import os
import time

PATH = 'stadiaplaytime/static'


def remove_old_graphs(time_limit=1700):
    files = [f for f in os.listdir(PATH) if ".png" in f]
    current_time = time.time()

    for file in files:
        mod_time = os.path.getmtime(os.path.join(PATH, file))
        if current_time - mod_time > time_limit:
            os.remove(os.path.join(PATH, file))


if __name__ == '__main__':
    remove_old_graphs()