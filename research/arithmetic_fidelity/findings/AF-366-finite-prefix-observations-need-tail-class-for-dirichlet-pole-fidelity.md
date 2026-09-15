# AF-366 — finite-prefix observations need a tail class to preserve Dirichlet poles

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `ARITHMETIC-FIDELITY`, `QUANTITATIVE-FIDELITY`, `SOURCE-TAIL-GATE`, `NO-NOVELTY-CLAIM`

## Claim

AF-365 proves that a **global** fractional Riesz profile observed modulo `O(X^theta)` preserves every Dirichlet principal part strictly to the right of `Re(s)=theta`. That result deliberately does not cover finite observation windows, sparse samples, or local-window data. The finite-horizon boundary is sharp and considerably stronger than mere poor conditioning: without a source-tail restriction, every observation that factors through finitely many Dirichlet coefficients is completely blind to later meromorphic pole data.

Let

\[
\pi_N(c)=(c_1,\ldots,c_N)
\]

and let `T_N` be **any** observation of a coefficient sequence which factors through `pi_N`. Thus `T_N(c)` may be nonlinear and may process the visible prefix arbitrarily, but it has no access to coefficients `c_n` with `n>N`.

Fix a point

\[
\rho=\beta+i\gamma,
\qquad \beta<1,
\]

and a nonzero residue `r`. Define the invisible tail

\[
d_n^{(N)}=
\begin{cases}
0,&n\le N,\\
r n^{\rho-1},&n>N.
\end{cases}
\tag{1}
\]

Then

\[
\boxed{T_N(d^{(N)})=T_N(0),}
\tag{2}
\]

while its Dirichlet transform, initially for `Re(s)>beta`, is

\[
\begin{aligned}
D_N(s)
&:=\sum_{n>N}d_n^{(N)}n^{-s}\\
&=r\left(
\zeta(s-\rho+1)-\sum_{n\le N}n^{\rho-1-s}
\right).
\end{aligned}
\tag{3}
\]

Hence `D_N` has a meromorphic continuation to the plane with a simple pole at `s=rho` of residue `r`. The finite Dirichlet polynomial in `(3)` is entire and cannot alter that principal part.

Moreover,

\[
\boxed{
\sup_{n>N}|d_n^{(N)}|
\le |r|N^{\beta-1}\longrightarrow0
}
\qquad(N\to\infty),
\tag{4}
\]

because `beta<1`. Thus a fixed nonzero pole in the critical-strip range can be hidden beyond longer and longer finite prefixes by coefficient tails whose ordinary `ell^infty` amplitude tends to zero.

For real coefficient sequences, when `gamma\ne0`, use the conjugation-symmetric perturbation

\[
d_n^{(N)}
=2\operatorname{Re}\!\left(rn^{\rho-1}\right)\mathbf 1_{n>N}.
\tag{5}
\]

Its transform has conjugate simple poles at `rho` and `\bar\rho` with residues `r` and `\bar r`. Finite sums of such tails realize any finite conjugation-symmetric set of prescribed simple poles with real coefficients.

The obstruction has an exact complementary recovery gate. Let `a,b` be two coefficient sequences and put `d_n=a_n-b_n`. If for some real `theta` and constants `M,N` one has

\[
|d_n|\le M n^{\theta-1}
\qquad(n>N),
\tag{6}
\]

then the tail Dirichlet series

\[
\sum_{n>N}d_n n^{-s}
\tag{7}
\]

converges absolutely and locally uniformly on `Re(s)>theta`, and therefore defines a holomorphic function there. The finitely many terms with `n\le N` form an entire Dirichlet polynomial. Consequently, whenever the Dirichlet transforms `A,B` admit meromorphic continuations to `Re(s)>theta`, uniqueness of continuation gives

\[
\boxed{A-B\in\operatorname{Hol}(\Re s>\theta).}
\tag{8}
\]

