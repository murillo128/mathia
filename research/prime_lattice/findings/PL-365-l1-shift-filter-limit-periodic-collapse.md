# PL-365 — `ell^1` lattice-shift filters are bounded but collapse to limit-periodic outputs with the same `0/1` convergence strip

**Evidence:** `EXACT-DERIVED + CLASSICAL-WIENER-DIRICHLET/WINTNER-CONTROL + DECISIVE-NEGATIVE`.

**Parent finding:** `PL-364`.

**Status:** `THE-FIRST-NATURAL-OPERATOR-NORM-CONSTRAINED-INFINITE-SHIFT-CLASS-IS-NONPROGRAMMABLE-BUT-STILL-ONLY-PRODUCES-LIMIT-PERIODIC-CANCELLATION-WITH-NO-CRITICAL-LINE-RIGIDITY`.

## Precise claim

`PL-364` shows that an unrestricted infinite signed lattice-shift filter is algebraically universal: by Möbius inversion its coefficients can program an arbitrary arithmetic output. It therefore leaves as the next meaningful regime an independently justified analytic restriction on the filter. The strongest elementary such restriction is absolute summability.

Let

\[
c=(c_m)_{m\ge1}\in \ell^1(\mathbb N),
\qquad
S_m e_n=e_{mn},
\tag{PL365-1}
\]

on the standard coefficient Hilbert space `mathcal H^2 ~= ell^2(N)` of Dirichlet series. Then

\[
T_c:=\sum_{m\ge1}c_mS_m
\tag{PL365-2}
\]

converges in operator norm and

\[
\|T_c\|\le \|c\|_1.
\tag{PL365-3}
\]

On the formal coefficient-one zeta source `Omega=sum_{n>=1}e_n`, which is **not** itself an `mathcal H^2` vector, the coefficientwise readout remains

\[
b_n=(c*\mathbf 1)(n)=\sum_{d\mid n}c_d.
\tag{PL365-4}
\]

Unlike the unconstrained class of `PL-364`, these outputs cannot be arbitrary. They are uniformly limit-periodic: if

\[
b_n^{(M)}:=\sum_{\substack{d\mid n\\d\le M}}c_d,
\qquad
L_M:=\operatorname{lcm}(1,\ldots,M),
\tag{PL365-5}
\]

then `b^(M)` is periodic modulo `L_M` and

\[
\sup_n|b_n-b_n^{(M)}|
\le \sum_{d>M}|c_d|\longrightarrow0.
\tag{PL365-6}
\]

Write

\[
C(s):=\sum_{d\ge1}c_dd^{-s},
\qquad
A:=C(1)=\sum_{d\ge1}\frac{c_d}{d}.
\tag{PL365-7}
\]

The output summatory function has the exact uniform estimate

\[
\boxed{
\sum_{n\le x}b_n=xA+R(x),
\qquad
|R(x)|\le \|c\|_1.
}
\tag{PL365-8}
\]

Hence the same single pole-cancellation condition as in the finite case,

\[
C(1)=0,
\tag{PL365-9}
\]

forces bounded partial sums. For every nonzero `c in ell^1` satisfying (PL365-9), the ordinary and absolute abscissae of the output Dirichlet series

\[
B(s):=\sum_{n\ge1}b_nn^{-s}
\tag{PL365-10}
\]

are exactly

\[
\boxed{\sigma_c(B)=0,\qquad \sigma_a(B)=1.}
\tag{PL365-11}
\]

Moreover, initially by an absolutely convergent Dirichlet product only for `Re(s)>1`,

\[
B(s)=C(s)\zeta(s).
\tag{PL365-12}
\]

The bounded-partial-sum argument independently defines the left side by ordinary locally uniform convergence throughout `Re(s)>0`. Since `C` is holomorphic there and (PL365-9) removes zeta's simple pole at `1`, identity theorem then extends (PL365-12) to `Re(s)>0` when the right side is interpreted using the known meromorphic continuation of zeta.

