"""This is a trivial example of a gitrepo-based profile; The profile source code and other software, documentation, etc. are stored in in a publicly accessible GIT repository (say, github.com). When you instantiate this profile, the repository is cloned to all of the nodes in your experiment, to `/local/repository`. 

This particular profile is a simple example of using a single raw PC. It can be instantiated on any cluster; the node will boot the default operating system, which is typically a recent version of Ubuntu.

Instructions:
Wait for the profile instance to start, then click on the node in the topology and choose the `shell` menu item. 
"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

image = 'UBUNTU22-64-STD'
node_type = 'xl170'

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()
 
names = ['client', 'server']
for name in names:
    node = request.RawPC(name)
    node.hardware_type = node_type
    node.disk_image = image
    node.addService(pg.Execute(shell="sh", command="/local/repository/setup-ssh.sh"))
    nodes[name] = node

nodes[client].addService(pg.Execute(shell="sh", command="/local/repository/setup-github-ci-runner.sh"))

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