So **all meromorphic principal parts strictly to the right of the tail exponent are identical**. The visible finite prefix is irrelevant to that pole-fidelity conclusion; the decisive information is the admissible tail class.

The gate is quantitative away from its boundary. If `Re(s)>=theta+eta` with `eta>0`, then

\[
\boxed{
\left|
\sum_{n>N}d_n n^{-s}
\right|
\le
M\sum_{n>N}n^{-1-\eta}
\le
\frac{M}{\eta}N^{-\eta}.
}
\tag{9}
\]

And the exponent line is sharp in the elementary sense relevant here: the tail `d_n=n^{\beta-1}\mathbf 1_{n>N}` satisfies `(6)` exactly at `theta=beta` but produces a pole on the boundary `Re(s)=beta`. For every `theta<beta` it violates that stronger tail class. Thus a coefficient envelope `O(n^{\theta-1})` protects principal parts only in the open half-plane `Re(s)>theta`, and no better boundary follows from that envelope alone.

For the Riesz channel of AF-365,

\[
\mathcal R_\delta[c](X)
=\sum_{n\le X}c_n\left(1-\frac nX\right)^\delta,
\qquad \delta\ge0,
\tag{10}
\]

the full continuous observation window `1<=X<=N` factors through `pi_N`. Therefore `(1)`--`(5)` apply for **every** fixed Riesz order, including a fractional order: a finite Riesz horizon can be exactly identical while the unseen tail changes the Dirichlet pole divisor.

This gives the precise destination-interface separation left open by AF-365:

\[
\boxed{
\text{global Riesz error control can preserve poles, but finite Riesz data alone cannot.}
}
\tag{11}
\]

To consume the surviving prime/zero discriminator from finite or growing observations, a downstream argument must import or prove a tail restriction, obtain genuinely global asymptotic control, or retain another nonlocal certificate. Exact finite-horizon data and small unweighted tail coefficients are not enough.

## Derivation

### 1. Every finite-prefix observation has the same invisible tail fiber

By assumption there is a map `\widetilde T_N` with

\[
T_N=\widetilde T_N\circ\pi_N.
\tag{12}
\]

Any perturbation `d` with `d_1=\cdots=d_N=0` therefore satisfies

\[
\pi_N(c+d)=\pi_N(c)
\]

and hence

\[
T_N(c+d)=T_N(c).
\tag{13}
\]

No linearity, continuity, spectral structure, or choice of coordinates for `T_N` is involved. The entire coefficient tail belongs to one observation fiber.

For `(10)`, if `X<=N` then every summand has index `n<=X<=N`; hence the profile `X\mapsto\mathcal R_\delta[c](X)` on that whole interval is a special case of `(12)`. This remains true at every order `delta`: smoothing changes how the visible prefix is combined, not which future coefficients are accessible.

### 2. An invisible power-law tail inserts a prescribed pole

For `d^{(N)}` from `(1)` and `Re(s)>beta`, absolute convergence gives

\[
\begin{aligned}
D_N(s)
&=r\sum_{n>N}n^{-(s-\rho+1)}\\
&=r\zeta(s-\rho+1)
-r\sum_{n\le N}n^{\rho-1-s}.
\end{aligned}
\tag{14}
\]

The Riemann zeta function has a meromorphic continuation with a unique simple pole at `1` of residue `1`. Translation therefore puts a simple pole of residue `r` at `s=rho`. Subtracting the finite Dirichlet polynomial cannot change it.

Equation `(4)` is immediate from `beta-1<0`. It is important not to interpret this as smallness in a norm adapted to analytic continuation. In the weighted norm

\[
\sup_{n>N} n^{1-\beta}|d_n^{(N)}|,
\tag{15}
\]

the same perturbation has size `|r|`, not a vanishing size. The obstruction is precisely that ordinary pointwise or unweighted-tail smallness is too weak to control coherent accumulation across infinitely many coefficients.

The conjugate construction `(5)` follows by adding `(14)` to its complex conjugate coefficient sequence. For distinct nonreal `rho` and `\bar rho`, the two translated zeta factors have distinct poles, so neither can cancel the other locally.

