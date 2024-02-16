import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import json
import sys
import time

# ANSI color codes for terminal colors
RED = '\033[91m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
CYAN = '\033[96m'
BLUE = '\033[94m'
BOLD = '\033[1m'
END_COLOR = '\033[0m'

# ASCII art
ASCII_ART = f"""{BOLD}{BLUE}
       _                                     
      (_)____      ____  ____ ______________ 
     / / ___/     / __ \\/ __ `/ ___/ ___/ _ \\
    / (__  )     / /_/ / /_/ / /  (__  )  __/
 __/ /____/_____/ .___/\\__,_/_/  /____/\\___/ 
/___/    /_____/_/                           
{END_COLOR}"""

AUTHORS = f"{BLUE}{BOLD}## Hunting JavaScript Secrets\n## Authors: 0x2458 & shriyanss{END_COLOR}"

# Centering function for multiline strings
def center_multiline(text, width):
    lines = text.split('\n')
    centered_lines = [line.center(width) for line in lines]
    return '\n'.join(centered_lines)

# Printing ASCII art and authors centered
print(center_multiline(ASCII_ART, 100))
print(center_multiline(AUTHORS, 100))

# Function to extract JS files from a given URL
def extract_js_files(url):
    js_files = []
    try:
        sys.stdout.write(f"{RED}~# {END_COLOR}{YELLOW}Checking domain: {url}...{END_COLOR}")
        sys.stdout.flush()
        animation = "|/-\\"
        idx = 0
        while True:
            sys.stdout.write("\b" + animation[idx % len(animation)])
            sys.stdout.flush()
            idx += 1
            time.sleep(0.1)
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                scripts = soup.find_all('script', src=True)
                for script in scripts:
                    js_url = urljoin(url, script['src'])
                    js_files.append(js_url)
                break
            else:
                print(f"\bFailed to fetch {url}. Status code: {response.status_code}")
                return js_files
        print(f"\b{GREEN} Done ✔{END_COLOR}")
    except Exception as e:
        print(f"Error extracting JS files from {url}: {e}")
    return js_files

# Function to extract sensitive information from a JS file
def extract_sensitive_info(js_url):
    sensitive_info = []
    try:
        response = requests.get(js_url)
        if response.status_code == 200:
            # Define patterns to search for sensitive information
            json_config = json.load(open(args.config, 'r'))
            patterns = json_config['patterns']

            for pattern in patterns:
                collected_info = re.findall(pattern, response.text, re.IGNORECASE)
                if collected_info:
                    sensitive_info.extend(collected_info)
        else:
            print(f"Failed to fetch {js_url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error extracting sensitive info from {js_url}: {e}")
    return sensitive_info

# Function to write output to a file
def write_output(output_file, domain, js_files):
    with open(output_file, 'a') as f:
        f.write(f"{YELLOW}Files found for {domain}{END_COLOR}\n")
        for idx, js_file in enumerate(js_files, start=1):
            f.write(f"{CYAN}{idx}. {js_file}{END_COLOR}\n")
            f.write(f"{GREEN}Extracted info:{END_COLOR}\n")
            sensitive_info = extract_sensitive_info(js_file)
            if sensitive_info:
                for info in sensitive_info:
                    f.write(f"{GREEN}{info}{END_COLOR}\n")
            else:
                f.write(f"{GREEN}No sensitive information found.{END_COLOR}\n")

# Main function
def main():
    parser = argparse.ArgumentParser(description="Extract JS files from a given domain or domains file and extract sensitive information from them.")
    parser.add_argument("-d", "--domain", help="Single domain to extract JS files from.")
    parser.add_argument("-i", "--input", help="Input file containing multiple domains.")
    parser.add_argument('-c', '--config', help="Patterns configuration file", default="patterns.json")
    parser.add_argument("-o", "--output", help="Output file to write results.")

    # making it global for easier access
    global args
    args = parser.parse_args()

    output_file = args.output if args.output else "output.txt"

    if args.domain:
        domain = args.domain
        js_files = extract_js_files(domain)
        write_output(output_file, domain, js_files)
    elif args.input:
        with open(args.input, 'r') as file:
            for line in file:
                domain = line.strip()
                js_files = extract_js_files(domain)
                write_output(output_file, domain, js_files)
    else:
        print("Please provide either a single domain or an input file containing multiple domains.")

if __name__ == "__main__":
    main()

