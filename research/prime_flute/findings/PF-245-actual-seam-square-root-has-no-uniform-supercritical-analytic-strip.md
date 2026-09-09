# PF-245 — actual seam square root has no uniform supercritical analytic strip

**Status:** `EXACT-DERIVED + STURM-LIOUVILLE-THRESHOLD + ANALYTICITY-BARRIER + DECISIVE-NEGATIVE/PROOF-STRATEGY-OBSTRUCTION + ROUTE-NARROWING`.

PF-243 reduces the remaining high-high shear gate to a one-sided separated Robin-Poisson smoothing estimate with a fixed gain `R>1`. PF-244 then shows that positivity, one-sided form domination, energy contraction, and positive source/observation separation cannot imply such a gain abstractly: an arbitrary seam square root can leak high tangential frequency into a low mode before propagation. The actual PF-205/PF-234 complete-lift seam has much more structure than that countermodel, because in intrinsic signed Fermi-area coordinates it is translation invariant along the seam and hence Fourier diagonal.

That extra structure removes arbitrary spectral mixing, but it does **not** provide a uniform supercritical analytic-locality margin for the bare seam square root. Let `q_w^{hyp,+}(xi)` be the exact symmetric intrinsic seam Dirichlet-to-Neumann multiplier at halfwidth `w`. It has a simple zero at an imaginary frequency

\[
\xi=\pm i\kappa_w,
\]

where `kappa_w^2` is the lowest Neumann-Neumann eigenvalue of an explicit regular Sturm-Liouville problem. Its Rayleigh quotient gives the sharp-enough bounds

\[
\boxed{
1\le \kappa_w^2\le \frac{w}{\arctan w},
\qquad
1\le\kappa_w\le 1+\frac{w^2}{6}+O(w^4).
}
\]

Because the zero of `q_w^{hyp,+}` is simple, the positive real-axis square-root symbol

\[
s_w(\xi)=\sqrt{q_w^{hyp,+}(\xi)}
\]

has a square-root branch point at `xi=+-i kappa_w`. Therefore, for every fixed `epsilon>0`, the canonical tail eventually admits **no** single-valued holomorphic extension of `s_{w_n}` to the strip `|Im xi|<1+epsilon`. PF-234 gives `w_n=O(P_n^{-1})`, so the obstruction approaches the critical distance `1` with only `O(P_n^{-2})` room.

This does not refute PF-243's separated Poisson estimate. It rules out a narrower positive strategy: the required fixed supercritical gain cannot be charged solely to a family-uniform holomorphic strip of the **raw actual seam square root**. Any successful argument must use additional joint structure of the Robin inverse/corridor/seam system, a cancellation unavailable to the bare square root, a stronger microlocal statement not equivalent to strip analyticity, or the finite physical trace realization.

## Claim

Work on one complete lifted PF-234 symmetric seam strip in intrinsic signed Fermi-area coordinates. On the even half-strip `0<=x<=w`, the exact metric energy for tangential Fourier frequency `xi` is

\[
\mathcal E_{w,\xi}[v]
=
\int_0^w
\left[
(1+x^2)|v'(x)|^2
+\left(1+\frac{\xi^2}{1+x^2}\right)|v(x)|^2
\right]dx.
\tag{1}
\]

For the symmetric branch impose

\[
v'(0)=0,
\qquad
v(w)=1.
\tag{2}
\]

The Euler-Lagrange equation is

