import threading
import time


def run_each_item_separate_thread(jobs_queue):
    """
    :param jobs_queue: queue that contains jobs to run
    """
    while 1:
        job_func = jobs_queue.get()
        threading.Thread(target=job_func).start()
        jobs_queue.task_done()


def insert_pending_jobs(schedule):

    while 1:
        schedule.run_pending()
        time.sleep(1)
