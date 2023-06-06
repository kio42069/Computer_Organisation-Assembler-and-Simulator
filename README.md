# CSE112 - Semester Project
CSE112 - Computer Organisation

Objective: To create a basic assembler and simulator

Language: Python

# Collaborators
Prashi Jain [@ded-avishi](https://www.github.com/ded-avishi)

Surat Sathi Samanta [@surat-ss](https://www.github.com/surat-ss)

Riya Sachdeva [@riyasach189](https://www.github.com/riyasach189)

Tanish Verma [@VerTanish](https://www.github.com/vertanish)

# Automation

The final assembler is `final_assembler.py`

Errors thrown are 1-indexed while line addresses of labels and variables are 0-indexed

If label is not followed by an instruction, we are ignoring it and not throwing an error

In case a file has multiple errors, we are storing them in a text file in the same directory as the source code named `errors.txt`. It catches all errors in a single line too.

We are printing one of the errors on the terminal

.