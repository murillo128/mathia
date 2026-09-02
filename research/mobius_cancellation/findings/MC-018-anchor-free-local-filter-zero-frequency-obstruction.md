# MC-018 — Anchor-free local linear filters cancel the inverse-summation low-frequency gain

**Status:** `EXACT-DERIVED`, `DECISIVE-NEGATIVE`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

The low-frequency carrier isolated in `MC-017` cannot be recovered from a **single finite translation-invariant local linear statistic of the partial-sum process without paying an explicit scale loss**.

Let a sequence `a(n)` have a primitive

\[
A(k)-A(k-1)=a(k).
\]

For fixed local radius `R`, choose complex weights `w_0,\dots,w_R` and define

\[
T_w(x)=\sum_{r=0}^{R}w_r A(x+r).
\tag{1}
\]

Write

\[
W=\sum_{r=0}^{R}w_r,\qquad
P_w(z)=\sum_{r=0}^{R}w_r z^r.
\tag{2}
\]

Then the following are equivalent:

1. `T_w(x)` is invariant under changing the unknown local anchor `A -> A+C`;
2. `T_w(x)` can be written using only the local increments `a(x+1),\dots,a(x+R)`;
3. `W=0`;
4. `P_w(1)=0`;
5. `P_w(z)` has the exact factorization
   \[
   P_w(z)=(z-1)Q_w(z).
   \tag{3}
   \]

More explicitly, with

\[
c_j=\sum_{r=j}^{R}w_r,
\qquad
Q_w(z)=\sum_{j=1}^{R}c_j z^{j-1},
\tag{4}
\]

one has, when `W=0`,

\[
\boxed{
T_w(x)=\sum_{j=1}^{R}c_j\,a(x+j).
}
\tag{5}
\]

Thus **removing dependence on the global prefix anchor forces a zero at the DC frequency of the partial-sum filter**. In the Fourier coordinates of `MC-017`, this zero cancels the inverse-summation factor that makes the path energy sensitive to the critical low-frequency core.

The loss is quantitative. Normalize the local filter by

\[
\|w\|_1=\sum_{r=0}^{R}|w_r|\le C.
\tag{6}
\]

For `z=e^{2\pi i t}`,

\[
|Q_w(z)|
\le \sum_{j=1}^{R}|c_j|
\le \sum_{r=1}^{R}r|w_r|
\le CR.
\tag{7}
\]

Equivalently,

\[
|P_w(e^{2\pi i t})|
\le 2\pi C R\,\|t\|
\tag{8}
\]

for distance `||t||` to the nearest integer. At the critical frequency `||t|| \asymp 1/N`, a genuinely local filter `R=o(N)` therefore has response `o(1)` on the partial-sum process, while the inverse-summation multiplier in `MC-017` has size `\asymp N` on the increment polynomial. A single bounded-mass local filter can supply at most `O(R)` gain on the increment polynomial there. Relative to the `O(N)` gain required by the primitive, it loses a factor `R/N`.

This is an algebraic obstruction, not a statistical one. It persists even if the local statistic retains signs perfectly and uses no absolute values.

## 1. Exact anchor/filter factorization

Expand every translated primitive around the same local anchor:

\[
A(x+r)=A(x)+\sum_{j=1}^{r}a(x+j).
\]

Substituting into (1),

\[
\begin{aligned}
T_w(x)
&=
\left(\sum_{r=0}^{R}w_r\right)A(x)
+
\sum_{r=0}^{R}w_r\sum_{j=1}^{r}a(x+j)\\
&=
W A(x)
+
\sum_{j=1}^{R}
\left(\sum_{r=j}^{R}w_r\right)a(x+j).
\end{aligned}
\tag{9}
\]

This proves (5) when `W=0`. Conversely, replacing `A(k)` by `A(k)+C` leaves all increments unchanged but changes `T_w(x)` by `CW`; therefore an expression depending only on the local increments is possible for every primitive only if `W=0`.

The polynomial factorization follows because `P_w(1)=W`. Directly,

\[
(z-1)\sum_{j=1}^{R}c_j z^{j-1}
=
\sum_{r=0}^{R}w_r z^r
\tag{10}
\]

when `W=0`.

The standard short-interval sum is exactly this mechanism. Taking `w_0=-1`, `w_H=1`, and all other weights zero gives

