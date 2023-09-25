import subprocess

# Execute the command
command = "dita -i my_map.ditamap -f pdf"
subprocess.run(command, shell=True, check=True)

