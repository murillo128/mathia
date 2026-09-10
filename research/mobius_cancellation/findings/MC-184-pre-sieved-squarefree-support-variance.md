# MC-184 — Logarithmic pre-sieving preserves squarefree short-interval variance up to subpower loss

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-183` separated the logarithmically rough Möbius coefficient

\[
g_y(n)=\mu(n)\mathbf 1_{P^-(n)>y}
\]

into two unsigned/signed layers,

\[
\alpha_y(n)=\mathbf 1_{P^-(n)>y},
\qquad
\beta_y(n):=|g_y(n)|=\mu^2(n)\alpha_y(n),
\qquad
g_y(n)=\mu(n)\alpha_y(n),
\]

and showed that the standard rough-number variance controls only the larger periodic envelope `alpha_y`. The first missing operation was therefore the restoration of square-free support `alpha_y -> beta_y`; the second was restoration of Möbius parity `beta_y -> g_y`.

For the polynomial-window range in which the best unconditional squarefree variance theorem is available, the first missing layer is **not** a fixed-power variance obstruction. Fix

\[
H=X^\theta,
\qquad
0<\theta<\frac6{11},
\qquad
y=c\log X,
\qquad
0<c<\min(\theta,1-\theta).
\tag{1}
\]

Let

\[
\rho_y
:=
\prod_{p\le y}\left(1-\frac1p\right)
\prod_{p>y}\left(1-\frac1{p^2}\right)
\tag{2}
\]

be the density of square-free integers with no prime factor at most `y`, and put

\[
B_y(x,H)
:=
\sum_{x<n\le x+H}\beta_y(n)-\rho_yH.
\tag{3}
\]

Then, unconditionally,

\[
\boxed{
\int_X^{2X}|B_y(x,H)|^2\,dx
\le X^{1+o(1)}H^{1/2}.
}
\tag{4}
\]

The `o(1)` may depend on the fixed `theta` and `c`. Thus at every fixed `theta<6/11`, the actual unsigned support of the rough Möbius coefficient has a centered local variance much smaller than the strongest fixed-power currency needed in `MC-180`:

\[
X^{1+o(1)}H^{1/2}
\ll
X^{1+o(1)}H.
\tag{5}
\]

The proof is an exponent-preserving pre-sieving transfer from the classical squarefree variance theorem of Gorodetsky--Matomäki--Radziwiłł--Rodgers. It uses only a logarithmically smooth convolution kernel, whose cardinality and relevant Euler norms are `X^{o(1)}` at `y=c log X`.

Consequently, in this range the live frontier of `MC-180`--`MC-183` sharpens again: **ordinary rough eligibility is controlled, and square-free rough support is also controlled at fixed-power variance scale; the unresolved layer is the signed prime-factor-parity orientation itself.** A route that continues to improve only unsigned support estimates cannot prove the required rough Möbius variance without an additional sign-sensitive mechanism.

## 1. Exact pre-sieving convolution

Let

\[
\delta:=\frac1{\zeta(2)}
\]

and define the multiplicative logarithmically smooth kernel

\[
\kappa_y(d)
:=
\lambda(d)\mathbf 1_{P^+(d)\le y},
\tag{6}
\]

where `lambda(d)=(-1)^{Omega(d)}` is the Liouville function. At a prime `p<=y`, the local generating series is

\[
(1+z)(1-z+z^2-z^3+\cdots)=1,
\]

while at `p>y` the kernel has only its constant term and leaves `1+z` unchanged. Hence coefficientwise

\[
\boxed{\beta_y=\mu^2*\kappa_y.}
\tag{7}
\]

This is the unsigned analogue of the logarithmic smooth inverse used in `MC-181`, but with `mu^2` rather than `mu` as the unsifted coefficient.

Because only finitely many primes occur in `kappa_y`, for every fixed `sigma>0`,

\[
\sum_{d\ge1}\frac{|\kappa_y(d)|}{d^\sigma}
=
\prod_{p\le y}(1-p^{-\sigma})^{-1}
<\infty.
\tag{8}
\]

At `sigma=1`,

\[
\delta\sum_{d\ge1}\frac{\kappa_y(d)}d
=
\delta\prod_{p\le y}(1+p^{-1})^{-1}
=
\rho_y.
\tag{9}
\]

Indeed, multiplying the `p<=y` factors of `delta=prod_p(1-p^{-2})` by `(1+p^{-1})^{-1}` changes them exactly to `(1-p^{-1})`, proving `(2)`.

Define the centered squarefree interval error

\[
E(u,L)
:=
\sum_{u<m\le u+L}\mu^2(m)-\delta L.
\tag{10}
\]

Summing `(7)` over `(x,x+H]` and using the absolutely convergent identity `(9)` gives the exact centered representation

\[
\boxed{
B_y(x,H)
=
\sum_{\substack{d\ge1\\P^+(d)\le y}}
\kappa_y(d)
E\!\left(\frac xd,\frac Hd\right).
}
\tag{11}
\]

So imposing the entire initial-prime exclusion `p<=c log X` is an exact linear transform of the ordinary squarefree error. The question is whether the transform costs a fixed power. It does not.

## 2. The logarithmically smooth kernel has only subpower complexity

`MC-181` already proved

\[
\Psi(3X,y)
:=
\#\{d\le3X:P^+(d)\le y\}
=
X^{o(1)}
\tag{12}
\]

when `y=c log X`.

We also need the half-power Euler norm

\[
K_{1/2}(y)
:=
\sum_{P^+(d)\le y}d^{-1/2}
=
\prod_{p\le y}(1-p^{-1/2})^{-1}.
\tag{13}
\]

The prime number theorem (or standard Chebyshev bounds plus partial summation) gives

\[
\log K_{1/2}(y)
=O\!\left(\sum_{p\le y}p^{-1/2}+\sum_{p\le y}p^{-1}\right)
=O\!\left(\frac{\sqrt y}{\log y}+\log\log y\right).
\tag{14}
\]

Since `y=c log X`, the right side is `o(log X)`, and therefore

\[
\boxed{K_{1/2}(y)=X^{o(1)}.}
\tag{15}
\]

The same estimate gives, for any `D>=1`,

\[
\sum_{\substack{d>D\\P^+(d)\le y}}\frac1d
\le
D^{-1/2}K_{1/2}(y)
=
D^{-1/2}X^{o(1)}.
\tag{16}
\]

This elementary tail estimate is what prevents the all-powers inverse kernel from reintroducing a large deterministic centering error.

## 3. Transfer of the classical squarefree variance

For

\[
V_{\mathrm{sf}}(U,L)
:=
\int_U^{2U}|E(u,L)|^2\,du,
\tag{17}
\]

Gorodetsky, Matomäki, Radziwiłł and Rodgers prove that for every fixed `epsilon in (0,1/100)` and

\[
1\le L\le U^{6/11-\varepsilon},
\]

one has the asymptotic

\[
\frac1U V_{\mathrm{sf}}(U,L)
=
C\sqrt L+O_\varepsilon(L^{1/2-\varepsilon/16}),
\tag{18}
\]

with an explicit positive Euler-product constant `C`. In particular,

\[
V_{\mathrm{sf}}(U,L)\ll_\varepsilon U\sqrt L.
\tag{19}
\]

Choose a fixed `epsilon>0` so small that

\[
\theta\le\frac6{11}-\varepsilon.
\tag{20}
\]

Split `(11)` at `d=3X`. For the finite part, Cauchy--Schwarz and `(12)` give

\[
\int_X^{2X}
\left|
\sum_{\substack{d\le3X\\P^+(d)\le y}}
\kappa_y(d)E(x/d,H/d)
\right|^2dx
\le
\Psi(3X,y)
\sum_{\substack{d\le3X\\P^+(d)\le y}}
 d\,V_{\mathrm{sf}}(X/d,H/d).
\tag{21}
\]

For `d<=H`, set `U=X/d` and `L=H/d`. Then `L>=1`, and

\[
L=\frac{X^\theta}{d}
\le
\left(\frac Xd\right)^\theta
=U^\theta
\le U^{6/11-\varepsilon}.
\tag{22}
\]

Therefore `(19)` applies and gives

\[
d\,V_{\mathrm{sf}}(X/d,H/d)
\ll
X\sqrt{H/d}.
\tag{23}
\]

Summing `(23)` over logarithmically smooth `d` and using `(15)`,

\[
\sum_{\substack{d\le H\\P^+(d)\le y}}
 d\,V_{\mathrm{sf}}(X/d,H/d)
\le
XH^{1/2}K_{1/2}(y)
=
X^{1+o(1)}H^{1/2}.
\tag{24}
\]

For `H<d<=3X`, the scaled interval length `L=H/d` is below one. Such an interval contains at most one integer, so from `(10)` one has the elementary bound

\[
V_{\mathrm{sf}}(U,L)
\ll L(U+1),
\qquad 0<L<1.
\tag{25}
\]

Indeed, the set of `u in [U,2U]` for which `(u,u+L]` contains an integer has measure `O(L(U+1))`, and the deterministic centering contribution is smaller at `L<1`.

Thus

\[
d\,V_{\mathrm{sf}}(X/d,H/d)
\ll
H\left(\frac Xd+1\right).
\tag{26}
\]

Using `(12)` and the reciprocal-tail estimate `(16)` with `D=H`,

\[
\sum_{\substack{H<d\le3X\\P^+(d)\le y}}
 d\,V_{\mathrm{sf}}(X/d,H/d)
\ll
XH^{1/2+o(1)}+H X^{o(1)}
=
X^{1+o(1)}H^{1/2}.
\tag{27}
\]

Multiplying `(24)` and `(27)` by the outer `Psi(3X,y)=X^{o(1)}` factor in `(21)` still leaves

\[
\boxed{
I_{\le3X}
\le X^{1+o(1)}H^{1/2}.
}
\tag{28}
\]

## 4. The infinite smooth tail is also below the same scale

For `x in [X,2X]` and `d>3X`, one has `d>x+H`, so the interval `(x/d,(x+H)/d]` contains no positive integer. Hence

\[
E(x/d,H/d)=-\delta H/d,
\]

and the entire tail of `(11)` is independent of `x`:

\[
T_y
=-\delta H
\sum_{\substack{d>3X\\P^+(d)\le y}}
\frac{\kappa_y(d)}d.
\tag{29}
\]

Taking absolute values and applying `(16)` at `D=3X`,

\[
|T_y|
\le
H X^{-1/2+o(1)}.
\tag{30}
\]

Its contribution to the integrated square is therefore

\[
X|T_y|^2
\le
H^2X^{o(1)}.
\tag{31}
\]

Since `theta<6/11<2/3`,

\[
H^2
\le
XH^{1/2}X^{-\delta_\theta}
\]

for some fixed `delta_theta>0`. Thus `(31)` is absorbed by `(28)`. Combining the finite and infinite pieces proves `(4)`.

No cancellation in `kappa_y` was used in the norm estimates; only its restriction to the first `c log X` primes mattered. The transfer is therefore robust against phase choices in the smooth inverse kernel and does not smuggle in zero-free information.

## 5. What is now genuinely missing

`MC-183` showed that ordinary rough-number variance stops before square-free support. Equation `(4)` supplies that missing support control by a different route: start from the established squarefree variance, then pre-sieve the initial logarithmic prime segment through `(7)`.

The three layers now have sharply different status for `theta<6/11`:

\[
\alpha_y
\quad\text{(periodic rough eligibility: controlled)},
\]

\[
\beta_y=\mu^2\alpha_y
\quad\text{(square-free rough support: controlled by `(4)`)},
\]

\[
g_y=\mu\alpha_y=(-1)^{\omega(n)}\beta_y
\quad\text{(signed rough parity: unresolved)}.
\tag{32}
\]

The support theorem is centered because `beta_y` has positive density `rho_y`. The live `MC-180` target is instead the signed second moment

\[
\int_X^{2X}
\left|
\sum_{x<n\le x+H}g_y(n)
\right|^2dx,
\tag{33}
\]

where the sign is the mathematical content. There is no inequality converting `(4)` into a useful bound for `(33)`: replacing `beta_y` by `(-1)^{omega(n)}beta_y` can change coherent interval sums without changing support at all.

This turns the earlier two-step warning into a one-step research target, at least in the unconditional polynomial range `(1)`: **the next useful theorem must price orientation on a support whose centered counting fluctuations are already strongly controlled.** Candidate Type-II, bilinear, harmonic, parity-sensitive sieve, or other signed mechanisms should therefore be tested directly against `(33)`, rather than spending further effort regularizing the unsigned support.

## 6. Prior-art and novelty assessment

The input `(18)` is established prior art: Ofir Gorodetsky, Kaisa Matomäki, Maksym Radziwiłł and Brad Rodgers, *On the variance of squarefree integers in short intervals and arithmetic progressions*, Geometric and Functional Analysis 31 (2021), 111--149, DOI `10.1007/s00039-021-00557-5`, arXiv `2006.04060`. Their Theorem 1 gives exactly the `C sqrt(H)` variance asymptotic used above for `H<=X^(6/11-epsilon)`. They also show that extending the sharp variance bound through the full polynomial range is itself RH-equivalent, so the `6/11` boundary here is deliberately unconditional rather than cosmetic.

General `B`-free variance is also established literature. Gorodetsky, Mangerel and Rodgers, *Squarefrees are Gaussian in short intervals*, Journal für die reine und angewandte Mathematik 2023(795), 1--44, DOI `10.1515/crelle-2022-0066`, treats a fixed pairwise-coprime sieving set `B` and proves general variance/moment results, with squarefrees as the model case. For each fixed `y`, `beta_y` can indeed be viewed as the indicator of the `B_y`-free set

\[
B_y=\{p:p\le y\}\cup\{p^2:p>y\}.
\tag{34}
\]

That framework is important prior art, but it does not by itself supply the moving-family statement `(4)`: here `y=c log X` changes with `X`, and the desired window `H=X^theta` is polynomial rather than the `H=X^{o(1)}` central-limit regime emphasized in the general `B`-free theorem. The proof above instead obtains the required uniform moving pre-sieve directly from the ordinary squarefree variance plus the explicit smooth convolution.

The convolution `(7)`, density identity `(9)`, smooth-number bound `(12)`, and Euler estimates `(13)`--`(16)` are classical mechanisms. No novelty is claimed for them individually, nor for squarefree variance or `B`-free theory. The durable contribution is the **rate-preserving synthesis at the exact live cutoff**: logarithmic pre-sieving costs only subpower factors even at the half-power squarefree variance scale, which removes square-free support as the current fixed-power bottleneck and leaves Möbius parity as the surviving obstruction.

## 7. Boundaries and falsification tests

- The unconditional range proved here is `theta<6/11`. Extending `(4)` by the same input beyond the range of the squarefree variance theorem is not claimed. In particular, no RH-equivalent extension of that theorem is silently assumed.
- The estimate is for the **centered support count** `B_y`. The uncentered second moment of `beta_y` contains the positive-density main term and is of order `X rho_y^2 H^2`; it must not be compared directly with the signed target `(33)`.
- The result does not prove any cancellation for `g_y`, `M(X)`, or `1/zeta(s)`. It only removes the unsigned support layer from the current local-variance bottleneck.
- The moving cutoff is logarithmic. The subpower bounds `(12)` and `(15)` are essential; a substantially larger prime cutoff can make the inverse pre-sieving transform cost a fixed power and is outside this claim.
- The exact density `(2)` and centering identity `(9)` are load-bearing. Using the rough density `prod_{p<=y}(1-1/p)` alone would miscenter the square-free support and invalidate `(4)`.
- The `d>H` range is not discarded. Equation `(25)` prices the sub-unit scaled windows, and `(16)` is required to keep their total contribution at the half-power scale.
- General fixed-`B` results are not treated as uniform theorems for `B=B_y(X)`. The moving-family estimate is derived explicitly instead.
- The claim is falsified if `(7)` fails coefficientwise, if `(9)` gives the wrong density, if the smooth half-norm `(15)` is not subpower at `y=c log X`, or if the scaled windows in `(22)` leave the unconditional range of the cited squarefree variance theorem.

## Consequence for the active frontier

The source-side question left by `MC-183` can now be narrowed. There is no need, in the range `theta<6/11`, to search for a new fixed-power theorem merely to restore the square-free projector `mu^2` after ordinary rough-number counting. That projector already inherits `X^{1+o(1)}H^{1/2}` centered variance from classical squarefree theory through a subpower logarithmic pre-sieve.

The live missing estimate is therefore genuinely signed: establish, refute, or sharply constrain a fixed-power bound for `(33)` while retaining the orientation `(-1)^{omega(n)}` on the already-regular rough square-free support. This is the exact point at which the classical parity phenomenon becomes quantitative rather than terminological.