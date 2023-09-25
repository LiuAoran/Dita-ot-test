import subprocess

# Execute the command
command = "dita -i my_map.ditamap -f markdown"
subprocess.run(command, shell=True, check=True)