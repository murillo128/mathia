# WI-245 — Exact Robin spectrum upgrades the finite-radius odd source tariff from exponential to quadratic scale

## Status

- **Evidence:** `EXACT-DERIVED + CLASSICAL-SPECTRAL + LITERATURE-BACKED + STRUCTURAL-RIGIDITY`.
- **Scope:** this sharpens the odd finite-radius necessary condition of `WI-244`. It does **not** prove RH, does not show that Suzuki's first zero crossing lies in the odd sector, and does not supply the missing arithmetic upper bound for the signed von Mangoldt discrepancy.
- **Novelty boundary:** the exponential covariance kernel, its Green-operator interpretation, and the Dirichlet--Robin Sturm--Liouville spectrum are classical. The zeta-specific step is to insert the exact odd-sector spectral gap into the positive digamma-resolvent expansion isolated in `WI-244`. A targeted audit found the classical Ornstein--Uhlenbeck/Karhunen--Loève and Robin-eigenvalue machinery, but did not locate this combined finite-radius Weil/source tariff. No priority claim is made.

## Claim

Retain the normalization of `WI-241` and `WI-244`. For `alpha>0`, define

\[
K_\alpha(x)=\frac\alpha2 e^{-\alpha|x|}
\]

and, on `L^2(0,a)`, its odd-sector compression

\[
(K^-_{\alpha,a}f)(x)
:=\int_0^a \frac\alpha2
\left(e^{-\alpha|x-y|}-e^{-\alpha(x+y)}\right)f(y)\,dy.
\]

Let `kappa_alpha(a)` be the smallest positive solution of

\[
\boxed{
\kappa\cos(\kappa a)+\alpha\sin(\kappa a)=0,
\qquad
\frac{\pi}{2a}<\kappa<\frac\pi a.
}
\]

Equivalently,

\[
\boxed{
\kappa_\alpha(a)a+\arctan\!\frac{\kappa_\alpha(a)}\alpha=\pi.
}
\]

Then the single-resolvent odd support gap is exactly

\[
\boxed{
 d_\alpha(a)
 :=1-\|K^-_{\alpha,a}\|_{2\to2}
 =\frac{\kappa_\alpha(a)^2}{\alpha^2+\kappa_\alpha(a)^2}.
}
\]

Consequently every odd `v in L^2(R)` supported in `[-a,a]` obeys

\[
\boxed{
\frac1{2\pi}\int_{\mathbb R}
\frac{z^2}{z^2+\alpha^2}|\widehat v(z)|^2\,dz
\ge d_\alpha(a)\|v\|_2^2.
}
\]

This replaces the Schur reserve used in `WI-244` by the exact norm loss of each exponential resolvent.

For the positive resolvent expansion

\[
M(z)-M(0)
=\sum_{n=1}^\infty
\frac1{b_n}\frac{z^2}{z^2+\alpha_n^2},
\qquad
b_n=n+\frac14,
\quad
\alpha_n=2b_n,
\]

define

\[
\boxed{
B_{\rm Robin}(a)
:=\sum_{n=1}^\infty \frac{d_{\alpha_n}(a)}{b_n}.
}
\]

Then every normalized odd `v` supported in `[-a,a]` satisfies

\[
\boxed{
Q_{\rm mean}(v)\ge M(0)+B_{\rm Robin}(a)
}
\]

and hence every normalized odd zero witness satisfies

\[
\boxed{
Q_W(v)=0
\quad\Longrightarrow\quad
\Delta(v)\ge\frac{M(0)+B_{\rm Robin}(a)}2.
}
\]

The improvement over `WI-244` is qualitative as well as quantitative. The exact Robin gap has only quadratic large-radius decay. More precisely,

\[
\boxed{
\lim_{a\to\infty}a^2 B_{\rm Robin}(a)
=\frac{\pi^2}{4}\,\zeta\!\left(3,\frac54\right)
=1.6380334913770623\ldots
}
\]

so the extra source tariff above the slow-dilate floor is asymptotically

\[
\boxed{
\frac12B_{\rm Robin}(a)
=\frac{\pi^2}{8}\zeta\!\left(3,\frac54\right)a^{-2}
+o(a^{-2})
=0.8190167456885312\ldots\,a^{-2}+o(a^{-2}).
}
\]

