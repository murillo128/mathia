# MC-241 — Smooth-conductor cancellation forces blind support to diverge

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the `MC-238`–`MC-240` shell-character setup. Let

\[
T\subset\{r\text{ prime}:y<r\le 2y\}
\]

be the active local support of a nonprincipal character in the smooth-dilation annihilator, and let

\[
q_\chi=\prod_{r\in T}r,
\qquad
k=|T|.
\]

By `MC-239`, every blind character factors through the squarefree shell radical and its active primitive conductor has precisely this form. Blindness means

\[
\chi(p)=1
\qquad (p\le y\text{ prime}).
\tag{1}
\]

The fixed support floor `k>=7` from `MC-240` can be strengthened qualitatively:

\[
\boxed{
\text{for every fixed }K,\text{ all sufficiently large }y\text{ admit no blind character with }k\le K.
}
\tag{2}
\]

Equivalently, along any sequence of nonprincipal blind shell characters,

\[
\boxed{k(\chi)\longrightarrow\infty.}
\tag{3}
\]

For the quadratic Legendre matrix `A` of `MC-238`, this says that its binary blind sector has no bounded-weight vector asymptotically: for every fixed `K`, every sufficiently large shell matrix has

\[
Av=0,\ v\ne0
\quad\Longrightarrow\quad
\operatorname{wt}(v)>K.
\tag{4}
\]

Thus the unresolved annihilator is not merely forced beyond six shell primes. **Any surviving blind relation must couple an unbounded number of shell-prime factors.**

The input that makes `(2)` possible is the 2026 smooth-modulus character-sum theorem of Cochrane–Granville–Zheng. Its near-linear smoothness threshold crosses exactly the scaling that older Graham–Ringrose-type bounds did not uniformly cross for arbitrarily large fixed support.

No rate of divergence for `k(chi)`, no proof that the annihilator is eventually trivial, no Fourier decay on support growing with `y`, and no bound for the Möbius progression vector are claimed.

## 1. Blindness is exact on every `y`-smooth integer

From `(1)` and complete multiplicativity,

\[
\chi(n)=1
\qquad\text{whenever }P^+(n)\le y.
\tag{5}
\]

There is no conductor-zero issue on this set: every prime divisor of `q_chi` lies in `(y,2y]`, so every `y`-smooth integer is automatically coprime to `q_chi`.

This upgrades the prime-witness formulation used in `MC-240` to a full positive-density block once one looks slightly beyond `y`.

Fix

\[
1<u<\sqrt e,
\qquad
N=y^u.
\tag{6}
\]

Since `u<2`, every integer `n<=N` has at most one prime divisor greater than `y`. Hence, writing

\[
\Psi(N,y)=\#\{n\le N:P^+(n)\le y\},
\]

one has the elementary identity

\[
N-\Psi(N,y)
=
\sum_{y<p\le N}\left\lfloor\frac Np\right\rfloor.
\tag{7}
\]

Mertens' theorem for reciprocal primes gives

\[
\sum_{y<p\le y^u}\frac1p
=
\log\log(y^u)-\log\log y+o(1)
=
\log u+o(1).
\tag{8}
\]

Since `pi(N)=o(N)`, `(7)`–`(8)` yield

\[
\boxed{
\Psi(y^u,y)
=
(1-\log u+o(1))y^u.
}
\tag{9}
\]

This is the `1<u<2` Dickman law, but no Dickman machinery is needed here.

Using `(5)` on the smooth set and only `Re chi(n)>=-1` elsewhere,

\[
\begin{aligned}
\operatorname{Re}\sum_{n\le N}\chi(n)
&\ge
\Psi(N,y)-(N-\Psi(N,y))\\
&=
\bigl(1-2\log u+o(1)\bigr)N.
\end{aligned}
\tag{10}
\]

Because `u<sqrt(e)`,

\[
1-2\log u>0.
\tag{11}
\]

Therefore every blind character has a **linear-sized ordinary character sum** at the slightly super-`y` scale `N=y^u`.

## 2. Smooth shell conductors force cancellation at the same scale when support is fixed

Now suppose that `k>=2` is fixed. Then

\[
y^k<q_\chi\le(2y)^k.
\tag{12}
\]

Choose fixed positive numbers `tau,epsilon` sufficiently small that

\[
(1+\tau)(1+\epsilon)<u.
\tag{13}
\]

Set

\[
\delta=\frac{1+\tau}{k},
\qquad
Y=q_\chi^\delta.
\tag{14}
\]

For large `y`, `(12)` gives

\[
Y\ge y^{1+\tau}>2y.
\tag{15}
\]

Hence every prime factor of `q_chi` is at most `Y`; in the notation of Cochrane–Granville–Zheng, the squarefree conductor belongs to their smooth-modulus class `N(Y)`. Their fixed exceptional integer `mathcal M` is harmless here because all prime factors of `q_chi` tend to infinity, so `(q_chi,mathcal M)=1` eventually.

On the other hand,

\[
Y^{1+\epsilon}
\le
(2y)^{(1+\tau)(1+\epsilon)}
<y^u=N
\tag{16}
\]

for sufficiently large `y`, by `(13)`. Also `N<q_chi` for every fixed `k>=2`, because `u<2<=k`.

