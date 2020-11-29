from nornir import InitNornir
from random import random
import time


def my_task(task):
	time.sleep(random())
	print(
			"\n--Lesson 1, Exercise 4A--\n",
			task.host.hostname,
			"-" * 12,
			"\n\nYour message goes here...\n",
	)


if __name__ == "__main__":
	nr = InitNornir()
	nr.run(task=my_task)
