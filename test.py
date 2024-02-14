import time
from lullu_util.iteration import job_iterator


if __name__ == "__main__":
    jobs = list(range(10))
    for i in job_iterator(jobs):
        print("processing", i)
        time.sleep(1)
