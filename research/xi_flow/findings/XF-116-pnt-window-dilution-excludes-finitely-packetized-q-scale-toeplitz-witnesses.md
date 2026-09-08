# XF-116 — PNT window dilution excludes finitely packetized q-scale Toeplitz witnesses

**Status:** `EXACT-DERIVED` + `SOURCE-SPECIFIC` + `PNT-WINDOW-DILUTION` + `NON-PLANE-WAVE-GATE`. XF-115 proved that every degree-`K` plane-wave/Fejer test of the mass-preserving Xi source is asymptotically positive on the full mesh-angle circle, but explicitly left open nonuniform and multi-packet coefficient vectors. The simplest such escape is a finite-section corner mode: place coefficient mass in a few narrow index packets separated by q-scale distances, so that their cross-interactions sample high Toeplitz lags which a single Fejer translate suppresses. For the actual Xi source, this mechanism cannot remain packetized on a vanishing physical lag scale.

Keep the mass-preserving source interface of XF-108--XF-115,

\[
N=2q^2,
\qquad
\Delta^2\asymp q^{-3},
\qquad
a:=N\Delta\asymp q^{1/2},
\qquad
\Delta\asymp a^{-3},
\tag{1}
\]

with

\[
L=\log a+c,
\qquad
K=\left\lfloor\frac L\Delta\right\rfloor,
\qquad c\in\mathbf R\text{ fixed},
\tag{2}
\]

and normalized moments

\[
\widehat\mu_0=1,
\qquad
\widehat\mu_m
=
\frac{\Delta}{a}B(m\Delta)
-
\frac1{2a}
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
\omega_\psi\!\left(m,\frac{\lambda_n}{\Delta}\right),
\qquad
\lambda_n=\frac12\log n,
\tag{3}
\]

where `omega_psi` is the nonnegative mass-preserving deposition from XF-108 and `sum_m omega_psi(m,u)=1`.

For `0<h<=1`, define the largest absolute source mass in a physical lag window of width `h`,

\[
\mathfrak W_a(h)
:=
\sup_{0\le u\le L}
\sum_{\substack{1\le m\le K\\m\Delta\in[u,u+h]}}
|\widehat\mu_m|.
\tag{4}
\]

Then there is `c_0>0` such that

\[
\boxed{
\mathfrak W_a(h)
\ll_{\psi,c}
 h
+a^{-1/2}
+e^{-c_0\sqrt{\log a}}
+\frac{\log a}{a}.
}
\tag{5}
\]

In particular,

\[
\boxed{
\lim_{h\downarrow0}
\limsup_{a\to\infty}
\mathfrak W_a(h)=0.
}
\tag{6}
\]

This absolute-continuity statement is stronger than the pointwise dilution of XF-106 and is different from the full-circle Fejer cancellation of XF-115: it controls the **total absolute Toeplitz mass in every narrow physical lag window**, uniformly over where the window sits in the entire q-scale prefix.

The matrix consequence is immediate but restrictive. Suppose a principal coordinate set `S_a subset {0,...,K}` can be covered by `p` index intervals, where `p` is fixed and every covering interval has physical diameter at most `h_a`, meaning index diameter at most `h_a/Delta+O(1)`. Then

\[
\boxed{
\|\widehat T_{S_a}-I\|_{\rm op}
\le
2p\,\mathfrak W_a(h_a+O(\Delta)),
}
\tag{7}
\]

and consequently

\[
\boxed{
h_a\to0
\quad\Longrightarrow\quad
\lambda_{\min}(\widehat T_{S_a})=1-o(1).
}
\tag{8}
\]

For every fixed packet count `p`, there is therefore a fixed physical width `h_p>0` such that every sufficiently large `p`-packet principal section with packet widths at most `h_p` has, say, `lambda_min>=1/2`. A nonpositive q-scale Toeplitz witness cannot be a bounded number of shrinking coefficient packets, no matter how far apart those packets are.

## 1. Mass-preserving deposition turns a lag window into one logarithmic prime interval

From `(3)` and nonnegativity of `omega_psi`, for a mesh window

\[
I=[u,u+h]
\]

one has

