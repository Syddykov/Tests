import json
import sys

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def update_values(tests, results):
    results_dict = {item['id']: item['value'] for item in results}
    
    def update_node(node):
        if 'id' in node and node['id'] in results_dict:
            node['value'] = results_dict[node['id']]
        
        if 'values' in node:
            for sub_node in node['values']:
                update_node(sub_node)
    
    for test in tests:
        update_node(test)

def main():
    if len(sys.argv) != 4:
        print("Usage: python update_report.py <values.json> <tests.json> <report.json>")
        sys.exit(1)
    
    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]
    
    values_data = load_json(values_path)
    tests_data = load_json(tests_path)
    
    update_values(tests_data['tests'], values_data['values'])
    
    save_json(tests_data, report_path)

if __name__ == "__main__":
    main()