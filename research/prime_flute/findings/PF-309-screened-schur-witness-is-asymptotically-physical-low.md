# PF-309 — screened Schur witness is asymptotically physical-low

**Status:** `EXACT-DERIVED + ASYMPTOTIC-DERIVED + POSITIVE/ROUTE-NARROWING`.

PF-307 and PF-308 show that the explicit PF-217 tail screening family simultaneously forces the global constant/nonconstant Schur angle to one and makes the full killing-normalized constant Green compression diverge. The remaining question is whether the narrower physical `P/H` entrance and reassembly actually reach that bad family.

For the **specific screened family already responsible for PF-307--PF-308**, the source-side fixed physical high pass is strongly suppressing rather than amplifying. PF-217 uses smooth tangential bumps

\[
\phi_n^{(M)}(s)=z_n\,\chi\!\left(\frac{s}{R_M}\right),
\qquad
R_M=\varepsilon\log P_M,
\qquad M\le n\le2M,
\tag{1}
\]

with the same profile on the two sides of the PF-205 seam strip. For every fixed physical cutoff `\kappa>0` and every integer `r\ge1`, the corresponding normalized seam-boundary vector

\[
f_n^{(M)}=\Lambda_{Q,n}^{1/2}\Phi_n^{(M)},
\qquad
\Phi_n^{(M)}=(\phi_n^{(M)},\phi_n^{(M)}),
\tag{2}
\]

satisfies

\[
\boxed{
\|H_{\kappa,n}f_n^{(M)}\|^2
\le
C_{r,\kappa}\,w_n|z_n|^2R_M^{1-2r},
}
\tag{3}
\]

where `H_{\kappa,n}=I-P_{\kappa,n}` is the exact PF-212 fixed-physical-frequency high projection and `w_n\asymp P_n^{-1}` is the PF-205 strip halfwidth. Summing over the PF-217 block gives

\[
\boxed{
\sum_{n=M}^{2M}\|H_{\kappa,n}f_n^{(M)}\|^2
\le
C_{r,\kappa}\frac{M}{P_M}R_M^{1-2r}
=O_{r,\kappa}((\log M)^{-2r}).
}
\tag{4}
\]

Thus the physical-high seam energy of this explicit screening family tends to zero faster than any prescribed inverse power of `\log M` by choosing `r` sufficiently large. The same statement holds for its nonconstant component: the constant symmetric module mode lies inside `P_{\kappa,n}`, so removing the constant projection does not change the physical-high part.

PF-308 simultaneously gives macroscopic killing-normalized source mass for the constant projection,

\[
\langle t^{(M)},D_Mt^{(M)}\rangle\ge cM.
\tag{5}
\]

Consequently

\[
\boxed{
\frac{
\sum_{n=M}^{2M}\|H_{\kappa,n}Q_nf_n^{(M)}\|^2
}{
\langle t^{(M)},D_Mt^{(M)}\rangle
}
\le
\frac{C_{r,\kappa}}{M(\log M)^{2r}}
\longrightarrow0,
}
\tag{6}
\]

where `Q_n` denotes removal of the low-symmetric constant module direction on the `n`th seam module.

This separates two statements that had remained entangled. The full killing-normalized constant sector **does** reach a direction with divergent screened backreaction (PF-308), but the concrete nonconstant relaxation producing that divergence is asymptotically concentrated below every fixed physical-frequency cutoff. Therefore PF-308 does not itself provide a dangerous physical-high source direction for the final `P/H` response. Any failure of the final physical estimate must come from later reassembly converting this low-frequency screening into a high component, from a different family of nearly screened directions with genuine physical-high leakage, from moving-end/support effects not captured by a fixed-window source test, or from multiplicity that survives the actual source/target maps.

## 1. Representation and normalization dictionary

The statement is made in the same PF-205 simultaneous seam-cut representation used by PF-212, PF-217, and PF-306--PF-308. On the `n`th two-sided Fermi strip

