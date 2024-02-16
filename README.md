# Js_Parse
                                  _                                                                 
                                 (_)____      ____  ____ ______________                             
                                / / ___/     / __ \/ __ `/ ___/ ___/ _ \                            
                               / (__  )     / /_/ / /_/ / /  (__  )  __/                            
                            __/ /____/_____/ .___/\__,_/_/  /____/\___/                             
                           /___/    /_____/_/                                                       
                                                                             
Supercharge your bug-hunting with JS_Parse, revealing hidden vulnerabilities inside the JS Files. JS_Parse is a Python script designed to extract JavaScript (JS) files from specified domains or a list of domains provided in a file. It then scans these JS files for potentially sensitive information such as API keys, tokens, passwords, and other configuration details.

# Features
- Domain Extraction: Extracts JS files from specified domains or a list of domains provided in a file.
- Sensitive Information Detection: Searches for sensitive information such as API keys, tokens, passwords, etc., within the extracted JS files.
- Configurability: Allows users to define custom patterns for sensitive information detection through a configuration file (patterns.json by default).
- Output Logging: Logs the results including the files found for each domain, extracted JS files, and any sensitive information detected.

# Installation
```
> git clone https://github.com/0x2458bughunt/Js_Parse
> cd Js_Parse
> python3 JS_Parse.py -i input.txt -o output.txt
```

# Usage
The tool can be executed with the following command-line arguments:
-d or --domain: Specify a single domain to extract JS files from.
-i or --input: Provide an input file containing multiple domains.
-c or --config: Specify a custom patterns configuration file (default is patterns.json).
-o or --output: Specify the output file to save the results (default is output.txt).

# Credits
A Big thanks to Shriyanss for updating the Regex-Check feature and improving the Overall Code! 

# Socials:
- 0x2458: https://twitter.com/0x2458
- Shriyanss: https://twitter.com/ss0x00
