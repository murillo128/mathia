# FD-033 — critical-line zeros force superlinear physical Schur-tail energy

**Status:** `EXACT-DERIVED + LITERATURE-DERIVED + SCHUR-JORDAN-TAIL + MELLIN-HARDY-SPACE + DECISIVE-NEGATIVE + LINEAR-PRIME-BREADTH`.

`FD-031` reduces every fixed positive linear prime-prefix relaxation to a bounded synthetic head plus a forced physical Mertens tail, and `FD-032` proves that asymptotic GCD-duality saturation would require the Schur-tail energy `E` to satisfy `E/H -> infinity`. That escape condition looked like a possible source of coercivity: an independent bound `E=O(H)` would have produced a uniform angular defect.

The escape is in fact automatic. For every fixed Schur head dimension `D`, the physical tail energy has an exact positive Jordan-mode representation whose quotient-shell coefficient is a summatory arithmetic function with Dirichlet series `zeta(s+1)/zeta(s)`. Hardy's classical theorem that `zeta` has zeros on `Re(s)=1/2` forces the critical weighted square norm of that summatory function to diverge. Consequently

\[
\boxed{
\frac{E_{H,D}}{H}\longrightarrow\infty
\qquad(H\to\infty)
}
\tag{1}
\]

for every fixed `D`. The convergence is uniform over the bounded set of head dimensions arising from any fixed linear ancestry breadth `Y>=lambda H`.

Thus the superlinear-energy alternative in `FD-032` does **not** distinguish a hypothetical saturating physical tail from ordinary unconditional Mertens behavior. In particular, the proposed sufficient route `E=O(H)` is impossible. Any useful linear-prefix gap must control the **normalized/projective** Schur defect, or the independent endpoint-reachability defect from `FD-031`, rather than absolute transverse energy alone.

## 1. The Schur complement is exactly the high-Jordan-mode energy

Retain the notation of `FD-031` and `FD-032`. For integers `1<=D<H`, write

\[
K_H=
\begin{pmatrix}
K_D&P\\
P^T&B
\end{pmatrix},
\qquad
S=B-P^TK_D^{-1}P,
\tag{2}
\]

and let the physical tail be

\[
y_d=\mathbf M\!\left(\left\lfloor\frac Hd\right\rfloor\right),
\qquad D<d\le H,
\tag{3}
\]

where `mathbf M` is the Mertens function. Put

\[
E_{H,D}:=y^TSy.
\tag{4}
\]

The `FD-003` Jordan decomposition says that for every full vector `q=(q_1,...,q_H)`,

\[
q^TK_Hq
=
\sum_{r\le H}J_2(r)
\left(
\sum_{\substack{d\le H\\r\mid d}}
\frac{q_d}{d}
\right)^2.
\tag{5}
\]

For a prescribed tail `y`, the Schur variational identity is

\[
E_{H,D}
=
\min_{x\in\mathbb R^D}
\binom{x}{y}^{\!T}
K_H
\binom{x}{y}.
\tag{6}
\]

If `r>D`, no head index `d<=D` is divisible by `r`; the corresponding Jordan row in (5) is therefore completely fixed by `y`. Conversely, for `1<=r<=D`, the map

\[
(x_1,...,x_D)
\longmapsto
\left(
\sum_{\substack{d\le D\\r\mid d}}
\frac{x_d}{d}
\right)_{1\le r\le D}
\tag{7}
\]

is triangular in decreasing divisor order, with nonzero diagonal entries `1/r`. Hence it is invertible. There is a unique head `x` that cancels all first `D` Jordan rows simultaneously, and changing the head cannot affect any row `r>D`.

Therefore the minimization in (6) is exact row deletion:

\[
\boxed{
E_{H,D}
=
\sum_{r>D}J_2(r)
\left(
\sum_{\substack{d\le H\\r\mid d}}
\frac{\mathbf M(\lfloor H/d\rfloor)}{d}
\right)^2.
}
\tag{8}
\]

This sharpens the interpretation of the `FD-031` Schur complement. It is not an opaque norm of the Mertens tail: it is precisely the portion of the physical `FD-003` Jordan energy lying above the first `D` divisor-incidence modes.

