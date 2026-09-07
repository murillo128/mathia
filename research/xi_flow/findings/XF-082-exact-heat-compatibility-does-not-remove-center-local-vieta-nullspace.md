# XF-082 — exact heat compatibility does not remove the center-local Vieta nullspace

**Status:** `EXACT-DERIVED` + `NEGATIVE/INTERFACE` + `DYNAMIC-CHEBYSHEV-NULLSPACE` + `HEAT-COMPATIBLE-NO-GO`. XF-081 proves that static center-local accuracy does not identify the periodic Vieta state: an exponentially small Chebyshev correction can prescribe both outer Fourier edges and force an arbitrarily long low power-sum prefix to vanish. One obvious repair left open there was to demand that the surrogate belong to an exact periodic backward-heat trajectory rather than be chosen independently at one frozen time.

That repair is still insufficient at the Xi scale. Let

\[
A_D(\theta)=\sum_{m=-D}^{D}p_{m,D}e^{im\theta},
\qquad
B_D(\theta)=\sum_{m=-D}^{D}b_{m,D}e^{im\theta},
\qquad N=2D,
\tag{1}
\]

be the XF-078 explicit approximant and the XF-081 Chebyshev-repaired carrier, with

\[
b_{D,D}=b_{-D,D}=1,
\qquad
b_{D-r,D}=b_{-D+r,D}=0
\quad (1\le r\le K),
\tag{2}
\]

where `K log D=o(D)`. Put `theta=2 pi z/L` and

\[
\kappa_L:=\left(\frac{2\pi}{L}\right)^2.
\tag{3}
\]

Evolve both trigonometric polynomials by the **exact same periodic backward heat equation** as XF-067:

\[
A_D(\theta,t)
:=\sum_{m=-D}^{D}p_{m,D}e^{\kappa_Lm^2t}e^{im\theta},
\qquad
B_D(\theta,t)
:=\sum_{m=-D}^{D}b_{m,D}e^{\kappa_Lm^2t}e^{im\theta}.
\tag{4}
\]

Equivalently, as functions of `z`,

\[
\partial_t A_D=-\partial_z^2 A_D,
\qquad
\partial_t B_D=-\partial_z^2 B_D.
\tag{5}
\]

Suppose `L=L(D)` and a heat horizon `t_D` satisfy

\[
\boxed{\frac{D\,t_D}{L^2}\longrightarrow0.}
\tag{6}
\]

Then for every fixed derivative order `J` there are constants `c_J>0`, `eta_*>0`, and `D_J` such that

\[
\boxed{
\sup_{0\le t\le t_D}
\sup_{\substack{|\Re\theta|\le\pi/2\\|\Im\theta|\le\eta_*}}
\max_{0\le j\le J}
\left|
\partial_\theta^j
\bigl(B_D(\theta,t)-A_D(\theta,t)\bigr)
\right|
\le e^{-c_JD}
}
\tag{7}
\]

for `D>=D_J`, after reducing `eta_*` by a fixed factor if necessary.

At the same time the two normalized Vieta trajectories remain macroscopically different. For the repaired carrier,

\[
\boxed{
E_0^{B}(t)=E_N^{B}(t)=1,
\qquad
E_r^{B}(t)=E_{N-r}^{B}(t)=0
\quad(1\le r\le K),
}
\tag{8}
\]

for every `t`, and therefore

\[
\boxed{
P_1^{B}(t)=\cdots=P_K^{B}(t)=0.
}
\tag{9}
\]

For the explicit XF-078 carrier, positive-edge normalization gives the exact first mode

\[
\boxed{
P_1^{A}(t)
=
\frac{2D(2D-1)}{2D-3}
\exp\!\left[-\kappa_L(2D-1)t\right].
}
\tag{10}
\]

Under (6),

\[
\boxed{
\inf_{0\le t\le t_D}|P_1^{A}(t)|
=(2+o(1))D,
}
\tag{11}
\]

whereas `P_1^B(t)` is identically zero. Thus two degree-`N`, **exact heat-compatible** periodic carriers can remain exponentially indistinguishable throughout the whole center observation cylinder while carrying incompatible low Vieta states.

At the Xi parameters,

\[
D=M=q^2=\Theta((\log T)^4),
\qquad
L=(\log T)^3,
\tag{12}
\]

so

\[
\frac{L^2}{D}=\Theta((\log T)^2).
\tag{13}
\]

Therefore (7)--(11) hold not only on every fixed de Bruijn heat interval but on every horizon

\[
t_D=o((\log T)^2).
\tag{14}
\]

The full guarded/source-visible range `K=O(q log log T)` still satisfies `K log D=o(D)`. Exact periodic heat compatibility therefore does **not** repair the source dictionary left open by XF-081. A positive dictionary must impose information that distinguishes the global divisor/root geometry or must map the Xi analytic carrier directly to the destination observable; local function accuracy plus exact free heat evolution is not enough.

## 1. The XF-081 nullspace is exponentially small on a fixed thin complex strip

XF-081 only needed the actual Xi height `|Im theta|=O(D^(-1/2))`. For the heat argument one can retain a small complex strip of fixed height.

