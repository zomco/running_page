import argparse
import os

import xml.etree.ElementTree as ET

# getting content root directory
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
ET.register_namespace('', "http://www.topografix.com/GPX/1/1")
ET.register_namespace('', "http://www.topografix.com/GPX/1/0")

def remove_whitespace(xml_string):
    root = ET.fromstring(xml_string)
    for elem in root.iter():
        if elem.text:
            old_text = elem.text
            elem.text = elem.text.strip()
            print(elem.text, old_text)
    return ET.tostring(root, encoding="utf-8").decode("utf-8")


if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("in_dir", help="origin tcx files location")
    # parser.add_argument("out_dir", help="pretty tcx files location")
    # options = parser.parse_args()
    # upload new tcx to strava
    print("Need to load all tcx files maybe take some time")


    # input_dir = options.in_dir
    # output_dir = options.out_dir

    input_dir = os.path.join(parent, "backup", "nrc_origin_test")
    output_dir = os.path.join(parent, "backup", "nrc_pretty_test")
    for filename in os.listdir(input_dir):
        if not filename.endswith(".tcx"):
            continue
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        tree = ET.parse(input_path)
        root = tree.getroot()
        # for elem in root.iter():
        #     if elem.text:
        #        elem.text = elem.text.strip()
        tree.write(output_path)
        # with open(input_path, 'r', encoding='utf-8') as file:
        #     xml_content = file.read()
        # formatted_xml = remove_whitespace(xml_content)
        # with open(output_path, 'w', encoding='utf-8') as file:
        #     file.write(formatted_xml)
    

