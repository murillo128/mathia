# NB-018 — periodic shell mean governs fixed-section deep-dilation visibility

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + FIXED-SECTION-DEEP-DILATION-ASYMPTOTIC + SOURCE-VISIBILITY-LIMIT + PERIODIC-MIXING + NEGATIVE/DIAGONAL-SCALE-BOUNDARY`. `NB-017` identifies the all-depth compressed enrichment channel as a rooted multiplicative graph and shows that its exact blind future-pairing profiles are componentwise reciprocal. For the **actual** finite Nyman residual, the opposite extreme `M -> infinity` with the section `N` held fixed can be solved exactly. The residual has a finite-period harmonic-shell sequence, so sufficiently deep dilation averages that sequence to one scalar: its arithmetic shell mean.

Let

\[
V_N=\operatorname{span}\{g_2,\ldots,g_N\},\qquad
r_N=e-P_Ne,\qquad d_N=\|r_N\|,
\tag{1}
\]

in Bagchi's canonical real-space model, and let `r_(N,n)` be the value of `r_N` on

\[
I_n=\left(\frac1{n+1},\frac1n\right].
\]

Put

\[
\Lambda_N:=\operatorname{lcm}(2,3,\ldots,N),
\qquad
\mu_N:=\frac1{\Lambda_N}
\sum_{a=1}^{\Lambda_N}r_{N,a}.
\tag{2}
\]

Then for fixed `N>=2`, as `m -> infinity`,

\[
\boxed{
\sqrt m\,A_m^*r_N\longrightarrow \mu_N e
\quad\text{strongly in }\mathcal M.
}
\tag{3}
\]

More explicitly,

\[
\boxed{
\left\|\sqrt m\,A_m^*r_N-\mu_Ne\right\|
\le
\frac{2\Lambda_N}{m}
\|r_N-\mu_Ne\|_{\infty}.
}
\tag{4}
\]

Thus the deep compressed adjoint forgets all fixed-section shell information except the arithmetic mean. This gives exact asymptotics for both the full semigroup defect and the part visible to actual section enrichment. With

\[
D_m=A_m^*-m^{-1/2}I,
\]

one has

\[
\boxed{
\|D_mr_N\|^2
=
\frac{A_N}{m}+O_N(m^{-2}),
}
\qquad
A_N:=\|r_N-\mu_Ne\|^2,
\tag{5}
\]

and, because `P_Nr_N=0`,

\[
\boxed{
\|P_ND_mr_N\|^2
=
\frac{\mu_N^2(1-d_N^2)}{m}+O_N(m^{-2}).
}
\tag{6}
\]

The coefficient in (5) has the orthogonal decomposition

\[
\boxed{
A_N
=
\mu_N^2(1-d_N^2)
+d_N^2(1-\mu_N)^2
>0.
}
\tag{7}
\]

Consequently the `NB-014`--`NB-015` observables satisfy

\[
\boxed{
\mathcal E_M(r_N)
=A_N\log M+O_N(1),
}
\tag{8}
\]

\[
\boxed{
\mathcal J_{N,M}
=\mu_N^2(1-d_N^2)\log M+O_N(1),
}
\tag{9}
\]

and hence

\[
\boxed{
\rho_{N,M}
\longrightarrow
R_N:=
\frac{\mu_N^2(1-d_N^2)}
{\mu_N^2(1-d_N^2)+d_N^2(1-\mu_N)^2}.
}
\tag{10}
\]

In particular, the fixed-section visible defect has an exact dichotomy:

\[
\boxed{
\sum_{m=2}^{\infty}\|P_ND_mr_N\|^2<\infty
\iff \mu_N=0.
}
\tag{11}
\]

If `mu_N=0`, the deep defect becomes asymptotically invisible to the old section. If `mu_N != 0`, a positive fraction `R_N` of the harmonic-order defect is visible, but the compressed frame cost must itself grow at least logarithmically. Indeed `NB-015` gives

\[
\mathcal J_{N,M}
\le
\beta_{N,M}(d_N^2-d_{MN}^2),
\]

so (9) implies

\[
\boxed{
\liminf_{M\to\infty}
\frac{\beta_{N,M}}{\log M}
\ge
\frac{\mu_N^2(1-d_N^2)}{d_N^2}
\quad(\mu_N\ne0).
}
\tag{12}
\]

This is a fixed-section control result, not an RH-facing visibility bound. The convergence in (4) explicitly pays the period `Lambda_N`, whose logarithm is `psi(N)=N+o(N)`. The mechanism therefore becomes transparent only at dilation depths that resolve an exponentially large shell period, whereas the defect lower bound used in the `NB-015` diagonal budget assumes roughly `M<=N^2`. The new result identifies the scalar that governs the very-deep limit, but it does **not** supply a uniform estimate for `mu_N`, a useful pre-period mixing theorem, or the scale-coupled lower bound still required by the live research line.

## 1. Finite Nyman residuals are periodic and have a canonical shell mean

Bagchi's sequence realization gives

\[
g_j|_{I_n}=\left\{\frac nj\right\}.
\tag{13}
\]

Hence `g_j` has period `j` in the harmonic-shell index. Since `P_Ne` is a finite linear combination of `g_2,...,g_N`, both `P_Ne` and `r_N=e-P_Ne` are `Lambda_N`-periodic in that index. This is the same elementary periodicity used in `NB-008`, but here it is applied to deep semigroup compression rather than to the common-zero lcm shell.

The scalar in (2) is also the limiting normalized tail average from `NB-007`--`NB-010`. For a shell-periodic `h`, set

\[
c_n(h)=n\int_0^{1/n}h(x)\,dx
=n\sum_{\ell\ge n}
\frac{h_\ell}{\ell(\ell+1)}.
\tag{14}
\]

If `h_l=mu+u_l` with `u` periodic of period `P` and arithmetic mean zero, every consecutive partial sum of `u` has modulus at most `P||u||_infinity`. Summation by parts against the decreasing weights `n/(ell(ell+1))` gives

\[
|c_n(h)-\mu|
\le
\frac{P\|u\|_\infty}{n+1}.
\tag{15}
\]

Therefore

\[
\boxed{
\mu_N=\lim_{n\to\infty}c_n(r_N).
}
\tag{16}
\]

No positivity or nonvanishing of `mu_N` is asserted. It is an actual source-selected scalar of the finite best residual, and either sign or zero is a priori allowed by the argument.

## 2. Deep dilation is a weighted period average on every harmonic shell

Let `P_mathcalM` denote orthogonal projection onto Bagchi's harmonic-shell space `mathcal M`. `NB-004` reconstructs the load-bearing compression identity

\[
A_m^*=P_{\mathcal M}T_m^*|_{\mathcal M},
\qquad
(T_m^*h)(y)=m^{-1/2}h(y/m).
\tag{17}
\]

Define

\[
Q_mh:=\sqrt m\,A_m^*h
=P_{\mathcal M}[h(\,\cdot\,/m)].
\tag{18}
\]

For `y in I_n`, the projection is the average over that shell. After the substitution `x=y/m`, the interval is exactly a union of `m` consecutive harmonic shells:

\[
\left(\frac1{m(n+1)},\frac1{mn}\right]
=
\bigcup_{\ell=mn}^{m(n+1)-1}I_\ell.
\]

Therefore

\[
\boxed{
(Q_mh)|_{I_n}
=
mn(n+1)
\sum_{\ell=mn}^{m(n+1)-1}
\frac{h_\ell}{\ell(\ell+1)}.
}
\tag{19}
\]

The coefficients

\[
\omega_\ell
:=
\frac{mn(n+1)}{\ell(\ell+1)}
\qquad(mn\le\ell<m(n+1))
\tag{20}
\]

are positive, decreasing, and sum to one. If `u` has period `P` and zero mean, write the weighted sum in (19) by Abel summation from the left endpoint. Consecutive partial sums of `u` are bounded by `P||u||_infinity`, while

\[
\omega_{mn}
=\frac{n+1}{mn+1}
\le\frac2m.
\tag{21}
\]

Hence uniformly in the shell index `n`,

\[
|(Q_mu)|_{I_n}|
\le
\frac{2P\|u\|_\infty}{m}.
\tag{22}
\]

Since the harmonic shells partition `(0,1]`, the same uniform estimate is an `L^2` estimate. Taking `h=r_N`, `P=Lambda_N`, and `u=r_N-mu_Ne` proves (4), and therefore (3).

This step must use the compressed adjoint in (17). Replacing `A_m^*` by the full-space adjoint without `P_mathcalM` would preserve the rapidly oscillating function `r_N(y/m)` and would not give the strong mixing statement (3). This is exactly the invariant-versus-reducing distinction that forced the withdrawal of the earlier `NB-003` claim.

## 3. The shell mean splits deep defect into visible and invisible orthogonal pieces

Equation (18) rewrites the semigroup defect as

\[
\sqrt m\,D_mr_N
=Q_mr_N-r_N.
\tag{23}
\]

By (4),

\[
Q_mr_N-r_N
=\mu_Ne-r_N+O_{L^2,N}(m^{-1}).
\tag{24}
\]

Squaring and dividing by `m` proves (5). The residual projection identity

\[
e=P_Ne+r_N,
\qquad P_Ne\perp r_N,
\tag{25}
\]

then gives

\[
\mu_Ne-r_N
=\mu_NP_Ne+(\mu_N-1)r_N,
\]

with orthogonal summands. Since

\[
\|P_Ne\|^2=1-d_N^2,
\]

this proves (7).

Project (23) back onto the old section. Since `P_Nr_N=0`,

\[
\sqrt m\,P_ND_mr_N
=P_NQ_mr_N
=\mu_NP_Ne+O_{L^2,N}(m^{-1}),
\tag{26}
\]

which proves (6). Summing (5)--(6) over `m` uses only

\[
\sum_{m\le M}\frac1m=\log M+O(1),
\qquad
\sum_{m\ge2}\frac1{m^2}<\infty,
\]

and yields (8)--(10). If `mu_N=0`, (26) is actually `O_N(m^{-1})` before the outer factor `m^{-1/2}`, so the squared visible defect is `O_N(m^{-3})` and its full sum converges. If `mu_N!=0`, (6) has a positive harmonic leading coefficient because `0<d_N<1`; this proves (11).

## 4. Relation to the reciprocal blind modes of `NB-017`

The same limit can be read directly in the future residual field used by `NB-017`. Put

\[
q_k=\langle r_N,g_k\rangle,
\qquad
s_k=kq_k.
\tag{27}
\]

For fixed `2<=j<=N`, the exact dilation identity gives

\[
\langle Q_mr_N,g_j\rangle
=
\frac{s_{mj}-s_m}{j}.
\tag{28}
\]

The real-space target pairing is

\[
\langle e,g_j\rangle=\frac{\log j}{j}.
\tag{29}
\]

Combining (3)--(4) with (28)--(29),

\[
\boxed{
s_{mj}-s_m
=\mu_N\log j+O_N(m^{-1})
\qquad(j\text{ fixed}).
}
\tag{30}
\]

Thus the fixed-section source field has a sharp deep-edge alternative. When `mu_N=0`, its increments along every fixed old-index multiplication edge tend to zero, so it asymptotically shadows the componentwise-constant `s` fields corresponding to `NB-017`'s reciprocal blind profiles `q_k=a_C/k`. When `mu_N!=0`, it cannot become constant: the limiting edge increment is the logarithmic cocycle `mu_N log j`.

Equation (30) is not a claim that rough-core components are completely classified by their core, nor that the actual residual realizes an exact blind profile. `NB-017` proves only that rough core is a component invariant and characterizes exact blindness by constancy on the actual graph components. The present statement concerns fixed old multipliers at deep channel source `m` and is compatible with that finer component geometry.

## 5. Scale boundary and consequence for the live visibility problem

The fixed-section limit resolves one natural ambiguity left by `NB-017`: increasing the probe depth indefinitely does not produce arbitrary source behavior. Deep compression averages the periodic residual to `mu_Ne`, and the entire asymptotic visible fraction is the explicit scalar expression (10).

But this does not solve the `NB-015` scale-coupled problem. The quantitative mixing estimate (4) carries the full period `Lambda_N`. By the prime number theorem,

\[
\log\Lambda_N=\psi(N)=N+o(N),
\tag{31}
\]

so the elementary period-averaging mechanism only becomes uniform after probing scales comparable with an exponentially large arithmetic period. In contrast, the prime-normal-equation lower bound feeding the `NB-015` budget is available in the diagonal chamber `sqrt(M) lesssim N`, i.e. roughly `M<=N^2`. Holding `N` fixed and sending `M` to infinity eventually leaves that chamber entirely.

There is also no free gain from superdeep probing even when `mu_N!=0`. The section decrement `d_N^2-d_(MN)^2` is bounded by `d_N^2`, while (9) grows like `log M`; the exact transport inequality therefore forces the compressed frame cost to grow at least as in (12). The deep limit either loses visible defect (`mu_N=0`) or pays increasing overlap cost (`mu_N!=0`). This is a method boundary, not a proof that every diagonal source-visible estimate must fail.

The live theorem remains the one isolated by `NB-015`--`NB-017`: obtain information **before** full-period averaging, with `N` and `M` growing together, that forces the actual future field away from approximate reciprocal blindness strongly enough relative to `beta_(N,M)` to violate the summable visibility budget. `mu_N` is now an exact endpoint diagnostic for that problem, not a substitute for the missing diagonal estimate.

## 6. Prior-art boundary and falsification controls

Bagchi's 2006 formulation is the primary literature input. It identifies the canonical weighted sequence model and explicitly emphasizes approximation by periodic sequences; the shell formula (13) and the compressed dilation framework are already anchored in this line. `NB-008` uses the same finite-period structure at the lcm common-zero shell. The new derivation here is the elementary weighted-period averaging of the compressed adjoint and its consequences for the `NB-014`--`NB-017` visibility observables.

A targeted prior-art check covered Bagchi's semigroup/periodic-sequence formulation, Báez-Duarte's discrete criterion, finite-section numerical work, Ehm's 2024 Gram-matrix decompositions and associated fractional-part series, recent multiscale Nyman Gram work, and searches for residual-pairing/deep-dilation asymptotics. No located source stated the fixed-section limits (3), (8)--(10), or the visible-defect dichotomy (11). Search absence is not a novelty proof. No specialized external theorem is load-bearing beyond the already anchored Bagchi model and the standard `log lcm(1,...,N)=psi(N)=N+o(N)` scale boundary, so `SOURCES.md` does not change.

The result is falsified by any periodic shell vector for which (19) fails, any violation of the Abel bound (22), or any actual residual for which the asymptotic coefficients in (5)--(6) disagree with direct finite-section projection. Several boundaries are essential: `N` is fixed in every limit; `mu_N` is not known to be nonzero or bounded away from zero; constants hidden in `O_N` are not uniform in `N`; and neither a positive fixed-section limit `R_N` nor logarithmic growth of `mathcal J_(N,M)` yields a new approximation rate or RH without a scale-coupled control of the frame cost and section growth.