Recall its Chebyshev basis

\[
y(\theta)=2\cos\theta-1,
\tag{15}
\]

\[
C_n(\theta)=2^{1-n}T_n(y(\theta)),
\qquad
S_n(\theta)
=2^{1-n}(e^{i\theta}-e^{-i\theta})U_{n-1}(y(\theta)).
\tag{16}
\]

For `|Re theta|<=pi/2` and `|Im theta|<=eta`, the point `y(theta)` lies in an `O(eta)`-neighborhood of `[-1,1]`. Using

\[
T_n(y)=\frac12(\zeta^n+\zeta^{-n}),
\qquad
\zeta=y+\sqrt{y^2-1},
\tag{17}
\]

one has uniformly in this neighborhood

\[
\log^+|\zeta|\le C\sqrt{\eta}.
\tag{18}
\]

The corresponding second-kind formula adds only a polynomial factor in `n` and `eta^(-1)`. Hence, for every fixed `J`,

\[
\max_{j\le J}
\sup_{\substack{|\Re\theta|\le\pi/2\\|\Im\theta|\le\eta}}
\left(
|\partial_\theta^j C_n(\theta)|
+
|\partial_\theta^j S_n(\theta)|
\right)
\le
C_{J,\eta}n^{C_J}
\exp\!\left[-(\log2-C\sqrt{\eta})n\right].
\tag{19}
\]

Choose a fixed `eta_0>0` so small that `C sqrt(eta_0)<(log 2)/4`. XF-081's triangular repair uses only terminal degrees `D-r`, `0<=r<=K`, with coefficients

\[
|\alpha_r|+|\beta_r|
\le (CD)^{C(r+1)}.
\tag{20}
\]

Consequently its correction

\[
Q_{D,K}:=B_D-A_D
\tag{21}
\]

satisfies, for fixed `J`,

\[
\max_{j\le J}
\sup_{\substack{|\Re\theta|\le\pi/2\\|\Im\theta|\le\eta_0}}
|\partial_\theta^jQ_{D,K}(\theta)|
\le
\exp\!\left[
-c_0D+O_J(K\log D)
\right]
\le e^{-c_1D}.
\tag{22}
\]

The last inequality uses `K log D=o(D)`. This is a modest strengthening of the shrinking-strip estimate in XF-081, but it is exactly what is needed to test a dynamical repair.

No contradiction with analytic continuation is involved. Equation (22) is an exponentially accurate **approximate** nullspace, not exact vanishing on an open set.

## 2. Exact backward heat cannot amplify the hidden state fast enough

Let

\[
\tau:=\kappa_L t.
\tag{23}
\]

For a trigonometric polynomial `Q(theta)=sum_{|m|<=D} q_m e^(im theta)`, exact backward heat has the imaginary-Gaussian representation

\[
\boxed{
(e^{-\tau\partial_\theta^2}Q)(\theta)
=
\frac1{\sqrt{4\pi\tau}}
\int_{\mathbb R}
e^{-y^2/(4\tau)}
Q(\theta+iy)\,dy,
}
\tag{24}
\]

because the `m`-th Fourier mode acquires the Gaussian moment `e^(m^2 tau)`.

Apply (24) to `Q_{D,K}`. On a slightly smaller fixed strip, split the integral at a fixed imaginary displacement smaller than the margin in (22). The central part is bounded by `e^(-c_1 D)`.

For the tail, a crude global coefficient bound is sufficient. The Chebyshev recurrences and (20) give

\[
\sum_{|m|\le D}|q_m|
\le \exp(CD+o(D)),
\tag{25}
\]

so

\[
|Q_{D,K}(\theta+iy)|
\le
\exp(CD+o(D)+D|y|).
\tag{26}
\]

Condition (6) is exactly

\[
\tau D
=O\!\left(\frac{Dt_D}{L^2}\right)
=o(1).
\tag{27}
\]

Thus the stationary point of the tail exponent

\[
-\frac{y^2}{4\tau}+D|y|
\tag{28}
\]

lies at `|y|=2 tau D=o(1)`, inside the central strip. Beyond any fixed tail threshold the exponent is decreasing, while

\[
\frac1\tau\gg D.
\tag{29}
\]

The Gaussian tail therefore contributes `e^(-omega(D))`, even after the global factor `e^(CD+o(D))`. Fixed `theta`-derivatives only insert polynomial powers of `D` and do not change the exponential conclusion. This proves (7).

The scale boundary is informative. The largest raw Fourier amplification is

\[
\exp(\kappa_LD^2t).
\tag{30}
\]

To compete with an `e^(-cD)` local nullspace requires heat time of order `L^2/D`, not order one. At Xi scale that is `Theta((log T)^2)`, parametrically longer than the fixed heat intervals used by the current transition program.

## 3. The Vieta discrepancy is preserved exactly by the same heat flow

The periodic heat flow acts diagonally on raw Fourier coefficients. For `B_D`, equations (2) imply

\[
b_{\pm D}(t)=e^{\kappa_LD^2t},
\qquad
b_{D-r}(t)=b_{-D+r}(t)=0
\quad(1\le r\le K).
\tag{31}
\]