For `r>D`, write `d=rs` and set

\[
X=\left\lfloor\frac Hr\right\rfloor.
\tag{9}
\]

The elementary floor identity

\[
\left\lfloor\frac{H}{rs}\right\rfloor
=
\left\lfloor\frac{\lfloor H/r\rfloor}{s}\right\rfloor
\tag{10}
\]

then gives

\[
\sum_{\substack{d\le H\\r\mid d}}
\frac{\mathbf M(\lfloor H/d\rfloor)}{d}
=
\frac1r
\sum_{s\le X}
\frac{\mathbf M(\lfloor X/s\rfloor)}{s}.
\tag{11}
\]

Define the quotient-shell function

\[
\boxed{
\mathcal H(X)
:=
\sum_{s\le X}
\frac{\mathbf M(\lfloor X/s\rfloor)}{s}.
}
\tag{12}
\]

Then (8) becomes the exact formula

\[
\boxed{
E_{H,D}
=
\sum_{r>D}
\frac{J_2(r)}{r^2}
\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right)^2.
}
\tag{13}
\]

No estimate for `M` or asymptotic approximation enters (13).

## 2. The quotient-shell source has Dirichlet series `zeta(s+1)/zeta(s)`

Expand (12) before estimating it:

\[
\begin{aligned}
\mathcal H(X)
&=\sum_{s\le X}\frac1s
  \sum_{k\le X/s}\mu(k)\\
&=\sum_{sk\le X}\frac{\mu(k)}s\\
&=\sum_{n\le X}c(n),
\end{aligned}
\tag{14}
\]

where

\[
\boxed{
c(n)
:=
\frac1n\sum_{d\mid n}d\mu(d)
=
\frac{\mu(\operatorname{rad}n)\,\varphi(\operatorname{rad}n)}{n}.
}
\tag{15}
\]

The second form follows from

\[
\sum_{d\mid n}d\mu(d)
=
\prod_{p\mid n}(1-p).
\tag{16}
\]

For `Re(s)>1`, absolute convergence permits Dirichlet convolution, and

\[
\begin{aligned}
\sum_{n\ge1}\frac{c(n)}{n^s}
&=\sum_{n\ge1}\frac1{n^{s+1}}
  \sum_{d\mid n}d\mu(d)\\
&=\left(\sum_{m\ge1}\frac1{m^{s+1}}\right)
  \left(\sum_{d\ge1}\frac{\mu(d)}{d^s}\right)\\
&=\boxed{\frac{\zeta(s+1)}{\zeta(s)}}.
\end{aligned}
\tag{17}
\]

Thus the source hidden in the physical Schur tail is an elementary Möbius convolution whose singularities are inherited directly from zeros of `zeta(s)`.

## 3. A critical weighted square norm must diverge

Let

\[
G(x):=\sum_{n\le x}c(n)
=\mathcal H(\lfloor x\rfloor).
\tag{18}
\]

The critical square quantity relevant to (13) is

\[
\mathcal Q
:=
\int_1^\infty\frac{|G(x)|^2}{x^2}\,dx.
\tag{19}
\]

Because `G` is constant on each interval `[n,n+1)`, this is exactly

\[
\boxed{
\mathcal Q
=
\sum_{n\ge1}
\frac{\mathcal H(n)^2}{n(n+1)}.
}
\tag{20}
\]

We now show unconditionally that

\[
\boxed{\mathcal Q=\infty.}
\tag{21}
\]

Suppose instead that `mathcal Q<infinity`. Abel summation applied to (17) gives, initially for `Re(s)>1`,

\[
\frac{\zeta(s+1)}{s\zeta(s)}
=
\int_1^\infty G(x)x^{-s-1}\,dx.
\tag{22}
\]

Put `x=e^u` and

\[
f(u):=e^{-u/2}G(e^u).
\tag{23}
\]

Then (19) is exactly

\[
\|f\|_{L^2(0,\infty)}^2=\mathcal Q<\infty.
\tag{24}
\]

Its Laplace transform

\[
L(z)=\int_0^\infty f(u)e^{-zu}\,du,
\qquad \Re z>0,
\tag{25}
\]

