# FD-172 — Dyadic midpoint sensing rigidifies bounded squarefree multiplicative sources

- **Date:** 2026-09-17
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** restricted temporal acquisition / multiplicative positivity / dyadic target-rigidity / stability
- **Depends on:** FD-117, FD-166, FD-170, FD-171
- **Classification:** `EXACT-DERIVED + SOURCE-RESTRICTED + DYADIC-ACQUISITION + POSITIVITY + TARGET-RIGIDITY`

## Claim

`FD-171` shows that midpoint-only temporal sensing has zero exact redundancy over the unrestricted normalized arithmetic-source space: omit one horizon and an explicit permanent pulse-pair perturbation survives. That obstruction disappears sharply once the source is required to retain a substantial part of the Möbius architecture.

Let `a` be multiplicative and satisfy

\[
a(1)=1,
\qquad
a(p^r)=0\quad(r\ge2),
\qquad
-1\le a(p)\le1\quad(p\text{ prime}).
\tag{1}
\]

Thus `a` is squarefree-supported, multiplicative, and has prime amplitudes on the Möbius scale; Möbius is the special point `a(p)=-1` for every prime.

Write

\[
P_a(H):=\mathcal D_{H,a}(1/2),
\qquad
E_H:=P_a(H)-P_\mu(H).
\tag{2}
\]

Then

\[
\boxed{
P_a(2^m)=P_\mu(2^m)\ \text{for every }m\ge1
\quad\Longrightarrow\quad
a=\mu.
}
\tag{3}
\]

More locally, exact agreement at the dyadic horizons through `2^M` forces

\[
\boxed{
a(n)=\mu(n)\qquad(1\le n\le2^M).}
\tag{4}
\]

There is also a quantitative one-sided stability statement. If

\[
|E_{2^m}|\le\varepsilon
\qquad(m\ge1),
\tag{5}
\]

then every prime satisfies

\[
\boxed{0\le1+a(p)\le2\varepsilon.}
\tag{6}
\]

If additionally `epsilon<=1/2`, then for every squarefree `n`,

\[
|a(n)-\mu(n)|
\le
2\varepsilon\,\omega(n),
\tag{7}
\]

while both sides vanish on nonsquarefree `n`.

The key point is not dyadic arithmetic by itself. In the midpoint convolution coordinates of `FD-170`, the restrictions (1) turn every prime defect away from Möbius into **nonnegative mass**. Dyadic horizons then cover all primes by multiplicative annuli `(H/2,H]`, so that mass cannot hide by the pulse cancellation used in `FD-171`.

## 1. The midpoint transform becomes positive on odd integers

Let

\[
u(n):=1_{2\nmid n},
\qquad
F:=u*a.
\tag{8}
\]

`FD-170` gives

\[
E_H-E_{H-1}
=-\frac12\bigl(u*(a-\mu)\bigr)(H).
\tag{9}
\]

Since

\[
u*\mu=\varepsilon-e_2,
\tag{10}
\]

the cumulative Möbius transform has total sum zero through every horizon `H>=2`. Summing (9) therefore yields the particularly simple identity

\[
\boxed{
E_H=-\frac12\sum_{n\le H}F(n)
\qquad(H\ge2).
}
\tag{11}
\]

The source restrictions are transparent in Euler-factor coordinates. At the prime `2`, the odd-indicator has trivial local factor, so

\[
F_2(x)=1+a(2)x.
\tag{12}
\]

For an odd prime `p`,

\[
F_p(x)
=\frac{1+a(p)x}{1-x}
=1+(1+a(p))(x+x^2+x^3+\cdots).
\tag{13}
\]

Consequently, for odd `m`,

\[
\boxed{
F(m)=\prod_{p\mid m}(1+a(p))\ge0.
}
\tag{14}
\]

The value depends only on the set of odd prime divisors, not on their exponents. In particular,

