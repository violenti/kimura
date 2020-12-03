#
import yaml
from deployment import deploy

Deployment = deploy("mysql","2","3306")


#print(yaml.dump (data))