### 3. A polynomial tail exponent protects the corresponding half-plane

Assume `(6)` and let `s=\sigma+it` with `sigma>theta`. Then

\[
|d_n n^{-s}|
\le
M n^{\theta-1-\sigma}
=M n^{-1-(\sigma-\theta)}.
\tag{16}
\]

The majorant is summable. On every compact subset of `Re(s)>theta` the same estimate holds with a fixed positive margin, so the Weierstrass test gives locally uniform convergence and holomorphy of `(7)`.

Adding the finite prefix

\[
P_N(s)=\sum_{n\le N}d_n n^{-s}
\tag{17}
\]

cannot introduce a pole because `P_N` is entire. This proves `(8)` after comparing with the common right half-plane in which the original Dirichlet series for `A` and `B` agree with their meromorphic continuations.

For `sigma>=theta+eta`, `(16)` and the integral comparison for the decreasing function `x^{-1-eta}` give

\[
\sum_{n>N}n^{-1-\eta}
\le
\int_N^\infty x^{-1-\eta}\,dx
=\frac{N^{-\eta}}{\eta},
\tag{18}
\]

which proves `(9)`.

### 4. The exponent boundary is attained by the same counterexample

Set `rho=beta` real and `r=1` in `(1)`. The coefficient tail is exactly `n^{beta-1}` and its transform is

\[
\zeta(s-\beta+1)-\sum_{n\le N}n^{\beta-1-s}.
\tag{19}
\]

It has a simple pole at `s=beta`. Thus the hypothesis `O(n^{theta-1})` with `theta=beta` cannot guarantee holomorphy **on** the line `Re(s)=theta`. Nor can a weaker exponent `theta<beta` admit this tail. The open-half-plane location in `(8)` is therefore the natural sharp boundary for this source class.

## Relation to AF-365 and the current Arithmetic Fidelity frontier

AF-365 separates exact discriminator survival from stable coordinate recovery. Its beta-function Mellin multiplier is zero-free, so a **global eventual** Riesz error `O(X^theta)` forces the Dirichlet difference to be holomorphic in `Re(s)>theta`. The current result identifies what fails when the destination has only a finite horizon: the observation quotient contains the entire coefficient tail, and that tail can carry an arbitrary prescribed critical-strip pole while being pointwise small.

This is not a contradiction. The hypotheses live at different information layers. AF-365 controls the transformed profile for arbitrarily large `X`; AF-366 permits unrestricted completions after one finite horizon. The missing global information is exactly where `(1)` stores its principal part.

The source-tail gate `(6)` is one sufficient way to bridge the layers. For `theta>0`, it also implies the crude global Riesz estimate

\[
|\mathcal R_\delta[d](X)|
\le \sum_{n\le X}|d_n|
=O(X^\theta)
\tag{20}
\]

up to the harmless finite prefix, because the Riesz weights in `(10)` have modulus at most one for real `delta>=0`. Thus a sufficiently strong source-tail theorem can feed AF-365's global principal-part gate directly. But `(6)` is a source-class assumption, not information manufactured by finite Riesz smoothing.

The resulting research distinction is useful:

- **full/global transformed control** can preserve the arithmetic pole discriminator;
- **finite-prefix observation** cannot preserve it over an unrestricted completion class;
- **tail-rate information** can restore exact pole fidelity without reconstructing every coefficient;
- the quantitative cost of *extracting* a pole or another endpoint from noisy finite data remains a separate stability problem.

For an RH-facing application this says exactly what must not be hidden. A finite prime/Riesz certificate can only exclude an off-critical pole at `rho` if its admissible completion class already forbids a tail of the `n^{rho-1}` type, or if another nonlocal argument constrains the continuation. Merely enlarging `N` while measuring tail coefficients in an unweighted sup norm does not solve the problem, since `(4)` gets smaller while the pole residue stays fixed.

## Boundaries and falsification

