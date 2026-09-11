# NB-055 — Hardy-regularized cell recurrence gives near-critical raw-tail decay

**Status:** `EXACT-DERIVED + CORRECTION/REPLACEMENT + HARDY-DOMAIN-REPAIR + REGULARIZED-CELL-RECURRENCE + FRACTIONAL-SHIFT-RATE + FINITE-GRID-RAW-TAIL + NEGATIVE/METHOD-BOUNDARY + LITERATURE-BACKED`.

This finding replaces the withdrawn `NB-054` claim and repairs the Hardy-domain error removed from `NB-053`. The invalid step was treating Burnol's deflated outer factor

\[
O(s)=\frac{s-1}{s}\frac{\zeta(s)}{B(s)}
\tag{1}
\]

as a vector of `H^2(Re s>1/2)`. It is not. The correct Hardy vector has one additional factor `1/s`:

\[
\boxed{
E(s):=\frac{O(s)}s
=\frac{s-1}{s^2}\frac{\zeta(s)}{B(s)}\in H^2(\Re s>1/2).
}
\tag{2}
\]

For the shift semigroup

\[
(U_tF)(s)=e^{-t(s-1/2)}F(s),
\tag{3}
\]

and the natural deflated closure

\[
\mathcal A_{\rm nat}=\overline{\operatorname{span}}\{\phi_{1/n}:n\ge2\},
\qquad Q=I-P_{\mathcal A_{\rm nat}},
\tag{4}
\]

the continuous generator has the exact `H^2` identity

\[
\boxed{
\phi_{e^{-a}}
=e^{-a}\left[
E-e^{a/2}U_aE+
\int_0^a e^{u/2}U_uE\,du
\right]
\qquad(a\ge0).
}
\tag{5}
\]

The integral is now a legitimate Bochner integral of a norm-continuous orbit. Since `phi_(1/n) in A_nat`, projecting (5) gives an exact recurrence across the shrinking logarithmic cells. If

\[
y(t)=Q U_tE,
\qquad y_n=y(\log n),
\qquad \Delta_n=\log\left(1+\frac1n\right),
\tag{6}
\]

then

\[
\boxed{
\sqrt{n+1}\,y_{n+1}-\sqrt n\,y_n
=
\int_{\log n}^{\log(n+1)}e^{u/2}y(u)\,du.
}
\tag{7}
\]

Unlike the withdrawn `NB-054` zero-mean law, (7) contains an endpoint transport term. That term changes the quantitative tail substantially, but it is still coercive enough to force the **regularized** source orbit into the natural closure:

\[
\boxed{
\sup_{t\ge\log N}\operatorname{dist}(U_tE,\mathcal A_{\rm nat})
\longrightarrow0.
}
\tag{8}
\]

More is available. For every `0<alpha<1/2`, the classical critical-line second moment of `zeta` gives a fractional boundary moment for `E`, hence

\[
\boxed{
\sup_{t\ge\log N}\operatorname{dist}(U_tE,\mathcal A_{\rm nat})
\ll_\alpha N^{-\alpha}.
}
\tag{9}
\]

This transfers to the finite `NB-050` enrichment grid. Uniformly for

\[
\frac1{n+1}\le\theta\le\frac1n,
\tag{10}
\]

one has

\[
\boxed{
\operatorname{dist}(\phi_\theta,\mathcal A_{\rm nat})
\ll_\alpha n^{-1/2-\alpha}
\qquad(0<\alpha<1/2).
}
\tag{11}
\]

Consequently, uniformly in the finite-grid parameters `M,N`,

\[
\boxed{
\frac1M
\sum_{\substack{M<k\le N\\ k/M\ge R}}
\operatorname{dist}(\phi_{M/k},\mathcal A_{\rm nat})^2
\ll_\alpha R^{-2\alpha}.
}
\tag{12}
\]

Equivalently, for every `epsilon>0`, the raw quotient-energy tail is `O_epsilon(R^(-1+epsilon))`. Thus the qualitative conclusion sought in `NB-054` survives after the domain repair — large-ratio **raw** quotient mass vanishes uniformly — but the claimed `o(R^-2)` rate does not follow and is withdrawn. As before, raw smallness does not control the span after normalization; tiny quotient columns may remain target-bearing through their directions and conditioning.

## 1. Why the unregularized outer factor is not in `H^2`

Burnol's primary argument records the Hardy-space function

\[
\frac{s-1}{s^2}\zeta(s)\in H^2(\Re s>1/2),
\tag{13}
\]

then removes the Blaschke product `B` associated with zeros to the right of the critical line. Because multiplication or division by the common inner factor preserves the boundary norm on the appropriate factor, (2) is in `H^2`.

