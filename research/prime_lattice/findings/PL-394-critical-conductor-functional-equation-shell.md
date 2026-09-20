# PL-394 — Critical-conductor one-sided Bohr geometry remains Haar; continuation enters through functional-equation mode coupling

**Evidence/status:** `CLASSICAL-MEAN-VALUE+CLASSICAL-APPROXIMATE-FE+EXACT-DERIVED + ROUTE-RESTRICTION/PRIOR-ART-REDIRECT`.

**Parent findings:** `PL-072`, `PL-392`, `PL-393`.

## Claim

`PL-393` leaves coupled limits `N=N(T)` as one possible escape from the fact that a fixed-cutoff infinite-height Jessen mean forgets the Euler--Maclaurin continuation tail. The most canonical zeta scale is the square-root analytic-conductor scale appearing in the approximate functional equation,

\[
N\asymp \sqrt{T/(2\pi)}.
\]

At that scale, however, the **one-sided positive-cone quadratic geometry still becomes Haar**. This is already an exact consequence of the Montgomery--Vaughan estimate stored in `PL-072`: if

\[
G_{T,N}(m,n)=\frac1T\int_T^{2T}e^{-it(\log n-\log m)}\,dt,
\qquad 1\le m,n\le N,
\]

then

\[
\|G_{T,N}-I\|=O(N/T).
\]

Hence for `N asymp sqrt(T)`,

\[
\boxed{\|G_{T,N}-I\|=O(T^{-1/2}).}
\]

In exponent coordinates this is the Gram matrix of the characters

\[
e^{-it\langle v(n),(\log p)_p\rangle},
\]

restricted to the energy ball `log n <= log N`. Thus merely coupling the cutoff to height at the Riemann--Siegel length does **not** make the positive-cone `L^2` geometry retain analytic continuation: its full quadratic form converges in operator norm to Haar orthogonality.

The continuation-faithful high-height representation of zeta instead introduces a qualitatively different structure. On the critical line the classical approximate functional equation gives

\[
\zeta\!\left(\frac12+it\right)
=
\sum_{n\le m(t)}n^{-1/2-it}
+
\chi\!\left(\frac12+it\right)
\sum_{n\le m(t)}n^{-1/2+it}
+O(t^{-1/4}),
\]

with

\[
m(t)=\left\lfloor\sqrt{t/(2\pi)}\right\rfloor,
\qquad
|\chi(1/2+it)|=1.
\]

The second main term is not another positive-cone Kronecker packet. It uses the reflected modes `-v(n)` in the group completion and multiplies them by the nonlinear archimedean phase

\[
\chi(1/2+it)=e^{-2i\theta(t)}.
\]

For a quadratic observable, the interaction between the two halves has termwise phase

\[
2\theta(t)-t\log(nm).
\]

Stirling's expansion gives

\[
2\theta'(t)=\log\frac{t}{2\pi}+O(t^{-1}),
\]

so stationary interaction occurs only near

\[
\boxed{nm\asymp \frac{t}{2\pi}},
\]

or, in prime-exponent coordinates,

\[
\boxed{
\left\langle v(n)+v(m),(\log p)_p\right\rangle
\asymp \log\frac{t}{2\pi}.
}
\]

Thus the first canonical coupled-height escape from `PL-393` is already classical and is more specific than `N=N(T)`: **same-sign positive-cone geometry is asymptotically Haar at the critical conductor, while the functional equation introduces an opposite-mode, archimedean-chirped coupling whose stationary set is a sum-energy shell**. This is a representation-level redirect, not an RH mechanism. The critical line is singled out here because it is the self-dual line of the functional equation, where the two Dirichlet packets have equal weight and `|chi|=1`; nothing in this argument forces all nontrivial zeros to lie there.

## 1. `PL-072` already controls the growing one-sided Gram operator

For coefficients `a=(a_n)_(n<=N)`, let

\[
D_a(t)=\sum_{n\le N}a_n n^{-it}.
\]

The Montgomery--Vaughan mean-value theorem gives uniformly in the coefficient vector

\[
\int_T^{2T}|D_a(t)|^2\,dt
=
T\sum_{n\le N}|a_n|^2
+O\!\left(N\sum_{n\le N}|a_n|^2\right).
\]

Equivalently,

\[
\left|\langle(G_{T,N}-I)a,a\rangle\right|
\le C\frac NT\|a\|_2^2,
\]

and self-adjointness gives

\[
\|G_{T,N}-I\|\le C N/T.
\]

This was the main finite-time classification in `PL-072`; no novelty is claimed for the estimate. Its consequence for the present frontier is immediate but load-bearing. The approximate-functional-equation cutoff satisfies `N asymp T^(1/2)`, far below the `N asymp T` resolution transition of `PL-072`. Therefore the entire one-sided character family is not merely coefficientwise decorrelated but uniformly asymptotically orthogonal in quadratic form at the critical conductor.

