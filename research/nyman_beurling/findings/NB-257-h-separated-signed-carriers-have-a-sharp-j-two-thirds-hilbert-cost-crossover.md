# NB-257 — H-separated signed carriers have a sharp `J^(2/3)` Hilbert-cost crossover

**Date:** 2026-09-20  
**Status:** `EXACT-DERIVED + SIGNED-COMPLEX-MIXTURE + H-SEPARATED-DICTIONARY + MINIMUM-L2-INTERPOLATION + SHARP-TWO-THIRDS-CROSSOVER + NB-256-REFINEMENT + SOURCE-ONLY + METHOD-BOUNDARY + FRESH-PRIOR-ART-AUDIT`.

`NB-256` shows that raw Euler-normalized coefficient total variation is not a physical conditioning norm: arbitrarily large opposite coefficients can hide in microscopic dipoles whose separation is `o(H)`, while both the actual smooth-shell source and the Ford-scale carrier stay essentially unchanged. The most concrete escape left there was to forbid that degeneracy by requiring carrier centers to be separated on the shell scale `H`, where smooth-shell synthesis should become coercive.

That coercivity is exact, but it does **not** close the signed scalar route. If the shell centers are `H`-separated, their physical supports are disjoint, so the shell-scaled source `L^2` norm is exactly the coefficient `ell^2` norm up to the fixed profile factor. Nevertheless, `K` separated channels can collectively create an order-one change of the normalized carrier on the Ford scale `1/R`. The minimum possible Hilbert cost is

\[
\boxed{
H^{1/2}\|h_\nu\|_2
\asymp
\frac{J}{K^{3/2}},
\qquad
J=\frac RH,
}
\]

for a filled `H`-grid spanning `W\asymp KH`. Hence there is a sharp crossover

\[
\boxed{
K\asymp \frac WH\asymp J^{2/3}.
}
\]

Below that scale, every `H`-separated construction that forces a Ford-scale notch has diverging shell-Hilbert cost. At `K\asymp J^{2/3}`, the cost is order one, while the total span is still strongly mesoscopic,

\[
\frac WR\asymp J^{-1/3}\to0.
\]

The least-norm construction is not another microscopic-dipole artifact. Its coefficient total variation is

\[
V\asymp \frac JK,
\]

so

\[
WV\asymp R.
\]

It therefore pays exactly the scale required by the `NB-255` coherence bound, while the separation condition makes that cost visible in the actual source. At the crossover, `V\asymp J^{1/3}` and the same prime-number-theorem error ledger used in `NB-255` remains harmless under the standing `J\le\log Q` restriction.

More strongly, the optimal carrier does not merely have one accidental zero. On bounded Ford coordinates it converges to a linear ramp,

\[
B_\lambda(x/R)
=
1-\frac{x}{\vartheta}+o(1),
\]

when the imposed notch is at `z_*=\vartheta/R`. Thus its genuine coherence radius is `Theta(1/R)`, rather than `1/W` or `1/(WV)` only as a loose coefficient bound.

This is a source-side route correction. `H`-separation successfully quotients out the fake variation of `NB-256`, but a growing number of genuinely resolved channels can amortize the cancellation in the Hilbert norm. What remains open is whether a **family** of Ford-scale notches, or the full Hardy-projected carrier-band energy required by `NB-250`--`NB-251`, can be suppressed with the same bounded Hilbert cost after the legal Nyman/Hardy destination map.

## 1. Exact separated-shell synthesis

Retain the Ford normalization of `NB-230`--`NB-256`:

\[
Q:=\log(10+|t_0|),
\qquad
R:=Q^{2/3}(\log Q)^{1/3},
\qquad
Y:=\frac XR\asymp1,
\qquad
J:=\frac RH\to\infty,
\tag{1}
\]

with the conservative matched-control restriction

\[
J\le\log Q.
\tag{2}
\]

Fix

\[
0<a<b<1,
\qquad
0\le\phi\in C_c^\infty((a,b)),
\qquad
\phi\not\equiv0.
\tag{3}
\]

