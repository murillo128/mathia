# WI-374 — The gamma endpoint reserve expels the negative bulk debt from late arithmetic collars

**Status:** `EXACT-DERIVED + PRIMARY-SOURCE-CRITICAL-AUDIT + SPATIAL-REPAIR-CONSTRAINT + NON-ESTABLISHED-RH`.

## Claim

WI-369 reconstructs the exact gamma-corrected odd archimedean block from Marco Desogus's *The Three Gates: A Rooted-Operator Approach to Weil Positivity* (`arXiv:2609.20367v1`) in the normalized half-interval coordinate `u in (0,1)` as

\[
\mathcal A_A[f]+C_\Gamma\|f\|_2^2
=
D_A[f]
+\int_0^1\bigl(H(Au)+H(A(1-u))\bigr)|f(u)|^2\,du
+J_A[f],
\tag{1}
\]

where `D_A>=0`, `J_A>=0`,

\[
H(z)=\operatorname{artanh}(e^{-z/2})+\arctan(e^{-z/2}),
\qquad
C_\Gamma=\frac\pi2+\gamma+\log(8\pi),
\tag{2}
\]

and `H'(z)=-h(z)<0`. The uniform floor `-C_Gamma` is therefore a bulk statement, not an endpoint-local one. If a test function is supported in a right endpoint strip of physical width at most `r`,

\[
\operatorname{supp}f\subset\{u:A(1-u)\le r\},
\]

then

\[
\boxed{
\mathcal A_A[f]
\ge
\bigl(H(r)-C_\Gamma\bigr)\|f\|_2^2.
}
\tag{3}
\]

The same statement holds at the left endpoint with `Au<=r`.

This becomes directly relevant to Desogus's arithmetic endpoint induction. At endpoint `Y=j`, the physical localization radius is

\[
a_j=\frac12\log j.
\tag{4}
\]

Hence the step `k -> k+1` adds an outer physical collar of half-width

\[
a_{k+1}-a_k
=\frac12\log\frac{k+1}{k}
=\frac12 w_k,
\qquad
w_k:=\log\left(1+\frac1k\right).
\tag{5}
\]

After the odd fold, a function supported entirely in the newly added collar is supported near `u=1` with

\[
a_{k+1}(1-u)\le\frac12w_k.
\tag{6}
\]

Thus (3) gives the exact bound

\[
\mathcal A_{a_{k+1}}[f]
\ge
\left(H\!\left(\frac{w_k}{2}\right)-C_\Gamma\right)\|f\|_2^2
\ge
\bigl(H(w_k)-C_\Gamma\bigr)\|f\|_2^2.
\tag{7}
\]

Moreover

\[
\boxed{
H(w_k)
=
\log(\sqrt{k+1}+\sqrt k)
+
\arctan\sqrt{\frac{k}{k+1}}.
}
\tag{8}
\]

In particular a completely elementary enclosure proves

\[
\boxed{
H(w_k)>C_\Gamma
\qquad(k\ge16384).
}
\tag{9}
\]

Therefore every sufficiently late newly added arithmetic collar is already nonnegative for the **corrected gamma archimedean block itself**. The linear gamma-negative sector of WI-371--WI-373 is an inherited interior/bulk phenomenon; it is not recreated locally on each shrinking endpoint collar.

This materially narrows the repair question left by WI-369--WI-373. It is too crude to require every late new collar, or every new source born there, to pay the whole uniform debit `C_Gamma` or the full bulk negative-index profile. Any remaining obstruction must survive through the inherited old core, old--new coupling, or the true common-cut/rooted-Schur geometry. Equation (9) is only a compression statement: it does **not** prove that the Schur complement against the old core is nonnegative, does not validate Desogus's printed gamma cancellation, and does not establish RH.

## 1. The exact endpoint-strip coercivity is already present in WI-369's form

All terms on the right of (1) are nonnegative. On the support condition `A(1-u)<=r`, monotonicity of `H` gives

\[
H(A(1-u))\ge H(r).
\tag{10}
\]

Dropping `D_A`, `J_A`, and the other endpoint multiplier `H(Au)` therefore yields

\[
\mathcal A_A[f]+C_\Gamma\|f\|_2^2
\ge H(r)\|f\|_2^2,
\]

which is exactly (3). No compactness, spectral approximation, interval computation, or source hypothesis enters this step.

This also clarifies the relation to WI-369's sharp floor. Its quasimodes were deliberately supported in a fixed interior interval `[delta,1-delta]`. There both endpoint multipliers vanish exponentially as `A` grows. A shrinking boundary collar has the opposite geometry: its physical distance to the endpoint tends to zero, and `H` diverges there. The two statements are therefore complementary rather than contradictory.

## 2. Desogus's endpoint nesting places every new collar inside the positive boundary layer

The preprint uses `Y=e^{2a}` and advances through integer endpoints. Consequently (4)--(5) are exact. At the new endpoint `a_{k+1}`, rescale the positive half of the physical interval `(0,a_{k+1})` to `u in (0,1)`. The old positive half ends at