For the zeta coefficient vector `a_n=n^{-1/2}` this says

\[
\frac1T\int_T^{2T}
\left|\sum_{n\le N}n^{-1/2-it}\right|^2dt
=
\sum_{n\le N}\frac1n
+O\!\left(\frac NT\sum_{n\le N}\frac1n\right).
\]

The right-hand main term is exactly the Haar `L^2` norm of the Bohr polynomial

\[
F_N(z)=\sum_{n\le N}n^{-1/2}z^{v(n)}
\]

on the infinite torus. With `N asymp sqrt(T)`, the relative quadratic defect is `O(T^(-1/2))`.

This closes a tempting but insufficient reading of the live `N=N(T)` escape in `RESEARCH_LINES.md`: **growth of the cutoff at the natural zeta conductor does not by itself prevent one-sided Haar washout.** Any continuation-sensitive coupled limit must use an observable or coupling not contained in this same-sign Gram geometry.

## 2. The approximate functional equation changes the representation, not just the cutoff

The DLMF/Titchmarsh approximate functional equation states that for `s=sigma+it`, `0<=sigma<=1`, and `2 pi x y=t`,

\[
\zeta(s)
=
\sum_{n\le x}n^{-s}
+
\chi(s)\sum_{n\le y}n^{-(1-s)}
+O(x^{-\sigma})
+O(y^{\sigma-1}t^{1/2-\sigma}),
\]

where

\[
\chi(s)=\pi^{s-1/2}
\frac{\Gamma((1-s)/2)}{\Gamma(s/2)}.
\]

At `sigma=1/2`, choosing `x=y=sqrt(t/(2 pi))` gives

\[
\zeta(1/2+it)
=A(t)+\chi(1/2+it)\overline{A(t)}+O(t^{-1/4}),
\]

with the common moving cutoff `m(t)=floor sqrt(t/(2 pi))`.

This formula is a genuine analytic-continuation statement; it is not obtained by formally evaluating the Euler product in the critical strip. It also shows why the continuation information cannot be represented by simply taking a longer positive-cone Bohr polynomial. The reflected packet has frequencies

\[
+\log n=-\langle -v(n),(\log p)_p\rangle,
\]

so it lives on the negative cone of the group completion `Z^(P)`. More importantly, it is multiplied by `chi(1/2+it)`, whose phase is nonlinear in `t`. The full leading approximation is therefore not the restriction of one fixed trigonometric polynomial along the original linear Kronecker flow.

On the critical line define the Riemann--Siegel phase by

\[
\theta(t)=\operatorname{Im}\log\Gamma\!\left(\frac14+\frac{it}{2}\right)
-\frac t2\log\pi.
\]

Then

\[
\chi(1/2+it)=e^{-2i\theta(t)}.
\]

This is the standard self-dual rewriting behind the Riemann--Siegel formula. The lattice contribution supplies the linear phases `t log n`; the archimedean Gamma factor supplies the chirp `theta(t)`.

## 3. The functional-equation cross channel sees a sum-energy shell

To isolate what the second packet adds, temporarily suppress the moving-cutoff bookkeeping and inspect a term that is present over a height interval. Write

\[
A(t)=\sum_n a_n e^{-it\log n},
\qquad
B(t)=e^{-2i\theta(t)}\sum_m a_m e^{+it\log m}.
\]

The same-half products `A overline{A}` have phases

\[
t(\log m-\log n)
=
t\left\langle v(m)-v(n),(\log p)_p\right\rangle,
\]

which are exactly the difference-frequency Gram phases controlled by `PL-072`.

By contrast, the cross term `A overline{B}` contains

\[
e^{2i\theta(t)}e^{-it(\log n+\log m)}.
\]

Its phase derivative is

\[
2\theta'(t)-\log(nm).
\]

The standard Stirling expansion of the Gamma factor yields

\[
\theta'(t)=\frac12\log\frac{t}{2\pi}+O(t^{-1}),
\]

so stationary phase can occur only when

\[
\log(nm)=\log\frac{t}{2\pi}+O(t^{-1}),
\]

i.e. near `nm=t/(2 pi)`. Because `log(nm)=<v(n)+v(m),log p>`, the reflected interaction replaces the Haar difference geometry by a moving **sum-energy shell**.

This shell is not evidence for RH. It is a classical consequence of the functional equation and the Riemann--Siegel phase. Its value for this research line is diagnostic: it identifies exactly which structure survives after `PL-072` has erased the one-sided critical-conductor Gram defect.

## 4. Prior-art and novelty audit

No theorem-level novelty is claimed.

