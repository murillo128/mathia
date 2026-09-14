# PF-335 — completed translation commutators inherit Hilbert–Schmidt control from the normalized pant insertion

**Status:** `EXACT-DERIVED + HILBERT-SCHMIDT-COMMUTATOR-TRANSFER + CONDITION-NUMBER-FREE + ROUTE-SHARPENING`.

PF-332 identifies the completed low whitening map

\[
F=\bigl(Q+\Lambda_{LL}\bigr)^{1/2}Q^{-1/2}
\]

and proves that its physical-translation defect is a resolvent-dressed version of the pant/core defect. PF-334 then shows that the same relative square-root map is dimension-free in Hilbert--Schmidt norm, even though PF-333 rules out a dimension-free generic operator-norm perturbation theorem.

Those two observations combine more sharply than the raw resolvent formula suggests. Put

\[
K=Q^{-1/2}\Lambda_{LL}Q^{-1/2}\ge0,
\qquad
\Phi_Q(K)
:=\bigl(Q^{1/2}(I+K)Q^{1/2}\bigr)^{1/2}Q^{-1/2}.
\]

Thus `F=\Phi_Q(K)`. If `V` is any unitary commuting with `Q`, then on every finite section

\[
\boxed{
\|[F,V]\|_{\mathcal S_2}
\le
\frac{\sqrt{1+\|K\|}}{\sqrt2}
\|[K,V]\|_{\mathcal S_2}.
}
\tag{1}
\]

More generally, if `X=X^*` is bounded and commutes with `Q`,

\[
\boxed{
\|[F,X]\|_{\mathcal S_2}
\le
\frac{\sqrt{1+\|K\|}}{\sqrt2}
\|[K,X]\|_{\mathcal S_2}.
}
\tag{2}
\]

The constants are independent of the retained dimension and of the condition number of `Q`. For the PF-325 physical translations, which commute with the seam block,

\[
[K,\tau_t]
=Q^{-1/2}[\Lambda_{LL},\tau_t]Q^{-1/2},
\]

so (1) removes the apparently singular terminal factor `Q^{-1/2}` from PF-332's commutator formula after the defect is measured in the natural seam-energy-normalized variable.

This still does **not** prove Prime-Flute locality. It replaces the translation branch of the completed square-root problem by a cleaner one: under a uniform envelope `\|K_n\|\le M`, it is enough to prove a Hilbert--Schmidt translation-commutator estimate for the normalized pant insertion itself. In particular,

\[
\sup_{t\in I_n}\|[K_n,\tau_t]\|_{\mathcal S_2}=o(1)
\quad\Longrightarrow\quad
\sup_{t\in I_n}\|[F_n,\tau_t]\|=o(1),
\tag{3}
\]

and PF-331 then gives the same `o(1)` translation compatibility for the completed polar unitary. No logarithmic-rank or seam-conditioning loss is created by the relative square root in this transfer.

## 1. A finite-difference Hilbert--Schmidt bound for the relative square-root map

Let `K_0,K_1\ge0` and set

\[
K_s=(1-s)K_0+sK_1,
\qquad
D=K_1-K_0=D^*,
\qquad 0\le s\le1.
\]

Define

\[
A_s=Q^{1/2}(I+K_s)Q^{1/2},
\qquad
F_s=A_s^{1/2}Q^{-1/2}=\Phi_Q(K_s).
\]

Because `K_s\ge0`, one has `A_s\ge Q`. Put

\[
E_s=A_s^{-1/2}Q^{1/2}DQ^{1/2}A_s^{-1/2}
=C_sDC_s^*,
\qquad
C_s=A_s^{-1/2}Q^{1/2}.
\]

The order `A_s\ge Q` gives

\[
C_sC_s^*=A_s^{-1/2}QA_s^{-1/2}\le I,
\]

hence

\[
\|E_s\|_{\mathcal S_2}\le\|D\|_{\mathcal S_2}.
\tag{4}
\]

PF-334's exact relative derivative estimate applies because `E_s=E_s^*`:

\[
\left\|\frac{dF_s}{ds}\right\|_{\mathcal S_2}
\le
\frac1{\sqrt2}
\|E_s\|_{\mathcal S_2}\,\|F_s\|.
\tag{5}
\]