\[
\begin{aligned}
\sum_{m\Delta\in I}|\widehat\mu_m|
&\le
\frac\Delta a
\sum_{m\Delta\in I}|B(m\Delta)|\\
&\quad+
\frac1{2a}
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\sum_{m\Delta\in I}
\omega_\psi\!\left(m,\frac{\lambda_n}{\Delta}\right).
\end{aligned}
\tag{9}
\]

The deposition has support one mesh cell from `lambda_n`. Its inner sum in `(9)` is at most one, and it vanishes unless

\[
\lambda_n\in
[u-O(\Delta),u+h+O(\Delta)].
\tag{10}
\]

Thus an arbitrary location of the mesh relative to the prime-power atom cannot amplify the window mass: every atom is charged at most once. This is exactly where the mass normalization introduced in XF-108 is load-bearing.

Write the corresponding integer interval as

\[
X=e^{2u+O(\Delta)},
\qquad
Y=e^{2(u+h)+O(\Delta)}.
\tag{11}
\]

The prime contribution in `(9)` is bounded by

\[
\frac1{2a}
\sum_{X\le n\le Y}
\frac{\Lambda(n)}{\sqrt n}.
\tag{12}
\]

There are two uniform regimes. If the upper logarithmic endpoint is at most `(1/2)log a+O(1)`, the Chebyshev estimate already used in XF-104 gives

\[
\sum_{n\le Y}\frac{\Lambda(n)}{\sqrt n}
\ll\sqrt Y,
\]

hence `(12)=O(a^{-1/2})` for `h<=1`.

If the window reaches above that split, then because `h<=1` its lower endpoint satisfies `X\gg a`. The classical prime-number-theorem error used in XF-108,

\[
\Psi(x)=x+O\!\left(xe^{-c\sqrt{\log x}}\right),
\tag{13}
\]

is therefore uniform throughout `[X,Y]` with an error

\[
E_a:=e^{-c_0\sqrt{\log a}}.
\tag{14}
\]

Since `Y/X=e^{O(h+Delta)}`,

\[
\Psi(Y)-\Psi(X^-)
\ll
Y(h+\Delta+E_a).
\tag{15}
\]

Using `n^{-1/2}<=X^{-1/2}` in `(12)` and `sqrt X/a<=e^L/a=O_c(1)` gives

\[
\boxed{
\frac1{2a}
\sum_{X\le n\le Y}
\frac{\Lambda(n)}{\sqrt n}
\ll_c h+\Delta+E_a+a^{-1/2}.
}
\tag{16}
\]

No short-interval prime theorem is being imported here. The interval has fixed or shrinking **multiplicative** width, and the ordinary quantitative PNT is enough because its endpoint error is already `o(x)` uniformly on the upper half of the q-scale logarithmic band.

## 2. The archimedean background has the same uniform absolute continuity

XF-052 gives

\[
B(\xi)
=e^\xi-
\frac{e^{-5\xi}}{1-e^{-4\xi}}.
\tag{17}
\]

The exponential part contributes, uniformly in `u`,

\[
\frac\Delta a
\sum_{m\Delta\in[u,u+h]}e^{m\Delta}
\ll_c h+\Delta,
\tag{18}
\]

because `e^L/a=e^c`. The second term in `(17)` is exponentially summable away from zero and behaves like `1/(4xi)` at zero. Its worst possible window is therefore the initial one, where

\[
\frac\Delta a
\sum_{1\le m\le h/\Delta+O(1)}
\frac1{m\Delta}
\ll
\frac{\log(1/\Delta)}a
\ll
\frac{\log a}{a}.
\tag{19}
\]

Equations `(9)`, `(16)`, `(18)`, and `(19)`, together with `Delta asymp a^{-3}`, prove `(5)` and `(6)`.

The important feature is uniformity in the window center. Below the q-scale edge, Chebyshev makes the whole accumulated prime mass small after normalization; near the edge, PNT controls the difference of the two endpoint masses. There is no intermediate logarithmic region in which a vanishing-width lag window can retain order-one absolute source mass.

## 3. A finite number of shrinking coefficient packets is asymptotically invisible

