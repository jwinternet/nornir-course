from nornir import InitNornir


def main():
	nr = InitNornir()
	print(
			"\n--Lesson 1, Exercise 1A--",
			"\nnr.inventory:\n",
			nr.inventory,
			"\n\nnr.inventory.hosts:\n",
			nr.inventory.hosts,
			"\n\nnr.inventory.hosts['my_host']:\n",
			nr.inventory.hosts['my_host'],
			"\n\nnr.inventory.hosts['my_host'].hostname:\n",
			nr.inventory.hosts['my_host'].hostname,
	)


if __name__ == "__main__":
	main()
