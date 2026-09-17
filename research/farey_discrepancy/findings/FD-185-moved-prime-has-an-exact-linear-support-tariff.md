# FD-185 — A moved prime has an exact linear support tariff

- **Date:** 2026-09-17
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** relational source rigidity / moved-prime support tariff / prime-label matching / sharp multiplicative control
- **Depends on:** FD-181, FD-184
- **Classification:** `EXACT-DERIVED + RELATIONAL-RIGIDITY + MOVED-PRIME-LINEAR-TARIFF + SHARP-CONTROL`

## Claim

`FD-181` treated moving prime coordinates robustly but its clean-parent argument only exposed the `x/log x` fan emitted by one changed coordinate. For a changed **prime** this is not the dominant geometry. The same prime labels a positive-density matching of the squarefree extension graph, so moving that label while keeping relation energy subcritical forces a **linear** set of coefficient changes.

Let `a` be a real-valued arithmetic source with

\[
a(1)=1,
\qquad
a(n)=0\quad\text{whenever }\mu(n)=0,
\tag{1}
\]

and put

\[
\delta(n):=a(n)-\mu(n),
\qquad
S:=\{n:\delta(n)\ne0\},
\qquad
S(x):=|S\cap[1,x]|.
\tag{2}
\]

For fixed `1<=q<infinity`, retain the prime-extension energy

\[
\mathcal M_{a,q}(x)
:=
\sum_{(n,rn)\in E_x}
|a(rn)-a(r)a(n)|^q,
\tag{3}
\]

where

\[
E_x:=\{(n,rn):rn\le x,\ r\text{ prime},\ r\nmid n,\ \mu^2(n)=1\}.
\tag{4}
\]

Fix a prime `p` with

\[
\Delta_p:=|\delta(p)|=|a(p)+1|>0.
\tag{5}
\]

Then, uniformly as `x -> infinity` with `p` fixed,

\[
\boxed{
S(x)
\ge
\frac{x}{\zeta(2)(p+1)}
-
\frac{\mathcal M_{a,q}(x)}{\Delta_p^q}
+
O_p(\sqrt x).
}
\tag{6}
\]

Consequently the subcritical relation-energy hypothesis

\[
\mathcal M_{a,q}(x)=o(x/\log x)
\tag{7}
\]

forces

\[
\boxed{
\liminf_{x\to\infty}\frac{S(x)}x
\ge
\frac1{\zeta(2)(p+1)}.
}
\tag{8}
\]

In fact `o(x)` energy already suffices for (8). Thus **any moved prime is incompatible with sublinear perturbation support** once prime-extension energy is sublinear, a fortiori at the `FD-181` subcritical scale.

The constant is sharp, even with zero relation energy. For every prime `p` and every real `gamma!=-1`, define the squarefree multiplicative source

\[
a_{p,\gamma}(n)
=
\begin{cases}
0,&\mu(n)=0,\\
\mu(n),&\mu^2(n)=1,\ p\nmid n,\\
\gamma\,\mu(n/p),&\mu^2(n)=1,\ p\mid n.
\end{cases}
\tag{9}
\]

Then `a_(p,gamma)(p)=gamma`, the source is multiplicative on coprime squarefree factors, and

\[
\boxed{
\mathcal M_{a_{p,\gamma},q}(x)=0
\quad\text{for every }x.
}
\tag{10}
\]

Its changed support is exactly the squarefree multiples of `p`, so

\[
\boxed{
S_{p,\gamma}(x)
=
\frac{x}{\zeta(2)(p+1)}+O_p(\sqrt x).
}
\tag{11}
\]

Therefore the linear tariff in (8), including its leading constant for one prescribed moved prime, cannot be improved under relation energy alone.

A useful global corollary combines this with `FD-184`. If

\[
S(x)=o(x),
\qquad
\mathcal M_{a,q}(x)=o(x/\log x),
\tag{12}
\]

then every prime coordinate is automatically physical:

\[
a(p)=-1\qquad(p\text{ prime}).
\tag{13}
\]

Hence, if `a!=mu` and `n_0=min S`, the all-fixed-rank theorem `FD-184` applies without assuming (13) separately. For every fixed integer `r>=1`,

\[
\boxed{
S(x)
\ge
\left(
\frac1{n_0(r-1)!}+o(1)
\right)
\frac{x(\log\log x)^{r-1}}{\log x}.
}
\tag{14}
\]

Equivalently, for every fixed real `A>=0`,

\[
\boxed{
\frac{S(x)\log x}{x(\log\log x)^A}\longrightarrow\infty.
}
\tag{15}
\]

