import json
from typing import Dict, Union, Set
import os

class JsonDiffer:
    def __init__(self):
        pass
    
    def read_json_file(self, file_path: str) -> Dict:
        """Read JSON data from a file"""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
            
        with open(file_path, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as e:
                raise json.JSONDecodeError(f"Invalid JSON in {file_path}: {str(e)}", e.doc, e.pos)

    def _get_all_keys(self, obj: Union[Dict, list], prefix: str = '') -> Set[str]:
        """Recursively get all keys from nested dictionary"""
        keys = set()
        if isinstance(obj, dict):
            for key, value in obj.items():
                current_key = f"{prefix}.{key}" if prefix else key
                keys.add(current_key)
                keys.update(self._get_all_keys(value, current_key))
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                keys.update(self._get_all_keys(item, f"{prefix}[{i}]"))
        return keys

    def compare_json_files(self, file_path1: str, file_path2: str) -> Dict:
        """Compare two JSON files and find key differences"""
        json1 = self.read_json_file(file_path1)
        json2 = self.read_json_file(file_path2)
        return self.find_key_differences(json1, json2)

    def find_key_differences(self, json1: dict, json2: dict) -> dict:
        """Find differences between two JSON objects"""
        keys1 = set(self._get_all_keys(json1))
        keys2 = set(self._get_all_keys(json2))
        
        return {
            "keys_only_in_first": sorted(list(keys1 - keys2)),
            "keys_only_in_second": sorted(list(keys2 - keys1)),
            "common_keys": sorted(list(keys1 & keys2))
        }

def main():
    differ = JsonDiffer()
    
    try:
        # Example usage
        file1 = "first.json"
        file2 = "second.json"
        
        differences = differ.compare_json_files(file1, file2)
        
        print("\nDifferences found:")
        print(f"Keys only in first file: {differences['keys_only_in_first']}")
        print(f"Keys only in second file: {differences['keys_only_in_second']}")
        print(f"Common keys: {differences['common_keys']}")
        
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
