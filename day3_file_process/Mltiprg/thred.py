import multiprocessing as m
import threading as t
print(m.cpu_count())
print(t.current_thread().getName())