Let `S_a` be covered by index intervals `J_1,...,J_p` as above. Fix a row index `i in S_a`. For a fixed packet `J_r`, the differences `i-j` with `j in J_r` occupy one signed lag interval of physical width at most `h_a+O(Delta)`. If that interval crosses lag zero, split it once into positive and negative pieces. Since

\[
|\widehat\mu_{-m}|=|\widehat\mu_m|,
\]

the total off-diagonal row mass contributed by `J_r` is at most

\[
2\mathfrak W_a(h_a+O(\Delta)).
\tag{20}
\]

Summing over the fixed `p` packets gives

\[
\max_{i\in S_a}
\sum_{\substack{j\in S_a\\j\ne i}}
|\widehat\mu_{i-j}|
\le
2p\mathfrak W_a(h_a+O(\Delta)).
\tag{21}
\]

The Rayleigh quotient or Gershgorin then proves `(7)`. Substitution of `(5)` proves `(8)` whenever `p` is fixed and `h_a->0`.

There is also a fixed-width version. From `(5)` there is a constant `C_{psi,c}` such that

\[
\limsup_{a\to\infty}\mathfrak W_a(h)
\le C_{\psi,c}h.
\tag{22}
\]

For any fixed `p`, choose `h_p>0` with `2p C_{psi,c}h_p<1/4`. Then `(7)` gives

\[
\lambda_{\min}(\widehat T_{S_a})\ge\frac12
\tag{23}
\]

for all sufficiently large `a`. Thus the exclusion is not merely qualitative: every bounded packet count has a fixed positive physical resolution below which q-scale Toeplitz negativity is impossible.

## 4. The corner/Hankel escape left by XF-115 must have fixed physical thickness

A natural adversary to XF-115 places coefficients in two packets, one near index zero and one near index `K`. Their self-interactions use small lags, while their cross-interactions use terminal lags near `K`; after reversing one edge block, the latter are a finite Hankel/corner channel. A single plane wave suppresses those terminal moments by the Fejer factor

\[
1-\frac m{K+1}
=\frac{K+1-m}{K+1},
\tag{24}
\]

so full-circle plane-wave flatness alone does not control the corner norm.

Equation `(23)` supplies the missing source-specific restriction. If both edge packets have physical widths tending to zero, the entire two-packet principal section tends to the identity even though its total coordinate diameter is

\[
K\Delta=L=\log a+O(1),
\]

exactly the q-scale span required by XF-107. More quantitatively, any nonpositive two-packet corner witness must have at least one packet whose physical width is bounded below by a positive constant depending only on the fixed source interface. In index units that means a packet diameter of order at least

\[
\boxed{
\Delta^{-1}\asymp a^3\asymp q^{3/2}.
}
\tag{25}
\]

This is a geometric width statement, not a cardinality statement: the packet may still be sparse inside that interval. XF-111 independently requires broad support cardinality. Together they show that the remaining non-plane-wave witness cannot be a thin boundary crystal with many coefficients packed into an asymptotically vanishing physical strip.

For a genuine two-edge corner channel, a terminal lag strip of physical width `h_a=o(1)` corresponds through `lambda_n=(log n)/2` to an arithmetic interval

\[
[e^{2L-O(h_a)},e^{2L}]
=
q\,[e^{-O(h_a)},1]
\tag{26}
\]

up to the fixed normalization constants in `(1)`--`(2)`. Its relative width is `O(h_a)`. Hence `(8)` rules out a bounded-packet corner obstruction supported only by a `q(1+o(1))` arithmetic boundary layer. Any such corner route must reach a fixed multiplicative depth into the q-scale arithmetic data.

## 5. Adversarial control: full-circle Fejer flatness still does not imply PSD at fixed packet width

The new theorem should not be over-read as Toeplitz positivity. An abstract Toeplitz control can satisfy all earlier coarse gates and the XF-115 plane-wave conclusion while retaining a fixed-width corner instability.

Fix a small constant `h_*>0`, take an even integer

\[
R\sim\frac{h_*}{\Delta},
\qquad R=o(K),
\tag{27}
\]

and put, for `K-R+1<=m<=K`,

