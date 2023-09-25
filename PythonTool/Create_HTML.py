import subprocess

# Execute the command
command = "dita -i my_map.ditamap -f html5"
subprocess.run(command, shell=True, check=True)