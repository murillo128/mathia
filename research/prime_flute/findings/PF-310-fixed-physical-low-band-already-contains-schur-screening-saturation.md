# PF-310 — a fixed physical low band already contains Schur-screening saturation

**Status:** `EXACT-DERIVED + ASYMPTOTIC-DERIVED + PHYSICAL-BAND-LOCALIZATION + ROUTE-SHARPENING`.

PF-309 shows that the explicit compactly supported PF-217 screening family is asymptotically physical-low at entrance: every fixed physical high pass sees only a rapidly decaying tail. That still leaves a logical loophole. The PF-217 bump is not itself exactly band-limited, so one could imagine that the tiny high-frequency tail is load-bearing for the variational screening once the narrow-pant conductance factor is paid.

It is not. One can replace the compact PF-217 bump by a common Gaussian screening profile on a much smaller tangential scale

\[
R_M\asymp \sqrt{\log P_M},
\]

periodize it on each long cuff, and then truncate its Fourier series to one **fixed physical low band** `|\xi|\le\kappa`. Gaussian Fourier decay makes this truncation exponentially small in `R_M^2\asymp\log P_M`, while the Gaussian itself is concentrated far inside the growing pant corridor. After choosing one sufficiently large but fixed `\kappa`, both errors remain negligible even after the worst `s_n^{-1}\lesssim P_n` conductance loss.

The resulting boundary data are exactly physical-low on every seam, retain a constant projection of size `R_M/L_n\asymp(\log P_M)^{-1/2}`, and still screen that projection to a vanishing fraction of its raw PF-216 mass currency. Therefore the PF-307 Schur-angle saturation already occurs after restricting the complementary relaxation space to **nonconstant modes inside a fixed physical low band**. The same traces still carry PF-303 Robin-killing mass of order `M/\log P_M`, so the corresponding restricted killing-normalized constant Green block diverges as well.

Thus the bad Schur reservoir does not require physical-high boundary modes at all. PF-309's entrance filtering can be strengthened from “the known witness is asymptotically low” to the structural statement that **there are exact fixed-low-band witnesses**. Any final physical-high obstruction must therefore be created downstream: low-to-high conversion after screening, target-side reassembly, another source-accessible family, or a multiplicity/counting effect. This finding does not control those later vertices and does not prove the final mixed `P/H` response is small.

## Claim

Use the canonical PF-205 simultaneous seam cut, the normalized positive boundary form

\[
\mathfrak a[f]=\|f\|^2+\mathfrak k[f],
\]

and the constant/nonconstant split `P\oplus Q` of PF-216--PF-217. For a fixed physical cutoff `\kappa>0`, let `P_\kappa` denote the direct sum of the seamwise tangential Fourier projectors

\[
\left|\frac{2\pi k}{L_n}\right|\le\kappa,
\]

and put

\[
Q_{\le\kappa}:=Q P_\kappa .
\]

Because the PF-205 strip metric is translation invariant in the tangential coordinate, `P_\kappa` commutes with the strip DtN form and its positive square root. Hence physical Fourier support may be checked before or after the canonical `\Lambda_Q^{1/2}` normalization.

There exists a finite cutoff `\kappa_0` such that for every fixed `\kappa\ge\kappa_0` there are tail-block constant vectors `x^{(M)}` supported on `M\le n\le2M` and exact relaxations

\[
y^{(M)}\in Q_{\le\kappa}\operatorname{Dom}(\mathfrak a)
\]

for which, writing

\[
\mathfrak m_0[x]
=\sum_n\frac{|x_n|^2}{q_n},
\]

one has

\[
\boxed{
\mathfrak m_0[x^{(M)}]\asymp \frac{M}{\log P_M}
}
\tag{1}
\]

and

\[
\boxed{
\frac{\mathfrak a[x^{(M)}+y^{(M)}]}
{\mathfrak m_0[x^{(M)}]}
\longrightarrow0.
}
\tag{2}
\]

Consequently the restricted shorted form

\[
\mathfrak s_{\le\kappa}[x]
:=
\inf_{y\in Q_{\le\kappa}\operatorname{Dom}(\mathfrak a)}
\mathfrak a[x+y]
\tag{3}
\]

satisfies

\[
\boxed{
\inf_{x\ne0}
\frac{\mathfrak s_{\le\kappa}[x]}
{\mathfrak m_0[x]}=0.
}
\tag{4}
\]

Let `C^{\le\kappa}_M` be the normalized Schur conversion in a finite tail section between the cuff-constant variables and the retained nonconstant physical-low modes. Then

