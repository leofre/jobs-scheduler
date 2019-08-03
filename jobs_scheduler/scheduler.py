import functools


class Scheduler(object):

    def __init__(self, job_queue):
        self.jobs = []
        self.job_queue = job_queue

    def run_pending(self):

        pending_jobs = (job for job in self.jobs if job.should_run)
        for job in sorted(pending_jobs):
            # Changing the func to insert the original func into the jobs queue
            job.job_func = functools.partial(self.job_queue.put, job.job_func)
            job.run()