Also

\[
F_s^*F_s=I+K_s,
\]

so, with

\[
M=\max\{\|K_0\|,\|K_1\|\},
\]

convexity of the operator norm gives

\[
\|F_s\|=\sqrt{1+\|K_s\|}
\le\sqrt{1+M}.
\tag{6}
\]

Integrating (5), using (4)--(6), yields the finite-difference estimate

\[
\boxed{
\|\Phi_Q(K_1)-\Phi_Q(K_0)\|_{\mathcal S_2}
\le
\frac{\sqrt{1+M}}{\sqrt2}
\|K_1-K_0\|_{\mathcal S_2}.
}
\tag{7}
\]

This is the useful nonlinear form. It is relative to the normalized positive insertions and contains neither the smallest eigenvalue nor the condition number of `Q`.

## 2. Equivariance converts finite differences into commutators

Let `V` be unitary and `[V,Q]=0`. Then

\[
Q^{1/2}(I+VKV^*)Q^{1/2}
=V\,Q^{1/2}(I+K)Q^{1/2}V^*,
\]

and functional calculus gives the exact equivariance

\[
\Phi_Q(VKV^*)=V\Phi_Q(K)V^*.
\tag{8}
\]

Apply (7) with

\[
K_0=K,
\qquad
K_1=VKV^*.
\]

The two endpoints have the same operator norm, and unitary invariance of the Hilbert--Schmidt norm gives

\[
\begin{aligned}
\|\Phi_Q(VKV^*)-\Phi_Q(K)\|_{\mathcal S_2}
&=\|VF-FV\|_{\mathcal S_2},\\
\|VKV^*-K\|_{\mathcal S_2}
&=\|VK-KV\|_{\mathcal S_2}.
\end{aligned}
\]

Equation (1) follows.

If `X=X^*` and `[X,Q]=0`, take `V_t=e^{itX}` in (1), divide by `|t|`, and let `t\to0`. Finite-dimensional differentiability gives

\[
\frac{e^{itX}Fe^{-itX}-F}{t}\to i[X,F],
\qquad
\frac{e^{itX}Ke^{-itX}-K}{t}\to i[X,K]
\]

in Hilbert--Schmidt norm, proving (2).

A useful special case is a projection `P` commuting with `Q`. Since `K=K^*`,

\[
\|[K,P]\|_{\mathcal S_2}^2
=2\|(I-P)KP\|_{\mathcal S_2}^2.
\]

Therefore (2) implies

\[
\boxed{
\|(I-P)FP\|_{\mathcal S_2}
\le
\sqrt{1+\|K\|}\,
\|(I-P)KP\|_{\mathcal S_2}.
}
\tag{9}
\]

Thus any seam-energy spectral decomposition that commutes with `Q` inherits an off-diagonal Hilbert--Schmidt estimate from the normalized insertion without a rank factor. Spatial cutoffs generally do not commute with `Q`, so (9) must not be misread as the fixed-window locality theorem still needed for the strongest PF-328 obstruction.

## 3. Consequence for the PF-325/PF-331 translation branch

For the completed Prime-Flute low block,

\[
K_n=Q_{L,n}^{-1/2}\Lambda_{LL,n}Q_{L,n}^{-1/2}\ge0,
\qquad
F_n=\Phi_{Q_{L,n}}(K_n).
\]

PF-325's physical translations satisfy

\[
[Q_{L,n},\tau_t]=0.
\]

Hence (1) becomes

\[
\boxed{
\|[F_n,\tau_t]\|_{\mathcal S_2}
\le
\frac{\sqrt{1+\|K_n\|}}{\sqrt2}
\left\|
Q_{L,n}^{-1/2}[\Lambda_{LL,n},\tau_t]Q_{L,n}^{-1/2}
\right\|_{\mathcal S_2}.
}
\tag{10}
\]

If `\sup_n\|K_n\|<\infty`, then the completed square-root translation problem has exactly the same asymptotic Hilbert--Schmidt scale as the normalized pant translation defect. In particular, no separate factor involving the shrinking seam eigenvalue or the retained rank appears in (10).

Because `\|T\|\le\|T\|_{\mathcal S_2}`, an `o(1)` right-hand side in (10) gives the operator-norm translation compatibility required by PF-331. Its polar estimate then yields

