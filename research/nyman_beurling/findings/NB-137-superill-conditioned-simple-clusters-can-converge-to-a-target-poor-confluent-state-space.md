# NB-137 — superill-conditioned simple clusters can converge to a target-poor confluent state space

**Status:** `DERIVED + NYMAN-FINITE-WINDOW-STATE-GEOMETRY + GROWING-SIMPLE-CLUSTER + CONFLUENT-GRASSMANN-LIMIT + TARGET-AWARE + MATCHED-ZERO-ENVELOPE-CONTROL + REPRESENTATION-AUDIT + NEGATIVE/METHOD-BOUNDARY`.

`NB-136` shows that a polynomial-height packet with only `Theta(log R)` distinct components can make the full natural-prefix zero-power matrix superpolynomially ill-conditioned. Its own limitation is essential: a tiny singular value of an ordinary Vandermonde coordinate matrix does not say whether the nearly invisible direction is target-bearing, and it may disappear after passing to confluent coordinates.

The two previously separate threads can be spliced exactly. The growing confluent packet of `NB-111` is target-poor below its explicit `1/8` logarithmic window. A packet of **distinct simple states** may be chosen arbitrarily close to that confluent packet in the Grassmannian while its ordinary natural-prefix zero-power matrix becomes arbitrarily worse conditioned. In particular, under the same coarse zero-count and zero-free-region envelopes used by `NB-133`--`NB-136`, one can have simultaneously

\[
\boxed{
\kappa_2(V_G)\ge
\exp\!\bigl((c+o(1))(\log G)^4\bigr)
}
\tag{1}
\]

and

\[
\boxed{
\frac{\|P_{\mathcal S_G^{\rm split}}e_G\|^2}
     {\|e_G\|^2}
\longrightarrow0.
}
\tag{2}
\]

Thus the conditioning collapse exhibited by `NB-136` is not merely insufficient to prove target capture. There are matched packets for which the collapse becomes vastly stronger while the **entire canonical state span becomes asymptotically orthogonal to the Nyman target**. Any continuation after `NB-136` therefore has to be target-aware or quotient out the confluent coordinate singularity; ordinary power-basis conditioning cannot by itself distinguish rescue from irrelevance.

## 1. A growing simple cluster has the confluent jet as its exact Grassmann limit

Fix

\[
r\ge1,
\qquad
0<a<\frac12,
\qquad
q\ge2,
\tag{3}
\]

and let `G -> infinity`. Put

\[
m_G=\lceil G\rceil,
\qquad
R_G=m_Gq,
\qquad
\lambda_G=a+iG,
\qquad
\rho_G=\lambda_G+\frac12.
\tag{4}
\]

For a real vertical displacement `h`, define the analytic one-state representer `w_G(h)` on the fully backfilled cell space

\[
\mathcal E_{r,R_G}
=
\operatorname{span}\{\phi_n:r\le n<R_G\},
\qquad
\phi_n(t)=e^{-t/2}\mathbf1_{[\log n,\log(n+1))}(t),
\tag{5}
\]

by

\[
\boxed{
\langle\phi_n,w_G(h)\rangle
=
\sqrt{2a}\,m_G^{\lambda_G+ih}
\int_n^{n+1}t^{-\lambda_G-ih-3/2}\,dt.
}
\tag{6}
\]

At `h=0`, differentiating under the integral gives

\[
\left.
\frac{d^k}{dh^k}w_G(h)
\right|_{h=0}
=
\left(-\frac{i}{2a}\right)^k w_{k,G},
\tag{7}
\]

where `w_(k,G)` is exactly the derivative-state basis used in `NB-108`--`NB-111`, up to the displayed nonzero scalar. Therefore

\[
\mathcal S_G^{\rm conf}
:=
\operatorname{span}\{w_G^{(k)}(0):0\le k<d_G\}
\tag{8}
\]

is the same confluent state space as in those findings.

