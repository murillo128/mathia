# MC-093 — Fixed-gap Hamming deformation cannot hide endpoint power

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `BOUNDARY/CONDITIONAL-GAIN`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

The prime-symmetric-difference deformation of `MC-091`,

\[
\mathcal Q_N(t)
=
\sum_{m,n\le N}
\mu(m)^2\mu(n)^2
(-t)^{d_\triangle(m,n)}
 z\!\left(\frac{N^2}{mn}\right),
\qquad 0\le t\le1,
\tag{1}
\]

cannot concentrate a different **polynomial power scale** only at the Möbius endpoint `t=1` while remaining uniformly smaller on any fixed-gap interior interval. The reason is exact and independent of zeta zeros: `mathcal Q_N(t)` has degree only

\[
D_N:=\deg_t\mathcal Q_N
=O\!\left(\frac{\log N}{\log\log N}\right).
\tag{2}
\]

Fix `0<eta<1` and define

\[
B_N(\eta)
:=
\sup_{0\le t\le1-\eta}|\mathcal Q_N(t)|.
\tag{3}
\]

Classical Chebyshev/Remez extremality on one interval gives

\[
\boxed{
|\mathcal Q_N(1)|
\le
B_N(\eta)
T_{D_N}\!\left(\frac{1+\eta}{1-\eta}\right)
\le
B_N(\eta)
\left(\frac{1+\sqrt\eta}{1-\sqrt\eta}\right)^{D_N}.
}
\tag{4}
\]

Because `eta` is fixed and `(2)` is sublogarithmic,

\[
\left(\frac{1+\sqrt\eta}{1-\sqrt\eta}\right)^{D_N}
=
\exp\!\left(O_\eta\!\left(\frac{\log N}{\log\log N}\right)\right)
=N^{o_\eta(1)}.
\tag{5}
\]

Hence

\[
\boxed{
|\mathcal Q_N(1)|
\le B_N(\eta)N^{o_\eta(1)},
\qquad
B_N(\eta)
\ge |\mathcal Q_N(1)|N^{-o_\eta(1)}.
}
\tag{6}
\]

At the level of fixed powers of `N`, the hard endpoint and the supremum on every fixed interior interval therefore have the same possible scale. In particular, a theorem

\[
\sup_{0\le t\le1-\eta}|\mathcal Q_N(t)|
=O(N^\gamma)
\tag{7}
\]

implies

\[
\mathcal Q_N(1)=O(N^{\gamma+o(1)}).
\tag{8}
\]

So **uniform fixed-gap regularization is not a cheaper power-level carrier**. If one hopes that damping parity by taking `t<1` makes the entire deformed family uniformly easier, any strict power gain obtained uniformly on a fixed interval already transfers to the Möbius endpoint with only subpolynomial loss.

This also removes one ambiguity in the continuation of `MC-091`--`MC-092`. An estimate of the endpoint derivative alone still does not reconstruct `mathcal Q_N(1)`, exactly as those findings warn. But if a source-natural argument controls the whole deformation on any fixed interval separated from `1`, interpolation itself costs no fixed power. The real burden is obtaining that uniform interior estimate, together with the separate coarse/source residual and scale-iteration obligations; the polynomial extrapolation step is not an additional exponent barrier.

No bound of the form `(7)` is proved here, and no improved Mertens estimate is claimed.

## 1. The product-fiber quotient forces sublogarithmic degree

`MC-092` gives the exact product-fiber form

\[
\mathcal Q_N(t)
=
\sum_{\substack{a,b\ \mathrm{squarefree}\\(a,b)=1\\ab^2\le N^2}}
R_N(a,b)(-t)^{\omega(a)}
 z\!\left(\frac{N^2}{ab^2}\right).
\tag{9}
\]

Every power of `t` that occurs is therefore `omega(a)` for some square-free `a<=N^2`. Let

\[
K(X):=\max_{\substack{a\le X\\a\ \mathrm{squarefree}}}\omega(a).
\]

Then

\[
D_N\le K(N^2).
\tag{10}
\]

If `omega(a)=k`, the smallest possible square-free positive integer with `k` prime factors is the product of the first `k` primes. Since the `j`-th prime is at least `j+1`, in particular

