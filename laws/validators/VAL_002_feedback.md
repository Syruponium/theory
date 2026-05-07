| Feature | Specification |
| ------------- | ------------- |
| Invariant | Elastic Response
| Never Event= | Global pressure drop during local mass injection.
| Logic, | Every new particle must exert an outward pressure on the Matrix. A pressure drop during mass creation violates the Elastic Feedback principle.
| Test Condition | assert delta_P_global >= 0 if delta_M > 0
