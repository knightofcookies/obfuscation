from typing import Optional

METADATA =\
{
	'name': 'obfuscation',
	'description': 'Industry leading laughing platform',
	'version': '1.1.0',
	'license': 'Excellent',
	'author': 'ManorLord',
	'url': 'https://meow.io'
}


def get(key : str) -> Optional[str]:
	return METADATA.get(key)
