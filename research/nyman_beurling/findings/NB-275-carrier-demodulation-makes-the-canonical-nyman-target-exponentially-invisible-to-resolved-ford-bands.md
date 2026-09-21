---
finding_id: NB-275
prefix: NB
title: Carrier demodulation makes the canonical Nyman target exponentially invisible to resolved Ford bands
status: proposed
verdict: pending
reviewed: false
created: 2026-09-21
updated: 2026-09-21
authors:
  - OpenAI
origin:
  kind: research-watch
  ref: nyman_beurling
depends_on:
  - NB-001
  - NB-269
  - NB-272
  - NB-274
supersedes: []
superseded_by: []
related_findings:
  - NB-271
  - NB-273
---

# Carrier demodulation makes the canonical Nyman target exponentially invisible to resolved Ford bands

## Claim

`NB-274` reduced the remaining target-anchor branch of the exact full-line resolved Ford channel to a concrete question: after carrying the canonical Nyman target through the same center translation, rescaling, and carrier demodulation as `NB-269`, does the transformed target remain frequency-tight in the positive residual shell coordinate?

For the canonical Hardy target the answer is stronger than yes. The target becomes **exponentially invisible** on every resolved Ford shell band.

In the Bagchi Hardy formulation used in `NB-001`, the target is

\[
E(s)=\frac1s,
\qquad
\|E\|_{H^2(\Re s>1/2)}=1.
\tag{1}
\]

On the boundary `s=1/2+it`, use the exact Laplace representation

\[
E(1/2+it)
=\int_0^\infty e^{-x/2}e^{-itx}\,dx.
\tag{2}
\]

The `NB-269` center variable is

\[
z=H(t-t_0),
\qquad
YJ=\frac XH,
\tag{3}
\]

and the common physical carrier `X` is removed by multiplication by `e^{iYJz}`. The unitary image of the canonical target under exactly that center normalization is therefore

\[
\boxed{
 g_{X,H,t_0}(z)
 :=H^{-1/2}e^{iYJz}
 E\!\left(\frac12+i\left(t_0+\frac zH\right)\right).
}
\tag{4}
\]

With the Fourier convention used in `NB-269`, write

\[
g(z)=\int_{\mathbb R}\Gamma(\xi)e^{-i\xi z}\,d\xi,
\qquad
\frac1{2\pi}\int_{\mathbb R}|g(z)|^2dz
=\int_{\mathbb R}|\Gamma(\xi)|^2d\xi.
\tag{5}
\]

A direct change of variables in (2) gives the exact transformed target spectrum

\[
\boxed{
\Gamma_{X,H,t_0}(\xi)
=
\sqrt H\,
 e^{-(X+H\xi)/2}
 e^{-it_0(X+H\xi)}
 \mathbf 1_{\{\xi\ge-X/H\}}.
}
\tag{6}
\]

Hence for every `a>0`,

\[
\boxed{
\int_a^\infty
|\Gamma_{X,H,t_0}(\xi)|^2d\xi
=e^{-X-aH}.
}
\tag{7}
\]

The resolved shell atoms of `NB-269` have Fourier supports

\[
E_j=j+\operatorname{supp}\phi,
\qquad
0\le j<K,
\qquad
\operatorname{supp}\phi\subset[a,b]\subset(0,1),
\tag{8}
\]

so their complete span lies in positive residual frequencies `xi>=a`. If `S_K` denotes the corresponding full-line synthesis map, then

\[
\boxed{
\|P_{\operatorname{ran}S_K}g_{X,H,t_0}\|_2^2
\le e^{-X-aH}.
}
\tag{9}
\]

Therefore the unconstrained section defect from `NB-272` satisfies

\[
\boxed{
\delta_K^2
=\operatorname{dist}(g_{X,H,t_0},\operatorname{ran}S_K)^2
\ge1-e^{-X-aH}
\longrightarrow1.
}
\tag{10}
\]

This is the opposite of the branch contemplated after `NB-272`: the canonical target does not approach the resolved Ford span while an anchor mismatch remains mysterious. It is already asymptotically orthogonal to that span before the Euler anchor is imposed.

Under the live `NB-274` shell-norm bound

\[
q_{K,j}=\|s_{K,j}\|_2^2\le q_+,
\tag{11}
\]

the uniform legal anchor vector `c_j=1/K` gives the matching upper control