\[
\boxed{
\|C^{\le\kappa}_M\|\longrightarrow1
}
\tag{5}
\]

along a sequence of tail sections.

In physical cuff-constant coordinates let `D_M` be PF-303's Robin-killing diagonal and `H^{\mathrm{eff},\le\kappa}_M` the constant form after shorting only `Q_{\le\kappa}`. The same witnesses satisfy

\[
\boxed{
\langle t^{(M)},D_Mt^{(M)}\rangle
\asymp \frac{M}{\log P_M},
\qquad
\langle t^{(M)},H^{\mathrm{eff},\le\kappa}_Mt^{(M)}\rangle
=o\!\left(\frac{M}{\log P_M}\right),
}
\tag{6}
\]

and therefore

\[
\boxed{
\left\|
D_M^{1/2}
(H^{\mathrm{eff},\le\kappa}_M)^{-1}
D_M^{1/2}
\right\|\longrightarrow\infty.
}
\tag{7}
\]

The cutoff in this theorem is one fixed physical cutoff, independent of `M`. The statement does **not** claim (4)--(7) for every arbitrarily small prescribed `\kappa`; PF-212 permits choosing any fixed physical cutoff in the low/high decomposition, and the construction spends that freedom once.

## 1. A common Gaussian has the right screening scale

Put

\[
\mathcal L_M:=\log P_M,
\qquad
R_M:=\sqrt{\eta\mathcal L_M},
\tag{8}
\]

where `\eta>0` will be fixed sufficiently small. On the block `M\le n\le2M`, PF-217 gives

\[
c\mathcal L_M\le L_n\le C\mathcal L_M,
\qquad
P_n^{-1}\lesssim s_n\lesssim P_n^{-0.475},
\tag{9}
\]

uniformly after a finite head. In particular

\[
R_M\to\infty,
\qquad
\frac{R_M}{L_n}\asymp \mathcal L_M^{-1/2}\to0.
\tag{10}
\]

Use the same real-line Gaussian at every cuff origin,

\[
g_M(t)=\exp\!\left(-\frac{t^2}{2R_M^2}\right),
\tag{11}
\]

and the PF-217 discrete sine envelope

\[
z_n=
\sin\!\left(\frac{\pi(n-M)}{M}\right)
\quad(M\le n\le2M).
\tag{12}
\]

Before imposing exact Fourier support, the common profile `z_ng_M` has the same narrow-gap advantage as PF-217's compact bump. The transverse interpolation term still pays

\[
\frac{|z_{n+1}-z_n|^2}{s_n}
\int_{\mathbb R}\frac{g_M(t)^2}{\cosh t}\,dt
\le
C\frac{|z_{n+1}-z_n|^2}{s_n},
\tag{13}
\]

because the integral is uniformly bounded. Summing with PF-217's `s_n^{-1}\lesssim M\log M` and

\[
\sum |z_{n+1}-z_n|^2=O(M^{-1})
\]

gives the same `O(\log M)` block conductance budget.

The positive-shift same-sign term is even easier to estimate explicitly. Completing the square gives

\[
\begin{aligned}
 s_n\int_{\mathbb R}
 \cosh t\,g_M(t)^2\,dt
&\le
C s_n\int_{\mathbb R}
 e^{|t|-t^2/R_M^2}\,dt\\
&\le C s_n R_M e^{R_M^2/4}.
\end{aligned}
\tag{14}
\]

Choose `\eta<1`, for example. By (8)--(9),

\[
s_nR_Me^{R_M^2/4}
\le
C R_M P_M^{-(0.475-\eta/4)}
=P_M^{-\delta+o(1)}
\tag{15}
\]

for some fixed `\delta>0`. Tangential derivatives introduce only an additional `R_M^{-2}` factor. Thus the Gaussian occupies a tangential scale tending to infinity, but still so far inside the growing pant corridor that the PF-216 same-sign floor disappears.

The point of using `R_M\asymp\sqrt{\log P_M}` rather than PF-217's `R_M\asymp\log P_M` is not geometric. It creates enough simultaneous spatial and Fourier concentration to survive an **exact fixed physical low-pass**.

## 2. Periodization and fixed physical low-pass cost only a polynomially tiny error

For the `n`th cuff periodize the common Gaussian,

\[
G_{n,M}(t)
:=
\sum_{j\in\mathbb Z}
\exp\!\left(-\frac{(t+jL_n)^2}{2R_M^2}\right).
\tag{16}
\]

Poisson summation gives the exact Fourier series

