from jobs_scheduler.job import Job
from jobs_scheduler.scheduler import Scheduler
from jobs_scheduler.utils import run_each_item_separate_thread
from jobs_scheduler.utils import insert_pending_jobs
import time
import threading
import queue


def example_func(interval, sleep=None):
    """  Example for a function that need to schedule """

    print(f"run every {interval} seconds and sleeping {sleep} sec")
    if sleep:
        time.sleep(sleep)
    print(f"After sleeping {sleep} seconds")


if __name__ == "__main__":

    job_queue = queue.Queue()
    interval = 20
    scheduler = Scheduler(job_queue)
    job = Job(interval, example_func, interval, sleep=50)
    scheduler.jobs.append(job)

    threading.Thread(target=run_each_item_separate_thread, kwargs={"jobs_queue": job_queue}).start()
    threading.Thread(target=insert_pending_jobs, kwargs={"schedule": scheduler}).start()

    print("test 1")
    time.sleep(40)
    print("test after 40 seconds")
    print("test 3")
