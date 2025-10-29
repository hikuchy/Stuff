import re
def extract_patterns(file_path: str, pattern: str) -> None:
    with open(file_path, 'r') as file:
        for line in file:
            matches: List[str] = re.findall(pattern, line)
            if matches:
                print(matches)
