# FD-043 — critical density-pole cancellation controls growing Mellin packets

**Status:** `EXACT-DERIVED + GROWING-CRITICAL-MELLIN-PACKETS + DENSITY-POLE-CANCELLATION + QUANTITATIVE-OCCUPATION + PHYSICAL-APPROXIMATION-OBSTRUCTION`.

`FD-042` proves universal nonsquarefree Jordan occupation for every fixed finite critical Mellin packet, but leaves growing packet dimension and moving frequency windows as possible escape mechanisms. Centering by the universal nonsquarefree density before estimating the Gram matrices removes the critical density pole. A further adaptive partial-summation split shows that the remaining centered Mellin kernel grows only **logarithmically** with frequency difference, not linearly.

For every fixed Schur-head cutoff `D` and every fixed `sigma in (1/2,1)`, let

\[
P(r)=\sum_{j=1}^m z_j r^{-i\gamma_j},
\qquad
\Omega:=\max_{j,k}|\gamma_j-\gamma_k|.
\]

Then, uniformly in the row horizon `R`,

\[
\boxed{
\left|
\|P\|_{\mathrm{ns},R,D}^2
-\delta_{\mathrm{ns}}\|P\|_{R,D}^2
\right|
\le
C_{D,\sigma}\,m\log(2+\Omega)\|z\|_2^2.
}
\tag{1}
\]

Here

\[
\|P\|_{R,D}^2
:=\sum_{D<r\le R}\frac{w(r)}r|P(r)|^2,
\qquad
\|P\|_{\mathrm{ns},R,D}^2
:=\sum_{\substack{D<r\le R\\\mu(r)=0}}
\frac{w(r)}r|P(r)|^2,
\]

with `w(r)=J_2(r)/r^2` and the same `delta_ns` as in `FD-038` and `FD-042`.

Consequently every moving packet family satisfying

\[
\frac{m_R\log(2+\Omega_R)\|z_R\|_2^2}
     {\|P_R\|_{R,D}^2}
\longrightarrow0
\tag{2}
\]

has

\[
\boxed{
\frac{\|P_R\|_{\mathrm{ns},R,D}^2}
     {\|P_R\|_{R,D}^2}
\longrightarrow\delta_{\mathrm{ns}}>0.
}
\tag{3}
\]

Thus a critical spectral escape cannot be attributed merely to many frequencies, close frequencies, or even a moderately widening frequency window. It requires quantitative coefficient coherence/ill-conditioning, a packet dimension too large for its realized row energy, or a macroscopic nonpacket remainder in the physical row norm.

## 1. Centering removes the critical density pole

Retain the constants from `FD-038`:

\[
a:=\frac1{\zeta(3)},
\qquad
b:=a-c_{\mathrm{sf}},
\qquad
\delta_{\mathrm{ns}}:=\frac ba.
\tag{4}
\]

That finding proves

\[
W(x):=\sum_{r\le x}w(r)=ax+O(1)
\tag{5}
\]

and, for every fixed `sigma>1/2`,

\[
W_{\mathrm{ns}}(x)
:=\sum_{\substack{r\le x\\\mu(r)=0}}w(r)
=bx+O_\sigma(x^\sigma).
\tag{6}
\]

Define the centered arithmetic weight

\[
c(r):=w(r)
\left(\mathbf 1_{\mu(r)=0}-\delta_{\mathrm{ns}}\right)
\tag{7}
\]

and its summatory function

\[
C(x):=\sum_{r\le x}c(r)
=W_{\mathrm{ns}}(x)-\delta_{\mathrm{ns}}W(x).
\tag{8}
\]

Since `delta_ns=b/a`, the linear terms cancel exactly:

\[
\boxed{
C(x)=O_\sigma(x^\sigma)
\qquad(\sigma>1/2).
}
\tag{9}
\]

Also `0<w(r)<=1` and `0<delta_ns<1`, hence

\[
|c(r)|\le1.
\tag{10}
\]

Equation (9) is the arithmetic cancellation; (10) supplies a trivial but uniform short-range estimate. Their combination is stronger than applying partial summation from the fixed lower endpoint `D` for every frequency.

## 2. Adaptive splitting gives a logarithmic frequency bound

For real `t`, set

\[
K_{R,D}(t)
:=\sum_{D<r\le R}c(r)r^{-1+it}.
\tag{11}
\]

Fix `sigma in (1/2,1)` and put

\[
T:=2+|t|,
\qquad
X:=T^{1/(1-\sigma)}.
\tag{12}
\]

If `R<=X`, the pointwise bound (10) immediately gives

