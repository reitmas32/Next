######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 02/06/2022
### license = PSF
### version = 3.4.0 
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################

import ruamel.yaml
from io import StringIO
from pathlib import Path

# setup loader (basically options)
yaml = ruamel.yaml.YAML()
yaml.allow_duplicate_keys = True
# show null
def represent_of_null(self, data):
    return self.represent_scalar(u'tag:yaml.org,2002:null', u'null')
yaml.representer.add_representer(type(None), represent_of_null)

# o->s
def object_to_yaml_str(obj, options=None):
    if options == None: options = {}
    string_stream = StringIO()
    yaml.dump(obj, string_stream, **options)
    output_str = string_stream.getvalue()
    string_stream.close()
    return output_str

# s->o
def yaml_string_to_object(string, options=None):
    if options == None: options = {}
    return yaml.load(string, **options)

# f->o
def yaml_file_to_object(file_path, options=None):
    if options == None: options = {}
    as_path_object = Path(file_path)
    return yaml.load(as_path_object, **options)

# o->f
def object_to_yaml_file(obj, file_path, options=None):
    if options == None: options = {}
    as_path_object = Path(Path(file_path))
    with as_path_object.open('w') as output_file:
        return yaml.dump(obj, output_file, **options)