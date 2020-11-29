from nornir import InitNornir


def main():
	nr = InitNornir()
	print(f"\nNumber of workers: {nr.config.core.num_workers}\n")


if __name__ == "__main__":
	main()
