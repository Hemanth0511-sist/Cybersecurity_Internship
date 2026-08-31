# 🔐 Cybersecurity Internship – Phase 1

## 15-Day Practical Cybersecurity Internship

**Name:** Hemanth Kumar D  
**Domain:** Cybersecurity  
**Duration:** 15 Days  
**Programming Language:** Python  
**Platform:** Windows  
**Environment:** Controlled and Authorized Training Laboratory

---

## 📌 About This Repository

This repository contains the practical cybersecurity work completed
during my 15-day internship.

The internship covered practical exercises in:

- Passive OSINT
- Email harvesting
- Phishing URL detection
- Vishing and smishing awareness
- GitHub OSINT
- Phishing awareness
- Email security
- Rate-limit defense
- USB security awareness
- Fake profile detection
- Honeypot monitoring
- Security awareness training
- Machine learning for phishing detection
- SIEM log analysis
- Incident response
- Social-engineering attack-chain analysis

All activities were performed in controlled and authorized
educational environments.

---

# 🎯 Internship Objectives

The main objectives of the internship were:

- Understand fundamental cybersecurity concepts.
- Gain hands-on experience with Python-based security tools.
- Understand passive reconnaissance and OSINT.
- Identify phishing and social-engineering indicators.
- Learn basic defensive security controls.
- Analyze security logs and generate alerts.
- Understand honeypot monitoring.
- Apply machine learning to phishing-email classification.
- Understand the incident-response lifecycle.
- Develop cybersecurity documentation and reporting skills.
- Improve troubleshooting and debugging abilities.

---

# 🛠️ Technologies and Tools

### Programming

- Python 3
- Flask
- Pandas
- Scikit-learn
- Requests
- Regular Expressions

### Data Formats

- JSON
- CSV
- HTML

### Tools & Environment

- Windows
- Command Prompt
- Visual Studio Code
- Notepad
- Localhost
- GitHub

### Cybersecurity Concepts

- OSINT
- DNS
- WHOIS
- Phishing
- Social Engineering
- Vishing
- Smishing
- SPF
- DKIM
- DMARC
- Rate Limiting
- USB Security
- Fake Profile Detection
- Honeypots
- SIEM
- Machine Learning
- Incident Response

---

# 📅 DAY 1 – PASSIVE OSINT

### File

`day01_osint_scanner.py`

## Objective

The objective of Day 1 was to understand Open Source Intelligence
(OSINT) and passive domain information gathering.

## Activities

The laboratory covered:

- Domain information
- DNS/IP resolution
- WHOIS information
- Registrar information
- Domain dates
- Name servers
- IP information
- Organization information
- Geolocation-related information

## Security Learning

This exercise demonstrated how publicly available information can
help security professionals understand an organization's external
digital footprint.

The activity focused on passive information gathering and did not
involve active scanning.

---

# 📅 DAY 2 – EMAIL HARVESTING

### File

`day02_email_harvester.py`

## Objective

The objective of Day 2 was to demonstrate controlled extraction of
email addresses from webpage content.

## Activities

The laboratory demonstrated:

- HTML content processing
- Email pattern matching
- Regular expressions
- Controlled webpage analysis
- Local laboratory testing

## Example Training Data

