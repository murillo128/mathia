# PF-247 — fixed axis compactification is parity-Jacobi in corridor modes

**Status:** `EXACT-DERIVED + MODE-LOCALITY + ASYMPTOTIC-JACOBI + CRITICAL-RELATIVE-SPECTRUM + POSITIVE/ROUTE-NARROWING`.

PF-243 reduces the remaining high-high shear gate to separated Robin-Poisson smoothing of order `R>1`. PF-244 shows that one-sided seam form domination alone allows arbitrary high-to-low leakage, while PF-245 shows that the bare actual seam square root cannot obtain the required gain merely from a family-uniform supercritical Fourier strip. PF-246 gives the opposite calibration: if the seam normalizer commutes with the corridor transverse operator, separation gives smoothing of every order.

The fixed boundary compactification already present in PF-238 has substantially more structure than the abstract PF-244 countermodel. Let

\[
A=-\partial_\theta^2+\csc^2\theta,
\qquad
L=-\partial_\theta(\sin^2\theta\,\partial_\theta)
+\frac34(1+\sin^2\theta),
\tag{1}
\]

on `L^2((0,\pi),d\theta)`. PF-238 identifies `L=U(1-\partial_\tau^2)U^*`, where `\tau=\log\tan(\theta/2)` and `U` is the density-corrected axis compactification. Put

\[
\alpha=\frac{1+\sqrt5}{2},
\qquad
\kappa_n=n+\alpha.
\tag{2}
\]

The Friedrichs eigenbasis of `A` is the normalized Gegenbauer basis

\[
e_n(\theta)
=h_n^{-1/2}\sin^\alpha\theta\,C_n^{(\alpha)}(\cos\theta),
\qquad
Ae_n=\kappa_n^2e_n.
\tag{3}
\]

In this basis the compactified axis generator `L` is **exactly parity tridiagonal**:

\[
\boxed{
\langle e_m,Le_n\rangle=0
\quad\text{unless}\quad m-n\in\{-2,0,2\}.
}
\tag{4}
\]

Thus the width-independent compactification does not possess PF-244's arbitrary direct high-mode-to-fixed-low-mode coupling at generator level. Spectral conversion occurs through nearest-neighbor steps inside the even and odd mode chains.

There is also a sharp relative spectral statement. Define the bounded positive operator

\[
J:=A^{-1/2}LA^{-1/2}.
\tag{5}
\]

Each parity sector of `J` is a half-line Jacobi matrix whose diagonal and off-diagonal coefficients satisfy

\[
\boxed{
b_n\longrightarrow\frac12,
\qquad
a_n\longrightarrow-\frac14.}
\tag{6}
\]

After the harmless alternating sign change on each parity chain, `J` is therefore a compact perturbation of two copies of the constant Jacobi matrix with diagonal `1/2` and off-diagonal `1/4`. Consequently

\[
\boxed{\sigma_{\rm ess}(J)=[0,1].}
\tag{7}
\]

This both sharpens and explains PF-237/PF-238's one-sided geometry. There can be no positive constant `c` with `L\ge cA`, because `0` lies in the essential spectrum of the relative operator. But the loss of coercivity is **critical and mode-local**: it is generated asymptotically by a nearest-neighbor Jacobi chain, not by an unrestricted nonlocal mixer.

PF-247 does **not** prove the desired separated `R>1` Robin-Poisson estimate. The actual hyperbolic seam still includes PF-235's width-dependent Fermi-to-axis reparameterization, PF-233 uses the variable transverse operator `K_a=T_a^{1/2}` rather than exactly `A^{1/2}`, and taking non-polynomial functions such as seam square roots can spread a tridiagonal generator across arbitrarily many mode steps. The new reduction is that the fixed compactification part of the conversion problem now has an exact discrete model. A positive proof should quantify functional-calculus decay or commutators for this critical parity-Jacobi structure and then show that the `O(w^2)` hypercycle-coordinate defect and the `T_a` replacement preserve enough of that locality.

## Claim

Let `A,L` be as in (1), with Friedrichs realization for `A`. Let `\alpha` and `\kappa_n` be as in (2), and define

\[
\phi_n(\theta)=\sin^\alpha\theta\,C_n^{(\alpha)}(\cos\theta).
\tag{8}
\]

Then:

