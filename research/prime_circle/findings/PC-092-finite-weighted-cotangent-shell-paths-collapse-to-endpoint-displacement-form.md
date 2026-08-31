# PC-092 — finite weighted cotangent shell paths collapse to endpoint displacement form

**Status:** `EXACT-DERIVED` + `STRUCTURAL-COLLAPSE` + `DECISIVE-BOUNDARY` for finite serial words built from the intrinsic Prime-Circle cotangent kernel, exact-order shell restrictions, and arbitrary shell-local diagonal weights. PC-089 showed that one unweighted intermediate shell collapses to endpoint cyclotomic potentials. The weighted identity below removes the main escape left there: inserting nonconstant geometry-derived weights does not restore an irreducible interior tensor, and iterating finitely many weighted shell propagations stays in a small endpoint-generated matrix algebra.

This does **not** say that the resulting endpoint profiles are arithmetically trivial, that their cross-level organization is classical, or that every nonlinear cotangent construction is exhausted. The obstruction is specifically to **finite serial propagation through shell-local diagonal memories**. Branching tensor networks, genuinely different geometric operators, nonlinear operations not expressible by such serial matrix products, infinite-depth limits, Hardy/Hankel operators, and global uniformization/monodromy remain outside the theorem.

## 1. Weighted two-hop identity

For distinct points `z,w` on the unit circle use the intrinsic oriented cotangent kernel

\[
K(z,w)=i\cot\!\left(\frac{\theta_z-\theta_w}{2}\right)
=-\frac{z+w}{z-w},
\qquad K(z,z)=0.
\]

Let `B` be a finite set disjoint from the endpoints and let `f:B->C` be **arbitrary**. Define

\[
(T_Bf)(z)=\sum_{u\in B}f(u)K(z,u),
\qquad
s_B(f)=\sum_{u\in B}f(u).
\]

The three-point identity from PC-089,

\[
K(z,u)K(u,w)
=K(z,w)\bigl(K(z,u)+K(u,w)\bigr)-1,
\]

can be multiplied by `f(u)` and summed over `u`. Since `K(u,w)=-K(w,u)`, this gives the exact weighted formula

\[
\boxed{
\sum_{u\in B}f(u)K(z,u)K(u,w)
=K(z,w)\bigl((T_Bf)(z)-(T_Bf)(w)\bigr)-s_B(f).
}
\]

No condition is imposed on `f`; in particular it may be a shell potential, a chord-derived profile, a previous endpoint transform, or any other geometry-forced diagonal weight.

For finite endpoint sets `A,C` disjoint from `B` and from one another, let `K_{A,B}` denote the restricted kernel matrix and `D_f` the diagonal matrix on `B`. Then

\[
\boxed{
K_{A,B}D_fK_{B,C}
=D_{T_Bf|_A}K_{A,C}
-K_{A,C}D_{T_Bf|_C}
-s_B(f)J_{A,C}.
}
\]

Thus a weighted intermediate shell still leaves only the **direct endpoint cotangent block**, endpoint scalar profiles, and a separable rank-one term.

## 2. Return paths add only an endpoint-local diagonal correction

If the two endpoint sets coincide, the off-diagonal entries obey the same identity but the zero-diagonal convention must be restored explicitly. Put

\[
(Q_Bf)(z)=\sum_{u\in B}f(u)K(z,u)^2.
\]

For `A` disjoint from `B`, direct evaluation of the diagonal gives

\[
(K_{A,B}D_fK_{B,A})(z,z)=-(Q_Bf)(z).
\]

Hence the exact return formula is

\[
\boxed{
K_{A,B}D_fK_{B,A}
=D_{T_Bf|_A}K_{A,A}
-K_{A,A}D_{T_Bf|_A}
-s_B(f)J_{A,A}
+D_{s_B(f)-Q_Bf|_A}.
}
\]

The additional information created by closing the path is therefore **endpoint-local diagonal data**, not a new tensor indexed by the interior shell.

For `f=1` and distinct endpoints, Section 1 reduces exactly to PC-089. PC-092 is therefore a strict extension rather than a different kernel construction.

