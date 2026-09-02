# PC-125 — relative-scale resultant spectralization is purely cyclotomic

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` + `PRIOR-ART-REDIRECTION`.

PC-002/PC-004 use the scalar shell resultant

\[
\operatorname{Res}(\Phi_m,\Phi_n)
\]

as the exact total logarithmic interaction between two primitive root shells. A natural attempt to retain information discarded by evaluation at one geometry is to promote the relative rotation/radial scale to a complex spectral parameter before taking the resultant. That deformation is intrinsic to the original prime-circle geometry: one shell remains on the unit circle while the second is multiplied by a single complex number `t`.

For this natural spectralization there is an exact obstruction. The entire divisor in `t` is already finite cyclotomic torsion. No Riemann-zero-like divisor, critical line, or new spectral scale is created.

## 1. Relative-scale shell resultant

For `m,n>1`, put

\[
R_{m,n}(t)
:=
\operatorname{Res}_z\!\bigl(\Phi_m(z),\Phi_n(tz)\bigr).
\]

Since `Phi_m` is monic,

\[
R_{m,n}(t)
=
\prod_{\alpha\in P_m^*}\Phi_n(t\alpha)
=
\prod_{\alpha\in P_m^*}
\prod_{\beta\in P_n^*}
(t\alpha-\beta).
\]

Thus the zeros are exactly the relative collision parameters

\[
\boxed{t=\beta/\alpha,
\qquad
\alpha\in P_m^*,\ \beta\in P_n^*.}
\]

If

\[
L=\operatorname{lcm}(m,n),
\]

then every ratio `beta/alpha` belongs to `mu_L`. Hence every zero of `R_{m,n}` is a root of unity of order dividing `L`.

The coefficients of `Phi_n(tz)` lie in `Z[t]`, so the resultant lies in `Z[t]`. Its leading coefficient is a sign. Therefore, after the harmless monic sign normalization

\[
\widehat R_{m,n}(t)
:=(-1)^{\varphi(m)\varphi(n)}R_{m,n}(t),
\]

there are nonnegative integers `e_d(m,n)` such that

\[
\boxed{
\widehat R_{m,n}(t)
=
\prod_{d\mid L}\Phi_d(t)^{e_d(m,n)}.
}
\]

This is not merely a statement about the location of the zeros. It classifies the full finite spectral divisor as a product of ordinary cyclotomic polynomials.

## 2. Exact multiplicities are Ramanujan triple correlations

For a fixed `gamma in mu_L`, let

\[
N_{m,n}(\gamma)
:=
\#\{(\alpha,\beta)\in P_m^*\times P_n^*:\beta/\alpha=\gamma\}.
\]

On the finite cyclic group `mu_L`, the indicator of the exact-order-`r` shell has Fourier transform `c_r(k)`, the Ramanujan sum. Fourier inversion therefore gives

\[
\boxed{
N_{m,n}(\gamma)
=
\frac1L\sum_{k=0}^{L-1}
 c_m(k)c_n(k)\gamma^{-k}.
}
\]

Galois automorphisms of `Q(mu_L)` preserve exact orders and act transitively on primitive `d`-th roots, so `N_{m,n}(gamma)` depends only on `d=ord(gamma)`. This common value is precisely the cyclotomic multiplicity `e_d(m,n)`. Averaging the preceding identity over primitive `d`-th roots yields

\[
\boxed{
 e_d(m,n)
 =
 \frac{1}{L\varphi(d)}
 \sum_{k=0}^{L-1}
 c_m(k)c_n(k)c_d(k).
}
\]

The right-hand side is therefore automatically a nonnegative integer. All arithmetic retained by the parameterized resultant is a finite Ramanujan correlation on the same cyclic group containing the two shells.

The degree check is exact:

\[
\sum_{d\mid L}e_d(m,n)\varphi(d)
=
\varphi(m)\varphi(n).
\]

## 3. The ordinary shell resultant is only the specialization `t=1`

At `t=1`,

\[
R_{m,n}(1)=\operatorname{Res}(\Phi_m,\Phi_n),
\]

so PC-002 is recovered by evaluating the full cyclotomic divisor at one point. For distinct shells `e_1(m,n)=0`; hence the specialization is nonzero and

\[
\bigl|R_{m,n}(1)\bigr|
=
\prod_{\substack{d\mid L\\d>1}}
\Phi_d(1)^{e_d(m,n)}.
\]

The classical identity

\[
\Phi_d(1)=
\begin{cases}
p,&d=p^a,\\
1,&d>1\text{ is not a prime power}
\end{cases}
\]

then explains why evaluating at the coincident scale collapses the richer finite torsion divisor to the prime-power resultant support seen in PC-002/PC-004.

Thus promoting the resultant to a relative-scale polynomial does retain more angular information than `R_{m,n}(1)`, but the extra information is exactly the finite root-of-unity ratio distribution, not a new analytic spectrum.

## 4. Exact stress tests

Direct symbolic resultant calculations agree with the factorization and multiplicity formula. Representative examples are

\[
\begin{aligned}
\widehat R_{3,5}(t)&=\Phi_{15}(t),\\
\widehat R_{3,9}(t)&=\Phi_9(t)^2,\\
\widehat R_{6,15}(t)&=\Phi_{10}(t)^2\Phi_{30}(t),\\
\widehat R_{8,12}(t)&=\Phi_{24}(t)^2.
\end{aligned}
\]

Consequently

\[
R_{3,9}(1)=9,
\qquad
R_{6,15}(1)=R_{8,12}(1)=1,
\]

matching the classical cyclotomic-resultant specialization. The Ramanujan triple-correlation formula gives the same exponents in each case.

These checks are only stress tests; the root-ratio and Fourier arguments above are exact for all `m,n>1`.

## 5. Why this does not produce a critical-line mechanism

For `0<|t|<1` there are no zeros at all. On the unit circle, zeros occur exactly when a rotated/scaled shell collides with the other shell, at rational torsion angles. A logarithmic derivative is consequently only

\[
\frac{R'_{m,n}(t)}{R_{m,n}(t)}
=
\sum_{d\mid L}e_d(m,n)
\frac{\Phi_d'(t)}{\Phi_d(t)},
\]

a rational cyclotomic function.

If one introduces a logarithmic coordinate `t=e^{-s}`, every zero lifts to an arithmetic imaginary lattice because `t` is a root of unity. In the unshifted coordinate the divisor lies on `Re(s)=0`; replacing `t` by `e^{-(s-1/2)}` merely translates that torsion divisor to `Re(s)=1/2` by definition. It does not generate the Riemann ordinates, the gamma factor, the zero-counting law, or the functional equation.

Likewise the reciprocal symmetry inherited from unit-circle roots is only the finite cyclotomic inversion `t <-> 1/t`. Re-centering its logarithmic coordinate at `1/2` would insert the critical line rather than derive it.

Therefore the natural route

\[
\boxed{
\text{pairwise primitive-shell resultant}
\to
\text{relative rotation/dilation parameter}
\to
\text{spectral divisor}
\to
\text{RH}
}
\]

fails at the second arrow: its full divisor is already cyclotomic torsion.

## 6. Prior art and novelty audit

The general scaled-resultant problem is classical. T. M. Apostol, **The Resultant of the Cyclotomic Polynomials `F_m(ax)` and `F_n(bx)`**, *Mathematics of Computation* 29 (1975), 1–6, calculated the resultant for arbitrary positive integers `m,n` and arbitrary nonzero complex scaling parameters `a,b`. This directly contains the algebraic family to which `R_{m,n}(t)` belongs. The earlier Apostol 1970 theorem used in PC-002 is the unscaled specialization.

Accordingly, no theorem-level novelty is claimed for parameterized cyclotomic resultants. The exact root-ratio factorization, its Ramanujan multiplicity formula, and the Prime-Circle interpretation are recorded here as a **negative classification**: the most direct way to turn the pairwise shell resultant into a one-complex-parameter spectral object remains entirely within classical cyclotomic/Ramanujan data.

This also matches the broader boundary established by PC-021, PC-024, PC-037 and PC-124: adding a spectral wrapper that is determined by finite root-of-unity data does not by itself create the global analytic structure needed for RH.

## 7. Boundary of the obstruction

PC-125 rules out the single-parameter deformation obtained by multiplying one complete primitive shell by one complex scalar before taking the resultant, and any finite product of such divisors. It does **not** rule out:

- genuinely nonuniform deformations in which different vertices move by different coupled parameters;
- noncommutative or matrix-valued cross-level transport that is not determined by the scalar resultant;
- an infinite cross-level construction whose convergence/renormalization contributes genuinely new analytic structure rather than merely multiplying these finite cyclotomic divisors;
- the nonlinear uniformization/monodromy sector represented by PC-017.

Any future resultant-based RH candidate should therefore demonstrate where it leaves this finite cyclotomic-torsion class before its spectral interpretation is counted as progress.