Thus imposing the first natural operator-norm summability constraint does remove the programmability pathology of `PL-364`, but it **does not improve the RH geometry**. The output class is the uniform closure of periodic divisor filters, the conditional-convergence strip remains exactly `0<Re(s)<=1`, and `Re(s)=1/2` is not distinguished.

## 1. The infinite filter is now a genuine bounded operator

Every multiplicative shift `S_m` is an isometry on coefficient `ell^2`:

\[
\|S_m f\|_2=\|f\|_2.
\tag{PL365-13}
\]

Therefore

\[
\sum_{m\ge1}\|c_mS_m\|
=\sum_{m\ge1}|c_m|<\infty,
\tag{PL365-14}
\]

so (PL365-2) converges absolutely in operator norm. On Dirichlet polynomials, this operator is multiplication by the absolutely convergent Dirichlet series `C(s)` from (PL365-7). In particular,

\[
|C(s)|\le \|c\|_1
\qquad (\operatorname{Re}s\ge0),
\tag{PL365-15}
\]

and `C` belongs to the classical Wiener–Dirichlet algebra of absolutely convergent Dirichlet series.

This removes an important caveat from `PL-364`: the filter itself is no longer merely formal. A different caveat remains essential, however. The coefficient-one vector `Omega` has infinite `ell^2` norm, so `T_c Omega` is not an application of a bounded Hilbert-space operator to a Hilbert-space vector. Equation (PL365-4) is still a **coefficientwise source readout**, justified because each coefficient receives only finitely many divisor contributions.

## 2. Absolute summability forces limit-periodic arithmetic geometry

For fixed `M`, each indicator `1_{d|n}` with `d<=M` is periodic with period `d`. Consequently the finite divisor sum `b^(M)` in (PL365-5) is periodic with period `L_M`. The `ell^1` tail gives the uniform estimate (PL365-6), so `b` is a limit-periodic sequence, hence a Bohr uniformly almost-periodic sequence on the integer index.

This is a genuinely stronger restriction than the algebraic setting of `PL-364`. Möbius inversion still gives the formal inverse `c=mu*b`, but a target sequence is reachable in this operator-norm class only if its Möbius transform lies in `ell^1`; in particular an arbitrary arithmetic target is no longer programmable.

The terminology must not be confused with the vertical almost-periodicity of Dirichlet series under `s -> s+it`. Here the almost-periodicity is in the **integer coefficient index `n`**, arising because divisibility indicators are uniformly approximated by finite periodic divisor patterns.

## 3. Exact summatory law and the sharp conditional strip

For real `x>=1`, finite rearrangement gives

\[
\begin{aligned}
S_b(x)
:=\sum_{n\le x}b_n
&=\sum_{n\le x}\sum_{d\mid n}c_d\\
&=\sum_{d\le x}c_d\left\lfloor\frac{x}{d}\right\rfloor.
\end{aligned}
\tag{PL365-16}
\]

Subtracting `xA` yields

\[
S_b(x)-xA
=
\sum_{d\le x}c_d
\left(\left\lfloor\frac{x}{d}\right\rfloor-\frac{x}{d}\right)
-x\sum_{d>x}\frac{c_d}{d}.
\tag{PL365-17}
\]

Therefore

\[
|S_b(x)-xA|
\le
\sum_{d\le x}|c_d|
+
\sum_{d>x}|c_d|
=
\|c\|_1,
\tag{PL365-18}
\]

which proves (PL365-8). Under `A=0`, Abel/Dirichlet summation gives ordinary locally uniform convergence of (PL365-10) for every `Re(s)>0`; equivalently,

\[
B(s)=s\int_1^\infty S_b(x)x^{-s-1}\,dx
\tag{PL365-19}
\]

there, with the usual step-function interpretation of `S_b`.

