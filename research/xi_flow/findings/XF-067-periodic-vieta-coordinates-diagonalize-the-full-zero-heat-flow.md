# XF-067 — periodic Vieta coordinates diagonalize the full zero heat flow

**Status:** `EXACT-DERIVED` + `COLLISION-SAFE` + `NONLINEAR-DIAGONALIZATION` + `STRUCTURAL/BRIDGE` + `LITERATURE-CALIBRATED`. XF-062 identifies the exact Cauchy multiplier of the arithmetic-lattice tangent flow, while XF-064--XF-066 progressively lift the moving-line measurement side to finite displacement and reduce its remaining destination hypothesis to a local state criterion. The difficult step is now dynamical: obtain the required post-heat state from the actual nonlinear zero flow, preferably in coordinates that do not break at collisions.

For a globally periodic matched zero system, there is an exact coordinate system with precisely that property. If one period has `N` roots and physical length `L=Ns`, the elementary symmetric coefficients of their unit-circle variables evolve **diagonally under the full backward heat equation**, with decay rates

\[
\boxed{
\delta_k
=\frac{4\pi^2}{L^2}k(N-k),
\qquad 0\le k\le N.
}
\tag{1}
\]

These coordinates remain analytic through multiple roots and through intervals in which the roots are complex. At the arithmetic lattice their first variations are exactly the discrete root-displacement Fourier modes, and (1) becomes the XF-062 tangent Cauchy multiplier. Thus the tangent spectrum is not merely a linearized coincidence: it is the differential of an **exact nonlinear diagonalization** of the periodic heat flow.

There is also an exact triangular bridge back to the positive-frequency root sums. If

\[
P_m=\sum_{j=1}^N e^{2\pi i m x_j/L},
\tag{2}
\]

then Newton identities recover the `k`th Vieta coordinate using only `P_1,\ldots,P_k`. Hence no high positive frequency is required to define a low Vieta mode. The unresolved Xi-scale question is quantitative rather than algebraic: whether the source-controlled moving-line band gives sufficiently strong control of this growing Newton map, and whether the periodic diagonalization can survive localization errors on the `L\asymp\log^3T` window.

## 1. Every periodic zero configuration has a finite trigonometric heat representative

Take one period of roots

\[
x_1,\ldots,x_N\pmod L
\]

and define

\[
\boxed{
G(z,t_0)
:=
\prod_{j=1}^N
2\sin\!\left(\frac{\pi(z-x_j)}L\right).
}
\tag{3}
\]

The function is `L`-periodic when `N` is even and `L`-antiperiodic when `N` is odd. Put

\[
w=e^{2\pi i z/L},
\qquad
u_j=e^{2\pi i x_j/L}.
\tag{4}
\]

Up to a nonzero factor independent of `z`, (3) is

\[
G(z,t_0)
\propto
 e^{-\pi iNz/L}
 \prod_{j=1}^N(w-\nu_j).
\tag{5}
\]

Writing

\[
\prod_{j=1}^N(w-\nu_j)
=
\sum_{k=0}^N(-1)^kE_k(t_0)w^{N-k},
\qquad
E_k=e_k(\nu_1,\ldots,\nu_N),
\tag{6}
\]

therefore gives the finite Fourier expansion

\[
G(z,t_0)
=
A_0(t_0)
\sum_{k=0}^N
(-1)^kE_k(t_0)
 e^{\pi i(N-2k)z/L},
\tag{7}
\]

after absorbing the harmless common phase into `A_0`. In particular `E_0=1`. If the roots are real, `|\nu_j|=1`, so

\[
|E_N|=1,
\qquad
E_{N-k}=E_N\,\overline{E_k}.
\tag{8}
\]

No ordering or simplicity is needed for (5)--(8); roots are counted with multiplicity.

## 2. Backward heat makes the Vieta coordinates exactly diagonal

Evolve (7) by the same backward heat equation as the de Bruijn--Newman family,

\[
\partial_tG=-\partial_z^2G.
\tag{9}
\]

Each trigonometric Fourier coefficient evolves independently. The mode indexed by `k` has spatial frequency

\[
\lambda_k=\frac{\pi}{L}(N-2k),
\tag{10}
\]

so

\[
A_k(t)
=A_k(t_0)e^{\lambda_k^2(t-t_0)}.
\tag{11}
\]

The two outer modes `k=0,N` have the common maximal square frequency `\pi^2N^2/L^2`. Normalize every coefficient by the `k=0` outer mode. Equations (10)--(11) then give

\[
\boxed{
E_k(t)
=E_k(t_0)
\exp\!\left[
-\frac{4\pi^2}{L^2}k(N-k)(t-t_0)
\right].
}
\tag{12}
\]

Thus every nonlinear Vieta mode has an autonomous scalar evolution law

