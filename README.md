# Smart Traffic Signal Optimization System

A Python-based simulation designed to dynamically allocate traffic signal timings and determine signal order at a four-way intersection (North, South, East, West). 

Unlike traditional fixed-timer traffic lights, this system calculates real-time priority scores based on vehicle density, waiting time, and emergency vehicle presence to reduce overall traffic delay and gridlock.

---

## Features

* **Dynamic Green-Light Allocation:** Allocates signal duration dynamically from a total cycle pool (120s) based on real-time traffic demand.
* **Emergency Vehicle Override:** Automatically boosts the priority score of any direction with an active emergency vehicle, prioritizing it to receive a green light first.
* **Fairness Base Guarantee:** Reserves a minimum green-light time (10 seconds) for all directions so low-traffic roads are never neglected.
* **Congestion Detection:** Identifies bottleneck roads based on vehicle count or wait time thresholds and displays a `congested` alert.
* **Performance Comparison:** Computes and compares total wait delays between a traditional fixed-timer system (30s per lane) and the optimized dynamic system.
* **Robust Input Validation:** Prevents crashes by validating numerical ranges and handling invalid string inputs safely.
* **Simulation Loop:** Allows users to run multiple traffic scenarios sequentially without re-executing the script.

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
\text{Green Time} = 10 + \left( \frac{\text{Direction Priority}}{\text{Total Intersection Priority}} \times 80 \right)
```

### 3. Congestion Thresholds
A road is flagged as **`congested`** if:
* Vehicles > 20
 OR
* text > 60 sec

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
[Performance Engine]► Compares delay reductions against fixed 30s timers
       │
[Report Output] ────► Displays order, scores, statuses, and % improvement