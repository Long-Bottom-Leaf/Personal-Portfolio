# Loading bar for user interface

from rich.progress import Progress
import time

def loading_bar(task_name="Processing...", total=25, speed=0.05):
    with Progress() as progress:
        task = progress.add_task(task_name, total=total)

        while not progress.finished:
            progress.update(task, advance=1)
            time.sleep(speed)