\[
a\ge \prod_{j=1}^k p_j\ge k!.
\tag{11}
\]

Thus `k!<=X`. The elementary Stirling lower bound

\[
\log(k!)=k\log k-k+O(\log k)
\]

implies

\[
K(X)=O\!\left(\frac{\log X}{\log\log X}\right).
\tag{12}
\]

Taking `X=N^2` proves `(2)`. Cancellation between the top polynomial coefficients may reduce the actual degree, but can only strengthen the endpoint estimate below.

The small degree is not an externally imposed approximation. It is forced by the arithmetic source: the deformation parameter counts distinct exclusive prime coordinates, and an integer of size at most `N^2` can carry only `O(log N/log log N)` such coordinates.

## 2. Exact Chebyshev extrapolation from a fixed interior interval

Assume first that `B_N(eta)>0` and put

\[
P_N(x)
:=
\frac{1}{B_N(\eta)}
\mathcal Q_N\!\left(\frac{1-\eta}{2}(x+1)\right).
\tag{13}
\]

Then `P_N` is a real polynomial of degree at most `D_N` and

\[
|P_N(x)|\le1
\qquad(-1\le x\le1).
\tag{14}
\]

The point `t=1` maps to

\[
x_\eta
=
\frac{1+\eta}{1-\eta}>1.
\tag{15}
\]

The classical one-interval Chebyshev extremal theorem gives, for every real polynomial of degree at most `D_N` satisfying `(14)`,

\[
|P_N(x_\eta)|\le T_{D_N}(x_\eta).
\tag{16}
\]

For `x>1`,

\[
T_D(x)=\cosh(D\,\operatorname{arcosh}x)
\le
\left(x+\sqrt{x^2-1}\right)^D.
\tag{17}
\]

A direct calculation at `(15)` gives

\[
x_\eta+\sqrt{x_\eta^2-1}
=
\frac{1+\sqrt\eta}{1-\sqrt\eta}.
\tag{18}
\]

Equations `(13)`--`(18)` prove `(4)`. If `B_N(eta)=0`, the polynomial vanishes on an interval and hence identically, so the same conclusion is trivial.

For fixed `eta`, the logarithm of the factor in `(4)` is a constant times `D_N`. Combining with `(2)` proves `(5)` and `(6)`.

A useful power-ledger form is the following. If for some fixed `alpha` and `eta`

\[
B_N(\eta)\le N^{2\alpha+o(1)},
\tag{19}
\]

then

\[
|\mathcal Q_N(1)|\le N^{2\alpha+o(1)}.
\tag{20}
\]

Therefore a strict exponent margin below an old square-scale exponent survives fixed-gap extrapolation. Conversely, if the endpoint has size at least `N^{2\beta-o(1)}` along a subsequence, then the interior supremum has at least the same power `N^{2\beta-o(1)}` there.

## 3. The deformation is exactly a biased random-multiplicative expectation

There is an exact probabilistic interpretation that clarifies what an interior estimate would mean without turning randomness into arithmetic evidence. For fixed `0<=t<=1`, choose independent prime signs `xi_p in {+1,-1}` with

\[
\mathbb E\xi_p=-t,
\qquad
\mathbb P(\xi_p=1)=\frac{1-t}{2},
\qquad
\mathbb P(\xi_p=-1)=\frac{1+t}{2}.
\tag{21}
\]

On square-free support define

\[
f_\xi(n):=\mu(n)^2\prod_{p\mid n}\xi_p.
\tag{22}
\]

For square-free `m,n`, common prime factors occur twice and cancel from the product, while each prime in the symmetric difference occurs once. Independence therefore gives

\[
\mathbb E[f_\xi(m)f_\xi(n)]
=
\mu(m)^2\mu(n)^2(-t)^{d_\triangle(m,n)}.
\tag{23}
\]

Consequently

\[
\boxed{
\mathcal Q_N(t)
=
\mathbb E\!\left[
\sum_{m,n\le N}
f_\xi(m)f_\xi(n)
 z\!\left(\frac{N^2}{mn}\right)
\right].
}
\tag{24}
\]

At `t=0` this is the unbiased prime-sign ensemble and only equal support survives in expectation, reproducing the diagonal endpoint. At `t=1` every `xi_p=-1` deterministically and `f_xi=mu`, reproducing the Möbius endpoint.