Now choose `d_G` distinct vertical offsets

\[
h_{j,G}=j\varepsilon,
\qquad
0\le j<d_G,
\tag{9}
\]

and let

\[
\mathcal S_G^{\rm split}(\varepsilon)
:=
\operatorname{span}\{w_G(j\varepsilon):0\le j<d_G\}.
\tag{10}
\]

For `0<=k<d_G`, form the forward divided-difference columns

\[
v_{k,G}(\varepsilon)
:=
\varepsilon^{-k}
\sum_{j=0}^k
(-1)^{k-j}\binom{k}{j}w_G(j\varepsilon).
\tag{11}
\]

For every nonzero spacing `ε`, the transformation from the raw columns in `(10)` to the columns `(11)` is triangular with nonzero diagonal. Hence it is invertible and

\[
\boxed{
\operatorname{span}\{v_{k,G}(\varepsilon):k<d_G\}
=
\mathcal S_G^{\rm split}(\varepsilon).
}
\tag{12}
\]

For fixed `G` and its finite `d_G`, analyticity of `(6)` gives

\[
v_{k,G}(\varepsilon)
\longrightarrow
w_G^{(k)}(0)
\qquad(\varepsilon\to0)
\tag{13}
\]

simultaneously for all `k<d_G` in the finite-dimensional Hilbert norm of the cell space `(5)`. Under the logarithmic rank condition imposed below, the coercive estimate in `NB-111` makes the jet synthesis map injective for all sufficiently large `G`, so its smallest singular value is positive.

It follows by elementary finite-dimensional subspace perturbation that, for each sufficiently large `G` and every prescribed `eta_G>0`, there is a number

\[
\varepsilon_*(G,\eta_G)>0
\tag{14}
\]

such that

\[
0<\varepsilon<\varepsilon_*(G,\eta_G)
\quad\Longrightarrow\quad
\boxed{
\|P_{\mathcal S_G^{\rm split}(\varepsilon)}
-P_{\mathcal S_G^{\rm conf}}\|\le\eta_G.
}
\tag{15}
\]

No uniform conditioning of the raw columns is being smuggled into `(15)`. The divided-difference change of coordinates is allowed to become arbitrarily ill-conditioned; projector convergence is a statement about the **subspace**, not the ordinary power basis.

## 2. Below the zero-count budget, the split packet can remain target-poor

Choose a fixed constant

\[
0<c<0.10076
\tag{16}
\]

and put

\[
d_G=\lfloor c\log G\rfloor.
\tag{17}
\]

Because `0.10076<1/8`, there is a fixed `delta>0` such that

\[
d_G\le\left(\frac18-\delta\right)\log G
\tag{18}
\]

for all sufficiently large `G`. With `q` and `a` fixed, `(4)` is exactly the radial-depth regime of `NB-111`: `R_G` is comparable to `G` and

\[
2a\log q\in(0,\infty)
\tag{19}
\]

is fixed. Hence, writing

\[
e_G
=e^{-t/2}\mathbf1_{[\log r,\log R_G)},
\tag{20}
\]

`NB-111` gives

\[
\delta_G^{\rm conf}
:=
\frac{\|P_{\mathcal S_G^{\rm conf}}e_G\|}
     {\|e_G\|}
\longrightarrow0.
\tag{21}
\]

Take `eta_G -> 0`, for example `eta_G=1/log G`, and choose a positive spacing satisfying

\[
\boxed{
\varepsilon_G
\le
\min\left\{
\varepsilon_*(G,\eta_G),
\exp\bigl(- (\log G)^3\bigr)
\right\}.
}
\tag{22}
\]

Then `(15)` and the triangle inequality for the two orthogonal projectors imply

\[
\frac{\|P_{\mathcal S_G^{\rm split}}e_G\|}
     {\|e_G\|}
\le
\delta_G^{\rm conf}+\eta_G
\longrightarrow0,
\tag{23}
\]

