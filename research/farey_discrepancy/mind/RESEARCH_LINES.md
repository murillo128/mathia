# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Push source-side rigidity into weighted amplitude stability, then expose it from Farey observations

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-029-dyadic-signed-fourier-recovery-has-a-sharp-square-root-bandwidth-threshold`.

The observation geometry is sharply source-class relative. Complete Farey fields and consecutive midpoint histories are exactly invertible over unrestricted formal sources. Sparse geometric horizons become target-rigid inside the bounded squarefree multiplicative cone, while FD-175--FD-179 construct permanent deletion-only controls that match every dyadic midpoint despite agreeing with Möbius through essentially the whole squarefree-rank range.

Prime-extension energy is now the exact source-side relation currency. For a squarefree-supported source `a`, put `delta=a-mu` and `M_(a,q)(x)=sum_((n,pn) in E_x) |a(pn)-a(p)a(n)|^q`. FD-182 shows that the complete dyadic midpoint ladder cannot control this relation below its critical `x/log x` scale on the broad null-source class.

Inside the physical-prime fibre `a(p)=-1`, FD-187 identifies the exact finite certificate behind the relation rigidity. If `n_0` is a changed squarefree composite, `k=omega(n_0)` and `Delta=|a(n_0)-mu(n_0)|`, every fresh prime generates a translated divisor cube; its exact `q`-capacity shows that subcritical `M_(a,q)=o(x/log x)` is fully rigid on the physical-prime fibre.

FD-188 removes support cardinality from the complementary moved-prime problem. With coefficient amplitude mass

`D_(a,q)(x)=sum_(n<=x, mu^2(n)=1) |a(n)-mu(n)|^q`,

subcritical relation energy forces positive linear coefficient mass for every nonzero prime error. Together FD-187--FD-188 give the support-free classification

`D_(a,q)(x)=o(x)` and `M_(a,q)(x)=o(x/log x)  =>  a=mu`.

FD-189 now makes one important observation-side threshold exact over unrestricted formal sources. At a dyadic horizon `H=2^m`, the signed Farey Fourier modes through `k<=H^alpha` are, after divisor Möbius inversion, exactly the quotient samples `A(floor(H/k))`. Across all dyadic horizons these bands recover every sufficiently large source coordinate if and only if `alpha>1/2`. At and below the square-root endpoint, infinitely many Mersenne indices `2^r-1` are never sampled and support explicit formal-source null perturbations.

Thus a full signed dyadic band has a sharp square-root recovery transition: super-square-root bandwidth is tail-injective, while square-root and sub-square-root bands retain an infinite kernel. This does not contradict the midpoint null-source results; the signed band retains many coordinates that scalar midpoint observations discard.

The high-value observation frontier is therefore split cleanly. Over the unrestricted formal source class, merely repackaging signed dyadic Fourier data cannot beat the square-root bandwidth threshold. A genuinely sparser route must either exploit physical squarefree/multiplicative admissibility or use a different statistic. On the physical source class, the open question is whether those constraints lower the effective threshold and, more importantly, whether the recovered information quantitatively controls enough of the exact `D_q` and `M_q` currencies to reach the Franel--Landau destination.

A secondary source-side question remains whether the explicit moved-prime constants are globally sharp for prescribed nonzero `a(p)`, where simultaneous multiplicative consistency may impose more cost than the isolated-edge convex relaxation. Inside the genuinely multiplicative cone, the finite certification bound for geometric ladders also remains quantitatively crude.

## Apply information budgets only after fixing source class, observation family and destination

The same Farey representation can be complete, sparse-target-rigid, or permanently noninjective depending on the source class and the observation family. FD-189 adds another exact distinction: a growing signed Fourier band has a sharp scale-coverage threshold even before multiplicative structure is invoked. Sample count by itself is not the invariant; what matters is which source indices the quotient geometry actually reaches.

Any lower bound should therefore first declare whether it concerns unrestricted recovery, one-target testing, pairwise recovery or quotient recovery; whether changing horizon counts as a new operator; the source class and which coordinates are fixed or allowed to move; the relation graph and normalization; the observation/noise topology; and whether support cardinality, weighted amplitude mass or scale coverage is the relevant fidelity currency. Only then do rank, bandwidth, inverse modulus, support cardinality or information capacity become meaningful.

## Keep source coercivity and the Franel--Landau destination separate

FD-187--FD-189 are source-recovery or source-rigidity theorems. They do not prove the RH-critical discrepancy estimate. In particular, super-square-root dyadic signed-band recovery says that the formal source can be reconstructed; it does not improve the Franel--Landau norm or supply a cancellation mechanism at the critical exponent.

Conversely, the source-side results are now exact enough to state what a successful richer observation theorem must do: expose the right coefficient/relation currencies with a useful modulus, or exploit physical multiplicativity strongly enough to cross the formal square-root observation barrier, and only then connect that information to the nonlocal discrepancy destination.