\[
-\frac d{dx}\!\left((1+x^2)v'\right)
+v
+\frac{\xi^2}{1+x^2}v
=0,
\tag{3}
\]

and the boundary flux is the exact symmetric seam multiplier

\[
q_w^{\rm hyp,+}(\xi)
=(1+w^2)v'(w).
\tag{4}
\]

For real `xi`, this is positive. Analytically continue to `xi=i kappa` and put `lambda=kappa^2`. Equation (3) becomes

\[
-\frac d{dx}\!\left((1+x^2)v'\right)+v
=\lambda\frac{v}{1+x^2}.
\tag{5}
\]

Let `lambda_w` be the lowest eigenvalue of (5) with Neumann conditions at both endpoints,

\[
v'(0)=v'(w)=0.
\tag{6}
\]

Then, with `kappa_w=sqrt(lambda_w)`:

1. `q_w^{hyp,+}(i kappa_w)=0`;
2. this zero is simple as a zero of the analytic continuation in `xi`;
3. the Rayleigh principle gives
   \[
   1\le\lambda_w\le\frac{w}{\arctan w};
   \tag{7}
   \]
4. hence
   \[
   1\le\kappa_w\le
   \sqrt{\frac{w}{\arctan w}}
   =1+\frac{w^2}{6}+O(w^4);
   \tag{8}
   \]
5. consequently `sqrt(q_w^{hyp,+}(xi))`, chosen positive for real `xi`, cannot extend as a single-valued holomorphic function through `xi=i kappa_w` or `xi=-i kappa_w`;
6. for any fixed `epsilon>0` there is `w_epsilon>0` such that every `0<w<w_epsilon` blocks a holomorphic extension of this square root to the whole strip
   \[
   |\operatorname{Im}\xi|<1+\epsilon.
   \tag{9}
   \]

On the canonical prime-flute tail `w_n=O(P_n^{-1})`, the branch obstruction therefore lies at

\[
\kappa_{w_n}=1+O(P_n^{-2}),
\tag{10}
\]

with no fixed positive margin beyond `1`.

## 1. Imaginary Fourier frequency turns the seam problem into a regular Sturm-Liouville problem

PF-234 derives the exact intrinsic metric

\[
g=\frac{dx^2}{1+x^2}+(1+x^2)ds^2,
\]

with area form `dx ds`. Fourier transformation in the complete seam coordinate `s` gives (1). The equal-trace symmetric branch on `(-w,w)` is even, so it is enough to solve on `(0,w)` with the Neumann condition at the center and prescribed trace at the outer boundary.

For `xi=i kappa`, the tangential term changes sign and gives (5), a regular scalar Sturm-Liouville problem with

\[
p(x)=1+x^2,
\qquad
r(x)=\frac1{1+x^2},
\qquad
V(x)=1.
\tag{11}
\]

If `v_w` is the first Neumann-Neumann eigenfunction, then `v_w(w)` cannot vanish: simultaneous `v_w(w)=v_w'(w)=0` would force the solution to vanish identically. Scale it so that `v_w(w)=1`. It then satisfies the seam boundary-value problem at `xi=i kappa_w`, while its outward flux at `w` is zero. Equation (4) gives

\[
q_w^{\rm hyp,+}(i\kappa_w)=0.
\tag{12}
\]

Thus the actual seam, not an abstract comparison model, has an imaginary-frequency zero whose distance from the real axis can be estimated directly from the intrinsic PF geometry.

## 2. The principal Neumann zero approaches the flat critical point quadratically

The variational characterization of the first eigenvalue in (5)--(6) is

\[
\lambda_w
=
\inf_{u\ne0}
\frac{
\int_0^w\left((1+x^2)|u'|^2+|u|^2\right)dx
}{
\int_0^w\frac{|u|^2}{1+x^2}\,dx
}.
\tag{13}
\]

Since `(1+x^2)^{-1}<=1`, the denominator is at most `int |u|^2`, while the numerator is at least `int |u|^2`. Hence

\[
\lambda_w\ge1.
\tag{14}
\]

For the constant trial function `u=1`,

\[
\lambda_w
\le
\frac{\int_0^w dx}{\int_0^w(1+x^2)^{-1}dx}
=
\frac{w}{\arctan w}.
\tag{15}
\]

This proves (7), and the Taylor expansion of `arctan w` gives (8).

The flat PF-234 reference makes the meaning transparent. Its exact multiplier is

\[
q_w^{0,+}(\xi)
=\sqrt{1+\xi^2}\,
\tanh\!\left(w\sqrt{1+\xi^2}\right).
\tag{16}
\]

Near `xi=+-i`, the oddness of `tanh` makes (16) analytic in `1+xi^2` and gives

\[
q_w^{0,+}(\xi)=w(1+\xi^2)+O((1+\xi^2)^2),
\tag{17}
\]

so the flat DtN multiplier has a simple zero exactly at `xi=+-i`, and its square root already has the critical branch point there. Equations (7)--(8) show that the intrinsic hyperbolic seam moves that obstruction by at most `O(w^2)` rather than opening a uniform wider analytic strip.

## 3. The DtN zero is simple, so the square root really branches

The square-root obstruction requires more than `q=0`: an even-order zero could admit a holomorphic square root. Simplicity follows directly from the one-dimensional boundary problem.

Let `y(x,lambda)` solve (5) with the fixed initial normalization

\[
y(0,\lambda)=1,
\qquad
y'(0,\lambda)=0,
\tag{18}
\]

and define

\[
F(\lambda)=(1+w^2)y'(w,\lambda),
\qquad
G(\lambda)=y(w,\lambda).
\tag{19}
\]

Away from the Dirichlet poles, the continued DtN function is `m(lambda)=F(lambda)/G(lambda)`, with

\[
q_w^{\rm hyp,+}(\xi)=m(-\xi^2).
\tag{20}
\]

At `lambda=lambda_w`, one has `F(lambda_w)=0` and `G(lambda_w)\ne0`. Differentiate (5) in `lambda`. The Lagrange identity between `y` and `partial_lambda y`, using the fixed initial data and `y'(w,lambda_w)=0`, gives

\[
-(1+w^2)y(w,\lambda_w)
\,\partial_\lambda y'(w,\lambda_w)
=
\int_0^w\frac{|y(x,\lambda_w)|^2}{1+x^2}\,dx>0.
\tag{21}
\]

Therefore `F'(lambda_w)\ne0`, and hence

\[
m'(\lambda_w)\ne0.
\tag{22}
\]

Because `lambda=-xi^2` has nonzero derivative at `xi=+-i kappa_w`, equation (20) shows that both corresponding zeros of `q_w^{hyp,+}(xi)` are simple. A holomorphic function cannot have a holomorphic square root across a simple zero. Thus the real-positive branch `s_w=sqrt(q_w^{hyp,+})` must branch there.

## 4. Canonical PF widths remove every fixed supercritical strip margin

PF-234 records the canonical seam widths

\[
w_n=\kappa d_n=O(P_n^{-1}),
\tag{23}
\]

so `w_n->0`. From (8),

\[
1\le\kappa_{w_n}
\le1+O(P_n^{-2}).
\tag{24}
\]

Fix any `epsilon>0`. For all sufficiently large `n`, `kappa_{w_n}<1+epsilon`. The simple branch point `i kappa_{w_n}` then lies inside the proposed strip `|Im xi|<1+epsilon`. Therefore no branch choice of the **bare actual seam square root** can be holomorphic on that entire strip uniformly down the canonical tail.

Classical contour-shift/Paley-Wiener arguments convert suitable strip analyticity into exponential off-diagonal transform decay. PF-245 uses only the contrapositive proof-strategy boundary needed here: a uniform exponential locality argument whose sole input is a family-wide holomorphic strip of `sqrt(q_w)` cannot obtain a fixed strip margin beyond `1`, because that strip does not exist.

This statement is intentionally narrower than a general kernel lower bound. A branch point prevents the specified holomorphic-strip mechanism; it does not by itself determine every weighted operator norm or every possible microlocal estimate for the full Robin problem.

## 5. Relation to PF-243 and PF-244

PF-244 shows that abstract form information cannot prevent seam-induced high-to-low leakage. PF-245 now tests one concrete extra structure of the **actual** seam. Translation invariance makes the isolated intrinsic seam Fourier diagonal, so the artificial rank-one leakage mechanism from PF-244 is absent at this stage. But diagonalization does not automatically give the supercritical margin PF-243 needs: the square-root symbol carries a genuine complex-frequency obstruction converging to the flat mass threshold.

Hence a proof of PF-243 cannot end with the slogan "the actual seam is pseudodifferential/analytic, therefore separation gives `R>1`". It must identify where the extra gain enters the **joint** map

\[
Q^{1/2}(\Lambda_t+Q)^{-1}
\tag{25}
\]

or its source-to-bulk realization. Possible surviving mechanisms include cancellation between the zero/branch structure of `Q^{1/2}` and the Robin inverse, corridor propagation that adds decay after the seam normalization, commutator estimates tailored to the compactified `K_a` calculus rather than bare Fourier-strip analyticity, or imposing the finite physical closed-cuff trace before the complete-lift obstruction is invoked.

PF-245 does not choose among those routes. It removes one insufficient source of the desired `R>1` gain and makes the remaining proof obligation more precise.

## 6. Prior-art and novelty audit

The ingredients are classical. Regular Sturm-Liouville theory identifies separated-boundary eigenvalues through one-dimensional Weyl/Dirichlet-to-Neumann functions, and energy-parameter Dirichlet-to-Neumann maps are a standard spectral tool; a representative modern reference is J. Behrndt and J. Rohleder, *Titchmarsh-Weyl theory for Schrödinger operators on unbounded domains*, arXiv:1208.5224. Strip analyticity and transform decay are likewise classical Paley-Wiener territory; see Z. Harper, *Laplace transform representations and Paley-Wiener theorems for functions on vertical strips*, Documenta Mathematica 15 (2010), 235--254, DOI `10.4171/DM/296`.

No novelty is claimed for those general facts, for simple Sturm-Liouville eigenvalues, or for the flat multiplier (16). A targeted literature search did not identify a source making the PF-specific statement proved here: the **intrinsic hyperbolic symmetric seam** has a principal imaginary DtN zero with the explicit bracket `1<=kappa_w^2<=w/arctan w`, so its square-root analytic margin collapses to the flat critical distance along the canonical prime-flute widths. The mathematical proof of that specialization is self-contained in (1)--(24); the external references are prior-art context, not theorem dependencies.

## 7. Falsification and boundary checks

1. **Bare seam only.** The branch obstruction is for the isolated actual complete-lift symmetric seam square root. It is not automatically inherited by the full Robin Poisson map.
2. **No refutation of PF-243.** The desired separated `R>1` estimate may still hold through cancellation, corridor propagation, compactified microlocal structure, or the physical finite trace.
3. **No equivalence between strip width and every `K_a` estimate is asserted.** PF-245 rules out a direct uniform analytic-strip proof for the raw seam square root; it does not claim that all supercritical weighted estimates are impossible.
4. **Complete lift versus closed cuff.** The analytic Fourier parameter belongs to the translation-invariant complete lift used in PF-234/PF-235/PF-237. A finite periodic cuff has discrete tangential frequencies and requires a separate quantitative argument.
5. **The Rayleigh bound is one-sidedly sharp enough, not an exact eigenvalue formula.** Only `kappa_w->1` at quadratic scale is needed for the no-uniform-strip conclusion.
6. **No imported arithmetic.** Prime arithmetic enters only through the already-established canonical width decay `w_n=O(P_n^{-1})`.
7. **No RH-level conclusion.** Global weak-trace reassembly, wave/scattering theory, determinants/resonances, prime/clone separation, zeta zeros, and RH remain outside the result.

## Consequences for the research line

The actual-seam locality route survives, but in a narrower form. PF-244 says one-sided energy control is too weak; PF-245 says raw seam Fourier analyticity also has only an asymptotically critical margin. The next useful attack on the accepted Robin-homotopy clue should therefore target the **combined normalized Robin source-to-bulk operator**, not attempt to manufacture the needed fixed `R>1` solely from the standalone seam square root.

In particular, a positive result should exhibit an explicit cancellation, joint symbol estimate, compactified commutator bound, corridor-assisted decay, or finite-trace mechanism that is absent from both PF-244's abstract countermodel and PF-245's bare-seam analytic barrier. That is now the discriminating local question.