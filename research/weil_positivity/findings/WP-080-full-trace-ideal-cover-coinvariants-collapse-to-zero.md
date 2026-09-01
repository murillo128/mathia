# WP-080 — Full trace-ideal cover coinvariants collapse to zero

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + STANDARD-SCHATTEN-DUALITY + MATHIA-SPECIALIZATION`.

`WP-079` classified the canonical cover-coinvariant quotient on the **diagonal** trace ideal and left open a specific escape: perhaps enlarging the coefficient space to retain off-diagonal/internal operator data would produce nontrivial coinvariants capable of carrying cross-prime or archimedean information. For the most direct enlargement — the full trace class, or more generally any standard Schatten/compact ideal, with the same cover transfer already forced by the positive cocycle of `WP-076`--`WP-078` — the escape fails more strongly than in the diagonal model.

Let

\[
H=\ell^2(\mathbb N_0),
\qquad
W_n e_k=\frac1{\sqrt n}\sum_{r=0}^{n-1}e_{nk+r},
\qquad n\ge2,
\]

and let the canonical cover transfer be

\[
\boxed{
\rho_n(X):=nW_n^*XW_n.
}
\tag{1}
\]

This is exactly the action for which the positive pointed-cover defects satisfy

\[
Q_{mn}=\rho_n(Q_m)+Q_n.
\]

Then for every fixed `n>1`,

\[
\boxed{
\overline{\operatorname{ran}(I-\rho_n)}^{\|\cdot\|_1}
=\mathcal S_1(H).
}
\tag{2}
\]

Consequently the Hausdorff coinvariant quotient of the full trace class is zero:

\[
\boxed{
\mathcal S_1(H)
\Big/
\overline{\operatorname{span}}
\{\rho_mX-X:m\ge2,\ X\in\mathcal S_1(H)\}
=0.
}
\tag{3}
\]

The same conclusion holds on the real self-adjoint part and, with the corresponding norm closure, on every Schatten class `S_p(H)`, `1<=p<infinity`, and on the compact operators `K(H)`.

Equivalently, every bounded linear readout from any of these spaces that is invariant under even **one** degree-`n` cover transfer is zero. In particular, merely enlarging `WP-079` from diagonal trace-class observables to ordinary non-diagonal operator ideals does not preserve the one-dimensional trace class and add new coherence; it destroys the last scalar coinvariant as well. The positive prime-power classes of `WP-078` become zero together with every mixed-prime class.

This is a no-go only for **zeroth Hausdorff coinvariants of the canonical transfer (1) on standard operator ideals**. It does not rule out higher homology/cohomology, a nontrivial coefficient module, a different geometric action, a selective quotient, an unbounded/non-Hausdorff invariant, a nonlinear rank/volume mechanism, or a finite--archimedean coupling introduced before quotienting.

## 1. Off-diagonal coherence destroys the trace invariant

On matrix units

\[
E_{ij}=|e_i\rangle\langle e_j|,
\]

the transfer (1) is completely explicit. Since

\[
W_n^*e_{na+r}=\frac1{\sqrt n}e_a,
\qquad 0\le r<n,
\]

one obtains

\[
\boxed{
\rho_n(E_{ij})
=E_{\lfloor i/n\rfloor,\lfloor j/n\rfloor}.
}
\tag{4}
\]

Equivalently, for an arbitrary matrix `X`,

\[
(\rho_nX)_{ab}
=
\sum_{r,s=0}^{n-1}X_{na+r,\,nb+s}.
\tag{5}
\]

The diagonal algebra used in `WP-079` is invariant because (5) reduces there to the block-sum map

\[
(\rho_nd)_a=\sum_{r=0}^{n-1}d_{na+r},
\]

and ordinary trace is preserved on that restricted algebra.

But trace is **not** invariant on the full trace class. Already for degree two,

\[
\rho_2(E_{01})=E_{00},
\tag{6}
\]

so a trace-zero off-diagonal matrix unit is transported to a trace-one diagonal projection. Thus the scalar invariant that survived the diagonal quotient cannot extend to a bounded transport-invariant functional on the full operator space.

This observation also shows why the non-diagonal enlargement is not a harmless addition of extra coordinates. The cover compression identifies different residue classes before the output matrix is read; off-diagonal block coherence can feed directly into diagonal mass.

## 2. The full trace-class quotient is zero by duality

The dual of the trace class is `B(H)` under

\[
\langle A,X\rangle=\operatorname{Tr}(AX),
\qquad
A\in B(H),\ X\in\mathcal S_1(H).
\]

For `A in B(H)` and `X in S_1(H)`, cyclicity of the trace gives

\[
\begin{aligned}
\langle A,\rho_n(X)\rangle
&=\operatorname{Tr}\!\left(A\,nW_n^*XW_n\right)\\
&=\operatorname{Tr}\!\left(nW_nAW_n^*X\right).
\end{aligned}
\]

Hence the Banach adjoint of `rho_n` is

\[
\boxed{
\rho_n^*(A)=nW_nAW_n^*.
}
\tag{7}
\]

Now suppose a bounded functional annihilates `ran(I-rho_n)`. Its representing operator `A` then satisfies

\[
(I-\rho_n^*)A=0,
\qquad\text{i.e.}\qquad
A=nW_nAW_n^*.
\tag{8}
\]

Because `W_n` is an isometry,

\[
\boxed{
\|W_nAW_n^*\|=\|A\|.
}
\tag{9}
\]

The upper bound is immediate from `||W_n||=1`; the reverse bound follows by compressing back:

\[
W_n^*(W_nAW_n^*)W_n=A.
\]

Taking norms in (8) therefore gives

\[
\|A\|=n\|A\|.
\]

For `n>1`, this forces

\[
\boxed{A=0.}
\tag{10}
\]

Thus

\[
\ker(I-\rho_n^*)=\{0\}.
\tag{11}
\]

The standard Banach-space annihilator identity

\[
\overline{\operatorname{ran}T}
=(\ker T^*)_\perp
\tag{12}
\]

now yields (2) with `T=I-rho_n`:

\[
\overline{\operatorname{ran}(I-\rho_n)}
=\mathcal S_1(H).
\]

No use of primality, zeta, zero data, a functional equation, or analytic continuation enters this argument. Degree `2` alone already makes the full trace-class Hausdorff quotient vanish.

## 3. Every bounded invariant readout vanishes

Let `Y` be any Banach space and let

\[
\Phi:\mathcal S_1(H)\to Y
\]

be bounded linear with

\[
\Phi\rho_n=\Phi
\tag{13}
\]

for one fixed `n>1`. Then `Phi` annihilates `ran(I-rho_n)`. By (2) that range is dense, so continuity gives

\[
\boxed{\Phi=0.}
\tag{14}
\]

Therefore there is no nonzero bounded positive functional, bounded vector-valued invariant, or bounded quotient readout on the full trace class that identifies canonical cover transports.

This is strictly stronger than the diagonal result `WP-079`. There the restricted dual is `ell^infinity`, and the constant sequence gives the surviving trace functional. In the full dual `B(H)`, the analogous operator is the identity, but

\[
\rho_n^*(I)=nW_nW_n^*\ne I.
\tag{15}
\]

So there is no contradiction between

\[
\text{diagonal coinvariants}\cong\mathbb R\operatorname{Tr}
\]

and

\[
\text{full trace-class coinvariants}=0.
\]

The diagonal restriction removed exactly the off-diagonal directions that can be compressed into diagonal mass.

## 4. The collapse persists across standard Schatten and compact ideals

The proof is not peculiar to the trace norm. For `1<p<infinity`, the dual of `S_p(H)` is `S_q(H)` with `1/p+1/q=1`; for `p=1` it is `B(H)`; and the dual of `K(H)` is `S_1(H)`. In every case the adjoint transfer under the trace pairing is still

\[
A\longmapsto nW_nAW_n^*.
\tag{16}
\]

For every Schatten norm, as well as the operator norm,

\[
\boxed{
\|W_nAW_n^*\|_q=\|A\|_q,
}
\tag{17}
\]

because `W_nAW_n^*` has the same nonzero singular values as `A`. Thus the fixed-point equation

\[
A=nW_nAW_n^*
\]

again implies

\[
\|A\|_q=n\|A\|_q,
\]

hence `A=0`. The annihilator argument gives

\[
\boxed{
\overline{\operatorname{ran}(I-\rho_n)}^{\|\cdot\|_p}
=\mathcal S_p(H),
\qquad 1\le p<\infty,
}
\tag{18}
\]

and

\[
\boxed{
\overline{\operatorname{ran}(I-\rho_n)}^{\|\cdot\|}
=\mathcal K(H).
}
\tag{19}
\]

Since `rho_n` commutes with adjoint, the same zero-coinvariant conclusion holds on the real self-adjoint parts: if a self-adjoint element is approximated by `(I-rho_n)X_j`, taking self-adjoint parts of the approximants preserves convergence and the range relation.

Thus changing from trace-class to Hilbert--Schmidt, another Schatten ideal, or compact operators does not provide the missing internal quotient geometry. The obstruction is the norm-expanding factor `n` in the **dual** transfer, which is forced by the same normalization that makes the pointed-cover cocycle exact.

## 5. Consequence for the positive cover cocycle and Mangoldt primitive

`WP-074` gives positive trace-class defects

\[
Q_m\succeq0,
\qquad
\operatorname{Tr}Q_m=\log m,
\]

while `WP-078` defines the Möbius primitives

\[
M_m=\sum_{d\mid m}\mu(d)Q_{m/d},
\qquad
\operatorname{Tr}M_m=\Lambda(m).
\]

On the diagonal coinvariant quotient of `WP-079`, these become

\[
[Q_m]=(\log m)[E_0],
\qquad
[M_m]=\Lambda(m)[E_0].
\]

On the full trace-class quotient, by contrast,

\[
\boxed{
[Q_m]=[M_m]=0
\qquad\text{for every }m.
}
\tag{20}
\]

So the proposed non-diagonal escape does not merely fail to add a cross-prime coupling. It also erases the exact positive finite information already extracted by the pointed geometry.

One could instead renormalize the transfer to `W_n^*XW_n`, removing the factor `n`, but that is a different action. It no longer matches the canonical cocycle law

\[
Q_{mn}=\rho_n(Q_m)+Q_n
\]

whose Möbius primitive was being quotiented in `WP-078`--`WP-079`. Such a change is therefore outside the present no-go and would need its own independent geometric justification and an exact finite-weight audit.

## 6. Matched controls and the archimedean boundary

Everything above depends only on the normalized degree-`n` block-replication isometry and the transfer normalization in (1). The same vanishing occurs for any matched cyclic-cover system carrying the same pointed Hardy representation. It does not distinguish rational primes from arbitrary cover degrees and therefore cannot itself encode the global arithmetic completion.

The conclusion sharpens the route boundary after `WP-079`:

```text
diagonal trace-class H_0 coinvariants
    -> one scalar survives: ordinary trace
    -> Mangoldt support survives only as the scalar identity Lambda=mu*log

