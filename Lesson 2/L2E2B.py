from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import netmiko_send_command


def main():
	nr = InitNornir(config_file="config.yaml")
	filt = F(groups__contains="ios")
	nr = nr.filter(filt)
	my_results = nr.run(
		task=netmiko_send_command, command_string="show ver | i uptime"
	)
	print(
			"\n",
			nr.inventory.hosts,
			"\n",
			f"my_results type: {type(my_results)}\n",
			f"items() method: {my_results.items()}\n",
			f"keys() method: {my_results.keys()}\n",
			f"values() method: {my_results.values()}\n",
	)


if __name__ == "__main__":
	main()