Theorem 1 / Corollary 2 of Cochrane–Granville–Zheng, specialized to `f(x)=x` and `g(x)=0`, therefore supplies an `eta=eta(delta,epsilon)>0` such that every nonprincipal primitive character of conductor `q_chi` satisfies

\[
\boxed{
\left|\sum_{n\le N}\chi(n)\right|
\ll
\frac{N}{q_\chi^\eta}
=o(N).
}
\tag{17}
\]

This contradicts the positive linear lower bound `(10)`.

Thus no fixed `k>=2` can occur for arbitrarily large `y`. The already established one-prime and bounded-small-support exclusions in `MC-239`–`MC-240` cover the remaining trivial initial cases, proving `(2)`–`(3)`.

## 3. Why the 2026 smoothness threshold changes the frontier

The source theorem is tailored to exactly the shape of the shell conductor. Cochrane–Granville–Zheng prove power cancellation on intervals of length `N` once the modulus is smooth essentially up to

\[
P^+(q)\le N^{1-\epsilon}.
\tag{18}
\]

For the shell conductor with fixed support,

\[
P^+(q_\chi)\asymp y,
\qquad
q_\chi\asymp y^k,
\qquad
N=y^u=q_\chi^{u/k+o(1)}.
\tag{19}
\]

Condition `(18)` becomes, at exponent level,

\[
1<u(1-\epsilon),
\tag{20}
\]

which is compatible with every `u>1`. This leaves room to choose simultaneously `u<sqrt(e)`, where the smooth integers occupy more than half of `[1,N]` and force `(10)`.

The paper explicitly contrasts this near-linear smoothness threshold with the older Graham–Ringrose theorem, where an admissible modulus-smoothness exponent was much smaller, of order `Delta^2` when the interval length is `q^Delta`. In the shell scaling `Delta=u/k`, a quadratic-in-`Delta` smoothness threshold does not uniformly dominate the shell factor exponent `1/k` as fixed `k` grows. The new linear-scale threshold does. That is the precise reason the literature upgrade converts the numerical floor of `MC-240` into the unbounded-support statement `(3)`.

## 4. Consequence for the exact `MC-238` annihilator

`MC-238` identifies every residue-only smooth-dilation blind mode with a nonprincipal character trivial on the small-prime subgroup. `MC-239` removes prime-square local kernel and all single-shell-factor obstructions. `MC-240` then proves support at least seven by a generic least-prime-character-witness theorem.

The present result closes the entire **bounded-support** version of that escape. A future annihilator argument cannot gain anything by testing more elaborate relations involving a fixed number of shell primes: any such family disappears once `y` is large enough.

What remains is genuinely collective. Since a full shell has order `y/log y` primes, `(3)` still permits support growing arbitrarily slowly with `y`; the current theorem is not uniform enough in the smoothness parameter `delta~1/k` to exclude such relations. Nor does it imply that an unbounded-support annihilator mode has a large coefficient against the Möbius progression vector. The live gate is therefore narrowed to:

- quantitative character-sum control with `delta -> 0` fast enough to track growing shell support; or
- a source-specific argument showing that any surviving high-support character couples weakly to the exact progression/dilation vector even if the abstract annihilator is nontrivial.

This is a strict frontier improvement over `MC-240`: bounded cross-shell compatibility is no longer a live obstruction.

## 5. Prior art and novelty audit

Todd Cochrane, Andrew Granville and Junren Zheng, *Mixed incomplete character sums of rational functions with smooth moduli*, arXiv:`2601.10927` (submitted 16 January 2026), Theorem 1 and Corollary 2, prove power-saving incomplete character-sum bounds for nonprincipal characters to moduli smooth at essentially the `N^(1-epsilon)` scale. Their introduction records the older Graham–Ringrose `q`-analogue van der Corput theorem and explains that its admissible smoothness exponent is much smaller than the interval exponent. The character-sum estimate itself is literature, not a Mathia result.

The reciprocal-prime asymptotic used in `(8)` is classical Mertens theory and is already anchored in `MC-S6`. The smooth-density lower bound `(9)` is the elementary `1<u<2` specialization of the classical Dickman–de Bruijn law.

Least-character-nonresidue arguments that combine a region on which `chi=1` with character-sum cancellation are classical; `MC-240` already uses Pollack's Burgess/Norton/smooth-number implementation of that paradigm. The durable Mathia delta here is narrower and source-specific: applying the 2026 near-linear smooth-modulus theorem to the exact shell-radical conductors from `MC-239` shows that **no bounded number of shell primes can support an `MC-238` blind character**. No claim of novelty is made for the general analytic-number-theory ingredients or for the abstract implication from a suitable smooth-modulus bound.

## Boundaries

- `(3)` is qualitative. It supplies no explicit function `k(y)->infinity`.
- The theorem does not prove `H_y(Q_S)=G_S`; high-support blind characters remain possible.
- The argument uses fixed `k` before taking `y->infinity`. It must not be read as uniform in growing `k`.
- No assumption about RH, GRH, or zeta zero-free regions enters the proof.
- No estimate for `B_S(X)`, `M(X)`, an individual Möbius progression, or the zeta zero set follows directly.
- The result concerns the abstract annihilator of the smooth-dilation residue orbit. It does not assert that every surviving high-support mode is dynamically relevant to the Möbius coefficients.
