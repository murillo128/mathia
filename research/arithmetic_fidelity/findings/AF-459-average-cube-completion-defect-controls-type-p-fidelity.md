# AF-459 — Average cube-completion defect controls type-p fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `SOURCE-LAW`, `QUANTITATIVE-FIDELITY`, `COMPLETED-SECANT`, `NO-NOVELTY-CLAIM`

## Claim

AF-458 shows that one exact completable paired `k`-cube inside a normalized source-law secant carrier transfers the Rademacher-type obstruction of the target into that restricted source law. Exact inclusion of all `2^k` sign orientations is stronger than necessary. The obstruction is quantitatively stable under incomplete or approximate source-side completion, and the relevant source invariant is an **average cube-completion defect**.

Let `A` be an alphabet with at least `2k` atoms. Work in the total-variation difference geometry

\[
\|h\|_{TV}=\|h\|_1
\]

on zero-mass signed atomic measures. Let

\[
C\subset\{h:\ h(A)=0,\ \|h\|_1=1\}
\tag{1}
\]

be a nonempty normalized completed-secant carrier, for example the AF-452 carrier of one fixed source-law fiber.

For a paired block of `2k` distinct atoms

\[
B=((a_1,b_1),\ldots,(a_k,b_k)),
\tag{2}
\]

define the ideal paired sign cube

\[
q^B_\varepsilon
=
\frac1{2k}\sum_{j=1}^k
\varepsilon_j(\delta_{a_j}-\delta_{b_j}),
\qquad
\varepsilon\in\{-1,+1\}^k.
\tag{3}
\]

Every `q^B_\varepsilon` has zero mass and `\ell^1` norm one. Define the mean completion defect of this block by

\[
D_B(C)
:=
\mathbb E_\varepsilon
\operatorname{dist}_1(q^B_\varepsilon,C),
\tag{4}
\]

and the best `k`-cube completion profile

\[
D_k(C)
:=
\inf_B D_B(C),
\tag{5}
\]

where the infimum runs over paired blocks of `2k` distinct atoms.

Let `Y` be a Banach space of Rademacher type `p in [1,2]`, with

\[
\mathbb E_\varepsilon
\left\|
\sum_j\varepsilon_j y_j
\right\|_Y
\le
T_p(Y)
\left(\sum_j\|y_j\|_Y^p\right)^{1/p}.
\tag{6}
\]

Let

\[
\phi:A\to Y,
\qquad
\sup_{a\in A}\|\phi(a)\|_Y\le M,
\tag{7}
\]

and extend `phi` affinely to probability laws. Write

\[
T_\phi h=\sum_{a\in A}h(a)\phi(a),
\qquad
\|T_\phi\|_{\ell^1\to Y}\le M.
\tag{8}
\]

Then the restricted lower gain on `C`,

\[
\kappa_C(F_\phi)
:=
\inf_{h\in C}\|T_\phi h\|_Y,
\tag{9}
\]

obeys, for every paired block `B`,

\[
\boxed{
\kappa_C(F_\phi)
\le
\frac{T_p(Y)}{2k}
\left(
\sum_{j=1}^k
\|\phi(a_j)-\phi(b_j)\|_Y^p
\right)^{1/p}
+
M D_B(C).
}
\tag{10}
\]

Consequently,

\[
\boxed{
\kappa_C(F_\phi)
\le
M\left[
T_p(Y)k^{1/p-1}+D_k(C)
\right].
}
\tag{11}
\]

Thus AF-458 is the zero-defect case `D_k(C)=0`, but exact cube inclusion is unnecessary. For `p>1`, any sequence of scales with

\[
D_k(C)\to0
\tag{12}
\]

forces `\kappa_C(F_\phi)=0` for a fixed carrier supporting arbitrarily large such blocks. More generally, for a family of source-law carriers `C_k`,

\[
D_k(C_k)\to0
\quad\Longrightarrow\quad
\kappa_{C_k}(F_\phi)\to0.
\tag{13}
\]

The contrapositive is a quantitative source-rigidity requirement. If `p>1` and a bounded affine representation has

\[
\kappa_C(F_\phi)\ge\kappa_0>0,
\tag{14}
\]

then at every admissible scale

\[
\boxed{
D_k(C)
\ge
\max\left\{
0,
\frac{\kappa_0}{M}-T_p(Y)k^{1/p-1}
\right\}.
}
\tag{15}
\]

Hence a source law that retains a complexity-independent discriminator in a nontrivial-type target must stay a **positive average TV distance from every large paired sign cube**. Merely deleting one or a few bad sign orientations does not provide an escape.

## Exact derivation

Fix a paired block `B`. For `delta>0` and each sign vector `epsilon`, choose `c_epsilon in C` such that

\[
\|c_\varepsilon-q^B_\varepsilon\|_1
\le
\operatorname{dist}_1(q^B_\varepsilon,C)+\delta.
\tag{16}
\]

Because every `c_epsilon` belongs to the normalized carrier,

\[
\kappa_C(F_\phi)
\le
\mathbb E_\varepsilon\|T_\phi c_\varepsilon\|_Y.
\tag{17}
\]