## 3. Finite serial weighted paths are closed under endpoint displacement

For disjoint finite root sets `A,C`, define the endpoint-displacement class

\[
\mathcal E(A,C)
=
\left\{
\sum_{j=1}^{r}D_{a_j}K_{A,C}D_{c_j}
+
\sum_{k=1}^{t}u_kv_k^{\mathsf T}
\right\}.
\]

When `A=C`, allow in addition endpoint diagonal matrices. The number of summands is part of the representation; the point is that it will depend on **path depth, not shell cardinality**.

Take `X in E(A,B)` and `Y in E(B,C)` and insert an arbitrary diagonal weight `D_f` on the intermediate set `B`. Expanding `XD_fY` term by term gives four cases.

1. A direct-kernel term times a direct-kernel term has the form
   \[
   D_aK_{A,B}D_gK_{B,C}D_c,
   \]
   and the weighted identity of Section 1 reduces it to two endpoint-weighted copies of `K_{A,C}` plus one rank-one term; when `A=C`, Section 2 adds only an endpoint diagonal term.
2. A rank-one term times a direct-kernel term remains rank one.
3. A direct-kernel term times a rank-one term remains rank one.
4. A rank-one term times a rank-one term remains rank one.

Therefore

\[
\boxed{
X\in\mathcal E(A,B),\quad
Y\in\mathcal E(B,C)
\quad\Longrightarrow\quad
XD_fY\in\mathcal E(A,C),
}
\]

with the stated diagonal extension for returns.

By induction, every finite serial shell path

\[
\boxed{
K_{S_0,S_1}D_{f_1}K_{S_1,S_2}D_{f_2}\cdots
D_{f_{m-1}}K_{S_{m-1},S_m}
}
\]

through pairwise distinct exact-order shells belongs to `E(S_0,S_m)`. For a simple non-returning path with `m` cotangent propagators, one may choose a representation with at most

\[
\boxed{2^{m-1}}
\]

endpoint-weighted direct-kernel terms and at most

\[
\boxed{2^{m-1}-1}
\]

rank-one terms. These bounds are crude but, crucially, **independent of every shell size**. If the path closes, only endpoint diagonal corrections are added.

So adding a second, third, or any fixed finite number of weighted exact-order shell memories does not generate a new interior matrix species. It recursively renormalizes endpoint profiles and separable corrections.

## 4. The algebraic reason is Cauchy-like displacement structure

The same collapse has a coordinate-free matrix warning. Let

\[
Z_A=\operatorname{diag}(z:z\in A),
\qquad
Z_B=\operatorname{diag}(w:w\in B).
\]

For a cotangent block,

\[
(z-w)K(z,w)=-(z+w),
\]

and therefore

\[
\boxed{
Z_AK_{A,B}-K_{A,B}Z_B
=-x_A\mathbf1_B^{\mathsf T}
-\mathbf1_Ax_B^{\mathsf T}.
}
\]

Its Sylvester displacement rank is at most two. Shell-local diagonal weights commute with their node diagonal, and serial products inherit bounded displacement complexity depending on path depth. This is exactly the structural regime of classical Cauchy-like/displacement-structured matrix theory, so low displacement complexity itself is not a new arithmetic invariant.

This viewpoint is only a prior-art/structure check; the stronger Prime-Circle statement above is the explicit cotangent composition formula, which identifies the surviving data as endpoint profiles rather than merely bounding a matrix rank.

## 5. Exact-order shells do not rescue the serial construction

Now specialize every `S_j` to a complete primitive shell `P_{n_j}^*`. PC-089 already gives, for the unweighted transform,

