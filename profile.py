"""Allocates a client and server node, sets up passwordless SSH between them, and then installs/starts the Github CI runner on the client

Uses a fixed node type and image to automate as much as possible to streamline CI runs.

Instructions:
Wait for the profile instance to start, then click on the node in the topology and choose the `shell` menu item. 
"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# image list here: https://www.cloudlab.us/images.php
image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD'
node_type = 'xl170'

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()
 
names = ['client', 'server']
nodes = {}
for name in names:
    node = request.RawPC(name)

    node.hardware_type = node_type
    node.disk_image = image

    # This step isn't needed on repo-based CloudLab profiles since the repo is automatically
    # cloned on each machine, but this line can be added to use this repo with a regular
    # CloudLab profile.
    #node.addService(pg.Execute(shell="sh", command="git clone https://github.com/utah-scs/cxl-monster-ci.git /local/repository"))

    node.addService(pg.Execute(shell="sh", command="/local/repository/setup-ssh.sh"))

    nodes[name] = node

nodes['client'].addService(pg.Execute(shell="sh", command="/local/repository/setup-github-ci-runner.sh"))

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
