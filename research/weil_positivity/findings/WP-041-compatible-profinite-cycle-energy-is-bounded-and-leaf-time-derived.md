# WP-041 — compatible profinite cycle energy is bounded and leaf-time derived

**Status:** `EXACT-DERIVED + CLASSICAL-CYCLE/ODOMETER-STRUCTURE + DECISIVE-NEGATIVE` for the most direct genuinely embedded transverse-energy escape left open by `WP-040`. The polygon edges in the Prime-Circle refinement tower do force a canonical positive nearest-neighbor form on the profinite anchor fiber once exact cover compatibility is required, but the compatible normalization is unique up to scale and yields only the bounded adding-one difference operator. In the adelic-solenoid model of `PC-064`, that adding-one fiber translation is exactly an integer leaf-time translation, so this candidate is not an independent finite-adic derivative. Its character energy is `4 sin^2(pi gamma)`, which is bounded and has arbitrarily soft high-conductor modes. Consequently neither its ordinary Sobolev powers nor finite-range polygon-edge variants can host the singular Weil/Haar tangent of `WP-037`. An unbounded conductor operator can evade this obstruction, but `PC-066` shows that choosing its conductor scale is additional spectral reweighting rather than a scale fixed by the abstract transverse symmetry; the local cycle-edge geometry does not supply that missing choice.

## 1. Exact object: the edge form forced by the compatible polygon tower

At level `n`, the regular root polygon carries the distinguished cyclic order

\[
K_n=\mathbb Z/n\mathbb Z,
\qquad
x\longleftrightarrow x+1.
\]

For `m|n`, the Prime-Circle covering map on roots is reduction

\[
\pi_{n,m}:K_n\to K_m,
\qquad
x\mapsto x\pmod m,
\]

and sends every oriented polygon edge `x -> x+1` to the corresponding edge modulo `m`. The orientation will not matter because the quadratic energy is symmetric.

Consider the most direct positive polygon-edge form

\[
\mathcal E_n^{(a)}(f)
=
 a_n\sum_{x\in K_n}|f(x+1)-f(x)|^2,
\qquad a_n>0.
\tag{1}
\]

If `f` is a function on `K_m`, its pullback to `K_n` repeats the same `m` edge differences exactly `n/m` times. Hence

\[
\sum_{x\in K_n}
|f(\pi_{n,m}(x+1))-f(\pi_{n,m}(x))|^2
=
\frac nm
\sum_{y\in K_m}|f(y+1)-f(y)|^2.
\tag{2}
\]

Exact refinement compatibility

\[
\mathcal E_n^{(a)}(f\circ\pi_{n,m})
=
\mathcal E_m^{(a)}(f)
\tag{3}
\]

therefore forces

\[
a_n\frac nm=a_m.
\tag{4}
\]

For arbitrary `m,n>=2`, apply (4) through `lcm(m,n)`. It follows that

\[
\boxed{n a_n=m a_m=c}
\tag{5}
\]

for one constant `c>0`. Thus, within the nearest-neighbor polygon-edge class (1), exact compatibility fixes the normalization uniquely up to an overall scalar:

\[
\boxed{a_n=\frac c n.}
\tag{6}
\]

The trivial one-point level imposes no extra condition because its edge energy vanishes identically.

Taking `c=1`, (1) is just normalized counting measure on each finite quotient. Since

\[
K=\widehat{\mathbb Z}=\varprojlim K_n
\]

with Haar probability measure `m_H`, the compatible forms descend on cylinder functions to

\[
\boxed{
\mathcal E_{\rm cyc}(f)
=
\int_K |f(x+1)-f(x)|^2\,dm_H(x).
}
\tag{7}
\]

This is a real Mathia-native positive form: it uses the actual cyclic polygon edge, the actual refinement maps, and no zeta data, zeros, kernel fitting, or regularization choice.

## 2. The limit operator is the bounded adding-one difference

Let

\[
(Uf)(x)=f(x+1)
\]

on `L^2(K,m_H)`. Haar invariance makes `U` unitary, and (7) is

