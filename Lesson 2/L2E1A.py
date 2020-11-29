from nornir import InitNornir


def main():
	nr = InitNornir(config_file="config.yaml")
	print(f"\nNumber of workers: {nr.config.core.num_workers}\n")


if __name__ == "__main__":
	main()