\[
\nu_m
=-\frac5R\cos\frac{\pi m}{2},
\qquad
\nu_m=0\text{ otherwise},
\qquad
\nu_0=1.
\tag{28}
\]

Then

\[
\max_m|\nu_m|=O(R^{-1})=O(\Delta),
\qquad
\sum_m|\nu_m|=O(1),
\qquad
\sum_m|\nu_m|^2=O(R^{-1})=O(\Delta),
\tag{29}
\]

so the pointwise and `ell^2` dilution gates of XF-106/XF-110 are comfortably satisfied. Its Fejer plane-wave average obeys uniformly in `theta`

\[
\begin{aligned}
\left|
2\sum_{m=1}^K
\left(1-\frac m{K+1}\right)
\nu_m\cos(m\theta)
\right|
&\le
\frac{10}{R(K+1)}
\sum_{r=0}^{R-1}(r+1)\\
&=O\!\left(\frac RK\right)
=O\!\left(\frac1{\log a}\right)
=o(1).
\end{aligned}
\tag{30}
\]

Thus every plane wave sees `1+o(1)` exactly as in the conclusion of XF-115.

Nevertheless take the unit vector supported on the first and last `R` coordinates,

\[
v_j=(2R)^{-1/2}e^{-i\pi j/2}
\]

on those two blocks and zero elsewhere. For terminal lag `m=K-r`, `0<=r<R`, its autocorrelation has magnitude `(r+1)/(2R)` and phase `e^{-i\pi m/2}`. Hence

\[
v^*T(\nu)v
=
1-
\frac5{R^2}
\sum_{r=0}^{R-1}
(r+1)\cos^2\!\frac{\pi(K-r)}2.
\tag{31}
\]

For even `R`, the weighted parity sum is at least `R^2/4`, so

\[
\boxed{
v^*T(\nu)v\le-\frac14.}
\tag{32}
\]

Because the matrix is real symmetric, one of `Re v` or `Im v` is already a real negative Rayleigh direction. This control confirms the boundary of the theorem: full-circle Fejer flatness plus coefficient dilution does not remove fixed-physical-width corner modes. What excludes *shrinking* corner packets for Xi is the new source-specific window estimate `(5)`, not an abstract property of Toeplitz matrices.

## 6. Stress tests, prior art, and the live frontier

The proof uses positivity and exact mass preservation of the deposition weights. If the extractor were allowed signed mesh weights with large cancellation, the passage from `(9)` to one logarithmic prime interval would fail. This is the same interface issue that XF-108 fixed before invoking PNT. The result also uses only the ordinary quantitative prime number theorem already load-bearing in XF-108; it does not assume RH and does not require a prime theorem in genuinely short additive intervals.

The packet count `p` must stay fixed in `(8)`. If `p=p(a)` grows, `(7)` only gives the useful condition

\[
p(a)\,\mathfrak W_a(h_a)=o(1).
\tag{33}
\]

Thus a negative witness may still evade by increasing its coefficient-space packet complexity while shrinking packet width. Nor does `(25)` imply `Omega(a^3)` nonzero coefficients: it forces geometric packet diameter, not density. The theorem also does not control a vector already spread throughout a fixed positive fraction of the full physical interval `[0,L]`; that remains the principal source-side PSD frontier.

Finite-section and boundary effects for Toeplitz operators are classical; a directed prior-art check found the standard finite-section literature, including Böttcher--Silbermann and later work on singular values of finite Toeplitz sections. No novelty is claimed for Gershgorin, finite-section corner blocks, or the prime number theorem. The line-specific delta is the uniform q-dependent estimate `(5)` for the Guinand--Weil/Vieta source moments and its consequence `(8)` for coefficient-packet complexity. No new external theorem is load-bearing, so `SOURCES.md` needs no change.

The live source-side gate after XF-115 is therefore narrower. A possible negative eigenvector must be non-plane-wave **and** cannot be assembled from a bounded number of physically shrinking coefficient packets. In the corner/Hankel channel it must penetrate a fixed physical distance, hence a fixed multiplicative fraction of the natural q arithmetic scale. The next useful attack is to control fixed-width and growing-packet quadratic forms using the actual signed PNT discrepancy, rather than continuing to sharpen plane-wave Fejer averages.