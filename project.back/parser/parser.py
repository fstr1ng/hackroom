ldb_path = '/var/lib/clamav/Sprinthost.ldb'
ndb_path = '/var/lib/clamav/Sprinthost.ndb'
hdb_path = '/var/lib/clamav/Sprinthost.hdb'

dump_path = 'signatures.json'
bda_categories_path = 'categories.json'
bda_descriptions_path = 'descriptions.json'

from pprint import pprint
import json
import re
from dataclasses import dataclass

import pdb

signatures = []
with open(ldb_path) as ldb_file:
    for line in ldb_file:
        name, tdb, logic, *subsigs_raw = line.strip().split(';', maxsplit=4)
        subsigs = []
        subsigs.append({'type': 'hex', 'value': subsigs_raw[0], 'offset': '0'})
        subsigs.append({'type': 're', 'value': subsigs_raw[1:]})
        issue_match = re.search('\d{5,}', name)
        issue = issue_match.group(0) if issue_match else ''
        signatures.append({
            'line': line,
            'name': name,
            'issue': issue,
            'short_name': name.replace('Sprinthost', '').replace(issue, '').strip('.'),
            'type': 'regexp',
            'tdb': {arg:val for arg, val in [argval.split(':') for argval in tdb.split(',')]},
            'logic': logic,
            'subsigs': subsigs,
            'subsigs_rest': subsigs_raw[2:],
            })

with open(ndb_path) as ndb_file:
    for line in ndb_file:
        name, target, offset, value = line.strip().split(':')
        issue_match = re.search('\d{5,}', name)
        issue = issue_match.group(0) if issue_match else ''
        signatures.append({
            'line': line.strip(),
            'name': name,
            'issue': issue,
            'short_name': name.replace('Sprinthost', '').replace(issue, '').strip('.'),
            'type': 'body',
            'tdb': {'Target': target},
            'subsigs': {'type': 'hex', 'value': value, 'offset': offset},
            })

with open(hdb_path) as hdb_file:
    for line in hdb_file:
        hash_string, file_size, name = line.strip().split(':')
        issue_match = re.search('\d{5,}', name)
        issue = issue_match.group(0) if issue_match else ''
        signatures.append({
            'line': line.strip(),
            'name': name,
            'issue': issue,
            'short_name': name.replace('Sprinthost', '').replace(issue, '').replace('..', '').strip('.'),
            'type': 'hash',
            'subsigs': {'type': 'hash', 'value': hash_string, 'size': file_size},
        })

import MySQLdb
from MySQLdb.constants import FIELD_TYPE
#pdb.set_trace()
config_path = '/opt/configs/.my.bda.cnf'
conversion = {FIELD_TYPE.TIMESTAMP: str, FIELD_TYPE.LONG: int}
db=MySQLdb.connect(read_default_file=config_path, use_unicode=True, conv=conversion)

db.query('select * from hackscan_signatures_classes')
r1 = db.store_result()
db.query('select * from hackscan_signatures')
r2 = db.store_result()

categories = r1.fetch_row(maxrows=0, how=1)
descriptions = r2.fetch_row(maxrows=0, how=1)
db.close()

with open(bda_categories_path, 'w') as dump_file:
    json.dump(categories, dump_file)
with open(bda_descriptions_path, 'w') as dump_file:
    json.dump(descriptions, dump_file)


with open(dump_path, 'w') as dump_file:
    json.dump(signatures, dump_file)