For an odd integer `K=K_J` satisfying

\[
K\to\infty,
\qquad
K=o(J),
\tag{4}
\]

take the `H`-spaced offsets

\[
\xi_j=jH,
\qquad
-\frac{K-1}{2}\le j\le\frac{K-1}{2}.
\tag{5}
\]

Their span is

\[
W=(K-1)H\asymp KH,
\qquad
\frac WR\asymp\frac KJ\to0,
\qquad
\frac WX\to0.
\tag{6}
\]

Let the Euler-normalized coefficient measure be

\[
\lambda=\sum_j c_j\delta_{\xi_j},
\qquad
\sum_j c_j=1.
\tag{7}
\]

As in `NB-255`, convert back to the actual shell coefficients through

\[
d\nu(\xi)=e^{r\xi/X}\,d\lambda(\xi),
\tag{8}
\]

so that

\[
\int e^{-r\xi/X}\,d\nu(\xi)=1.
\tag{9}
\]

The physical source is

\[
h_\nu(u)
=
\sum_j e^{r\xi_j/X}c_j
\frac1H\phi\!\left(\frac{u-X-\xi_j}{H}\right).
\tag{10}
\]

Because `supp phi` has diameter strictly smaller than one and neighboring centers differ by exactly `H`, the translated shell supports in (10) are pairwise disjoint. Consequently there is no hidden coefficient cancellation after synthesis:

\[
\boxed{
H\|h_\nu\|_2^2
=
\|\phi\|_2^2
\sum_j e^{2r\xi_j/X}|c_j|^2,
}
\tag{11}
\]

and, since `W/X=o(1)`, uniformly over the whole dictionary,

\[
\boxed{
H^{1/2}\|h_\nu\|_2
=(1+o(1))\|\phi\|_2\|c\|_{\ell^2}.
}
\tag{12}
\]

Likewise disjointness and `phi>=0` give

\[
\boxed{
\|h_\nu\|_1
=(1+o(1))\|\phi\|_1\|c\|_{\ell^1}.
}
\tag{13}
\]

Thus the separated dictionary does exactly what `NB-256` asked of it: coefficient geometry at scale `H` is now physical source geometry.

## 2. Any Ford-scale notch costs at least `J/(B sqrt K)` in source `L^2`

The Euler-normalized carrier is

\[
B_\lambda(z)
:=
\sum_j c_j e^{i\xi_j z}.
\tag{14}
\]

Consider more generally any `K` coefficient atoms in `[-W/2,W/2]` with total mass one, and suppose that for a fixed `vartheta>0`

\[
B_\lambda(z_*)=0,
\qquad
z_*:=\frac{\vartheta}{R}.
\tag{15}
\]

Then

\[
1
=
\left|
\sum_j c_j(1-e^{i\xi_j z_*})
\right|.
\tag{16}
\]

Since `z_*` is real,

\[
|1-e^{i\xi_jz_*}|
\le
|\xi_jz_*|.
\tag{17}
\]

Cauchy--Schwarz therefore gives

\[
1
\le
|z_*|\,\|c\|_2
\left(\sum_j\xi_j^2\right)^{1/2}
\le
\frac{\vartheta W\sqrt K}{2R}\,\|c\|_2.
\tag{18}
\]

Hence

\[
\boxed{
\|c\|_2
\ge
\frac{2R}{\vartheta W\sqrt K}.
}
\tag{19}
\]

Now write

\[
B:=\frac WH.
\tag{20}
\]

For an `H`-separated dictionary, packing gives `K<=B+1`. Combining (12), (19), and `R=JH`, any such source that creates the notch (15) obeys

\[
\boxed{
H^{1/2}\|h_\nu\|_2
\gg_{\phi,\vartheta}
\frac{J}{B\sqrt K}
\gg
\frac{J}{B^{3/2}}.
}
\tag{21}
\]

Therefore