The one-sided operator-norm estimate is already stored in `PL-072` and comes from Montgomery--Vaughan's 1974 strengthened Hilbert inequality/Dirichlet-polynomial mean-value theorem. A targeted repository check before this finding found no later `prime_lattice` result superseding `PL-393` and no existing local finding combining the `PL-072` finite-time threshold with the post-`PL-393` continuation-tail problem.

The two-piece representation, the square-root cutoff, the unit-modulus critical-line factor and the Riemann--Siegel phase are classical. DLMF Section 25.9 records the Titchmarsh approximate functional equation with `2 pi x y=t` and its balanced critical-line specialization; DLMF Section 5.11 supplies the Gamma/digamma asymptotics used for the phase derivative. Classical Riemann--Siegel analysis and modern zeta moment calculations routinely exploit the same dual packet and stationary-phase structure.

A targeted literature search for combinations of the Bohr lift/infinite torus with the approximate functional equation and Riemann--Siegel formula did not uncover a basis for claiming that the prime-exponent wording or the sum-energy-shell dictionary is a new theorem. The durable delta is instead the **line-specific route restriction**: after `PL-393`, the most natural coupled cutoff lies safely inside the already-classified Haar regime of `PL-072`, so continuation sensitivity has to come from the functional-equation coupling (or another representative-sensitive mechanism), not from the growing positive-cone Gram geometry itself.

### Sources

1. H. L. Montgomery, R. C. Vaughan, “Hilbert's Inequality,” *Journal of the London Mathematical Society* (2) **8**(1) (1974), 73--82. DOI: https://doi.org/10.1112/jlms/s2-8.1.73. Primary source behind the Dirichlet-polynomial mean-value estimate already anchored in `SOURCES.md` for `PL-072`.
2. NIST Digital Library of Mathematical Functions, §25.9, “Asymptotic Approximations” for the Riemann zeta function, especially equations 25.9.1--25.9.3: https://dlmf.nist.gov/25.9. These formulas cite E. C. Titchmarsh, *The Theory of the Riemann Zeta-function*, 2nd ed., revised by D. R. Heath-Brown, Oxford University Press, 1986, §§4.11--4.18.
3. NIST Digital Library of Mathematical Functions, §5.11, “Asymptotic Expansions” for `Gamma` and the digamma function, especially 5.11.1--5.11.2: https://dlmf.nist.gov/5.11.

## 5. Adversarial boundaries

1. **This does not rule out all coupled limits `N=N(T)`.** It rules out obtaining new continuation information from the one-sided quadratic Gram geometry at the canonical square-root conductor. Nonlinear, local, determinant, target-relative or individual-zero-sensitive observables remain outside the claim.

2. **The Montgomery--Vaughan statement uses a frozen cutoff on a fixed height window.** The balanced approximate functional equation uses the moving cutoff `m(t)=floor sqrt(t/(2 pi))`. The operator-norm estimate is therefore a route restriction on the frozen one-sided packet at the same scale, not a proof that every moving-cutoff statistic is Haar.

3. **The sum-energy shell is not a new zero-localization principle.** It is the stationary-phase geometry of the classical functional-equation cross channel. It remains compatible with the existence of off-critical zeros and supplies no positivity theorem equivalent to RH.

4. **The critical line is selected by self-duality, not by the bare lattice.** At `sigma=1/2`, the reflected exponents have the same coefficient magnitude and `|chi|=1`. Off the line, the two packets carry different weights. This is the familiar functional-equation symmetry and must not be advertised as an intrinsic geometric proof of `Re(s)=1/2`.

5. **The archimedean phase is load-bearing.** Replacing `chi(1/2+it)` by a fixed character `e^{-ict}` destroys the moving stationary condition and returns to ordinary fixed-frequency torus geometry. The continuation-faithful leading representation is therefore not contained in the bare prime Kronecker flow.

6. **No formal Euler-product continuation is used.** The critical-strip formula is imported from the proven approximate functional equation. The positive-cone Gram estimate is a finite Dirichlet-polynomial statement valid independently of any continuation of zeta.

## Research consequence

The live post-`PL-393` question can be narrowed. A coupled-height proposal should not be accepted merely because its cutoff grows with `T` or because it is tuned to the Riemann--Siegel length: at that length the entire frozen positive-cone quadratic Gram operator is already asymptotically Haar by `PL-072`.

The first canonical continuation-sensitive object instead has three ingredients simultaneously: the positive exponent packet, its reflected negative packet, and the archimedean Gamma-phase chirp. In quadratic interactions those ingredients produce the shell

\[
\langle v(n)+v(m),(\log p)_p\rangle\approx\log(t/(2\pi)).
\]

Future finite-height work should therefore test observables that genuinely retain this self-dual cross channel (or another representative-sensitive continuation mechanism) and are sensitive to individual zeros. Repackaging only the same-sign `v(n)-v(m)` Gram geometry at `N asymp sqrt(T)` is already ruled out by the classical finite-time estimate.