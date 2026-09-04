# WP-148 — Canonical resultant graph Laplacian has infinite critical degree and trivial natural ℓ² domain

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + PRIME-CIRCLE + CYCLOTOMIC-RESULTANT + GRAPH-DIRICHLET + CANONICAL-DIAGONAL-COMPLETION + INDEPENDENT-FINITE-POSITIVITY + INFINITE-CRITICAL-DEGREE + TRIVIAL-L2-DOMAIN + MATCHED-FINITE-PRIME-CONTROL + PRIOR-ART-CLASSICALIZATION`

## Claim

The zero-order Prime-Circle resultant kernel left open by `WP-145`--`WP-147` has a canonical positive diagonal completion on every finite shell set: take the weighted graph Laplacian whose off-diagonal entries are the negatives of the normalized cyclotomic-resultant weights. This completion is not hand-picked at finite level. Once the off-diagonal resultant interaction and conservation of constants are required, the diagonal is uniquely forced, and positivity follows from the ordinary Dirichlet-energy identity.

However, this natural escape does **not** globalize on the shell-uniform Hilbert space relevant to the normalized resultant kernel. At the critical half-density, every fixed shell has infinite weighted degree because adjoining a fresh prime produces the exact edge weight

\[
J_{m,mp}=\frac{\log p}{\sqrt{p-1}}.
\]

More strongly, the resulting formal global Dirichlet energy has **trivial finite-energy domain inside natural `ℓ²`**: every nonzero `ℓ²` vector has infinite energy. Thus the canonical conservative diagonal completion of the actual resultant kernel cannot define a densely defined positive quadratic form on the natural shell-uniform Hilbert space.

This is a narrower and stronger obstruction than the generic infinite-diagonal requirement of `WP-096`. It closes the most canonical diagonal/Markov completion explicitly left outside `WP-146` and `WP-147`, while leaving genuinely different noncompact energy spaces, source-forced changes of measure, mixed-prime completions, and nonseparable finite--archimedean constructions open.

## 1. The finite conservative completion is canonical and positive

Write the normalized zero-order shell coupling as

\[
J_{m,n}
:=
\frac{\log|\operatorname{Res}(\Phi_m,\Phi_n)|}
{\sqrt{\varphi(m)\varphi(n)}}
\qquad(m\ne n).
\tag{1}
\]

By the cyclotomic resultant theorem used in `WP-145`, `J_{m,n}\ge0`, with nonzero support exactly when one shell index differs from the other by a prime power. Let `F` be any finite set of shell indices and put

\[
D_F(m,m):=\sum_{\substack{n\in F\\n\ne m}}J_{m,n},
\qquad
L_F:=D_F-J_F,
\tag{2}
\]

where `J_F` has zero diagonal. Then for every `f\in\mathbb C^F`,

\[
\boxed{
\langle f,L_Ff\rangle
=
\frac12\sum_{m,n\in F}J_{m,n}|f_m-f_n|^2
\ge0.
}
\tag{3}
\]

Hence `L_F\succeq0` for an entirely independent geometric reason: it is the weighted graph Dirichlet form of the resultant graph. Constants lie in its kernel.

This diagonal is also forced by the natural conservation law. If a Hermitian matrix `A_F` is required to retain exactly the off-diagonal interaction

\[
(A_F)_{m,n}=-J_{m,n}
\qquad(m\ne n)
\tag{4}
\]

and to annihilate constants,

\[
A_F\mathbf 1=0,
\tag{5}
\]

then necessarily

\[
(A_F)_{m,m}=\sum_{n\ne m}J_{m,n}=D_F(m,m).
\tag{6}
\]

So within the conservative Markov/Dirichlet category there is no diagonal tuning parameter: `A_F=L_F` uniquely.

This is exactly the attractive escape from `WP-146`: the off-diagonal sign becomes `-J_{m,n}`, while positivity is supplied by a canonical diagonal self-energy rather than by changing the sparse resultant selector itself.

## 2. Fresh-prime edges force infinite critical degree

Fix a shell `m\ge1`. For every prime `p\nmid m`, the ratio from `m` to `mp` is a fresh prime step. Apostol's cyclotomic-resultant formula gives

\[
\log|\operatorname{Res}(\Phi_m,\Phi_{mp})|
=
\varphi(m)\log p,
\tag{7}
\]

while

\[
\varphi(mp)=\varphi(m)(p-1).
\tag{8}
\]

(The case `m=1` follows directly from `\Phi_p(1)=p`.) Therefore the normalized edge weight is

\[
\boxed{
J_{m,mp}
=
\frac{\log p}{\sqrt{p-1}}.
}
\tag{9}
\]

Only finitely many primes divide `m`, so the formal global weighted degree at `m` obeys

\[
d(m)
:=
\sum_{n\ne m}J_{m,n}
\ge
\sum_{p\nmid m}\frac{\log p}{\sqrt{p-1}}.
\tag{10}
\]

For all sufficiently large primes,

\[
\frac{\log p}{\sqrt{p-1}}\ge\frac1p,
\tag{11}
\]

and Euler's classical divergence of `\sum_p1/p` gives

\[
\boxed{d(m)=\infty\quad\text{for every shell }m.}
\tag{12}
\]

Thus the diagonal dictated by finite-cutoff conservation diverges at **every** vertex as the prime alphabet is opened. This is not the single scalar counterterm of `WP-096`; it is the exact vertex degree of the actual normalized resultant graph.

## 3. The natural global `ℓ²` finite-energy domain collapses to `{0}`

The normalized uniform shell vectors used in `WP-145` make the natural ambient coefficient space the counting-space Hilbert space

\[
\mathcal H_{\rm sh}=\ell^2(\{m\ge1\}).
\tag{13}
\]

The monotone finite-cutoff limit suggested by (3) is the extended nonnegative energy

\[
\mathcal E(f)
:=
\frac12\sum_{m\ne n}J_{m,n}|f_m-f_n|^2
\in[0,\infty].
\tag{14}
\]

Take any nonzero `f\in\mathcal H_{\rm sh}` and choose `m` with `f_m\ne0`. As `p` ranges through distinct primes not dividing `m`, the indices `mp` escape to infinity. Since every `ℓ²` sequence vanishes along every escaping sequence of distinct coordinates,

\[
f_{mp}\longrightarrow0.
\tag{15}
\]

Hence for all sufficiently large such primes,

\[
|f_m-f_{mp}|\ge\frac{|f_m|}{2}.
\tag{16}
\]

Keeping only the fresh-prime edges adjacent to `m` in (14) yields

\[
\mathcal E(f)
\ge
\frac{|f_m|^2}{4}
\sum_{\substack{p\nmid m\\p\ge p_0}}
\frac{\log p}{\sqrt{p-1}}
=
\infty.
\tag{17}
\]

Therefore

\[
\boxed{
\operatorname{Dom}(\mathcal E)\cap\mathcal H_{\rm sh}
=
\{0\}.
}
\tag{18}
\]

In particular, the canonical positive cutoff forms do not converge to a densely defined quadratic form on the natural `ℓ²` shell space; even every nonzero finitely supported vector has infinite limiting energy. This is stronger than merely saying that the formal diagonal entries diverge.

The constant null mode of every finite `L_F` does not contradict (18): a nonzero constant sequence is not in counting-space `ℓ²`. A quotient-by-constants or an extended noncompact energy space would therefore be a genuinely different Hilbert/topological construction, not the natural inductive limit of these forms inside `\mathcal H_{\rm sh}`.

## 4. Matched controls isolate the obstruction to infinitely many new-prime directions

The failure is not caused by weighted graph Laplacians themselves.

First, every finite shell set `F` gives the exact PSD identity (3). Second, on a single prime-power ray, `WP-145` gives

\[
J_{p^a,p^{a+k}}=\frac{\log p}{p^{k/2}},
\tag{19}
\]

whose outward tail is summable. More generally, restrict the shell indices to the multiplicative monoid generated by a finite prime alphabet `P`. For a fixed vertex `m` and a fixed `p\in P`, the prime-power neighbors have a geometric tail. If `p\nmid m`,

\[
J_{m,mp^a}
=
\frac{\log p}
{p^{(a-1)/2}\sqrt{p-1}},
\qquad a\ge1,
\tag{20}
\]

while if `p\mid m`,

\[
J_{m,mp^a}
=
\frac{\log p}{p^{a/2}}.
\tag{21}
\]

There are only finitely many prime directions, so the weighted degree is finite and every finitely supported vector has finite graph energy.

Thus the critical collapse in (18) is specifically an **infinite-prime-alphabet effect**: each newly available prime direction contributes the nonsummable first-step weight (9). This matched control is important because a merely local or one-prime realization would incorrectly suggest that the canonical Dirichlet completion globalizes harmlessly.

## 5. Relation to the existing no-go chain

This result does not replace `WP-096`. That finding classifies exact cover-covariant positive Gram completions abstractly and shows that sparse Weil support requires divergent scalar diagonal mass unless mixed-prime coefficients are added. Here the input is much narrower: the **actual zero-order cyclotomic-resultant kernel** of `WP-145`--`WP-147`, and the diagonal is fixed by the standard conservative graph law rather than optimized over positive completions.

The gain is correspondingly sharper. `WP-146` and `WP-147` left arbitrary diagonal/full-rank repairs outside their inertia obstructions. Equations (2)--(6) identify the most canonical such repair and prove finite positivity; equations (9)--(18) then show that its natural global realization fails more severely than finite inertia does. The positive operator cannot even be obtained as a densely defined `ℓ²` Dirichlet form without changing topology, measure, or the interaction itself.

`WP-097`-type mixed-prime positive completions remain logically distinct. They alter the off-diagonal kernel rather than merely supplying the conservative diagonal demanded by `J`. Likewise, `WP-147` already shows that a fixed finite-dimensional archimedean Schur complement cannot repair the extensive inertia of the uncompleted kernel; `WP-148` says that the canonical full diagonal completion does repair every finite cutoff but becomes singular at the infinite-prime limit.

## 6. Consequence for Weil positivity

The candidate has two desirable ingredients at finite level:

1. the off-diagonal arithmetic selector is still the exact prime-power resultant kernel, with the sign `-J` supplied by a positive Dirichlet form;
2. nonnegativity follows independently from geometry, not from RH, a zero list, or an inserted Weil-positive functional.

But the global arithmetic requirement activates infinitely many fresh-prime directions, and precisely there the canonical positive form loses its natural Hilbert-space domain. A subtraction of the divergent diagonal would not automatically inherit (3): it would be a renormalized form requiring a new, independently justified positivity theorem and a source-forced finite--archimedean matching. Merely declaring a counterterm would be exactly the arbitrary-regularization escape excluded by the research mandate.

Therefore the conservative graph-Laplacian route does **not** provide the requested global Weil positivity. A surviving route must change something structurally before the infinite-prime limit: for example derive a non-counting vertex measure/topology from Mathia, add source-forced mixed-prime couplings, use a genuinely noncompact quotient/energy space with an independent theorem, or introduce an infinite-dimensional/nonseparable finite--archimedean mechanism. None of those possibilities is established here.

## 7. Prior-art audit and novelty boundary

The arithmetic input is classical. T. M. Apostol, *Resultants of cyclotomic polynomials*, Proc. Amer. Math. Soc. **24** (1970), 457--462, gives the prime-power support and resultant values used above. Weighted graph Laplacians, identities of the form (3), and infinite-graph Dirichlet forms are also standard; representative modern references include M. Keller and D. Lenz, *Unbounded Laplacians on Graphs: Basic Spectral Properties and the Heat Equation*, Math. Model. Nat. Phenom. **5** (2010), 198--224, and S. Haeseler, M. Keller, D. Lenz, R. Wojciechowski, *Laplacians on infinite graphs: Dirichlet and Neumann boundary conditions*, J. Spectr. Theory **2** (2012), 397--432 / arXiv:1103.3695.

A bounded search for combinations of cyclotomic resultants, graph Laplacians, and Dirichlet forms did not surface a source identifying this exact normalized cyclotomic-resultant graph and the domain collapse (18). No generic novelty is claimed for graph-Laplacian positivity, infinite weighted degree, or Dirichlet-form theory. The Mathia-specific contribution is the exact specialization:

\[
\text{normalized cyclotomic resultant selector}
\;\longrightarrow\;
\text{unique conservative positive completion}
\;\longrightarrow\;
\frac{\log p}{\sqrt{p-1}}\text{ fresh-prime degree}
\;\longrightarrow\;
\operatorname{Dom}_{\ell^2}\mathcal E=\{0\}.
\tag{22}
\]

This also differs from classical Weil/explicit-formula positivity, Hilbert--Pólya, Connes/trace, Frobenius/cohomology, and intersection-form routes: no zero data or RH-equivalent functional is used to prove the finite sign. The obstruction occurs earlier, when the Mathia-native arithmetic selector is assembled into its canonical conservative positive geometry.

## 8. Falsification surface

`WP-148` would be invalidated or materially weakened by any of the following:

- an error in the normalized fresh-prime weight (9);
- a source-forced natural shell measure for which the same resultant interaction has a nontrivial dense finite-energy domain and still matches the Weil normalization;
- a canonical renormalized limit of the finite `L_F` with an independent positivity theorem, not merely subtraction of divergent degrees;
- a Mathia-native mixed-prime or finite--archimedean coupling that changes the global form before the divergent new-prime degree is created while preserving the exact required arithmetic coefficients.

The first item is an exact arithmetic check; the latter three are genuine open escape routes rather than consequences of this finding.