\[
\boxed{
B=o(J^{2/3})
\quad\Longrightarrow\quad
H^{1/2}\|h_\nu\|_2\to\infty
}
\tag{22}
\]

for every `H`-separated scalar dictionary that forces an order-one carrier change by distance `Theta(1/R)` from the origin.

This is already a genuine coercive statement after quotienting microscopic dipoles. It does not use raw total variation and it is measured directly on the synthesized source.

## 3. A filled `H`-grid attains the lower-bound scale

For the symmetric grid (5), put

\[
\alpha:=Hz_*=rac{\vartheta}{J}
\tag{23}
\]

and

\[
S_K
:=
\sum_{j=-(K-1)/2}^{(K-1)/2}e^{ij\alpha}
=
\frac{\sin(K\alpha/2)}{\sin(\alpha/2)}.
\tag{24}
\]

Among all coefficient vectors satisfying

\[
\sum_jc_j=1,
\qquad
\sum_jc_je^{ij\alpha}=0,
\tag{25}
\]

the unique minimum-`ell^2` solution is the ordinary minimum-norm solution of this two-row interpolation system. Since the `2x2` row Gram matrix is

\[
G_K
=
\begin{pmatrix}
K&S_K\\
S_K&K
\end{pmatrix},
\tag{26}
\]

we obtain explicitly

\[
\boxed{
\|c^{\min}\|_2^2
=
\frac{K}{K^2-S_K^2}.
}
\tag{27}
\]

One convenient formula for the coefficients themselves is

\[
\boxed{
c_j^{\min}
=
\frac{K-S_Ke^{-ij\alpha}}
{K^2-S_K^2}.
}
\tag{28}
\]

Because `K/J->0`, we have `K alpha ->0`. The elementary sine expansion gives

\[
\frac{S_K}{K}
=
1-
\frac{(K^2-1)\alpha^2}{24}
+O(K^4\alpha^4),
\tag{29}
\]

and hence

\[
K^2-S_K^2
=
\frac{K^2(K^2-1)\alpha^2}{12}
\left(1+O(K^2\alpha^2)\right).
\tag{30}
\]

Substituting `alpha=vartheta/J` into (27),

\[
\boxed{
\|c^{\min}\|_2
=
\frac{\sqrt{12}}{\vartheta}
\frac{J}{K^{3/2}}
(1+o(1)).
}
\tag{31}
\]

By the exact synthesis identity (12),

\[
\boxed{
H^{1/2}\|h_{\nu^{\min}}\|_2
=
\frac{\sqrt{12}\,\|\phi\|_2}{\vartheta}
\frac{J}{K^{3/2}}
(1+o(1)).
}
\tag{32}
\]

Thus the exponent in the universal lower bound (21) is sharp when the separated dictionary fills its available span.

In particular, for

\[
K\sim\kappa J^{2/3},
\qquad \kappa>0,
\tag{33}
\]

we get

\[
\boxed{
H^{1/2}\|h_{\nu^{\min}}\|_2
\longrightarrow
\frac{\sqrt{12}\,\|\phi\|_2}
{\vartheta\kappa^{3/2}}.
}
\tag{34}
\]

At the same time,

\[
W\asymp KH
\asymp
H J^{2/3}
=
R J^{-1/3},
\tag{35}
\]

so

\[
\boxed{
H\ll W\ll R\asymp X.
}
\tag{36}
\]

The bounded-Hilbert-cost construction therefore occurs well inside the mesoscopic carrier regime that remained open after `NB-251`--`NB-256`.

## 4. The least-norm solution pays the `NB-255` tax honestly

The same two constraints give a matching estimate for coefficient total variation. From (16)--(17), now without Cauchy--Schwarz,

\[
1
\le
\frac{\vartheta W}{2R}\|c\|_1,
\tag{37}
\]

hence

\[
\|c\|_1
\ge
\frac{2R}{\vartheta W}
\asymp
\frac{J}{K}.
\tag{38}
\]

