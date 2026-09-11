# MC-229 — High first-shell incidence is support-harmless above the one-quarter multiplicity threshold

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the first square-defect shell of `MC-209` and `MC-221`--`MC-228`. Fix

\[
0<c<\frac12,
\qquad
y=c\log X,
\qquad
P=\prod_{p\le y}p,
\qquad
T=X-P,
\]

and let

\[
\mathcal D_y=\{d:\ y<d\le2y,\ d\text{ prime}\},
\qquad
\mathcal R_d=\{n\le T:(n,P)=1,\ n\equiv-P\pmod{d^2}\}.
\]

For a rough input `n`, define its shell-incidence multiplicity

\[
r_y(n):=\#\{d\in\mathcal D_y:d^2\mid n+P\}.
\tag{1}
\]

Thus `r_y(n)` counts how many first-shell coordinates receive the same integer input. `MC-228` analyzed only the extreme event `r_y(n)=|\mathcal D_y|`, the full CRT common block. The whole high-incidence tail admits a uniform support bound.

For fixed `0<\alpha<c`, put

\[
r_\alpha(X):=
\left\lceil
\alpha\frac{\log X}{\log\log X}
\right\rceil
\tag{2}
\]

and

\[
E_{\ge\alpha}(X)
:=
\{n\le T:(n,P)=1,\ r_y(n)\ge r_\alpha(X)\}.
\tag{3}
\]

Then

\[
\boxed{
|E_{\ge\alpha}(X)|
\le X^{1-2\alpha+o(1)}.
}
\tag{4}
\]

This estimate uses no Möbius cancellation. Consequently, if

\[
A_d^{\ge\alpha}(T)
:=
\sum_{n\in\mathcal R_d\cap E_{\ge\alpha}(X)}\mu(n)
\tag{5}
\]

and

\[
W_y^{\ge\alpha}(X)
:=
\sum_{d\in\mathcal D_y}d\,|A_d^{\ge\alpha}(T)|^2,
\tag{6}
\]

then

\[
\boxed{
W_y^{\ge\alpha}(X)
\le X^{2-4\alpha+o(1)}.
}
\tag{7}
\]

Hence every fixed `c>1/4` has a support-only high-incidence cutoff at

\[
\boxed{
r_*(X)=
\left\lceil
\frac14\frac{\log X}{\log\log X}
\right\rceil:
\qquad
W_y^{\ge1/4}(X)\le X^{1+o(1)}.
}
\tag{8}
\]

For any fixed `\alpha>1/4` with `\alpha<c`, the high-incidence tail is even power-saving relative to the diagonal target:

\[
W_y^{\ge\alpha}(X)
\le X^{1-4(\alpha-1/4)+o(1)}.
\tag{9}
\]

Equivalently, since

\[
|\mathcal D_y|
=(c+o(1))\frac{\log X}{\log\log X},
\tag{10}
\]

when `c>1/4` all inputs shared by at least the asymptotic fraction

\[
\frac{1}{4c}+o(1)
\tag{11}
\]

of the shell coordinates can be separated and bounded by cardinality without losing the target power.

This sharply localizes the unresolved source coupling left by `MC-228`. The full common intersection is only the top incidence level. In the entire regime `c>1/4`, **every sufficiently high multiplicity level is already harmless before using signs**. Any polynomial excess above the diagonal scale must therefore be carried by incidence below `\frac14\frac{\log X}{\log\log X}`, or by coherent interference between such lower-multiplicity pieces.

No estimate for the low-incidence energy is proved. No improved bound for `W_y`, `M(X)`, or the zeta zero set follows by itself.

## 1. Every partial intersection is one CRT progression

Let `S\subseteq\mathcal D_y` be nonempty and define

\[
Q_S:=\prod_{d\in S}d^2.
\tag{12}
\]

The moduli `d^2` are pairwise coprime and are also coprime to `P`. Therefore simultaneous membership in the selected residue classes gives

\[
n\equiv-P\pmod{Q_S}.
\tag{13}
\]

Writing `n=kQ_S-P`, the conditions `1\le n\le T=X-P` are exactly

\[
\frac{P}{Q_S}<k\le\frac{X}{Q_S}.
\tag{14}
\]

Moreover, because `(Q_S,P)=1`,

\[
(n,P)=1
\iff
(kQ_S,P)=1
\iff
(k,P)=1.
\tag{15}
\]

Thus one has the exact partial-intersection identity

\[
\boxed{
\bigcap_{d\in S}\mathcal R_d
=
\left\{
 kQ_S-P:
 \frac{P}{Q_S}<k\le\frac{X}{Q_S},
 \ (k,P)=1
\right\}.
}
\tag{16}
\]

