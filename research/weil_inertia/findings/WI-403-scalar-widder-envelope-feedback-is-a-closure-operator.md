# WI-403 — scalar Widder envelope feedback is a closure operator

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-AUDITED + SHARP-STRUCTURAL-BARRIER`.

**Parent findings:** [WI-399](./WI-399-widder-root-growth-gives-effective-shift-bootstrap.md), [WI-400](./WI-400-widder-root-profile-exactly-recovers-horizontal-defect-width.md), [WI-401](./WI-401-widder-sampling-mesh-has-exact-horizontal-resolution.md), [WI-402](./WI-402-widder-sampled-root-bounds-have-exact-mesh-margin-resolution-law.md).

## Claim

The height-dependent zero-free-width route left open after WI-399 does **not** produce a self-improving Widder bootstrap if it is fed back only through the same scalar fixed-height maximum. The obstruction is more general than WI-400's constant-width identity: for an arbitrary admissible set of possible zero parameters, the operation

\[
\text{zero geometry}
\longrightarrow
\text{sharp scalar Widder envelope}
\longrightarrow
\text{zero geometry compatible with that envelope}
\]

is a closure operator. It is extensive, monotone, and idempotent. Consequently it can preserve or lose zero-side information, but it can never sharpen the zero geometry from which its own sharp scalar envelope was derived.

For

\[
\rho=\frac12+\delta+i\gamma,
\qquad d:=|\delta|,
\]

write the one-zero response from WI-399 as

\[
r_{\gamma,d}(T)
:=
4T^2\frac{\gamma^2+d^2}
{(T^2+\gamma^2-d^2)^2+4\gamma^2d^2},
\qquad T\ge2.
\tag{1}
\]

Let

\[
\Omega
:=
\{(\gamma,d):\gamma>0,\ 0\le d<1/2\}
\]

be the geometric parameter space. For any admissible subset `A` of `Omega`, define its clipped sharp scalar envelope

\[
C_A(T)
:=
\max\left\{1,\sup_{(\gamma,d)\in A}r_{\gamma,d}(T)\right\},
\tag{2}
\]

and, for any function `C(T)>=1`, define the set compatible with all scalar root bounds

\[
\Gamma(C)
:=
\{(\gamma,d)\in\Omega:
 r_{\gamma,d}(T)\le C(T)\ \text{for every }T\ge2\}.
\tag{3}
\]

The feedback map

\[
\mathfrak F(A):=\Gamma(C_A)
\tag{4}
\]

satisfies

\[
\boxed{A\subseteq\mathfrak F(A)},
\qquad
\boxed{A\subseteq B\Longrightarrow\mathfrak F(A)\subseteq\mathfrak F(B)},
\qquad
\boxed{\mathfrak F(\mathfrak F(A))=\mathfrak F(A)}.
\tag{5}
\]

Thus no deterministic height-dependent width profile, verified-height region, piecewise zero-free region, or other geometric exclusion set can become strictly stronger merely by taking its sharp scalar Widder envelope and feeding that envelope back through the same one-zero response.

In particular, if

\[
A_b
:=
\{(\gamma,d):0\le d\le b(\gamma)\}
\tag{6}
\]

for any profile `b`, and one defines the recovered boundary

\[
b^+(\gamma)
:=
\sup\{d:(\gamma,d)\in\mathfrak F(A_b)\},
\tag{7}
\]

then wherever the boundary point belongs to the profile class,

\[
\boxed{b^+(\gamma)\ge b(\gamma)}.
\tag{8}
\]

A strict defect-to-zero contraction therefore requires information not implied by the starting geometry itself: for example a signed-prime estimate strictly below `C_A` at load-bearing heights, a coupled multi-height or phase observable, zero-population information, or another independent invariant.

No improved simple-critical-zero proportion and no proof of RH is claimed.

## 1. Exact proof of the closure law

The first inclusion in (5) is immediate but decisive. If `x=(gamma,d)` lies in `A`, then by definition of the supremum

\[
r_x(T)\le C_A(T)
\qquad\text{for every }T\ge2.
\]

Hence `x` lies in `Gamma(C_A)=F(A)`, proving extensivity.

If `A subseteq B`, then

\[
C_A(T)\le C_B(T)
\qquad(T\ge2),
\]

so every point satisfying all bounds `r_x(T)<=C_A(T)` also satisfies the weaker family `r_x(T)<=C_B(T)`. This proves monotonicity.

For idempotence, extensivity first gives

\[
C_A(T)\le C_{\mathfrak F(A)}(T).
\tag{9}
\]

But every point `x` in `F(A)` satisfies

\[
r_x(T)\le C_A(T)
\]

for every `T`. Taking the supremum over `x in F(A)` and clipping at one therefore gives the reverse inequality

\[
C_{\mathfrak F(A)}(T)\le C_A(T).
\tag{10}
\]

Thus

\[
\boxed{C_{\mathfrak F(A)}=C_A},
\tag{11}
\]

and applying `Gamma` once more proves

\[
\mathfrak F(\mathfrak F(A))
=
\Gamma(C_{\mathfrak F(A)})
=
\Gamma(C_A)
=
\mathfrak F(A).
\]

No property special to a constant strip width was used. The result depends only on using a pointwise supremum of the same scalar response that is later inverted.

## 2. Why the theorem applies to the prime-side Widder criterion

WI-399 independently reconstructed the fixed-height prime/zero interface

\[
\boxed{
\max\{1,L_{\mathcal P}(T)\}
=
\max\{1,\mathcal R_Z(T)\}
}
\tag{12}
\]

where `Z` is the actual zero geometry and

\[
\mathcal R_Z(T)
=
\sup_{(\gamma,d)\in Z}r_{\gamma,d}(T).
\]

Suppose the only zero-side input is

\[
Z\subseteq A.
\tag{13}
\]

Then (2) and (12) imply the scalar prime bound

\[
\max\{1,L_{\mathcal P}(T)\}
\le C_A(T).
\tag{14}
\]

If one now treats (14) as new input and translates it back to zero geometry through the same fixed-height response, the strongest conclusion available at this interface is only

\[
Z\subseteq\Gamma(C_A)=\mathfrak F(A).
\tag{15}
\]

But (5) gives `A subseteq F(A)`. Therefore this feedback cannot replace (13) by a smaller admissible set. At best `A` was already closed and is reproduced exactly; otherwise the scalar maximum has discarded information and the recovered class is larger.

This identifies the exact novelty gate for a genuine Widder bootstrap. A prime-side theorem is useful only if it proves a profile `D(T)` that is **strictly stronger than the geometry-implied envelope** in a way that removes at least one boundary configuration:

\[
D(T)\le C_A(T)
\quad\text{for all }T,
\qquad
D(T)<C_A(T)
\quad\text{at load-bearing heights}.
\tag{16}
\]

Such a strict inequality cannot follow from `Z subseteq A` by the scalar supremum argument alone. It represents genuinely new arithmetic cancellation or independent structural information.

## 3. Constant width is only the first special case

WI-400 considered

\[
A_a
=
\{(\gamma,d):0\le d\le a\}
\]

and showed by explicit saddle calculation that its sharp scalar envelope is

\[
C_{A_a}(T)=M(a/T),
\qquad
M(\sigma)=\frac{2}{1+\sqrt{1-4\sigma^2}},
\]

with exact recovery of the same width `a`. That result is therefore the constant-profile case in which the closure `F(A_a)` happens to retain exactly the boundary statistic being tracked.

The present finding is stronger in a different direction: **no regularity, monotonicity, or explicit formula for the boundary is required**. The admissible set may encode a height-dependent zero-free region, exact verification below a height, several disjoint forbidden regions, or any other deterministic geometric information. Once that information is compressed to the scalar pointwise maximum (2), feeding it back cannot sharpen the original set.

WI-401 and WI-402 fit the same information picture. Their sampled threshold and mesh--margin laws quantify what happens when only part of a scalar envelope is controlled. The closure theorem says that even complete control of the sharp envelope generated by an existing geometric profile is not a contraction mechanism. Finer sampling cannot change that fact unless the certified values beat the geometry-implied envelope.

## 4. Consequence for current explicit zero-free regions

The Rafik preprint already uses height-dependent zero-free information in several ways. Proposition A3 maps any classical zero-free region into analytic continuation of the terminal real semicircle; Theorem A5 uses the Platt--Trudgian verification through

\[
H_*=3\cdot10^{12}
\]

to obtain exact fixed-height root control below that scale; and Appendix B combines the verified height with a classical zero-free width to obtain finite-order Widder positivity.

For example, a classical region

\[
\zeta(\sigma+it)\ne0
\qquad
\left(\sigma\ge1-\frac1{R\log t}\right)
\tag{17}
\]

implies, by functional equation symmetry,

\[
d\le b_R(\gamma)
:=
\frac12-\frac1{R\log\gamma}
\tag{18}
\]

in its range. One may combine this with the verified-height input into an admissible set `A_{R,H_*}` having `d=0` below `H_*` and `d<=b_R(gamma)` above it.

The published Mossinghoff--Trudgian--Yang input used by Rafik has `R=5.558691`; the newer Bellotti--Trudgian--Yang 2026 preprint gives `R=4.896`. The latter was checked again during this audit at arXiv:2603.21490 and remains a March 2026 preprint. Rafik's version 2, posted 17 September 2026, explicitly distinguishes the published and preprint constants.

Applying (5) to `A_{R,H_*}` gives a decisive negative conclusion:

\[
\boxed{
\text{verified height + height-dependent zero-free width}
\not\Rightarrow
\text{a stricter zero-free geometry by scalar Widder feedback alone}.
}
\tag{19}
\]

The known zero-free region remains useful: it enlarges the analytically controlled terminal collar and strengthens finite-order positivity. What it cannot do is bootstrap itself into a smaller horizontal defect merely by being encoded in, and then decoded from, the same scalar root envelope.

This removes a possible ambiguity in the post-WI-399 frontier. A height-dependent zero-free width is not, by itself, the missing extra invariant. It becomes useful for contraction only if coupled to an arithmetic estimate that is stronger than the sharp scalar envelope implied by that width, or to information that is not compressed into a pointwise maximum over individual zero responses.

## 5. Prior-art audit and provenance

The direct recent source remains Zeraoulia Rafik, *Uniform Beta Smoothing of Widder Sums for the Riemann xi-Function and a Schur--Triple Application to Simple Critical Zeros*, Preprints.org manuscript `202609.1018`, version 2, posted 17 September 2026:

<https://www.preprints.org/manuscript/202609.1018>

The source is explicitly non-peer-reviewed. Proposition A1 and Lemma A1 supply the fixed-height zero/prime root interface independently rederived in WI-399. Proposition A3 uses a classical height-dependent zero-free region to penetrate the terminal semicircle. Theorem A5 transfers the published finite-height RH verification to exact root control below that height. Appendix B uses the same zero-free information to enlarge the range of finite-order Widder positivity. Remark A4 explicitly says that crossing the remaining terminal arc requires new information about `-zeta'/zeta` in `1/2<Re s<=1` rather than algebraic resummation alone.