By contrast, on the critical boundary `s=1/2+it`, `|B(s)|=1` almost everywhere and

\[
|O(s)|^2
=
\left|\frac{s-1}{s}\right|^2
|\zeta(s)|^2.
\tag{14}
\]

The rational prefactor tends to one as `|t|->infinity`. The classical Titchmarsh mean-square theorem gives

\[
\int_0^T|\zeta(1/2+it)|^2\,dt\asymp T\log T,
\tag{15}
\]

so the boundary square integral of `O` diverges. Hence

\[
\boxed{O\notin H^2(\Re s>1/2).}
\tag{16}
\]

This is not a cosmetic distinction. A modulus such as `sup_(0<=u<=r)||U_uO-O||` is not an `H^2` quantity, and the Bochner orbit integral used in the withdrawn `NB-054` proof was therefore not defined in the claimed Hilbert space.

## 2. The regularized generator identity is exact

The deflated continuous generator is

\[
\phi_{e^{-a}}(s)
=e^{-a}O(s)\frac{1-e^{-a(s-1)}}{s-1}.
\tag{17}
\]

Since `O=sE`, and

\[
e^{a/2}U_aE=e^{-a(s-1)}E,
\tag{18}
\]

while

\[
\int_0^a e^{u/2}U_uE\,du
=E\frac{1-e^{-a(s-1)}}{s-1},
\tag{19}
\]

we have

\[
\begin{aligned}
E-e^{a/2}U_aE+
\int_0^a e^{u/2}U_uE\,du
&=E\left(1-e^{-a(s-1)}\right)\left(1+\frac1{s-1}\right)\\
&=sE\frac{1-e^{-a(s-1)}}{s-1},
\end{aligned}
\tag{20}
\]

which is (5). Every term is now in `H^2`, so (5) is a genuine Hilbert-space identity.

Define

\[
H(a)=QE-e^{a/2}Q U_aE+
\int_0^a e^{u/2}Q U_uE\,du.
\tag{21}
\]

Equation (5) gives `H(a)=e^a Q phi_(e^-a)`. Since `phi_1=0` and `phi_(1/n) in A_nat`,

\[
H(\log n)=0\qquad(n\ge1).
\tag{22}
\]

Subtracting the identities at `log n` and `log(n+1)` yields (7). The endpoint term in (7) is exactly what disappears incorrectly if one differentiates through the non-Hardy factor `O` as though it were a fixed Hilbert vector.

## 3. The endpoint recurrence is backward stable

Let

\[
\omega_E(r)=\sup_{0\le v\le r}\|U_vE-E\|,
\qquad
\omega_n=\omega_E(\Delta_n).
\tag{23}
\]

Strong continuity gives `omega_n->0`. For `u in [log n,log(n+1)]`, semigroup isometry implies

\[
\|y(u)-y_n\|\le\omega_n.
\tag{24}
\]

Write

\[
c_n=1-\sqrt{\frac n{n+1}}.
\tag{25}
\]

Splitting the integral in (7) into the constant part `y_n` plus the variation gives

\[
\boxed{
y_{n+1}=(1+c_n)y_n+\varepsilon_n,}
\tag{26}
\]

with

\[
\|\varepsilon_n\|\le2c_n\omega_n.
\tag{27}
\]

Moreover

\[
\frac1{2(n+1)}\le c_n\le\frac1{2n}.
\tag{28}
\]

Let

\[
P_{n,j}=\prod_{k=n}^j(1+c_k).
\tag{29}
\]

Because `log(1+c)>=c/2` for the present range of `c`, (28) gives an absolute constant `C>0` such that

\[
P_{n,j}\ge C\left(\frac{j+2}{n+1}\right)^{1/4}.
\tag{30}
\]

The vectors `y_j` are bounded by `||E||`. Iterating (26) backwards and letting the upper endpoint tend to infinity therefore gives the convergent identity

\[
y_n=-\sum_{j=n}^\infty\frac{\varepsilon_j}{P_{n,j}}.
\tag{31}
\]

Since `omega_j<=omega_n` for `j>=n`, equations (27)--(30) imply

\[
\begin{aligned}
\|y_n\|
&\ll
\omega_n(n+1)^{1/4}
\sum_{j\ge n}j^{-5/4}\\
&\ll\omega_n.
\end{aligned}
\tag{32}
\]

For arbitrary `t` in the same cell, (24) then gives

\[
\boxed{
\sup_{t\in[\log n,\log(n+1)]}\|Q U_tE\|
\ll\omega_E(\Delta_n).
}
\tag{33}
\]

As the cell widths decrease, (33) proves (8). This is a fixed-source-orbit statement, not operator-norm convergence of `Q U_t`.