1. `A\phi_n=\kappa_n^2\phi_n` and the normalized `e_n=\phi_n/\|\phi_n\|` form an orthonormal basis;
2. `L\phi_n` lies in `\operatorname{span}\{\phi_{n-2},\phi_n,\phi_{n+2}\}` with negative-index terms omitted;
3. writing
   \[
   L\phi_n=d_n^+\phi_{n+2}+d_n^0\phi_n+d_n^-\phi_{n-2},
   \tag{9}
   \]
   the coefficients are explicit rational functions of `n` and `\alpha` given below;
4. the normalized relative operator `J=A^{-1/2}LA^{-1/2}` preserves parity and is Jacobi on each parity sector;
5. its coefficients converge as in (6), hence `J` differs compactly from the direct sum of two constant half-line Jacobi matrices;
6. `\sigma_{\rm ess}(J)=[0,1]`, and therefore no uniform reverse form bound `L\ge cA` with `c>0` can hold.

## 1. The corridor basis is Gegenbauer

The parameter `\alpha` satisfies

\[
\alpha(\alpha-1)=1.
\tag{10}
\]

With `x=\cos\theta`, the Gegenbauer equation

\[
(1-x^2)p''-(2\alpha+1)xp'+n(n+2\alpha)p=0
\tag{11}
\]

shows directly that

\[
A\bigl(\sin^\alpha\theta\,C_n^{(\alpha)}(\cos\theta)\bigr)
=(n+\alpha)^2
\sin^\alpha\theta\,C_n^{(\alpha)}(\cos\theta).
\tag{12}
\]

The norm is the standard Gegenbauer norm

\[
h_n
=\frac{\pi 2^{1-2\alpha}\Gamma(n+2\alpha)}
{n!(n+\alpha)\Gamma(\alpha)^2}.
\tag{13}
\]

This is the same exact `A` spectrum used in PF-231/PF-233, now with the eigenfunctions retained because spectral conversion rather than only eigenvalue counting is the issue.

## 2. The compactified axis generator moves only two Gegenbauer degrees

For a function `y(\theta)=\sin^\alpha\theta\,p(x)` with `x=\cos\theta`, direct differentiation gives

\[
\frac{Ly}{\sin^\alpha\theta}
=-(1-x^2)^2p''
+(2\alpha+3)x(1-x^2)p'
+\left[\alpha+\frac32
-(\alpha+\tfrac12)(\alpha+\tfrac32)x^2\right]p.
\tag{14}
\]

For `p=C_n^{(\alpha)}`, use (11) and put

\[
H_n:=\left(\kappa_n+1\right)^2-\frac14.
\tag{15}
\]

Then (14) reduces to

\[
\frac{L\phi_n}{\sin^\alpha\theta}
=\left(\kappa_n^2+\frac12\right)C_n^{(\alpha)}
+2(n+2\alpha-1)xC_{n-1}^{(\alpha)}
-H_nx^2C_n^{(\alpha)}.
\tag{16}
\]

The standard Gegenbauer recurrences give

\[
xC_{n-1}^{(\alpha)}
=\frac{n}{2(\kappa_n-1)}C_n^{(\alpha)}
+\frac{n+2\alpha-2}{2(\kappa_n-1)}C_{n-2}^{(\alpha)},
\tag{17}
\]

and

\[
x^2C_n^{(\alpha)}
=P_nC_{n+2}^{(\alpha)}+Q_nC_n^{(\alpha)}+R_nC_{n-2}^{(\alpha)},
\tag{18}
\]

where

\[
P_n=\frac{(n+1)(n+2)}{4\kappa_n(\kappa_n+1)},
\tag{19}
\]

\[
Q_n=\frac{n^2+2\alpha n+\alpha-1}
{2(\kappa_n-1)(\kappa_n+1)},
\tag{20}
\]

and

\[
R_n=\frac{(n+2\alpha-1)(n+2\alpha-2)}
{4\kappa_n(\kappa_n-1)}.
\tag{21}
\]

Substitution into (16) proves the exact three-term parity law (9), with

\[
\boxed{d_n^+=-H_nP_n,}
\tag{22}
\]

\[
\boxed{
d_n^0=
\kappa_n^2+\frac12-H_nQ_n
+\frac{n(n+2\alpha-1)}{\kappa_n-1},}
\tag{23}
\]

and

