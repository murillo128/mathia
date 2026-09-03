# WP-134 — Repeated-prime full-chord coarse compression is exactly stationary

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + PRIME-CIRCLE + MATCHED-CONTROL + COMPUTATION-CHECKED + PRIOR-ART-CLASSICALIZATION` for the canonical fiber-constant repeated-prime compression of the normalized full primitive-shell inverse-square chord operator.

`PC-155` classifies the corresponding **new-prime** refinement `N -> Nq`, `q \nmid N`, but explicitly leaves repeated-prime refinement open. In the repeated-prime case the answer is much more rigid.

Let

\[
U(N):=(\mathbb Z/N\mathbb Z)^\times
\]

and use exactly the full inverse-square primitive-shell Laplacian and normalization of `PC-155`,

\[
(L_N^{\rm int}f)(a)
=\sum_{\substack{b\in U(N)\\b\ne a}}
\frac{f(a)-f(b)}{4\sin^2(\pi(a-b)/N)},
\qquad
A_N:=N^{-2}L_N^{\rm int}.
\tag{1}
\]

If `p` is prime and `p | N`, reduction

\[
U(Np)\longrightarrow U(N)
\]

has exactly `p` points in every fiber. Let `J_{N,p}` be the normalized pullback of a coarse function to the fiber-constant fine subspace. Then

\[
\boxed{
J_{N,p}^*A_{Np}J_{N,p}=A_N.
}
\tag{2}
\]

Thus once a prime is already present, increasing its exponent produces **no normalized coarse compression defect at all**. Iterating,

\[
J_{N,p^r}^*A_{Np^r}J_{N,p^r}=A_N
\qquad(r\ge1).
\tag{3}
\]

This gives a precise no-go for one natural Weil route. The finite explicit formula requires a nonzero contribution at every repeated prime power, with

\[
\Lambda(p^k)=\log p
\qquad(k\ge1).
\tag{4}
\]

But the canonical level-to-level coarse defect after the first occurrence of `p`,

\[
\Delta_{p,k}
:=J^*A_{p^{k+1}M}J-A_{p^kM},
\qquad p\nmid M,
\tag{5}
\]

is identically zero for every `k>=1`. Therefore the normalized full-chord **coarse-compression increment itself cannot be the intrinsic source of the repeated prime-power Mangoldt tower**. Any successful Prime-Circle mechanism must read additional fine-fiber information, use a nonlinear/absolute-level observable, or couple levels before the coarse positive form is taken.

This is not a global Weil-positivity theorem and it does not say that the finer full-chord operator forgets prime-power depth. The theorem concerns one exact and canonical sector: normalized fiber-constant compression and its level-to-level defect.

## 1. Repeated-prime fibers have constant multiplicity `p`

Write

\[
N=p^aM,
\qquad a\ge1,
\qquad (p,M)=1.
\]

Every unit modulo `N` has exactly `p` lifts modulo `Np`, and all of them remain units. If `a in U(N)`, its fiber is

\[
\{a+kN:0\le k<p\}\pmod{Np}.
\tag{6}
\]

Let `R_{N,p}` be the unnormalized fiber-incidence matrix,

\[
R_{N,p}(a,x)=1_{x\equiv a\pmod N},
\qquad
a\in U(N),\ x\in U(Np).
\tag{7}
\]

Then

\[
R_{N,p}R_{N,p}^*=pI,
\qquad
J_{N,p}:=p^{-1/2}R_{N,p}^*.
\tag{8}
\]

The image of `J_{N,p}` is exactly the fiber-constant subspace of `ell^2(U(Np))`.

## 2. The cosecant multiplication law gives an exact `p^3` raw compression

Fix distinct coarse units `a,b in U(N)` and choose an integer representative

\[
h=a-b.
\]

A pair of lifts has difference

\[
h+(k-\ell)N,
\qquad 0\le k,\ell<p.
\tag{9}
\]

For every residue `t mod p`, exactly `p` ordered pairs `(k,ell)` satisfy `k-ell=t mod p`. Therefore the total fine conductance between the two coarse fibers is

\[
p\sum_{t=0}^{p-1}
\frac1{4\sin^2\!\left(\pi(h+tN)/(Np)\right)}.
\tag{10}
\]

The differentiated cotangent multiplication formula gives the classical identity

\[
\sum_{t=0}^{p-1}
\csc^2\!\left(x+\frac{\pi t}{p}\right)
=p^2\csc^2(px).
\tag{11}
\]

Taking

\[
x=\frac{\pi h}{Np}
\]

in (11) turns (10) into

\[
\frac{p^3}{4\sin^2(\pi h/N)}.
\tag{12}
\]

Hence every off-diagonal coarse conductance is exactly `p^3` times the corresponding conductance at level `N`. Both sides are Laplacians and annihilate the constant vector, so the diagonal entries are then forced by zero row sum. Thus the raw operators satisfy

\[
\boxed{
R_{N,p}L_{Np}^{\rm int}R_{N,p}^*
=p^3L_N^{\rm int}.
}
\tag{13}
\]

Now combine (8), (13), and the normalization `A_N=N^{-2}L_N^{int}`:

\[
\begin{aligned}
J_{N,p}^*A_{Np}J_{N,p}
&=\frac1p\,R_{N,p}\frac{L_{Np}^{\rm int}}{N^2p^2}R_{N,p}^*\\
&=\frac1p\frac{p^3}{N^2p^2}L_N^{\rm int}\\
&=A_N.
\end{aligned}
\tag{14}
\]

This proves (2) exactly.

## 3. The entire repeated-prime coarse tower is stationary

Apply (2) successively along

\[
N\leftarrow Np\leftarrow Np^2\leftarrow\cdots.
\]

The normalized pullbacks compose to the normalized pullback from `U(N)` to `U(Np^r)`, because each stage has the same fiber multiplicity `p`. Therefore

\[
\boxed{
J_{N,p^r}^*A_{Np^r}J_{N,p^r}=A_N
\qquad(r\ge1).
}
\tag{15}
\]

Equivalently, if `N=p^kM` with `k>=1` and `p \nmid M`, then the canonical coarse increment is

\[
\boxed{
\Delta_{p,k}
:=J_{p^kM,p}^*A_{p^{k+1}M}J_{p^kM,p}-A_{p^kM}
=0.
}
\tag{16}
\]

No limiting argument, asymptotic estimate, zeta identity, zero data, regularization, or RH assumption enters this statement. It is a finite exact identity on every repeated-prime refinement step.

## 4. Weil consequence: the coarse defect cannot supply repeated prime powers

The finite-prime side of a Weil explicit formula contains every prime power. In the standard von-Mangoldt packaging the coefficient is

\[
\Lambda(p^k)=\log p,
\qquad k\ge1,
\tag{17}
\]

with whatever test-function/critical normalization is appropriate to the chosen explicit-formula convention. The important structural fact here is not the external test weight but the persistence of a nonzero arithmetic event at **every** depth `k`.

Equation (16) shows that the natural normalized full-chord fiber-constant defect has the opposite behavior: after `p` first appears it is exactly stationary. Thus a construction of the form

\[
\text{prime-power arithmetic event}
\quad\leftrightarrow\quad
\text{new normalized coarse-compression defect}
\]

cannot reproduce the Mangoldt prime-power tower.

This no-go is deliberately narrower than saying that the absolute operator `A_{p^kM}` has no `k`-dependence. It may have substantial depth information outside the coarse sector. Nor does (16) prevent a researcher from externally indexing the same stationary coarse object once at each depth. What fails is the stronger and branch-relevant claim that **repeated prime powers are generated intrinsically as new events by this canonical positive coarse compression**. Repeating an unchanged object because the external arithmetic index says to repeat it would insert, rather than derive, the prime-power multiplicity.

## 5. Matched control: new-prime refinement is not stationary

The identity is not a tautology of fiber compression. `PC-155` treats the matched refinement `N -> Nq` with `q \nmid N`, where each coarse unit has `q-1` unit lifts. For the same normalized full primitive-shell operator it proves

\[
J_{N,q}^*A_{Nq}J_{N,q}
=
\frac{q-2}{q-1}A_N
+
\frac{1}{q^2(q-1)}V_qA_NV_q^{-1},
\tag{18}
\]

where `V_q` is the multiplicative permutation `f(a) -> f(q^{-1}a)` on `U(N)`.

That compression is a nontrivial commuting invertible conjugacy-polynomial superoperator. The repeated-prime case (2) is qualitatively different: all `p` lifts remain units, the omitted-residue correction responsible for the second term of (18) disappears, and the full cosecant multiplication sum survives. Exact stationarity is therefore a **repeated-prime phenomenon**, not a generic feature of the full-chord observable.

This matched control also explains the arithmetic tension. Fresh-prime birth remains visible in the canonical coarse operator, while multiplicity of an already-present prime becomes invisible to its normalized coarse defect. The Weil finite term needs both.

## 6. What survives outside the fiber-constant sector

Equation (2) classifies a compression, not the complete fine operator. Decompose

\[
\ell^2(U(Np))
=
\operatorname{im}J_{N,p}
\oplus
(\operatorname{im}J_{N,p})^\perp.
\tag{19}
\]

The theorem fixes the upper-left fiber-constant block of `A_{Np}` after compression. It does **not** classify the zero-mean fiber-fluctuation block or the couplings between that block and the coarse subspace. Those sectors are the natural place where genuine repeated-prime depth could still live.

Accordingly, the result does not rule out:

- a positive construction that uses the fine fiber-fluctuation sector before compression;
- a Schur complement or boundary response in which coarse and fluctuation sectors are coupled;
- nonlinear spectral functions, determinants, or log-determinants of the absolute fine operator;
- an absolute-level readout that depends on `k` even though the normalized coarse defect is zero;
- a cross-level construction whose sign theorem acts before the fiber-constant quotient;
- a later finite--archimedean coupling with an independently proved positive form.

Those are different mechanisms and require separate falsification. In particular, this finding does not claim a complete repeated-prime classification of the full-chord operator.

## 7. Computational validation

The exact matrix identity (2) was checked independently on finite primitive-unit shells for

\[
(N,p)=(3,3),(6,3),(9,3),(10,5),(12,2),(15,3),(18,3),(25,5).
\tag{20}
\]

For each pair, the normalized fiber pullback was built explicitly and the residual

\[
\left\|J_{N,p}^*A_{Np}J_{N,p}-A_N\right\|
\]

was at machine precision (`~10^{-16}` or smaller), while `J_{N,p}^*J_{N,p}=I`. These checks are not evidence in place of the proof; they are a matched implementation check on the multiplicity and normalization factors in (13)--(14), including composite `N`, higher existing `p`-adic depth, and `p=2`.

## 8. Prior-art and novelty audit

No theorem-level historical novelty is claimed for the ambient mechanisms. The cosecant-square multiplication formula (11) is classical, obtained by differentiating the cotangent multiplication formula. Likewise, compression to fiber-constant subspaces is standard quotient/equitable-partition linear algebra for weighted graph Laplacians.

A bounded search across cosecant multiplication identities, graph-cover/equitable-partition Laplacian quotients, reduced-residue/primitive-residue trigonometric matrices, and explicit-formula prime-power weights located these standard ingredients but not the specific identity (2) for the Mathia full primitive-unit inverse-square chord operator, nor the defect-level obstruction (16) to producing the repeated Mangoldt tower. That absence is not evidence of historical novelty; the durable contribution is the exact Mathia-specific specialization and its consequence for this research branch.

The nearest internal results are informative but distinct. `PC-050` and `PC-051` show radical invariance and affine repeated-prime fiber-copy behavior for the cotangent observable. `PC-067` studies compatible inverse-square chord energy and its scale behavior. `PC-078` and `PC-085` classify repeated-prime Hardy/tensor inflation in another operator family. Most directly, `PC-155` solves the **new-prime** full-chord primitive-shell compression and explicitly leaves repeated-prime refinement unclassified. Equation (2) fills exactly that remaining local case for the canonical coarse sector.

On the Weil side, earlier findings already warn that squarefree birth alone cannot provide the complete prime-power explicit-formula measure and that positive spectral packaging is not automatically the required Weil pairing. The present result adds a sharper operator statement: passing from fresh-prime birth to repeated-prime refinement inside this particular normalized full-chord coarse geometry does not cure that deficit; the incremental signal collapses to zero.

## 9. Falsification boundary

The theorem would fail if any of the following exact claims failed under the `PC-155` operator convention:

1. a unit modulo `N` had other than exactly `p` unit lifts modulo `Np` when `p | N`;
2. the ordered-pair multiplicity in (10) were not exactly `p` for every difference class modulo `p`;
3. the classical cosecant-square distribution law did not yield the `p^2` factor in (11);
4. the raw compressed Laplacian failed the `p^3` identity (13), including its diagonal entries;
5. the normalization and isometric fiber factor failed to cancel exactly in (14); or
6. an existing canonical Mathia finding already proved the same full-chord repeated-prime primitive-shell compression theorem.

The finite calculations in (20) directly challenge items 1--5 on representative cases; the exact derivation proves them generally; and the internal novelty audit found related but different repeated-prime theorems, with `PC-155` itself identifying this full-chord case as open.

The **Weil no-go** is falsified by a construction that genuinely obtains the repeated prime-power coefficient from information outside the defect (16). Such a construction would not falsify (2); it would show that the wrong readout was being tested. The present claim should therefore be used only to eliminate the canonical normalized coarse-increment route, not to discard Prime Circle as a whole.

## 10. Consequence for the Weil-positivity search

The full-chord operator now has a clean cross-level dichotomy. Adjoining a new prime yields the nontrivial but commuting/invertible coarse transformation of `PC-155`; increasing the exponent of an existing prime yields the exact stationary compression (2). Neither behavior by itself supplies the local-to-global mechanism required by the branch mandate.

For repeated prime powers in particular, the next serious candidates must use structure discarded by the fiber-constant expectation: **fiber fluctuations, coarse--fine coupling, a nonlinear absolute-level invariant, or a joint finite--archimedean operation applied before positivity/quotienting**. Any proposal that reads `Lambda(p^k)` directly from the normalized repeated-prime coarse defect can now be rejected without further numerical experimentation.

No zeta zero set, RH-equivalent positivity functional, hand-picked kernel, or arbitrary regularization is used here. The result is a finite exact obstruction that materially narrows one Prime-Circle-native route to the finite part of a global Weil-positive geometry.

## Cross-references

- `research/prime_circle/findings/PC-050-cotangent-refinement-averaging-is-radical-invariant.md`
- `research/prime_circle/findings/PC-051-repeated-prime-cotangent-fiber-details-are-affine-base-copies.md`
- `research/prime_circle/findings/PC-067-compatible-inverse-square-chord-energy-resolves-order-but-not-rh-scale.md`
- `research/prime_circle/findings/PC-078-repeated-prime-hardy-refinement-is-signed-radical-tensor-inflation.md`
- `research/prime_circle/findings/PC-085-common-repeated-prime-depth-is-universal-mixed-hardy-tensor-inflation.md`
- `research/prime_circle/findings/PC-155-full-chord-primitive-refinement-compression-is-a-commuting-invertible-conjugacy-polynomial.md`