## 4. Critical-line mean square gives every fractional rate below `1/2`

On the critical boundary and for large `|t|`,

\[
|E(1/2+it)|^2
\asymp
\frac{|\zeta(1/2+it)|^2}{1+t^2},
\tag{34}
\]

because `|B|=1`. Fix `0<alpha<1/2`. On a dyadic block `[T,2T]`, the classical second-moment estimate gives

\[
\int_T^{2T}|t|^{2\alpha}|E(1/2+it)|^2\,dt
\ll
T^{2\alpha-1}\log T.
\tag{35}
\]

The dyadic series converges because `2alpha-1<0`. Therefore

\[
\int_{\mathbb R}|t|^{2\alpha}|E(1/2+it)|^2\,dt<\infty.
\tag{36}
\]

On the boundary, `U_h` multiplies by `e^{-iht}`. The elementary inequality

\[
|e^{-ix}-1|\ll_\alpha |x|^\alpha
\tag{37}
\]

and (36) give

\[
\boxed{\omega_E(h)\ll_\alpha h^\alpha.}
\tag{38}
\]

Since `Delta_n asymp 1/n`, equations (33) and (38) prove (9). The endpoint `alpha=1/2` is deliberately not asserted: the simple weighted second-moment argument is borderline there.

## 5. Continuous bridges have near-`n^-1` raw quotient size

Take `a in [log n,log(n+1)]`. Subtracting `H(log n)=0` from (21) gives

\[
e^a Q\phi_{e^{-a}}
=-e^{a/2}y(a)+\sqrt n\,y_n
+\int_{\log n}^{a}e^{u/2}y(u)\,du.
\tag{39}
\]

Write `y(u)=y_n+r(u)`, with `||r(u)||<=omega_n`. The constant part of (39) is

\[
(e^{a/2}-\sqrt n)y_n,
\tag{40}
\]

while the remaining terms are bounded by a constant times `sqrt(n) omega_n`. Using (32) and `e^-a<=1/n` gives the uniform cell estimate

\[
\boxed{
\sup_{1/(n+1)\le\theta\le1/n}
\|Q\phi_\theta\|
\ll n^{-1/2}\omega_E(\Delta_n).
}
\tag{41}
\]

Combining with (38) proves (11).

For the finite grid `theta=M/k`, put `j=floor(k/M)`. Integer ratios give `Q phi_(1/j)=0` exactly. Each noninteger ratio cell contains at most `M` grid points, so (11) yields

\[
\begin{aligned}
\frac1M
\sum_{\substack{M<k\le N\\k/M\ge R}}
\|Q\phi_{M/k}\|^2
&\ll_\alpha
\sum_{j\ge R}j^{-1-2\alpha}\\
&\ll_\alpha R^{-2\alpha},
\end{aligned}
\tag{42}
\]

uniformly in `M,N`. This is (12). Letting `alpha` approach `1/2` gives the convenient reformulation `O_epsilon(R^(-1+epsilon))` for every positive `epsilon`.

This is only a **raw column-energy** statement. A nonzero vector and an arbitrarily small rescaling have the same span. Therefore (42) cannot be converted into a bound on the enrichment target gain without a normalized-frame, principal-angle, quotient-Gram, or coefficient estimate. That conditioning boundary is exactly the live obstruction already isolated by `NB-050`--`NB-053`.

## 6. Prior-art boundary and consequence

The Hardy-space ingredients are classical. Burnol supplies the Mellin/Hardy factorization, the common Blaschke factor, and the fact that `((s-1)zeta(s))/s^2` lies in `H^2`; Titchmarsh supplies the classical critical-line second moment. Strong continuity of the shift semigroup and the fractional translation estimate are standard Hilbert/Fourier facts. None of those ingredients is claimed new.

The line-local delta is the correction and transfer: the invalid `O`-orbit argument is replaced by the exact regularized identity (5), whose reciprocal-integer endpoints force the expanding recurrence (26); backward boundedness then collapses the distinguished `E` orbit in the quotient, and the classical zeta second moment turns that collapse into the finite-grid raw-tail estimate (12). A targeted literature audit did not locate this exact regularized logarithmic-cell recurrence or its `NB-050` finite-grid consequence, but no priority claim follows from that bounded search.

The result also sharpens the method boundary. Large-ratio raw quotient mass cannot carry the weighted repair defect persistently, even after repairing the Hardy domain. What remains potentially target-bearing is the **normalized direction and conditioning** of those tiny columns, plus bounded/moderate ratio geometry or a finite-section correction that breaks the exact natural-grid endpoint relation. No estimate of `delta_def`, `Delta_*`, or `d_N` is obtained, and no RH implication follows.