# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Require finite-prefix identifiability before pricing joint pole recovery

**Linked intuitions:** `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class` and the current shell-carrier/derivative-depth intuitions.

AF-416--AF-435 separate left-tail scaling, source selection and downstream transport. AF-436 shows that the exact Euler moments `s_k=zeta(2k)` retain the full reciprocal-square shell ladder, while AF-437 shows that sequential shell peeling is exponentially ill-conditioned.

AF-438 removes that particular representation artifact. The exact generating transform

`F(z)=sum_(k>=1) zeta(2k) z^(k-1)=sum_(m>=1) 1/(m^2-z)`

is a Stieltjes/Markov carrier whose poles expose all shells simultaneously with residue `-1`. Exact shell provenance is therefore present without recursive subtraction.

AF-439 moves the finite-data frontier one step earlier than conditioning. For every fixed moment depth `N`, even inside a nearby positive finite Stieltjes class with the same unit-residue normalization, there are local pole-moving fibres with exactly the same first `N` moments. The construction perturbs the constant elementary-symmetric coefficient of `N+1` positive nodes; Newton identities keep the first `N` power sums fixed while every pole moves. The perturbed nodes need not remain reciprocal integer squares, so this is a generalized-shell identifiability obstruction, not a second Riemann source.

The live question is therefore two-stage. First specify a source/tail/support class strong enough that the finite observation map is injective, or quantify the residual fibre when it is not. Only after that gate is passed does it make sense to compare Padé, Stieltjes continued fractions, Hankel/Prony or another joint inverse by condition number. A numerically stable algorithm cannot recover a pole that the admissible finite-data class does not identify.

## Keep source class, exact carrier, identifiability, conditioning and destination transport separate

Exact analytic continuation from the complete moment sequence is not finite-prefix recovery. Likewise, removing the artificial AF-437 peeling cascade does not prove that the remaining inverse is stable, and a narrow source class can restore identifiability without supplying a useful quantitative modulus.

A continuation should therefore state the admissible completion class explicitly, prove the finite-prefix map is target-pure on that class, then price the inverse at the precision and shell depth consumed downstream. Alternatively, a negative theorem may show that every source-natural class broad enough to be useful retains pole-moving fibres or an equivalent instability. Treating AF-438's exact carrier as a finite-data reconstruction theorem would skip the new AF-439 gate.