\[
Q_{L_n,w_n}=(-w_n,w_n)\times(\mathbb R/L_n\mathbb Z)
\]

let `\Lambda_{Q,n}` be the positive shifted two-boundary DtN form. Its metric is tangentially translation invariant, so `\Lambda_{Q,n}`, its positive square root, and the PF-212 physical projectors are diagonal in the same Fourier blocks

\[
\xi_k=\frac{2\pi k}{L_n}.
\tag{7}
\]

Hence

\[
H_{\kappa,n}\Lambda_{Q,n}^{1/2}
=
\Lambda_{Q,n}^{1/2}H_{\kappa,n}.
\tag{8}
\]

The PF-217 trial uses a symmetric datum on the two strip boundaries. Its constant projection is the symmetric `k=0` block. For every fixed `\kappa>0`, that block lies in the physical-low projection `P_{\kappa,n}`. Therefore, if `P_n^{\rm c}` is the low-symmetric constant projection and `Q_n=I-P_n^{\rm c}`,

\[
\boxed{
H_{\kappa,n}Q_nf_n^{(M)}
=
H_{\kappa,n}f_n^{(M)}.
}
\tag{9}
\]

This is a representation-specific but exact identity; no numerical singular value is being transported between incompatible normalizations.

## 2. Smooth expanding bumps have negligible fixed physical-high tail

The cutoff `\chi\in C_c^\infty((-1,1))` in PF-217 is fixed, with `\chi=1` on a smaller central interval. The PF-217 choice of `\varepsilon` keeps the support of `\chi(s/R_M)` inside the cuff fundamental segment on the whole tail block. Periodic differentiation therefore gives, for every integer `r\ge1`,

\[
\|\partial_s^r\phi_n^{(M)}\|_2^2
=
C_r|z_n|^2R_M^{1-2r}.
\tag{10}
\]

Because every Fourier mode in the range of `H_{\kappa,n}` has `|\xi_k|>\kappa`, Parseval gives

\[
\|H_{\kappa,n}\phi_n^{(M)}\|_2^2
\le
\kappa^{-2r}
\|\partial_s^r\phi_n^{(M)}\|_2^2
\le
C_{r,\kappa}|z_n|^2R_M^{1-2r},
\tag{11}
\]

and similarly

\[
\|\partial_sH_{\kappa,n}\phi_n^{(M)}\|_2^2
\le
C_{r,\kappa}|z_n|^2R_M^{-1-2r}.
\tag{12}
\]

The key point is that the cutoff scale `R_M` grows. The PF-217 screening mode is globally nonconstant, but its tangential variation moves to physical frequencies of order `R_M^{-1}` rather than to a fixed or increasing physical-high band.

## 3. The PF-205 boundary-energy normalization preserves the decay

Let `\psi=H_{\kappa,n}\phi_n^{(M)}` and impose the symmetric datum `(\psi,\psi)` on the two strip boundaries. The extension constant in the normal coordinate is an admissible competitor for the shifted DtN energy. The exact PF-205 metric therefore gives

\[
\langle(\psi,\psi),
\Lambda_{Q,n}(\psi,\psi)\rangle
\le
Cw_n\left(
\|\psi\|_2^2+
\|\partial_s\psi\|_2^2
\right).
\tag{13}
\]

This is the same two-sided low/symmetric geometry behind PF-212's warning that no inverse power of the thin-strip width should be inserted at low physical frequency. Combining (8), (11)--(13) yields (3).

On the block `M\le n\le2M`, PF-217 chooses a discrete envelope with

\[
\sum_{n=M}^{2M}|z_n|^2\asymp M.
\tag{14}
\]

Also `w_n\asymp P_n^{-1}\le C P_M^{-1}` there. Hence

\[
\sum_{n=M}^{2M}\|H_{\kappa,n}f_n^{(M)}\|^2
\le
C_{r,\kappa}\frac{M}{P_M}R_M^{1-2r}.
\tag{15}
\]

