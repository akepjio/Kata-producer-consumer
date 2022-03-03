[![Matrix SVG](https://raw.githubusercontent.com/rodrigograca31/rodrigograca31/master/matrix.svg)](https://www.youtube.com/watch?v=SDkAGkd4NLc) 
# Kata-challenge-producer/consumer

the goal of this project is to create an application that generate pass (QRcode, PDF, ...) using Producer/Consumer pattern

### Technical Requirements

- Your Python's version must be greater than 2.7.10. 
Run `$ python --version` to check your Python's version

### Install Pip requirements

`$ pip install -r requirements.txt`

Freeze pip dependencies: 
`$ pip freeze > requirements.txt`

## Launch GUI
---

### Usage
Run  `$ python run.py`

### The structure of the project should be as follows: 
```
project
├── README.md
├── App
│     ├── app.py
├── Data
│     ├── data_generator.py
├── Queue
│     ├── producer.py
│     └── consumer.py
├── run.py
```