Thus the earlier moving-prime `x/log x` support frontier is not sharp inside the sublinear-support regime. A genuinely moved-prime, subcritical-energy escape must already pay positive-density support; every sublinear-support escape reduces to the physical-prime fibre and inherits the full `FD-184` fixed-rank tariff.

## 1. A fixed prime labels a matching of positive density

Fix `p` and consider only the edges in (4) labelled by that prime:

\[
E_{p,x}
:=
\{(n,pn):n\le x/p,\ \mu^2(n)=1,\ p\nmid n\}.
\tag{16}
\]

This is a matching. A squarefree integer not divisible by `p` can occur as the parent of at most one `p`-edge, and a squarefree integer divisible by `p` can occur as the child of exactly the edge obtained by removing `p`; no vertex is an endpoint of two distinct edges in `E_(p,x)`.

Let

\[
Q_p(X)
:=
\#\{n\le X:\mu^2(n)=1,\ p\nmid n\}.
\tag{17}
\]

The standard squarefree inclusion-exclusion gives, for fixed `p`,

\[
\begin{aligned}
Q_p(X)
&=
\sum_{\substack{d\le\sqrt X\\p\nmid d}}
\mu(d)
\left(
\left\lfloor\frac{X}{d^2}\right\rfloor
-
\left\lfloor\frac{X}{pd^2}\right\rfloor
\right)\\
&=
X\left(1-\frac1p\right)
\sum_{\substack{d\ge1\\p\nmid d}}\frac{\mu(d)}{d^2}
+O_p(\sqrt X)\\
&=
\frac{p}{(p+1)\zeta(2)}X+O_p(\sqrt X).
\end{aligned}
\tag{18}
\]

Putting `X=x/p` yields

\[
\boxed{
|E_{p,x}|
=
\frac{x}{\zeta(2)(p+1)}+O_p(\sqrt x).
}
\tag{19}
\]

The scale is linear, not prime-fan scale. This is the extra incidence information that the parent-based proof of `FD-181` deliberately did not exploit.

## 2. Every clean labelled edge exposes the moved prime with full amplitude

Call an edge `(n,pn) in E_(p,x)` clean when neither endpoint belongs to `S`. On a clean edge,

\[
a(n)=\mu(n),
\qquad
a(pn)=\mu(pn)=-\mu(n).
\tag{20}
\]

Since `a(p)=-1+delta(p)`, its multiplicativity defect is exactly

\[
\begin{aligned}
a(pn)-a(p)a(n)
&=-\mu(n)-(-1+\delta(p))\mu(n)\\
&=-\delta(p)\mu(n),
\end{aligned}
\tag{21}
\]

and therefore has absolute value `Delta_p`.

Because `E_(p,x)` is a matching, one changed coordinate can contaminate at most one of these labelled edges. Hence the number of clean `p`-edges is at least

\[
|E_{p,x}|-S(x).
\tag{22}
\]

If the right-hand side is negative, replace it by zero. Positivity of the energy gives

\[
\mathcal M_{a,q}(x)
\ge
\Delta_p^q\max\{|E_{p,x}|-S(x),0\}.
\tag{23}
\]

In either case,

\[
S(x)
\ge
|E_{p,x}|-
\frac{\mathcal M_{a,q}(x)}{\Delta_p^q}.
\tag{24}
\]

Combining (19) and (24) proves (6), and (7) immediately gives (8).

This proof uses neither a sign condition nor a lower bound on any composite perturbation. The moved prime itself supplies a fixed defect amplitude, while matching geometry prevents one changed composite from screening multiple edges with the same prime label.

## 3. The lower bound is attained by exact multiplicative propagation

For the source (9), prime values are

\[
a_{p,\gamma}(p)=\gamma,
\qquad
a_{p,\gamma}(r)=-1\quad(r\ne p\text{ prime}).
\tag{25}
\]

On squarefree integers the value is the product of its prime-coordinate values. Therefore whenever `r` is prime, `r\nmid n`, and `mu^2(n)=1`,

\[
a_{p,\gamma}(rn)=a_{p,\gamma}(r)a_{p,\gamma}(n).
\tag{26}
\]

Every summand in (3) vanishes, proving (10).

The source differs from Möbius exactly when the squarefree argument contains `p`. The map `m -> pm` identifies that support up to `x` with squarefree `m<=x/p` avoiding `p`. Thus

\[
S_{p,\gamma}(x)=Q_p(x/p),
\tag{27}
\]

and (11) follows from (18). The matching lower bound is therefore not merely of the right order: its leading density is exactly realized by a zero-energy source.