\[
\boxed{
d_n^-=
-H_nR_n
+\frac{(n+2\alpha-1)(n+2\alpha-2)}{\kappa_n-1}.}
\tag{24}
\]

No estimate or asymptotic argument is used in (14)--(24). The bandedness is exact.

## 3. Relative normalization exposes a critical Jacobi limit

Passing to the orthonormal basis `e_n=\phi_n/\sqrt{h_n}`, the upper off-diagonal entry of `L` is

\[
\ell_n^+
=d_n^+\sqrt{\frac{h_{n+2}}{h_n}},
\tag{25}
\]

where

\[
\frac{h_{n+2}}{h_n}
=\frac{(n+2\alpha)(n+2\alpha+1)}{(n+1)(n+2)}
\frac{n+\alpha}{n+\alpha+2}.
\tag{26}
\]

Because `A^{-1/2}e_n=\kappa_n^{-1}e_n`, the relative Jacobi coefficients are

\[
a_n
=\frac{\ell_n^+}{\kappa_n\kappa_{n+2}},
\qquad
b_n=\frac{d_n^0}{\kappa_n^2}.
\tag{27}
\]

Equations (19)--(27) give immediately

\[
\lim_{n\to\infty}a_n=-\frac14,
\qquad
\lim_{n\to\infty}b_n=\frac12.
\tag{28}
\]

Only equal parity indices couple, so after identifying `e_{2j}` and `e_{2j+1}` with two copies of `\ell^2(\mathbb N_0)`, each block has the ordinary Jacobi form

\[
(J_\pm u)_j
=a_j^{(\pm)}u_{j+1}
+b_j^{(\pm)}u_j
+a_{j-1}^{(\pm)}u_{j-1},
\tag{29}
\]

with coefficients tending to `-1/4` and `1/2`. Multiplying the `j`-th basis vector in either block by `(-1)^j` changes the limiting off-diagonal sign to `+1/4` and changes nothing spectral.

PF-238 already proves `0<L\le 2A`, so `J` is a bounded positive self-adjoint operator. Since the coefficient differences in (29) tend to zero, the difference between each parity block and its constant-coefficient limit is compact: truncate after mode `N`; the operator norm of the remaining banded tail is bounded by a fixed multiple of the suprema of the coefficient differences beyond `N`, which tend to zero.

The constant limit has Fourier symbol

\[
\frac12-\frac12\cos t
=\sin^2\frac t2,
\tag{30}
\]

and hence spectrum `[0,1]`. Compact perturbations preserve essential spectrum, proving (7).

## 4. What the Jacobi limit says about endpoint escape

PF-237 detects a genuine spectral-type mismatch: the complete-axis/actual lifted seam permits translation escape, whereas the matched corridor normalizer has compact inverse. Equation (7) gives a more precise calibration for the fixed axis compactification. Relative to the confining corridor basis, the loss of coercivity is represented by the bottom edge of a constant Jacobi band.

In particular, approximate zero-energy sequences for `J` can be built from slowly varying packets supported at large **mode index** in either parity chain. They do not require an operator that sends one arbitrarily high mode directly into one fixed low mode. This distinction is exactly the extra structure absent from PF-244's abstract countermodel.

At the same time, (7) explains why a reverse order cannot be recovered by a clever equivalent norm. The compactification is critically noncoercive relative to `A`; its limiting Jacobi symbol touches zero. The correct positive question is therefore not whether `L` and `A` are uniformly equivalent, but whether the particular non-polynomial seam/Robin functions of the compactified generator retain enough **off-diagonal decay along this mode chain** after source separation.

## 5. Consequences for the PF-243 smoothing gate

PF-247 changes the surviving proof target in three ways.

First, the width-independent `\tau\leftrightarrow\theta` compactification is no longer an opaque source of arbitrary spectral mixing. Its basic generator has an exact nearest-neighbor parity model.

Second, PF-245's Fourier-strip obstruction should not be read as the only possible locality currency. The relevant conversion problem can also be posed as matrix decay for functions of an asymptotically constant Jacobi operator relative to the `A` mode index. A strip width barely above the intrinsic Fourier mass threshold does not by itself decide that discrete mode-decay problem.

Third, the remaining perturbations are now identifiable. PF-235's actual hypercycle footpoint map `T_\rho` is a width-dependent deformation of the axis coordinate with `O(w^2)` Jacobian defect, while PF-233 replaces the reference `sA^{1/2}` by `K_a=T_a^{1/2}` under only the currently proved variable-width form bounds. Either perturbation could still destroy the amount of mode locality needed for `R>1`; PF-247 does not assume otherwise.

