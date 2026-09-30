# Aalto / Korpi-Lagg — SOP / Cover Letter Working Points

## Core narrative
This opportunity is compelling because it recombines two trajectories that have so far developed separately:

1. **Physics:** training in Engineering Physics / Quantum Science & Technology, including statistical physics and advanced statistical physics, plus experimental research experience.
2. **Computation:** several years of performance-sensitive C/C++ engineering, including low-level optimization, SIMD/NEON, memory/cache behavior, profiling, debugging, and instruction-level analysis.

The central story should be: **I do not want to leave either trajectory behind. I want to use serious computation to investigate a fundamental physical system. This project makes advances in physical understanding and advances in computational capability mutually reinforcing.**

## 1. Why I care about the problem

### Long-term motivation
A persistent personal motivation is to work on problems that contribute to humanity's long-term capabilities and future expansion.

For this application, keep the motivation specific:
- Understanding and assessing **exoplanet habitability** is a concrete contribution to identifying planetary environments that could support life.
- Stellar magnetic activity and space-weather environments are part of determining whether apparently promising planets are actually habitable.
- Independently of the application, stellar dynamos are a compelling **fundamental-physics problem**: how nonlinear, turbulent, magnetized plasma generates coherent large-scale magnetic structure and activity.

### Important SOP discipline
Do **not** foreground alternative missions such as fusion energy or optical communications in this application. They explain my broader career reasoning, but would dilute the case for this specific project. The cover letter should make clear why *this* scientific problem is worth pursuing on its own.

## 2. My preferred research loop
This project closely matches how I naturally want to investigate physical problems:

**physical question -> model -> mathematical/computational representation -> simulate/predict -> compare with observation -> investigate mismatch -> identify mechanism or model deficiency -> refine -> probe again**

Key emphasis:
- I want **mechanistic understanding**, not merely a model that fits data.
- Simulation is a scientific experiment: alter assumptions/parameters, observe emergent behavior, compare with reality, and use discrepancies to learn physics.
- The observational constraints keep the work grounded in a real physical system rather than becoming simulation for its own sake.
- The project combines both **physics debugging** (why does the model disagree with the star?) and **computational debugging** (why is the simulation slow, unstable, inaccurate, or unable to reach the required regime?).

## 3. What I bring

### Physics foundation
- Integrated B.Tech + M.Tech from IIT Madras: Engineering Physics + Quantum Science & Technology.
- Relevant conceptual foundation includes Statistical Physics and Advanced Statistical Physics.
- Broader training includes quantum mechanics, condensed matter, optics, and related mathematical physics.
- M.Tech experimental research provides experience connecting measurements, physical models, and interpretation.

### Computational / systems foundation
- Several years of production C/C++ engineering.
- Performance-sensitive algorithm implementation.
- SIMD / ARM NEON optimization.
- Cache, memory, and low-level performance reasoning.
- Profiling and bottleneck identification.
- Reading compiler output / disassembly and reasoning at instruction level.
- Debugging complex systems.
- Familiarity with Linux, version control, build/debug workflows.

### Why this matters specifically here
The project is not merely using computation as plumbing. Its scientific reach is constrained by computational capability: high-resolution global/local MHD, GPU acceleration, radiative transfer, high-cadence extraction, and LUMI-class production runs.

Therefore my existing optimization background can become part of the scientific method: **better computational performance can enable more physical scales, longer integrations, larger parameter studies, or higher-fidelity models.**

## 4. The bridge / acknowledged knowledge gap
I have not previously specialized in stellar astrophysics, fluid dynamics, MHD, or radiative transfer. This should be acknowledged directly rather than hidden.

The transition is nevertheless intellectually coherent:

**statistical physics / collective behavior -> nonlinear multiscale plasma -> emergent macroscopic magnetic behavior**

The new foundations I would deliberately build are:
- fluid dynamics and MHD;
- numerical methods for PDEs;
- stellar/solar dynamo physics;
- radiative transfer;
- relevant computational astrophysics.

The argument is not that I already know the domain. It is that I bring a strong physics base plus an unusually relevant computational implementation background, and I am motivated to acquire the missing domain theory.

## 5. Why this project / Korpi-Lagg / Aalto
Specific features to reference:
- Fully compressible MHD of stellar dynamos.
- Simultaneous small-scale and large-scale dynamo behavior.
- Observation-constrained model selection and calibration.
- Global + local radiative MHD coupling.
- GPU acceleration and LUMI-class HPC.
- Physics-informed ML used as a scientific tool, not as the end goal.
- Connection from interior dynamo -> surface magnetic maps -> corona/winds -> exoplanet environment.
- High-Performance Computing Lab gives an unusually natural home for combining physical modelling and serious computing.

Potential central sentence/theme:
> **What attracts me particularly is that in this project, improving the physical model and improving the computational capability are coupled parts of the same scientific investigation.**

## 6. What I want to contribute / become
Near-term contribution:
- bring strong C/C++ and performance-engineering habits to scientific simulation;
- learn the MHD/numerical-physics foundations needed to contribute scientifically;
- take ownership of the model -> implementation -> simulation -> interpretation loop.

Long-term identity:
**a deep-domain physical-systems modeller who can move between theory, numerical modelling, high-performance implementation, simulation, and measurement/observation.**

## Suggested cover-letter flow
1. Opening: scientific problem + why it matters to me.
2. Why the stellar-dynamo / exoplanet-habitability question is compelling.
3. My preferred research loop and why this project matches it.
4. Physics preparation and previous research.
5. C/C++ / low-level optimization / performance-engineering experience.
6. Explicit bridge: what I know, what I need to learn, why the transition is credible.
7. Why Korpi-Lagg / HPCLab / this exact project.
8. Close with the physics + computation recombination theme.

## To develop before final draft
- Identify 1–2 concrete examples from my M.Tech research that demonstrate model/measurement iteration.
- Identify 1–2 Qualcomm examples that can be described publicly and demonstrate profiling, optimization, numerical/algorithmic debugging, or performance ownership.
- Read 2–4 recent Korpi-Lagg papers and reference one scientific question naturally.
- Inspect the group's simulation/code ecosystem enough to make the HPC fit concrete.
- Decide which public code/thesis links strengthen the application.
