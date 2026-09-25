# Testing

## Test Case 1 — Normal Traffic

### Input

| Direction | Vehicles | Wait Time | Emergency |
|---|---:|---:|---|
| North | 10 | 20 | No |
| South | 12 | 25 | No |
| East | 8 | 15 | No |
| West | 15 | 30 | No |

### Expected Result

- No emergency priority should be applied.
- Signal order should be based on calculated priority.
- Green time should be distributed according to priority.
- The system should generate a final performance report.

---

## Test Case 2 — Emergency Vehicle

### Input

| Direction | Vehicles | Wait Time | Emergency |
|---|---:|---:|---|
| North | 10 | 20 | No |
| South | 8 | 15 | No |
| East | 12 | 25 | Yes |
| West | 15 | 30 | No |

### Expected Result

- East receives an emergency priority bonus.
- East should receive a significantly higher priority score.
- The signal schedule should reflect the emergency condition.

---

## Test Case 3 — Congestion Detection

### Input

| Direction | Vehicles | Wait Time | Emergency |
|---|---:|---:|---|
| North | 25 | 40 | No |
| South | 10 | 20 | No |
| East | 8 | 15 | No |
| West | 12 | 30 | No |

### Expected Result

North should be identified as `congested` because the vehicle count exceeds 20.

---

## Test Case 4 — Input Validation

### Input

Enter invalid values such as:

- Non-numeric vehicle count
- Non-numeric waiting time
- Invalid emergency response such as `maybe`

### Expected Result

The program should reject the invalid input and ask the user to enter a valid value.

---

## Test Case 5 — Multiple Simulations

### Input

Run one traffic scenario and select `yes` when asked whether to run another simulation.

### Expected Result

The program should accept a new traffic scenario without restarting the Python program.