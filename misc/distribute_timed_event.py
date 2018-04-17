from datetime import datetime, timedelta
import random

time_now = datetime.utcnow()
time_format = '%Y-%m-%d_%H:%M:%S'
snapshot_dict = {
    'current_snapshots': []
}


for hour in range(24 * 365):
    snapshot_time = time_now + timedelta(hours=hour)

    # Each hour, add a snapshot
    snapshot_add = snapshot_time.strftime(time_format)
    snapshot_dict['current_snapshots'].insert(0, snapshot_add)

    # Each hour, remove a snapshot
    if len(snapshot_dict['current_snapshots']) > 20:
        # Do something more intelligent here to decide which snapshot to remove
        snapshot_remove = snapshot_dict['current_snapshots'].pop(
            random.randint(1, 20)
        )

    # Print current list of snapshots
    print(f'Current Snapshots: {snapshot_dict["current_snapshots"]}')

    # Print list of snapshots in terms of spread
    snapshot_spread = [
        (
            datetime.strptime(
                snapshot_dict['current_snapshots'][0], time_format
            ) - datetime.strptime(i, time_format)
        )
        // timedelta(hours=1) + 1
        for i in snapshot_dict['current_snapshots']
    ]
    print(snapshot_spread)