For the minimum-`ell^2` vector, (31) and `\|c\|_1<=\sqrt K\|c\|_2` give the reverse order bound

\[
\|c^{\min}\|_1
\ll_\vartheta
\frac JK.
\tag{39}
\]

Therefore

\[
\boxed{
V:=\|\lambda\|_{TV}
=\|c^{\min}\|_1
\asymp_\vartheta
\frac JK.
}
\tag{40}
\]

Since `W\asymp KH`,

\[
\boxed{
WV\asymp R.
}
\tag{41}
\]

This is exactly the boundary isolated by `NB-255`: its generic forced-coherence capacity

\[
J_*:=\frac{R}{WV}
\tag{42}
\]

is now only `Theta(1)`. Unlike the artificial `V->infinity` construction in `NB-256`, however, the present variation is carried by `H`-resolved, disjoint shells and cannot disappear under smooth-shell synthesis.

The norm distinction is sharp. Equations (13) and (40) give

\[
\|h_{\nu^{\min}}\|_1
\asymp
\frac JK,
\tag{43}
\]

whereas (32) gives the shell-scaled Hilbert cost `J/K^(3/2)`. At the crossover `K\asymp J^(2/3)`, the `L^1` source cost still grows like `J^(1/3)`, while the Hilbert cost stays bounded. Thus an `L^1`/transport geometry would continue to price this cancellation heavily, but the Hilbert geometry can amortize it across the `K` genuinely distinct channels.

This matters for Nyman--Beurling because the destination problem is Hilbertian. It does **not** yet identify (32) with the final Nyman distance or prove that the Hardy projection preserves the bounded cost; it says that separated-source coercivity alone cannot supply a divergent Hilbert tariff beyond the `J^(2/3)` crossover.

## 5. The carrier really changes on the Ford scale

The notch at `vartheta/R` is not a narrow accidental defect produced by a huge unresolved derivative. For the minimum-norm coefficients let

\[
m_1:=\sum_jc_j^{\min}\xi_j.
\tag{44}
\]

From (40) and `|xi_j|<=W/2`, for every fixed `A>0` and uniformly on `|x|<=A`, Taylor expansion gives

\[
B_\lambda(x/R)
=
1+
\frac{ix}{R}m_1
+
O_A\!\left(
\frac{V W^2}{R^2}
\right).
\tag{45}
\]

Using `V\asymp J/K`, `W\asymp KH`, and `R=JH`,

\[
\frac{VW^2}{R^2}
\asymp
\frac KJ
\to0.
\tag{46}
\]

The exact notch condition at `x=vartheta` therefore implies

\[
\frac{i m_1}{R}
=
-\frac1\vartheta+o(1).
\tag{47}
\]

Substituting back into (45),

\[
\boxed{
B_\lambda(x/R)
=
1-\frac{x}{\vartheta}
+O_A(K/J)
}
\tag{48}
\]

uniformly for bounded `x`.

Thus the construction has a genuine `1/R` coherence scale. Its normalized carrier falls from `1` at the origin to `0` at `vartheta/R` and approaches a deterministic linear profile on every fixed Ford-scale window. The `H`-separated dictionary has therefore produced actual super-resolution of the carrier response relative to its total span `W`, because

\[
\frac{1/R}{1/W}
=
\frac WR
\to0.
\tag{49}
\]

## 6. Arithmetic ledger remains source-safe at the crossover

The Euler normalization (9) is exactly the one used in `NB-255`. Hence the same Stieltjes/PNT calculation gives

\[
\sum_{n\ge2}
\Lambda(n)h_\nu(\log n)n^{-\sigma_X}
=
 e^{-r}
\int_0^1\phi(y)e^{-rHy/X}\,dy
+o(1),
\tag{50}
\]

provided the prime-number-theorem remainder remains uniform after integration against the coefficient variation.

For the least-norm separated construction,

\[
V\asymp\frac JK\le J\le\log Q.
\tag{51}
\]