\[
\mathcal E_{\rm cyc}(f)
=
\langle f,L_{\rm cyc}f\rangle,
\qquad
L_{\rm cyc}=(U-I)^*(U-I)
=2I-U-U^*.
\tag{8}
\]

Therefore

\[
\boxed{0\le L_{\rm cyc}\le4I.}
\tag{9}
\]

The form is closed on all of `L^2(K)` and its positivity is completely independent of RH. But it is a bounded jump/difference energy rather than an unbounded transverse derivative.

For a character `chi_gamma`, `gamma in Q/Z`,

\[
U\chi_\gamma
=e^{2\pi i\gamma}\chi_\gamma
\]

(up to the harmless inverse convention for the character pairing). Hence

\[
\boxed{
L_{\rm cyc}\chi_\gamma
=4\sin^2(\pi\gamma)\chi_\gamma.
}
\tag{10}
\]

This is exactly the ordinary cycle-graph Fourier symbol. In particular, for the primitive character of exact order `q` represented by `gamma=1/q`,

\[
\lambda_q
=4\sin^2\frac\pi q
\sim\frac{4\pi^2}{q^2}
\longrightarrow0.
\tag{11}
\]

So high arithmetic conductor is not expensive. It becomes arbitrarily cheap.

## 3. On the solenoid this is not an independent transverse derivative

`PC-064` gives the exact Prime-Circle completion

\[
\Sigma_{\mathbb Q}
\cong
(\mathbb R\times\widehat{\mathbb Z})/\mathbb Z_{\rm diag},
\tag{12}
\]

with the anchor fiber represented by `(0,a)`, `a in K`. The diagonal identification is

\[
(t,a)\sim(t+k,a+k),
\qquad k\in\mathbb Z.
\tag{13}
\]

Consequently the distinguished adding-one displacement on the fiber satisfies

\[
\boxed{[(0,1)]=[(-1,0)]\in\Sigma_{\mathbb Q}.}
\tag{14}
\]

Thus the odometer step `a -> a+1` is exactly the time-`-1` translation of the real leaf when viewed inside the full compatible solenoid. The corresponding positive form (7) is therefore a bounded finite-difference function of the already-present leaf flow.

This explains structurally why (10) sees only the phase of the rational leaf frequency modulo integers. The most obvious polygon-edge attempt to create a new transverse derivative collapses back to a discrete sampling of the archimedean leaf translation rather than producing independent finite-adic regularity.

## 4. It cannot regularize the Weil/Haar tangent from WP-037

`WP-037` derives the scaled first variation `eta` of the normalized radial law at profinite Haar. On nontrivial torsion characters its Fourier data are

\[
\widehat\eta(\chi_\gamma)
=-\Log(1-e^{2\pi i\gamma}),
\tag{15}
\]

with, in particular,

\[
\operatorname{Re}\widehat\eta(\chi_{1/q})
=
\log q-\log(2\pi)+o(1).
\tag{16}
\]

Because `L_cyc` is bounded, for every finite real `s` the inhomogeneous Sobolev norm generated by it,

\[
\|f\|_{s,\rm cyc}^2
=
\langle f,(1+L_{\rm cyc})^s f\rangle,
\tag{17}
\]

is equivalent to the ordinary `L^2(K)` norm:

\[
1\le1+\lambda(\gamma)\le5.
\tag{18}
\]

Thus no positive or negative finite Sobolev order built from `(1+L_cyc)` creates conductor growth. Since `eta` is not an `L^2` Haar density, it is not continuous in the dual of any of these spaces.

Even replacing the inhomogeneous scale by homogeneous powers or inverse powers does not solve the global conductor problem. Let `q` run through odd integers and set

\[
\gamma_q=\frac{q-1}{2q}.
\tag{19}
\]

This character has exact order `q`, while

\[
4\sin^2(\pi\gamma_q)\longrightarrow4
\tag{20}
\]

and

\[
-\Log(1-e^{2\pi i\gamma_q})
\longrightarrow-\log2\ne0.
\tag{21}
\]