By contrast, the simple reserve retained in `WI-244` decayed exponentially.

A completely explicit nonasymptotic consequence follows from

\[
\kappa_\alpha(a)>\frac{\pi}{a+1/\alpha},
\]

which gives

\[
\boxed{
B_{\rm Robin}(a)
\ge
\pi^2\sum_{n=1}^\infty
\frac{1/b_n}{(2ab_n+1)^2+\pi^2}
\ge
\frac{4\pi^2/5}{(5a/2+1)^2+\pi^2}.
}
\]

Therefore every normalized odd finite-radius zero witness must satisfy the closed-form tariff

\[
\boxed{
\Delta(v)
\ge
\frac{M(0)}2
+
\frac{2\pi^2/5}{(5a/2+1)^2+\pi^2}.
}
\]

## Exact derivation

### 1. The odd exponential kernel is a Dirichlet--Robin Green operator

Let `f in L^2(0,a)` and put

\[
u(x):=(K^-_{\alpha,a}f)(x).
\]

Direct differentiation of the exponential Green kernel, first for smooth `f` and then by density, gives

\[
\boxed{
-u''+\alpha^2u=\alpha^2f
\quad\text{on }(0,a),
}
\]

with boundary conditions

\[
\boxed{
u(0)=0,
\qquad
u'(a)+\alpha u(a)=0.
}
\]

The first condition is the odd reflection at the origin. For the second, when `x=a>y` both exponentials in the kernel acquire the same derivative factor `-alpha`, so `u'(a)=-alpha u(a)`.

Suppose

\[
K^-_{\alpha,a}f=\mu f,
\qquad f\ne0.
\]

The kernel is positive and compact. Moreover its quadratic form is the restriction of the full-line convolution multiplier `alpha^2/(alpha^2+z^2)`, so every nonzero compactly supported vector has Rayleigh quotient strictly between `0` and `1`. Hence `0<mu<1`. Substituting `u=mu f` into the differential equation gives

\[
-f''=\kappa^2 f,
\qquad
\kappa^2=\alpha^2\left(\mu^{-1}-1\right)>0,
\]

with

\[
f(0)=0,
\qquad
f'(a)+\alpha f(a)=0.
\]

Thus `f(x)=A sin(kappa x)` and

\[
\kappa\cos(\kappa a)+\alpha\sin(\kappa a)=0.
\]

The Dirichlet--Robin Sturm--Liouville spectrum is discrete and increasing in `kappa^2`. Its first positive root lies uniquely in `(pi/(2a),pi/a)`, where `tan(kappa a)` runs from `-infinity` to `0`. Therefore the largest eigenvalue of the positive compact operator is

\[
\|K^-_{\alpha,a}\|
=\frac{\alpha^2}{\alpha^2+\kappa_\alpha(a)^2},
\]

which proves the exact formula for `d_alpha(a)`. For the single resolvent this constant is sharp on `L^2(0,a)`, with eigenfunction `sin(kappa_alpha(a)x)`. On `C_c^infty(-a,a)` the same constant is the closure-level infimum; no boundary regularity of that extremizer is being asserted.

### 2. Return to an odd function on the full interval

Let `v` be odd and supported in `[-a,a]`, and write `f=v|_(0,a)`. Reflection gives

\[
\langle v,K_\alpha*v\rangle_{L^2(\mathbb R)}
=2\langle f,K^-_{\alpha,a}f\rangle_{L^2(0,a)},
\qquad
\|v\|_2^2=2\|f\|_2^2.
\]

Since the Fourier multiplier of `K_alpha` is `alpha^2/(alpha^2+z^2)`, Parseval yields

\[
\frac1{2\pi}\int
\frac{z^2}{z^2+\alpha^2}|\widehat v(z)|^2\,dz
=\|v\|_2^2-\langle v,K_\alpha*v\rangle.
\]

Using the exact odd-sector operator norm gives

\[
\frac1{2\pi}\int
\frac{z^2}{z^2+\alpha^2}|\widehat v(z)|^2\,dz
\ge d_\alpha(a)\|v\|_2^2.
\]

The Schur reserve `delta_alpha(a)` from `WI-244` is therefore automatically bounded above by `d_alpha(a)`, because it was a valid lower bound for this same Rayleigh defect. Thus the present result strictly refines, rather than replaces by an unrelated estimate, the earlier finite-radius mechanism.

