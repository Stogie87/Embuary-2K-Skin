import os
import hashlib

def generate_addons_xml(path='.', output='addons.xml'):
    addons = ''
    for d in os.listdir(path):
        addon_dir = os.path.join(path, d)
        if os.path.isdir(addon_dir) and os.path.exists(os.path.join(addon_dir, 'addon.xml')):
            with open(os.path.join(addon_dir, 'addon.xml'), 'r', encoding='utf-8') as f:
                addon_data = f.read().strip()
                addons += addon_data + '\n'
    addons = '<?xml version="1.0" encoding="UTF-8"?>\n<addons>\n' + addons + '</addons>'
    with open(output, 'w', encoding='utf-8') as f:
        f.write(addons)
    with open(output + '.md5', 'w') as f:
        f.write(hashlib.md5(addons.encode('utf-8')).hexdigest())

if __name__ == '__main__':
    generate_addons_xml()