\[
\boxed{
G_{n,M}(t)
=
\frac{\sqrt{2\pi}R_M}{L_n}
\sum_{k\in\mathbb Z}
\exp\!\left(-\frac{R_M^2\xi_{n,k}^2}{2}\right)
 e^{i\xi_{n,k}t},
\qquad
\xi_{n,k}=\frac{2\pi k}{L_n}.
}
\tag{17}
\]

Define the exact physical-low profile

\[
b_{n,M}:=P_{\kappa,n}G_{n,M}.
\tag{18}
\]

Then

\[
P_{\kappa,n}b_{n,M}=b_{n,M}
\tag{19}
\]

exactly, while the zero Fourier coefficient is untouched:

\[
\boxed{
\frac1{L_n}\int_0^{L_n}b_{n,M}(t)\,dt
=
\frac{\sqrt{2\pi}R_M}{L_n}.
}
\tag{20}
\]

The omitted Fourier tail has Gaussian decay. Uniformly on the block, standard comparison of the Fourier sum with its Gaussian integral gives

\[
\|G_{n,M}-b_{n,M}\|_{C^1}
\le
C_\kappa e^{-c\kappa^2R_M^2}
=
O(P_M^{-A_\kappa}),
\tag{21}
\]

where `A_\kappa>0` grows quadratically with the fixed cutoff. Periodic-image errors near the common-perpendicular region likewise obey `O(P_M^{-A_{\rm per}})` after `\eta` is fixed sufficiently small, because `L_n/R_M\asymp\sqrt{\mathcal L_M}`.

The dangerous place for an approximation error is the transverse pant term, where one may pay `s_n^{-1}\lesssim P_n`. Fix `\eta` first so that the periodic-image error has exponent larger than one after squaring and paying this loss; then choose one finite `\kappa_0` so that for every `\kappa\ge\kappa_0` the same is true of (21). With that choice, replacing the common Gaussian by the exact low-band profiles changes the complete block trial energy by

\[
\boxed{
o\!\left(\frac{M}{\mathcal L_M}\right).}
\tag{22}
\]

This is the only reason the theorem asks for a sufficiently large fixed cutoff. No cutoff is allowed to grow with `M`.

The same argument absorbs the small exact hyperbolic normal-correspondence displacement used in PF-217. The Gaussian mass lives at `|t|=O(R_M)=o(\log P_M)`; on that region PF-217's displacement `O(s_n^2e^{2|t|})` is polynomially negligible, while the Gaussian tails outside it are themselves polynomially tiny after the choices above.

## 3. The exact low-band profile keeps enough constant mass

Prescribe

\[
\phi_n(t)=z_n b_{n,M}(t)
\tag{23}
\]

on both sides of the `n`th PF-205 seam strip. Let

\[
f^{(M)}=\Lambda_Q^{1/2}\phi,
\qquad
x^{(M)}=Pf^{(M)}.
\tag{24}
\]

The zero-twist marking is again load-bearing: the same centered profile is used on both strip sides, so the normal strip extension has no `w_n^{-1}` phase-welding cost.

PF-217's exact projection identity and (20) give the physical cuff mean

\[
t_n
=z_n\frac{\sqrt{2\pi}R_M}{L_n}
\tag{25}
\]

and therefore

\[
\frac{|x_n|^2}{q_n}=|t_n|^2.
\tag{26}
\]

On the dyadic index block `L_n\asymp\mathcal L_M`, while `\sum z_n^2\asymp M`. Hence

\[
\boxed{
\mathfrak m_0[x^{(M)}]
=\sum_n|t_n|^2
\asymp
M\frac{R_M^2}{\mathcal L_M^2}
\asymp
\frac{M}{\mathcal L_M},
}
\tag{27}
\]

which proves (1). The constant projection is smaller than PF-217's original order-`M` mass, but it still diverges much faster than the logarithmic conductance cost.

Because `b_{n,M}` is exactly physical-low and `\Lambda_{Q,n}^{1/2}` preserves every tangential Fourier block, the nonconstant remainder

\[
y^{(M)}:=Qf^{(M)}
\]

belongs exactly to `Q_{\le\kappa}`. There is no Galerkin approximation and no residual physical-high component.

## 4. Its total cut energy is negligible relative to that mass

The constant-normal strip extension gives, exactly as in PF-217,

\[
\langle\phi_n,\Lambda_{Q,n}\phi_n\rangle
\le
Cw_nz_n^2
\left(
\|b_{n,M}\|_2^2+
\|b_{n,M}'\|_2^2
\right).
\tag{28}
\]

The Gaussian formulas and (21) give

\[
\|b_{n,M}\|_2^2=O(R_M),
\qquad
\|b_{n,M}'\|_2^2=O(R_M^{-1}),
\tag{29}
\]

