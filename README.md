# Forensic Anti-patterns in Machine Learning Engineering 

## Farzana Ahmed Bhuiyan and Akond Rahman 

### Details 

> Demo video for the work in progress: https://drive.google.com/file/d/14lcIbDCIfHu8chqEOS7IX-yEckDFjT8z/view?usp=sharing

# MLForensics SQA Project  
**COMP 5710 / 6710 – Software Quality Assurance**  
**Fall 2025**

## Project Overview
This project applies core software quality assurance techniques to the existing **MLForensics** codebase. The goal is to integrate SQA activities such as fuzzing, logging (forensics), and continuous integration into the Python project, demonstrating practical application of workshop concepts.

---

## Student Information
**Student:** Cora Baldwin  
**StudentID:** 904149371
**Username:** coramb2  
**Repository:** [CoraBaldwin-Fall2025-SQA](https://github.com/coramb2/CoraBaldwin-Fall2025-SQA)

---

## Objectives
The project includes the following required SQA activities:

### 1. Fuzzing
A `fuzz.py` script will be implemented to automatically fuzz **five selected Python methods** within the MLForensics project.  
The script will:

- Generate randomized and mutated input data  
- Attempt to break or stress-test target functions  
- Capture and report discovered exceptions or bugs  
- Run automatically via GitHub Actions

### 2. Logging / Forensics Integration
Five Python methods will be enhanced with structured logging to improve traceability and observability. Logged data will include:

- Function entry and exit  
- Input parameters  
- Key internal states  
- Errors or exceptions  
- Timestamps and log levels

### 3. Continuous Integration
A GitHub Actions workflow will be created to ensure:

- Automated execution of `fuzz.py`
- Basic static checks / validations
- Artifact collection (fuzzing logs, crash outputs)
- CI status badge in the README

### 4. Reporting
A comprehensive documentation file (`SQA-REPORT.md`) will describe:

- How fuzzing was implemented  
- Bugs discovered during testing  
- Logging design and effectiveness  
- CI pipeline and results  
- Lessons learned  

---

## Repository Structure
MLForensics/
FAME-ML/
empirical/
mining/
task1.1.md
task1.2.md
CodingTasks.md
Verb.Object.Mapping.md
...additional support files...

fuzz.py # (to be added)
SQA-REPORT.md # (to be added)
.github/workflows/sqa.yml # (to be added)
README.md # this file

---

## Tools & Environment
- Python 3.x  
- GitHub Actions  
- Logging module (Python standard library)  
- Custom fuzzing utilities  
- Ubuntu (WSL2) development environment  

---

## Notes
This repository contains both the original MLForensics project materials and all new SQA additions required for COMP 5710/6710. All SQA artifacts will be clearly separated and documented.

---

## Author
**Cora Baldwin**  
Auburn University – Software Engineering  
COMP 5710 / 6710 – Fall 2025