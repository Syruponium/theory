**VAL_006_COUPLING (Linked to LAW_006)**
| Feature | Specification | 
|---|---|
 | Invariant,Momentum Synchronization | 
 | Never Event | Persistent slip (friction) in the superfluid phase. | 
 | Logic | "In the superfluid phase (T>13.84K), matter must lock to the Matrix flow perfectly. Any delta in velocity over time is a violation." | 
 | Test Condition | if T > 13.84: assert particle.v == matrix.v | 