Use the triangle inequality and `(8)`:

\[
\begin{aligned}
\mathbb E_\varepsilon\|T_\phi c_\varepsilon\|_Y
&\le
\mathbb E_\varepsilon\|T_\phi q^B_\varepsilon\|_Y
+
M\,\mathbb E_\varepsilon
\|c_\varepsilon-q^B_\varepsilon\|_1\\
&\le
\mathbb E_\varepsilon\|T_\phi q^B_\varepsilon\|_Y
+M(D_B(C)+\delta).
\end{aligned}
\tag{18}
\]

Put

\[
d_j=\phi(a_j)-\phi(b_j).
\tag{19}
\]

Then

\[
T_\phi q^B_\varepsilon
=
\frac1{2k}\sum_{j=1}^k\varepsilon_j d_j.
\tag{20}
\]

Applying Rademacher type gives

\[
\mathbb E_\varepsilon\|T_\phi q^B_\varepsilon\|_Y
\le
\frac{T_p(Y)}{2k}
\left(\sum_{j=1}^k\|d_j\|_Y^p\right)^{1/p}.
\tag{21}
\]

Equations `(17)`--`(21)` and `delta downarrow 0` prove `(10)`. Since `\|d_j\|_Y\le2M`,

\[
\frac{T_p(Y)}{2k}
\left(\sum_j\|d_j\|_Y^p\right)^{1/p}
\le
T_p(Y)M k^{1/p-1}.
\tag{22}
\]

Apply `(22)` to blocks whose defects approach the infimum in `(5)` to obtain `(11)`.

The key point is that no correlation assumption is needed between target cancellation and source completion quality. Both quantities are averaged over the same uniform sign cube. The average of their sum is small, so at least one orientation simultaneously has sufficiently small retained gain after replacement by an actual carrier element. This is why the **mean** completion defect, rather than worst-orientation Hausdorff distance, is the natural sufficient quantity.

## Dense exact completion already suffices

The average-defect formulation weakens AF-458 even when no approximate secants are constructed explicitly. Suppose that for one paired block `B`, a subset

\[
G\subset\{-1,+1\}^k
\]

of sign orientations is exactly completable:

\[
q^B_\varepsilon\in C
\qquad(\varepsilon\in G),
\tag{23}
\]

and

\[
|G|\ge(1-\theta)2^k.
\tag{24}
\]

Because `C` is nonempty and both `q^B_epsilon` and every carrier element have `\ell^1` norm one,

\[
\operatorname{dist}_1(q^B_\varepsilon,C)\le2
\tag{25}
\]

for every missing orientation. Therefore

\[
D_B(C)\le2\theta,
\tag{26}
\]

and `(11)` sharpens to the directly checkable bound

\[
\boxed{
\kappa_C(F_\phi)
\le
M\left[
T_p(Y)k^{1/p-1}+2\theta
\right].
}
\tag{27}
\]

In particular, for `p>1`, exact completion of a `1-o(1)` fraction of the orientations of growing paired cubes already forces vanishing lower gain. A source law does **not** escape the type obstruction merely because each large cube has a small exceptional set of forbidden sign patterns.

Conversely, if `(14)` holds and exact completion occurs on a fraction at least `1-theta_k`, then `(27)` implies

\[
\theta_k
\ge
\frac12
\max\left\{
0,
\frac{\kappa_0}{M}-T_p(Y)k^{1/p-1}
\right\}.
\tag{28}
\]

So stable bounded affine fidelity in a nontrivial-type target requires a positive asymptotic density of sign orientations to remain non-completable, or else requires the missing orientations to be separated from the actual carrier by a comparable positive TV gap.

## What this adds to AF-452 and AF-458

AF-452 identifies the exact object that controls fixed-source-law conditioning: the normalized carrier of source-law secants that can actually be completed into the fiber. AF-458 then gives a finite sufficient certificate for collapse: one full paired sign cube inside that carrier.

AF-459 replaces the binary question

\[
q^B_\varepsilon\in C\ \text{for every }\varepsilon?
\]

by a quantitative source profile `D_k(C)`. This removes an artificial all-or-nothing gate. The arithmetic source law may fail exact cube completion at some orientations and still be too cube-rich to preserve a discriminator after bounded affine compression into a target of nontrivial type.

The resulting compatibility test has two independent terms:

\[
\boxed{
\text{retained gain}
\ \lesssim\
\text{target type cancellation}
+
\text{source cube-completion defect}.
}
\tag{29}
\]

The first is target geometry. The second is intrinsic to the normalized source-law secant carrier. A positive lower gain can survive only if the source geometry contributes enough defect to offset the target's increasingly strong cancellation.

This is also the correct normalization for AF-452: distance is measured between normalized secant directions, so common completion weights and common positive backgrounds have already canceled before `D_k(C)` is evaluated.

## Prior art and novelty audit

The Banach-space and discrete-cube ingredients are classical, and this finding makes **no novelty claim** for Rademacher type, sign-cube averaging, or stability under perturbation.