\[
\sup_{t\in I_n}\|[U_{L,n},\tau_t]\|=o(1)
\]

on any critical interval `I_n` for which the normalized insertion commutator is uniformly Hilbert--Schmidt small.

This does not by itself complete the packet obstruction. PF-331 already notes that translation compatibility transports one reference profile but does not prove that the reference profile is physically concentrated. The stronger fixed-window cutoff route remains separate because those cutoffs do not commute with `Q`. Nor does (10) prove that the completed raw correlation stays bounded below in either PF-324 arithmetic terminal regime.

## Prior-art and novelty audit

The surrounding operator theory is classical. E. B. Davies, *Lipschitz Continuity of Functions of Operators in the Schatten Classes*, J. London Math. Soc. (2) 37 (1988), 148--157, DOI `10.1112/jlms/s2-37.121.148`, proves Schatten-`p` Lipschitz results for functions of self-adjoint operators. Birman and Solomyak's double-operator-integral framework is a standard source for Hilbert--Schmidt functional-calculus difference and commutator estimates; see M. Sh. Birman and M. Z. Solomyak, *Double Operator Integrals in a Hilbert Space*, Integral Equations Operator Theory 47 (2003), 131--168, DOI `10.1007/s00020-003-1157-8`. Mathias's 1997 relative matrix-square-root result and Li's 2005 graded positive-polar analysis, already audited in PF-333/PF-334, cover the neighboring relative-perturbation setting.

No new general functional-calculus theorem is claimed. Equation (7) is derived directly from PF-334's project-specific relative derivative in the exact congruence variable used by PF-332. The targeted prior-art check did not identify a source stating the Prime-Flute specialization (10), nor a theorem that by itself supplies the degeneration-uniform normalized pant commutator required here. The project-specific contribution is the reduction of the completed translation-locality gate to the seam-energy-normalized pant insertion with a dimension- and condition-number-free `S_2` transfer.

No external theorem is imported as a proof dependency for (7)--(10), so `SOURCES.md` acquires no new theorem dependency.

## Boundaries and adversarial checks

1. **A uniform `\|K_n\|` envelope remains load-bearing.** The transfer constant grows like `\sqrt{1+\|K_n\|}`. PF-335 does not prove that the actual pant/core normalized insertion has a uniform operator bound.
2. **The normalized insertion commutator is still unproved.** Equation (10) relocates the estimate; it does not establish reciprocal-prime or `o(1)` Hilbert--Schmidt decay for `Q^{-1/2}[\Lambda_{LL},\tau_t]Q^{-1/2}`.
3. **Translation locality is weaker than fixed-window locality.** Physical translations commute with `Q`; spatial cutoffs generally do not. The PF-328 obstruction still needs a localized reference profile, or the stronger cutoff/off-diagonal estimate, before physical packet concentration is known after completion.
4. **The PF-318 endpoint is not closed.** The direct-angle low/high block is not automatically the full `K_n` or its translation commutator. PF-318's local cross-block Hilbert--Schmidt budget remains a separate upper-bound route.
5. **Finite sections are the exact setting.** Passing the estimate to the infinite boundary realization requires the compatible limiting control already left open by PF-329--PF-334.
6. **No lower bound for completed correlation is proved.** The finite-boundary and escaping-boundary PF-324 regimes remain to be tested only after spatial transfer is established.
7. **No scattering/determinant theorem, zeta-zero correspondence, critical-line result, or RH implication follows.**

## Consequence for the research line

The completed translation-locality problem no longer needs to be attacked through PF-332's weighted resolvent integral directly. Under a uniform normalized insertion envelope, it is enough to prove

\[
\sup_{t\in I_n}
\|[K_n,\tau_t]\|_{\mathcal S_2}=o(1),
\qquad
K_n=Q_{L,n}^{-1/2}\Lambda_{LL,n}Q_{L,n}^{-1/2},
\]

on the PF-328 critical interval. PF-335 transfers that estimate to `F_n` without retained-rank or seam-conditioning loss, and PF-331 transfers it further to the completed polar rotation. The remaining obstruction-side work is therefore geometric/PDE control of the **normalized pant insertion** plus concentration of one completed reference profile, not a generic square-root or polar perturbation problem.