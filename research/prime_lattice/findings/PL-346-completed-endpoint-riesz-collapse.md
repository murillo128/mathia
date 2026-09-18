# PL-346 — The completed endpoint state collapses to the classical logarithmic Riesz residual

**Evidence:** `LITERATURE+EXACT-DERIVED + FULL-WEIL-COMPLETION + CLASSICAL-RIESZ-REDUCTION + DECISIVE-NEGATIVE`

**Status:** `FULL-SAME-STATE-CLOSURE + INNER-PRIME-MISMATCH-RESOLVED + LI-ONE-CONSTANT + NO-NEW-RH-MECHANISM`

## Precise claim

`PL-341` identified the sharp Schur endpoint state for the PNT-scale prime block, while `PL-345` showed that the centered outer-shell response is asymptotic to the classical first logarithmic Riesz residual

\[
\mathcal R_a(0)
=
e^{-a}\left[
\sum_{n<e^{2a}}\Lambda(n)(2a-\log n)
-
\int_1^{e^{2a}}(2a-\log x)\,dx
\right].
\tag{PL346-1}
\]

What remained open in `PL-345` was whether the **full completed Weil form on the same endpoint state** supplies an additional order-one term capable of changing that conclusion. It does not.

Put

\[
N_a:=1-e^{-a}
\]

and take the normalized even endpoint state

\[
u_a(x)
=
\frac{e^{-(a-|x|)/2}}{\sqrt{2N_a}}
\mathbf 1_{|x|<a}.
\tag{PL346-2}
\]

This function belongs to the logarithmic Fourier form domain of the localized Weil form despite its endpoint jumps. With the completed Weil normalization used in `PL-059`, `PL-061`, and source 26, one has

\[
\boxed{
Q_W^a(u_a)
=
2+\gamma_E-\log(4\pi)-\mathcal R_a(0)+o(1)
}
\qquad(a\to\infty).
\tag{PL346-3}
\]

Equivalently, using the absolutely convergent zero expansion from `PL-345`,

\[
\boxed{
Q_W^a(u_a)
=
C_\zeta+
\sum_\rho\frac{e^{(2\rho-1)a}}{\rho^2}
+o(1),
\qquad
C_\zeta:=2+\gamma_E-\log(4\pi)=2\lambda_1.
}
\tag{PL346-4}
\]

The sum is over nontrivial zeros with multiplicity. Consequently

\[
\boxed{
\sup_{a\ge a_0}|Q_W^a(u_a)|<\infty
\quad\Longleftrightarrow\quad
RH.
}
\tag{PL346-5}
\]

However, (PL346-5) is **not a new RH criterion**: by (PL346-3) it is exactly the classical logarithmic Riesz boundedness criterion already isolated in `PL-345`, transported into this completed endpoint-state geometry. The full completion supplies a fixed Li-coefficient constant but no independent zero-localizing rigidity.

The main correction to the unfinished comparison in `PL-345` is also precise. The previously observed `3a+O(1)` mismatch arose from comparing the exact pole term only with the **outer** prime shell. The omitted same-end/inner prime sector contributes at the missing linear scale. The archimedean integral tends to zero and does **not** repair that mismatch.

## 1. Exact autocorrelation of the endpoint state

Let

\[
\phi_a:=u_a*\widetilde u_a,
\qquad
\widetilde u_a(x)=\overline{u_a(-x)}.
\]

The state is real and even, so `phi_a` is real and even. Direct integration gives, for `x>=0`,

\[
\phi_a(x)
=
\begin{cases}
\displaystyle
\frac{e^{-x/2}+(x/2-1)e^{-a+x/2}}{N_a},
&0\le x\le a,\\[1.2ex]
\displaystyle
\frac{(2a-x)e^{-a+x/2}}{2N_a},
&a\le x\le2a,\\[1.2ex]
0,&x\ge2a.
\end{cases}
\tag{PL346-6}
\]

In particular,

\[
\phi_a(0)=1,
\]

and the two displayed pieces agree at `x=a`.

