from enum import Enum

class PolicyType(str, Enum):
    sign   = 'signature'
    wlist  = 'whitelist'
    blist  = 'blacklist'
    cgroup = 'control_group'


class FileType(str, Enum):
    malware = 'malware_file'
    legit   = 'legitimate_file'

class SubSignType(str, Enum):
    regexp = 'regular_expression'
    hex    = 'hex_string'

class SignatureKeys(str, Enum):
    target    = 'target'
    engine    = 'engine'
    filesize  = 'file_size'
    entry     = 'entry_point'
    sections  = 'number_of_sections'
    container = 'container'
    inter     = 'intermediates'