\[
|K_{R,D}(t)|
\le\sum_{D<r\le R}\frac1r
\ll_D 1+\log X
\ll_{D,\sigma}\log T.
\tag{13}
\]

Suppose now that `R>X`; replacing `X` by a neighboring integer changes only an absolute endpoint term. Split

\[
K_{R,D}(t)
=
\sum_{D<r\le X}c(r)r^{-1+it}
+
\sum_{X<r\le R}c(r)r^{-1+it}.
\tag{14}
\]

The first sum is again `O_(D,sigma)(log T)`. For the tail, partial summation with (9) gives

\[
\begin{aligned}
\sum_{X<r\le R}c(r)r^{-1+it}
={}&C(R)R^{-1+it}-C(X)X^{-1+it}\\
&+(1-it)\int_X^R C(x)x^{-2+it}\,dx
+O(X^{-1}).
\end{aligned}
\tag{15}
\]

Because `sigma<1`,

\[
\begin{aligned}
\left|\sum_{X<r\le R}c(r)r^{-1+it}\right|
&\ll_\sigma
X^{\sigma-1}
+(1+|t|)\int_X^\infty x^{\sigma-2}\,dx\\
&\ll_\sigma
T X^{\sigma-1}
\ll_\sigma1,
\end{aligned}
\tag{16}
\]

where the last step uses `X^(sigma-1)=T^(-1)`. Combining (13)--(16) yields the uniform estimate

\[
\boxed{
|K_{R,D}(t)|
\le C_{D,\sigma}\log(2+|t|)
}
\tag{17}
\]

for every `R>D` and every real `t`, including `t=0`.

The important feature is still the absence of any inverse minimum-frequency-gap factor, but the dependence on a widening frequency window is now only logarithmic. The previous direct fixed-endpoint partial-summation estimate `O(1+|t|)` was valid but unnecessarily crude because it paid the derivative factor `|t|` before moving into the range where the summatory cancellation (9) compensates it.

## 3. Growing critical packets obey the sharpened occupation estimate

Define the full and nonsquarefree critical Gram matrices

\[
G_{\mathrm{all}}^{(R)}(j,k)
:=\sum_{D<r\le R}\frac{w(r)}r
r^{i(\gamma_j-\gamma_k)},
\tag{18}
\]

\[
G_{\mathrm{ns}}^{(R)}(j,k)
:=\sum_{\substack{D<r\le R\\\mu(r)=0}}
\frac{w(r)}r
r^{i(\gamma_j-\gamma_k)}.
\tag{19}
\]

By (7) and (11), every entry of

\[
\mathcal D_R
:=G_{\mathrm{ns}}^{(R)}
-\delta_{\mathrm{ns}}G_{\mathrm{all}}^{(R)}
\tag{20}
\]

is `K_(R,D)(gamma_j-gamma_k)`. Equation (17) and the elementary row-sum operator-norm bound therefore give

\[
\boxed{
\|\mathcal D_R\|_{\mathrm{op}}
\le C_{D,\sigma}m\log(2+\Omega).
}
\tag{21}
\]

For

\[
P_z(r)=\sum_{j=1}^m z_jr^{-i\gamma_j},
\tag{22}
\]

we have

\[
\|P_z\|_{R,D}^2
=z^*G_{\mathrm{all}}^{(R)}z,
\qquad
\|P_z\|_{\mathrm{ns},R,D}^2
=z^*G_{\mathrm{ns}}^{(R)}z.
\tag{23}
\]

Equations (20)--(23) prove (1). Introduce the sharpened conditioning parameter

\[
\boxed{
\chi_R(P_z)
:=
\frac{m\log(2+\Omega)\|z\|_2^2}
     {\|P_z\|_{R,D}^2}.
}
\tag{24}
\]

Then

\[
\boxed{
\frac{\|P_z\|_{\mathrm{ns},R,D}^2}
     {\|P_z\|_{R,D}^2}
=
\delta_{\mathrm{ns}}+O_{D,\sigma}(\chi_R(P_z)).
}
\tag{25}
\]

whenever the denominator is nonzero.

`FD-042` is recovered when the packet is fixed: its full norm is `(a log R+O(1))||z||_2^2`, so `chi_R=O(1/log R)`. More generally, any moving family with natural critical energy

\[
\|P_R\|_{R,D}^2
\gg (\log R)\|z_R\|_2^2
\tag{26}
\]

and

\[
\boxed{
m_R\log(2+\Omega_R)=o(\log R)}
\tag{27}
\]

still has universal occupation `delta_ns+o(1)`. For fixed packet dimension, (27) permits every subpower frequency diameter

\[
\Omega_R=R^{o(1)},
\tag{28}
\]