\[
(T_{P_r^*}1)(z)
=\varphi(r)-2z\frac{\Phi_r'(z)}{\Phi_r(z)}.
\]

With nonconstant weights, later transforms may be more complicated and can retain genuine arithmetic dependence. PC-092 does **not** claim that these functions reduce to one cyclotomic logarithmic derivative. What is exact is the information-flow statement:

\[
\boxed{
\text{finite serial shell memory}
\longrightarrow
\text{endpoint profiles + direct endpoint }K
\text{ + separable/diagonal terms}.
}
\]

Consequently, a nonzero two-prime path defect obtained merely by adding finitely many shell-local diagonal insertions is not by itself evidence for a new curvature, associator, or holonomy. One must first show that the claimed invariant survives this endpoint-displacement normal form.

The theorem is also prime-blind at the mechanism level: the weighted two-hop identity holds for **any finite intermediate set of distinct circle points**, not only primitive shells. Primality can enter the values of the endpoint transforms, but it does not alter the serial composition law.

## 6. Prior-art and novelty audit

No historical novelty is claimed for the abstract matrix mechanism.

- The weighted two-hop formula is an immediate linear consequence of the elementary cotangent addition identity already used in PC-089.
- The algebraic representation `K(z,w)=-(z+w)/(z-w)` places these blocks in the classical Cauchy-like/displacement-structured matrix setting. A directed audit of that literature confirms that low Sylvester displacement rank and its stability under products are standard structured-matrix phenomena, so they cannot be presented as a new Prime-Circle spectral mechanism.
- Girstmair's character-coordinate treatment, Beck's Dedekind-cotangent framework, and the finite cotangent-matrix literature already anchored in `research/prime_circle/SOURCES.md` are further warnings that finite rational-angle cotangent algebra is highly classicalized.
- Lewis--Zagier remains an essential counter-warning: a different **cross-scale/asymptotic** rational-cotangent matrix family can encode GRH. Therefore the present theorem must not be inflated into a blanket no-go for cotangent matrices or for cross-level limits.

The durable contribution is the research-specific boundary: the exact serial shell-memory family explicitly left open by PC-089 closes under endpoint displacement even with arbitrary intermediate diagonal weights.

## 7. Stress tests and falsification controls

The claim is finite and directly auditable.

1. For arbitrary distinct unit-circle points `z,u,w` and any scalar `f(u)`, verify the weighted three-point identity termwise.
2. For random finite disjoint sets `A,B,C` and arbitrary complex diagonal `D_f`, compare `K_AB D_f K_BC` entrywise with the formula in Section 1.
3. For a return `A=C`, check that the off-diagonal formula is unchanged and that the diagonal correction is exactly `D_{s_B(f)-Q_Bf}`.
4. Compose three or more blocks with independent diagonal weights and recursively reduce them; no term other than endpoint-weighted `K`, separable rank-one terms, and return diagonals may appear.
5. Replace primitive shells by matched non-prime finite root sets. The composition law must remain identical; only the endpoint transforms may change.

Any counterexample to the weighted two-hop identity refutes the theorem. A candidate carrying new arithmetic solely in an endpoint transform does **not** refute it; such a candidate would instead have to prove that a later cross-level or nonlinear use of those endpoint data escapes the stated finite serial class.

## 8. Consequence for the surviving cocycle clue

The accepted `CLUE-preimage-tube-fiber-sector-cocycle` had survived PC-089 specifically by allowing at least two weighted intermediate shells or a distinct multi-operator tensor. The first alternative is now closed for the canonical cotangent propagator:

\[
\boxed{
\text{any fixed finite serial word of }K
\text{ with shell-local diagonal weights}
\in\mathcal E(\text{endpoints}).
}
\]

Together with PC-090 and PC-091, this gives a sharper hierarchy:

- odd fully contracted cotangent loops vanish by reflection;
- even fully contracted finite exact-shell scalars are Galois-rational;
- before contraction, finite **serial** weighted cotangent shell paths have endpoint-displacement normal form.

A genuinely surviving finite-dimensional clue candidate must therefore be non-serial/branching, use a genuinely different intrinsic operator or tensor, or prove that an endpoint profile itself participates in a cross-level construction outside this normal form. Infinite-depth limits, Hardy/Hankel words, and global uniformization remain separate branches. PC-092 introduces no spectral parameter, functional equation, gamma factor, or critical-line selector.