Hence any finite power `L_cyc^s` or `L_cyc^{-s}` has weights bounded above and below along this infinite high-conductor sequence, while the tangent coefficients do not tend to zero. Such powers therefore cannot turn `eta` into a Hilbert-dual vector either. The failure is not confined to the soft sequence `1/q`: conductor is invisible across the whole bounded trigonometric spectrum.

## 5. Finite-range polygon-edge refinements remain bounded

A natural objection is that nearest neighbor may be too restrictive. Suppose one keeps finitely many integer edge steps `j` with nonnegative geometric weights `c_j` and uses

\[
\mathcal E_S(f)
=
\sum_{j\in S}c_j
\int_K|f(x+j)-f(x)|^2\,dm_H(x).
\tag{22}
\]

Then

\[
L_S
=
\sum_{j\in S}c_j(2I-U^j-U^{-j})\succeq0
\tag{23}
\]

and

\[
\boxed{
\lambda_S(\gamma)
=4\sum_{j\in S}c_j\sin^2(\pi j\gamma)
\le4\sum_{j\in S}c_j.
}
\tag{24}
\]

So every finite-range integer-step energy is still bounded and still a finite combination of leaf-time translations. Along `gamma=1/q`,

\[
\lambda_S(1/q)
\sim
\frac{4\pi^2}{q^2}
\sum_{j\in S}c_jj^2.
\tag{25}
\]

No finite local stencil derived from a fixed set of polygon steps generates a conductor-growing transverse Sobolev scale.

This does not rule out an infinite-range cross-level form whose weights are themselves intrinsically forced by richer Prime-Circle geometry. Such a form would be a genuinely new object and must be audited separately.

## 6. Matched control: the conductor operator works analytically but is an extra scale

`PC-066` classifies translation- and unit-invariant operators on `L^2(K)` as

\[
T=\sum_{n\ge1}h(n)P_n,
\tag{26}
\]

where `P_n` projects onto exact-order-`n` characters. The exact-order decomposition is canonical, but the spectral scale `h(n)` is not fixed. Choosing

\[
C\chi_\gamma
=\operatorname{ord}(\gamma)\chi_\gamma
\tag{27}
\]

gives a positive compact-resolvent operator and can of course provide conductor-growing Sobolev weights.

The cycle result identifies precisely what the embedded local geometry contributes to this ambiguity. The actual polygon edge does **not** choose `h(n)=n`, `log n`, or another growing conductor scale. It chooses the bounded phase symbol (10), which even varies among primitive characters of the same conductor because the edge geometry breaks the abstract unit symmetry.

Equivalently, the unitary `U` remembers every root-of-unity eigenphase, so one can recover its exact order by a discontinuous Borel reweighting of the dense root spectrum. But order tends to infinity along roots approaching `1`, whereas every continuous functional calculus of the local shift or of `L_cyc` remains bounded on its compact spectrum. Passing from (10) to (27) is therefore a singular conductor reweighting, not a regular consequence of the local positive edge form.

This is the matched control required by the intrinsic-geometry gate: the profinite fiber is not incapable of carrying a useful unbounded operator. What is missing is a Mathia theorem that forces the required unbounded scale rather than selecting it because it regularizes the arithmetic tangent.

## 7. Relation to WP-039 and WP-040

There is no conflict with `WP-039`. The form (7) is a perfectly valid scalar translation-invariant Markov/Dirichlet energy, but its symbol is the trigonometric quantity (10), not Mangoldt support. It therefore illustrates rather than evades the subgroup/support obstruction: canonical positive transverse diffusion exists, yet it carries no prime-power selector.

`WP-040` left open a genuinely transverse finite-adic operator because all leafwise Sobolev traces collapse to `L^2(K)`. The present calculation closes the **first embedded candidate** for that escape. The finite quotient polygons themselves do force a positive edge energy, but exact refinement compatibility turns it into the bounded odometer difference, and the solenoid diagonal relation (14) shows that this difference is already a leaf-time operator.

The remaining escape is narrower:

