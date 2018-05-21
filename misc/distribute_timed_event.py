from datetime import datetime, timedelta
import random

time_now = datetime.utcnow()
time_format = '%Y-%m-%d_%H:%M:%S'
current_snapshots = []
snapshot_spread = []
number_of_snapshots = 20


def which_to_pop(spread):
    sum_spread = sum(spread)
    population = range(1, number_of_snapshots + 1)
    weights = [1 / (i / sum_spread) for i in spread]
    return random.choices(population, weights)[0]


for hour in range(24 * 365):
    snapshot_time = time_now + timedelta(hours=hour)

    # Each hour, add a snapshot
    snapshot_add = snapshot_time.strftime(time_format)
    current_snapshots.insert(0, snapshot_add)

    # Each hour, remove a snapshot
    if len(current_snapshots) > number_of_snapshots:
        # Do something more intelligent here to decide which snapshot to remove
        snapshot_remove = current_snapshots.pop(which_to_pop(snapshot_spread))

    # Print current list of snapshots
    print(f'Current Snapshots: {current_snapshots}')

    # Print list of snapshots in terms of spread
    snapshot_spread = [
        (
            datetime.strptime(current_snapshots[0], time_format)
            - datetime.strptime(i, time_format)
        )
        // timedelta(hours=1) + 1
        for i in current_snapshots
    ]
    print(f'Snapshot spread: {snapshot_spread}')
