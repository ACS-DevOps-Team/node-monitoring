# Node-monitoring
A python script to monitor the status of nodes.

## Pre-requisites
* Python 3.6 installed on the node.
* Virtualenv python module installed.

## How to install script on node.
* Create a virtualenv on in the home director
code: python3 -m virtualenv <name of file e.g monitor>
* Copy/move the nodemonitor.py script to the virtualenv created in step one.
* Create a .env file in the root of the script file and add the following keypairs: webhook_url & node_endpoint.
* Copy/move the monitor.service file to etc/systemd/system/
* Replace "/home/<username>/<project_folder>/" in monitor.service with the virtualenv path.
* Run the following systemctl commands.
- systemctl daemon-reload
- systemctl start monitor.service
- systemctl enable monitor.service
* Run systemctl status monitor.service to confirm the status of the daemon.