Normalizing by the positive outer mode leaves the terminal ratio equal to one because the `+D` and `-D` modes have the same heat rate. This proves (8), and Newton identities give (9) at every time. The entire source-visible prefix can therefore remain exactly absent along the full heat trajectory.

For `A_D`, XF-080 gives at `t=0`

\[
P_1^{A}(0)=E_1^{A}(0)
=\frac{2D(2D-1)}{2D-3}.
\tag{32}
\]

The `D-1` raw mode grows as `e^(kappa_L (D-1)^2 t)`, while the normalized `D` outer mode grows as `e^(kappa_L D^2 t)`. Hence

\[
E_1^{A}(t)
=
E_1^{A}(0)
e^{-\kappa_L(2D-1)t},
\tag{33}
\]

which is (10). Under (6),

\[
\kappa_L(2D-1)t_D
=O(Dt_D/L^2)
=o(1),
\tag{34}
\]

so (11) follows uniformly.

This is not merely the statement that backward heat is ill-conditioned. The two compared objects obey the exact finite periodic heat equation, have the same degree and frequency lattice, and remain locally exponentially close on the source observation region, while one carries a macroscopic first Vieta mode and the other has an arbitrarily long exactly vanishing Vieta prefix.

## 4. Stress tests and evidence boundary

Several possible loopholes are excluded by the construction.

First, the effect is not caused by changing the mode budget: both trajectories use exactly the `2D+1=N+1` Fourier modes of the XF-067 carrier.

Second, it is not caused by a frozen-time residual: both trajectories satisfy the periodic backward heat equation exactly, so every local free-heat residual is identically zero.

Third, the low-mode difference does not disappear on the relevant heat clock. The exact decay exponent of `P_1^A` is `O(Dt/L^2)`, which is `o(1)` throughout (6).

Fourth, the repaired carrier has both outer modes nonzero and equal after normalization, and its degree is preserved. The argument therefore does not exploit a disappearing leading coefficient.

The boundary is equally important. This finding does **not** prove that `B_D` has real roots, bounded-displacement roots, or the actual Xi divisor. It does not show that either heat trajectory approximates the time-dependent Gaussian quotient `R_{T,L}(t)` on its whole evolution; rather, it proves that if a local dynamic comparison admits one such periodic heat carrier at any tolerance larger than the null correction, exact heat compatibility alone cannot make that carrier unique. A root-faithful/global-divisor condition may still remove the freedom.

Exact equality on an open center cylinder would also be a different problem: analyticity would then identify the trigonometric solution globally. The no-go concerns the exponentially accurate asymptotic interface supplied by XF-073/XF-078, where exponentially small local changes remain admissible.

## 5. Prior-art and novelty boundary

The broad mechanisms are classical. Remez/Logvinenko--Sereda spectral inequalities quantify that band-limited functions can be recovered from restricted observation only with constants that deteriorate exponentially with spectral width; heat observability uses the same spectral-inequality architecture. Fourier-extension theory likewise exhibits highly accurate local approximation together with severe coefficient nonuniqueness/conditioning. A targeted search found no source stating the specific Vieta-prefix construction or the Xi-scale comparison `L^2/D=Theta((log T)^2)`.

No external theorem is load-bearing here. The proof uses the explicit Chebyshev nullspace already derived in XF-081, the elementary imaginary-Gaussian representation of finite Fourier backward heat, and the exact coefficient/Vieta evolution from XF-067/XF-080. `SOURCES.md` therefore does not require a new durable dependency.

The line-specific delta is the dynamic boundary:

\[
\boxed{
\text{center-local accuracy}
+
\text{exact periodic heat compatibility}
\not\Rightarrow
\text{source-faithful Vieta state}
}
\tag{35}
\]

through every heat horizon `t=o(L^2/D)`, in particular every fixed Xi heat horizon.

## 6. Falsification / audit test and consequence

The decisive audit is finite and exact apart from the displayed asymptotics.

1. Reconstruct the XF-081 triangular correction and verify (2) exactly for several `D,K`.
2. Evolve every Fourier coefficient by `e^(kappa_L m^2 t)`. The edge zeros must remain exact and the normalized first mode of `A_D` must agree with (10).
3. Numerically maximize `|B_D-A_D|` on a fixed thin center strip for increasing `D` at any fixed `t`, or for `t=o(L^2/D)`. The logarithm should remain linear negative in `D`, up to the sublinear correction predicted above.
4. Any counterexample to the fixed-strip Chebyshev bound (19), or a heat horizon satisfying (6) on which the local difference becomes non-exponential, would falsify the new dynamic step.

The practical consequence for the current frontier is restrictive. XF-081 left “heat-compatible global/divisor constraint” as one possible repair. XF-082 removes **heat compatibility by itself** from that list. The surviving positive routes must add genuinely source-faithful global divisor/root information, or bypass the surrogate-to-root-polynomial dictionary and map the Gaussian/logarithmic-derivative carrier directly into the one-center weighted selector. The independent positive-`Lambda` destination-mass gate remains unchanged.