The same exponentially decaying PNT remainder used in `NB-253`--`NB-256` therefore absorbs the coefficient variation, while `W/X=o(1)` keeps the Euler tilt uniform. In particular, at `K\asymp J^(2/3)`,

\[
V\asymp J^{1/3},
\qquad
W/R\asymp J^{-1/3},
\tag{52}
\]

and the normalized Euler return in (50) remains order one.

So the `J^(2/3)` construction is not excluded by the elementary source-side arithmetic ledger already used in this line. This still does not establish legality after every later Hardy/Nyman operation; it clears only the same source-return gate as `NB-255`--`NB-256`.

## 7. Prior-art and representation audit

The generic harmonic-analysis mechanism is classical. Minimum-energy interpolation by band-limited exponential systems, and the severe conditioning associated with creating sub-bandwidth oscillations, are standard themes in the superoscillation literature. Ferreira and Kempf, *Superoscillations: Faster Than the Nyquist Rate*, IEEE Trans. Signal Process. 54 (2006), 3732--3740, DOI `10.1109/TSP.2006.877642`, explicitly study minimum-energy band-limited interpolation and its energy/dynamic-range cost. Their earlier work with Kempf also treats the energy expense of superoscillations. A fresh search additionally finds Bondar and Talbayev, *Synthesizing superoscillations with just two frequencies*, arXiv:2607.19542 (21 July 2026), which emphasizes that destructive interference between very few harmonics can already create local superoscillatory behavior.

No novelty is claimed here for minimum-norm interpolation, disjoint translates, or the general superoscillation phenomenon. The line-local contribution is the exact insertion of the Ford/Nyman scales and Euler normalization: the resolved smooth-shell source turns coefficient `ell^2` into physical shell-Hilbert norm, the two-constraint Gram matrix yields the sharp `J/K^(3/2)` cost, and combining that with `W\asymp KH` produces the specific crossover

\[
\boxed{
W/H\asymp J^{2/3},
\qquad
W/R\asymp J^{-1/3},
\qquad
V\asymp J^{1/3},
\qquad
WV\asymp R.
}
\tag{53}
\]

The argument is self-contained and does not use an external theorem as a load-bearing step, so no new durable dependency is required in `SOURCES.md`.

Representation-wise, (11), (26)--(31), and the superoscillation interpretation are generic Hilbert/Fourier geometry. What is specific to the present Nyman--Beurling route is the Ford scale `R`, the shell scale `H`, the capacity `J=R/H`, the Euler tilt (8)--(9), the PNT ledger (50)--(52), and the question whether this source-side construction survives the one-sided Hardy/Nyman destination map.

## 8. Adversarial boundary and next target

This finding should not be read as a solution of the Ford obstruction. It proves one exact carrier notch, together with its full bounded-Ford-scale profile, for a legal-looking source-side signed mixture. It does **not** prove small Hardy-projected carrier-band energy, control the actual zeros of zeta, or produce a Nyman--Beurling approximation rate.

The construction also uses complex coefficients. It is therefore an audit of the signed/complex scalar route left open by `NB-254`--`NB-256`, not of positive scalar mixtures, which remain subject to the `1/W` coherence window of `NB-254`.

The important method correction is narrower. `NB-256` suggested that imposing `H`-scale separation might restore a coercive source geometry strong enough to make Ford-scale cancellation expensive. It does restore exact synthesis coercivity, but **only coefficientwise**. Once `K` resolved channels are available, the Hilbert norm gains the usual `sqrt K` aggregation advantage, and the cancellation becomes bounded-cost exactly at `K\asymp J^(2/3)`.

The next source-side question is therefore no longer whether one Ford-scale notch is expensive. It is whether the object actually required by `NB-250`--`NB-251` forces **many independent Ford-scale interpolation constraints**. A fixed or growing family of notches, derivative constraints, or direct carrier-band-energy suppression may change the exponent and could restore a divergent Hilbert tariff. That interpolation-rank question should be solved before spending more effort on coefficient total variation or on another scalar coherence-radius bound.