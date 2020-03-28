ldb_path = '/var/lib/clamav/Sprinthost.ldb'
ndb_path = '/var/lib/clamav/Sprinthost.ndb'
hdb_path = '/var/lib/clamav/Sprinthost.hdb'

dump_path = 'signatures.yaml'
from pprint import pprint
import yaml
import re
from dataclasses import dataclass

#pdb.set_trace()
#import pdb

signatures = []
with open(ldb_path) as ldb_file:
    for line in ldb_file:
        legacy_name, tdb, logic, *subsigs_raw = line.strip().split(';', maxsplit=4)
        subsigs = []
        subsigs.append({'type': 'hex', 'value': subsigs_raw[0], 'offset': '0'})
        subsigs.append({'type': 're', 'value': subsigs_raw[1:]})
        issue_match = re.search('\d{5,}', legacy_name)
        issue = issue_match.group(0) if issue_match else ''
        signatures.append({
            'line': line,
            'legacy_name': legacy_name,
            'issue': issue,
            'name': legacy_name.replace('Sprinthost', '').replace(issue, '').strip('.'),
            'type': 'logical',
            'tdb': {arg:val for arg, val in [argval.split(':') for argval in tdb.split(',')]},
            'logic': logic,
            'subsigs': subsigs,
            'subsigs_rest': subsigs_raw[2:],
            })

with open(ndb_path) as ndb_file:
    for line in ndb_file:
        legacy_name, target, offset, value = line.strip().split(':')
        issue_match = re.search('\d{5,}', legacy_name)
        issue = issue_match.group(0) if issue_match else ''
        signatures.append({
            'line': line.strip(),
            'legacy_name': legacy_name,
            'issue': issue,
            'name': legacy_name.replace('Sprinthost', '').replace(issue, '').strip('.'),
            'type': 'body',
            'tdb': {'Target': target},
            'subsigs': {'type': 'hex', 'value': value, 'offset': offset},
            })

with open(hdb_path) as hdb_file:
    for line in hdb_file:
        hash_string, file_size, legacy_name = line.strip().split(':')
        issue_match = re.search('\d{5,}', legacy_name)
        issue = issue_match.group(0) if issue_match else ''
        signatures.append({
            'line': line.strip(),
            'legacy_name': legacy_name,
            'issue': issue,
            'name': legacy_name.replace('Sprinthost', '').replace(issue, '').replace('..', '').strip('.'),
            'type': 'hash',
            'subsigs': {'type': 'hash', 'value': hash_string, 'size': file_size},
        })

pprint(signatures, sort_dicts=False, width=100)
#print(yaml.dump(signatures))

#with open(dump_path, 'w') as dump_file:
#    yaml.dump(signatures, dump_file)
