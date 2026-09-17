# FD-181 — Sparse signed perturbations cannot hide from prime-extension multiplicativity

- **Date:** 2026-09-17
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** relational source rigidity / prime-extension ancestry / signed sparse perturbations / moving-prime robustness
- **Depends on:** FD-147, FD-175, FD-179, FD-180
- **Classification:** `EXACT-DERIVED + RELATIONAL-RIGIDITY + SIGNED-SPARSE-PERTURBATIONS + MOVING-PRIME-ROBUSTNESS + PRIME-FAN-LOWER-BOUND`

## Claim

`FD-180` showed that a deletion-only dyadic-null source with physical prime coordinates pays an exact `x/log x` prime-extension boundary. The deletion-only and fixed-prime assumptions are not needed for the coercive direction. A single signed source error emits a prime fan that survives arbitrary compensating edits and arbitrary changes of prime coordinates as long as the total set of changed coefficients is `o(x/log x)`.

Let `a` be a real-valued arithmetic source with

\[
a(1)=1,
\qquad
a(n)=0\quad\text{whenever }\mu(n)=0,
\tag{1}
\]

and write

\[
\delta(n):=a(n)-\mu(n),
\qquad
S:=\{n:\delta(n)\ne0\},
\qquad
S(x):=|S\cap[1,x]|.
\tag{2}
\]

No sign, amplitude, deletion-only, or fixed-prime restriction is imposed. Assume only

\[
\boxed{
S(x)=o(x/\log x).
}
\tag{3}
\]

On the squarefree prime-extension graph of `FD-180`,

\[
E_x:=\{(n,pn):pn\le x,\ p\text{ prime},\ p\nmid n,\ \mu^2(n)=1\},
\tag{4}
\]

define, for fixed `1<=q<infinity`, the **true multiplicativity defect energy**

\[
\mathcal M_{a,q}(x)
:=
\sum_{(n,pn)\in E_x}
|a(pn)-a(p)a(n)|^q.
\tag{5}
\]

For Möbius this vanishes identically. Define also the reciprocal perturbation mass

\[
C_{\delta,q}
:=
\sum_{n\in S}\frac{|\delta(n)|^q}{n}
\in(0,+\infty]
\tag{6}
\]

when `a!=mu`.

Then

\[
\boxed{
\liminf_{x\to\infty}
\frac{\log x}{x}\,
\mathcal M_{a,q}(x)
\ge
C_{\delta,q}.
}
\tag{7}
\]

Using the squarefree ancestry edge count from `FD-147`,

\[
|E_x|
=
\frac{x}{\zeta(2)}\log\log x+O(x),
\tag{8}
\]

we obtain

\[
\boxed{
\liminf_{x\to\infty}
(\log x\,\log\log x)^{1/q}
\left(
\frac{\mathcal M_{a,q}(x)}{|E_x|}
\right)^{1/q}
\ge
(\zeta(2)C_{\delta,q})^{1/q}.
}
\tag{9}
\]

The right-hand side is interpreted as `+infinity` if the series diverges. In particular, throughout the broad class (1)--(3),

\[
\boxed{
\left(
\frac{\mathcal M_{a,q}(x)}{|E_x|}
\right)^{1/q}
=
o\!\left((\log x\,\log\log x)^{-1/q}\right)
\quad\Longrightarrow\quad
a=\mu.
}
\tag{10}
\]

Thus the rate separator found in `FD-180` is not an artefact of deletion-only sources. It survives arbitrary signed compensations and even moving prime coordinates, and the required support hypothesis can be weakened from subpolynomial to `o(x/log x)`.

There is also a sharpness statement on the old fixed-prime fibre. If in addition

\[
a(p)=-1\quad(p\text{ prime}),
\qquad
S(x)=x^{o(1)},
\qquad
\sup_{\mu^2(n)=1}|\delta(n)|<\infty,
\tag{11}
\]

then `C_{delta,q}<infinity` and

\[
\boxed{
\mathcal M_{a,q}(x)
=
(C_{\delta,q}+o(1))\frac{x}{\log x}.
}
\tag{12}
\]

For deletion-only coefficients `|delta(n)|=1` on `S`, so (12) reduces exactly to the `FD-180` asymptotic.

## 1. One changed coordinate has an overwhelming clean prime fan

Fix `n in S`. Call a prime `p` **clean for `n` at scale `x`** when

\[
p\le x/n,
\qquad
p\nmid n,
\qquad
p\notin S,
\qquad
pn\notin S.
\tag{13}
\]

On such an edge both the extending prime and the child retain their Möbius values:

\[
a(p)=-1,
\qquad
a(pn)=\mu(pn)=-\mu(n).
\tag{14}
\]

Since `a(n)=mu(n)+delta(n)`, its true multiplicativity defect is therefore exactly

\[
a(pn)-a(p)a(n)
=
-\mu(n)+\mu(n)+\delta(n)
=
\delta(n).
\tag{15}
\]

The number of primes excluded from (13) is at most

\[
\omega(n)+S(x/n)+S(x).
\tag{16}
\]