which proves `(2)`.

This conclusion is basis-invariant. In particular, if the split points were actual distinct right-half zeta zeros, `NB-095` shows that sequential canonical Blaschke deflation changes the raw state columns by an invertible triangular matrix. Its conditioning may explode during confluence, but its range is still precisely the same split state space. Thus `(23)` concerns the canonical finite-state range, not a convenient but lossy coordinate choice.

## 3. The same packet makes the complete natural-prefix power matrix catastrophically ill-conditioned

Define the distinct simple formal points

\[
\rho_{j,G}
=
\rho_G+ij\varepsilon_G,
\qquad
0\le j<d_G,
\tag{24}
\]

and use **all** natural samples up to the finite-section cutoff:

\[
V_G
=
\left(n^{-\overline{\rho_{j,G}}}\right)_
{1\le n\le R_G,\ 0\le j<d_G}.
\tag{25}
\]

Let `M_G=d_G-1` and take the binomial vector

\[
x_j=(-1)^{M_G-j}\binom{M_G}{j}.
\tag{26}
\]

The same exact finite-difference identity used in `NB-136` gives, row by row,

\[
(V_Gx)_n
=
n^{-\overline{\rho_G}}
\left(e^{i\varepsilon_G\log n}-1\right)^{M_G}.
\tag{27}
\]

Also

\[
\|x\|_2^2
=
\sum_{j=0}^{M_G}\binom{M_G}{j}^2
=
\binom{2M_G}{M_G}.
\tag{28}
\]

Since `β=1/2+a>1/2`,

\[
\sum_{n\le R_G}n^{-2\beta}
\le\zeta(2\beta)<\infty.
\tag{29}
\]

Thus for the unit vector `u=x/||x||_2`,

\[
\|V_Gu\|_2
\le
C_a
\frac{(\varepsilon_G\log R_G)^{M_G}}
     {\binom{2M_G}{M_G}^{1/2}}.
\tag{30}
\]

For sufficiently small `ε_G`, the numbers `e^(i ε_G log n)`, `1<=n<=d_G`, are distinct, so the first `d_G` rows contain an ordinary Vandermonde minor and `V_G` has full column rank. Moreover its first column has norm at least one. Therefore

\[
\boxed{
\kappa_2(V_G)
\ge
C_a^{-1}
\binom{2M_G}{M_G}^{1/2}
(\varepsilon_G\log R_G)^{-M_G}.
}
\tag{31}
\]

Using `(17)`, `(22)`, and `log R_G=log G+O(1)`,

\[
\boxed{
\log\kappa_2(V_G)
\ge
(c+o(1))(\log G)^4,
}
\tag{32}
\]

which proves `(1)`. The exponent `4` is not claimed to be canonical; it only records the convenient choice in `(22)`. Because projector convergence permits taking the split spacing still smaller, the ordinary-coordinate condition number can be made larger than **any prescribed finite function of `G`** while preserving `(23)`.

That last statement is deliberately coordinate-sensitive: it concerns the matrix `(25)`. The target conclusion `(23)` is coordinate-free. Their coexistence is the point.

## 4. Matched control: current coarse zero laws allow the same geometry

The construction above is a matched control, not an assertion that the points `(24)` are genuine zeta zeros.

Its height is `G`, the cutoff `R_G` is comparable to `G`, and the right-half packet cardinality is

\[
d_G=(c+o(1))\log G,
\qquad c<0.10076.
\tag{33}
\]

Its entire vertical diameter is

\[
(d_G-1)\varepsilon_G
\le
\exp\bigl(-(1+o(1))(\log G)^3\bigr),
\tag{34}
\]

so the main Riemann--von Mangoldt contribution across that shrinking window is negligible. Reapplying the explicit endpoint error used in `NB-112`, `NB-132`, and `NB-133` permits at most

\[
(0.20152+o(1))\log G
\tag{35}
\]