\[
A(x+H)-A(x)=\sum_{x<n\le x+H}a(n),
\tag{11}
\]

with

\[
P(z)=z^H-1=(z-1)(1+z+\cdots+z^{H-1}).
\tag{12}
\]

So the familiar local window is not merely one example among many: as a filter on the primitive, it exhibits the forced zero at `z=1` that every finite translation-invariant anchor-free linear statistic must have.

## 2. Relation to the `MC-017` path-energy carrier

For a finite horizon `N`, `MC-017` defines

\[
H_N(t)
=
F_N(t)-A(N-1)e^{2\pi iNt},
\qquad
F_N(t)=\sum_{n=1}^{N-1}a(n)e^{2\pi int},
\tag{13}
\]

and

\[
G_N(t)=\sum_{k=1}^{N-1}A(k)e^{2\pi ikt}.
\tag{14}
\]

The exact finite telescoping identity is

\[
(1-e^{2\pi it})G_N(t)=H_N(t),
\tag{15}
\]

hence

\[
V_a(N)=\sum_{k<N}|A(k)|^2
=
\int_0^1 |G_N(t)|^2\,dt
=
\int_0^1
\frac{|H_N(t)|^2}{|1-e^{2\pi it}|^2}\,dt.
\tag{16}
\]

An anchor-free filter has `P_w(z)=(z-1)Q_w(z)`. Therefore, up to an irrelevant sign,

\[
P_w(e^{2\pi it})G_N(t)
=
Q_w(e^{2\pi it})H_N(t).
\tag{17}
\]

The factor `(z-1)` has cancelled the inverse-summation denominator in (15). This is the precise information loss: the target norm keeps the low-frequency amplification `|1-e(t)|^{-1}`, whereas a local anchor-free linear observable replaces it by a bounded-degree polynomial `Q_w`.

With the normalization (6), (7) gives

\[
|Q_w(e^{2\pi it})|\le CR.
\tag{18}
\]

But on `||t||\asymp1/N`,

\[
|1-e^{2\pi it}|^{-1}\asymp N.
\tag{19}
\]

Thus a direct inversion from one such local observable to the primitive is ill-conditioned by at least order `N/R` at the critical core. Multiplying all weights by `N/R` does not create information: it multiplies both the observable and any input bound by the same factor. The relevant comparison is therefore made after a fixed operator normalization such as (6).

This explains structurally why `MC-001` and `MC-006` keep finding a polynomial information deficit. Their losses are not identical to the present one—those findings audit exceptional mass and an absolute correlation norm—but the usual local linear windows already operate after the inverse-summation singularity has been cancelled.

## 3. Boundary cancellation makes the missing coarse component explicit

The obstruction can also be seen without asymptotics. Define the finite boundary-cancelled coefficient sequence

\[
h_N(n)=
\begin{cases}
a(n),&1\le n\le N-1,\\
-A(N-1),&n=N,\\
0,&\text{otherwise}.
\end{cases}
\tag{20}
\]

Its Fourier polynomial is exactly `H_N(t)` from (13), and its total mass is zero.

For an integer window length `1\le L\le N`, define the sliding sums

\[
W_L(x)=\sum_{x<n\le x+L}h_N(n).
\tag{21}
\]

Let

\[
D_L(t)=\sum_{j=1}^{L}e^{2\pi ijt}.
\tag{22}
\]

Finite Parseval gives

\[
\sum_{x=1-L}^{N-1}|W_L(x)|^2
=
\int_0^1 |H_N(t)|^2|D_L(t)|^2\,dt.
\tag{23}
\]

The time-side quantity has the exact decomposition

\[
\boxed{
\begin{aligned}
\sum_{x=1-L}^{N-1}|W_L(x)|^2
={}&
\sum_{k=1}^{L-1}|A(k)|^2\\
&+\sum_{x=0}^{N-L-1}|A(x+L)-A(x)|^2\\
&+\sum_{x=N-L}^{N-1}|A(x)|^2.
\end{aligned}
}
\tag{24}
\]

The middle term is the ordinary length-`L` short-interval energy of the increments. The two boundary terms are pieces of the primitive energy itself. They arise because the endpoint correction `-A(N-1)` that makes `H_N(0)=0` is global data.

For even `N` and `L=N/2`, the first and third terms in (24) partition all of

\[
V_a(N)=\sum_{k=1}^{N-1}|A(k)|^2.
\tag{25}
\]