Indeed, the first term covers `p|n`, the second covers changed prime coordinates, and the map `p -> pn` is injective, so the third covers all changed children. Hence

\[
N_n(x)
:=
\#\{p:p\text{ is clean for }n\}
\ge
\pi(x/n)-\omega(n)-S(x/n)-S(x).
\tag{17}
\]

Under (3), for every fixed `n`, the prime number theorem gives

\[
\boxed{
N_n(x)
=
(1+o_n(1))\frac{x}{n\log x}.
}
\tag{18}
\]

This is the key robustness step. To hide one fixed defect `delta(n)`, a source must corrupt essentially an entire prime fan: either move almost all extending primes or move almost all children `pn`. A global modification budget `o(x/log x)` cannot do either.

## 2. Finite collections of source errors add without cancellation

Let `F` be any finite subset of `S`. The clean edges emitted by distinct parents are distinct graph edges. By (15) and (18),

\[
\mathcal M_{a,q}(x)
\ge
\sum_{n\in F}|\delta(n)|^q N_n(x)
=
\left(
\sum_{n\in F}\frac{|\delta(n)|^q}{n}
+o_F(1)
\right)
\frac{x}{\log x}.
\tag{19}
\]

Therefore

\[
\liminf_{x\to\infty}
\frac{\log x}{x}\mathcal M_{a,q}(x)
\ge
\sum_{n\in F}\frac{|\delta(n)|^q}{n}.
\tag{20}
\]

Now exhaust `S` by finite subsets. The right-hand side increases monotonically to `C_{delta,q}`, which proves (7), including the case `C_{delta,q}=+infinity`.

There is no signed cancellation loophole here. The observable is an edgewise finite-`L^q` energy, and on every clean edge the defect is exactly the fixed parent error `delta(n)`. Compensating edits elsewhere can only remove an edge from the clean fan by spending another changed coordinate.

Equation (9) follows immediately from (7) and the ancestry edge asymptotic (8). If the normalized defect were little-`o` of the scale in (10), then the left-hand side of (9) would vanish. Hence `C_{delta,q}=0`; every summand in (6) is nonnegative, so `S` is empty and `a=mu`.

## 3. Why moving the prime coordinates does not help

The live question after `FD-180` explicitly allowed prime coordinates to move. The clean-fan argument shows why a sparse set of such changes cannot screen a defect.

Suppose, for example, that the first changed coordinate is itself a prime `r`. The edge `(1,r)` carries no information because `a(1)=1` makes the multiplicativity identity tautological there. But `r` is now a parent. For almost every clean prime `p`, the edge `(r,rp)` has defect exactly `delta(r)`. Hiding those descendants requires changing order `x/log x` primes `p` or order `x/log x` products `rp` by scale `x`.

More generally, a changed prime can corrupt many extension relations, but there are only `S(x)=o(x/log x)` changed primes available. For each fixed erroneous parent the physical primes still have density one inside its prime fan at the first-order `x/log x` scale. The same argument simultaneously handles composite perturbations and arbitrary signed amplitudes.

This clarifies the actual sparsity threshold used by the proof. `FD-180` assumed `S(x)=x^{o(1)}` because it wanted an exact global boundary asymptotic. The one-parent coercive mechanism itself only needs the changed-coordinate budget to be negligible compared with one prime fan, namely (3).

## 4. The exact fixed-prime asymptotic survives signed amplitudes

Assume now (11). Since `S(x)=x^{o(1)}`, partial summation as in `FD-180` gives

\[
\sum_{n\in S}\frac1n<\infty.
\tag{21}
\]

Boundedness of `delta` then implies `C_{delta,q}<infinity`.

Because every prime is physical, for every edge `(n,pn)` we have

\[
a(pn)-a(p)a(n)
=
\delta(pn)+\delta(n).
\tag{22}
\]

Start from the weighted outgoing-fan sum

\[
O_{\delta,q}(x)
:=
\sum_{\substack{n\in S\\n\le x/2}}
|\delta(n)|^q
\#\{p\le x/n:p\text{ prime},\ p\nmid n\}.
\tag{23}
\]

The same fixed-`M`, reciprocal-tail and `n>sqrt(x)` decomposition used in `FD-180`, now with bounded weights `|delta(n)|^q`, gives

\[
\boxed{
O_{\delta,q}(x)
=
(C_{\delta,q}+o(1))\frac{x}{\log x}.
}
\tag{24}
\]

The only discrepancy between (23) and the true energy comes from edges whose child also lies in `S`, plus incoming edges from an unchanged parent to a changed child. Their total number is at most

\[
\sum_{\substack{m\in S\\m\le x}}\omega(m)
\le
S(x)\log_2x
=x^{o(1)}.
\tag{25}
\]

All edge defects are uniformly bounded under (11), so changing the contribution on these exceptional edges costs only `x^{o(1)}=o(x/log x)`. Combining (22)--(25) proves (12).

Thus `FD-180` was already at the correct first-order scale and constant for its deletion fibre; the new point is that the same weighted reciprocal mass is the exact constant for arbitrary bounded signed perturbations when primes remain fixed, and a universal lower constant even when primes are allowed to move.