This also explains the geometry. Relation energy cannot distinguish Möbius from another exactly multiplicative squarefree source; moving one prime coordinate changes one whole codimension-one Boolean face of squarefree integers. The support price of exact consistency is precisely the density of that face.

## 4. Stress tests and boundaries

**The theorem does not force a moved prime back to `-1` without a support condition.** The control (9) has zero energy and a moved prime, so relation energy alone cannot identify the prime values. What it forces is the exact support tariff needed to propagate that move consistently.

**The linear conclusion is specific to moving a prime label.** A changed composite is a parent of a prime fan of size only `asymp x/log x`; it does not label a positive-density matching. That is why `FD-181` and the fixed-prime propagation of `FD-184` remain necessary for composite seeds.

**Large moved primes still have positive but small density cost.** The constant `1/(zeta(2)(p+1))` depends on the fixed moved prime. Since every nonempty set of moved primes has a least element, any fixed source with at least one moved prime still pays a positive asymptotic density. No uniform positive constant over all possible sources is claimed.

**Several moved primes can only increase the structural obligations, but no multi-prime optimal density is claimed here.** The one-prime theorem is sufficient to rule out all prime movement under `S(x)=o(x)`. Exact optimization for a prescribed finite or infinite set of moved primes is a different Boolean-face union problem.

**Squarefree support is retained.** This matches the source class of `FD-181`--`FD-184`. Values on nonsquarefree coordinates are not needed by the edge set (4), but relaxing that source convention is not part of this claim.

**The source-side/observation-side boundary is unchanged.** No Farey spatial observable appears in the proof. `FD-182` still shows that exact dyadic midpoint data alone do not control the relation energy at the required rate. The result sharpens what subcritical relation energy would imply if some independent Farey-to-relation bridge were found.

**No RH consequence follows.** The theorem is a rigidity statement for an augmented source observable, not an estimate of Franel--Landau discrepancy.

## Representation audit

The argument stays entirely in the original arithmetic coefficient coordinates and the prime-extension graph already used by `FD-181`--`FD-184`. No cumulative inversion, adaptive basis, spectral weighting, or source-dependent reconstruction is introduced.

The generic mechanism is elementary matching rigidity: a global parameter attached to every edge of a matching cannot move by a fixed amount while almost all endpoints remain unchanged and the total nonnegative edge defect is sublinear. The arithmetic splice is that a fixed prime `p` labels a positive-density matching of squarefree integers, whose density is `1/(zeta(2)(p+1))`, and Möbius has the exact edge law `mu(pn)=-mu(n)`.

The information deliberately discarded is all Farey geometry and all edges with labels different from the selected moved prime. The sharpness control shows that nothing stronger can be extracted from this one labelled face plus relation energy alone.

## Prior-art audit

The load-bearing ingredients are elementary: squarefree inclusion-exclusion and the matching identity (21). The squarefree density is already within the line's anchored classical squarefree-counting input; no new external theorem is required.

A targeted literature search was made for stability of multiplicative arithmetic functions under approximate multiplicativity, property testing of multiplicativity, and expansion/divisibility graphs. The closest serious neighbor remains Helfgott--Radziwiłł, *Expansion, divisibility and parity* (arXiv:2103.06853), which studies a different prime-divisibility graph with additive moves `n -> n +/- p` when `p|n` and proves local spectral expansion almost everywhere. General approximate-homomorphism literature likewise concerns group-averaged multiplicative laws rather than this deterministic squarefree prime-extension matching with support cost measured against Möbius.

No direct prior-art match was found for the sharp labelled-prime support inequality (6) or its exact one-prime multiplicative saturator (9). This is not a claim of global novelty; the Mathia-specific contribution is the identification of the moved-prime face as the missing linear-scale branch in the `FD-181` relation-energy frontier.

Because no new external theorem is load-bearing, `SOURCES.md` requires no change.

## Research consequence

The moving-prime branch left after `FD-181` is now sharply separated from the fixed-prime growing-rank branch. At subcritical relation energy, **moving even one prime costs positive-density support**, and that linear scale is exactly attainable by multiplicatively propagating the changed prime through its squarefree face.

Therefore every non-Möbius source with sublinear support and subcritical relation energy automatically has physical prime coordinates and falls under `FD-184`. In that regime the source tariff already beats `x(log log x)^A/log x` for every fixed `A`; the unresolved question is only whether the fixed-prime growing-rank bootstrap can be made uniform enough to approach linear support, not whether moving primes can realize an `x/log x` escape.

The observation-side frontier remains separate: a useful Farey theorem would still need to control prime-extension relation energy from a source-native spatial statistic, and `FD-182` rules out obtaining that control from the exact dyadic midpoint ladder alone on the broad null-source fibre.