\[
\boxed{
\inf_{e_K^*c=1}
\|g_{X,H,t_0}-S_Kc\|_2^2
\longrightarrow1
}
\tag{12}
\]

as `X,K -> infinity`. Thus the canonical target distance inside the exact full-line resolved Ford channel is asymptotically **maximal**, not merely bounded away from zero.

The conclusion is a method boundary, not a statement that the full Nyman distance tends to one. The `NB-269` Ford current is a local high-carrier diagnostic, not the complete canonical Nyman synthesis. Equation (12) shows that it cannot itself serve as the missing rank-uniform bridge from the shallow Ford obstruction to approximation of the fixed Nyman target.

## 1. The canonical target has an exact positive-frequency density

The Hardy target identity in `NB-001` is

\[
E(s)=1/s.
\]

On `Re s=1/2`, elementary Laplace inversion gives (2). In particular, before any Ford normalization its boundary Fourier density is

\[
\widehat E(x)=e^{-x/2}\mathbf 1_{\{x\ge0\}}.
\tag{13}
\]

With the normalized Hardy boundary measure, Plancherel reads

\[
\|E\|^2
=\int_0^\infty e^{-x}dx
=1.
\tag{14}
\]

This is also the simplest way to track the target through the `NB-269` coordinate changes. There is no need to infer its behavior from the discrete generator pairings `-\log k/k`; those live in a different coordinate system, exactly as `NB-274` warned.

The positive-frequency Hardy projection used before the `NB-269` squaring step does not alter `E`: it is already an `H^2` boundary function with one-sided spectral support. What changes its location relative to the resolved source bands is the subsequent carrier demodulation.

## 2. Exact center translation, rescaling, and demodulation

Translation to `t_0`, rescaling by `z=H(t-t_0)`, and multiplication by a unimodular carrier are all unitary on the boundary Hilbert space when the Jacobian factor `H^{-1/2}` is included. Thus (4) has norm one.

Insert (2) into (4):

\[
\begin{aligned}
g_{X,H,t_0}(z)
&=H^{-1/2}e^{i(X/H)z}
  \int_0^\infty
  e^{-x/2}e^{-it_0x}e^{-izx/H}\,dx.
\end{aligned}
\tag{15}
\]

Set

\[
\xi=\frac xH-\frac XH,
\qquad
x=X+H\xi,
\qquad
dx=H\,d\xi.
\tag{16}
\]

The lower endpoint `x=0` becomes `xi=-X/H`. Equation (15) becomes

\[
g_{X,H,t_0}(z)
=
\int_{-X/H}^{\infty}
\sqrt H\,
 e^{-(X+H\xi)/2}
 e^{-it_0(X+H\xi)}
 e^{-i\xi z}\,d\xi,
\tag{17}
\]

which proves (6).

There is a useful sign check. Before demodulation the `NB-269` shell `j` lives at the physical carrier

\[
X+H(j+u).
\tag{18}
\]

After multiplication by `e^{i(X/H)z}`, that same frequency becomes the residual frequency `j+u`. Equation (6) therefore evaluates the canonical target on a residual shell `xi=j+u` exactly at its original Hardy frequency

\[
x=X+H(j+u),
\tag{19}
\]

where its squared density is proportional to `e^{-x}`. This fixes the demodulation sign independently of Fourier-normalization conventions.

Most of the target mass is consequently transported to residual frequencies near `-X/H=-YJ`, while the source dictionary has been transported to positive residual frequencies beginning at `a`. The two objects move in opposite directions in the demodulated frame.

## 3. Exponential target invisibility of the complete resolved source span

Squaring (6) removes the irrelevant `t_0` phase. For any `L>=0`,

\[
\int_L^\infty
|\Gamma_{X,H,t_0}(\xi)|^2d\xi
=
\int_L^\infty
H e^{-X-H\xi}\,d\xi
=e^{-X-HL}.
\tag{20}
\]

In particular (7) follows by setting `L=a`.

Every source atom in `NB-274` satisfies

\[
\operatorname{supp}\widehat s_{K,j}
\subset j+\operatorname{supp}\phi
\subset[a,\infty).
\tag{21}
\]

Therefore

\[
\operatorname{ran}S_K
\subset
\{f:\operatorname{supp}\widehat f\subset[a,\infty)\}.
\tag{22}
\]