The boundary is sharp for every nonzero filter. Since convolution by `mathbf 1` is injective by Möbius inversion, `c != 0` implies `b != 0`. Choose `n_0` with `|b_{n_0}|=delta>0`, then choose `M>=n_0` so that the `ell^1` tail in (PL365-6) is below `delta/4`. Periodicity of `b^(M)` gives

\[
b^{(M)}_{n_0+kL_M}=b^{(M)}_{n_0}
\qquad(k\ge0),
\tag{PL365-20}
\]

and the uniform tail estimate implies

\[
|b_{n_0+kL_M}|\ge \delta/2.
\tag{PL365-21}
\]

Thus the terms `b_n n^{-s}` fail to tend to zero anywhere on `Re(s)<=0`, proving `sigma_c=0`. The same arithmetic progression has positive density, so

\[
\sum_n |b_n|n^{-\sigma}
\tag{PL365-22}
\]

diverges for every real `sigma<=1`; while `|b_n|<=||c||_1` gives absolute convergence for `sigma>1`. Hence `sigma_a=1` and (PL365-11) follows.

The infinite `ell^1` class therefore enlarges finite periodic filters to genuinely nonperiodic limit-periodic outputs, but **does not move either convergence boundary** found in `PL-363`.

## 4. What survives in the critical strip — and what does not

For `Re(s)>1`, both `C(s)` and zeta's coefficient-one series are absolutely convergent, so Dirichlet convolution rigorously gives (PL365-12). No claim below that line is obtained by formally continuing an Euler product.

When `C(1)=0`, the coefficient argument above already defines `B(s)` holomorphically on `Re(s)>0`. Separately, the known meromorphic continuation of zeta shows that `C(s)zeta(s)` is holomorphic on the same half-plane because the only zeta pole there is the simple pole at `1`, cancelled by `C(1)=0`. Agreement on `Re(s)>1` and the identity theorem then give

\[
\boxed{B(s)=C(s)\zeta(s)\quad\text{on }\operatorname{Re}s>0,}
\tag{PL365-23}
\]

with the domains and justification kept distinct.

This does put an ordinary convergent filtered series on the critical line, exactly as finite eta-type filters do. It does **not** produce a continuation or localization theorem for zeta itself. Recovering zeta requires division by `C`, whose zero set is independent filter data, and the construction supplies no reason for `C` to be canonical, zero-free in the desired region, compatible with the functional equation, positive in a Weil sense, or spectrally tied to the zeta divisor.

Indeed one can prescribe extraneous filter zeros even inside this constrained class. Given any chosen point `s_0 != 1`, a nonzero three-term filter supported on `{1,2,3}` can be chosen to satisfy simultaneously

\[
C(1)=c_1+\frac{c_2}{2}+\frac{c_3}{3}=0,
\qquad
C(s_0)=c_1+c_2 2^{-s_0}+c_3 3^{-s_0}=0,
\tag{PL365-24}
\]

because these are only two homogeneous linear conditions on three coefficients. Such a filter already lies in `ell^1`. This finite-support stress test is not new relative to `PL-363`; it simply shows that the `ell^1` operator restriction does not turn filter zeros into arithmetic evidence.

## 5. Prior-art and novelty audit

No theorem-level novelty is claimed for the surrounding functional analysis or mean-value theory.

Bayart, Finet, Li and Queffélec study the classical Wiener–Dirichlet algebra `A^+` of absolutely convergent Dirichlet series, with `ell^1` coefficient norm, in **F. Bayart, C. Finet, D. Li, H. Queffélec, “Composition operators on the Wiener-Dirichlet algebra,” Journal of Operator Theory 60 (2008), 45–70**, https://jot.theta.ro/jot/archive/2008-060-001/2008-060-001-003.pdf. Thus the analytic class imposed in (PL365-1) is standard prior art, not a newly invented function space.

