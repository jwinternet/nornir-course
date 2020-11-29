from nornir import InitNornir
from random import random
import time


def my_task(task):
	time.sleep(random())
	host = task.host
	print(
			task.host.hostname,
			"\n",
			"-" * 20,
			f"\n\n   DNS1: {host['dns1']}",
			f"\n   DNS2: {host['dns2']}\n",
	)


if __name__ == "__main__":
	nr = InitNornir()
	nr.run(task=my_task)
