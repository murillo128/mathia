# MI-001 — Farey transfer is governed by source coherence plus a separate multiplicative-recurrence constraint after the normalization ledger is paid

**Evidence level:** supported by exact source/occupation reductions through FD-067 plus the cited all-short-interval Möbius theorem; no positive global occupation theorem is claimed.

The cumulative Farey obstruction is controlled by the physical shell source

\[
c(n)=\Delta\mathcal H(n)=\sum_{dm=n}\frac{\mu(m)}d.
\]

FD-054--FD-058 separate deterministic transfer, genuine short-interval cancellation, sparse represented-start sampling, and maximal ambient-window localization. FD-059 identifies the deterministic critical host scale `Q_X=X/A_X`, where `A_X=|\mathcal H(X)|`: favorable squarefree hosts at `q\asymp Q_X` force a nearby nonsquarefree row that retains a fixed fraction of the spike. FD-060 shows that subpower slack can be spent on packet multiplicity.

FD-062--FD-063 show that physical short-interval cancellation changes the geometry and removes combinatorial host scarcity. FD-064 then classifies the larger power-gap family. On a zero-frontier spike `A_X=X^{\Theta+o(1)}`, hosts `q\asymp X^\lambda` can support polynomial packets, but after paying the later horizon the optimized loss retains the exact `\Theta=2/3` crossover. FD-065 shows that moving the Schur head cannot repair the pointwise ledger: the denominator saving and scalar-leverage loss carry the same head penalty.

FD-066 exposes the invariant source-side quantity hidden in those coordinates. Assume the source spike stays comparable on a backward window

\[
L_X=X^{\ell+o(1)}.
\]

Reciprocal-floor geometry turns that window into `K_X=X^{\lambda+\ell-1+o(1)}` nearby rows. After the generic zero-frontier denominator and Schur scalarization are included, the direct coherent packet and deterministic terminal obstruction differ by the exact power

\[
\boxed{\gamma_{\rm coh}-\gamma_{\rm term}
=\frac{2-2\Theta-\ell}{1+\lambda}.}
\]

Therefore the direct packet improves the terminal scalar obstruction **iff**

\[
\boxed{\ell>2(1-\Theta).}
\]

Host exponent and Schur-head exponent cannot change the sign. Their apparent freedoms are bookkeeping transformations inside a fixed source-coherence budget. The present all-short-interval input supplies coherence only for fixed `\ell<\Theta`, so below two thirds the missing source theorem is qualitatively stronger than “shorter intervals”: it needs source-relative variation `o(A_X)` across a window longer in power scale than the spike amplitude itself, or another mechanism that bypasses this direct ledger.

FD-067 reveals a second, genuinely cross-scale fact that is invisible to the pointwise exponent comparison. For every nonsquarefree `q>1`,

\[
U_{H,D}\ge w(q)E_{\lfloor H/q\rfloor,\lfloor D/q\rfloor},
\qquad w(q)=\frac{J_2(q)}{q^2}.
\]

Along a `q`-adic horizon chain `H_j=q^jH_0`, any head schedule satisfying `floor(D_j/q)<=D_(j-1)` therefore obeys the exact product law

\[
\prod_{j=1}^n\nu_j
\ge w(q)^n\frac{E_0}{E_n},
\qquad
\nu_j=\frac{U_{H_j,D_j}}{E_{H_j,D_j}}.
\]

For polynomial heads `D_j=H_j^{\delta+o(1)}`, the zero-frontier envelope gives

\[
\liminf_{n\to\infty}
\left(\prod_{j=1}^n\nu_j\right)^{1/n}
\ge
w(q)q^{-\{\delta+2\Theta(1-\delta)\}}.
\]

Consequently a positive lower proportion of every such fixed dilation chain has scalar Schur loss `\mathfrak D_{H_j,D_j}\gg1/D_j`. Head growth may weaken the scalar leverage, but it cannot create an **all-scale escape on one multiplicative ray**. At linear head and `q=4`, the occupation lower bound is the `\Theta`-independent constant `3/16`.

This recurrent theorem does not contradict the FD-066 pointwise barrier. A zero-frontier spike sequence may select different multiplicative rays at successive scales, so positive-density good scales on each fixed ray do not force the adaptive spikes to land on them. The new distinction is therefore: **source coherence controls direct local transfer, while multiplicative recurrence controls how completely the defect can escape across scales**. Neither is reducible to host count or head location.

A genuine escape must change a load-bearing currency: prove source-relative coherence beyond `2(1-Theta)`, couple adaptive spike localization to one or a controlled family of dilation rays, obtain a cross-ray recurrence strong enough to prevent ray hopping, exploit source/denominator correlation at the same horizon, or use another interaction that avoids the direct reciprocal-floor/horizon ledger.

**Boundary.** FD-066 is a conditional classification of direct coherent packets inside the current zero-frontier denominator and Schur scalarization. FD-067 is a recurrent fixed-dilation-chain statement, not a pointwise all-horizon gap and not a localization theorem for adaptive zero-frontier spikes. Neither gives a new zero-free region or RH proof.