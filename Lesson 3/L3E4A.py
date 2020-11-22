from pprint import pprint
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

	print("\nExercise 4c - final dictionary")
	print("-" * 20)
	combined_data = {}
	for device_name, multi_result in agg_result.items():
		combined_data[device_name] = {}
		device_result = multi_result[0]
		for intf_dict in device_result.result:
			intf_name = intf_dict["port"]
			inner_dict = {
				"status": intf_dict["status"],
				"vlan": intf_dict["vlan"]
			}
			combined_data[device_name][intf_name] = inner_dict
	pprint(combined_data)
	print("-" * 20)
	print()


if __name__ == "__main__":
	main()