\[
\boxed{E_k'=-\delta_kE_k.}
\tag{13}
\]

The center/translation information sits in the phase of `E_N`, for which `\delta_N=0`; all interior coordinates decay relative to the outer carrier.

Equation (12) is valid whether the roots of `G(\cdot,t)` are real, complex, simple, or multiple. The coefficients remain analytic in `t`, and the polynomial in `w` retains degree `N` because both outer Fourier coefficients stay nonzero. Consequently the unordered root multiset modulo `L` has a coefficient-level continuation through every collision. This is the periodic analogue of the collision-safe symmetric-coordinate principle in XF-050, but here the heat evolution is not merely regular: it is completely diagonal.

For any fixed nonnegative weights `a_k`, one immediately gets the exact dissipation identity

\[
\frac d{dt}
\sum_{k=1}^{N-1}a_k|E_k|^2
=
-2\sum_{k=1}^{N-1}a_k\delta_k|E_k|^2.
\tag{14}
\]

There is therefore no nonlinear mode-to-mode replenishment in these coordinates on the periodic model.

## 3. On real-simple slices this is exactly the periodic logarithmic zero flow

Suppose the roots are real and simple at some time. Differentiating `G(x_j(t),t)=0` under (9) gives

\[
x_j'
=\frac{G_{zz}(x_j)}{G_z(x_j)}.
\tag{15}
\]

Using the product (3),

\[
\frac{G_{zz}(x_j)}{G_z(x_j)}
=
\frac{2\pi}{L}
\sum_{\ell\ne j}
\cot\!\left(
\frac{\pi(x_j-x_\ell)}L
\right).
\tag{16}
\]

The classical cotangent partial fraction

\[
\frac{\pi}{L}\cot\!\left(\frac{\pi y}{L}\right)
=
\operatorname{PV}\sum_{m\in\mathbb Z}\frac1{y-mL}
\tag{17}
\]

turns (16) into

\[
\boxed{
 x_j'
 =2\operatorname{PV}
 \sum_{(\ell,m)\ne(j,0)}
 \frac1{x_j-x_\ell-mL}.
}
\tag{18}
\]

This is exactly the logarithmic zero-motion law for the infinite periodic continuation. Hence (12) is not a different heat model imposed on the same initial roots: it is an exact coefficient representation of the periodic nonlinear zero dynamics used in XF-040--XF-041. Away from collisions uniqueness of the finite cotangent ODE identifies the two descriptions; at a collision the coefficient flow supplies the canonical continuation even though labelled roots cease to be smooth.

The `N=2` case recovers XF-040 immediately. There is only one interior coordinate and

\[
\delta_1=\frac{4\pi^2}{L^2}=\omega^2,
\tag{19}
\]

which is precisely the exact exponential factor in the two-gap sine law.

## 4. The XF-062 Cauchy multiplier is the tangent of the exact Vieta flow

Set `L=Ns` and linearize around the arithmetic lattice

\[
x_j=s(j+\varepsilon a_j),
\qquad
j\in\mathbb Z/N\mathbb Z.
\tag{20}
\]

Let `\zeta=e^{2\pi i/N}`. Then

\[
\nu_j
=\zeta^j
\exp\!\left(\frac{2\pi i\varepsilon a_j}{N}\right).
\tag{21}
\]

At `\varepsilon=0`, the polynomial is `w^N-1`, so every interior Vieta coordinate vanishes. For `1\le k<N`, the power sum

\[
p_k:=\sum_j\nu_j^k
\tag{22}
\]

also vanishes at the lattice, and its first variation is

\[
\delta p_k
=
\frac{2\pi i k}{N}
\sum_j a_j\zeta^{jk}.
\tag{23}
\]

Newton's identity

\[
kE_k
=
\sum_{m=1}^k
(-1)^{m-1}E_{k-m}p_m
\tag{24}
\]

therefore reduces at first order to

\[
\boxed{
\delta E_k
=(-1)^{k-1}
\frac{2\pi i}{N}
\sum_j a_j\zeta^{jk}.
}
\tag{25}
\]

With the unitary discrete Fourier transform, this is `2\pi/\sqrt N` times the root-displacement Fourier mode `N-k`, up to phase and sign. Meanwhile (1) becomes

\[
\delta_k
=
\frac{4\pi^2}{N^2s^2}k(N-k).
\tag{26}
\]

Equation (26) is exactly the XF-062 arithmetic-lattice multiplier `rho_{N,s}^{(k)}`. The symmetry `k\leftrightarrow N-k` matches the positive/negative root-frequency pair. Thus the complete nonlinear periodic flow has coordinates whose differential at equilibrium is the exact tangent Fourier basis and whose finite-amplitude evolution keeps the **same decay eigenvalues**.

This also clarifies the relation to XF-041. Its nonlinear positive-conductance argument proves variance contraction without choosing coordinates and remains useful under coarse gap-envelope hypotheses. The Vieta representation is stronger but more special: it uses global periodicity to restore the finite trigonometric carrier, thereby converting the nonlinear root interaction into diagonal coefficient evolution.

## 5. Low Vieta modes are triangular functions of low positive-frequency root sums

The same variables `nu_j` give the periodic zero Fourier samples

\[
\boxed{
P_m(t)
:=
\sum_{j=1}^N\nu_j(t)^m
=
\sum_{j=1}^N
 e^{2\pi i m x_j(t)/L}.
}
\tag{27}
\]

For complex roots the last expression is still entire and symmetric in the root multiset. Newton identities give, for every `1\le k\le N`,

\[
\boxed{
kE_k
=
\sum_{m=1}^k
(-1)^{m-1}E_{k-m}P_m.}
\tag{28}
\]

Consequently `E_k` is determined only by

\[
P_1,\ldots,P_k.
\tag{29}
\]

This is an exact finite-amplitude one-sidedness statement. A high positive-frequency root sum cannot enter a lower Vieta coordinate through the change of variables. Conversely, the usual inverse Newton identities recover `P_k` from `E_1,\ldots,E_k`, so the low-positive-frequency root field and the low Vieta field contain the same finite algebraic information.

Combining (12) and (28) yields a collision-safe nonlinear transport scheme:

\[
(P_1,\ldots,P_k)_{t_0}
\quad\longleftrightarrow\quad
(E_1,\ldots,E_k)_{t_0}
\quad\xrightarrow{\text{diagonal heat}}
(E_1,\ldots,E_k)_t
\quad\longleftrightarrow\quad
(P_1,\ldots,P_k)_t.
\tag{30}
\]

Unlike a labelled-root argument, every arrow in (30) remains meaningful on the discriminant. Unlike a generic nonlinear Fourier evolution, the middle arrow has no convolution or high-to-low mixing at all.

## 6. Source-scale match and the remaining quantitative obstruction

Use the current XF-062--XF-066 frame

\[
q\asymp\log^2T,
\qquad
M=q^2,
\qquad
N=2M,
\qquad
s\asymp\frac1{\log T}.
\tag{31}
\]

Then the natural periodic physical length is

\[
L=Ns\asymp\log^3T,
\tag{32}
\]

which is exactly the window scale already singled out by the moving-line construction. The periodic root frequency corresponding to `E_k` is

\[
\xi_k=\frac{2\pi k}{L},
\tag{33}
\]

while the index frequency is `theta_k=2\pi k/N`. Thus `k\asymp q` corresponds to the memory frequency `xi\asymp1/\log T`, and the XF-062/XF-066 upper edge

\[
|\theta|\lesssim\frac{\log\log T}{q}
\tag{34}
\]

corresponds to

\[
k\lesssim q\log\log T.
\tag{35}
\]

On exactly this range, (12) supplies the same fixed-time Cauchy damping exponent used tangent-linearly in XF-062, but now at arbitrary finite amplitude and across collisions.

What is **not** automatic is the quantitative change of coordinates in (28) when `k` grows as in (35). At an all-real slice, the crude unit-circle estimate is only

\[
|E_k|\le {N\choose k},
\tag{36}
\]

which is far too large to combine directly with the `O(\log\log T)` damping exponent near the upper memory edge. Therefore (12) does not by itself prove the XF-066 state package, nor does it show that the actual nonperiodic Xi window can be replaced by a periodic carrier with negligible error.

The next exact gate is now sharply stated: obtain a scale-appropriate bound for the triangular Newton map (28) from the source-controlled moving-line power sums on `k\lesssim q\log\log T`, and quantify the error made by replacing the Gaussian/localized Xi window of length `\asymp\log^3T` by its periodic trigonometric carrier. If both errors are `o(1)` in the selector normalization, the collision and finite-amplitude parts of the destination transport would already be supplied by (12).

## 7. Prior-art and novelty boundary

Backward heat flow of trigonometric polynomials and its unitary-polynomial representation are classical structures. Kabluchko's 2025 work on unitary Hermite polynomials, already anchored in `research/xi_flow/SOURCES.md`, explicitly places trigonometric polynomials and their backward heat flow in the finite/free-probability setting. No novelty is claimed for the elementary fact that the heat operator acts diagonally on trigonometric Fourier coefficients, for Vieta/Newton identities, or for the cotangent partial fraction.

The line-specific contribution is their combination with the existing Xi-flow architecture: equations (12), (25)--(26), and (28) identify the periodic Vieta coefficients as **exact nonlinear, collision-safe continuations of the XF-062 root Fourier modes**, with exactly the same Cauchy clock and an explicitly triangular interface to the positive-frequency zero field used by XF-048--XF-060. This removes mode mixing and root-label singularities from the periodic matched problem; the remaining obstruction is localization plus quantitative conditioning of the growing Newton transform, not nonlinear periodic heat transport itself.

## 8. Consequence for `xi_flow`

XF-066 leaves a physical finite-difference smoothing target because the selector frame is expressed directly in root displacement. The present result provides a second nonlinear destination coordinate that is much better adapted to dynamics: on a periodic `\log^3T` carrier it evolves exactly, diagonally, and through collisions, while linearizing to the same Fourier modes that underlie the `R_4` criterion.

This does not prove that an actual Xi transition slice reaches the XF-066 state conditions, and it does not justify periodizing a nonperiodic Xi block. It does, however, eliminate a substantial matched-model uncertainty. **Finite amplitude and collisions do not intrinsically destroy the Cauchy slow-mode clock; in periodic Vieta coordinates the full heat flow retains that clock exactly.** A viable continuation can now attack the source-to-Vieta conditioning and localization errors directly instead of first proving a general high-order nonlinear smoothing theorem for labelled gaps.