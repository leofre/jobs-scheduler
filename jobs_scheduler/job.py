import datetime
import functools


class Job(object):

    def __init__(self, interval, job_func, *args, **kwargs):
        self.interval = interval
        self.job_func = functools.partial(job_func, *args, **kwargs)
        self.last_run = None
        self.next_run = None
        self.period = None  # timedelta between runs
        self._schedule_next_run()

    def __lt__(self, other):

        return self.next_run < other.next_run

    @property
    def should_run(self):

        return datetime.datetime.now() >= self.next_run

    def run(self):

        self.job_func()
        self.last_run = datetime.datetime.now()
        self._schedule_next_run()

    def _schedule_next_run(self):

        interval = self.interval
        self.period = datetime.timedelta(seconds=interval)
        self.next_run = datetime.datetime.now() + self.period