Orthogonal projection can only decrease norm, so

\[
\|P_{\operatorname{ran}S_K}g_{X,H,t_0}\|_2^2
\le
\|\mathbf1_{[a,\infty)}\Gamma_{X,H,t_0}\|_2^2
=e^{-X-aH}.
\tag{23}
\]

Because `||g||=1`,

\[
\delta_K^2
=1-\|P_{\operatorname{ran}S_K}g\|_2^2
\ge1-e^{-X-aH}.
\tag{24}
\]

The Ford regime has `X -> infinity`, so the right-hand side tends to one without requiring any subtle relation between `K` and `H`. This is stronger than the one-sided frequency-tightness hypothesis of `NB-274`: the **entire positive-frequency mass** of the transformed canonical target is already only `e^{-X}`.

The same estimate controls all target pairings at once. Since the shell cells are disjoint,

\[
\sum_{j<K}
\frac{|\langle s_{K,j},g\rangle|^2}{q_{K,j}}
=
\|P_{\operatorname{ran}S_K}g\|_2^2
\le e^{-X-aH},
\tag{25}
\]

where the equality is the orthogonal-shell projection identity. Thus no inverse-Gram amplification is hiding target mass inside the exact full-line channel.

## 4. The Euler anchor cannot repair a target-poor span

The lower bound for the anchored problem is immediate from (24): imposing `e_K^*c=1` only shrinks the admissible set, hence

\[
\inf_{e_K^*c=1}\|g-S_Kc\|_2^2
\ge1-e^{-X-aH}.
\tag{26}
\]

For the reverse asymptotic bound use the legal uniform anchor vector

\[
c^{\rm unif}=K^{-1}e_K.
\tag{27}
\]

Exact shell orthogonality and (11) give

\[
\|S_Kc^{\rm unif}\|_2^2
=\frac1{K^2}\sum_{j<K}q_{K,j}
\le\frac{q_+}{K}.
\tag{28}
\]

Furthermore, because `S_Kc^{unif}` lies in the positive shell region,

\[
|\langle g,S_Kc^{\rm unif}\rangle|
\le
 e^{-(X+aH)/2}
 \sqrt{\frac{q_+}{K}}.
\tag{29}
\]

Therefore

\[
\inf_{e_K^*c=1}\|g-S_Kc\|_2^2
\le
1+rac{q_+}{K}
+2e^{-(X+aH)/2}\sqrt{\frac{q_+}{K}}.
\tag{30}
\]

Together, (26) and (30) prove (12).

This also clarifies the decomposition of `NB-272`. For the canonical transformed target, the decisive term is not the anchor mismatch `mu_K`; the unconstrained section defect itself tends to its maximum possible value. Whether `mu_K` tends to one, remains bounded, or has some finer asymptotic is irrelevant to the target-distance conclusion because `delta_K^2 -> 1` already saturates the residual.

## 5. Consequence for the Ford-to-Nyman route

The chain `NB-269`--`NB-274` asked whether the local Hardy-projected Ford channel could contain a hidden destination mechanism that turns the shallow source obstruction into a lower bound for the canonical Nyman approximation problem. The present calculation answers that question for the direct target embedding.

It cannot. The carrier demodulation that makes the source dictionary simple simultaneously moves the fixed Nyman target away from those source bands. In physical Hardy frequency, the Ford shells sit near `X`; the target `1/s` has spectral density `e^{-x/2}` there. Thus the resolved current is an effective diagnostic of high-frequency zeta/source behavior precisely in a region where the fixed Nyman target has exponentially little Hilbert mass.

This is not a contradiction with the global Nyman criterion. The canonical generators `G_k(s)=(k^{-s}-k^{-1})zeta(s)/s` are not the `NB-269` Ford current atoms. A successful bridge would need an additional operator or global coupling that transports information from the high-carrier Ford diagnostic back into the target-bearing part of the canonical Nyman geometry. `NB-271` says that if such a bridge appears as a new positive source-source Gram on the resolved shell coordinates, it must have `Omega(K)` relative strength before it can enforce a rank-uniform anchored floor.

The next useful object is therefore not another estimate of `delta_K` or `mu_K` inside `S_K`: both target branches are now settled for the direct canonical embedding, and the section defect is maximally bad. The unresolved question is to identify the **actual map from a Ford shell perturbation to the canonical Nyman residual**, if one exists, and test its relative Gram against the `NB-271` `Omega(K)` threshold.

