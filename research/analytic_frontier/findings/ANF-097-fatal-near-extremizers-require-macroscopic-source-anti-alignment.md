# ANF-097 — fatal near-extremizers require macroscopic source anti-alignment

**Status:** `EXACT-DERIVED + QUOTIENT-AWARE-STABILITY + INTERFERENCE-CERTIFICATE + NEAR-EQUALITY-RIGIDITY + REMOTE-SURGERY-CLOSURE`. `ANF-093` shows that even the exact Lamzouri source quotient can be exponentially ill-conditioned on the safe separable cone, while `ANF-096` closes the explicit arithmetic sparse-surgery family by computing its physical positive structure factor rather than the signed Rayleigh witness. The remaining question can be separated from conditioning altogether. For every compatible separable comparator, the Montgomery--Taylor excess admits an exact polarization identity in which all terms are nonnegative except one: the source interference between the comparator and the physical defect. Because the central-notch norm is pointwise dominated by the Montgomery--Taylor norm, a configuration that is simultaneously Montgomery--Taylor near-extremal and a fixed positive distance from the separable cone must therefore exhibit **macroscopic destructive Montgomery--Taylor interference with every compatible separable carrier**. In particular, source-orthogonal, nonnegatively correlated, and asymptotically remote surgeries cannot realize the fatal gate.

Retain the central-notch data from `ANF-034`, `ANF-081`, and `ANF-086`,

\[
0\le J_s=J_{\rm MT}-s\phi_\eta\le J_{\rm MT},
\qquad
q_s>0,
\tag{1}
\]

and the structure-factor notation

\[
S_W(\alpha)=\sum_{z\in W}e^{-2\pi i\alpha z},
\qquad
L(W)=2|W|-\sigma(W),
\qquad
\Delta(W)=\|S_W\|_{\rm MT}^2-L(W).
\tag{2}
\]

For `P in Sep(W)` in the sense of `ANF-086`, define the physical defect and its Montgomery--Taylor interference with the comparator by

\[
D_{W\mid P}:=S_W-S_P,
\qquad
\mathcal I_{\rm MT}(W\mid P)
:=\operatorname{Re}\langle S_P,D_{W\mid P}\rangle_{\rm MT}.
\tag{3}
\]

Then one has the exact identity

\[
\boxed{
\Delta(W)
=
\Delta(P)
+\bigl(L(P)-L(W)\bigr)
+\|D_{W\mid P}\|_{\rm MT}^2
+2\mathcal I_{\rm MT}(W\mid P).
}
\tag{4}
\]

Every term on the right except the final interference is nonnegative. Moreover the destination defect obeys

\[
\boxed{
q_s\,L(P)\,\delta_s(W\mid P)^2
\le
\|D_{W\mid P}\|_{\rm MT}^2.
}
\tag{5}
\]

Consequently

\[
\boxed{
q_s\,\delta_s(W\mid P)^2
\le
\frac{
\Delta(W)-\Delta(P)-\bigl(L(P)-L(W)\bigr)
-2\mathcal I_{\rm MT}(W\mid P)
}{L(P)}.
}
\tag{6}
\]

Thus a large quotient-aware destination defect is impossible unless it is paid either by Montgomery--Taylor excess or by negative source interference. There is no Gram condition number in (4)--(6).

## 1. Polarization isolates the only possible cancellation mechanism

Use the Montgomery--Taylor inner product

\[
\langle f,g\rangle_{\rm MT}
:=
\int_{-1}^{1}J_{\rm MT}(\alpha)
 f(\alpha)\overline{g(\alpha)}\,d\alpha.
\tag{7}
\]

Since `S_W=S_P+D_{W|P}`, Hilbert-space polarization gives

\[
\|S_W\|_{\rm MT}^2
=
\|S_P\|_{\rm MT}^2
+\|D_{W\mid P}\|_{\rm MT}^2
+2\mathcal I_{\rm MT}(W\mid P).
\tag{8}
\]

Subtract `L(W)` and insert

\[
\|S_P\|_{\rm MT}^2=L(P)+\Delta(P),
\tag{9}
\]

which proves (4). Because `P in Sep(W)`, `ANF-086` gives

\[
L(P)\ge L(W),
\tag{10}
\]

and Lamzouri's global Montgomery--Taylor inequality gives `Delta(P)>=0`. Therefore, apart from `I_MT`, every term added to `Delta(W)` in (4) has a fixed nonnegative sign.

This is the key distinction from the generalized-eigenvalue path of `ANF-089`--`ANF-093`. A nearly singular labelled source system can create directions with a very small quadratic cost, but a **physical configuration** is not a free signed coefficient vector. Once a concrete separable comparator is chosen, any physical departure from it enters (4) through its full positive defect energy. To keep the total excess small while that defect is macroscopic, the configuration must arrange a negative cross term of the same macroscopic size.

