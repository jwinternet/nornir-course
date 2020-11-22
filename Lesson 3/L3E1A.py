from nornir import InitNornir


def main():
	nr = InitNornir()
	print()
	print(nr.inventory.hosts["arista3"].data)
	print(dict(nr.inventory.hosts["arista3"].items()))
	print()


if __name__ == "__main__":
	main()
