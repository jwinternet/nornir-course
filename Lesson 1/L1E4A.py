from nornir import InitNornir
from random import random
import time


def my_task(task):
	time.sleep(random())
	host = task.host
	print(
			"\n--Lesson 1, Exercise 4A--\n",
			task.host.hostname,
			"\n",
			"-" * 20,
			f"\n\nDNS1: {host['dns1']}",
			f"\nDNS2: {host['dns2']}\n",
	)


if __name__ == "__main__":
	nr = InitNornir()
	nr.run(task=my_task)
