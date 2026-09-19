# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Require finite-prefix identifiability before pricing joint pole recovery

**Linked intuitions:** `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class` and the current shell-carrier/derivative-depth intuitions.

AF-416--AF-435 separate left-tail scaling, source selection and downstream transport. AF-436 shows that the exact Euler moments `s_k=zeta(2k)` retain the full reciprocal-square shell ladder, while AF-437 shows that sequential shell peeling is exponentially ill-conditioned. AF-438 removes that representation artifact: the generating transform `F(z)=sum_(k>=1) zeta(2k) z^(k-1)=sum_(m>=1) 1/(m^2-z)` exposes all shells simultaneously.

AF-439 shows that every fixed moment depth remains locally noninjective in a nearby movable positive Stieltjes class, while AF-440 proves a complementary positive theorem on the exact reciprocal-square support with a separated finite mark alphabet: one sufficiently deep moment determines a linearly deep prefix with an explicit separation margin.

AF-441 now isolates the load-bearing distinction more sharply. Small support jitter is not itself fatal when the displaced support remains **marked by source provenance**: under the finding's exact separation hypotheses, the first differing mark is still recoverable to linear depth. But if the same finite support is allowed to move latently and only an unmarked finite moment prefix is observed, Newton/Prony fibres again give local nonidentifiability. Full support provenance is sufficient, though not claimed minimal.

The live question is therefore to identify the **minimal provenance lift** that keeps finite observation fibres target-pure under realistic support uncertainty: cell or interval identity, order plus separation, a low-dimensional deformation law, or another canonical source-derived label. Only after that structural gate is passed should Padé, Stieltjes continued fractions, Hankel/Prony or another joint inverse be compared by conditioning at the shell depth consumed downstream.

## Keep source class, provenance, exact carrier, identifiability, conditioning and destination transport separate

Exact analytic continuation from the complete moment sequence is not finite-prefix recovery, and removing the AF-437 peeling cascade does not prove a stable inverse. AF-439--AF-441 show that support uncertainty has two mathematically different forms: **marked deformation can preserve fidelity, while latent deformation restores fibres**. Treating “jitter” as one scalar noise parameter erases the source information doing the work.

A continuation should state the admissible completion class and retained provenance explicitly, prove or refute target-purity of the finite observation fibre on that class, and then price the inverse at the required precision and shell depth. The highest-value boundary is no longer simply rigid versus movable support, but how little source identity can be retained while still excluding the latent Prony fibre.