Therefore a Gallagher/Selberg-style attempt to control the boundary-cancelled Fourier polynomial through sliding short sums does not magically reduce `V_a` to interior short-interval cancellation: at a macroscopic window the exact boundary bookkeeping already contains the target path energy. At small windows the interior statistic is genuinely local, but the scale ratio from Section 2 remains.

This is a finite identity, not a heuristic about uncertainty or wavelets.

## 4. Prior art and novelty assessment

The factorization `P(1)=0 => P(z)=(z-1)Q(z)`, finite-difference annihilation of constants, and the interpretation of zero-mean local filters as removing the DC/coarse component are classical. In wavelet/filter-bank language, vanishing moments suppress low-order coarse modes and a multiresolution reconstruction retains a separate scaling/coarse component; see Ingrid Daubechies, *Ten Lectures on Wavelets*, SIAM, 1992, DOI `10.1137/1.9781611970104`.

Likewise, relating mean-square exponential sums to short-interval or Selberg-type sums is classical Gallagher-lemma territory. A directly relevant modern reference is Giovanni Coppola and Maurizio Laporta, *A modified Gallagher's Lemma*, arXiv `1301.0008`, and their *A generalization of Gallagher's lemma for exponential sums*, arXiv `1411.1739`.

No novelty is claimed for those harmonic-analysis mechanisms, for short-interval differencing, or for Parseval. The line-specific derived content is narrower: combining the exact `MC-017` boundary-cancelled primitive identity with the anchor-free filter factorization shows that **the same condition that removes the unknown local Mertens anchor also cancels the inverse-frequency gain whose weighted norm is the active path-energy carrier**. Equation (24) then makes the boundary/coarse information reappear explicitly when one tries to apply short-window Fourier machinery to `H_N`.

A targeted prior-art search found the classical filter/wavelet and Gallagher frameworks above. The result is therefore classified as an exact obstruction built from classical mechanisms, not as a new theorem of harmonic analysis or analytic number theory.

## 5. Boundaries and escape routes

This finding does **not** prove that local methods, short intervals, wavelets, or multiscale methods cannot contribute to Möbius cancellation. It rules out a narrower but broad direct strategy: choose a finite translation-invariant linear statistic of `M`, require it to depend only on local Möbius increments, and expect that statistic alone to retain the critical inverse-summation gain without a scale cost.

Several escape routes remain mathematically real:

- use filters with support `R\asymp N`, which are no longer local at the target horizon;
- retain an explicit coarse/scaling coefficient or other global anchor together with local detail coefficients;
- combine many scales with a proved frame/reconstruction inequality whose total low-frequency conditioning is audited rather than hidden;
- use a nonlinear or multiplicative identity that reconstructs the coarse mode from local arithmetic data;
- use non-translation-invariant or boundary-aware statistics whose extra anchor information is independently controllable;
- exploit a theorem that couples exceptional/local pieces coherently enough to pay the `N/R` reconstruction cost.

The statement is also per normalized filter. A sufficiently rich family of local filters may collectively encode global information, just as all first differences plus one boundary value determine a sequence. Any such route must identify and control the missing coarse datum or the aggregate conditioning; it cannot infer success merely from the strength of each local detail estimate.

The finding does not establish a new bound for `M(x)` or `V_M(N)`, and it does not rely on the still-audited Pintz implication in `MC-009`.

## Consequences for the active clue

`MC-017` localized the remaining mean-absolute route to boundary-cancelled inverse-frequency energy. The present obstruction eliminates a natural but overly broad repair: **replacing the existing short-window statistic by another finite zero-mean local linear filter does not restore the missing low-frequency primitive information**. Anchor removal itself forces the factor that cancels it.

The next useful transfer candidate must therefore make the coarse component explicit. A decisive continuation should do one of the following:

1. exhibit an arithmetic multiscale decomposition with an independently bounded coarse/scaling coefficient and prove that its detail bounds sum at `N^(2+epsilon)` path-energy scale;
2. derive a nonlinear or multiplicative relation that controls the critical `1/N` core without first assuming Mertens-scale cancellation;
3. construct a multiplicative exact-support comparator showing that a proposed coarse/local reconstruction still allows superquadratic `V_a(N)`.

This narrows the active question from generic "local Fourier control" to a precise **coarse-mode reconstruction problem**.