full standard operator-ideal H_0 coinvariants
    -> no bounded scalar or operator class survives at all
    -> even the positive prime-power defect classes vanish
```

Hence the missing global Weil mechanism cannot be obtained merely by retaining ordinary off-diagonal matrix coefficients and then taking the same universal cover-coinvariant quotient.

This does **not** say that cohomology is impossible. It says the opposite more precisely: if the pointed-cover system has a viable cohomological route, it cannot be just degree-zero Hausdorff coinvariants of a standard operator ideal. A survivor must use genuinely higher/derived structure, a nontrivial coefficient system, a selective geometric nullspace, or a finite--archimedean interaction formed before the quotient. Those are exactly the kinds of enrichments that the endomotive/cyclic-homology prior art already warns are necessary before a multiplicative semigroup can behave like a Frobenius/Lefschetz geometry.

## 7. Prior-art and novelty audit

The functional analysis used in (7)--(19) is standard: trace/Schatten duality, preservation of singular values under isometric corner embedding `A -> WAW^*`, and the Hahn--Banach identity relating dense range to fixed vectors of the Banach adjoint. No theorem-level novelty is claimed for those facts.

A directed literature search around Schatten-class coinvariants, trace-class transfer/compression maps, isometric corner embeddings, and dense range of `I-T` found the expected general operator-ideal and Banach-space machinery but no reason to treat (2), (18), or (19) as new abstract functional analysis. The durable Mathia content is the specialization to the exact transfer normalization forced by `WP-076`--`WP-078`, and the resulting closure of the explicit non-diagonal quotient escape left open by `WP-079`.

The broader prior-art boundary remains the Bost--Connes/endomotive material already retained in `SOURCES.md`: meaningful arithmetic cohomology in that setting is substantially richer than zeroth coinvariants of a flat semigroup action. The present calculation reinforces that boundary rather than competing with it.

## 8. Exact falsification surface

This finding can be falsified by any of the following:

1. failure of the matrix-unit formula (4) for the normalized cover operators used in `WP-074`--`WP-079`;
2. failure of the adjoint identity `rho_n^*(A)=nW_nAW_n^*` under trace duality;
3. a nonzero bounded operator `A` solving `A=nW_nAW_n^*` for some `n>1`;
4. failure of the annihilator identity (12) in the stated Banach setting;
5. a nonzero bounded linear functional on `S_1(H)` invariant under one `rho_n`, `n>1`;
6. a nonzero class in the Hausdorff full trace-class coinvariant quotient;
7. a standard Schatten/compact ideal for which the same transfer has a nonzero Hausdorff coinvariant under the stated norm topology.

Items 2--7 are ruled out by the norm argument above once the cover isometry and normalization (1) are fixed.

The scope boundary is essential. This finding does **not** rule out:

- non-Hausdorff or deliberately discontinuous algebraic coinvariants;
- unbounded invariant functionals with a separately justified domain;
- a normalized or twisted action different from (1);
- higher semigroup homology/cohomology or derived coinvariants;
- coefficient modules carrying genuinely new internal/arithmetic data;
- a selective quotient whose kernel is forced by independent geometry rather than universal transport identification;
- nonlinear determinant/rank/volume constructions such as `WP-030`;
- a nonseparable finite--archimedean block constructed before positivity and before quotienting.

Any such route must still pass the line mandate: it must retain the exact finite `Lambda(p^k)/sqrt(p^k)` structure, generate the archimedean and polar terms intrinsically, and obtain the final sign from geometry rather than from RH, zero data, or a fitted positivity functional.

## Research consequence

`WP-079` left open the possibility that its trace-only diagonal quotient was an artifact of throwing away off-diagonal operator data. `WP-080` rules out that interpretation for the canonical cover transfer on all standard Schatten/compact ideals:

\[
\boxed{
\text{diagonal coinvariants}=\mathbb R\operatorname{Tr},
\qquad
\text{full standard operator-ideal coinvariants}=0.
}
\]

Thus ordinary non-diagonal coherence is not the missing global degree of freedom. The next viable quotient/cohomological route must change category in a substantive way — higher/derived structure, nontrivial coefficients, or a genuinely nonseparable finite--archimedean geometry — before the sign theorem is read out.