is analytic on the right half-plane. Fourier Plancherel on every vertical line gives, for `delta>0`,

\[
\boxed{
\int_{-\infty}^{\infty}
|L(\delta+it)|^2\,dt
=
2\pi\int_0^\infty
|f(u)|^2e^{-2\delta u}\,du
\le2\pi\mathcal Q.
}
\tag{26}
\]

Equations (22)--(25) identify, for `Re(s)>1`,

\[
L(s-1/2)
=
\frac{\zeta(s+1)}{s\zeta(s)}.
\tag{27}
\]

Hence the assumption `mathcal Q<infinity` supplies an analytic continuation of the right side throughout `Re(s)>1/2` with the uniform Hardy-space bound (26). If `zeta` had a zero `rho` with `Re(rho)>1/2`, this would already be impossible: `zeta(rho+1)` is nonzero because `Re(rho+1)>1`, while the quotient in (27) has a pole at `rho`.

It remains only the possible boundary. Hardy proved in 1914 that `zeta` has infinitely many nontrivial zeros on

\[
\Re(s)=\frac12.
\tag{28}
\]

Choose one, `rho=1/2+i gamma`, of multiplicity `m>=1`. Again `zeta(rho+1) != 0` because `Re(rho+1)=3/2`, and `rho != 0`. Thus the meromorphic quotient in (27) has a pole of order `m` at `rho`. In a sufficiently small right-hand neighborhood of `rho`, its principal Laurent term gives

\[
\left|
\frac{\zeta(s+1)}{s\zeta(s)}
\right|
\gg
|s-\rho|^{-m}.
\tag{29}
\]

Taking `s=1/2+delta+it` and integrating over a fixed small interval about `t=gamma` yields

\[
\int
\left|
L(\delta+it)
\right|^2dt
\gg
\int_{|v|<\eta}
(\delta^2+v^2)^{-m}\,dv
\gg
\delta^{1-2m},
\tag{30}
\]

which diverges as `delta->0+`. This contradicts the uniform bound (26). Therefore (21) holds.

Only the existence of one critical-line zero is needed. No assumption of RH, simplicity, zero density, or quantitative zero spacing enters the argument. If an off-critical zero to the right exists, the contradiction occurs in the open half-plane even earlier.

## 4. Divergence of the critical norm forces `E_{H,D}/H -> infinity`

The elementary Euler-product bound used already in `FD-003` and `FD-032` gives

\[
\frac{J_2(r)}{r^2}
=\prod_{p\mid r}(1-p^{-2})
\ge\frac1{\zeta(2)}.
\tag{31}
\]

Fix `D` and an arbitrary positive integer `K`. For all sufficiently large `H`, every integer `r` satisfying

\[
\left\lfloor\frac Hr\right\rfloor\le K
\tag{32}
\]

also satisfies `r>D`. Grouping the corresponding terms of (13) by the quotient

\[
k=\left\lfloor\frac Hr\right\rfloor
\tag{33}
\]

gives

\[
\frac{E_{H,D}}H
\ge
\frac1{\zeta(2)}
\sum_{k=1}^{K}
\mathcal H(k)^2
\frac{
\lfloor H/k\rfloor-\lfloor H/(k+1)\rfloor
}{H}.
\tag{34}
\]

For each fixed `k`,

\[
\frac{
\lfloor H/k\rfloor-\lfloor H/(k+1)\rfloor
}{H}
\longrightarrow
\frac1{k(k+1)}.
\tag{35}
\]

Therefore

\[
\liminf_{H\to\infty}
\frac{E_{H,D}}H
\ge
\frac1{\zeta(2)}
\sum_{k=1}^{K}
\frac{\mathcal H(k)^2}{k(k+1)}.
\tag{36}
\]

Since `K` is arbitrary and the series on the right diverges by (20)--(21), (1) follows.

The result is uniform in the regime relevant to `FD-031`. Fix `0<lambda<1` and let

\[
Y\ge\lambda H,
\qquad
D(H,Y)=\left\lfloor\frac{H}{Y+1}\right\rfloor.
\tag{37}
\]

