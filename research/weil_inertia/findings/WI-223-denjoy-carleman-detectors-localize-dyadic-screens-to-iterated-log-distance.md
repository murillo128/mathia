# WI-223 — Denjoy--Carleman detectors localize dyadic screens to iterated-log distance

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + STRUCTURAL-RIGIDITY + PRIOR-ART-REDIRECT + DECISIVE-NEGATIVE`.

WI-222 uses a fixed compact Gevrey detector of order `s>1` and forces any dyadic zeta-zero screen that cancels the fixed-band bow to return order-`M` radial-weighted source to physical ordinate radius

\[
O_\varepsilon\!\left(M(\log T)^\varepsilon\right).
\]

That finding explicitly leaves open whether non-Gevrey Denjoy--Carleman / Beurling--Malliavin style cutoffs can get closer to exponential Fourier decay. They can, and the gain is substantial. For every fixed integer `r>=1` and every fixed `epsilon>0`, one can choose a **fixed compact detector** for which the same dyadic-screen argument localizes order-`M` radial-weighted source to

\[
\boxed{
|\gamma-\gamma_0|
\ll_{r,\varepsilon,k,d}
M\,D_{r,\varepsilon}(\log T),
}
\tag{1}
\]

where, for large `x`,

\[
D_{r,\varepsilon}(x)
:=
\prod_{j=1}^{r-1}\log_j x\;
(\log_r x)^{1+\varepsilon},
\qquad
\log_1x=\log x,
\quad
\log_{j+1}x=\log(\log_jx).
\tag{2}
\]

Equivalently,

\[
D_{r,\varepsilon}(\log T)
=
\left(\prod_{j=2}^{r}\log_jT\right)
(\log_{r+1}T)^{1+\varepsilon}.
\tag{3}
\]

For `r=1`, this is already

\[
\boxed{
|\gamma-\gamma_0|
\ll_\varepsilon
M(\log\log T)^{1+\varepsilon},
}
\tag{4}
\]

which is asymptotically much smaller than the `M(log T)^epsilon` radius of WI-222 for every fixed positive `epsilon`. Taking any fixed larger `r` replaces that loss by a deeper iterated-log hierarchy.

There is also a sharp architectural warning. The classical Ingham uncertainty theorem says that a nonzero compactly supported function can have a uniform Fourier envelope

\[
|\widehat\phi(\xi)|
\le C\exp[-|\xi|\Theta(|\xi|)]
\tag{5}
\]

for a decreasing `Theta->0` exactly in the non-quasianalytic regime

\[
\int_1^\infty \frac{\Theta(t)}t\,dt<\infty.
\tag{6}
\]

In particular a fixed nonzero compact detector cannot have genuine exponential Fourier decay. Therefore the **fixed-detector + total radial-mass tail estimate** used in WI-221--WI-223 cannot uniformly reach physical radius `O(M)`: that would require natural-frequency cutoff `R=O(log T)` and hence exponential suppression strong enough to beat `N_T/M=T^{1-vartheta+o(1)}`. It therefore cannot reach the much smaller original bow scale `M/log T` either. This does not rule out `T`-dependent detectors, multiple coupled observables, or a source-specific covariance theorem; it closes only the fixed compact-detector tail-suppression architecture.

## 1. Exact inherited screen model

Use exactly the WI-218--WI-222 normalization. At one fixed interior reciprocal harmonic

\[
0<k<d,
\tag{7}
\]

let

\[
M=T^{\vartheta+o(1)},
\qquad \vartheta>0,
\qquad
\eta_M=\frac{\log T}{2dM}=o(1),
\tag{8}
\]

and

\[
F_M:=K_{\eta_M}f_{M,k},
\qquad
F:=K_0(C_k\operatorname{sinc}),
\qquad
(K_\eta r)(u)=\int_0^1e^{\eta v}r(u+v)\,dv.
\tag{9}
\]

WI-218 gives compact convergence `F_M->F`, and `F` is not identically zero. Assume the same **dyadic-zero-screen hypothesis** as WI-221--WI-222: a finite screen assembled from functional-equation mirror pairs with `T<gamma<=2T` satisfies, on one fixed compact interval `J`,

\[
\left\|F_M+K_{\eta_M}g_M\right\|_{L^2(J)}=o(1).
\tag{10}
\]

For one mirror pair with normalized radial parameter `a>=0`, unfolded phase frequency `nu`, and multiplicity `mu`, the exact rescaled contribution is the sum of two exponential channels with

\[
|c_+|=\frac{\mu e^{ak}}M,
\qquad
|c_-|=\frac{\mu e^{-ak}}M,
\qquad
|\alpha_\pm|=\frac aM,
\qquad
|\xi_\pm|=\frac{|\nu|}M.
\tag{11}
\]

For a zeta zero in the critical strip,

\[
a
\le \frac{\log T+O(1)}{2d},
\tag{12}
\]

so `a/M=o(1)` uniformly over the dyadic population. The real tilts in (11) are therefore eventually bounded by `1`.

The other inherited input is Jutila's published near-line zero-density theorem in the form already audited in WI-029/WI-221/WI-222:

\[
\boxed{
\sum_{T<\gamma\le2T}
\mu_\rho\cosh(k a_\rho)
\ll_{k,d}N_T,
}
\qquad
N_T:=N(2T)-N(T)\asymp T\log T.
\tag{13}
\]

No stronger zero-density estimate is used below.

## 2. A non-quasianalytic compact bump with iterated-log derivative growth

Fix `r>=1` and `epsilon>0`. For sufficiently large integers `j`, put

\[
b_j
:=
\frac{1}{jD_{r,\varepsilon}(j)}.
\tag{14}
\]

The repeated logarithmic integral test gives

\[
\boxed{
\sum_j b_j<\infty,
}
\tag{15}
\]

because the last iterated logarithm in (2) has exponent `1+epsilon`. Altering finitely many initial terms has no effect on what follows.

Choose a fixed subinterval `J_0 compactly contained in J` on which the real continuous function `F` has constant nonzero sign. Scale the positive sequence `(b_j)` by a sufficiently small fixed constant so that

\[
\sum_j b_j<|J_0|.
\tag{16}
\]

Let

\[
h_j(u):=b_j^{-1}{\bf 1}_{[0,b_j]}(u)
\tag{17}
\]

and form the classical infinite convolution

\[
\phi_0=h_1*h_2*h_3*\cdots.
\tag{18}
\]

This is the standard infinite-convolution construction behind non-quasianalytic Denjoy--Carleman bump functions. It gives a nonnegative `C_c^infty` probability density supported on an interval of length `sum b_j`. After translation, take its support inside `J_0` and call the resulting function `phi`.

For completeness, the derivative estimate needed here follows directly from the construction. Splitting after the first `n` boxes and using

\[
D h_j
=
\frac1{b_j}(\delta_0-\delta_{b_j})
\tag{19}
\]

in the distributional sense gives

\[
\|\phi^{(n)}\|_\infty
\le
\frac{2^n}{b_1b_2\cdots b_nb_{n+1}}.
\tag{20}
\]

Monotonicity of the iterated logarithms and `n!<=n^n` therefore imply constants `C,B>0`, depending only on the fixed detector parameters, such that

\[
\boxed{
\|\phi^{(n)}\|_1
\le
CB^n\bigl[nD_{r,\varepsilon}(n)\bigr]^n
}
\tag{21}
\]

for every `n>=1`, after enlarging `B` to absorb finitely many initial terms and the harmless extra factor from `b_{n+1}^{-1}`.

This is exactly the Denjoy--Carleman scale expected from (15): the reciprocal derivative quotient has the summable asymptotic size

\[
\frac{1}{nD_{r,\varepsilon}(n)}.
\tag{22}
\]

No zeta input enters this construction.

## 3. The same bump has near-exponential Fourier--Laplace decay uniformly in the radial tilt

Because `phi` has fixed compact support, for every real `|alpha|<=1`, Leibniz applied to (21) gives new constants `C_1,B_1` with

\[
\left\|
\frac{d^n}{du^n}
\left(\phi(u)e^{\alpha u}\right)
\right\|_1
\le
C_1B_1^n
\bigl[nD_{r,\varepsilon}(n)\bigr]^n.
\tag{23}
\]

Indeed, for `j<=n`, the quantity `jD(j)` is eventually increasing, and the binomial sum contributes only another fixed exponential factor in `n`.

Integrating by parts `n` times gives

\[
\left|
\int_J\phi(u)e^{(\alpha+2\pi i\xi)u}\,du
\right|
\le
C_1
\left(
\frac{B_1nD_{r,\varepsilon}(n)}{2\pi|\xi|}
\right)^n.
\tag{24}
\]

For large `|xi|`, choose

\[
n
=
\left\lfloor
c_0\frac{|\xi|}{D_{r,\varepsilon}(|\xi|)}
\right\rfloor
\tag{25}
\]

with fixed `c_0>0` small enough. Since `n<=|xi|` and `D(n)<=D(|xi|)` for large arguments, the parenthesis in (24) is at most a fixed number below one. Hence

\[
\boxed{
\sup_{|\alpha|\le1}
\left|
\int_J\phi(u)e^{(\alpha+2\pi i\xi)u}\,du
\right|
\le
C_2\exp\!\left[
-c_2\frac{|\xi|}{D_{r,\varepsilon}(|\xi|)}
\right].
}
\tag{26}
\]

The Gallagher box does not change this rate. For

\[
q_\eta(z):=\int_0^1e^{(\eta+z)v}\,dv,
\tag{27}
\]

one has `K_eta(e^{z dot})=q_eta(z)e^{z dot}` and

\[
|q_\eta(z)|\le e^2
\tag{28}
\]

when `|eta|<=1` and `|Re z|<=1`. Therefore

\[
\boxed{
\sup_{|\alpha|\le1}
\left|
\int_J\phi(u)
K_\eta(e^{(\alpha+2\pi i\xi)\cdot})(u)
\,du
\right|
\le
C_3\exp\!\left[
-c_2\frac{|\xi|}{D_{r,\varepsilon}(|\xi|)}
\right].
}
\tag{29}
\]

Equation (29) is the iterated-log replacement for WI-222's Gevrey estimate `exp(-c|xi|^(1/s))`.

## 4. The far dyadic source dies at `R = log T times iterated logs`

Because `phi>=0` is supported where `F` has fixed nonzero sign,

\[
A:=\left|\int_J\phi(u)F(u)\,du\right|>0.
\tag{30}
\]

Compact convergence `F_M->F` and the cancellation hypothesis (10) imply

\[
\boxed{
\left|\int_J\phi K_{\eta_M}g_M\right|
=A+o(1).
}
\tag{31}
\]

Now split the dyadic screen at natural frequency `R`:

\[
\frac{|\nu_\rho|}{M}<R
\qquad\text{or}\qquad
\frac{|\nu_\rho|}{M}\ge R.
\tag{32}
\]

Using the exact pair coefficients (11), the uniform tilted estimate (29), and then (13), the complete far part contributes at most

\[
\begin{aligned}
\left|
\int_J\phi K_{\eta_M}g_{\rm far}
\right|
&\ll
\frac1M
\exp\!\left[-c_2\frac{R}{D_{r,\varepsilon}(R)}\right]
\sum_{T<\gamma\le2T}
\mu_\rho\cosh(k a_\rho)\\
&\ll_{k,d}
\frac{N_T}{M}
\exp\!\left[-c_2\frac{R}{D_{r,\varepsilon}(R)}\right].
\end{aligned}
\tag{33}
\]

Put `L=log T` and choose

\[
R_T
:=
A_{r,\varepsilon}L D_{r,\varepsilon}(L).
\tag{34}
\]

For fixed `r,epsilon`, elementary iterated-log asymptotics give

\[
D_{r,\varepsilon}(R_T)
=(1+o(1))D_{r,\varepsilon}(L).
\tag{35}
\]

Thus

\[
\frac{R_T}{D_{r,\varepsilon}(R_T)}
=(A_{r,\varepsilon}+o(1))L.
\tag{36}
\]

Since

\[
\frac{N_T}{M}
=T^{1-\vartheta+o(1)},
\tag{37}
\]

choosing the fixed constant `A_{r,epsilon}` sufficiently large makes (33) `o(1)`.

Subtracting this far contribution from (31), the near part has detector magnitude bounded below by a fixed positive constant. The trivial bounded-frequency version of (29), together with (11), then gives

\[
\boxed{
\sum_{\substack{T<\gamma\le2T\\
|\nu_\rho|<M R_T}}
\mu_\rho\cosh(k a_\rho)
\gg_{r,\varepsilon,k,d} M.
}
\tag{38}
\]

This is the exact weighted source-localization statement.

## 5. Conversion to physical ordinate distance

The source dictionary from WI-214--WI-222 is

\[
\nu_\rho
=
\frac{(\gamma-\gamma_0)\log T}{2\pi d}.
\tag{39}
\]

Combining (34), (38), and (39) yields

\[
\boxed{
\sum_{\substack{T<\gamma\le2T\\
|\gamma-\gamma_0|
<C_{r,\varepsilon,k,d}
M D_{r,\varepsilon}(\log T)}}
\mu_\rho\cosh(k a_\rho)
\gg_{r,\varepsilon,k,d}M.
}
\tag{40}
\]

For `r=1`,

\[
D_{1,\varepsilon}(\log T)
=(\log\log T)^{1+\varepsilon},
\tag{41}
\]

while `r=2` gives

\[
D_{2,\varepsilon}(\log T)
=(\log\log T)
(\log\log\log T)^{1+\varepsilon},
\tag{42}
\]

and so on. Each fixed deeper level eventually improves the preceding one.

The original bow itself has physical ordinate width of order

\[
\frac{M}{\log T}.
\tag{43}
\]

Thus (40) is still many bow widths away: its radius is

\[
O\!\left(
\log T\,D_{r,\varepsilon}(\log T)
\right)
\tag{44}
\]

natural bow widths. The gain over WI-222 is a source-transport gain, not yet a local-count contradiction.

## 6. Ingham identifies the fixed-detector uncertainty barrier

The relevant classical theorem is A. E. Ingham, **A Note on Fourier Transforms**, *Journal of the London Mathematical Society* s1-9:1 (1934), 29--32, DOI `10.1112/jlms/s1-9.1.29`. In a standard modern formulation, if `Theta:[0,infinity)->[0,infinity)` decreases to zero, there exists a nonzero compactly supported continuous `f` with

\[
|\widehat f(\xi)|
\le C e^{-|\xi|\Theta(|\xi|)}
\tag{45}
\]

if and only if

\[
\boxed{
\int_1^\infty \frac{\Theta(t)}t\,dt<\infty.
}
\tag{46}
\]

Bagchi--Ganguly--Sarkar--Thangavelu, **An analogue of Ingham's theorem on the Heisenberg group**, *Mathematische Annalen* (2022), DOI `10.1007/s00208-022-02479-5`, prints this real-line theorem explicitly as its Theorem 1.1 before proving the group analogue. The Denjoy--Carleman non-quasianalytic criterion is the derivative-side version of the same boundary; a modern statement is Theorem 3.5 of Fürdös--Schindl, **Ellipticity and the problem of iterates in Denjoy--Carleman classes**, *Collectanea Mathematica* 77 (2026), 23--49, DOI `10.1007/s13348-024-00455-7`.

Our explicit hierarchy corresponds to

\[
\Theta(t)
\asymp
\frac{1}{D_{r,\varepsilon}(t)},
\tag{47}
\]

and (46) is precisely the convergence already used in (15).

The theorem also shows why simply taking the limit `epsilon->0` or asking for a true exponential envelope is illegal. If a fixed compactly supported nonzero detector had

\[
|\widehat\phi(\xi)|
\ll e^{-c|\xi|}
\tag{48}
\]

for some `c>0`, then (45) would hold with `Theta>=c` eventually, contradicting (46). This is also the elementary Paley--Wiener analytic-continuation obstruction.

Now consider what the WI-221--WI-223 far-tail ledger would need in order to localize to **physical radius `O(M)`**. By (39), that radius corresponds to

\[
R_T=O(\log T)
\tag{49}
\]

in natural frequency. The available total radial-weighted source budget is `N_T/M=T^(1-vartheta+o(1))`. Uniformly suppressing an arbitrary far source with only this `ell^1` budget therefore requires the detector envelope at `R_T` to be

\[
\exp[-(1-\vartheta+o(1))\log T],
\tag{50}
\]

which, because `R_T=O(log T)`, is genuine exponential decay in the frequency cutoff. A fixed nonzero compact detector cannot supply it.

Hence

\[
\boxed{
\begin{array}{c}
\text{fixed compact detector}
+\text{ total dyadic radial-mass budget}
\\[2mm]
\not\Rightarrow
\text{uniform physical localization }O(M).
\end{array}
}
\tag{51}
\]

Since the actual bow width is `M/log T`, (51) leaves at least a full logarithmic-scale transport problem before local Riemann--von Mangoldt count can even become dimensionally competitive.

The quantifier `fixed compact detector` is essential. Ingham does not rule out a detector depending on `T`, a family of coupled detectors whose norms are jointly controlled, a signed source covariance estimate, or an argument exploiting the discrete zeta frequency set rather than a uniform tail supremum.

## 7. Why this is stronger than merely choosing a smaller Gevrey exponent

WI-222 uses a derivative class

\[
\|\phi^{(n)}\|
\ll B^n(n!)^s,
\qquad s>1,
\tag{52}
\]

and obtains

\[
|\widehat\phi(\xi)|
\ll e^{-c|\xi|^{1/s}}.
\tag{53}
\]

No fixed `s>1` gives (26). For example, the `r=1` denominator `D=(log |xi|)^(1+epsilon)` satisfies

\[
\frac{|\xi|}{(\log|\xi|)^{1+\varepsilon}}
\gg_s |\xi|^{1/s}
\tag{54}
\]

for every fixed `s>1`. Thus the resulting physical cutoff `M(log log T)^(1+epsilon)` is not obtainable by merely optimizing the constant or choosing another fixed Gevrey order in WI-222.

Conversely, the Ingham criterion shows that the improvement is not an unlimited free lunch. Each fixed compact detector must remain on the non-quasianalytic side of the Fourier-decay boundary. The iterated-log hierarchy approaches that boundary while retaining compact support and uniform bounded-tilt control.

## 8. The local-count mismatch survives

Equation (40) still asks only for order-`M` **radial-weighted** source. A physical interval of radius

\[
H=M D_{r,\varepsilon}(\log T)
\tag{55}
\]

has the crude local Riemann--von Mangoldt population scale

\[
O(H\log T)
=
O\!\left(
M\log T\,D_{r,\varepsilon}(\log T)
\right),
\tag{56}
\]

which is much larger than `M`. In addition, deeper off-line pairs can carry larger `cosh(ka)` weight. Therefore (40), by itself, still does not contradict zero-count admissibility and does not exclude an off-line zero.

This clarifies the frontier rather than solving it. The transport component of WI-222 can be pushed from a fixed power of `log T` down through arbitrarily deep fixed iterated-log hierarchies. But the same fixed-detector architecture cannot cross even the physical `O(M)` scale, whereas the source-count scale ultimately wanted by the bow is `M/log T`.

## 9. Prior-art and novelty audit

**Classical literature.** Ingham's 1934 theorem is the exact Fourier uncertainty boundary for compact support and near-exponential decay. Denjoy--Carleman theory supplies the equivalent non-quasianalytic derivative criterion and compact bump construction. The infinite-convolution proof used in Section 2 is classical. No novelty is claimed for any of those facts. WI-222 already anticipated that Beurling--Malliavin / Denjoy--Carleman type multipliers could improve its fixed-Gevrey rate, but deliberately did not audit or use them.

**Repository delta.** The new deduction is the explicit coupling of a non-quasianalytic derivative hierarchy to the already audited WI-218--WI-222 post-box source dictionary and Jutila radial budget. It yields the quantitative localization (38)--(40) and the fixed-detector no-go (51). This materially sharpens WI-222's source-transport radius while also showing that detector smoothness alone cannot close the remaining local-count gap.

A bounded structural search found the classical Ingham/Denjoy--Carleman theory and modern uncertainty-principle restatements, but no source tying this iterated-log compact-detector hierarchy to the Montgomery/Weil bow normalization, functional-equation pair coefficients, and Jutila dyadic radial moment used here. Absence of such a hit is not a priority claim.

## 10. Falsification hooks and research consequence

The finding fails if any of the following occurs:

1. the infinite-convolution bump from (14)--(18) does not satisfy the derivative bound (21);
2. multiplication by a bounded real exponential tilt loses more than a fixed exponential factor in the derivative ledger (23);
3. optimizing the integration-by-parts order does not produce (26);
4. the iterated-log comparison (35) fails for fixed `r,epsilon`;
5. the WI-222 source dictionary (11) or ordinate conversion (39) is mis-normalized;
6. Jutila's audited moment (13) is used at the excluded endpoint `k/d=1` rather than an interior harmonic;
7. Ingham's theorem is invoked without the fixed compact-support / uniform-tail-envelope hypotheses needed for the barrier (51).

Items 1--4 are explicit elementary estimates above; items 5--6 are inherited unchanged from WI-221--WI-222; item 7 is stated as a boundary rather than silently generalized.

The research consequence is two-sided. **Do not spend further cycles only optimizing a fixed Gevrey exponent:** compact non-quasianalytic detectors give much better source transport. But **do not expect a fixed compact detector plus the global radial `ell^1` budget to reach the source-count scale either:** Ingham blocks that architecture already at physical radius `O(M)`. The RH-facing continuation must therefore add a new currency -- for example a `T`-dependent detector with controlled conditioning, a multi-observable/source-covariance estimate, discrete-frequency structure, or a direct count/multiplicity/radial-depth coupling -- rather than merely another smooth fixed cutoff.