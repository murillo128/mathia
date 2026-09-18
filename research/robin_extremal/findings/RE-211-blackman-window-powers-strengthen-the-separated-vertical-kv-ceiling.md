# RE-211 — Blackman-window powers strengthen the separated vertical KV ceiling

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + WEIGHTED-PRIMITIVE-LOWER-BOUND + COMPACT-SUPPORT-WINDOW-SHAPING + ORDINARY-PRIME-SOURCE + SELECTOR-DEBT-SCALE + CHEBYSHEV-PREFIX-COERCIVITY + KV-BARRIER + INTEGER-MULTIPLICITIES`.

**Parent finding:** RE-210.

`RE-210` shows that the repeated-uniform compact-support test is substantially stronger when its true sinc sidelobes are retained: hiding a selector-scale local Euler packet from the whole interval `|t|<=T` across a fixed logarithmic repair gap `H` forces

\[
\log R\ge (\gamma_\star+o(1))HT,
\qquad
\gamma_\star=0.5979019108\ldots .
\]

That constant is exact for the optimized sinc-power tail used there, but it is not an extremal constant over all nonnegative compactly supported tests. Replacing the uniform base density by a normalized three-term Blackman density gives a strictly stronger certified rate

\[
\boxed{\gamma_B=0.7415820315\ldots .}
\tag{1}
\]

The arithmetic pullback is unchanged. Consequently every separated ordinary-prime `{0,1,2}` repair that hides the local selector-scale packet from `|t|<=T_Q` while preserving every fixed Korobov--Vinogradov envelope must satisfy

\[
\boxed{
\frac{\frac12\log Q-\gamma_BHT_Q}{V(Q)}\longrightarrow+\infty,
\qquad
V(Q)=\frac{(\log Q)^{3/5}}{(\log\log Q)^{1/5}}.
}
\tag{2}
\]

For `T_Q=c log Q` and the current corridor `H=log 8`, this lowers the universal ceiling from `0.4021548838...` to

\[
\boxed{c<0.3242381331\ldots .}
\tag{3}
\]

The constructive range from `RE-208`, `c<0.0289079...`, is unchanged. Thus the remaining factor between the explicit constructive and coercive constants drops from about `13.9` to about `11.2` without changing the source architecture.

## 1. A nonnegative Blackman density with an elementary transform

Define on `[-1,1]`

\[
b(t):=\frac{21+25\cos(\pi t)+4\cos(2\pi t)}{42}
=\frac{(1+\cos\pi t)(17+8\cos\pi t)}{42},
\tag{4}
\]

and put `b(t)=0` outside this interval. The factorization in (4) shows `b>=0`, and the cosine terms integrate to zero, so `int b=1`. It is therefore an admissible probability density for the same averaging argument as `RE-209`--`RE-210`.

Its Fourier transform is obtained by integrating the three cosine terms directly:

\[
B(x):=\int_{-1}^1 b(t)e^{-ixt}\,dt
=\frac{\pi^2(28\pi^2-3x^2)\sin x}
{7x(x^2-\pi^2)(x^2-4\pi^2)},
\tag{5}
\]

with the apparent singularities interpreted removably. This is the continuous centered form of the classical `0.42,0.50,0.08` Blackman window; no signal-processing result is used below, because the tail bound needed here follows directly from (5).

Set

\[
M_B:=\frac1{700}.
\tag{6}
\]

Let `a_B` be the last solution in `(2pi,3pi)` of

\[
B(a_B)=M_B.
\tag{7}
\]

Numerically,

\[
a_B=8.8339253870\ldots .
\tag{8}
\]

By the definition of the last crossing and `B(3pi)=0`, `|B(x)|<=M_B` on `[a_B,3pi]`. The same bound holds globally beyond `3pi`. Indeed, for `r=x/pi>=3`, (5) gives

\[
|B(x)|\le
\frac{|28-3r^2|}{7\pi r(r^2-1)(r^2-4)}.
\tag{9}
\]

For `3<=r<=sqrt(28/3)`, the numerator is at most `1` and the denominator is at least `840pi`, so (9) is smaller than `1/700`. For `r>=sqrt(28/3)`, using only `pi>3`, the desired inequality follows from

\[
P(r):=3r^5-15r^3-300r^2+12r+2800>0.
\tag{10}
\]

This last algebraic check is exact: a Sturm sequence for `P` has the same number of sign variations at `r=3` and at `+infinity`, hence no zero on `[3,infinity)`, while `P(3)=460>0`. Therefore

\[
\boxed{\sup_{x\ge a_B}|B(x)|\le\frac1{700}.}
\tag{11}
\]

The bound is deliberately conservative. The classical Blackman window is known for a roughly `-58 dB` worst sidelobe; (11) certifies only the slightly weaker level needed for a clean exact argument.

## 2. Convolution powers convert the improved tail into a stronger prefix tariff

Let `nu` be a finite real signed measure supported on `[H,infinity)` and suppose

\[
\sup_{|t|\le T}|1-\widehat\nu(t)|\le\epsilon,
\qquad 0\le\epsilon<1.
\tag{12}
\]

As in `RE-209`, define

\[
G(L):=\int_{[H,L]}e^u\,d\nu(u),
\qquad
R:=\sup_{L\ge H}e^{-L}|G(L)|.
\tag{13}
\]

Assume `HT->infinity` and choose

\[
n:=\left\lfloor\frac{HT}{a_B}\right\rfloor.
\tag{14}
\]

Scale (4) to a probability density `v_n(t)=(n/T)b(nt/T)` supported on `[-T/n,T/n]`, and let `w_n=v_n^{*n}`. Then `w_n` is a nonnegative probability density supported on `[-T,T]`, with Fourier transform

\[
\phi_n(L)=B(LT/n)^n.
\tag{15}
\]

Pairing (12) against `w_n` gives

\[
\left|\int\phi_n(L)\,d\nu(L)\right|\ge1-\epsilon.
\tag{16}
\]

Using `dnu=e^{-L}dG` and integrating by parts exactly as in `RE-209`--`RE-210`,

\[
1-\epsilon
\le
R\int_H^\infty\left(|\phi_n'(L)|+|\phi_n(L)|\right)dL.
\tag{17}
\]

Since `n<=HT/a_B`, every `L>=H` has `x=LT/n>=a_B`. On each fixed compact interval, (11) and boundedness of `B'` give a contribution `O(nM_B^{n-1})`. From (5), `B(x)=O(x^{-3})` and `B'(x)=O(x^{-3})`; choosing one fixed far-tail cutoff where the polynomial envelope is strictly below `M_B` makes the remaining integral exponentially smaller. Hence

\[
\int_H^\infty\left(|\phi_n'|+|\phi_n|\right)dL
\ll_H nM_B^{n-1}.
\tag{18}
\]

Combining (17)--(18),

\[
\log R
\ge
\left(\frac{\log700}{a_B}+o(1)\right)HT.
\tag{19}
\]

Thus

\[
\boxed{
\gamma_B:=\frac{\log700}{a_B}
=0.7415820315\ldots .
}
\tag{20}
\]

Compared with `gamma_*=0.5979019108...`, window shaping increases the certified exponent by about `24%`.

## 3. The ordinary-prime pullback is unchanged

Use the arithmetic setup of `RE-209`--`RE-210`: a local packet of

\[
B_Q\asymp\frac{\sqrt Q}{\log Q}
\]

ordinary primes near `X_0=2Q`, followed only after the fixed logarithmic gap `H` by remote ordinary-prime edits with coefficients in `{-1,+1}`. Assume `T_Q=O(log Q)` and the exact Euler discrepancy is `o(d_Q)` uniformly on `|t|<=T_Q`, where

\[
d_Q=\frac1{\sqrt Q\log Q}.
\]

After normalization by `X_0/B_Q`, the local first harmonic is `1+o(1)`, the exact prime-power remainder is `o(1)`, and the remote first harmonics define the same measure `nu_Q` as in `RE-210`. Its weighted primitive is exactly a signed prime-count prefix. Therefore (19) gives

\[
\sup_{L\ge H}e^{-L}|C_Q(X_0e^L)|
\ge
B_Q\exp\left((\gamma_B+o(1))HT_Q\right).
\tag{21}
\]

The maximal-prefix partial summation from `RE-209` is representation-independent and therefore unchanged:

\[
\boxed{
\sup_{x\ge X_0e^H}
\frac{|\Delta\vartheta_Q(x)|}{x}
\ge
Q^{-1/2}
\exp\left((\gamma_B+o(1))HT_Q\right).
}
\tag{22}
\]

If every affected scale must remain inside every fixed KV envelope, (22) forces (2). For `T_Q=c log Q`,

\[
c<\frac1{2\gamma_BH}.
\tag{23}
\]

With `H=log 8`, this is exactly the numerical ceiling in (3).

## 4. Negative control: smoothing alone does not explain the gain

A natural falsification is to replace the uniform density by the triangular density

\[
\tau(t)=1-|t|,
\qquad |t|\le1.
\tag{24}
\]

Its transform is

\[
\widehat\tau(x)=\left(\frac{\sin(x/2)}{x/2}\right)^2.
\tag{25}
\]

Applying the same convolution-power optimization to (25) merely doubles both the threshold location and the logarithmic attenuation of the optimized sinc tail. The ratio is therefore unchanged:

\[
\frac{2\log(1/M_\star)}{2a_\star}=\gamma_\star.
\tag{26}
\]

So the improvement in (20) is not a generic consequence of making the test smoother or convolving once more. It comes from changing the sidelobe/main-lobe tradeoff of the base compact-support window.

## 5. Representation audit, prior art and boundary

The Blackman window itself is classical signal-processing prior art, not a new object. Standard references give the `0.42,0.50,0.08` coefficients and its low-sidelobe motivation; see F. J. Harris, *On the use of windows for harmonic analysis with the discrete Fourier transform*, Proceedings of the IEEE 66(1), 1978, DOI `10.1109/PROC.1978.10837`. The proof here does not depend on a tabulated Blackman sidelobe theorem: nonnegativity, normalization, transform (5), and the conservative global bound (11) are derived directly.

The generic part of the argument is Fourier/spectral-gap geometry. The source-specific Mathia content is the same as in `RE-209`--`RE-210`: the weighted primitive becomes an actual signed ordinary-prime prefix, and that prefix forces a Chebyshev excursion constrained by KV fidelity. No new external theorem is load-bearing, so `SOURCES.md` needs no change.

The constant `gamma_B` is **not** claimed optimal, even within the Blackman family: `1/700` was chosen for an elementary global certificate. More importantly, no upper bound is proved for the natural compact-support extremal functional

\[
\Gamma(w):=
\sup_{a>0}
\frac{-\log\sup_{|x|\ge a}|\widehat w(x)|}{a},
\tag{27}
\]

where `w` ranges over nonnegative probability densities supported on `[-1,1]` with enough regularity to control the derivative tail. `RE-211` proves only

\[
\sup_w\Gamma(w)\ge\gamma_B=0.7415820315\ldots .
\tag{28}
\]

The finding also retains every boundary of `RE-210`: the repair is separated by a fixed pre-repair logarithmic gap; edits are ordinary primes with the stated integer multiplicities; the local packet has selector-scale mass; and the repair must respect every fixed KV envelope. It does not prove Robin, address zero-gap repairs, or show that a hypothetical Robin counterexample supplies the continuum vertical observation.

## Research consequence

The coercive side is now a concrete compact-support window-design problem rather than a question about the sinc family. `RE-210` optimized the uniform window internally; `RE-211` proves that changing the window strictly beats that optimum. The next obstruction-side step is therefore to bound or optimize `Gamma(w)` under positivity and compact support. On the constructive side the dual target remains unchanged: directly control signed weighted prefixes rather than only absolute coefficient variation. The current two-sided logarithmic-height interval for `H=log 8` is

\[
0<c<0.0289079\ldots
\quad\text{constructed},
\qquad
c\ge0.3242382\ldots
\quad\text{excluded within the separated KV architecture}.
\]
