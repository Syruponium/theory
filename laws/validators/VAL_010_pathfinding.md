**VAL_010_PATHFINDING (Linked to LAW_010)**
| Feature | Specification | 
|--- | --- | 
| Invariant | Least Resistance Flow | 
| Never Event | Filament formation through high-viscosity (cold) zones if a low-viscosity (warm) path exists. | 
| Logic | Matrix flow is governed by hydraulic efficiency. It must prioritize the superfluid path over the rigid path. | 
| Test Condition | assert flow_path.viscosity == min(available_paths.viscosity) | 