## 2. The central notch cannot amplify a physical defect beyond its source norm

The notch profile was constructed by subtracting a nonnegative central tent,

\[
J_s=J_{\rm MT}-s\phi_\eta,
\qquad \phi_\eta\ge0,
\tag{11}
\]

so pointwise

\[
0\le J_s\le J_{\rm MT}.
\tag{12}
\]

Hence every finite exponential sum `D` satisfies

\[
\|D\|_s^2\le\|D\|_{\rm MT}^2.
\tag{13}
\]

On the other hand `ANF-085`--`ANF-086` give the all-height separable floor

\[
\|S_P\|_s^2\ge q_sL(P).
\tag{14}
\]

By the definition of the relative destination defect,

\[
\delta_s(W\mid P)^2
=
\frac{\|D_{W\mid P}\|_s^2}{\|S_P\|_s^2},
\tag{15}
\]

and (13)--(14) prove (5). Combining (5) with the exact identity (4) proves (6).

The pointwise domination (12) does **not** by itself prove that every near-extremizer is close to the separable cone: the defect energy in (4) can be cancelled by the cross term. What it proves is that there is only one remaining way for source and destination geometry to decouple at the level of an actual multiset. The obstruction must be destructive interference with the comparator, not a hidden destination amplification of a source-small physical defect.

## 3. A quotient-wide anti-alignment invariant

Define the best normalized source interference against the complete compatible separable class by

\[
\boxed{
\iota_{\rm sep}(W)
:=
\sup_{P\in\operatorname{Sep}(W)}
\frac{\mathcal I_{\rm MT}(W\mid P)}{L(P)}.
}
\tag{16}
\]

The class `Sep(W)` is nonempty by `ANF-086`. Also (4), together with `Delta(P)>=0` and `L(P)>=L(W)`, implies for every `P in Sep(W)`

\[
\frac{\mathcal I_{\rm MT}(W\mid P)}{L(P)}
\le
\frac{\Delta(W)}{2L(P)}
\le
\frac{\Delta(W)}{2L(W)},
\tag{17}
\]

so the supremum is finite.

From (6), discarding the nonnegative `Delta(P)` and `L(P)-L(W)`, using `L(P)>=L(W)`, and then taking the infimum in the destination and the supremum in the interference gives

\[
\boxed{
q_s\,d_{\rm sep}(W)^2
+2\iota_{\rm sep}(W)
\le
\frac{\Delta(W)}{L(W)}.
}
\tag{18}
\]

This is a two-sided quotient statement absent from the raw Gram criteria. The destination has already been optimized over the entire nonlinear separable class through `d_sep`, while the source remembers only the most favorable compatible comparator through `iota_sep`. No labelled representation, smallest Gram eigenvalue, Schur-complement conditioning constant, or chosen real-axis collapse remains.

A particularly useful screening corollary is immediate. If a sequence `W_n` is Montgomery--Taylor near-extremal,

\[
\frac{\Delta(W_n)}{L(W_n)}\to0,
\tag{19}
\]

and there exist compatible separable carriers `P_n` with

\[
\mathcal I_{\rm MT}(W_n\mid P_n)
\ge -o\bigl(L(P_n)\bigr),
\tag{20}
\]

then (6) gives

\[
\boxed{d_{\rm sep}(W_n)\to0.}
\tag{21}
\]

Thus asymptotically source-orthogonal defects, nonnegative source interference, and remote surgeries whose cross term is `o(L)` are all automatically inside the protected separable tube once near-extremality is known.

## 4. Fatal near-extremizers must anti-align with every separable carrier

Retain the fixed fatal radius from `ANF-086`,

\[
\kappa_{\rm crit}
=1-\sqrt{\rho_s/q_s}>0.
\tag{22}
\]

Any configuration defeating the central-notch certificate satisfies

\[
d_{\rm sep}(W)\ge\kappa_{\rm crit}.
\tag{23}
\]

Substitution into (18) yields the necessary condition

\[
\boxed{
\iota_{\rm sep}(W)
\le
\frac12\left(
\frac{\Delta(W)}{L(W)}
-q_s\kappa_{\rm crit}^2
\right).
}
\tag{24}
\]

The comparator-wise version is stronger. Combining (4)--(5) with (23), every `P in Sep(W)` must satisfy

\[
\boxed{
\begin{aligned}
2\mathcal I_{\rm MT}(W\mid P)
\le{}&
\Delta(W)-\Delta(P)
-\bigl(L(P)-L(W)\bigr)\\
&-q_s\kappa_{\rm crit}^2L(P).
\end{aligned}}
\tag{25}
\]

Therefore if a fatal sequence were also genuinely Montgomery--Taylor near-extremal as in (19), then

\[
\boxed{
\limsup_{n\to\infty}\iota_{\rm sep}(W_n)
\le
-\frac{q_s\kappa_{\rm crit}^2}{2}<0.
}
\tag{26}
\]