zeros in the full critical strip inside such a window. Functional-equation symmetry pairs every off-critical right-half zero with a left-half mate at the same ordinate, so the corresponding right-half allowance is

\[
(0.10076+o(1))\log G.
\tag{36}
\]

Equation `(33)` lies strictly below that budget. The fixed horizontal location

\[
\Re\rho_G=\frac12+a<1
\tag{37}
\]

also lies safely to the left of the Vinogradov--Korobov zero-free boundary for all sufficiently large `G`. If desired, the formal packet can be completed by its functional-equation and conjugation partners without changing the right-half state calculation.

Hence the source information used in the recent `NB-132`--`NB-136` splice -- explicit local population allowance plus the standard near-one zero-free depth -- does not exclude packets for which **natural-prefix inversion is catastrophically ill-conditioned and target access nevertheless vanishes**. A minimum-spacing or other arrangement theorem would be genuinely new source information; it is not hidden in those two envelopes.

## 5. Representation audit and novelty boundary

There are three different objects here and they must not be conflated.

First, `(25)` is an ordinary power-coordinate evaluation matrix. Its condition number measures the instability of recovering coefficients attached to nearly coincident simple roots. The binomial witness `(26)` is exactly the classical near-confluence mechanism.

Second, `(11)` is an invertible divided-difference reparameterization of the **same finite state span**. At collision it converges to derivative/Jordan coordinates rather than losing a dimension. No packet information is discarded before the limit.

Third, `(23)` is the orthogonal projection of the actual finite Nyman target onto that span. It is invariant under every invertible change of packet coordinates. Thus neither the raw singular value in `(30)` nor the exploding triangular factors from canonical deflation can by themselves certify target rescue.

The general facts that clustered Vandermonde matrices become ill-conditioned and that divided differences converge to confluent/Hermite coordinates are classical. Modern superresolution work quantifies the singular-value loss of clustered Vandermonde and partial Fourier matrices, including its dependence on local cluster multiplicity. No novelty is claimed for those numerical-analysis phenomena. The line-local contribution is the splice with the exact Nyman geometry: `NB-111` supplies a growing-rank, fully backfilled, **target-aware** confluent obstruction, while `(11)`--`(23)` transfer that obstruction to distinct simple packets and `(27)`--`(32)` simultaneously force arbitrarily bad natural-prefix conditioning.

A targeted prior-art search found the expected clustered-Vandermonde/superresolution literature, but no Nyman--Beurling result identifying this coexistence of a confluence-driven conditioning collapse with vanishing finite-target access. No external theorem is load-bearing in the derivation above, so no new source anchor is required.

## 6. What this closes and what remains open

`NB-136` left two possible readings of its superpolynomial conditioning collapse. One was optimistic: perhaps the tiny singular directions exposed a hidden finite-section route by which a high zero packet could mimic the target. The other was representational: perhaps ordinary zero-power coordinates simply become singular as distinct roots approach a confluent jet. `NB-137` separates them. The second phenomenon can occur while the canonical state range is provably target-poor.

This does **not** show that every clustered packet is target-poor. The spacing threshold `ε_*(G,eta_G)` in `(14)` is existential and may be extremely small; the construction deliberately exploits the absence of any source-specific lower-spacing law. Nor does it show that actual zeta zeros realize the matched packet. It only proves that population and horizontal-depth information, even supplemented by the complete natural prefix, cannot turn raw packet conditioning into a target certificate.

The surviving problem is therefore sharper. A useful source-specific condition must control a **target-aware quotient** of the packet geometry: for example, the angle of the canonical state range to the harmonic target profile of `NB-117`, or the mass of the actual coefficient vector on target-bearing compression modes. Alternatively, a spacing/arrangement theorem strong enough to prevent the confluence regime would remove this matched control. Simply adding more samples to an ordinary Vandermonde inversion no longer addresses the relevant obstruction.