For `0<=x<=a`, the difference from the elementary archimedean reference profile has the exact form

\[
\phi_a(x)-e^{-x/2}
=
\frac{e^{-a}}{N_a}
\left[
 e^{-x/2}+
 \left(\frac x2-1\right)e^{x/2}
\right].
\tag{PL346-7}
\]

The bracket vanishes to second order at `x=0`. This observation will make the archimedean singularity harmless.

## 2. The full prime term contains the missing same-end contribution

For an even autocorrelation, the positive magnitude of the nonarchimedean term is

\[
\mathcal P_a
:=
2\sum_{n<e^{2a}}
\frac{\Lambda(n)}{\sqrt n}\,\phi_a(\log n),
\tag{PL346-8}
\]

so that the completed Weil form contains `-mathcal P_a`. Set `X=e^a`. Substituting (PL346-6) gives the exact split

\[
\boxed{
N_a\mathcal P_a
=
2\sum_{n<X}\frac{\Lambda(n)}n
+
X^{-1}\sum_{n<X}\Lambda(n)(\log n-2)
+
X^{-1}\sum_{X\le n<X^2}\Lambda(n)(2a-\log n).
}
\tag{PL346-9}
\]

The first two terms are exactly the same-end/inner sector absent from the outer-only comparison of `PL-345`.

Let

\[
W_a:=\sum_{n<X^2}\Lambda(n)(2a-\log n).
\]

Combining the last two sums in (PL346-9),

\[
N_a\mathcal P_a
=
2\sum_{n<X}\frac{\Lambda(n)}n
+
X^{-1}W_a
+
2X^{-1}\sum_{n<X}\Lambda(n)(\log n-a-1).
\tag{PL346-10}
\]

The prime number theorem and partial summation give

\[
\sum_{n<X}\frac{\Lambda(n)}n
=
a-\gamma_E+o(1),
\tag{PL346-11}
\]

and

\[
X^{-1}\sum_{n<X}\Lambda(n)(\log n-a-1)
=-2+o(1).
\tag{PL346-12}
\]

By definition of the `PL-345` residual,

\[
X^{-1}W_a
=
X-\frac{2a+1}{X}+\mathcal R_a(0),
\tag{PL346-13}
\]

because

\[
\int_1^{X^2}\log\frac{X^2}{x}\,dx
=X^2-1-2a.
\]

Substitution into (PL346-10) yields

\[
N_a\mathcal P_a
=
X+2a-4-2\gamma_E+\mathcal R_a(0)+o(1).
\tag{PL346-14}
\]

Finally `N_a=1-X^{-1}`. Dividing by `N_a` contributes the extra constant `+1` from the leading `X` term, so

\[
\boxed{
\mathcal P_a
=
e^a+2a-3-2\gamma_E+\mathcal R_a(0)+o(1).
}
\tag{PL346-15}
\]

This is the term that resolves the linear mismatch left by the outer-shell calculation.

## 3. Pole, scalar, and archimedean completion

The pole contribution factors through the bilateral Laplace functionals as in `PL-059`. Directly on (PL346-2),

\[
Q_{\rm pole}(u_a)
=
\frac{e^a}{N_a}\bigl(N_a+ae^{-a}\bigr)^2,
\tag{PL346-16}
\]

and hence

\[
\boxed{
Q_{\rm pole}(u_a)
=
e^a+2a-1+o(1).
}
\tag{PL346-17}
\]

The scalar term in the Bombieri/Weil additive explicit formula is

\[
-(\log4\pi+\gamma_E)\phi_a(0)
=
-(\log4\pi+\gamma_E).
\tag{PL346-18}
\]

It remains to check that the residual archimedean integral is not hiding another order-one correction. In the normalization of source 26 it is

\[
Q_{\infty,a}
=
-\int_0^\infty
\left[
\phi_a(x)+\phi_a(-x)-2e^{-x/2}\phi_a(0)
\right]
\frac{e^{x/2}}{e^x-e^{-x}}\,dx.
\tag{PL346-19}
\]