- Paata Ivanisvili, Ramon van Handel, and Alexander Volberg, **“Rademacher type and Enflo type coincide,”** *Annals of Mathematics* 192(2), 665--678 (2020), DOI `10.4007/annals.2020.192.2.8`. Their theorem establishes that Banach-space Rademacher type has an equivalent metric discrete-cube formulation and uses a dimension-free Pisier inequality. This is direct prior art for treating sign-cube geometry as a metric probe of target type.
- Grigory Ivanov, **“No-dimension Tverberg's theorem and its corollaries in Banach spaces of type p,”** *Bulletin of the London Mathematical Society* 53(2), 631--641 (2021), DOI `10.1112/blms.12449`. Ivanov derives approximate Radon/Tverberg/Caratheodory statements in type-`p` Banach spaces with the same exponent `1/p-1`, explicitly placing approximation error next to dimension-free combinatorial geometry.

The estimate `(18)` is only the operator triangle inequality, and `(21)` is the classical type inequality. The line-specific step is to apply those facts to the AF-452 completed-secant carrier and package source-side deviation from AF-458's exact cube certificate as the profile `(4)`--`(5)`. The cited prior art supports the target/cube mechanism but does not need to be reinterpreted as a new compression theory.

The fresh literature check also reinforces an important boundary: approximate/no-dimension convex geometry already studies how type controls errors when exact intersection or exact sparse representation is relaxed. AF-459 should therefore be read as a source-law specialization and quantitative audit tool, not as a new Banach-space theorem.

## Boundary and falsification audit

- **Affine/barycentric boundary.** The theorem acts on the linear signed-difference operator `T_phi`. An arbitrary nonlinear encoder of the entire law is outside its scope.
- **TV / `ell^1` source geometry is substantive.** The perturbation term is controlled by `\|T_phi\|_{ell^1 to Y}<=M`. A different source norm needs its own operator bound and its own normalized cube geometry; AF-452 already warns that changing the source metric changes the conditioning question.
- **The profile is sufficient, not complete.** Large `D_k(C)` does not prove positive fidelity. Other families of carrier secants can still have arbitrarily small gain.
- **The infimum over pairings is deliberate.** To import the obstruction it is enough to find one paired atom block with small mean defect. Stable fidelity therefore requires every large candidate block to stay quantitatively cube-poor.
- **Mean defect is weaker than full Hausdorff control.** One badly missing sign orientation does not block `(11)` if its contribution to the uniform average is negligible. This is a feature of the Rademacher averaging argument, not an omission.
- **`p=1` remains the boundary.** The type term in `(11)` does not decay for `p=1`; approximate cube richness alone yields no complexity-decay conclusion there. This is consistent with the `ell^1` fidelity boundary in AF-456.
- **Finite alphabets impose a cutoff.** `D_k(C)` is relevant only while `2k` distinct atoms are available.
- **Normalization matters.** The bound uses the AF-452 unit secant carrier. Measuring distance before normalization would mix completion weights into the defect and would not represent the fixed-fiber lower-Lipschitz problem.
- **No converse sufficiency is claimed.** Equation `(15)` is necessary source separation for one positive-gain bounded affine representation; it does not say that a carrier satisfying that separation admits such a representation.

## Arithmetic specialization

For a rational-prime source law, let `C` be the normalized completed secant carrier induced by the actual arithmetic constraints, rather than the unrestricted simplex of prime mixtures. AF-458 required proving a full paired prime cube inside `C`. AF-459 gives a strictly weaker target.

For paired distinct primes

\[
(p_1,q_1),\ldots,(p_k,q_k),
\]

form the ideal balanced prime secants

\[
q_\varepsilon
=
\frac1{2k}\sum_{j=1}^k
\varepsilon_j(\delta_{p_j}-\delta_{q_j}).
\tag{30}
\]

It is enough to show that, for growing `k`, these ideal cube directions can be chosen so that their **average** TV distance to genuinely completable arithmetic secants tends to zero. If so, every bounded affine prime mark into a Banach target of nontrivial type loses a uniform TV discriminator along that source-law family.

This substantially lowers the source-side burden. The arithmetic investigation no longer has to realize all `2^k` orientations exactly. It may instead look for asymptotically dense exact completion, approximate completion of most orientations, or any other mechanism driving `D_k(C)` downward.

If the physical prime source law resists this, `(15)` says what the surviving resource must look like: it must exclude every large paired sign cube by a positive **average normalized-secant distance**, not merely by isolated exceptional sign patterns. That is a concrete arithmetic rigidity property which can now be tested before downstream spectral, positive, quotient, or asymptotic compression is attempted.

## Consequence for the line

The paired-cube frontier is no longer binary. The reusable obstruction is

\[
\boxed{
D_k(C)\to0
+
\text{target type }p>1
\Longrightarrow
\text{bounded affine TV fidelity collapses}.
}
\tag{31}
\]

The next source-law question is therefore sharper than AF-458's exact-cube test: determine the asymptotic completion profile `D_k(C)` of the actual arithmetic carrier. Exact cube inclusion is one extreme, but an asymptotically vanishing mean defect is already enough to transfer the same qualitative obstruction.