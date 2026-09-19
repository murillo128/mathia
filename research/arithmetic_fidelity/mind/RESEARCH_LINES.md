# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Require finite-prefix identifiability before pricing joint pole recovery

**Linked intuitions:** `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class` and the current shell-carrier/derivative-depth intuitions.

AF-416--AF-435 separate left-tail scaling, source selection and downstream transport. AF-436 shows that the exact Euler moments `s_k=zeta(2k)` retain the full reciprocal-square shell ladder, while AF-437 shows that sequential shell peeling is exponentially ill-conditioned. AF-438 removes that representation artifact: the generating transform `F(z)=sum_(k>=1) zeta(2k) z^(k-1)=sum_(m>=1) 1/(m^2-z)` exposes all shells simultaneously.

AF-439 shows that every fixed moment depth remains locally noninjective in a nearby movable positive Stieltjes class, while AF-440 proves a complementary positive theorem on the exact reciprocal-square support with a separated finite mark alphabet: one sufficiently deep moment determines a linearly deep prefix with an explicit separation margin.

AF-441 isolates provenance as the load-bearing distinction. Small support jitter is not itself fatal when the displaced support remains explicitly marked by its realized source coordinate, whereas latent support motion restores Prony/Newton fibres. AF-442 sharpens the negative side further: **cell or shell identity alone does not rescue the single-high-moment mechanism.** A later discrete mark change can be hidden exactly by an exponentially small displacement of one earlier latent support point inside the same retained cell, with displacement scale `asymp (j/m)^(2N)/N`.

The live question is therefore no longer whether coarse cell provenance might substitute for the realized skeleton in AF-440. It cannot for the single scalar high moment. The next minimal-lift candidates must actually remove the support/mark trade: several independent moments whose Jacobian constrains the latent coordinate, a low-dimensional deformation law tying support motions together, relational support data that reconstructs the realized coordinates, or another source-derived constraint with a proved target-pure observation fibre. Only after such a structural gate passes should Padé, Stieltjes continued fractions, Hankel/Prony or another joint inverse be compared by conditioning at the shell depth consumed downstream.

## Keep source class, provenance, exact carrier, identifiability, conditioning and destination transport separate

Exact analytic continuation from the complete moment sequence is not finite-prefix recovery, and removing the AF-437 peeling cascade does not prove a stable inverse. AF-439--AF-442 now separate three materially different regimes: exact fixed support can make one high moment strongly mark-separating; marked realized support can preserve that separation under controlled jitter; but latent support can absorb a discrete mark change even when shell/cell provenance is retained.

The important quantitative warning from AF-442 is that increasing moment order has opposite effects on the two source classes. On a shared skeleton it strengthens the superincreasing mark hierarchy; with an earlier latent coordinate it makes the displacement needed to hide a later mark exponentially smaller. High order is therefore not intrinsically more faithful: its value depends on which coordinates are actually retained.

A continuation should state the admissible completion class and retained provenance explicitly, prove or refute target-purity of the finite observation fibre on that class, and only then price the inverse at the required precision and shell depth. Any proposed lift weaker than the realized support should first be tested against explicit two-coordinate compensation before being credited with arithmetic fidelity.