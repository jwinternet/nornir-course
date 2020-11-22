from pprint import pprint
from nornir import InitNornir
from nornir.plugins.tasks.networking import napalm_get


def main():
	nr = InitNornir(config_file="config.yaml")
	nr = nr.filter(groups=["nxos"])
	agg_result = nr.run(
			task=napalm_get,
			getters=["config", "facts"],
			getters_options={"config": {"retrieve": "all"}},
	)

	combined_data = {}
	for device_name, multi_result in agg_result.items():
		combined_data[device_name] = {}
		device_result = multi_result[0]
		config_get = device_result.result["config"]
		config_start = config_get["startup"].split("\n")[4:]
		config_running = config_get["running"].split("\n")[4:]
		fact_get = device_result.result["facts"]
		if config_running == config_start:
			combined_data[device_name]["start_running_match"] = True
		else:
			combined_data[device_name]["start_running_match"] = False
		combined_data[device_name]["vendor"] = fact_get["vendor"]
		combined_data[device_name]["model"] = fact_get["model"]
		combined_data[device_name]["uptime"] = fact_get["uptime"]

	pprint(combined_data)


if __name__ == "__main__":
	main()
