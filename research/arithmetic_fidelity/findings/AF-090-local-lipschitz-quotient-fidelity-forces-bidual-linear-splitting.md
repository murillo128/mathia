# AF-090 — Local Lipschitz quotient fidelity forces bidual linear splitting

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-LOCAL-COMPLEMENTATION-BOUNDARY`, `PRIOR-ART-BOUNDARY`

## Claim

Let `E` and `F` be real or complex Banach spaces and let

\[
q:E\to F
\tag{1}
\]

be a bounded linear surjection, with kernel `K=ker q`. Suppose that on some nontrivial quotient ball there is an `L`-Lipschitz right inverse

\[
s:y_0+rB_F\to E,
\qquad
qs(y)=y.
\tag{2}
\]

Then the local nonlinear recovery already forces two stronger global structures.

### 1. Exact metric globalization after canonical bidual relaxation

Let `J_E:E\to E^{**}` and `J_F:F\to F^{**}` be the canonical embeddings. There exists a global map

\[
S:F\to E^{**}
\tag{3}
\]

such that

\[
q^{**}S=J_F,
\qquad
\operatorname{Lip}(S)\le L.
\tag{4}
\]

Thus the local Lipschitz constant is preserved **without any loss** once representatives are allowed to live in the canonical bidual completion. AF-087's factor `3` is required only by its explicit `E`-valued conical globalization; it is not a finite-compatibility loss.

### 2. Linear splitting of the full bidual quotient

The kernel `K` is locally complemented in `E`. Equivalently, `K^\perp=q^*(F^*)` is complemented in `E^*`. Consequently the bidual quotient

\[
q^{**}:E^{**}\to F^{**}
\tag{5}
\]

has a bounded **linear** right inverse

\[
V:F^{**}\to E^{**},
\qquad
q^{**}V=I_{F^{**}}.
\tag{6}
\]

Therefore a Lipschitz right inverse on one neighborhood cannot be an arbitrarily nonlinear local accident. Even without separability, it places the original exact sequence

\[
0\to K\to E\xrightarrow{q}F\to0
\tag{7}
\]

inside the classical **locally split** class, and after bidualization the sequence splits linearly.

The remaining unrestricted nonreflexive boundary from AF-089 is consequently narrower than a generic compactness problem. It is a **range/category fidelity problem**:

\[
\boxed{
\text{exact metric compatibility globalizes in }E^{**},
\quad
\text{and linear structure exists in the bidual,}
\quad
\text{but neither conclusion forces the repair to remain in }J_E(E).
}
\tag{8}
\]

This gap is genuine in the nonseparable category: the classical Aharoni--Lindenstrauss construction gives a quotient with a Lipschitz lifting but no linear lifting into the original source. In the separable setting, AF-082/Godefroy--Kalton closes that escape and forces an `E`-valued bounded linear section.

## Derivation

### 1. Center and dilate the local patch

As in AF-087, translate (2) to the origin:

\[
f(h):=s(y_0+h)-s(y_0),
\qquad h\in rB_F.
\tag{9}
\]

Then

\[
f(0)=0,
\qquad
qf(h)=h,
\qquad
\operatorname{Lip}(f)\le L,
\qquad
\|f(h)\|\le L\|h\|.
\tag{10}
\]

For every positive integer `n`, define

\[
f_n(y):=n f(y/n),
\qquad y\in nrB_F.
\tag{11}
\]

Hence

\[
qf_n(y)=y,
\qquad
\operatorname{Lip}(f_n)\le L,
\qquad
\|f_n(y)\|\le L\|y\|.
\tag{12}
\]

Every finite subset of `F` therefore admits one compatible `E`-valued `L`-Lipschitz selection.

### 2. Bidual compactness closes all finite constraints at the same constant

For each `y\in F`, set

\[
K_y
:=
\{x^{**}\in E^{**}:q^{**}x^{**}=J_Fy,\ \|x^{**}\|\le L\|y\|\}.
\tag{13}
\]

Each `K_y` is nonempty by (12), after applying `J_E`. It is weak-star compact: the norm ball is weak-star compact by Banach--Alaoglu, while `q^{**}` is weak-star to weak-star continuous and therefore the affine fiber over `J_Fy` is weak-star closed.

Use AF-089's compact-fiber selection principle with base metric space `F`, target `E^{**}` carrying its weak-star topology, and distance

\[
d(u,v)=\|u-v\|.
\tag{14}
\]

Norm-distance sublevel sets are weak-star closed. For every finite `A\subset F`, choose `n` large enough that `A\subset nrB_F`; then

\[
y\mapsto J_E f_n(y)
\tag{15}
\]

is a selection from the fibers `(K_y)_{y\in A}` satisfying every pairwise `L`-Lipschitz inequality. The compact-fiber principle therefore produces one global selection `S` satisfying (3)--(4).

No reflexivity, separability, chosen predual, or weak-star compatibility of the original map `q:E\to F` is needed. Passing to the canonical bidual automatically supplies the compact topology compatible with the quotient equation.

### 3. The same local patch makes the kernel a Lipschitz retract

AF-087 gives an `E`-valued global right inverse

\[
H:F\to E,
\qquad
qH=I_F,
\qquad
\operatorname{Lip}(H)\le3L.
\tag{16}
\]

Replace `H` by `H-H(0)` so that `H(0)=0` without changing its Lipschitz constant or right-inverse identity. Define

\[
R:E\to K,
\qquad
R(x):=x-H(qx).
\tag{17}
\]

Then

\[
qR(x)=qx-qH(qx)=0,
\tag{18}
\]

so `R(x)\in K`, while for `k\in K`,

\[
R(k)=k-H(0)=k.
\tag{19}
\]

Thus `R` is a Lipschitz retraction of `E` onto the linear subspace `K`; explicitly,

\[
\operatorname{Lip}(R)
\le 1+\|q\|\operatorname{Lip}(H)
\le1+3L\|q\|.
\tag{20}
\]

Nigel Kalton's Proposition 3.21 in *The nonlinear geometry of Banach spaces* states that every linear subspace which is a Lipschitz retract of a Banach space is locally complemented. Applying that classical theorem to (17) yields

\[
K^\perp\text{ is complemented in }E^*.
\tag{21}
\]

Since `q` is a quotient map,

\[
K^\perp=q^*(F^*).
\tag{22}
\]

Hence there is a bounded linear map

\[
A:E^*\to F^*
\tag{23}
\]

with

\[
Aq^*=I_{F^*}.
\tag{24}
\]

Taking adjoints gives

\[
q^{**}A^*=(Aq^*)^*=I_{F^{**}}.
\tag{25}
\]

Therefore `V=A^*` is the bounded linear right inverse asserted in (6).

The two bidual conclusions are distinct. Equation (4) preserves the **same metric constant** on the original base `F` but need not be linear. Equation (6) is linear on the full `F^{**}`, but no claim is made that its norm equals `L`.

## Exact controls

### Reflexive-source control

If `E` is reflexive, `J_E(E)=E^{**}`. The exact metric globalization (3)--(4) therefore remains inside the original source and recovers AF-088:

\[
\lambda_{\mathrm{locLip}}(q)=\lambda_{\mathrm{Lip}}(q).
\]

Thus the new bidual statement specializes to the already-known no-loss result rather than producing an artificial extra completion.

### Weak-star-compatible dual control

If `E=X^*`, `F=Y^*`, and `q:X^*\to Y^*` is weak-star to weak-star continuous, AF-089 already obtains exact `E`-valued globalization because the relevant compact fibers are closed in the weak-star topology of `E` itself. The bidual escape is unnecessary in that category.

This identifies the missing ingredient precisely: the original representative space must itself carry a compact topology compatible with the quotient fibers if one wants the compactness argument to stay in `E`.

### Nonseparable Aharoni--Lindenstrauss control

Kalton's 2008 survey reconstructs the Aharoni--Lindenstrauss example from the quotient

\[
q:\ell^\infty\to\ell^\infty/c_0.
\]

Inside the quotient one chooses a nonseparable copy `E_0\cong c_0(I)` generated from an almost-disjoint family, and obtains a Lipschitz lifting

\[
f:E_0\to\ell^\infty,
\qquad
qf=I_{E_0},
\]

with Lipschitz constant `2`. Restricting the quotient to `q^{-1}(E_0)\to E_0` gives a nonseparable quotient with a global Lipschitz right inverse but no bounded linear right inverse; this is exactly the classical mechanism behind their Lipschitz-but-not-linear decomposition example.

The present theorem therefore cannot be strengthened from **bidual linear splitting** to **original-space linear splitting** without additional hypotheses. Its conclusion predicts instead that the kernel in this classical counterexample is locally complemented, which is consistent with Kalton's Lipschitz-retract theorem.

### Separable quotient control

When `F` is separable, AF-082/Godefroy--Kalton says that a global Lipschitz right inverse already yields a bounded linear right inverse `F\to E`. Combined with AF-087, one local Lipschitz patch therefore collapses the whole hierarchy:

\[
\text{local Lipschitz repair}
\Longrightarrow
\text{global Lipschitz repair}
\Longrightarrow
\text{linear splitting in }E.
\tag{26}
\]

The bidual boundary is relevant precisely because this final implication fails in general when separability is removed.

## Prior art and novelty assessment

The structural ingredients are classical, and no novelty is claimed for local complementation, Lipschitz retracts, bidual splitting, Banach--Alaoglu compactness, or the nonseparable nonlinear examples.

- Nigel J. Kalton, **“The nonlinear geometry of Banach spaces,”** *Revista Matemática Complutense* 21(1) (2008), 7--60. Proposition 3.21 proves that a linear subspace which is a Lipschitz retract is locally complemented. The same survey also gives a detailed reconstruction of the Aharoni--Lindenstrauss quotient/lifting example and explains why a Lipschitz lifting need not have a linear lifting in the nonseparable category.
- Israel Aharoni and Joram Lindenstrauss, **“Uniform equivalence between Banach spaces,”** *Bulletin of the American Mathematical Society* 84(2) (1978), 281--283, DOI `10.1090/S0002-9904-1978-14475-9`. This is the primary source for the classical nonseparable nonlinear-equivalence example used above.
- Gilles Godefroy and Nigel J. Kalton, **“Lipschitz-free Banach spaces,”** *Studia Mathematica* 159(1) (2003), 121--141, DOI `10.4064/sm159-1-6`. Their separable lifting theorem supplies the sharp contrasting boundary: for separable quotient targets, a Lipschitz lifting forces a bounded linear lifting with no larger norm.
- Félix Cabello Sánchez and Jesús M. F. Castillo, **“Local Methods in the Theory of Twisted Sums,”** in *Homological Methods in Banach Space Theory*, Cambridge University Press (2023). This places locally split exact sequences, finite-dimensional splitting, and their lifting/extension characterizations in the standard homological language used by (7), (21), and (25).
- AF-087--AF-089 supply the Mathia-local inputs: local-to-global `E`-valued Lipschitz existence with factor `3`, exact globalization under reflexive compactness, and the general compact-fiber principle with weak-star dual-quotient corollaries.

A targeted literature audit around Lipschitz liftings, Lipschitz retracts, local complementation, locally split exact sequences, and bidual quotient sections shows that the implication from a Lipschitz retract to local complementation is explicitly classical, and the nonseparable/separable lifting boundary is also classical. The same-constant map `F\to E^{**}` in (3)--(4) is a direct application of AF-089's elementary compact-fiber principle to the canonical bidual and is not presented as a new literature theorem.

The durable Arithmetic Fidelity result is the **combined category boundary**: a local Lipschitz patch already forces local linear splitting and full bidual linear splitting, while exact metric distortion can be globalized in the bidual without loss. The unresolved part is therefore not generic finite-scale compatibility and not absence of linear structure after completion; it is whether the required representatives can remain in the original source category with the same quantitative fidelity.

## Boundaries and failure modes

- Equation (4) gives a global map only on the canonical copy `J_F(F)\subset F^{**}` as written through the identification `F\to J_F(F)`. It does not assert an `L`-Lipschitz nonlinear section on all of `F^{**}`.
- Equation (6) gives a bounded linear section on all of `F^{**}`, but its operator norm is not claimed to equal the original local Lipschitz constant `L`.
- Local complementation of `K` is a necessary consequence here, not a sufficient condition for an `E`-valued Lipschitz right inverse of `q`.
- The Aharoni--Lindenstrauss example prevents replacing bidual linear splitting by original-space linear splitting in full generality. It does not establish a strict inequality between the optimal local and global `E`-valued Lipschitz constants.
- The result does not settle AF-089's remaining quantitative question whether every arbitrary Banach quotient satisfies `lambda_locLip(q)=lambda_Lip(q)` whenever these costs are finite. It shows instead that any strict gap must disappear after canonical bidual relaxation and must coexist with local complementation of the kernel.
- No canonicity follows. Neither the compactly selected map `S` nor the locally-complementing projection is required to be natural, equivariant, measurable, order-preserving, or compatible with an arithmetic provenance structure.
- The theorem concerns complete representative recovery for linear quotients. A discriminator-specific compression may admit a weaker faithful lift without recovering complete representatives, and nonlinear compression maps need not inherit the linear exact-sequence argument.
- No rational-prime or RH-specific conclusion follows directly. The reusable lesson is that a proposed local Lipschitz repair of lost structure cannot evade linear structure indefinitely: the escape, if any, must live in the distinction between the original range and its canonical completion, or in a weaker stability/category requirement.