\[
F(p^j)=1+a(p)\ge0
\qquad(p\text{ odd},\ j\ge1).
\tag{15}
\]

This is exactly what the unrestricted pulse construction of `FD-171` lacks: after imposing squarefree multiplicativity and the lower prime-amplitude bound, the transformed defect can no longer create an arbitrary signed pulse followed by a compensating pulse.

## 2. Each midpoint horizon measures a nonnegative multiplicative annulus

Define the odd transformed prefix

\[
A(x):=\sum_{\substack{m\le x\\m\text{ odd}}}F(m).
\tag{16}
\]

Because `F(2m)=a(2)F(m)` for odd `m` and `F(n)=0` when `4|n`, equation (11) becomes

\[
-2E_H
=A(H)+a(2)A(H/2).
\tag{17}
\]

Rewrite this as

\[
\boxed{
-2E_H
=\bigl(A(H)-A(H/2)\bigr)
 +(1+a(2))A(H/2).
}
\tag{18}
\]

Every term on the right is nonnegative by (1) and (14). Hence

\[
E_H\le0
\qquad(H\ge2).
\tag{19}
\]

At `H=2`, equation (18) gives

\[
-2E_2=1+a(2).
\tag{20}
\]

For any odd prime `p` lying in the top multiplicative annulus

\[
H/2<p\le H,
\tag{21}
\]

the first term in (18) contains `F(p)=1+a(p)`. Therefore

\[
\boxed{
0\le1+a(p)\le-2E_H.
}
\tag{22}
\]

This is the whole rigidity mechanism: a prime defect is a positive witness in every observed annulus that contains that prime, and all other admissible source contributions have the same sign after the midpoint transform.

## 3. Dyadic horizons cover every prime defect

For an odd prime `p`, choose

\[
H(p):=2^{\lceil\log_2 p\rceil}.
\tag{23}
\]

Because an odd prime is never a power of two,

\[
H(p)/2<p<H(p).
\tag{24}
\]

Thus (22) applies at the single dyadic horizon `H(p)`. If all dyadic midpoint values agree with Möbius, then (20) first gives `a(2)=-1`, and (22) gives

\[
a(p)=-1
\tag{25}
\]

for every odd prime. Multiplicativity and squarefree support then imply `a=mu`, proving (3).

The same argument is finite. If the dyadic observations agree through `2^M`, every prime `p<=2^M` is covered by one of the annuli attached to `2,4,...,2^M`, hence has `a(p)=-1`. Every integer `n<=2^M` factors only through those primes, so (4) follows.

Under the approximate hypothesis (5), (20) and (22) instead give (6). For squarefree `n` with `k=omega(n)`, write `delta_p:=1+a(p)`. When `epsilon<=1/2`, `0<=delta_p<=2epsilon<=1` and

\[
a(n)
=\mu(n)\prod_{p\mid n}(1-\delta_p).
\tag{26}
\]

Therefore

\[
|a(n)-\mu(n)|
=1-\prod_{p\mid n}(1-\delta_p)
\le\sum_{p\mid n}\delta_p
\le2\varepsilon\omega(n),
\tag{27}
\]

which proves (7).

So the sparse temporal compression is strong but very specific: only `O(log X)` dyadic midpoint horizons are needed to certify equality with the Möbius target through source scale `X` inside the class (1). This is **target-rigidity**, not pairwise injectivity of the dyadic observation map on all admissible sources.

## 4. Why this does not contradict FD-171

`FD-171` is a linear statement over the full normalized arithmetic-source space. Its invisible direction

\[
\delta a_k=\mu_{\rm odd}*(e_k-e_{k+1})
\tag{28}
\]

uses exactly the signed freedom that the present source class removes. In the transformed coordinate `F=u*a`, multiplicativity plus squarefree support forces each odd Euler factor to have coefficient `1+a(p)` at every positive prime power, while `a(p)>=-1` forces those coefficients to be nonnegative. The isolated positive/negative temporal pulse needed for (28) is therefore not admissible.

