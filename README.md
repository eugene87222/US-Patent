# US-Patent

## Environment
- windows 10 home
- Python 3.6.4

## Prerequisite
- [install Python](https://www.python.org/)
- install requests, beautifulsoup, pandas
```
pip3 install requests
pip3 install beautifulsoup4
pip3 install pandas
```
---
## How to use
You can either set the input terms by yourself or let the program to read input terms from input_terms.txt
In "input_terms.txt", the format of each line is 
```
term1, field1, boolop1, term2, field2, boolop2, ... , boolopN-1, termN, fieldN
```
e.g.  
Electric vehicle, Title, AND, lithium battery, All Fields

There are 3 types of boolean operator and 56 types of fields.  
Boolean operator:
  - AND
  - OR
  - ANDNOT

Fields:

| 56 Types |  |  |  |  |
| --- | --- | --- | --- | --- |
| All Fields | Title | Abstract | Issue Date | Patent Number |
| Application Date | Application Serial Number | Application Type | Applicant Name | Applicant City |
| Applicant State | Applicant Country | Applicant Type | Assignee Name | Assignee City |
| Assignee State | Assignee Country | International Classification |Current CPC Classification | Current CPC Classification Class |
| Current US Classification | Primary Examiner | Assistant Examiner | Inventor Name | Inventor City |
| Inventor State | Inventor Country | Government Interest | Attorney or Agent | Parent Case Information |
| PCT Information | PCT 371C124 Date | PCT Filing Date | Foreign Priority | Reissue Data |
| Reissued Patent Application Filing Date | Related US App. Data | Related Application Filing Date | Priority Claims Date | Prior Published Document Date |
| Referenced By | Foreign References | Other References | Claim(s) | Description/Specification |
| Patent Family ID | 130(b) Affirmation Flag | 130(b) Affirmation Statement | Certificate of Correction | PTAB Trial Certificate |
| Re-Examination Certificate | Supplemental Exam Certificate | International Registration Number | International Registration Date | Hague International Filing Date |
| International Registration Publication Date |

You can also set "switch_DOWNLOAD", "switch_PARSE", "switch_TXT" in [main.py](https://github.com/eugene87222/US-Patent/blob/master/main.py) if you want the program to do speific things.  

After all, use the command below to run the program.
```
python main.py
```