\[
\boxed{
\text{successful transverse regularity}
\Rightarrow
\text{intrinsically forced unbounded cross-level/conductor coupling}
}
\tag{28}
\]

or a genuinely nonseparable leaf--fiber operator before restriction. Ordinary local cycle edges and their finite-range extensions do not provide it.

## 8. Prior-art and novelty audit

No historical novelty is claimed for the ambient ingredients. The Fourier spectrum of a finite cycle graph is elementary spectral graph theory, and addition by one on an inverse limit of finite cyclic groups is the classical odometer/adding-machine construction. Targeted searches against standard cycle-Laplacian and odometer literature confirm that (8)--(10) are classical harmonic-analysis facts.

The project-specific result is the conjunction forced by Mathia's already-derived geometry:

1. the Prime-Circle divisor covers make the normalized polygon-edge form exactly compatible and uniquely fix its scalar normalization;
2. the resulting inverse-limit form is the adding-one difference on the specific anchor fiber `K=Zhat` of `PC-064`;
3. the solenoid diagonal gluing identifies that ostensibly transverse step with integer leaf time;
4. the resulting bounded spectrum fails exactly the conductor regularity demanded by the concrete tangent of `WP-037`;
5. the obvious unbounded conductor repair falls back into the scale freedom isolated by `PC-066`.

Thus this finding is not a new theorem about odometers. It is a Mathia-specific no-go for interpreting the canonical compatible polygon-edge energy as the missing positive finite-adic regularizer in the Weil-positivity program.

## 9. Boundaries and falsification tests

The claim is deliberately restricted. It does **not** rule out:

- an infinite-range transverse form whose cross-level weights are derived from a separate Prime-Circle observable;
- embedded chord/old-new couplings that are not functions of finitely many integer translations;
- a matrix-valued, graded, boundary-response, or cohomological operator;
- a genuinely nonseparable finite--archimedean form on the full solenoid;
- the conductor operator of `PC-066` if a new geometric argument independently forces its scale;
- or a nonlinear rank/volume mechanism such as `WP-030`.

The exact audit tests are:

1. for `m|n`, pull a function on `Z/mZ` back to `Z/nZ` and verify the raw edge energy scales by `n/m`;
2. impose exact compatibility and recover `a_n=c/n` using a common least multiple;
3. identify the limit form with `int |f(x+1)-f(x)|^2 dm_H`;
4. diagonalize it on `Q/Z` and recover `4 sin^2(pi gamma)`;
5. check `gamma=1/q` gives the `q^{-2}` soft mode;
6. in `(R x Zhat)/Z_diag`, verify `[(0,1)]=[(-1,0)]`;
7. insert the `WP-037` tangent coefficient and verify that all inhomogeneous powers remain `L^2`-equivalent;
8. use `gamma_q=(q-1)/(2q)` to verify that homogeneous positive/inverse powers also fail to control conductor globally;
9. replace nearest neighbor by any finite set of integer steps and verify the bounded symbol (24).

Failure of items 1--6 would invalidate the geometric/operator claim. Failure of items 7--9 would invalidate the stated regularity obstruction. None of these tests uses zeta zeros, RH, analytic continuation, or an RH-equivalent positivity theorem.

## Research consequence

The straightforward hierarchy is now sharper:

\[
\boxed{
\text{Prime-Circle polygon edges}
\to
\text{unique compatible positive form}
\to
\text{bounded odometer/leaf-time difference}
\not\to
\text{Weil transverse regularity}.
}
\]

Together `WP-037`, `WP-040`, `PC-066`, and this finding separate three notions that should not be conflated:

- the exact-order/projector **decomposition** of the profinite fiber is canonical;
- a conductor-growing **scale** on those projectors is not fixed by abstract symmetry;
- the most direct embedded local **positive geometry** fixes a scale, but it is bounded and conductor-soft.

A surviving Mathia-native route must therefore derive a new unbounded cross-level scale, or avoid scalar transverse Sobolev regularization entirely by coupling finite and archimedean sectors before the positivity theorem.