Equation `(24)` does **not** transfer random RMS estimates to Möbius. It says instead that the Hamming deformation is precisely a bias path through multiplicative prime-sign ensembles. Combining `(24)` with `(6)` shows that a uniform expected power gain throughout any fixed bias interval bounded away from the all-minus point cannot remain isolated from the deterministic endpoint at polynomial scale. The low polynomial degree forces leakage.

The local matrices `[[1,-t],[-t,1]]` are positive semidefinite for `0<=t<=1`, but the sawtooth-weighted bilinear form in `(24)` is not thereby positive or contractive. No operator-positivity conclusion is being inserted.

## 4. Prior art and novelty boundary

The one-interval extremal principle used in `(16)` is classical Chebyshev/Remez theory. A modern pointwise reference is B. Eichinger and P. Yuditskii, *Pointwise Remez inequality*, Constructive Approximation 54 (2021), 529--554, DOI `10.1007/s00365-021-09562-1`, arXiv `2007.01607`. Their formulation explicitly records that for a single interval the Remez extremal solution is a rescaled Chebyshev polynomial.

The Hamming/noise-kernel interpretation of the local matrices is standard Boolean-product harmonic analysis and was already treated as classical in `MC-091` and `MC-092`. The factorial bound on the support degree is elementary.

A targeted literature check around Möbius/Huxley--Watt deformations, Hamming kernels, Remez inequalities, and Chebyshev interpolation supplied no basis for claiming a new external theorem specialized to `(1)`. **No novelty claim is made.** The durable line-specific result is the exact combination of the source-forced degree bound `(2)` with the classical endpoint extremal inequality `(4)`, which closes a power-ledger question left open by `MC-091`--`MC-092`.

## 5. Boundaries and decisive continuation

The conclusion is **uniform-in-parameter**. A bound at one fixed `t<1`, or even a bound for `mathcal Q_N'(1)`, does not control `mathcal Q_N(1)`. Equation `(4)` uses a bound over an interval of fixed positive length. Discrete interpolation data may also suffice with a separately audited stability constant, but no such discrete theorem is asserted here.

The fixed-gap hypothesis matters to the displayed constant. This finding does not claim a uniform formula when the controlled interval degenerates with `N`; any `eta=eta_N` regime must retain the explicit Chebyshev factor in `(4)` and audit it quantitatively rather than replacing it by `N^{o(1)}` automatically.

The result also controls only the Huxley--Watt deformation endpoint `mathcal Q_N(1)=Q_1(N)`. Turning a bound for that block into an improved global Mertens exponent still requires the exact source identity and all coarse/residual terms to be subordinate, and any recursive gain must satisfy the small-state, signed-residual, and all-scale conditions isolated in `MC-027`. No part of `(4)` supplies those estimates.

Finally, `(24)` is an expectation identity, not an independence model for actual Möbius. A theorem about typical random multiplicative realizations, variance, or high-probability behavior does not imply a bound for the expectation uniformly in `t`, still less for the all-minus endpoint, without an exact bridge.

The decisive continuation is therefore sharper than “interpolate from an easier `t`.” One must identify source-natural arithmetic information that controls `mathcal Q_N(t)` uniformly on a sufficiently large parameter set at a strictly improved power scale, or another coupled statistic from which such control follows. If such a theorem is obtained on a fixed interior interval, the endpoint interpolation cost is already known to be subpolynomial; if only isolated parameter values or endpoint derivatives are controlled, the reconstruction gap remains.

## Consequence for the research line

`MC-091` left two logically separate uncertainties after exposing the prime-coordinate deformation: whether the new signed arithmetic input exists, and whether interpolation back to the hard endpoint would spend a power gain. `MC-092` then showed that prime labels themselves do not provide the needed orthogonality.

`MC-093` removes the second uncertainty for uniform fixed-gap control. **The deformation has too few arithmetic degrees to hide a different polynomial scale only at `t=1`.** Uniform interior power control and endpoint power control differ by at most `N^{o(1)}`. This is simultaneously a negative result and a useful conditional bridge: fixed-gap regularization is not a free escape from the Möbius endpoint, but once genuinely stronger uniform interior arithmetic information is available, polynomial extrapolation will not destroy its exponent margin.
