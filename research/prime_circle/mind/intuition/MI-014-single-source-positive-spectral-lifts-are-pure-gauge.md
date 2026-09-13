# MI-014 — Complete single-source torus spectralizations are gauge/permutation quotients

**Evidence level:** exact for fixed source-independent positive/Hermitian wrappers through [PC-278](../../findings/PC-278-single-source-dual-window-phase-spectra-are-diagonal-unitary-pure-gauge.md), and for arbitrary anchored pointwise nonlinearities on the complete coefficient torus through [PC-279](../../findings/PC-279-full-dual-torus-anchor-nonlinearities-are-source-blind-fourier-data.md). Truncated non-invariant windows, genuine flux, cross-source/cross-level couplings and other constructions outside these equivalences remain open.

For a fixed coefficient mask, the single-source dual phase field

`W_(p,r)(h,k)=A_(h,k) zeta_q^(hp+kr)`

factorizes as `D_p A E_r`. Hence every singular value, Schatten norm, rank and Gram spectrum is exactly source-independent. The analogous Hermitian coefficient-graph phase is a discrete gradient, so the source modulation is a unitary conjugacy with zero cycle holonomy.

PC-279 shows that anchoring/nonlinearity alone does not escape once both coefficient axes are complete. For any function `f: Z/qZ -> C`, including discontinuous source-selected thresholds,

`M_(p,r)^f(h,k)=f(hp+kr)`

is obtained from `M_(1,1)^f` by permuting rows by multiplication with `p` and columns by multiplication with `r`. Its entire singular spectrum is

`{|f_hat(j)| : j mod q}`.

Thus a genuinely source-dependent entrywise threshold can still have exactly universal positive spectral data. Likewise a full translation-invariant Hermitian kernel depending only on `(u-v).(p,r)` has only the Fourier modes parallel to the source direction as nonzero modes, with a source-independent eigenvalue multiset.

The two collapses are different but complementary. PC-278 removes phase modulation by **unitary gauge** when the mask/kernel is fixed. PC-279 removes arbitrary anchored scalar profiles by **index permutation** when the coefficient torus is complete. Merely putting a nonlinear selector between the raw phase field and a positive spectrum does not create a Prime-Circle carrier if the complete domain still lets source multiplication relabel everything.

The surviving finite-window near-resonance mechanism has a precise source of information: a truncated box such as `|h|,|k|<=B<q/2` is not preserved by multiplication by `p,r`. Restriction converts what was a pure relabeling on the full torus into a source-dependent boundary/intersection problem. The potential carrier is therefore the **mismatch between the distinguished window and the source permutation**, not the local profile `f` itself.

**Research consequence.** Before spectralizing a richer single-source observable, identify the symmetry that remains on its full domain. To escape the current no-go family one must break complete-domain relabeling or gauge before the invariant is taken—for example through a source-sensitive non-invariant window, genuine cycle flux, or a relative/cross-level construction with no single relabeling that removes all source data—and then audit that residual against the strongest source-only control.

**Boundary.** PC-279 does not close truncated windows or the intermediate scalar rational-microscopic regime. It also does not say every nonlinear or nonnormal construction is source-blind. It closes the complete-torus class whose source dependence factors only through the scalar phase coordinate `hp+kr`.
