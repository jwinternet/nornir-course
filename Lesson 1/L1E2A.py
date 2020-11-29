from nornir import InitNornir


def main():
	""""""
	nr = InitNornir()
	for host_name, host_obj in nr.inventory.hosts.items():
		print(
				f"Host: {host_name}",
				"-" * 20,
				f"Hostname: {host_obj.hostname}",
				f"Groups: {host_obj.groups}",
				f"Platform: {host_obj.platform}",
				f"Username: {host_obj.username}",
				f"Password: {host_obj.password}",
				f"Port: {host_obj.port}",
		)


if __name__ == "__main__":
	main()
