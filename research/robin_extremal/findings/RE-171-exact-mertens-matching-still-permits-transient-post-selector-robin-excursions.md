# RE-171 — Exact Mertens matching still permits transient post-selector Robin excursions

**Status:** `EXACT-DERIVED + EXACT-MERTENS-MATCHED-CONTROL + THREE-SHELL-COMPENSATION + KV-FIDELITY + PREFIX-NONRIGIDITY + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-167, RE-169, RE-170.

`RE-170` proves that critical-scale Mertens matching does not determine a selected finite Robin prefix: two bounded-multiplicative compensation shells can leave an order-one intermediate excursion while reducing the final Mertens mismatch to

\[
o\!\left((\sqrt p\log p)^{-1}\right).
\tag{1}
\]

It deliberately stops short of exact equality `\Gamma(Q_p)=\gamma`. That distinction is not load-bearing.

Fix

\[
1<B_1<C_1<B_2<C_2<B_3<C_3
\tag{2}
\]

and a Korobov--Vinogradov exponent `b>0`. There are finite generalized-prime modifications `Q_p` of the ordinary primes, supported in the three disjoint shells

\[
I_{j,p}=[B_jp,C_jp],\qquad j=1,2,3,
\tag{3}
\]

such that, along all sufficiently large primes `p`, all of the following hold.

First, the perturbation remains asymptotically invisible relative to the full KV envelope:

\[
\boxed{
\sup_{t\ge B_1p}
\frac{|\vartheta_{Q_p}(t)-\vartheta(t)|}
{t e^{-bV(t)}}
=o(1),
\qquad
V(t)=\frac{(\log t)^{3/5}}{(\log\log t)^{1/5}}.
}
\tag{4}
\]

Second, after the first shell and before the second there is a fixed order-one Robin excursion. For every `U_p` with

\[
C_1p<U_p<B_2p,
\tag{5}
\]

one can arrange

\[
\boxed{
\left|
\mathcal A_{p,U_p}(Q_p)-\mathcal A_{p,U_p}(P)
\right|
\ge\delta_0
}
\tag{6}
\]

for one fixed `\delta_0>0`, where

\[
\mathcal A_{p,U}(Q)
=
\frac{\sqrt p\log p}{Z_p}
\int_{p+p^\alpha}^{U}
\bigl(t-\vartheta_Q(t)\bigr)(-h'(t))\,dt,
\qquad
h(t)=\frac{-\log(1-t^{-1})}{\log t},
\qquad
Z_p=2+o(1).
\tag{7}
\]

Third, the completed source has **exactly the ordinary logarithmic Mertens normalization**:

\[
\boxed{\Gamma(Q_p)=\gamma.}
\tag{8}
\]

Finally, because the complete modification is compactly supported and (8) is exact, the full post-correction Robin displacement vanishes exactly:

\[
\boxed{
\mathcal A_{p,U}(Q_p)-\mathcal A_{p,U}(P)=0
\qquad(U\ge C_3p).
}
\tag{9}
\]

Thus even exact equality of the global Mertens constant does **not** rigidify a selected finite Robin prefix inside the generalized-source fidelity class. The missing resource after `RE-170` is spatial or selector-sensitive information, not finer scalar precision in `\Gamma`.

## 1. RE-170 leaves only a logarithmic-over-linear Mertens residual

Apply the first two shells of `RE-170`. Denote the resulting source by `Q_p^{(2)}`. The first shell produces the fixed excursion (6). The reverse packets in the second shell cancel it with the elementary mesh from `RE-170`, namely

\[
\left|
\mathcal A_{p,U}(Q_p^{(2)})-
\mathcal A_{p,U}(P)
\right|
=
O\!\left(\frac{(\log p)^2}{\sqrt p}\right)
\qquad(U\ge C_2p).
\tag{10}
\]

The complete two-shell modification is compactly supported. Hence the exact `RE-169` sum rule gives

\[
R_p
:=
\Gamma(Q_p^{(2)})-\gamma
=
-\frac{Z_p}{\sqrt p\log p}
\left(
\mathcal A_{p,U}(Q_p^{(2)})-
\mathcal A_{p,U}(P)
\right),
\tag{11}
\]

for every `U\ge C_2p`. Combining (10) and (11),

\[
\boxed{
R_p=O\!\left(\frac{\log p}{p}\right).
}
\tag{12}
\]

So the stronger exact-matching question reduces to removing a scalar residual of size at most `O((log p)/p)` without disturbing the order-one prefix already created before `B_2p`.

## 2. A Chebyshev-neutral two-prime dial moves the Mertens constant continuously

Put

\[
H(x):=-\log(1-x^{-1}).
\tag{13}
\]

For a finite source modification, each inserted generalized prime label `q` changes `\Gamma` by `H(q)`, while each deleted ordinary prime `r` changes it by `-H(r)`, because

\[
h(q)\log q=H(q).
\tag{14}
\]

Choose two fixed separated subintervals strictly inside the third shell. The ordinary PNT supplies `m_p=\lceil K\log p\rceil` disjoint pairs of ordinary primes

\[
r_j<s_j,
\qquad
r_j\asymp p,
\qquad
s_j\asymp p,
\qquad
\frac{s_j}{r_j}\ge 1+\eta
\tag{15}
\]

for one fixed `\eta>0`. Delete each pair `(r_j,s_j)`. For a real parameter `\tau` insert instead

\[
r_j(\tau)=r_j e^{-\tau},
\qquad
s_j(\tau)=s_j e^{\tau}.
\tag{16}
\]

Choose a fixed `\tau_0>0`, depending only on the shell geometry, small enough that for every `|\tau|\le\tau_0` all four locations remain inside `I_{3,p}` and

\[
r_j e^{-\tau}<s_j e^{\tau}.
\tag{17}
\]

Each pair is **exactly Chebyshev-mass neutral**:

\[
\log r_j(\tau)+\log s_j(\tau)
=
\log r_j+\log s_j.
\tag{18}
\]

Therefore the cumulative `\vartheta` discrepancy created by the micro-correction returns exactly to zero after the shell, independently of `\tau`.

The exact Mertens shift of one pair is

\[
g_j(\tau)
:=
H(r_j e^{-\tau})
+H(s_j e^{\tau})
-H(r_j)-H(s_j).
\tag{19}
\]

Since

\[
H'(x)=-\frac1{x(x-1)},
\tag{20}
\]

we obtain

\[
\boxed{
g_j'(\tau)
=
\frac1{r_j e^{-\tau}-1}
-
\frac1{s_j e^{\tau}-1}>0.}
\tag{21}
\]

The fixed proportional separation in (15)--(17) gives constants `0<c_0<C_0<\infty`, depending only on the chosen shell geometry, such that uniformly for `|\tau|\le\tau_0`,

\[
\frac{c_0}{p}
\le g_j'(\tau)
\le\frac{C_0}{p}.
\tag{22}
\]

Summing the `m_p` pairs,

\[
G_p(\tau):=\sum_{j=1}^{m_p}g_j(\tau)
\tag{23}
\]

is continuous, strictly increasing, satisfies `G_p(0)=0`, and obeys

\[
G_p(\tau_0)\ge
c_0\tau_0 K\frac{\log p}{p}+O(p^{-1}),
\qquad
G_p(-\tau_0)\le
-c_0\tau_0 K\frac{\log p}{p}+O(p^{-1}).
\tag{24}
\]

Choose the fixed constant `K` larger than the implicit constant in (12), divided by `c_0\tau_0`. Then for all sufficiently large `p`, `-R_p` lies strictly inside the interval

\[
[G_p(-\tau_0),G_p(\tau_0)].
\tag{25}
\]

The intermediate value theorem therefore supplies a parameter `\tau_p` such that

\[
\boxed{G_p(\tau_p)=-R_p.}
\tag{26}
\]

Adding this third-shell micro-correction to `Q_p^{(2)}` proves (8) **exactly**, not merely asymptotically.

If distinct generalized labels are required, use independent parameters `\tau_j` instead of one common `\tau`. Pairwise mass balance (18) remains automatic, while the single scalar equation `\sum_j g_j(\tau_j)=-R_p` leaves an `(m_p-1)`-dimensional local level set because every derivative in (21) is nonzero. An arbitrarily small generic perturbation inside that level set avoids coincidences without changing either the exact Mertens correction or the shell mass balance.

## 3. The exact correction is negligible for KV fidelity and leaves the prefix untouched

At any point inside the third shell, one moved pair contributes at most `O(\log p)` to the cumulative Chebyshev discrepancy. Since there are only `m_p=O(\log p)` pairs,

\[
\sup_t
|\vartheta_{Q_p}(t)-\vartheta_{Q_p^{(2)}}(t)|
=O((\log p)^2).
\tag{27}
\]

On a bounded-multiplicative shell `t\asymp p`, the KV allowance is

\[
t e^{-bV(t)}=p^{1-o(1)}.
\tag{28}
\]

Hence the relative cost of the exact correction is

\[
\boxed{
\frac{(\log p)^2}{p e^{-bV(B_3p)}}
=p^{-1+o(1)}=o(1).
}
\tag{29}
\]

This is smaller than the already vanishing `p^{-1/2+o(1)}` relative cost of the first two order-one shells in `RE-170`. Equation (4) follows.

The first-shell excursion is also unchanged. Both the approximate reverse shell and the exact micro-correction occur strictly after the gap (5), so every truncation there still sees precisely the first-shell displacement. This preserves (6).

After `C_3p`, the entire three-shell modification is compactly supported and the exact Mertens mismatch is zero. Applying the compact-support identity of `RE-169` gives

\[
\mathcal A_{p,U}(Q_p)-\mathcal A_{p,U}(P)
=
\frac{\sqrt p\log p}{Z_p}
\bigl(\Gamma(Q_p)-\gamma\bigr)
=0
\qquad(U\ge C_3p),
\tag{30}
\]

which proves (9).

## 4. Falsification checks and scope

**Does the exact tuning use fractional ordinary primes?** No. Every deletion is an actual ordinary prime. Continuity enters only through the positions of finitely many generalized labels, exactly as allowed by the matched generalized-source framework of `RE-167`--`RE-170`.

**Does the micro-correction change the selector data?** No. All three shells start above a fixed multiple `B_1p>p`; for sufficiently large `p` they also lie above `p+p^\alpha`. The source below the selected first-layer frontier is untouched.

**Does exact Mertens equality hide a nonzero final Robin displacement?** No. For compact support the `RE-169` identity makes the two statements equivalent. The construction deliberately leaves a transient order-one displacement and then returns the full normalized coordinate to zero exactly.

**Could the small correction violate the KV exponent even if it preserves total Chebyshev mass?** No. Equation (27) controls the worst cumulative discrepancy *inside* the shell, not merely at its endpoint, and (29) is uniform there.

**Does this construct an ordinary-prime or CA counterexample?** No. `Q_p` is a generalized matched control. The conclusion is informational: exact `\Gamma=\gamma`, the ordinary quantitative PNT envelope, and exact selector-prefix agreement still do not logically determine the selected finite Robin coordinate without a spatial/source-specific restriction.

**Is exact equality merely a consequence of assuming a continuous signed measure?** No. The correction is realized by finitely many genuine generalized-prime labels. The one-dimensional dial (19)--(26) is an explicit finite atomic interpolation.

A targeted prior-art audit checked the generalized Mertens literature represented by Pollack's *On Mertens' Theorem for Beurling Primes* (Canadian Mathematical Bulletin **56** (2013), 829--843, DOI `10.4153/CMB-2012-004-8`), Olofsson's work on Beurling generalized primes, and small-perturbation constructions of generalized prime systems. Those works establish Mertens/PNT properties or construct globally controlled generalized systems; no result located gives this exact finite three-shell interpolation preserving the ordinary Mertens constant while creating a transient Robin-kernel prefix excursion. None is load-bearing in the proof above, which uses only the internal exact Mertens sum rule and the finite shell constructions already established in this line. No new `SOURCES.md` anchor is required.

## 5. Research consequence

`RE-170` left a possible semantic escape: perhaps the ordinary source is special because its Mertens normalization is not merely correct to the critical Robin scale but **exactly** `\gamma`. `RE-171` removes that escape inside the generalized-source control class.

The source-fidelity hierarchy is now sharper:

\[
\boxed{
\text{selector-prefix agreement}
+
\text{KV fidelity}
+
\Gamma(Q)=\gamma
\not\Longrightarrow
\text{finite-prefix Robin rigidity}.
}
\tag{31}
\]

Exact global normalization constrains only the total future signed Robin-kernel displacement. A later bounded-multiplicative shell can repay an order-one earlier debt, and a still smaller `O((\log p)^2)` Chebyshev-neutral micro-correction can make the scalar normalization exact at negligible source cost.

Therefore the accepted `clean-peak-selector-height-coupling` clue remains open, but its missing resource is now unambiguously **spatial or selector-conditioned**. Sharpening the scalar Mertens precision further cannot help: there is no precision beyond exact equality. A successful ordinary-prime/CA argument must instead show that the selector-selected prefix constrains where opposite-sign future Mertens debt can occur, or supply another genuinely source-specific nonlocal invariant that the three-shell matched control cannot preserve.

**Provenance:** derived against default-branch snapshot `d4f0c39e9f2e2d09f37947ffdee67a31a2bd71c6`; stable finding prefix `RE`; no adversarial sidecar was open; no clue-state, `mind/**`, README, graph, or source-registry mutation required.