The current 2026 classical-shape zero-free input is Chiara Bellotti, Tim Trudgian, and Andrew Yang, *Zero-free regions inspired by work of Heath-Brown*, arXiv:2603.21490, posted 23 March 2026, proving the preprint region `sigma>1-1/(4.896 log t)` for `t>=3`:

<https://arxiv.org/abs/2603.21490>

For a fully published input, Mossinghoff, Trudgian, and Yang, *Explicit zero-free regions for the Riemann zeta-function*, Research in Number Theory 10 (2024), gives the classical constant `5.558691` used in Rafik's published-input theorem:

<https://doi.org/10.1007/s40993-023-00498-y>

A targeted audit around the Rafik appendix, fixed-height root growth, explicit zero-free regions, and feedback/iteration found the source's one-way uses of height-dependent zero-free information but no statement of the abstract envelope--inverse closure law (5). This absence is recorded only as a novelty audit, not as a priority claim. The closure proof itself is elementary order theory once the scalar response interface is isolated.

## 6. Barrier scope and falsification

The finding is deliberately narrow.

It does **not** say that zero-free regions are useless to Widder methods. They improve finite-order sector bounds, analytic-continuation collars, and any arithmetic estimate that can exploit their location information without collapsing it to the same scalar maximum.

It does **not** say that the prime root profile cannot beat `C_A`. Such a theorem is exactly what would be needed for progress. The point is that a strict improvement cannot be justified merely by reusing the geometric assumption `Z subseteq A`; it must come from signed prime cancellation, cross-height coupling, phase, density/correlation information, or another independent theorem.

It also does not assert that every point of an abstract admissible set `A` is realizable by a genuine zeta zero set satisfying the full explicit formula. The closure theorem is an information-interface barrier: if the proof retains only the membership statement `Z subseteq A` and then replaces `A` by its pointwise scalar supremum, no subsequent inversion of that same supremum can certify a smaller set.

A falsifier would be an argument that starts only from `Z subseteq A`, uses no additional arithmetic or joint zero information, proves the sharp scalar bound `C_A`, and then derives a zero parameter outside `F(A)` or a strict subset of `A`. Equations (2)--(5) rule this out identically.

## Research consequence

The post-WI-402 Widder frontier should therefore drop **height-dependent zero-free width by itself** from the list of possible bootstrap resources. The live arithmetic target is sharper: prove a signed-prime/root bound lying strictly below the geometry-implied envelope at the `O(d^2/\gamma^2)` margin scale identified by WI-402, or introduce a genuinely coupled observable that does not factor through the scalar pointwise maximum.

This is a decisive negative result for one named route, not a numerical improvement.