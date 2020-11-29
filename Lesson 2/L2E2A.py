from nornir import InitNornir
from nornir.core.filter import F


def main():
	nr = InitNornir(config_file="config.yaml")
	filt = F(groups__contains="ios")
	nr = nr.filter(filt)
	print(
			"\n",
			nr.inventory.hosts,
			"\n",
	)


if __name__ == "__main__":
	main()
