# NB-371 — Critical-line zeros force unbounded finite-dilation synthesis cost

- **Status:** proved (classical ingredients plus author derivation; independent adversarial review pending)
- **Research line:** `nyman_beurling`
- **Depends on:** NB-354 for the projected target and seed factorization; NB-356 for the lattice lift; NB-370 for the selected-component application
- **Classification:** LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION + COEFFICIENT-BUDGET-BOUNDARY

## Claim and scope

Finite lattice support does not give bounded absolute-coefficient synthesis from actual Nyman dilation generators. Every nonzero finite lattice lift used in NB-370 has a positive distance from every fixed absolute-coefficient budget in its seed orbit. The projected target itself satisfies a stronger uniform statement allowing arbitrary real seed indices, arbitrary numbers of columns, and arbitrary dilation ranges. A critical-line zero of multiplicity \(m\) forces coefficient cost at least of order \(\varepsilon^{-2m}\) as the physical error \(\varepsilon\) tends to zero.

These are necessary conditioning costs. They neither bound the number or range of dilations without a coefficient restriction nor supply an upper approximation rate. In particular they do not invalidate the closed-orbit construction.

Use
\[
H=L^2(0,1;dx),\quad e=1,\quad
g_v(x)=\{1/(vx)\}-v^{-1}\{1/x\},\quad v>1,
\qquad A_af(x)=\sqrt a f(ax)\mathbf1_{x\le1/a},\quad a\ge1.
\]
Let \(\mathcal N\) be the full continuous Nyman space, \(t=P_{\mathcal N}e\), and \(b=B(1)>0\), with the common inner factor \(B\) normalized as in NB-354. For a finite representation
\[
w=\sum_{\nu=1}^J c_\nu A_{a_\nu}g_{v_\nu},\qquad
Q=\sum_{\nu=1}^J|c_\nu|(v_\nu^{-1}+v_\nu^{-1/2}),
\qquad S=\sum_{\nu=1}^J|c_\nu|,
\tag{1}
\]
one has \(Q\le2S\). These are costs of the declared representation, not Hilbert norms. Put \(s_y=1/2+iy\). Then
\[
\boxed{\|t-w\|^2\ge\mathcal L_b(Q):=
\frac1{2\pi}\int_{\mathbb R}
\frac{[b-Q|\zeta(s_y)|]_+^2}{|s_y|^2}\,dy.}
\tag{2}
\]
For every finite \(Q\), \(\mathcal L_b(Q)>0\). More precisely, fix any critical-line zero \(\rho=1/2+i\gamma\) of multiplicity \(m\). There is a constant \(c_{\rho,b}>0\) such that every representation (1) obeys
\[
\boxed{\|t-w\|^2\ge c_{\rho,b}(1+Q)^{-1/m}.}
\tag{3}
\]
Thus \(\varepsilon=\|t-w\|\to0\) requires
\[
Q\gtrsim_{\rho,b}\varepsilon^{-2m},\qquad
S\gtrsim_{\rho,b}\varepsilon^{-2m}.
\tag{4}
\]
The weaker exponent \(2\) is unconditional without any simplicity assumption, since every zero has multiplicity at least one. All these bounds pass to the norm closure of representations with a fixed budget.

## 1. Integrate the boundary mismatch instead of evaluating a boundary point

