# from pprint import pprint
from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import netmiko_send_command


def main():
	nr = InitNornir(config_file="config.yaml")
	nr = nr.filter(F(groups__contains="eos"))
	agg_result = nr.run(
			task=netmiko_send_command,
			command_string="show int status",
			use_textfsm=True)
	print()
	print("Exercise 4b - verify structured data")
	print("-" * 20)
	print(type(agg_result["arista1"][0].result))
	print("-" * 20)


if __name__ == "__main__":
	main()