The mean-value aspect of (PL365-8) also lies inside classical Wintner theory. Wintner's theorem gives the mean of `f=mathbf 1*g` under the weaker weighted condition `sum |g(n)|/n < infinity`; a modern statement identifying the `k=1` case explicitly as Wintner's theorem appears in **R. Heyman and L. Tóth, “Hyperbolic summation for functions of the GCD and LCM of several integers,” Ramanujan Journal 62 (2023), 273–290**, https://doi.org/10.1007/s11139-022-00681-2. The stronger uniform `O(1)` remainder in (PL365-8) under the stronger assumption `c in ell^1` is derived directly above and is not presented as a novelty claim.

The durable delta is the **route classification relative to `PL-364`**. That finding explicitly left `ell^1` as a natural first constrained infinite-filter regime. The present calculation closes that regime: operator-norm summability is strong enough to eliminate arbitrary programmability, but so strong that the resulting coefficient geometry is merely limit-periodic and retains exactly the same `sigma_c=0`, `sigma_a=1` strip as the finite periodic filters of `PL-363`. It therefore does not expose a hidden `Re(s)=1/2` transition.

A search over the Wiener–Dirichlet, Wintner mean-value, almost-periodic arithmetic-function, and divisor-convolution literature found the individual ingredients to be classical but did not identify a source claiming an RH mechanism from this `ell^1` shift-filter class. Nothing here should be advertised as a new theorem of analytic number theory; the substantive research value is the exact negative boundary it places on the prime-lattice program.

## 6. Adversarial boundaries

1. **`ell^1` is sufficient, not necessary, for a bounded shift multiplier.** The finding does not classify all bounded multipliers of `mathcal H^2`, weighted `ell^2` filters, Schatten-type combinations, or other weaker operator classes. Those remain distinct regimes.

2. **The source vector remains formal.** Even though `T_c` is now a genuine bounded operator, `Omega` is outside `mathcal H^2`; the arithmetic output `b` is a coefficientwise readout, not a Hilbert-space vector `T_c Omega`. In fact the limit-periodic output need not lie in `ell^2`.

3. **Pole cancellation is chosen, not forced.** The condition `C(1)=0` uses prior knowledge of zeta's pole. Nothing in the bare exponent lattice forces that equation or a distinguished filter satisfying it.

4. **Ordinary convergence stops sharply at `Re(s)=0`.** The `ell^1` hypothesis does not by itself give analytic continuation of `C` through that boundary. An infinite Wiener–Dirichlet filter may have no continuation to the left, unlike the finite exponential polynomials of `PL-363`.

5. **The filtered product is not zeta.** Equation (PL365-23) is a statement about `B=C zeta`; dividing by `C` introduces independently chosen filter zeros. A zero or spectral feature of `B` must therefore be separated into inherited zeta data and filter data before it can have RH significance.

6. **Limit-periodicity here is coefficient-index geometry.** It should not be conflated with Bohr's vertical almost-periodicity in the complex variable `s`, Kronecker flow on the infinite prime torus, or a spectral statement about zeta zeros.

7. **No functional-equation or self-adjoint structure appears.** Absolute summability supplies boundedness and uniform periodic approximation, but no involution `s <-> 1-s`, archimedean factor, trace formula, positivity criterion, or mechanism forcing inherited zeros onto `Re(s)=1/2`.

## Research consequence

The first independently constrained infinite-filter escape from `PL-364` is now closed. Requiring operator-norm absolute summability produces a legitimate bounded lattice operator and destroys coefficientwise universality, but the price is a rigid limit-periodic arithmetic class whose pole-cancelling Dirichlet series still has the exact classical conditional strip

\[
0<\operatorname{Re}s\le1
\tag{PL365-25}
\]

with no internal transition at `1/2`.

A next filter-based candidate must therefore weaken or change the constraint rather than merely enlarge support inside `ell^1`: for example a genuinely larger multiplier/weighted-`ell^2` class, a scale-dependent source-forced renormalization, or non-coefficientwise mixing. Any such candidate must also explain why its cancellation and zero structure are forced by the arithmetic source rather than freely chosen filter data.