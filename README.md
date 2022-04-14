# Ninja Forms < 3.6.8 - Unauthenticated Email Address Disclosure

Description
---
The plugin does not delete the temporary files created when exporting submissions, which could allow unauthenticated attackers to download them and get sensitive information such as the email address of users who submitted a form given that the file is publicly accessible, and with a guessable name
Proof of Concept
The exported CSV (generated when exporting all submissions via the "Download All Submissions" button) are stored in the /wp-content/uploads/<year>/<month> folder using the following format: form-<id>-all-subs.csv

Example: https://example.com/wp-content/uploads/2022/03/form-1-all-subs.csv 
  
How to Run
---
```
python3 ninja.py -u http://wordpress.lan
```