## Adversarial review

The main possible error is a Fourier-sign mismatch. Equation (19) is the invariant check: the source cell `j+u` after demodulation must correspond to physical carrier `X+H(j+u)` before demodulation, exactly as in `NB-269`. The canonical target density at that physical frequency is `e^{-[X+H(j+u)]/2}`. Reversing the sign would fail to send the known source carrier to its declared residual cell.

The second possible overreach is to confuse the exact full-line channel with the hard-window current. Multiplication by a hard window in `z` convolves frequencies and can mix the target with the shell bands. Equations (9)--(12) concern the **full-line resolved synthesis map** used in `NB-274`, where shell supports are exact. They do not assert a corresponding exact support separation after hard-window restriction.

Third, this is not a theorem about the full Nyman distance. The operations leading to the Ford current were introduced as a source/zero diagnostic. The present result shows that treating that diagnostic itself as the canonical target approximation space is target-poor. It does not exclude a different, nonlocal map from the Ford current into the full Nyman residual.

Fourth, the exponential estimate uses only the canonical target `E=1/s`. If a later exact reformulation naturally transforms the target by an additional nonunitary multiplier before entering the resolved channel, its spectrum must be recomputed rather than importing (6).

Finally, `t_0` does not matter for the energy estimate: it contributes only the phase `e^{-it_0(X+Hxi)}`. The conclusion is uniform in the observation ordinate once `X` and `H` are fixed.

## Prior-art check

The Hardy-space identity `E(s)=1/s` and its role as the fixed Nyman target are classical and already anchored in `SOURCES.md` through Bagchi's 2006 Hardy/Mellin formulation. A fresh search also found Manzur--Noor--Quintero, *A Hardy space approximation supporting zero-free half-planes for the zeta-function* (arXiv:2606.16097, 15 June 2026), which again uses the same target and canonical generators. Neither source addresses the rank-coupled Ford center normalization of `NB-269` or the effect of demodulating a carrier at frequency `X` on the target/source overlap.

The load-bearing calculation here is elementary and self-contained: the Laplace representation (2), the exact unitary coordinate change (4), and Fourier support of the already-derived resolved shell atoms. No new external theorem is required, so `SOURCES.md` needs no new dependency.

## What is established

After the exact center translation, `z=H(t-t_0)` rescaling, and carrier demodulation used in `NB-269`, the canonical Nyman target has residual-frequency density (6). Its entire mass in the positive shell region `xi>=a` is exactly `e^{-X-aH}`. Consequently the exact full-line resolved Ford span captures at most that much target energy, its unconstrained canonical-target defect tends to one, and even the optimally chosen Euler-anchored residual tends to one.

This settles the `NB-274` transformed-target question in the direct full-line channel: the target is not merely frequency-tight; it is asymptotically absent from the resolved positive Ford bands.

## What is not established

No claim is made that the complete Nyman approximation error tends to one, that the actual zeta zeros realize any matched packet, or that every possible Ford-to-Nyman bridge is impossible. Hard-window frequency mixing is not diagonalized by this argument. An additional exact operator acting on the canonical target or on the source could change the relevant spectral overlap and must be audited separately.

## Falsification / audit test

Using any fixed `X,H,t_0`, compute the boundary target (4), Fourier transform it in `z`, and compare its squared spectral mass above a residual cutoff `L>=0` with

\[
e^{-X-HL}.
\]

Any discrepancy beyond Fourier-normalization constants would falsify the coordinate derivation. Independently, verify that a source atom with pre-demodulation carrier `X+H(j+u)` lands at residual frequency `j+u`; this checks the sign of the carrier shift without relying on transform conventions.

## Open seam

The direct target-aware continuation inside `S_K` is now exhausted: the canonical target has maximal section defect there. The next discriminating calculation is to derive the first **nonlocal or nonunitary source-to-destination operator** that actually connects the Ford current to the canonical Nyman residual. If its shell-coordinate Gram is `A_K`, `NB-271` supplies an immediate viability filter:

\[
\|R_K^{-1/2}A_KR_K^{-1/2}\|_{op}
\]

must reach `Omega(K)` and its inverse-Gram geometry must be aligned with the Euler anchor. An `o(K)` bridge cannot restore rank-uniform coercivity.