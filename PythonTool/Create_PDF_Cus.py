import subprocess

# Execute the command
command = "dita -i my_map.ditamap -f com.first.plugin"
subprocess.run(command, shell=True, check=True)
