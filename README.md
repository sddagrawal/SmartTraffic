# Smart Traffic Signal Optimization System

A Python-based simulation designed to dynamically allocate traffic signal timings and determine signal order at a four-way intersection i.e. North, South, East and West. 

Unlike usual fixed-timer traffic lights, this system calculates real-time priority scores based on vehicle density, waiting time, and emergency vehicle presence to reduce overall traffic delay and gridlock.

---

## Features
* **Dynamic Green-Light Allocation:** Allocates signal duration dynamically from a total 
cycle pool of 120 sec based on real-time traffic demand.
* **Emergency Vehicle Override:** Automatically boosts the priority score of any direction with an active emergency vehicle, prioritizing it to receive a green light first.
* **Fairness Base Guarantee:** Reserves a minimum green-light time for 10 seconds for all directions so low-traffic roads are never neglected.
* **Congestion Detection:** Identifies bottleneck roads based on vehicle count or wait time thresholds and displays a `congested` alert.
* **Performance Comparison:** Computes and compares total wait delays between a old fixed-timer system that is uaually 30s per lane and the optimized dynamic system.
* **Robust Input Validation:** Prevents crashes by validating numerical ranges and handling invalid string inputs safely.
* **Simulation Loop:** Allows users to run multiple traffic scenarios sequentially without re-executing the script again and again.

---

## Technical Concepts Used

This project is built using core Python without external libraries:
* **Dictionaries & Lists:** For storing structured traffic data per direction.
* **Functions & Algorithms:** Modular code for data processing, scoring, allocation, and comparison.
* **Lambda Functions:** For custom sorting based on priority score evaluation.
* **Exception Handling (`try-except`):** Ensures resilient user input processing.
* **Loops & Conditionals:** For control flow, simulation repetition, and edge-case branching.

---

## Algorithm Working

### 1. Priority Score Formula
Priority Score = (Vehicles x 2) + (Wait Time x 0.5) + Emergency Bonus

* **Vehicles (x2):** Heavily weights traffic volume to clear dense lanes.
* **Wait Time (x0.5):** Prevents starvation by gradually increasing score as vehicles wait longer.
* **Emergency Bonus (+100):** Grants immediate top-priority status to emergency vehicles.

### 2. Dynamic Time Allocation
* **Total Cycle Pool:** 120 seconds
* **Minimum Guaranteed Time:** 10 seconds per direction 
* **Remaining Dynamic Pool:** 120 - 40 = 80

```math
Green Time = 10s + [ (Direction Priority / Total Priority) × 80s ]
```

### 3. Congestion Thresholds
A road is flagged as **`congested`** if:
* Vehicles > 20
 OR
* wait time > 60 sec

Otherwise, status is marked **`normal`**.

---

## Project Structure & Workflow

```text
[Input Module] ────► Collects vehicles, wait times, and emergency presence
       │
[Scoring & Logic] ──► Calculates priority scores and checks congestion status
       │
[Scheduler] ────────► Sorts directions using lambda (highest priority first)
       │
[Allocator] ────────► Distributes the 120s green-light pool proportionally
       │
[Performance Engine] ──────► Compares delay reductions against fixed 30s timers
       │
[Report Output] ────► Displays order, scores, statuses, and % improvement
```

---

## Setup and Execution

### prerequisite

before running this project, following must be installed:

* Python 3.12.0
* Visual Studio Code (recommended)
* Git (for cloning repository from GitHub)

### 1. Clone the Repository
open terminal and run:
```bash
git clone
https://github.com/sddagrawal/SmartTraffic
```
after cloning, into project folder:
```bash
cd SmartTraffic
```
(skip if repository has already been downloaded)


### 2. Environmental Setup
python 3.12.0 or later is required to run this project

### 3. Dependency Installation
No external dependencies. 
All functionality is impemented using inbuilt python function

### 4. Configuration
No additional configuration or API keys, Database, or external services required.

### 5.Run the Program
In VS Code terminal inproject folder, run:
```bash
py main.py
```
The program will ask user to enter traffic information for four directions