so `w_n\asymp P_n^{-1}` yields a total strip cost

\[
O\!\left(\frac{R_M}{\log P_M}\right)
=o(1).
\tag{30}
\]

For the pant cores use the same normal-ray interpolation as PF-217. Equations (13)--(15), the sine-envelope estimate, and the approximation error (22) give

\[
\sum_{M\le n\le2M}
\mathcal E_{E_n}^{\rm trial}
\le
C\log M
+
C M R_M P_M^{-\delta}
+o\!\left(\frac{M}{\mathcal L_M}\right).
\tag{31}
\]

Together with the strip term and the exact total-energy identity of PF-217,

\[
\mathfrak a[f]
=
\langle\phi,\Lambda_Q\phi\rangle
+
\langle\phi,\Lambda_E\phi\rangle,
\tag{32}
\]

this gives

\[
\mathfrak a[f^{(M)}]
\le
C\log M
+o\!\left(\frac{M}{\mathcal L_M}\right).
\tag{33}
\]

Since `\mathcal L_M\asymp\log M`, equations (27) and (33) imply

\[
\frac{\mathfrak a[x^{(M)}+y^{(M)}]}
{\mathfrak m_0[x^{(M)}]}
\le
C\frac{(\log M)^2}{M}+o(1)
\longrightarrow0,
\tag{34}
\]

proving (2)--(4).

This is stronger than merely re-estimating the PF-217 bump's high Fourier tail. The variational competitor itself belongs to the fixed physical low sector.

## 5. The low-sector Schur angle therefore saturates

Restrict a finite block response to the cuff-constant sector plus `Q_{\le\kappa}` and write

\[
\mathcal A^{\le\kappa}_M
=
\begin{pmatrix}
H_M&B^{\le\kappa}_M\\
(B^{\le\kappa}_M)^*&J^{\le\kappa}_M
\end{pmatrix}>0,
\]

\[
C^{\le\kappa}_M
:=H_M^{-1/2}B^{\le\kappa}_M
(J^{\le\kappa}_M)^{-1/2}.
\tag{35}
\]

PF-216 gives for the same constant projection

\[
\mathfrak a[x^{(M)}]
\ge c\mathfrak m_0[x^{(M)}].
\tag{36}
\]

The PF-306/PF-307 completion-of-the-square identity applies verbatim to this smaller complementary sector. Therefore

\[
1-\|C^{\le\kappa}_M\|^2
\le
\frac{\mathfrak s_{\le\kappa}[x^{(M)}]}
{\mathfrak a[x^{(M)}]}
\le
C\frac{\mathfrak a[x^{(M)}+y^{(M)}]}
{\mathfrak m_0[x^{(M)}]}
\longrightarrow0.
\tag{37}
\]

This proves (5). The near-unit angle found in PF-307 is therefore not a high-frequency artifact of allowing all nonconstant modes. A growing but fixed-physical-band family of low tangential modes is already sufficient to screen the constant sector.

Notice the distinction between **fixed physical bandwidth** and **fixed rank**. On a cuff with `L_n\asymp\log P_n`, the number of modes below `\kappa` is `O(\kappa L_n)`. That rank grows logarithmically, exactly as in PF-212. The theorem does not claim that a fixed finite number of tangential Fourier modes suffices.

## 6. PF-303 killing also reaches the fixed-low-band screened directions

PF-308's killing-mass argument depends only on the physical constant traces and the PF-216 same-sign floor

\[
\kappa_{n,L}+\kappa_{n,R}\ge c_0>0.
\tag{38}
\]

On a fixed central fraction of the sine block, `|z_n|` and `|z_{n+1}|` are bounded below. Equation (25) therefore gives

\[
\boxed{
\langle t^{(M)},D_Mt^{(M)}\rangle
\ge
cM\frac{R_M^2}{\mathcal L_M^2}
\asymp
\frac{M}{\mathcal L_M}.
}
\tag{39}
\]

The restricted effective constant form is no larger than the explicit low-band trial energy, so (33)--(34) give

\[
\langle t^{(M)},H_M^{\mathrm{eff},\le\kappa}t^{(M)}\rangle
=o\!\left(\frac{M}{\mathcal L_M}\right).
\tag{40}
\]

The same generalized Rayleigh quotient used in PF-308 now yields (7).

Thus even **after forbidding every physical-high complementary mode**, the full killing-normalized constant sector still sees a divergent screened Green reservoir. The safe conclusion is not that screening disappears under the physical split. It is that the screening occurs wholly on the low side of that split.

## 7. Consequence for the current `P/H` frontier