\[
u_k=\frac{a_k}{a_{k+1}},
\]

so the newly added positive collar is `u in (u_k,1)`. For every point in it,

\[
a_{k+1}(1-u)
\le a_{k+1}-a_k
=\frac12w_k,
\]

proving (6). Oddness pairs this right half-collar with the corresponding left physical collar, so the folded compression is exactly the relevant odd new-collar compression.

The second inequality in (7) is intentionally conservative. Since `H` is decreasing and `w_k/2<w_k`, the actual endpoint reserve is at least `H(w_k/2)`, but `H(w_k)` is simpler to enclose and already suffices for a finite explicit threshold.

## 3. A fully elementary finite threshold

Set

\[
q_k=e^{-w_k/2}=\sqrt{\frac{k}{k+1}}.
\]

Then

\[
\operatorname{artanh}(q_k)
=\frac12\log\frac{1+q_k}{1-q_k}
=\log(\sqrt{k+1}+\sqrt k),
\tag{11}
\]

which proves (8).

For `k>=16384=128^2`,

\[
\sqrt{k+1}+\sqrt k>256,
\]

so

\[
\operatorname{artanh}(q_k)>\log256=8\log2.
\tag{12}
\]

The positive `atanh` series at `1/3` gives

\[
\log2
=2\sum_{j\ge0}\frac{1}{(2j+1)3^{2j+1}}
>\frac{842}{1215}>rac{693}{1000}.
\tag{13}
\]

Also `q_k>=1/sqrt2>7/10`, and the alternating arctangent series gives

\[
\arctan(q_k)
>\arctan\frac7{10}
>
\frac7{10}-\frac{(7/10)^3}{3}
+\frac{(7/10)^5}{5}
-\frac{(7/10)^7}{7}
=
\frac{18225473}{30000000}
>
\frac{243}{400}.
\tag{14}
\]

Therefore

\[
H(w_k)
>8\frac{693}{1000}+\frac{243}{400}
=\frac{12303}{2000}.
\tag{15}
\]

For the opposite side, use the classical elementary bounds `pi<22/7` and `gamma<1`. Moreover

\[
e^{33/10}
>
\sum_{n=0}^{6}\frac{(33/10)^n}{n!}
=
\frac{2058466061}{80000000}
>
\frac{176}{7}
>8\pi,
\tag{16}
\]

so `log(8pi)<33/10`. Hence

\[
C_\Gamma
<\frac{11}{7}+1+\frac{33}{10}
=\frac{411}{70}.
\tag{17}
\]

Finally

\[
\frac{12303}{2000}>\frac{411}{70},
\]

which proves (9) with ample margin. The threshold is deliberately not optimized; its role is to certify the qualitative finite transition without introducing a numerical certificate into the claim.

## 4. Consequence for the gamma-repair program

WI-370 correctly rules out one conservative repair: discard the positive remainder of WI-369 everywhere, replace the corrected gamma block by the uniform floor `-C_Gamma I`, and try to pay that scalar debit from the existing MASTER scalar reserve. Equation (9) shows why that reduction is also spatially very lossy. On late new collars, the endpoint multiplier alone already pays more than `C_Gamma`; the local corrected block has no negative gamma debt there at all.

WI-371--WI-373 remain equally valid on the full normalized core. Their extensive negative sector is produced by interior modes whose wavelength is `O(1/A)` while staying a fixed physical distance from the endpoints in normalized coordinates. Those modes live in the inherited bulk as the localization radius grows. The exact next question is therefore not whether each fresh source coordinate has enough nominal scalar reserve, rank, or singular-value mass. It is whether the full source/common-cut/rooted-Schur operation controls the inherited interior negative band and the old--new cross terms.

This distinction matters for any attempted repair of the Desogus program. A positive compression on the new collar does not imply a positive Schur complement after coupling it to an indefinite old core. Conversely, the existence of a large full-core negative index does not imply that the newly activated collar contributes new negative directions. A successful audit must keep these two geometries separate.

## 5. Evidence and prior-art boundary

The exact corrected form (1) and its endpoint function `H` come from WI-369's independent reconstruction of the primary source's odd archimedean block. The endpoint nesting (4)--(6) is read directly from Desogus's `Y=e^{2a}` integer-endpoint induction. The deduction (3), the collar specialization (7), and the finite threshold (9) are exact consequences of those ingredients.

Primary source under audit: Marco Desogus, **The Three Gates: A Rooted-Operator Approach to Weil Positivity**, arXiv:2609.20367v1 (17 Sep 2026), especially the localized operator, the `Y=e^{2a}` endpoint parametrization, and the endpoint-nesting step. As checked during this audit, the public arXiv record remains version 1. A targeted search found no independent public treatment of the corrected gamma endpoint-strip consequence. That search result is recorded only as novelty-audit context; no priority claim is made.

This finding does not import the preprint's RH conclusion, its computer-assisted certificates, or its printed gamma-free collar identity as established evidence. It refines the local repair geometry after the source-level correction already established in WI-364 and WI-369.