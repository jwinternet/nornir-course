import re
import colorama

from nornir import InitNornir
from nornir.plugins.tasks import networking

HOUR_SECONDS = 3600
DAY_SECONDS = 24 * HOUR_SECONDS
WEEK_SECONDS = 7 * DAY_SECONDS
YEAR_SECONDS = 365 * DAY_SECONDS
TEST = True


def parse_uptime(uptime_str):
	if "uptime is" in uptime_str:
		uptime_str = uptime_str.split("uptime is")[1]
	elif "Uptime:" in uptime_str:
		uptime_str = uptime_str.split("Uptime: ")[1]
	else:
		return 90

	(years, weeks, days, hours, minutes) = (0, 0, 0, 0, 0)

	uptime_str = uptime_str.strip()
	uptime_str = uptime_str.replace("and", ",")
	time_list = uptime_str.split(",")
	for element in time_list:
		if re.search("year", element):
			years = int(element.split()[0])
		elif re.search("week", element):
			weeks = int(element.split()[0])
		elif re.search("day", element):
			days = int(element.split()[0])
		elif re.search("hour", element):
			hours = int(element.split()[0])
		elif re.search("minute", element):
			minutes = int(element.split()[0])

	uptime_sec = ((years * YEAR_SECONDS) + (weeks * WEEK_SECONDS) + (
				days * DAY_SECONDS) + (hours * 3600) + (minutes * 60))
	return uptime_sec


def uptime(task):
	host = task.host
	platform = host.platform

	cmd_mapper = {
		"ios": "show version | inc uptime",
		"eos": "show version | inc Uptime",
		"nxos": "show version | inc uptime",
		"junos": "show system uptime | match System",
	}
	cmd = cmd_mapper[platform]
	multi_result = task.run(
			task=networking.netmiko_send_command,
			command_string=cmd
	)
	uptime_output = multi_result[0].result

	uptime_sec = parse_uptime(uptime_output)
	if uptime_sec < DAY_SECONDS:
		colorama.init()
		print()
		print(colorama.Fore.RED + colorama.Back.WHITE)
		print("-" * 40)
		print(f"{host.name}: device rebooted recently!")
		print(uptime_sec)
		print("-" * 40 + colorama.Style.RESET_ALL)
		print()
	elif TEST is True:
		print()
		print("-" * 40)
		print(f"{host.name}: device uptime is:")
		print(uptime_sec)
		print("-" * 40)
		print()


def main():
	nr = InitNornir(config_file="config.yaml")
	nr.run(task=uptime, num_workers=10)


if __name__ == "__main__":
	main()
