from nornir import InitNornir
from nornir.core.filter import F


def main():
	nr = InitNornir()
	filt = F(groups__contains="ios")
	nr = nr.filter(filt)
	print(nr.inventory.hosts)


if __name__ == "__main__":
	main()
