# Kid Hop-o Player Movement System

A selected technical overview of the Unity/C# player controller used in **Kid Hop-o: Rising Star**.

The movement stack has grown over multiple years of development and supports a momentum-focused platforming model rather than a stock character controller. A recent cleanup pass focused on clarifying ownership of movement state, documenting architecture, improving Inspector organization, and fixing integration bugs while preserving the existing game feel.

## Systems represented

- Walking, running, crouching, skidding, and ground-spin states
- Custom jump arcs and horizontal air momentum
- Variable jump behavior and fluttering
- Wall cling, wall jump, ricochet, ledge, vine, and slope interactions
- Rigidbody2D-based custom velocity control
- Animation and sprite-facing synchronization
- Designer-facing movement tuning
- Debugging and refactoring of legacy gameplay code

## Architecture

```text
Human / AI input
        ↓
PlayerMovement
        ├── locomotion & ability state
        ├── collision / environment probes
        ├── custom jump & air calculations
        ├── Rigidbody2D velocity
        └── state exposed to animation / interaction scripts
```

The controller intentionally uses direct `Rigidbody2D.velocity` control for precise arcade-platformer movement. The system also contains legacy timing and state behavior that was documented rather than aggressively rewritten so that the current gameplay feel remains stable.

## Detailed case study

For a fuller technical breakdown covering movement states, custom jump physics, environmental probes, ledge/vine interactions, cutscene movement, runtime tuning, animation integration, and refactoring lessons, see:

**[Full movement-system case study](CASE_STUDY.md)**

## Portfolio note

This documentation explains the architecture and responsibilities of the system without publishing the entire proprietary game project. The cleaned source is maintained as part of the private Kid Hop-o development repository and can be discussed in more detail during technical review or interviews.

**Project site:** https://kidhop-o.com/