For the canonical prime sequence, `M/P_M=O((\log M)^{-1})` and `R_M\asymp\log P_M\asymp\log M`, giving (4).

PF-307 obtains its finite Schur-angle witnesses by approximating this smooth PF-217 nonconstant trial in the positive boundary-form norm. Since `H_{\kappa}` is an orthogonal contraction on the normalized boundary-energy space, the finite tangential Galerkin cutoff can be chosen so that the same approximation preserves both the screening estimate and the vanishing physical-high leakage. Thus the angle-saturating finite sections need not acquire an artificial fixed-high-frequency component from the Galerkin truncation.

## 4. What this resolves about the current source gate

PF-291 already proves a broader fixed-window statement: precompact response profiles cannot maintain a positive optimized pairing against PF-227's fixed physical-high witness spaces. The present result is different and more specific to the live PF-307--PF-308 obstruction. It acts directly on the **explicit smooth screening family** that makes the Schur angle saturate and estimates its exact PF-212 high projection in the PF-205 boundary-energy norm.

The result identifies which PF-291 escape mechanism the known Schur witness uses. It is not increasing tangential frequency on a fixed central window. Its noncompactness is carried by the growing spatial scale of the cutoff and by the transition region moving outward with `R_M`; on every fixed central physical window the profile is eventually constant before its modulewise mean is removed, and after mean removal it is still locally constant.

Therefore the first source-adapted test has a positive answer for this one bad family:

\[
\boxed{
\text{fixed physical-high entrance suppresses the explicit PF-217/PF-308 screening witness.}
}
\tag{16}
\]

Equation (16) is deliberately not promoted to a theorem about the complete physical `P/H` response. The final response contains exterior propagation, Schur inversion, source normalization, and signed reassembly after the initial frequency split. Those later maps can generate or expose high-frequency output even when the screening competitor itself is physical-low.

## 5. Prior-art and novelty audit

No novelty is claimed for the abstract Fourier estimate. Rapid decay of the fixed-high-frequency tail of a smooth dilated cutoff follows immediately from Parseval and repeated differentiation; the surrounding finite-window time/band concentration phenomenon is classical and was already audited in PF-291 against the Slepian--Pollak literature. A targeted check of the concentration-compactness literature likewise confirms that loss of compactness through spatial escape/growing scale is classical language, not a new mechanism.

The project-specific content is the dictionary and consequence: the exact PF-217 screening family used to prove PF-307 Schur-angle saturation and PF-308 killing-normalized blowup lies asymptotically below PF-212's **physical** high cutoff even after the canonical seam-boundary energy normalization. No external theorem located in the audit identifies this prime-flute Schur witness or supplies the source/reassembly conclusion (16).

## 6. Boundaries and falsification checks

This finding does **not** show that the full `P/H` mixed response is bounded, compact, or weak trace class. It does not show that every near-unit singular direction of `C_{M,L}` is physical-low, and it gives no count of dangerous directions.

The estimate uses a **fixed physical cutoff** `\kappa`. If a later argument requires `\kappa=\kappa_M` growing so fast that `\kappa_MR_M` is no longer large in the relevant direction, the present conclusion must be recalculated rather than imported.

The estimate is for the PF-217 symmetric smooth screening competitor in the exact PF-205 seam normalization. A different interface representation or a source map that is not the PF-212 physical Fourier split requires its own dictionary. In particular, the result does not identify the high-frequency content after the full exterior Schur inverse or after final signed reassembly.

The decisive audit is direct: recheck the scaled derivative identity (10), the Fourier-block commutation (8), the constant-in-normal-direction DtN competitor (13), and PF-217's block scales (14)--(15). If any of those fail in the common PF-205 representation, (3)--(6) fail. Otherwise the suppression of this explicit screened witness by every fixed physical high pass is exact.