Because `iota_sep` is a supremum, (26) is much stronger than saying that one badly chosen comparator has negative cross term. **Every** compatible separable carrier must eventually have a fixed negative normalized interference with the physical defect. A near-extremal obstruction must therefore be globally anti-aligned with the whole separable class in the Montgomery--Taylor source geometry.

This is a falsifiable mechanism. To construct a counterexample one must now exhibit a physical positive multiset whose departure from every product carrier has macroscopic destination norm while simultaneously cancelling against every such carrier by an amount of order `L`. Conversely, any structural argument producing even one comparator with `I_MT=-o(L)` closes the configuration.

## 5. Relation to the sparse-conditioning branch

`ANF-093` shows that the signed binomial generalized-eigenvector can be exponentially source-small relative to a real-collapse destination defect even after the exact Lamzouri Schur quotient. Equation (18) explains why that fact is not yet physically dangerous: a generalized eigenvector is not required to satisfy the polarization balance (4) as the actual defect of a positive multiset relative to its best separable carrier.

`ANF-094`--`ANF-096` then attempt to realize a physical obstruction by changing a sparse block inside a much larger separable carrier. `ANF-096` finds that for the explicit arithmetic block the physical source and destination endpoint costs meet at the same `3 log n + 2 log log n` scale, while the remote padding cross terms are negligible. The present result abstracts the second half of that phenomenon. Once a surgery has

\[
\mathcal I_{\rm MT}(W_n\mid P_n)=o(L(P_n))
\tag{27}
\]

for its natural separable parent and is known independently to be Montgomery--Taylor near-extremal, its destination distance must vanish, **regardless of the internal horizontal synthesis, height profile, or conditioning of the edited block**. The detailed endpoint calculation of `ANF-096` remains useful because it determines when its explicit family is actually near-extremal; what no longer needs to be rediscovered family by family is the geometric consequence of a negligible cross term.

This removes an entire class of candidate obstructions. A surviving sparse or localized surgery cannot merely hide a high-energy defect far from the padding. It must be positioned and phased so that the padding or another large separable component cancels that defect macroscopically in the Montgomery--Taylor inner product. That is a much more rigid requirement than bad finite-section conditioning.

## 6. Adversarial audit and prior-art boundary

The argument was stress-tested against the main failure modes of the preceding conditioning approach. First, no attainment of the infimum defining `d_sep` or the supremum defining `iota_sep` is assumed; (6) holds comparator by comparator, so approximate minimizing/maximizing sequences suffice. Second, unbounded vertical heights cause no norm-comparison loss because `J_s<=J_MT` is pointwise on the same compact spectral interval. Third, a comparator with large Montgomery--Taylor excess only strengthens (25) through the explicit `-Delta(P)` term. Fourth, simple-real bookkeeping is retained through `L(P)-L(W)>=0` rather than silently identifying the affine denominators. Fifth, (26) is asserted only in the relative near-extremizer regime `Delta/L->0`; a generic fatal configuration allowed by the coarser upper bound in `ANF-086` need not make the right side of (24) negative.

There is also an important negative control. Equation (18) does **not** prove that the required negative interference is impossible. Hilbert-space polarization permits arbitrarily strong destructive interference in principle, and the nonlinear separable class is not a convex subspace for which an orthogonal metric-projection theorem could simply force a sign. The remaining mathematics is therefore genuine: one must either rule out uniform macroscopic anti-alignment using the positive-multiset/exponential structure and the exact projection taxes of `ANF-088`, or construct such a family explicitly.

A targeted literature check covered the current Lamzouri/Alpöge--Furman Hilbert-space pair-correlation proofs, generic near-equality stability, metric projection onto Hilbert-space sets/cones, and polarization identities. Polarization and projection geometry are classical, but no source located supplies the line-specific identity (4) combined with the central-notch domination (5), the nonlinear separable quotient invariant (16), or the fatal anti-alignment threshold (24)--(26). No external theorem is load-bearing here beyond the already anchored Montgomery--Taylor/Lamzouri and central-notch inputs, so `SOURCES.md` is unchanged.

## Research consequence

The sparse-conditioning program should now stop treating a large generalized source/destination singular-value ratio as a candidate obstruction by itself. After quotienting by the actual separable geometry, **the only surviving physical mechanism is macroscopic negative Montgomery--Taylor interference**. The next decisive target is therefore an interference rigidity theorem: prove that every Montgomery--Taylor near-extremal positive multiset admits at least one compatible separable carrier `P` with `I_MT(W|P)=-o(L(P))`. Such a theorem, together with (18), would force `d_sep->0` and close the remaining central-notch near-extremizer gate. A contrary construction must explicitly defeat this by anti-aligning with every compatible product carrier; remote-padding or source-orthogonal surgeries are no longer viable candidates.
