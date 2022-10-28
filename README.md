My implementation relies on ansible package community.docker
Here is a way to install it on your system:
"
>chmod og-rw ~/.netrc
>ansible-galaxy collection install community.docker
"

To run: <sudo> ansible-playbook create_containers.yml
	go on to input number of nodes you want (default 1000)
To change node number: <sudo> ansible-playbook create_containers.yml
	go on to input number of nodes you want (default 1000)
	this will reset just the dynamic partition
To clean repository: <sudo> bash ./scripts/cleanup.sh
	this will close the two docker containers and remove the python virtual environments
Extra: find IP addresses of the two docker containers by running <sudo> ansible-playbook add_to_inventory.yml
	this is not currently used but may be useful in the future
