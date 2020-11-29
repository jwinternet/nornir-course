from nornir import InitNornir


def main():
	nr = InitNornir()
	print(
			"\nnr.inventory:",
			nr.inventory,
			"\nnr.inventory.hosts:",
			nr.inventory.hosts,
			"\nnr.inventory.hosts['my_host']:",
			nr.inventory.hosts['my_host'],
			"\nnr.inventory.hosts['my_host'].hostname:",
			nr.inventory.hosts['my_host'].hostname,
	)


if __name__ == "__main__":
	main()