### 3. Summing the exact single-resolvent gaps

`WI-244` proved the positive expansion

\[
M(z)-M(0)
=\sum_{n=1}^\infty
\frac1{b_n}\frac{z^2}{z^2+\alpha_n^2},
\qquad
b_n=n+\frac14,
\quad
\alpha_n=2b_n.
\]

Every term is a nonnegative quadratic form, so the exact single-resolvent bound may be inserted termwise:

\[
Q_{\rm mean}(v)-M(0)\|v\|_2^2
\ge
\sum_{n=1}^\infty\frac{d_{\alpha_n}(a)}{b_n}\|v\|_2^2.
\]

The series converges for every fixed `a>0`. Indeed the first root satisfies `kappa_alpha(a)<pi/a`, hence

\[
0<d_\alpha(a)
<\frac{\pi^2}{\alpha^2a^2},
\]

and therefore

\[
\frac{d_{\alpha_n}(a)}{b_n}
<\frac{\pi^2}{4a^2b_n^3}.
\]

This proves the `B_Robin(a)` lower bound. It is **not** claimed that one vector simultaneously extremizes all resolvent terms, so `B_Robin(a)` is a rigorous termwise lower bound for the combined multiplier, not a claim that the combined finite-support variational problem has been solved exactly.

### 4. Explicit root bound and quadratic large-radius asymptotic

Because the first root lies in `(pi/(2a),pi/a)`, the boundary equation is equivalently

\[
\kappa a+\arctan(\kappa/\alpha)=\pi.
\]

Using `arctan t<t` for `t>0`,

\[
\pi
<\kappa\left(a+\frac1\alpha\right),
\]

so

\[
\kappa_\alpha(a)>\frac\pi{a+1/\alpha}.
\]

Substitution into `d_alpha` gives

\[
\boxed{
 d_\alpha(a)
>
\frac{\pi^2}{(\alpha a+1)^2+\pi^2}.
}
\]

For `alpha_n=2b_n` this yields the stated explicit series and, by retaining only `n=1`, the one-term rational expression in `a` and `pi`.

For fixed `alpha`, the root equation implies

\[
\kappa_\alpha(a)a\to\pi
\qquad(a\to\infty),
\]

because `kappa_alpha(a)/alpha ->0`. Hence

\[
a^2d_\alpha(a)\to\frac{\pi^2}{\alpha^2}.
\]

The uniform domination

\[
0<\frac{a^2d_{\alpha_n}(a)}{b_n}
<\frac{\pi^2}{4b_n^3}
\]

allows dominated convergence over `n`, giving

\[
\begin{aligned}
\lim_{a\to\infty}a^2B_{\rm Robin}(a)
&=\sum_{n=1}^\infty
\frac1{b_n}\frac{\pi^2}{(2b_n)^2}\\
&=\frac{\pi^2}{4}\sum_{n=1}^\infty\frac1{(n+1/4)^3}\\
&=\frac{\pi^2}{4}\zeta\!\left(3,\frac54\right).
\end{aligned}
\]

The numerical constants quoted above are only orientation; the exact Hurwitz-zeta expression is the claim.

### 5. Convert the spectral reserve into a source tariff

For odd tests the exact source decomposition from `WI-241` is

\[
Q_W(v)=Q_{\rm mean}(v)-2\Delta(v).
\]

Thus a normalized odd zero witness obeys

\[
\Delta(v)=\frac12Q_{\rm mean}(v)
\ge\frac{M(0)+B_{\rm Robin}(a)}2.
\]

Using only the first resolvent and the explicit root bound gives

\[
\Delta(v)
\ge
\frac{M(0)}2
+
\frac{2\pi^2/5}{(5a/2+1)^2+\pi^2}.
\]

This is the same one-way logical direction as `WI-244`: to exclude an odd first-crossing candidate at radius `a`, one would need a zeta-specific directional **upper** bound for `Delta(v)` that lies strictly below this tariff on the candidate class.

## Structural consequence for the finite-radius route

`WI-244` established that compact odd support prevents exact saturation of the spectral floor `M(0)`, but its Schur estimate made the reserve look exponentially fragile as the support radius grows. The exact Green/Robin calculation shows that this was proof slack: for each resolvent the true boundary leakage is of order `a^{-2}`, and after summing the digamma resolvents the retained reserve is