## 5. Consequence for the dyadic midpoint null sources

The permanent controls from `FD-175`--`FD-179` are much sparser than (3). They can therefore remain exactly invisible to every dyadic midpoint only by paying the relation-energy floor (9). This is now true even if the null-source construction is generalized to use signed repairs rather than deletions and to alter a sparse set of prime coordinates.

The separation is quantitative and source-class aware:

\[
\text{exact dyadic midpoint agreement}
\not\Rightarrow
\text{prime-extension consistency},
\tag{26}
\]

but within any `o(x/log x)` perturbation support,

\[
\text{prime-extension defect}
=
o((\log x\log\log x)^{-1/q})
\quad\Rightarrow\quad
a=\mu.
\tag{27}
\]

So the relational escape left open by `FD-180` is closed over a substantially larger fibre. The next source-class question is no longer whether signed compensation or sparse prime movement alone defeats the boundary. It is whether the support threshold near the size of one prime fan is sharp, and what replaces cardinal sparsity for dense but tiny-amplitude perturbations.

## 6. Stress tests and boundaries

**Internal cancellation.** Setting `delta(pn)=-delta(n)` can cancel the defect on a chosen internal edge, but doing so places `pn` in `S`. For a fixed parent, cancelling a first-order fraction of its prime fan therefore consumes a first-order `x/log x` number of changed children, excluded by (3).

**Moving primes.** Changing `a(p)` can alter every relation labelled by that prime. But screening one fixed parent requires changing almost every prime label up to `x/n`, again violating (3). A sparse set of exceptional primes only removes `o(x/log x)` edges from that fan.

**A genuinely different multiplicative source.** If one changes a prime value and then propagates the change multiplicatively to all of its squarefree multiples, the support is macroscopic rather than `o(x/log x)`. Such sources are intentionally outside the theorem. This is exactly where a distinct multiplicative source should escape a rigidity statement centered on `mu`.

**Dense tiny perturbations.** The theorem is support-sparse, not amplitude-sparse. A perturbation on many coordinates with very small `|delta(n)|` may evade the clean-fan counting argument even when an appropriate weighted norm remains small. No claim is made there.

**The support threshold.** Condition (3) is sufficient, not claimed optimal. At support size comparable to `x/log x`, a source has enough changed coordinates in principle to cover an entire prime fan. Whether an exact dyadic-null source can exploit that budget while also pushing the normalized true multiplicativity defect below the boundary scale is open.

**No RH consequence.** As in `FD-180`, this is a source-identifiability theorem. It does not supply the Franel--Landau critical discrepancy bound or transfer relation energy into that destination norm.

## Representation audit

The theorem is stated entirely in the original coefficient coordinates. The relation `a(pn)=a(p)a(n)` lives on the squarefree prime-extension graph and is not obtained by cumulative inversion, Möbius inversion, a Farey-field reconstruction, or a change of norm. The only transformed object is the finite-`L^q` aggregation of edgewise defects, whose normalization is explicit in (9).

The generic mechanism is graph-theoretic: a changed vertex in a graph with an asymptotically large labelled fan cannot be hidden by an error set smaller than that fan if clean edges expose the parent defect. The arithmetic splice is that almost all labels are physical primes, `mu(p)=-1`, `mu(pn)=-mu(n)`, and the PNT counts the surviving clean fan. The Farey-specific relevance is that `FD-175`--`FD-179` produced exactly the permanent midpoint-null sparse sources for which this cross-coordinate test supplies missing coercivity.

Crucially, the prime-extension energy remains an **additional source-faithfulness observable**. Nothing here proves that sparse Farey midpoint data, or even the full Farey field, automatically controls (5) at the required rate. Any future transfer from Farey observations to relation energy must be proved separately rather than smuggled in through the representation.

## Prior-art audit

Targeted searches were made around approximate multiplicativity, Ulam-type stability of multiplicative maps, property testing, divisibility-graph expansion, and sparse edge boundaries. These neighboring interfaces study genuine or approximate homomorphisms and divisor-graph expansion, but no direct result matching (7) for a sparse perturbation of Möbius on the prime-extension graph was found.

No new external theorem is load-bearing. The proof uses only the prime number theorem and the squarefree ancestry edge count already anchored in `SOURCES.md` and `FD-147`. No novelty is claimed for the PNT, for finite-`L^q` positivity, or for the elementary clean-fan injection. The durable Mathia contribution is the robustness statement: the exact relation-defect scale identified in `FD-180` survives signed compensations and moving primes under the much weaker support condition `S(x)=o(x/log x)`.

## Research consequence

The deletion-only restriction should be removed from the active relation-rigidity frontier. Signed edits and sparse prime-coordinate changes do not create a new escape: every fixed source error still leaks through `x/log x` clean prime extensions.

The two live questions are sharper. First, determine whether the cardinal threshold `S(x)=o(x/log x)` is close to optimal by constructing or excluding dyadic-null controls at prime-fan-scale support with subcritical relation energy. Second, and more important for the Farey program, derive a source-native bridge from Farey observations to a cross-coordinate consistency quantity such as (5), rather than imposing relation energy as an external prior.
