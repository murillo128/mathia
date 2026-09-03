# AF-096 — Dual-coefficient predual witnesses collapse by ultrasummand linearization

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `ADMISSIBLE-WITNESS-REFINEMENT`, `DECISIVE-NEGATIVE`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`

## Claim

Let

\[
0\longrightarrow Z_F\xrightarrow{j}\mathcal F(F)\xrightarrow{\beta_F}F\longrightarrow0,
\qquad Z_F=\ker\beta_F,
\tag{1}
\]

be the canonical Lipschitz-free exact sequence of a real Banach space `F`. Fix a real Banach space `Y`, take the coefficient in explicitly dual form `K=Y^*`, and define

\[
P:=Z_F\widehat\otimes_\pi Y,
\qquad
Q:=\mathcal F(F)\widehat\otimes_\pi Y,
\qquad
A:=j\widehat\otimes_\pi I_Y:P\to Q.
\tag{2}
\]

Projective-tensor duality gives canonical isometric identifications

\[
P^*\cong\mathcal L(Z_F,Y^*),
\qquad
Q^*\cong\mathcal L(\mathcal F(F),Y^*),
\tag{3}
\]

under which the restriction map from AF-093--AF-095 is exactly

\[
R_{F,Y^*}=A^*:
\mathcal L(\mathcal F(F),Y^*)
\longrightarrow
\mathcal L(Z_F,Y^*).
\tag{4}
\]

The declared dual coefficient forces

\[
\boxed{
R_{F,Y^*}\text{ is surjective for every Banach }F,Y.
}
\tag{5}
\]

Indeed, every dual Banach space is an ultrasummand. Every pushout associated by AF-093 to an operator `T:Z_F\to Y^*` has a canonical global `1`-Lipschitz section, so AF-091 forces that pushout to split linearly. AF-093 then says exactly that `T` extends boundedly from `Z_F` to `\mathcal F(F)`.

Consequently the complete Lipschitz-versus-linear defect vanishes:

\[
\boxed{
\ker\!\left(
\beta_F^*: \operatorname{Ext}(F,Y^*)
\to
\operatorname{Ext}(\mathcal F(F),Y^*)
\right)=0.
}
\tag{6}
\]

Since `A^*=R_{F,Y^*}` is surjective, the adjoint bounded-below/surjectivity theorem gives

\[
\boxed{
i(A):=\inf_{\|u\|_\pi=1}\|Au\|_\pi>0.
}
\tag{7}
\]

Thus `A` is an into isomorphism, not merely an injection. If

\[
E_{F,Y}
:=
\sup_{0\ne T\in\mathcal L(Z_F,Y^*)}
\frac{
\inf\{\|S\|:S\in\mathcal L(\mathcal F(F),Y^*),\ S|_{Z_F}=T\}
}{\|T\|},
\tag{8}
\]

then the exact quantitative duality is

\[
\boxed{
E_{F,Y}=\frac1{i(A)}<\infty.
}
\tag{9}
\]

Now regard `P^*=\mathcal L(Z_F,Y^*)` with the weak-star topology `\sigma(P^*,P)` supplied by this declared predual. Every weak-star continuous linear functional is evaluation by some `u\in P`,

\[
\Phi_u(T)=\langle T,u\rangle.
\tag{10}
\]

For a general bounded `A:P\to Q`,

\[
\Phi_u|_{\operatorname{ran}A^*}=0
\iff
u_A(u):=Au=0.
\tag{11}
\]

Equivalently, in the present notation the formal predual-normal witness space is

\[
W^{w^*}_{F,Y}\cong\ker(j\widehat\otimes_\pi I_Y).
\tag{12}
\]

But (7) forces that kernel to be zero. Hence

\[
\boxed{
W^{w^*}_{F,Y}=0.
}
\tag{13}
\]

More strongly, because `R_{F,Y^*}` is already surjective, the unrestricted AF-095 witness space and stability defect vanish as well:

\[
\boxed{
\operatorname{ran}R_{F,Y^*}
=
\mathcal L(Z_F,Y^*)
\Longrightarrow
W_{F,Y^*}=0,
\qquad
\rho_{F,Y^*}=0.
}
\tag{14}
\]

The decisive Arithmetic Fidelity boundary is therefore negative: **declaring a genuine Banach predual `Y` in order to obtain weak-star-normal witnesses simultaneously places the coefficient in the dual class `Y^*`, where the complete Lipschitz-versus-linear quotient defect has already disappeared.** A nontrivial AF-092--AF-095 defect requires a non-ultrasummand coefficient and cannot be recovered merely by choosing that coefficient to be a dual Banach space.

## Derivation

### 1. Restriction is the adjoint tensor map

For Banach spaces `X,Y`,

\[
(X\widehat\otimes_\pi Y)^*
\cong
\mathcal B(X\times Y)
\cong
\mathcal L(X,Y^*).
\tag{15}
\]

For `S\in\mathcal L(\mathcal F(F),Y^*)` and an algebraic tensor

\[
u:=\sum_i z_i\otimes y_i,
\tag{16}
\]

one has

\[
\begin{aligned}
\langle A^*S,u\rangle
&=\langle S,Au\rangle\\
&=\sum_i\langle S(jz_i),y_i\rangle\\
&=\langle S|_{Z_F},u\rangle.
\end{aligned}
\tag{17}
\]

Density proves `A^*=R_{F,Y^*}` on the completed tensor products.

### 2. A dual coefficient is automatically an ultrasummand

For `K=Y^*`, the canonical embedding

\[
J_{Y^*}:Y^*\to Y^{***}
\tag{18}
\]

has the norm-one left inverse

\[
J_Y^*:Y^{***}\to Y^*,
\qquad
J_Y^*J_{Y^*}=I_{Y^*}.
\tag{19}
\]

Therefore

\[
J_{Y^*}J_Y^*:Y^{***}\to J_{Y^*}(Y^*)
\tag{20}
\]

is a norm-one projection, so `Y^*` is an ultrasummand in the precise sense used by AF-091.

Fix `T:Z_F\to Y^*`. AF-093 forms the pushout exact sequence

\[
0\to Y^*\to P_T\to F\to0,
\tag{21}
\]

and supplies a global `1`-Lipschitz section through the Dirac embedding. AF-091 therefore forces (21) to split linearly. By the pushout criterion in AF-093, this is equivalent to bounded extension of `T` to `\mathcal F(F)`. Since `T` was arbitrary, (5) follows.

This closes the issue before witness selection: there is no nonextendable fiber operator left to separate.

### 3. The injection modulus is the reciprocal extension cost

For a bounded operator `B:X\to Z`, define

\[
i(B)=\inf_{\|x\|=1}\|Bx\|
\tag{22}
\]

and the surjection modulus

\[
q(B^*)
:=
\sup\{r\ge0:rB_{X^*}\subseteq B^*(B_{Z^*})\}.
\tag{23}
\]

Hahn--Banach gives the classical identity

\[
\boxed{q(B^*)=i(B).}
\tag{24}
\]

If `i(B)>=r` and `x^*` has norm at most `r`, the functional `Bx\mapsto x^*(x)` has norm at most one on `ran B` and extends to `Z`; hence `x^*\in B^*(B_{Z^*})`. Conversely, if `rB_{X^*}\subset B^*(B_{Z^*})`, then for every unit `x` choose norm-one `x^*` with `x^*(x)=1`; a preimage of `rx^*` under `B^*` gives `r\le\|Bx\|`.

Applying this to `B=A`, surjectivity of `A^*` gives `i(A)>0`. The reciprocal surjection modulus is exactly the worst optimal preimage norm under `A^*`, which under (3)--(4) is (8). This proves (9).

Thus the tensor distortion and operator-extension conditioning are exactly dual:

\[
\boxed{
\inf_{\|u\|_\pi=1}
\|(j\widehat\otimes_\pi I_Y)u\|_\pi
=
\frac1{E_{F,Y}}.
}
\tag{25}
\]

### 4. The general normal-annihilator formula becomes vacuous here

For any `u\in P` and `S\in Q^*`,

\[
\Phi_u(A^*S)
=
\langle A^*S,u\rangle
=
\langle S,Au\rangle.
\tag{26}
\]

Since `Q^*` separates points of `Q`, `\Phi_u` annihilates `ran A^*` iff `Au=0`. That proves the general identity (12). But (7) gives `ker A=0`, so in the actual dual-coefficient barycentric setting it has only the zero witness.

The fact that completed projective tensor products need not preserve arbitrary subspaces does not produce an escape here. AF-091 supplies extra structure peculiar to the barycentric kernel and dual coefficient that forces this particular tensor inclusion to be bounded below.

## Exact controls

### Arbitrary dual coefficient

No separability, reflexivity, finite-dimensionality, approximation property, or complementability assumption on `F` or `Y` is required. The condition `K=Y^*` alone makes the pushout kernel an ultrasummand and closes the defect.

### Finite-dimensional coefficient

Finite-dimensional coefficients are only a special case of the dual/ultrasummand gate. Their absence of normal tensor-kernel witnesses is subsumed by the stronger surjectivity statement (5).

### Non-ultrasummand coefficient

A genuine Lipschitz-but-not-linear defect can still occur when the coefficient `K` is not an ultrasummand. The Aharoni--Lindenstrauss control with kernel `c_0` remains the canonical escape. AF-091 gives non-ultrasummand status only as a necessary condition, not as an existence theorem.

### No robust-but-not-normal dual regime

For `K=Y^*`, neither a weak-star-normal separator nor a singular bounded separator survives, because `ran R` is already the full operator space. Any robust-but-non-normal regime must therefore belong to a coefficient category outside the ultrasummand gate; it cannot be generated merely by selecting a different predual for a dual coefficient.

### Exact fidelity versus metric distortion

Surjectivity of `R` gives `i(A)>0`, but it need not give `i(A)=1`. All fiber operators can therefore be recoverable while the tensor inclusion still distorts norms by a bounded factor. Equation (25) identifies that factor with the optimal uniform extension cost.

## Prior art and novelty assessment

The mechanism is classical, and **no novelty is claimed** for dual-space bidual complementability, ultrasummands, projective-tensor duality, operator extension, injection/surjection moduli, or the adjoint bounded-below/surjectivity theorem.

- Nigel J. Kalton, **“The nonlinear geometry of Banach spaces,”** *Revista Matemática Complutense* 21(1) (2008), 7--60, DOI `10.5209/rev_REMA.2008.v21.n1.16426`. Role: Lipschitz-retract/local-complementation mechanism used in AF-091 before ultrasummand descent.
- Félix Cabello Sánchez and Jesús M. F. Castillo, ***Homological Methods in Banach Space Theory***, Cambridge Studies in Advanced Mathematics 203, Cambridge University Press (2023), especially the local-splitting and `Ext` chapters. Role: classical locally-split/ultrasummand and homological framework used by AF-091--AF-093.
- Raymond A. Ryan, ***Introduction to Tensor Products of Banach Spaces***, Springer Monographs in Mathematics, Springer London (2002), DOI `10.1007/978-1-4471-3903-4`, Chapter 2. Role: projective-tensor duality and the classical relation between projective subspace structure and extension of operators into dual spaces.
- Eve Oja, **“Operators that are nuclear whenever they are nuclear for a larger range space,”** *Proceedings of the Edinburgh Mathematical Society* 47 (2004), 679--694, DOI `10.1017/S0013091502001165`. Theorems 3.1 and 3.3 explicitly connect projective-tensor inclusions, extension operators, and injection modulus, including reciprocal quantitative bounds.
- Eve Oja and Vaiki Randala, **“Into isomorphisms in tensor products of Banach spaces,”** *Quaestiones Mathematicae* 32(2) (2009), 269--279, DOI `10.2989/QM.2009.32.2.9.802`. Role: quantitative projective-tensor prior art formulated directly through injection modulus, extension operators, and local/projection constants.

The durable result is an internal consistency correction rather than a novelty claim. The formal identity `W^{w^*}\cong\ker A` is valid, but after specialization to the AF-093 barycentric defect with coefficient `K=Y^*`, AF-091 already forces `A^*=R` to be surjective. Therefore nonzero normal witnesses and robust-but-non-normal dual-coefficient branches are not live possibilities.

## Boundaries and failure modes

- The conclusion concerns the **complete quotient-repair defect** classified by AF-092--AF-093. Discriminator-specific observables may have weaker recovery requirements.
- This does not say that projective tensor products preserve every Banach subspace. It uses the special barycentric kernel `Z_F\subset\mathcal F(F)`, its canonical Lipschitz-split pushouts, and the dual/ultrasummand coefficient gate.
- `i(A)>0` does not imply `A` is isometric. Exact information fidelity and quantitative conditioning remain distinct.
- A non-ultrasummand coefficient need not possess a canonical predual. Forcing it into an artificial dual representation changes the admissible category instead of revealing an intrinsic witness.
- No arithmetic provenance, locality, positivity, equivariance, computability, rational-prime specificity, or RH conclusion follows.

## Consequences for Arithmetic Fidelity

AF-093 identifies complete nonlinear-repair defects with nonextendable operators on the forgotten barycentric fiber; AF-094 and AF-095 refine these into algebraic, robust, and continuously witnessable sectors. The dual-coefficient specialization now imposes the exact category gate

\[
\boxed{
K=Y^*
\Longrightarrow
K\text{ ultrasummand}
\Longrightarrow
\operatorname{ran}R_{F,K}=\mathcal L(Z_F,K)
\Longrightarrow
\text{no AF-093 defect}.
}
\tag{27}
\]

So demanding weak-star normality by declaring a predual is self-defeating for this quotient-repair model: the declaration itself moves the coefficient into a category in which the obstruction vanishes before the witness class is consulted.

The live question moves outward. A source-natural admissibility theory for a genuinely non-ultrasummand coefficient must be justified without first turning that coefficient into a dual Banach space. More generally, whenever a proposed observable category supplies extra regularity or duality, Arithmetic Fidelity must first check whether that category collapses the obstruction it was introduced to detect.