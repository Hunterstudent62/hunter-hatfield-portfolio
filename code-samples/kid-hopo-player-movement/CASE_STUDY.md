## Kid Hop-o Player Movement System

**Unity / C# / Rigidbody2D / Custom Platformer Physics**

I developed the player movement controller for *Kid Hop-o: Rising Star*, a platformer/RPG that combines traditional character movement with momentum-based traversal, aerial abilities, environmental interactions, and scripted cutscene movement.

Rather than relying primarily on Unity's built-in forces, the controller calculates the player's desired velocity and applies it through `Rigidbody2D`. Unity handles collision resolution while the movement code controls the game-specific behavior needed for responsive platforming.

### System Architecture

```text
Player Input ─────┐
                  │
Cutscene Movebot ─┴──> PlayerMovement
                         │
                         ├── Ground / Wall / Ceiling Detection
                         ├── Walking / Running / Skidding
                         ├── Custom Jump Physics
                         ├── Air Momentum
                         ├── Spin / Flutter / Wall Interaction
                         ├── Ledge / Vine Interaction
                         │
                         ▼
                    Rigidbody2D
                         │
                         ▼
                   Unity Physics
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
       PlayerAnimation        Visual Effects
```

`PlayerMovement` acts as the authoritative gameplay controller. Other systems either provide information to it or read its resulting state.

### Movement State Design

The controller uses a hybrid state system.

Major locomotion modes describe the basic type of movement being performed:

```text
Idle
Walk
Run
Skid
Crouch
Air
```

Additional substates can overlap with these modes to support more complex abilities:

```text
Ground Spin
Aerial Spin / Double Jump
Flutter
Wall Cling
Ledge Grab
Vine Hang
Sliding
Run Deceleration
```

This lets an airborne character, for example, remain in the general Air state while separately tracking whether the player is spinning, fluttering, wall-jumping, or interacting with a ledge.

### Custom Jump Physics

Jumping uses custom horizontal and vertical velocity values rather than depending entirely on Unity gravity.

Simplified pseudocode:

```text
when jump begins:
    verticalVelocity = baseJumpStrength
    horizontalMomentum = currentGroundMomentum

while airborne:
    if jump button is held:
        apply normal gravity
    else:
        apply stronger gravity to shorten the jump

    apply player air control
    clamp horizontal momentum

    rigidbody.velocity =
        (horizontalMomentum, verticalVelocity)
```

This allows:

- Variable jump height based on button hold time
- Preservation of running momentum when jumping
- Midair steering
- Maximum air-speed limits
- Different air control during spin and flutter states
- Custom falling acceleration

### Momentum and Ground Movement

The original controller uses direct velocity control with custom acceleration/deceleration behavior rather than purely force-driven physics.

Running, skidding, spinning, and releasing movement input modify working speed values over time. This creates momentum-like behavior while retaining precise platformer control.

The system is being extended toward a more continuous momentum model where:

```text
player input
    +
acceleration
    +
friction
    +
terrain slope
    =
current ground speed
```

Ground speed can then determine both physical movement and animation state, allowing the character to naturally transition from walking to running as speed increases.

### Environmental Detection

The controller uses dedicated physics probes rather than depending exclusively on collision callbacks.

```text
Ground Probe   -> Is the player supported?
Wall Probes    -> Is movement blocked horizontally?
Ceiling Probe  -> Did the player hit overhead terrain?
Slope Probe    -> Is the player interacting with angled terrain?
```

These checks use Unity `Physics2D` overlap tests with dedicated layer masks.

This provides more explicit control over platforming behavior such as:

- Walking off ledges
- Landing
- Ceiling collisions
- Wall stopping
- Wall interaction
- Slope behavior

### Ledges and Vines

Environmental interaction objects communicate with the main movement controller rather than implementing independent player physics.

Simplified flow:

```text
Ledge detects valid player overlap
        ↓
requests ledge grab
        ↓
PlayerMovement enters ledge state
        ↓
velocity is suspended
        ↓
player can hang, drop, or interact with a vine
```

Moving and stationary vines use the same general interaction system, with additional handling for hanging and downward sliding.

### Gameplay-Accurate Cutscene Movement

Cutscenes can take control of the same movement system through a lightweight synthetic-input controller.

Instead of directly moving the player's Transform:

```text
cutscene:
    "move right"
        ↓
PlayerMovement receives simulated Right input
        ↓
normal acceleration, collision, animation,
and platforming rules still apply
```

This allows scripted movement to visually match normal gameplay rather than looking like the character is being manually translated through the scene.

### Runtime Movement Tuning

I also created a developer-facing movement tuning menu that allows major controller parameters to be modified while the game is running.

Adjustable parameters include:

- Base walking speed
- Running speed
- Skid behavior
- Ground-spin speed
- Jump strength
- Gravity
- Ricochet jump strength
- Double-jump height
- Wall-jump height
- Flutter duration
- Maximum air momentum
- Normal air control
- Spin/flutter air control

This allows movement feel to be tested rapidly without repeatedly editing constants and recompiling the game.

### Animation Integration

Movement and animation are separated into different responsibilities.

```text
PlayerMovement
    ↓ exposes gameplay state

PlayerAnimation
    ↓ translates state

Unity Animator
```

Animation selection can therefore react to physical state rather than controlling the underlying movement itself.

For the newer momentum-based movement design, locomotion animation can also be driven by actual speed:

```text
0 speed
    -> Idle

low / medium speed
    -> Walk / Jog

high speed
    -> Run
```

Animation playback speed can increase alongside physical velocity to make acceleration visually readable.

### Engineering Lessons and Refactoring

The controller began as one of my earliest substantial gameplay programming systems and expanded as additional mechanics were added.

As the system grew, I identified several areas for architectural improvement:

- Separating visual facing direction from gameplay-facing state
- Reducing cross-script state modification
- Centralizing ledge transitions inside the movement controller
- Caching component references
- Separating tuning values from runtime movement values
- Improving input capture
- Organizing movement states and transition bookkeeping
- Replacing binary slope detection with surface-normal based terrain information
- Moving toward continuous momentum rather than fixed walk/run velocity modes

Rather than replacing functioning gameplay wholesale, I have been refactoring the controller incrementally so established movement behavior can be preserved while the architecture becomes easier to extend and maintain.

### Current / Planned Movement Features

**Implemented**
- Walking and running
- Skidding
- Variable-height jumping
- Ground momentum carried into jumps
- Air steering
- Double jump / spin slash
- Fluttering
- Ground spin
- Wall interaction
- Ledge grabbing
- Static and moving vine interaction
- Rope/vine sliding
- Cutscene-driven movement
- Runtime movement tuning

**In Development**
- Continuous acceleration-based movement
- Speed-driven walk/run animation transitions
- Surface-normal slope physics
- Momentum-based rolling
- Improved movement-state organization
- Unlockable instant-dash behavior