A decisive next theorem would bound high-to-low matrix blocks of the **normalized full Robin map**, not merely of `L`, in the `K_a` spectral decomposition. The exact Jacobi calibration tells such a theorem what must be preserved and gives a concrete falsification model: if the functional calculus or the two geometric perturbations generate a nondecaying long-range tail in parity index, the complete-lift smoothing route fails and the finite physical trace realization becomes the remaining natural escape.

## 6. Prior-art and novelty audit

The special-function ingredients are classical. NIST DLMF Chapter 18, especially §§18.8--18.9, records the Gegenbauer differential equation, recurrences, and derivative identities used in (11), (17), and (18):

- https://dlmf.nist.gov/18.8
- https://dlmf.nist.gov/18.9

The spectral theory of half-line Jacobi matrices and compact/asymptotically constant perturbations is classical; a standard reference is Gerald Teschl, *Jacobi Operators and Completely Integrable Nonlinear Lattices*, AMS Mathematical Surveys and Monographs 72 (2000):

- https://www.mat.univie.ac.at/~gerald/ftp/book-jac/index.html

A targeted search also finds tridiagonal-representation treatments of Pöschl--Teller systems, for example G.-Q. Huang-Fu and M.-C. Zhang, *Exact solution of the modified Pöschl--Teller potential in the tridiagonal representation*, International Journal of Quantum Chemistry 112 (2012), 2482--2485, DOI `10.1002/qua.23276`. That literature confirms that tridiagonal special-function representations are not novel in themselves.

No general novelty is claimed for Gegenbauer recurrences, Jacobi matrices, compact-perturbation essential-spectrum stability, or tridiagonal Pöschl--Teller representations. A targeted search did not identify the specific PF statement derived here: PF-238's density-corrected **axis compactification generator** relative to PF-233's Pöschl--Teller corridor reference splits into two parity Jacobi chains with limiting coefficients `(-1/4,1/2,-1/4)`, making the relative essential spectrum exactly `[0,1]`. The proof is elementary from the displayed operators and classical recurrences; external literature is context rather than a hidden theorem dependency.

## 7. Falsification and boundary checks

1. **Axis control, not the full actual seam.** `L` is PF-238's fixed compactified complete-axis generator. PF-235's width-dependent Fermi-to-axis map and PF-234/PF-245's intrinsic hyperbolic seam still require separate operator control.
2. **Generator locality is not square-root locality.** A tridiagonal `L` does not imply that `L^{1/2}`, `q_w(L)^{1/2}`, or a Robin resolvent is tridiagonal. Functional calculus can create long-range matrix tails.
3. **`A`, not yet `T_a`.** The exact basis above diagonalizes the Pöschl--Teller reference `A`. PF-233 proves two-sided form comparison between `T_a` and `s^2A`, not a spectral-basis equivalence strong enough to transfer (4) automatically to `K_a`.
4. **Critical bottom edge.** The result does not restore two-sided seam/corridor form equivalence. On the contrary, `0 in sigma_ess(J)` proves the reverse relative coercivity fails already for the fixed axis compactification.
5. **No contradiction with PF-245.** PF-245 concerns holomorphic Fourier-strip control of the bare actual seam square root. PF-247 identifies a different, discrete mode-conversion representation for the compactified axis generator; neither theorem implies the other.
6. **No weak-trace or RH conclusion.** The PF-243 shear estimate, physical `P/H` recoupling, finite-pant completion, neighboring-module extension, global weak-`S_1` reassembly, scattering/determinant bridge, and any zeta-zero statement remain open.

## 8. Reproducibility checks

The algebra is finite. Starting from (14), substitute the Gegenbauer differential equation and the two standard recurrences to recover (16)--(24). Independently, the first normalized relative coefficients are approximately

\[
a_0=-0.2331274162,\quad b_0=0.7092202598,
\]

\[
a_1=-0.2434721290,\quad b_1=0.5880709762,
\]

and by `n=10`

\[
a_{10}=-0.2495974452,\quad b_{10}=0.5046234476,
\]

consistent with (28). These decimals are diagnostics only; the theorem is the exact symbolic derivation above.