which is substantially wider than the regime supplied by the earlier linear-in-`Omega` estimate.

## 4. The exact physical row profile inherits the stronger obstruction

For a horizon `H`, define the exact normalized physical row profile

\[
B_H(r)
:=\sqrt{\frac rH}\,
\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right),
\qquad D<r\le H.
\tag{29}
\]

The Schur-tail definitions give the exact identities

\[
\boxed{
\|B_H\|_{H,D}^2=\frac{E_{H,D}}H,
\qquad
\|B_H\|_{\mathrm{ns},H,D}^2=\frac{U_{H,D}}H.
}
\tag{30}
\]

Suppose that along an unbounded sequence of horizons there are Mellin packets `P_H` such that

\[
\frac{\|B_H-P_H\|_{H,D}}
     {\|B_H\|_{H,D}}
\longrightarrow0
\tag{31}
\]

and, with the logarithmic conditioning parameter (24),

\[
\chi_H(P_H)\longrightarrow0.
\tag{32}
\]

The nonsquarefree norm is dominated by the full norm, so (31) also controls the numerator error and its cross terms. Equations (25), (30)--(32) imply

\[
\boxed{
\frac{U_{H,D}}{E_{H,D}}
\longrightarrow\delta_{\mathrm{ns}}>0.
}
\tag{33}
\]

Thus any physical sequence with `U_(H,D)/E_(H,D)->0` must defeat a considerably larger approximation class than recorded by the original version of this finding. It cannot admit a norm-accurate critical Mellin approximation whose realized energy dominates `m log(2+Omega)` times its coefficient mass.

The surviving alternatives remain genuinely source-specific: either every packet in this expanded well-conditioned class leaves a macroscopic remainder in the exact physical row norm, or accurate packets become increasingly coherent so that their coefficient mass is large relative to the row energy they actually realize.

## 5. Stress tests and boundary cases

The logarithmic dependence on `Omega` does **not** make frequency collisions harmless. If two frequencies nearly coincide with nearly opposite coefficients, the packet can have very small full norm while `||z||_2` stays large; then (24) is large and (25) gives no useful relative conclusion. The theorem records this loss as coefficient conditioning rather than as an inverse minimum-gap singularity.

The factor `m` also remains. The entrywise bound (17) alone cannot prevent many centered Gram entries from acting coherently, so no dimension-free operator estimate is claimed. Likewise, (1) gives no useful relative information when `m log(2+Omega)||z||_2^2` is comparable with the full critical row energy.

The result is invariant under a common translation of all Mellin frequencies because only differences occur. For one frequency, (17) reduces to a bounded centered diagonal error and reproduces the `O(1/log R)` occupation convergence of the simplest case of `FD-042`. The nontrivial zeros of `zeta` may still generate infinitely many comparable modes, a critical-size remainder, or coefficient coherence outside every packet class covered by (24).

A direct finite audit is available: for chosen `R,D,Gamma,z`, evaluate the two weighted row norms and the centered quadratic form in (1). A failure of every constant in the bound `C_(D,sigma)m log(2+Omega)||z||_2^2` as `R` varies would contradict the split partial-summation derivation from (9)--(10).

## 6. Prior-art boundary and consequence for the research line

Abel/partial summation, nonharmonic Fourier systems, Dirichlet-polynomial Gram matrices, and elementary operator-norm estimates are classical. A targeted literature search found the expected general analytic-number-theory and Fourier-frame machinery but no external theorem is load-bearing for (17): the logarithmic frequency-span estimate follows directly by combining the already-persisted centered summatory law (9), the elementary pointwise bound (10), and the adaptive split (12). No broad novelty claim is made for that analytic maneuver.

The Mathia-specific content is the centered Jordan weight (7), cancellation of its density pole, the quantitative occupation estimate (1), and the exact physical-row reduction (29)--(33). The strengthened comparison narrows the frontier left by `FD-042`: a critical spectral escape must exhibit **macroscopic nonpacket remainder, dimension growth, or genuine coefficient coherence/ill-conditioning** even after subpower frequency-window growth is allowed at fixed dimension.

This still does not prove a fixed positive `U_(H,D)/E_(H,D)` for the actual Mertens-derived source, so the accepted joint-occupation clue remains open. The next source-specific target is to use the exact increment law

\[
\Delta\mathcal H(n)
=\frac{\mu(\operatorname{rad}n)\varphi(\operatorname{rad}n)}n
\]

or the Dirichlet series `zeta(s+1)/zeta(s)` to rule out one of the two remaining physical alternatives: persistent critical-norm approximation failure or increasingly ill-conditioned Mellin representations.