The kernel is `O(1/x)` at zero and `O(e^{-x/2})` at infinity. On `0<=x<=a`, (PL346-7) vanishes quadratically at zero and gives an integral `O(a^2e^{-a})`. On `a<=x<=2a`, (PL346-6) together with the exponential decay of the kernel gives the same bound; on `x>=2a`, `phi_a=0` and the remaining reference tail is `O(e^{-2a})`. Therefore

\[
\boxed{
Q_{\infty,a}=O(a^2e^{-a})=o(1).
}
\tag{PL346-20}
\]

Combining (PL346-15), (PL346-17), (PL346-18), and (PL346-20) gives

\[
Q_W^a(u_a)
=
\bigl(e^a+2a-1\bigr)
-
\bigl(e^a+2a-3-2\gamma_E+\mathcal R_a(0)\bigr)
-
(\log4\pi+\gamma_E)
+o(1),
\]

which is exactly (PL346-3).

Thus the bookkeeping of the full completed form is:

\[
\text{pole}-\text{all primes}
\longrightarrow
2+2\gamma_E-\mathcal R_a(0),
\]

then the scalar term leaves `C_zeta-mathcal R_a(0)`, while the residual archimedean integral vanishes.

## 4. Independent zero-side audit

The prime-side calculation can be checked without using its asymptotic decomposition. For

\[
V_z(u):=\int_{\mathbb R}u(x)e^{zx}\,dx,
\]

direct integration gives, at `z=rho-1/2`,

\[
V_{\rho-1/2}(u_a)
=
\frac1{\sqrt{2N_a}}
\left[
\frac{e^{a(1/2-\rho)}}{1-\rho}
+
\frac{e^{a(\rho-1/2)}}{\rho}
-
e^{-a/2}
\left(
\frac1{1-\rho}+\frac1\rho
\right)
\right].
\tag{PL346-21}
\]

Because `u_a` is real and even, the zero-side Weil quadratic form is obtained by summing the corresponding squares and pairing the zero set under `rho -> 1-rho`. Expanding (PL346-21) gives the exact identity

\[
Q_W^a(u_a)
=
\frac1{N_a}
\left[
S_a+C_\zeta-2T_a+\frac{e^{-a}}2U
\right],
\tag{PL346-22}
\]

where

\[
S_a:=\sum_\rho\frac{e^{(2\rho-1)a}}{\rho^2},
\tag{PL346-23}
\]

\[
T_a:=\sum_\rho
\frac{e^{a(\rho-1)}}{\rho^2(1-\rho)},
\tag{PL346-24}
\]

and

\[
U:=\sum_\rho\frac1{\rho^2(1-\rho)^2}.
\tag{PL346-25}
\]

The paired constant is

\[
C_\zeta
=
\sum_\rho\frac1{\rho(1-\rho)}
=
2+\gamma_E-\log(4\pi)
=
2\lambda_1.
\tag{PL346-26}
\]

All sums in (PL346-22) are absolutely convergent after the displayed pairing: the Riemann--von Mangoldt count gives convergence of the relevant `|rho|^{-2}`, `|rho|^{-3}`, and `|rho|^{-4}` tails. Since every nontrivial zero satisfies `0<Re rho<1`, dominated convergence gives

\[
T_a\to0,
\qquad
e^{-a}U\to0,
\qquad
N_a\to1.
\tag{PL346-27}
\]

Hence

\[
Q_W^a(u_a)=C_\zeta+S_a+o(1),
\tag{PL346-28}
\]

which is (PL346-4). By `PL-345`,

\[
\mathcal R_a(0)=-S_a+O(ae^{-a}),
\tag{PL346-29}
\]

so the prime-side and zero-side derivations agree term by term at the claimed order.

This audit is useful because it detects sign or completion mistakes immediately: the prime/pole/scalar/archimedean calculation and the zero-side expansion are independent representations of the same closed Weil form.

## 5. RH equivalence and the exact scope of the negative result

