import csv
import queue
import threading
import time

def reader(q, output_file):
    while True:
        item = q.get()
        if item is None:
            break

        with open(output_file, "a") as f:
            writer = csv.writer(f,
                    delimiter=',',
                    quotechar='"',
                    quoting=csv.QUOTE_MINIMAL)
            writer.writerow(item)

        q.task_done()

def start_workers(worker, output_file, num_jobs):
    q = queue.Queue()
    threads = []
    for i in range(num_jobs):
        t = threading.Thread(target=worker, args=(q,))
        threads.append(t)
        t.start()

    r = threading.Thread(target=reader, args=(q, output_file,))
    r.start()

    for t in threads:
        t.join()

    q.put(None)

    r.join()