The unitary Mellin transform has boundary norm
\[
\|\mathcal Mf\|^2=\frac1{2\pi}\int_{\mathbb R}|\mathcal Mf(s_y)|^2dy.
\]
[[research/nyman_beurling/findings/NB-354-finite-seed-real-dilation-spaces-have-an-exact-target-loss-classification|NB-354]], using [[research/prior_art/incremental/PA-burnol-nyman-projection-factorization|Burnol's projection theorem]], gives
\[
\mathcal Mt(s)=\frac{bB(s)}s,\qquad
\mathcal M(A_ag_v)(s)=a^{1/2-s}\frac{\zeta(s)}s(v^{-1}-v^{-s}).
\tag{5}
\]
On the boundary, \(|a^{1/2-s_y}|=1\), \(|B(s_y)|=1\) almost everywhere, and
\[
|v^{-1}-v^{-s_y}|\le v^{-1}+v^{-1/2}.
\]
Consequently \(|\mathcal Mw(s_y)|\le Q|\zeta(s_y)|/|s_y|\), whereas \(|\mathcal Mt(s_y)|=b/|s_y|\) almost everywhere. The reverse triangle inequality and integration prove (2). The integral is finite because its integrand is bounded by \(b^2/|s_y|^2\).

Choose \(r>0\) and \(C>0\) such that
\[
|\zeta(\rho+iu)|\le C|u|^m\quad(|u|\le r),
\qquad R=\max_{|u|\le r}|\rho+iu|.
\]
Let
\[
\delta_Q=\min\left(r,\left(\frac b{2C(1+Q)}\right)^{1/m}\right).
\]
On \(|u|\le\delta_Q\), the numerator in (2) is at least \(b^2/4\). Hence
\[
\|t-w\|^2\ge\frac{b^2\delta_Q}{4\pi R^2}
\ge\frac{b^2}{4\pi R^2}
\min\left(r,\left(\frac b{2C}\right)^{1/m}\right)(1+Q)^{-1/m}.
\tag{6}
\]
Hardy's theorem supplies critical-line zeros unconditionally. No boundary evaluation is asserted to be a bounded functional on \(H^2\). The interval width in (6) shrinks with the coefficient budget, which is precisely why no positive budget-independent distance follows.

The bounds are uniform over all representations of budget at most a fixed number. Continuity of the Hilbert norm therefore passes them to that budget-constrained norm closure. Also each column belongs to \(\mathcal N\): explicitly
\[
A_ag_v=\sqrt a\,(g_{av}-v^{-1}g_a),\qquad g_1=0.
\]
Thus the original target retains the exact orthogonal decomposition
\[
\|e-w\|^2=1-b^2+\|t-w\|^2.
\tag{7}
\]
The new cost concerns the excess above the Burnol floor, even if that floor is nonzero.

## 2. Local multiplicity constant

The local contribution to (2) also has an explicit asymptotic. Write
\[
\kappa_\rho=\frac{|\zeta^{(m)}(\rho)|}{m!}>0,\qquad
I_m=\int_0^1(1-x^m)^2dx
=\frac{2m^2}{(m+1)(2m+1)}.
\]
For any sequence of representations with \(Q_n\to\infty\),
\[
\boxed{\liminf_{n\to\infty}Q_n^{1/m}\|t-w_n\|^2
\ge\frac{b^{2+1/m}}{\pi|\rho|^2\kappa_\rho^{1/m}}I_m.}
\tag{8}
\]
Indeed, restrict (2) to \(|y-\gamma|\le h_n\), where
\(h_n=(b/(\kappa_\rho Q_n))^{1/m}\), and substitute \(y=\gamma+h_nx\). Taylor expansion at the zero gives
\(Q_n|\zeta(\rho+ih_nx)|/b\to|x|^m\) uniformly on \([-1,1]\). Dominated convergence gives (8). For a finite collection of distinct zeros of the same multiplicity, their constants add because these intervals are eventually disjoint. No infinite zero sum, optimal global constant, or matching upper bound is claimed.

## 3. A nonzero finite lattice lift cannot have bounded synthesis cost

Fix \(q,v>1\), \(L=\log q\), \(\tau=2\pi/L\), and \(z_k=1+i\tau k\). Let \(d=(d_k)\ne0\) have finite support \(E\subset\mathbb Z\), of cardinality \(D\). [[research/nyman_beurling/findings/NB-356-finite-orbit-target-assembly-is-equivalent-to-a-reciprocal-phase-series|NB-356]]'s right inverse is explicitly
\[
V(s)=R_qd(s)
=\frac{1-q^{1-s}}L\sum_{k\in E}\frac{d_k}{s-z_k}.
\tag{9}
\]
The apparent singularities at the \(z_k\) are removable; this is the Laplace transform of
\(L^{-1}e^{u/2}\sum_{k\in E}d_ke^{i\tau ku}\mathbf1_{[0,L)}(u)\).
Define the physical closed-orbit vector
\[
h=\mathcal M^{-1}(B\Theta_vV),\qquad
\Theta_v(s)=\frac{s}{s-1}\frac{1-v^{1-s}}{\sqrt v(1-v^{-s})}.
\tag{10}
\]
The rational sum in (9) is nonzero, since its residues are the nonzero data. After putting it over the common denominator \(\prod_{k\in E}(s-z_k)\), its numerator has degree at most \(D-1\). On \(\Re s=1/2\), the prefactor \(1-q^{1-s}\) never vanishes, because \(|q^{1-s}|=\sqrt q>1\). Therefore \(V\) vanishes at at most \(D-1\) distinct points of that line.

Hardy's infinitely many distinct critical-line zeros imply that some such zero \(\rho\) satisfies \(V(\rho)\ne0\). At that point \(\Theta_v\) is analytic and nonzero; its modulus on the boundary is one. For any finite same-seed synthesis
\[
h_S=\sum_\nu c_\nu A_{a_\nu}g_v,\qquad \sum_\nu|c_\nu|\le S,
\]
the boundary estimates are
\[
|\mathcal Mh(s_y)|=|V(s_y)|\quad\text{almost everywhere},\qquad
|\mathcal Mh_S(s_y)|\le S|\mathcal Mg_v(s_y)|.
\tag{11}
\]
Near \(\rho\), continuity gives \(|V(\rho+iu)|\ge A>0\), while (5) gives
\(|\mathcal Mg_v(\rho+iu)|\le C_v|u|^m\), where \(m\) is the multiplicity of this zero. Integrating (11) on
\[
|u|\le\min\left(r,\left(\frac A{2C_v(1+S)}\right)^{1/m}\right)
\]
as in (6) proves
\[
\boxed{\inf_{\sum|c_\nu|\le S}
\left\|h-\sum_\nu c_\nu A_{a_\nu}g_v\right\|^2
\ge c_{h,v,q,\rho}(1+S)^{-1/m}>0.}
\tag{12}
\]
This also holds for the norm closure of that budget ball. In particular, \(h\) is not a finite combination of the generating dilations. Nor is it a Bochner integral against a finite-total-variation measure on the dilation parameter: strong continuity of \(a\mapsto A_ag_v\), its constant norm, and finite measure tightness approximate any such integral by finite sums with the same total-variation bound. Its closed-orbit membership remains valid, with necessarily divergent coefficient budgets along convergent syntheses.

Every nonzero selected component in [[research/nyman_beurling/findings/NB-370-adaptive-lattice-selection-removes-the-three-orbit-cutoff-logarithm|NB-370]] has precisely the form (9)--(10), with \(E\subset\{\pm n:n\in\Lambda\}\) and \(d_0=0\). For each fixed selection, (12) applies without a bad-approximation assumption. The selected zero and constant may depend on the data; no uniform component lower bound as \(\Lambda\) grows is inferred from this root count.

## Consequence for the finite-generator frontier

Suppose the NB-370 construction, including its anchor, is replaced by actual finite dilation sums \(w_M\) with total error \(\|t-w_M\|=O(M^{-1/2})\). Equation (4), applied at one fixed critical-line zero, forces
\[
S_M=\Omega(M),
\tag{13}
\]
and \(S_M=\Omega(M^m)\) if that zero has multiplicity \(m\). This bound does not deteriorate with the selected lattice set because it concerns the final projected target, not individual components. It allows all seed choices and all dilation ranges.

If the representation uses \(J_M\) columns and has coefficient Euclidean norm at most \(C_M\), then \(S_M\le\sqrt{J_M}C_M\). Thus (13) requires \(J_MC_M^2\gtrsim M^2\); a uniform Euclidean coefficient bound would require at least order \(M^2\) columns. Without a coefficient restriction there is no column-count conclusion. No lower bound on maximal dilation follows.

The phase-only adaptive selector therefore cannot by itself certify well-conditioned finite synthesis. Its \(\Theta(1/M)\) squared component truncation cost and finite search horizon price different resources from (1). The remaining upper-synthesis problem must permit, and quantitatively control, divergent coefficients.

## Prior art, controls, and evidence boundary

Burnol, *A note on Nyman's equivalent formulation of the Riemann Hypothesis*, [Section 2, equation (2.3) and Lemma 2.4](https://arxiv.org/pdf/math/9910055), supplies (5)'s classical Mellin and projection identities. Hardy's infinitude theorem is checked in Titchmarsh--Heath-Brown, *The Theory of the Riemann Zeta-function*, second edition (1986), [Section 10.2, pp. 256--258](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf). Only infinitude is used, not a proportion, zero-spacing estimate, simplicity, or RH.

Burnol, *A lower bound in an approximation problem involving the zeros of the Riemann zeta function*, [Theorems 1.3--1.4](https://arxiv.org/pdf/math/0103058), is the closest classical boundary-zero comparison: it prices the dilation cutoff and establishes the multiplicity-sensitive logarithmic distance bound, with a polynomial prediction model. The present budget is an absolute coefficient sum with unrestricted dilation range, and the target is the unconditional projection \(t\). Equations (2), (8), and (12) are derived directly; they neither replace nor improve Burnol's cutoff theorem. Alouges--Darses--Hillion's [Theorem 1.2](https://www.numdam.org/item/10.5802/jtnb.1227.pdf) is neighboring prior art for separating fractional-part approximation from coefficient control, not a source for the bound here.

The mechanism is classical Fourier/Mellin multiplier vanishing plus integration over a neighborhood of a zero. No new general approximation principle or bibliographic priority is claimed. The local delta is its actual-source application after finite lattice selection: finite sample lifts still require unbounded generator coefficients, and the final target gives a selection-independent necessary budget. [[research/nyman_beurling/findings/NB-353-finitely-many-seed-orbits-pay-a-quantitative-target-coefficient-cost|NB-353]] prices a different weighted cost at the one-line seed lattice; [[research/nyman_beurling/findings/NB-020-early-shell-mobius-inversion-forces-an-inverse-distance-coefficient-core|NB-020]] prices integer-section coefficients weighted by their indices; [[research/nyman_beurling/findings/NB-083-boundary-zeros-force-reciprocal-depth-screening|NB-083]] treats a stationary polynomial prediction model. None supplies (12) for these selected physical vectors.

- A boundary zero alone does not obstruct Hilbert closure. Removing the fixed budget lets the neighborhood in (6) shrink to zero.
- The inner factor is retained through \(t\) and \(b\). No assertion \(t=e\), source-only reconstruction of \(B\), or removal of the Burnol floor is made.
- The norm of a complete orbit component can stay bounded while its generating coefficient cost diverges. These currencies must not be identified.
- The exponent in (3) is a necessary lower bound, not a sharp global cost law. The constants for a moving selected component are not controlled uniformly.
- Rescaling the dictionary changes coefficient costs. The normalization of \(g_v\) and \(A_a\) above is part of the statement.

Evidence is the analytic derivation. The decisive checks are the unit-modulus boundary dilation, the shrinking interval rather than point evaluation, the retained target modulus \(b/|s|\), the finite rational numerator in (9), and fixed-target versus moving-component constants. No numerical optimum, Lean verification, independent adversarial approval, or RH advance is asserted.
