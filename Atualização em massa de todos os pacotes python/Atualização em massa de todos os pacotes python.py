from importlib.metadata import distributions
packages = [dist.metadata['Name'] for dist in distributions()]