In particular,

\[
\left|\bigcap_{d\in S}\mathcal R_d\right|
\le\frac{X}{Q_S}.
\tag{17}
\]

Unlike the full-shell formula in `MC-228`, `(16)` remains valid even when `Q_S<P`; only the lower endpoint for `k` changes. This is important for mesoscopic incidence levels.

## 2. A factorial-moment union bound gives the multiplicity tail

Let

\[
m_y:=|\mathcal D_y|.
\tag{18}
\]

If `r_y(n)\ge r`, then there is at least one `r`-element subset `S\subseteq\mathcal D_y` for which

\[
n\in\bigcap_{d\in S}\mathcal R_d.
\]

Therefore, for every integer `1\le r\le m_y`, the elementary union bound and `(17)` give

\[
\#\{n\le T:(n,P)=1,\ r_y(n)\ge r\}
\le
\sum_{\substack{S\subseteq\mathcal D_y\\|S|=r}}
\frac{X}{Q_S}.
\tag{19}
\]

Since every `d\in\mathcal D_y` satisfies `d>y`,

\[
Q_S>y^{2r},
\]

so

\[
\boxed{
\#\{n\le T:(n,P)=1,\ r_y(n)\ge r\}
\le
\binom{m_y}{r}\frac{X}{y^{2r}}.
}
\tag{20}
\]

This is the only counting input needed below. It is deliberately one-sided: points of incidence larger than `r` are counted many times. That overcount is harmless for the power boundary.

## 3. Mesoscopic incidence has an exact power scale

The prime number theorem on the fixed dyadic interval gives

\[
m_y
=\pi(2y)-\pi(y)
=(1+o(1))\frac{y}{\log y}
=(c+o(1))\frac{\log X}{\log\log X}.
\tag{21}
\]

For `r=r_\alpha(X)` with fixed `0<\alpha<c`, one therefore has `r\le m_y` for all sufficiently large `X`. Also

\[
\binom{m_y}{r}
\le2^{m_y}
=
\exp\!\left(O\!\left(\frac{\log X}{\log\log X}\right)\right)
=X^{o(1)}.
\tag{22}
\]

Since

\[
\log y
=\log\log X+O(1),
\tag{23}
\]

we have

\[
y^{2r_\alpha(X)}
=
\exp\!\left(2r_\alpha(X)\log y\right)
=X^{2\alpha+o(1)}.
\tag{24}
\]

Substituting `(22)` and `(24)` into `(20)` proves `(4)`.

This calculation exposes the origin of the exponent. Each additional shared shell coordinate imposes one further square divisibility condition and therefore costs approximately `(\log X)^2` in support density. Accumulating `\alpha\log X/\log\log X` such conditions costs the fixed power `X^{2\alpha+o(1)}`. The combinatorial choice of which shell primes are shared contributes only `X^{o(1)}`.

## 4. Support alone kills the high-incidence energy

Let

\[
N_\alpha(X):=|E_{\ge\alpha}(X)|.
\]

For every shell prime `d`, trivially

\[
|A_d^{\ge\alpha}(T)|
\le N_\alpha(X).
\tag{25}
\]

Furthermore

\[
H_y:=\sum_{d\in\mathcal D_y}d
\le2y\,m_y
=X^{o(1)}.
\tag{26}
\]

Hence `(4)` gives

\[
W_y^{\ge\alpha}(X)
\le H_y N_\alpha(X)^2
\le X^{2-4\alpha+o(1)},
\tag{27}
\]

which is `(7)`. The target energy scale from `MC-209` is `X^{1+o(1)}`; equating powers in `(27)` gives

\[
2-4\alpha=1,
\]

so the support transition is exactly

\[
\alpha=\frac14.
\tag{28}
\]

For fixed `c>1/4`, the threshold `r_*(X)` in `(8)` lies strictly below the total shell size `(21)`, so the decomposition is nonempty and valid. Splitting

\[
A_d(T)=A_d^{<1/4}(T)+A_d^{\ge1/4}(T),
\tag{29}
\]

one has

\[
|A_d|^2
\le2|A_d^{<1/4}|^2+2|A_d^{\ge1/4}|^2.
\tag{30}
\]

Thus the high-incidence tail can genuinely be removed from the hard part of the energy problem at no polynomial cost. A proof of diagonal-scale control for the complementary low-incidence piece would automatically recover the same scale for the full shell.

## 5. Relation to the current first-shell frontier

