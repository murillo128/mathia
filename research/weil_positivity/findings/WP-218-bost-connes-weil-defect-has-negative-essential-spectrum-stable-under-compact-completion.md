# WP-218 — Bost–Connes Weil defect has negative essential spectrum stable under compact completion

**Status:** `EXACT-DERIVED + BOST-CONNES-CRITICAL-GRAM + TOEPLITZ-ESSENTIAL-SPECTRUM + COMPACT-PERTURBATION-NO-GO + FINITE-BOUNDARY-SCHUR-COMPLEMENT + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

`WP-216` identifies the source-forced critical Bost–Connes prime-axis Gram

\[
G_{1,p}(a,b)=p^{-|a-b|/2}
\]

and the finite-Weil-oriented defect

\[
W_p=\log p\,(I-G_{1,p}).
\]

`WP-217` then shows that the canonical temperature/log-density score of the same Gram is exactly the already-audited Prime-Torus Poisson score, so scalar information geometry does not create a new sign theorem. The next natural escape is to ask whether an additional finite or compact geometric sector—boundary variables, finitely many GNS constraints, a compact archimedean coupling, or a compact Schur-complement correction—can repair the sign of `W_p` without changing its critical prime-power tail.

It cannot.

Let

\[
r=p^{-1/2}\in(0,1)
\]

and realize the one-prime axis on `ell^2(N_0)`. The matrix `r^{|a-b|}` is exactly the Toeplitz operator with Poisson symbol

\[
P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2}.
\]

Therefore

\[
W_p=T(w_p),
\qquad
w_p(\theta)=\log p\,(1-P_r(\theta)).
\]

The Toeplitz extension modulo compact operators sends `T(w_p)` to the continuous symbol `w_p`. Hence

\[
\boxed{
\sigma_{\rm ess}(W_p)=w_p(\mathbb T)
=
\left[
-\frac{2(\log p)r}{1-r},
\frac{2(\log p)r}{1+r}
\right].
}
\]

In particular the essential spectrum contains a nontrivial negative interval for every prime `p`. By Weyl invariance of essential spectrum, for every compact self-adjoint correction `K`,

\[
\boxed{
\sigma_{\rm ess}(W_p+K)=\sigma_{\rm ess}(W_p),
}
\]

so `W_p+K` can never be positive semidefinite. The same conclusion holds for relatively compact perturbations in the standard self-adjoint sense.

This is stronger than the scalar diagonal-cost obstruction in `WP-216`. A compact completion is not merely too small in total mass: **it is invisible in the Calkin algebra where the wrong Weil orientation already survives as negative essential spectrum**. Thus no finite-rank boundary repair, finite-dimensional positive bath, compact GNS centering correction, or bounded finite-sector Schur complement can turn the critical Bost–Connes defect into a positive prime-axis form while preserving the same bulk operator.

The conclusion is deliberately narrow. A surviving Bost–Connes completion must change the essential prime-axis symbol itself, destroy the prime axis as an asymptotically invariant channel, or restrict the admissible test space so strongly that the negative Weyl sequences are no longer available. In particular a genuinely noncompact mixed-prime or finite–archimedean coupling remains open. Such a coupling must be source-forced and must still produce the Gamma and polar sectors rather than importing them from the Weil target.

## 1. The critical conditioned Gram is a Toeplitz operator, not only a kernel

Fix one prime `p` and write

\[
r=p^{-1/2}.
\tag{1}
\]

On the prime-power ray `1,p,p^2,...`, `WP-216` gives

\[
G_{1,p}(a,b)=r^{|a-b|},
\qquad a,b\in\mathbb N_0.
\tag{2}
\]

The Poisson kernel has Fourier expansion

\[
P_r(\theta)
=1+2\sum_{k\ge1}r^k\cos(k\theta),
\tag{3}
\]

so its Fourier coefficients satisfy

\[
\widehat P_r(k)=r^{|k|}.
\tag{4}
\]

Under the standard identification `ell^2(N_0) ~= H^2(T)`, the Toeplitz operator `T(P_r)` therefore has matrix

\[
\langle e_a,T(P_r)e_b\rangle=r^{|a-b|}.
\tag{5}
\]

Consequently

\[
\boxed{G_{1,p}=T(P_r)}
\tag{6}
\]

as a bounded positive operator. Since Toeplitz quantization is linear,

\[
\boxed{
W_p=\log p\,(I-G_{1,p})
=T(w_p),
}
\tag{7}
\]

with

\[
w_p(\theta)=\log p\,(1-P_r(\theta)).
\tag{8}
\]

This operator formulation matters because compact boundary changes disappear in the Toeplitz quotient while the sign-changing symbol does not.

## 2. The wrong orientation occupies essential spectrum

For continuous scalar symbols, the Toeplitz C*-algebra fits into the classical extension

\[
0\longrightarrow\mathcal K
\longrightarrow\mathcal T
\longrightarrow C(\mathbb T)
\longrightarrow0,
\tag{9}
\]

where the quotient map sends `T(f)` to `f`. Thus the image of `W_p` in the Calkin algebra is exactly the real continuous function `w_p`, and its essential spectrum is the range of that function.

The Poisson kernel is extremal at `theta=0` and `theta=pi`:

\[
P_r(0)=\frac{1+r}{1-r},
\qquad
P_r(\pi)=\frac{1-r}{1+r}.
\tag{10}
\]

Therefore

\[
w_p(0)
=-\frac{2(\log p)r}{1-r}<0,
\tag{11}
\]

while

\[
w_p(\pi)
=\frac{2(\log p)r}{1+r}>0.
\tag{12}
\]

Since `w_p(T)` is a connected interval,

\[
\boxed{
\sigma_{\rm ess}(W_p)
=
\left[
-\frac{2(\log p)r}{1-r},
\frac{2(\log p)r}{1+r}
\right].
}
\tag{13}
\]

Thus the negative direction found pointwise in `WP-216` is not an isolated eigenvalue that could be removed by one global constraint. It is a stable bulk phenomenon of the prime-power Toeplitz channel.

Let `K=K^*` be compact. Weyl's theorem gives

\[
\sigma_{\rm ess}(W_p+K)
=
\sigma_{\rm ess}(W_p).
\tag{14}
\]

Equations (13)--(14) imply

\[
\inf\sigma_{\rm ess}(W_p+K)
=-\frac{2(\log p)r}{1-r}<0.
\tag{15}
\]

Hence

\[
\boxed{W_p+K\not\succeq0}
\tag{16}
\]

for every compact self-adjoint `K`.

The same argument applies whenever the perturbation is relatively compact with respect to the relevant self-adjoint realization, because the essential spectrum is again unchanged.

## 3. A concrete Weyl-sequence proof shows what compactness cannot touch

The quotient argument can be seen directly. Fix a small arc around `theta=0` and take normalized Hardy-space wave packets whose Fourier coefficients occupy longer and longer intervals translated to arbitrarily high prime-power grade. They converge weakly to zero while their Toeplitz Rayleigh quotients approach the local symbol value `w_p(0)`:

\[
\langle u_N,W_pu_N\rangle
\longrightarrow
-\frac{2(\log p)r}{1-r}.
\tag{17}
\]

If `K` is compact and `u_N\rightharpoonup0`, then

\[
\|Ku_N\|\longrightarrow0,
\qquad
\langle u_N,Ku_N\rangle\longrightarrow0.
\tag{18}
\]

Therefore

\[
\langle u_N,(W_p+K)u_N\rangle
\longrightarrow
-\frac{2(\log p)r}{1-r}<0.
\tag{19}
\]

This makes the geometric content of the obstruction explicit: the bad sign can be moved arbitrarily far out along the prime-power ray. Any correction whose action becomes negligible on weakly escaping packets cannot repair it.

## 4. Finite-dimensional boundary and GNS corrections are included automatically

Several natural completions proposed after `WP-216` fall inside (16).

Suppose a finite-dimensional auxiliary sector `E` is coupled boundedly to the prime-axis Hilbert space `H_p`, and eliminating that sector produces a Schur-complement correction

\[
B A^{-1}B^*
\tag{20}
\]

with `A` invertible on `E`. Since `dim E<infinity`, the operator in (20) has finite rank and is compact. Replacing `A^{-1}` by the Moore--Penrose inverse on its support does not change that conclusion. Therefore any effective operator of the form

\[
W_p+K_p,
\qquad
\operatorname{rank}K_p<\infty,
\tag{21}
\]

retains the negative essential interval (13).

Likewise, projecting a Gram family away from finitely many GNS vectors changes its covariance by a finite-rank Gram correction. Conditioning on finitely many source-defined boundary observables, subtracting finitely many rank-one means, or adjoining finitely many archimedean coordinates can alter isolated eigenvalues and finite-dimensional inertia, but it cannot reverse the bulk Toeplitz orientation.

The conclusion extends beyond finite rank: any source construction whose induced correction on the prime ray is compact has the same failure. The relevant dividing line is therefore **compact versus essential**, not merely finite versus infinite dimension.

## 5. This does not rule out a genuinely global completion

The theorem does not say that every archimedean or mixed-prime mechanism fails. It isolates what such a mechanism must do.

A possible survivor must violate at least one hypothesis behind (14). Concretely it must do one of the following:

1. induce a noncompact, translation-persistent correction on the prime-power ray, thereby changing the Calkin symbol;
2. couple different prime rays before compression so that no individual `W_p` remains an asymptotically invariant Toeplitz channel;
3. use an infinite-dimensional real-place sector whose coupling changes essential spectrum rather than only discrete spectrum;
4. impose a source-forced test-space constraint that removes the negative Weyl sequences, with that constraint itself surviving the Weil admissibility and matched-control tests.

Merely enlarging the Hilbert space is not enough. The extra geometry must reach the same escaping prime-power packets on which the negative symbol is realized.

This is compatible with `WP-217`: scalar Bochner/log-density scoring changes representation but not the missing positivity theorem, whereas `WP-218` shows that compact operator-theoretic completion is also too weak. The remaining Bost–Connes branch is therefore forced toward a genuinely noncompact relational completion.

## 6. Matched controls and arithmetic specificity

Nothing in the essential-spectrum calculation uses primality beyond the source-selected parameter

\[
r=p^{-1/2}\in(0,1).
\]

For any abstract generator with critical radius `0<r<1`, the defect

\[
I-T(P_r)
\]

has essential spectrum

\[
\left[-\frac{2r}{1-r},\frac{2r}{1+r}\right].
\tag{22}
\]

Thus the no-go survives generalized-prime and arbitrary positive-length controls whenever they preserve the same Poisson prime-axis geometry. This is a feature, not a weakness, for the present result: `WP-218` is an obstruction theorem about the completion category, not a candidate arithmetic positivity mechanism.

A future positive construction must therefore do more than evade compactness. It must also fail on source-compatible generalized controls, generate the finite Mangoldt orientation and real-place Gamma contribution in one declared form, and obtain nonnegativity from an independent geometric theorem rather than from the target explicit formula.

## 7. Prior-art and novelty audit

The operator theory used here is classical.

- L. A. Coburn, **“The C*-algebra generated by an isometry,”** *Bulletin of the American Mathematical Society* **73** (1967), 722–726, DOI `10.1090/S0002-9904-1967-11845-7`. Coburn's Toeplitz extension identifies the continuous symbol modulo compact operators.
- Standard Toeplitz theory then gives the essential spectrum of a self-adjoint Toeplitz operator with real continuous symbol as the range of that symbol; equivalently this follows immediately by taking the spectrum in the Calkin quotient `T(C(T))/K ~= C(T)`.
- Weyl's classical perturbation theorem says that compact self-adjoint perturbations preserve essential spectrum; the same principle extends to relatively compact perturbations under the usual hypotheses.
- J.-B. Bost and A. Connes, **“Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory,”** *Selecta Mathematica* **1** (1995), 411–457, DOI `10.1007/BF01589495`, supplies the established Bost–Connes system underlying the source construction.

The web/literature audit found no prior source asserting the specific Mathia conclusion proved here: that the `WP-216` critical Bost–Connes/Weil defect has a negative essential Toeplitz interval which makes every compact completion sign-inert. No novelty claim is made for the Toeplitz, Calkin, Weyl, Poisson, Bost–Connes, or Weil ingredients themselves. The contribution is the exact reduction of this current candidate completion family to those classical theorems.

Nearby prior art also warns against overclaiming. Connes--Consani's archimedean Weil-positivity work uses nontrivial phase-space cutoff/compression and Toeplitz analysis; it is not a compact correction of the prime-axis operator considered here. Therefore (16) is not a no-go for the Connes/trace/Sonin class as a whole and must not be represented as one.

## 8. Research disposition

This result passes the substantive-finding gate as a decisive negative for a broad and natural post-`WP-216` completion family.

The implication now excluded is

\[
\boxed{
\text{critical Bost--Connes Weil defect}
+\text{compact geometric/boundary completion}
\not\Rightarrow
\text{positive Weil form}.
}
\]

The obstruction is stronger than failure of one regularization: negative orientation lives in essential spectrum and is therefore stable under every compact perturbation. The surviving research question is correspondingly sharper: **can the Bost–Connes source force a noncompact mixed-prime or finite–archimedean operation that changes the essential prime-ray geometry and simultaneously supplies the Gamma/polar sectors with an independent sign theorem?**