`PL-345` proved

\[
\sup_{a\ge a_0}|\mathcal R_a(0)|<\infty
\quad\Longleftrightarrow\quad RH.
\tag{PL346-30}
\]

Equation (PL346-3) therefore yields (PL346-5). Under RH,

\[
S_a
=
\sum_\rho\frac{e^{2i\gamma a}}{\rho^2},
\]

an absolutely and uniformly convergent exponential series, so the completed endpoint observable is bounded and uniformly almost periodic up to the vanishing correction in (PL346-28). If RH fails, the same Riesz residual detects the off-line growth.

The important point is what this does **not** provide. The endpoint geometry has not manufactured a new condition forcing `Re rho=1/2`; it has selected a classical smoothing whose explicit formula already has neutral exponent `2 Re rho-1`. The completed state merely packages that known criterion as a single localized Weil Rayleigh value.

Accordingly, `DECISIVE-NEGATIVE` applies only to the route

\[
\text{PL-341 endpoint state}
+
\text{full same-state Weil completion}
\longrightarrow
\text{new endpoint spectral rigidity beyond the Riesz criterion}.
\]

It does **not** rule out different moving states, matrix-valued families, target-relative couplings, noncommutative observables, or structures that use more than this one endpoint Rayleigh value.

## 6. Prior-art, continuation, and matched-control audit

The underlying explicit formula and Weil quadratic functional are classical; source 25 is Weil's explicit-formula criterion and source 26 is Bombieri's formulation with the pole, prime, scalar, and archimedean terms used above. Source 56 gives the modern localized/screw-function realization of the same completed Weil form. `PL-345` already audited the first logarithmic Riesz mean as classical Hardy--Riesz/Dirichlet-series machinery.

A targeted literature check did not identify a published use of the exact endpoint profile (PL346-2) with the finite-`a` decomposition (PL346-22). No novelty is claimed from that profile: its only variable RH-sensitive asymptotic term is the already-classical logarithmic Riesz residual. The durable content here is the **closure of the line's unfinished same-state completion calculation** and the resulting negative redirect.

There is no illicit continuation of an Euler product. Equations (PL346-8)--(PL346-20) are prime-side identities plus PNT/partial summation inside the completed explicit formula. The zero expansion uses the analytically continued completed zeta/Weil distribution, exactly as in the classical explicit formula. The identity with `mathcal R_a(0)` is therefore a comparison between two legitimate representations of the same completed object, not a continuation of `sum Lambda(n)n^{-s}` beyond its half-plane of absolute convergence.

The matched-control conclusion is likewise limited. The leading `e^a+2a` pole/prime envelope is controlled by coarse PNT information and by the endpoint profile; that scale is not rational-prime-specific. The residual `S_a`, however, comes from the completed zeta divisor. Replacing the rational-prime source by a generalized prime system with its own explicit formula transports the same pattern with that system's zeros. Thus the endpoint construction does not force a Riemann-specific critical-line theorem from bare exponent-lattice geometry.

## Conclusion

The full completion answers the open bookkeeping question left by `PL-345`: **the missing linear term is supplied by the inner prime sector, not by the archimedean place**. After exact pole, scalar, and archimedean completion, the endpoint state's entire nonconstant order-one content is

\[
-\mathcal R_a(0)
\quad\text{or equivalently}\quad
\sum_\rho\frac{e^{(2\rho-1)a}}{\rho^2}.
\]

The fixed completion constant is `2 lambda_1`. Therefore this canonical endpoint family gives a clean geometric realization of the classical logarithmic Riesz criterion, but **no additional RH mechanism**. A future endpoint-based route must introduce information not already reducible to this one scalar Riesz observable.

## Sources

Uses existing entries in `research/prime_lattice/SOURCES.md`:

- source 25: André Weil, explicit-formula / positivity criterion.
- source 26: Enrico Bombieri, *Remarks on Weil's quadratic functional in the theory of prime numbers. I*.
- source 56: Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v2.

No new source entry is required.