\[
B_{\rm Robin}(a)
\sim
\frac{\pi^2}{4}\zeta\!\left(3,\frac54\right)a^{-2}.
\]

So the surviving non-circular source-side target is quantitatively stronger than previously recorded. A hypothetical odd finite-radius zero mode cannot merely reproduce the slow-dilate discrepancy floor up to exponentially small error; it must clear a polynomial `a^{-2}` archimedean surcharge.

This does **not** make the missing arithmetic estimate automatic. `WI-243` still blocks any attempt to replace the required directional finite-radius source estimate by a global subexponential discrepancy theorem, because that global statement already contains RH-level information. The useful next question is narrower: whether first-crossing structure, orthogonality, or the finite prime support `n<=e^{2a}` forces an upper bound on `Delta(v)` that misses the explicit Robin tariff.

## Prior-art audit

The following surfaces were checked in addition to the line-local findings and sources.

1. Classical finite-interval Dirichlet--Robin Sturm--Liouville theory gives `tan(ka)=-k/alpha` for `f(0)=0`, `f'(a)+alpha f(a)=0`. This is exactly the boundary problem obtained above.
2. The kernel `e^{-alpha|x-y|}-e^{-alpha(x+y)}` is, up to normalization, the covariance kernel of a centered Ornstein--Uhlenbeck process started from a deterministic zero state. The Karhunen--Loève literature treats the same conversion from exponential covariance operators to second-order boundary-value problems; Corlay--Pagès, *Functional quantization-based stratified sampling methods* (arXiv:1008.4441; later *Monte Carlo Methods and Applications* 21 (2015), 1--32, DOI `10.1515/mcma-2014-0010`) explicitly derives the Ornstein--Uhlenbeck case, and Corlay, *Properties of the Ornstein--Uhlenbeck bridge* (arXiv:1310.5617), Proposition 2.1, records the same covariance-operator-to-boundary-value mechanism for bridges.
3. Suzuki's localized Weil/screw-function papers, and the nearby public RH experiments located in the audit, do not appear to state the present termwise Robin sharpening of the digamma-resolvent source tariff.

Accordingly, the **spectral calculation is classical**. The durable content here is the exact splice with `WI-244` and the resulting polynomial finite-radius tariff. Absence from the targeted search is recorded only as an audit result, not as a priority assertion.

## Falsification and boundaries

1. **Parity is essential here.** The reflected positive kernel and the source decomposition used above are the odd-sector objects of `WI-241`/`WI-244`. Nothing here proves that a Suzuki first crossing must be odd. An even-sector crossing would require a separate analysis.
2. **The combined reserve is not claimed optimal.** Each `d_alpha(a)` is the exact single-resolvent gap, but the resolvents have different Robin parameters and generally different extremizers. Summing their separate minima is rigorous and may still leave positive slack.
3. **No arithmetic upper bound is proved.** The finding strengthens the amount of signed von Mangoldt discrepancy required by an odd zero witness; it does not show that the actual source fails to provide it.
4. **No global discrepancy estimate is being smuggled in.** The result is purely archimedean/spectral at fixed radius. The RH-equivalent global-growth barrier of `WI-243` remains intact.
5. **No percentage claim follows.** This is a finite-radius structural result aimed at individual off-line defects, consistent with the canonical mandate's requirement that density-level gains are secondary to an RH-closing mechanism.

## Sources

- `WI-241`, `WI-243`, and `WI-244` for the exact source decomposition, global discrepancy barrier, and positive digamma-resolvent expansion.
- Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096 (2026), for the localized Weil operator and finite-radius first-crossing framework.
- Sylvain Corlay and Gilles Pagès, **Functional quantization-based stratified sampling methods**, arXiv:1008.4441; *Monte Carlo Methods and Applications* 21 (2015), 1--32, DOI `10.1515/mcma-2014-0010`, for established finite-interval Ornstein--Uhlenbeck Karhunen--Loève/spectral prior art.
- Sylvain Corlay, **Properties of the Ornstein--Uhlenbeck bridge**, arXiv:1310.5617, especially Proposition 2.1, for the classical exponential-covariance-operator to Sturm--Liouville boundary-value reduction in a closely related finite-interval setting.