`MC-228` found the exact full-shell intersection and its `c=1/4` support boundary. The present result explains why that same fraction appears more generally. The full intersection corresponds to `\alpha=c`, since its multiplicity is `m_y=(c+o(1))\log X/\log\log X`; substituting `\alpha=c` into `(7)` reproduces the support exponent `X^{2-4c+o(1)}` from `MC-228`.

The new content is that the full common block is not exceptional. Every incidence threshold `\alpha` has the same power law, and the whole tail above `\alpha=1/4` is support-harmless. In particular, when `c>1/4`, the search for a source-coupled gain should not spend effort on the largest overlaps: those can already be separated safely.

This narrows the candidate left by the final paragraph of `MC-228`. If a useful orthogonal, martingale-like, or incidence decomposition exists, the genuinely hard range is

\[
1\le r_y(n)
<
\left(\frac14+o(1)\right)
\frac{\log X}{\log\log X},
\tag{31}
\]

where support cardinality alone permits a super-diagonal contribution. The unresolved mechanism must extract signed cancellation, cross-slice anti-alignment, or additional arithmetic sparsity there.

The result also clarifies the `c\le1/4` regime. Then the entire shell has only

\[
m_y\le\left(\frac14+o(1)\right)
\frac{\log X}{\log\log X},
\]

so there is no nontrivial high-incidence tail beyond the support threshold. This is consistent with `MC-228`: even the full common block then cannot be declared harmless by support alone.

## 6. Prior art and novelty boundary

The mechanisms used here are classical: the Chinese remainder theorem, prime counting in a dyadic interval, and a union bound over subsets of simultaneously imposed square divisibility conditions. The estimate `(20)` is a factorial-moment/sieve-style tail bound in elementary form. General sieve and additive-function literature contains much stronger machinery for counting integers with many divisibility conditions, so no novelty is claimed for the counting method or for high-divisibility tails as an abstract theme.

A targeted prior-art search around square-divisor counts, sieve large deviations, and factorial-moment bounds found established adjacent literature on square-free sieves and large deviations, but no reason to treat `(20)` as a new theorem. The durable line-specific delta is instead the composition with the source-selected first-shell geometry already fixed by `MC-209`--`MC-228`: the mesoscopic incidence variable has a clean power scale `X^{1-2\alpha+o(1)}`, and its separately controlled weighted energy crosses the exact diagonal power at `\alpha=1/4`.

## 7. Boundaries and falsification tests

- The result controls only the **high-incidence component** defined by `(3)`--`(6)`. It is not a bound for the full `W_y` and does not estimate the low-incidence component.
- The tail estimate is support-only and intentionally ignores Möbius signs. It therefore cannot establish any new cancellation in `M(X)`.
- The fixed-`\alpha` asymptotic requires `0<\alpha<c`. At the endpoint `\alpha=c`, the full-shell calculation of `MC-228` is the appropriate exact treatment; the upper-bound exponent remains consistent by continuity.
- Equation `(30)` shows that separating the high-incidence tail is safe for an upper-bound proof, but it says nothing about potentially useful cancellation between the high- and low-incidence pieces. Discarding that interference may lose constants or subpower factors, just not a fixed power once `\alpha\ge1/4`.
- The exponent `1/4` depends on the square-modulus shell and on the quadratic energy `\sum d|A_d|^2`. Changing the divisor power, shell width, or energy weight changes the calibration and must be recomputed.
- The binomial factor is only `X^{o(1)}` because the shell contains `O(\log X/\log\log X)` primes. A materially wider shell could make the combinatorial entropy part of the power budget.
- No independence of divisibility events is assumed. The bound remains valid under the exact source coupling because it sums actual CRT intersections.

The exact claim is falsified if `(16)` fails for a partial shell subset, if a point with `r_y(n)\ge r` need not belong to an `r`-fold intersection, or if the shell entropy in `(22)` contributes a fixed power of `X`. The energy consequence is falsified if `(25)`--`(27)` do not upper-bound the separately defined high-incidence component.

## Consequence for the live frontier

The first-shell coupling problem is now localized by incidence multiplicity. For `c>1/4`, all inputs shared by at least about `\frac14\log X/\log\log X` shell square moduli are already cheap enough to isolate by absolute support. The hard source information is therefore not concentrated at the largest CRT overlaps; it sits in the broad low/mesoscopic-incidence region where many different partial intersections coexist but none is individually sparse enough to meet the energy target.

The next useful question is correspondingly narrower: whether the low-incidence hypergraph admits a signed decomposition whose cross terms cancel before absolute values, or whether one can build an admissible matched control showing that incidence data below the one-quarter threshold is still insufficient. Either outcome would directly test the remaining mechanism rather than extending the already-harmless high-incidence tail.