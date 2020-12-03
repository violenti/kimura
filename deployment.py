import yaml

def deploy(name,replicas,port):
    Deploy = "Deployment"
    Name = name
    Replica = replicas
    Port = port
    data = {
    'apiVersion': 'apps/v1',
    'kind': Deploy,
    'metadata': {'name': Name, 'labels': {'app': Name}},
    'spec': {'replicas': Replica, 'selector': {'matchLabels': {'app': Name}}},
    'template': {'metadata': {'labels': {'app': Name}}},
    'spec': {'containers': { 'name': 'nginx', 'image': 'nginx:1.7.9',
        'ports': {'containerPort': Port } }
    }}

    print(yaml.dump (data))
