from nornir import InitNornir


def main():
	""""""
	nr = InitNornir()
	for host_name, host_obj in nr.inventory.hosts.items():
		print(
				f"\nHost: {host_name.title()}",
				"-" * 20,
				f"\n\nHostname: {host_obj.hostname}",
				f"\nGroups: {host_obj.groups[0]}",
				f"\nPlatform: {host_obj.platform}",
				f"\nUsername: {host_obj.username}",
				f"\nPassword: {host_obj.password}",
				f"\nPort: {host_obj.port}\n",
		)


if __name__ == "__main__":
	main()
