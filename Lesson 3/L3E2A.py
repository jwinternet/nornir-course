from nornir import InitNornir
from nornir.core.filter import F


def main():
	nr = InitNornir()

	print("\nExercise 3a (role AGG)")
	print("-" * 20)
	agg_devs = nr.filter(F(role__contains="AGG"))
	print(agg_devs.inventory.hosts)
	print("-" * 20)


if __name__ == "__main__":
	main()
