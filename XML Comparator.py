import difflib
import sys

def compare_xml_files(xml_files):
    # Create a list to store the file contents
    xml_contents = []
    for file in xml_files:
        try:
            with open(file, 'r') as f:
                xml_contents.append(f.read())
        except:
            print(f"Error: Failed to read {file}")
            return

    # Compare the file contents using the unified_diff function
    for i in range(len(xml_files)):
        for j in range(i+1, len(xml_files)):
            diff = difflib.unified_diff(xml_contents[i].splitlines(), xml_contents[j].splitlines(), fromfile=xml_files[i], tofile=xml_files[j])
            print("\n".join(diff))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Error: Not enough arguments. Usage: python xml_compare.py file1.xml file2.xml [file3.xml ...]")
    else:
        compare_xml_files(sys.argv[1:])