The distinction is also one between general source recovery and a source-specific null test. The dyadic measurements need not distinguish two arbitrary members of (1): subtracting two admissible multiplicative sources does not preserve the positivity argument. What they do is distinguish the Möbius point from every other member of the class. That is the relevant statement for testing whether source-faithful restrictions can destroy the `FD-171` kernel, but it should not be advertised as a full sparse inversion theorem.

The upper bound `a(p)<=1` is likewise not load-bearing for the exact positivity proof; it keeps the admissible class on the natural Möbius coefficient scale. The argument itself only needs squarefree multiplicativity and `a(p)>=-1`. Multiplicativity and the lower bound are load-bearing: without them, signed transformed mass can return and the one-hole pulse geometry of `FD-171` is no longer excluded.

## 5. Representation audit, prior art, and dependency ledger

The strongest baseline is `FD-171`: over unrestricted formal sources, midpoint sensing is injective only when every horizon is retained. The present result deliberately stays in the **same midpoint convolution representation** rather than changing observables. The new ingredient is to intersect that representation with a Möbius-like nonlinear source class. In those coordinates the arithmetic restriction becomes the positive local factor (13), turning a temporal cancellation problem into a multiplicative-annulus positivity problem.

The generic layer is elementary: a nonnegative defect measure cannot be invisible to a family of annuli that covers every possible defect location. Dyadic intervals `(2^(m-1),2^m]` are merely a canonical multiplicative cover. The source-specific layer is the exact Farey midpoint identity of `FD-170` together with the Euler-factor consequence of squarefree multiplicativity: a prime deviation `1+a(p)` reappears with one sign in `u*a` and therefore cannot be canceled inside its detecting annulus.

A focused prior-art search around Farey midpoints, dyadic horizons, Möbius inversion and multiplicative sources recovered the standard midpoint/Farey symmetry and standard Dirichlet-convolution machinery, but no direct statement of this dyadic target-rigidity mechanism. No external theorem is load-bearing: the proof uses only the exact internal identity from `FD-170`, Euler-factor multiplication, positivity and dyadic covering. `SOURCES.md` therefore needs no update.

The main falsifiers are explicit. Dropping multiplicativity, allowing prime amplitudes below `-1`, or asking for pairwise injectivity rather than rigidity relative to Möbius can restore cancellation and is not covered by the theorem. Nor does (3) provide new Möbius cancellation, control the Franel--Landau norm, or move the RH-critical destination estimate.

Dependency ledger: `FD-117` supplies the source-controlled Farey framework; `FD-166` is the complete-field permanent-source comparison; `FD-170` supplies the midpoint convolution identity; and `FD-171` is the unrestricted sparse-acquisition obstruction that this restricted theorem crosses. No accepted clue changes status.

## Research consequence

The source-faithful-restriction branch opened by `FD-171` is no longer purely hypothetical. Exact squarefree multiplicativity plus the natural prime-amplitude lower bound destroys the pulse-pair kernel strongly enough that **dyadic**, rather than consecutive, midpoint horizons certify the Möbius target. The approximate version also gives a direct prime-defect modulus.

The next useful boundary is therefore to weaken the source architecture rather than to add denser time samples immediately. In particular: determine whether squarefree ternary sources without multiplicativity still admit permanent sparse-time null directions; characterize which multiplicative-gap conditions on a horizon set suffice for Möbius target-rigidity; and separate target-rigidity from genuine pairwise sparse inversion. Mixed sparse-time/local-space acquisition remains the parallel route once these source restrictions are fixed.

## Related findings

- `FD-166` — any unbounded family of exact complete fields rigidifies a permanent source to Möbius.
- `FD-170` — consecutive midpoint horizons give exact inversion through the odd-indicator convolution.
- `FD-171` — unrestricted midpoint sensing has an exact permanent null direction for every omitted horizon.
