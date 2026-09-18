# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Push source-side rigidity into weighted amplitude stability, then expose it from Farey observations

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-030-sub-square-root-farey-bands-remain-noninjective-under-coordinatewise-mobius-fidelity`.

The observation geometry is sharply source-class relative. Complete Farey fields and consecutive midpoint histories are exactly invertible over unrestricted formal sources. Sparse geometric horizons become target-rigid inside the bounded squarefree multiplicative cone, while FD-175--FD-179 construct permanent deletion-only controls that match every dyadic midpoint despite agreeing with Möbius through essentially the whole squarefree-rank range.

Prime-extension energy is now the exact source-side relation currency. For a squarefree-supported source `a`, put `delta=a-mu` and `M_(a,q)(x)=sum_((n,pn) in E_x) |a(pn)-a(p)a(n)|^q`. FD-182 shows that the complete dyadic midpoint ladder cannot control this relation below its critical `x/log x` scale on the broad null-source class.

Inside the physical-prime fibre `a(p)=-1`, FD-187 identifies the exact finite certificate behind the relation rigidity. If `n_0` is a changed squarefree composite, `k=omega(n_0)` and `Delta=|a(n_0)-mu(n_0)|`, every fresh prime generates a translated divisor cube; its exact `q`-capacity shows that subcritical `M_(a,q)=o(x/log x)` is fully rigid on the physical-prime fibre.

FD-188 removes support cardinality from the complementary moved-prime problem. With coefficient amplitude mass

`D_(a,q)(x)=sum_(n<=x, mu^2(n)=1) |a(n)-mu(n)|^q`,

subcritical relation energy forces positive linear coefficient mass for every nonzero prime error. Together FD-187--FD-188 give the support-free classification

`D_(a,q)(x)=o(x)` and `M_(a,q)(x)=o(x/log x)  =>  a=mu`.

FD-189 makes one important observation-side threshold exact over unrestricted formal sources. At a dyadic horizon `H=2^m`, the signed Farey Fourier modes through `k<=H^alpha` are, after divisor Möbius inversion, exactly the quotient samples `A(floor(H/k))`. Across all dyadic horizons these bands recover every sufficiently large source coordinate if `alpha>1/2`; at and below the square-root endpoint, infinitely many formal cumulative coordinates remain unsampled.

FD-190 now shows that the sub-square-root obstruction is not an artefact of wildly nonphysical formal increments. For every fixed `alpha<1/2`, the complete quotient coverage in `[N,2N]` is only `O(N^(alpha/(1-alpha)))=o(N)`. Some unsampled corridor therefore contains polynomially many composite squarefree coordinates, yielding a polynomial-dimensional exact nullspace even after fixing every prime, every nonsquarefree coefficient and every Möbius sign. In particular a source can differ from Möbius at only two composite squarefree coordinates, with `D_q=O(1)`, and still have exactly the same complete dyadic signed low-band history.

Thus coordinatewise arithmetic fidelity does **not** lower the power-law barrier below square root. The endpoint `alpha=1/2` remains genuinely open for the squarefree/prime-faithful sign class: FD-189 gives formal Mersenne holes there, but FD-190's zero-density corridor argument loses its margin exactly at the endpoint. Any strict sub-square-root improvement must instead use cross-coordinate information such as multiplicativity, divisor compatibility or prime-extension consistency, or change the observation family.

The high-value observation frontier is therefore split cleanly. Over the unrestricted formal source class, super-square-root signed spatial data is complete and square-root data is not. Over coordinatewise Möbius-faithful squarefree classes, every strict sub-square-root band is still noninjective arbitrarily close to Möbius. The next exact observation question is whether the critical endpoint itself becomes injective under those restrictions; the more structural question is whether a genuinely thinner relation-sensitive Farey statistic can control the exact `D_q` and `M_q` currencies without reconstructing the whole source.

A secondary source-side question remains whether the explicit moved-prime constants are globally sharp for prescribed nonzero `a(p)`, where simultaneous multiplicative consistency may impose more cost than the isolated-edge convex relaxation. Inside the genuinely multiplicative cone, the finite certification bound for geometric ladders also remains quantitatively crude.

## Apply information budgets only after fixing source class, observation family and destination

The same Farey representation can be complete, sparse-target-rigid, or permanently noninjective depending on the source class and the observation family. FD-189--FD-190 sharpen this distinction: a growing signed Fourier band has a square-root scale-coverage transition, and below that transition even strong coordinatewise Möbius fidelity leaves a large exact kernel. Sample count by itself is not the invariant; what matters is which source indices the quotient geometry reaches and whether the admissible class couples them.

Any lower bound should therefore first declare whether it concerns unrestricted recovery, one-target testing, pairwise recovery or quotient recovery; whether changing horizon counts as a new operator; the source class and which coordinates are fixed or allowed to move; the relation graph and normalization; the observation/noise topology; and whether support cardinality, weighted amplitude mass or scale coverage is the relevant fidelity currency. Only then do rank, bandwidth, inverse modulus, support cardinality or information capacity become meaningful.

## Keep source coercivity and the Franel--Landau destination separate

FD-187--FD-190 are source-recovery, source-rigidity or observation-identifiability theorems. They do not prove the RH-critical discrepancy estimate. In particular, super-square-root dyadic signed-band recovery says that the formal source can be reconstructed; it does not improve the Franel--Landau norm or supply a cancellation mechanism at the critical exponent.

Conversely, the source-side results are now exact enough to state what a successful richer observation theorem must do: expose the right coefficient/relation currencies with a useful modulus, or exploit physical multiplicativity strongly enough to cross the coordinatewise square-root observation barrier, and only then connect that information to the nonlocal discrepancy destination.