```text

📅 DAY 3 – PHISHING URL DETECTION
File

day03_phishing_detector.py

Objective

The objective of Day 3 was to create a basic defensive phishing URL
risk analyzer.

Detection Indicators

The analyzer examined:

HTTPS usage
Suspicious keywords
Login-related keywords
Account-related keywords
Security-related keywords
IP addresses in URLs
Excessive subdomains
Output

The program generated:

Risk Score
Risk Level
Suspicious Indicators
Example Analysis
HTTPS Website
URL        : https://github.com
Risk Score : 0%
Risk Level : LOW
HTTP Website
URL        : http://example.com
Risk Score : 30%
Risk Level : LOW

Indicator:

Not using HTTPS
Suspicious URL
URL        : https://login.verify.account.example.com
Risk Score : 85%
Risk Level : HIGH

Indicators included:

Suspicious keyword: login
Suspicious keyword: verify
Suspicious keyword: account
Excessive subdomains
IP-Based URL
URL        : http://192.0.2.10/login
Risk Score : 70%
Risk Level : HIGH
Security Learning

The exercise demonstrated how multiple URL characteristics can be
combined to identify potentially suspicious links.

📅 DAY 4 – VISHING & SMISHING AWARENESS
File

day04_awareness_scripts.py

Objective

The objective of Day 4 was to understand social-engineering
techniques used through phone calls and messaging platforms.

Scenario 1 – IT Support

Scenario Type: IT Support

Pretext: Urgent account-security notification

Psychological Trigger: Authority + urgency

The scenario demonstrated how an attacker may attempt to use
authority and urgency to influence a user.

Scenario 2 – Banking

Scenario Type: Banking

Pretext: Suspicious transaction notification

Psychological Trigger: Fear + urgency

The scenario demonstrated how fear and urgency can influence a
recipient's decision-making.

Scenario 3 – Government Service

Scenario Type: Government Service

Pretext: Important account-verification notice

Psychological Trigger: Authority + fear

Common Red Flags
Unexpected contact
Urgency
Fear-based messaging
Authority claims
Requests for confidential information
Unusual instructions
Pressure to bypass normal procedures
Defensive Practices

Users should:

Never disclose passwords to unexpected contacts.
Never disclose OTPs.
Never disclose PINs.
Never disclose banking information.
Verify requests independently.
Use official communication channels.
Report suspicious activity.
Security Learning

The exercise demonstrated how social engineering relies on
psychological manipulation rather than purely technical attacks.

📅 DAY 5 – GITHUB OSINT
File

day05_github_profile.py

Objective

The objective of Day 5 was to understand how publicly available
GitHub information can be used for OSINT analysis.

Information Analyzed

The laboratory analyzed public profile information such as:

Username
Name
Company
Location
Public repositories
Programming languages
Public biography
Demonstration Result
Username      : torvalds
Name          : Linus Torvalds
Company       : Linux Foundation
Location      : Portland, OR
Public Repos  : 12
Top Languages
OpenSCAD : 1
C        : 8
C++      : 1
Evidence

github_profile.json

Security Learning

The exercise demonstrated how publicly available developer
information can contribute to an OSINT profile.

Only public information was considered.

📅 DAY 6 – PHISHING AWARENESS
File

day06_phishing_awareness.py

Objective

The objective of Day 6 was to understand common phishing indicators
and appropriate defensive responses.

Training Concepts

The controlled phishing-awareness exercise demonstrated:

Security notifications
Account verification requests
Urgency
Personalized information
Suspicious links
Training Link
https://training.invalid/awareness-test

The .invalid domain was used as a safe non-functional training
placeholder.

Phishing Red Flags
Unexpected security notification
Pressure to act quickly
Personalized information used to build trust
Account-verification request
Suspicious or unfamiliar link
Defensive Response

The recommended response was:

Stop and do not respond immediately.
Verify the request through an official channel.
Do not trust unexpected links.
Report suspicious activity.
Email Security Concepts
SPF

Sender Policy Framework helps identify mail servers authorized to
send email for a domain.

DKIM

DomainKeys Identified Mail uses cryptographic signatures to help
verify email authenticity and integrity.

DMARC

Domain-based Message Authentication, Reporting and Conformance
provides policies for handling email authentication failures.

Security Learning

Learned how phishing indicators and email authentication
mechanisms contribute to defensive email security.

📅 DAY 7 – RATE LIMIT DEFENSE LAB
File

day07_rate_limit_lab.py

Objective

The objective of Day 7 was to demonstrate rate limiting as a
defensive control against repeated authentication attempts.

Laboratory Configuration
Server : http://127.0.0.1:5000
Limit  : 5 attempts per 30 seconds
Technology

A Flask-based local application was used for the controlled
authentication laboratory.

Security Concept

Rate limiting restricts the number of requests allowed within a
defined time period.

This can help reduce repeated automated authentication attempts.

Testing

The local authentication endpoint was tested with repeated
requests.

Failed authentication responses included:

401 Unauthorized

After the configured request threshold was reached, the defensive
rate-limit response was:

429 Too Many Requests
Troubleshooting

During testing, a connection-refused error was encountered:

ConnectionRefusedError: [WinError 10061]

The issue occurred because the Flask server was not running when
the client attempted to connect.

The issue was resolved by ensuring that the server was running
before performing the client-side test.

Security Learning

Learned how rate limiting and HTTP 429 Too Many Requests can be
used as defensive controls against repeated requests.

📅 DAY 8 – USB DROP AWARENESS LAB
File

day08_usb_awareness.py

Objective

The objective of Day 8 was to understand security risks associated
with unknown USB devices through a safe simulation.

Simulation

The program explicitly operated as a benign educational simulation.

[SIMULATION] Benign USB payload
[SIMULATION] No automatic execution configured.
[SIMULATION] Collecting only local lab system information.
Evidence

The simulation generated:

recon_log.txt

Security Learning

The exercise demonstrated the importance of:

Avoiding unknown USB devices
Preventing automatic execution
Using endpoint protection
Scanning removable media
Following organizational USB policies
Security awareness training
Result

The controlled USB-drop awareness simulation completed successfully.

📅 DAY 9 – FAKE PROFILE DETECTION LAB
File

day09_fake_profile_detector.py

Objective

The objective of Day 9 was to identify suspicious characteristics
in synthetic social-media profiles.

Detection Indicators

The program evaluated:

Account age
Followers
Following
Number of posts
Profile-picture availability
Generic/default biography
Profile A
Account age       : 7 days
Followers         : 2
Following         : 900
Posts             : 1
No profile picture: True
Default bio       : True

Fake score        : 100%
Risk level        : HIGH

Indicators:

Very new account
Very high following-to-follower ratio
No profile picture
Very few posts
Generic/default bio
Profile B
Account age       : 1200 days
Followers         : 4500
Following         : 320
Posts             : 870
No profile picture: False
Default bio       : False

Fake score        : 0%
Risk level        : LOW

No strong suspicious indicators were detected.

Profile C
Account age       : 15 days
Followers         : 8
Following         : 250
Posts             : 3
No profile picture: False
Default bio       : True

Fake score        : 80%
Risk level        : HIGH

Indicators:

Very new account
Very high following-to-follower ratio
Very few posts
Generic/default bio
Profile D
Account age       : 600 days
Followers         : 800
Following         : 500
Posts             : 120
No profile picture: False
Default bio       : False

Fake score        : 0%
Risk level        : LOW

No strong suspicious indicators were detected.

Profile E
Account age       : 20 days
Followers         : 15
Following         : 200
Posts             : 4
No profile picture: True
Default bio       : True

Fake score        : 100%
Risk level        : HIGH

Indicators:

Very new account
Very high following-to-follower ratio
No profile picture
Very few posts
Generic/default bio
Result Summary
Profile	Fake Score	Risk Level
A	100%	HIGH
B	0%	LOW
C	80%	HIGH
D	0%	LOW
E	100%	HIGH
Security Learning

Learned how multiple profile characteristics can be combined to
generate a suspicious-profile risk score.

All profiles used were synthetic training profiles.

📅 DAY 10 – HONEYPOT MONITORING LAB
File

day10_honeypot_tracker.py

Objective

The objective of Day 10 was to demonstrate basic honeypot
monitoring and security-event logging in a controlled localhost
environment.

Laboratory Environment
Server : http://127.0.0.1:8080
Training Endpoint
/lab-bait
Information Logged

The honeypot recorded:

Timestamp
Source IP
Requested path
Browser user-agent
Controlled Test Result

A browser request to the laboratory endpoint generated an event:

IP   : 127.0.0.1
Path : /lab-bait

A browser request for:

/favicon.ico

was also observed.

Evidence

honeypot_log.json

Security Learning

The exercise demonstrated:

Honeypot monitoring
Security telemetry
Request logging
Event collection
Basic suspicious-activity monitoring
📅 DAY 11 – SECURITY AWARENESS TRAINING
File

day11_awareness_training.py

Objective

The objective of Day 11 was to evaluate and reinforce knowledge of
social-engineering and cybersecurity defensive practices.

Topics Covered
Phishing
Social engineering
Impersonation
Confidential information
Verification
Suspicious messages
Defensive responses
Assessment Result
Score      : 10/10
Percentage : 100.0%
Evidence

day11_score_report.json

Security Learning

The assessment reinforced:

Verification of unexpected requests
Protection of confidential information
Recognition of suspicious messages
Avoidance of pressure-based decisions
Reporting of suspicious activity
📅 DAY 12 – PHISHING EMAIL DETECTION WITH MACHINE LEARNING
Files

day12_phishing_ml.py

day12_secure_input.py

Objective

The objective of Day 12 was to develop a basic machine-learning
model to classify emails as phishing or legitimate.

Dataset
Total emails : 50
Phishing     : 25
Legitimate   : 25
Dataset Validation
Dataset validation : PASSED
Machine Learning Model

A Naive Bayes classification approach was used for the controlled
email dataset.

Dataset Split
Training samples : 40
Testing samples  : 10
Model Performance
Accuracy : 100.00%
Confusion Matrix
[[5 0]
 [0 5]]
Classification Report
              precision    recall  f1-score   support

Legitimate       1.00      1.00      1.00         5
Phishing         1.00      1.00      1.00         5

accuracy                           1.00        10
macro avg        1.00      1.00      1.00        10
weighted avg     1.00      1.00      1.00        10
Custom Email Predictions
PHISHING   : Please verify your PayPal login
LEGITIMATE : Meeting notes from yesterday
PHISHING   : Urgent update your bank account
LEGITIMATE : Please review the project report
Evidence

day12_ml_results.csv

Machine Learning Workflow
Dataset
   ↓
Validation
   ↓
Training
   ↓
Testing
   ↓
Performance Evaluation
   ↓
Custom Prediction
Security Learning

Learned the basic process of applying machine learning to a
cybersecurity classification problem.

Limitation

The 100% accuracy applies only to the controlled dataset and
10-sample test set used in this laboratory.

It should not be interpreted as production-level phishing-detection
performance.

📅 DAY 13 – SIEM LOG ANALYSIS LAB
File

day13_siem_log_analyzer.py

Objective

The objective of Day 13 was to analyze security logs and identify
suspicious events using basic SIEM-style detection rules.

Failed Login Analysis
User            : admin
Failed attempts : 3

Generated alert:

[ALERT] Possible brute-force activity: admin (3 failures)
Email Rule Analysis
User : admin
Rule : forward_all

Generated alert:

[ALERT] Suspicious email rule created by: admin
Security Summary
Failed-login users analyzed : 1
Email-rule events analyzed  : 1
Security alerts generated   : 2
Security Learning

The laboratory demonstrated:

Security-log analysis
Event identification
Suspicious-pattern detection
Alert generation
SIEM concepts
Basic security monitoring
📅 DAY 14 – INCIDENT RESPONSE LAB
File

day14_incident_response.py

Objective

The objective of Day 14 was to apply a structured incident-response
workflow to a controlled phishing-awareness incident.

Incident Details
Incident type : Phishing email
Reported by   : Training User
Severity      : MEDIUM
Description
Suspicious account-verification email reported during
awareness exercise
1. IDENTIFY
Confirm the reported incident.
Identify affected accounts.
Identify affected users and devices.
Identify relevant messages.
Preserve email headers and logs.
2. CONTAIN
Restrict affected accounts if necessary.
Block suspicious messages, domains, or indicators.
Prevent further unauthorized access.
3. ERADICATE
Remove malicious messages.
Remove unauthorized email rules.
Reset affected credentials through approved procedures.
Remove unauthorized software or persistence mechanisms.
4. RECOVER
Restore affected services safely.
Monitor accounts and systems.
Confirm normal operation before closing the incident.
5. LESSONS LEARNED
Document what happened.
Identify security-control weaknesses.
Improve security awareness training.
Improve preventive controls.
Evidence

day14_incident_report.json

Result

The controlled incident-response workflow was completed
successfully.

📅 DAY 15 – SOCIAL ENGINEERING ATTACK CHAIN SIMULATOR
File

day15_se_attack_chain.py

Objective

Day 15 was the final integration exercise.

The objective was to combine multiple defensive cybersecurity
concepts from the previous days into one controlled educational
simulation.

Available Modules
[1] OSINT    - Passive domain information
[2] Profile  - Synthetic profile analysis
[3] Phish    - Defensive URL risk scoring
[4] Template - Security awareness simulation
[5] IR       - Incident response workflow
[6] Full     - Run complete simulation
[0] Exit
Full Simulation

The complete simulation was executed using:

Select module: 6
Module 1 – Passive OSINT

The simulator processed a controlled training domain.

Result:

[INFO] Passive DNS resolution completed.
[INFO] No active scanning performed.
Module 2 – Synthetic Profile

The simulator generated:

username            : training_user
account_age_days    : 420
public_posts        : 85
profile_type        : synthetic training profile
data_source         : lab-generated data

The simulator confirmed:

[INFO] No real person's profile was collected.
Module 3 – Phishing URL Scorer

Controlled training URL:

http://secure-account.example.com/login
Risk Assessment
Risk Score : 60%
Risk Level : MEDIUM
Indicators
Not using HTTPS
Suspicious keyword: login
Suspicious keyword: account
Suspicious keyword: secure
Module 4 – Security Awareness Template

The simulator generated a controlled awareness message.

Defensive Response
Stop and do not respond immediately.
Verify the request through an official channel.
Do not trust links from unexpected messages.
Report suspicious activity through the approved process.

The generated template was explicitly marked:

TRAINING ONLY - DO NOT SEND TO REAL USERS
Module 5 – Incident Response

The simulator generated a controlled incident:

Type     : phishing awareness alert
Severity : MEDIUM
Recommended Defensive Actions
Record the security alert
Preserve relevant evidence
Notify the appropriate security team
Review affected accounts if applicable
Remove suspicious email rules if unauthorized
Monitor for additional suspicious activity
Document lessons learned
Final Evidence

day15_final_report.json

🔗 COMPLETE DEFENSIVE WORKFLOW

The final simulation integrated the major concepts learned during
the internship:

Passive OSINT
      ↓
Synthetic Profile Analysis
      ↓
Phishing URL Risk Scoring
      ↓
Security Awareness
      ↓
Incident Response
      ↓
Final Report
📊 15-DAY INTERNSHIP SUMMARY
Day	Project	Result
01	Passive OSINT	Domain and public information analysis
02	Email Harvesting	Controlled email extraction
03	Phishing URL Detection	URL risk analysis
04	Vishing & Smishing Awareness	Social-engineering awareness
05	GitHub OSINT	Public profile analysis
06	Phishing Awareness	Phishing indicators and email security
07	Rate Limit Defense	Flask rate-limiting laboratory
08	USB Drop Awareness	Benign USB security simulation
09	Fake Profile Detection	5 synthetic profiles analyzed
10	Honeypot Monitoring	Local security-event logging
11	Security Awareness Training	10/10 – 100%
12	ML Phishing Detection	100% test accuracy
13	SIEM Log Analysis	2 security alerts generated
14	Incident Response	Structured IR workflow
15	SE Attack Chain	Integrated defensive simulation
📁 SOURCE CODE
day01_osint_scanner.py
day02_email_harvester.py
day03_phishing_detector.py
day04_awareness_scripts.py
day05_github_profile.py
day06_phishing_awareness.py
day07_rate_limit_lab.py
day08_usb_awareness.py
day09_fake_profile_detector.py
day10_honeypot_tracker.py
day11_awareness_training.py
day12_phishing_ml.py
day12_secure_input.py
day13_siem_log_analyzer.py
day14_incident_response.py
day15_se_attack_chain.py
📄 EVIDENCE AND OUTPUT FILES
github_profile.json
honeypot_log.json
recon_log.txt
day11_score_report.json
day12_ml_results.csv
day14_incident_report.json
day15_final_report.json
lab_page.html
🧠 SKILLS DEVELOPED
Cybersecurity Skills
Passive OSINT
DNS and domain analysis
Phishing detection
Social engineering
Vishing awareness
Smishing awareness
Email security
SPF
DKIM
DMARC
Rate limiting
USB security awareness
Fake-profile analysis
Honeypot monitoring
SIEM log analysis
Security alert generation
Machine learning for phishing detection
Incident response
Programming Skills
Python
Flask
Pandas
Scikit-learn
Requests
Regular expressions
JSON
CSV
HTML
Professional Skills
Problem solving
Debugging
Troubleshooting
Security analysis
Evidence collection
Result interpretation
Technical documentation
Incident reporting
📈 LEARNING OUTCOMES

The internship provided practical exposure to the defensive
cybersecurity lifecycle.

Information Gathering
        ↓
Threat Identification
        ↓
Phishing Analysis
        ↓
Security Awareness
        ↓
Defensive Controls
        ↓
Security Monitoring
        ↓
SIEM Analysis
        ↓
Machine Learning
        ↓
Incident Response
        ↓
Lessons Learned

The internship strengthened my ability to:

Develop Python-based cybersecurity tools
Analyze security-related data
Identify suspicious indicators
Interpret security alerts
Troubleshoot technical issues
Collect and document evidence
Apply defensive cybersecurity concepts
Prepare technical documentation
🏆 INTERNSHIP OUTCOME

By completing the 15-day practical cybersecurity program, I gained
hands-on exposure to multiple areas of defensive security.

The internship combined programming, security analysis, monitoring,
machine learning, awareness training, and incident response into a
single practical learning experience.

The final Day 15 project integrated the knowledge gained throughout
the internship into a controlled social-engineering attack-chain
simulation.

🔒 ETHICAL AND SAFETY STATEMENT

All activities in this repository were performed for authorized
educational and defensive cybersecurity training.

The exercises used controlled environments, synthetic data,
localhost services, training domains, simulated events, and
non-functional training resources where applicable.

No unauthorized access to systems, accounts, networks, or private
information was intended.

Security testing and analysis should only be performed on systems,
applications, networks, and accounts where explicit permission has
been provided.

👤 AUTHOR
Hemanth Kumar D

Cybersecurity Internship – Phase 1

GitHub: Hemanth0511-sist

📌 DISCLAIMER

This repository is intended strictly for authorized educational and
defensive cybersecurity purposes.

Security testing and analysis should only be performed on systems,
applications, networks, and accounts where explicit permission has
been provided.
it-support@lab.example
security@lab.example
training@lab.example