- The pole-insertion controls are general Dirichlet coefficient sequences. They are not claimed to be rational-prime, Beurling-prime, multiplicative, positive, or Euler-product controls. The theorem therefore establishes insufficiency of the **observation topology**, not a matched-arithmetic counterexample inside every constrained source class.
- The result does not say that every small coefficient tail produces a pole. It says that unweighted pointwise/sup smallness does not rule one out. The coherent power-law phase in `(1)` is essential to the explicit construction.
- The real construction inserts a conjugate pair because real coefficients force the usual conjugation symmetry. It does not manufacture the functional-equation symmetry `rho -> 1-rho`; enforcing a zeta-like divisor class would require additional source structure.
- Equation `(8)` is one-way. A holomorphic difference in `Re(s)>theta` need not satisfy the pointwise coefficient envelope `(6)`; the latter is a transparent sufficient tail class, not a claimed characterization of all pole-faithful completions.
- The bound `(9)` concerns the tail Dirichlet function strictly inside the protected half-plane. It does not give stable analytic continuation from noisy boundary data, nor a stable estimator of pole locations near `Re(s)=theta`.
- At `theta=0`, `(6)` gives an `O(n^{-1})` coefficient tail and still yields absolute convergence for every `Re(s)>0`; the crude Riesz implication `(20)` becomes `O(log X)` rather than `O(1)`. The direct Dirichlet-series pole-fidelity conclusion `(8)` remains valid.
- For variable-order or non-prefix-local observations, `(12)` must be rechecked. The obstruction applies exactly when the declared finite data factor through finitely many source coefficients.

A direct falsification would require either a failure of `(14)`'s shifted-zeta identity or a pole in a half-plane where `(16)` makes the coefficient difference absolutely convergent. Both reduce to standard Dirichlet-series facts.

## Prior art and novelty assessment

No novelty is claimed for Dirichlet-series half-planes, absolute convergence, finite Dirichlet polynomials, shifted zeta functions, or the simple-pole construction `(14)`.

Hardy and Riesz, *The General Theory of Dirichlet's Series* (Cambridge Tracts in Mathematics and Mathematical Physics 18, 1915), is classical background for convergence half-planes and Riesz typical means. A modern account is Andreas Defant, Domingo García, Manuel Maestre, and Pablo Sevilla-Peris, *Dirichlet Series and Holomorphic Functions in High Dimensions* (Cambridge University Press, 2019), Chapter 1, which reviews convergence and absolute-convergence abscissas and the holomorphic half-planes defined by a Dirichlet series. NIST DLMF §25.2 records the specific zeta facts used in `(14)`: `zeta(s)=sum n^{-s}` for `Re(s)>1`, followed by meromorphic continuation with a single simple pole at `s=1` of residue `1`.

The durable Arithmetic Fidelity contribution is the **interface classification relative to AF-365**: exact finite-prefix/Riesz data, even with an unweighted tail tending uniformly to zero as the horizon grows, do not carry the meromorphic principal-part discriminator. A polynomial coefficient-tail exponent is an explicit source-side currency that restores that discriminator in the corresponding open half-plane. This moves the live question from “does the fractional Riesz multiplier erase the prime poles?”—AF-365 says no—to “what independently justified tail/global information lets a finite destination consume those poles without full ill-conditioned reconstruction?”

## Consequences for the line

The finite-horizon escape closes one tempting shortcut: exact or increasingly accurate local Riesz profiles cannot by themselves be promoted to pole-fidelity statements by taking a large but finite cutoff. The tail completion class has to be part of the theorem.

For future destination observables, the audit should therefore separate three ingredients explicitly: the finite data actually retained, the admissible source-tail or continuation class, and the topology in which the final pole-sensitive conclusion is stable. If a proposed endpoint uses only a finite prefix, its prime/zero sensitivity must come from an independently justified tail restriction or another genuinely nonlocal input; otherwise `(1)` supplies an exact same-observation/different-principal-part control.