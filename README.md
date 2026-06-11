# 🎓 Campus Navigation System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python)
![AI](https://img.shields.io/badge/Artificial%20Intelligence-A*-green?style=for-the-badge)
![Graph](https://img.shields.io/badge/Graph-Based%20Navigation-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-Completed-success?style=for-the-badge)

### 🚀 Intelligent Campus Navigation Assistant

*An AI-powered system that finds the optimal route inside a university campus using A* Search Algorithm.*

</div>

---

## 📖 Abstract

The Campus Navigation System is an intelligent AI-based navigation assistant designed to help students, faculty, and visitors efficiently navigate a university campus. The system models the campus as a graph where locations such as classrooms, laboratories, libraries, cafeterias, and administrative offices are represented as nodes, while pathways connecting them are represented as edges.

Using Artificial Intelligence search techniques, the system computes optimal routes based on distance, travel time, and accessibility constraints. The project demonstrates graph-based knowledge representation, heuristic search, explainable reasoning, and performance evaluation.

---

## 🎯 Objectives

✅ Model a campus as a graph

✅ Find shortest paths between locations

✅ Apply AI search algorithms

✅ Generate explainable route traces

✅ Analyze algorithm performance

---

## 🏫 Campus Map

```text
Gate
├── Library
│   ├── Lab
│   └── Admin
│
└── Cafeteria
    └── Lab

Lab
└── Classroom

Admin
└── Classroom
```

---

## 🧠 AI Concepts Used

### CO1

* PEAS Model
* Problem Formulation
* State Space Representation
* Graph Knowledge Representation

### CO2

* BFS
* DFS
* Uniform Cost Search
* Greedy Search
* A* Search Algorithm

### CO3

* Constraint Satisfaction Concepts
* Accessibility Constraints
* Route Restrictions

### CO4

* Utility-Based Decision Making
* Optimal Route Selection

### CO5

* Probabilistic Reasoning
* Uncertainty Handling

### CO6

* Hybrid AI System
* Explainable AI
* Performance Analysis

---

## ⚙️ Technologies Used

| Technology | Purpose               |
| ---------- | --------------------- |
| Python     | Programming Language  |
| Heap Queue | Priority Queue        |
| Graphs     | Campus Representation |
| A* Search  | Path Finding          |
| GitHub     | Version Control       |

---

## 🔍 Algorithm Used

### A* Search Algorithm

The A* algorithm combines:

```text
f(n) = g(n) + h(n)
```

Where:

* g(n) = Actual path cost
* h(n) = Heuristic estimate
* f(n) = Total estimated cost

This helps find the shortest route efficiently.

---

## ▶️ Sample Output

```text
===================================
AI CAMPUS NAVIGATION SYSTEM
===================================

Enter Starting Location: Gate
Enter Destination Location: Classroom

OPTIMAL PATH FOUND

Route:
Gate -> Library -> Lab -> Classroom

Total Distance:
9

Nodes Expanded:
4
```

---

## 📊 Features

✨ Shortest Path Calculation

✨ Graph-Based Navigation

✨ Explainable Search Trace

✨ Heuristic Route Planning

✨ Performance Metrics

✨ User-Friendly Interface

---

## 📂 Project Structure

```text
Campus-Navigation-System
│
├── main.py
├── README.md
└── requirements.txt
```

---

## 🚀 How to Run

### Clone Repository

```bash
git clone https://github.com/yourusername/Campus-Navigation-System.git
```

### Run Program

```bash
python main.py
```

---

## 📸 Screenshots

Upload screenshots into a folder named **images**.

```text
Campus-Navigation-System
│
├── images
│   ├── output1.png
│   ├── output2.png
│
├── main.py
└── README.md
```

Display them using:

```markdown
## Project Output

![Output 1](images/output1.png)

![Output 2](images/output2.png)
```

---

## 👩‍💻 Project Team

* Yerrolla Eekshitha
* Team Members

---

## 📚 Course

**Course:** CFAI (Computational Foundations of Artificial Intelligence)

**Project Title:** Campus Navigation System

**Academic Year:** 2025–26

---

<div align="center">

### 🌟 Thank You 🌟

⭐ If you like this project, give it a star on GitHub ⭐

</div>