As there,

\[
D(H,Y)
\le
D_\lambda
:=\left\lceil\frac1\lambda\right\rceil-1.
\tag{38}
\]

Formula (13) is a sum of nonnegative rows and therefore decreases when `D` increases. Hence

\[
E_{H,D(H,Y)}
\ge E_{H,D_\lambda},
\tag{39}
\]

and the fixed-`D` result yields

\[
\boxed{
\inf_{\lambda H\le Y<H}
\frac{E_{H,D(H,Y)}}H
\longrightarrow\infty.
}
\tag{40}
\]

Thus every fixed positive linear prime-prefix breadth lands in the same unconditional superlinear physical-tail regime.

## 5. Consequence for the linear-prefix program

`FD-032` proves, for fixed positive linear breadth, an exact tradeoff of the form

\[
E_{H,D}\,\mathfrak D_{H,D}
\gg_\lambda H,
\tag{41}
\]

where `mathfrak D` is the GCD-duality loss after the synthetic head is optimized away. It correctly follows that saturation would require `E/H->infinity`. The present result shows that this requirement is **already forced unconditionally**, whether or not saturation occurs.

In particular, the sufficient route suggested there,

\[
E_{H,D}=O_\lambda(H)
\quad\Longrightarrow\quad
\mathfrak D_{H,D}\gg_\lambda1,
\tag{42}
\]

is now ruled out: its premise is false for every fixed `D`, and uniformly for every fixed positive linear breadth. The macroscopic nonsquarefree support mismatch of `FD-032` remains an exact absolute-distance theorem, but the physical Mertens tail has enough growing Schur norm to dilute that compulsory distance.

This does **not** show that the physical tail approaches the equality ray. Equation (1) controls only its absolute norm. The live quantity remains a normalized one, for example

\[
\sin^2\theta_{H,D}
=
\frac{\mathfrak D_{H,D}}{\Delta_{H,D}},
\tag{43}
\]

or equivalently the transverse fraction `rho_(H,D)^2/E_(H,D)`. A lower bound for that normalized fraction can still produce a genuine linear-prefix gap. In the half-linear case, the discrete endpoint-reachability term in the exact `FD-031` two-defect identity remains an independent possible obstruction.

The result therefore narrows, rather than solves, the linear-prefix question: **absolute Schur-tail growth is not the missing Möbius rigidity. Any successful theorem must compare longitudinal and transverse growth inside the same physical tail, or exploit endpoint reachability.**

## 6. Prior-art and falsification boundary

The divisor-incidence/Jordan factorization and Schur-complement identities in Section 1 are already anchored through `FD-003`, `FD-031`, and `FD-032`. Equation (17) is an elementary Dirichlet-convolution identity, and the Mellin/Laplace plus Plancherel step is standard transform theory. The only load-bearing external arithmetic theorem newly required here is G. H. Hardy's 1914 theorem that infinitely many zeros of the Riemann zeta function lie on the critical line. It is added to `SOURCES.md`.

A targeted literature search covered the exact zeta quotient `zeta(s+1)/zeta(s)`, its Dirichlet-series coefficients, Mellin/Hardy-space formulations, and neighboring Hardy-space criteria for zeta. The ingredients are classical and no novelty is claimed for the quotient, boundary-pole argument, or critical-line-zero theorem. The line-specific delta is the exact identification (13) of the `FD-031` physical Schur complement with this quotient-shell square energy, followed by the consequence (40) that the `FD-032` superlinear-energy escape is automatic. No corpus-wide absence claim is made.

Several failure modes are explicitly excluded. `mathcal H` is not the ordinary Mertens function, and no pointwise asymptotic for it is asserted. Divergence of (20) gives no rate for `E/H` beyond divergence, and no monotonicity in `H` is claimed. The proof uses positivity only after the exact Schur/Jordan reduction; replacing `J_2(r)/r^2` by its lower bound cannot create a false divergence. Finally, (1) neither implies small angle defect nor GCD-duality saturation, does not improve the Franel--Landau exponent, and does not prove RH. It removes one proposed coercive escape and leaves the genuinely projective arithmetic problem intact.