PF-309 established that its explicit compact-bump witness is asymptotically invisible to a fixed physical-high entrance. The present construction removes the possible objection that the compact bump's residual high tail was secretly essential: exact low-band screening still saturates the Schur angle and still defeats the full killing-normalized constant Green bound.

The source-to-target problem therefore has a more precise two-stage structure:

\[
\text{constant / physical-low source}
\quad\longrightarrow\quad
\text{near-singular physical-low screening reservoir}
\quad\longrightarrow\quad
\text{possible physical-high target output}.
\]

Only the second arrow is now live. A dangerous final mixed response must prove that exterior propagation, Schur inversion, or reassembly converts enough of this amplified low reservoir into physical-high output, or else produce a different source-accessible family. Conversely, a positive endpoint result can focus on bounding that post-screening low-to-high conversion rather than trying to restore a global Schur-angle gap.

There is no contradiction with PF-212's low-sector estimate. PF-212 already allows `O(1+\kappa L_n)` low rank per module and controls low-containing recoupling words only after the PF coefficient and the required modulewise/fixed-color reassembly are included. PF-310 concerns an internal Schur Green amplification before those later weights and placement rules are spent.

## Prior-art and novelty audit

Localization of bandlimited functions is classical. Slepian and Pollak, *Prolate Spheroidal Wave Functions, Fourier Analysis and Uncertainty — I*, Bell System Technical Journal **40** (1961), 43--63, DOI `10.1002/j.1538-7305.1961.tb03976.x`, study the canonical time--band concentration problem. The present proof does not need their extremal theorem: equations (16)--(21) use only the explicit Fourier series of a periodized Gaussian and elementary Gaussian-tail estimates. The Slepian--Pollak literature is relevant prior-art context for why simultaneous spatial and frequency concentration itself is not novel.

A targeted literature search for hyperbolic pair-of-pants/Dirichlet-to-Neumann screening with this fixed physical-band Schur mechanism did not locate a theorem that substitutes for the project-specific argument. Search absence is not novelty evidence. No new general Fourier, uncertainty, Gaussian, Poisson-summation, shorted-operator, or Schur-complement theorem is claimed.

The Mathia-specific deduction is the combination of four persisted ingredients: PF-217's zero-twist narrow-gap screening geometry, PF-212's physical Fourier split, PF-216/PF-307's constant/nonconstant Schur normalization, and PF-303/PF-308's killing currency. Their combination shows that the near-singular screening reservoir exists **inside a fixed physical low band** on the canonical prime-flute tail.

## Boundaries and falsification

1. **Fixed but sufficiently large cutoff.** The proof uses the freedom in PF-212 to choose one fixed `\kappa`. It does not claim exact low-band screening for every arbitrarily small prescribed cutoff. An adversary should quantify the constants in (21)--(22) and verify that one finite `\kappa_0` works uniformly on the canonical tail.
2. **Gaussian Fourier truncation must be tested in the form norm, not only in `L^2`.** In particular the error must remain negligible after the worst `s_n^{-1}` conductance factor. This is why `R_M^2\asymp\log P_M` and the cutoff is chosen after `\eta`.
3. **Periodization must not reintroduce a narrow-gap mismatch.** Recheck the periodic-image estimates in the `1/(s_n\cosh t)` transverse weight. Near the common-perpendicular foot the images are polynomially tiny in `P_M`; near the pant ends the `\cosh` weight cancels the raw `s_n^{-1}` loss.
4. **The strip normalizer must preserve physical Fourier support.** PF-212's tangential translation invariance is the exact reason `\Lambda_{Q,n}^{1/2}` cannot create a high mode from (18).
5. **The zero-twist marking remains load-bearing.** The same centered profile must be prescribed on the two sides of a seam strip. A fixed phase mismatch across a shrinking strip would create a different cost.
6. **Only existence, not multiplicity.** Equation (5) gives a near-unit low-sector angle witness on growing tail blocks. It does not count how many such directions exist or establish a weak-Schatten bound or obstruction.
7. **No final physical-high conclusion.** The theorem proves neither that low-to-high reassembly is small nor that it is large. It isolates that conversion as the next exact gate.
8. **No RH implication.** Scattering determinants, resonances, zeta-zero correspondence, the critical line, and RH remain outside this finding.

The most useful next calculation is now explicit: insert the fixed-low-band screened reservoir into the **actual source-to-target reassembly map** and estimate the first operator that can create physical-high output. If that map is uniformly smoothing or carries the PF-212 low-rank/module weights before amplification can accumulate, the known Schur obstruction may still be harmless. If it converts the low reservoir coherently into high output, the responsible vertex is finally identified.