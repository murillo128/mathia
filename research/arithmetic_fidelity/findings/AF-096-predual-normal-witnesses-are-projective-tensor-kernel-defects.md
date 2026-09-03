# AF-096 — Dual-coefficient predual witnesses collapse by ultrasummand linearization

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `ADMISSIBLE-WITNESS-REFINEMENT`, `DECISIVE-NEGATIVE`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`

## Claim

Let

\[
0\longrightarrow Z_F\xrightarrow{j}\mathcal F(F)\xrightarrow{\beta_F}F\longrightarrow0,
\qquad Z_F=\ker\beta_F,
\tag{1}
\]

be the canonical Lipschitz-free exact sequence of a real Banach space `F`. Fix a real Banach space `Y`, put the coefficient space in explicitly dual form

\[
K=Y^*,
\tag{2}
\]

and set

\[
P:=Z_F\widehat\otimes_\pi Y,
\qquad
Q:=\mathcal F(F)\widehat\otimes_\pi Y,
\qquad
A:=j\widehat\otimes_\pi I_Y:P\to Q.
\tag{3}
\]

Projective-tensor duality gives canonical isometric identifications

\[
P^*\cong\mathcal L(Z_F,Y^*),
\qquad
Q^*\cong\mathcal L(\mathcal F(F),Y^*),
\tag{4}
\]

under which the restriction map from AF-093--AF-095 is exactly

\[
R_{F,Y^*}=A^*:
\mathcal L(\mathcal F(F),Y^*)
\longrightarrow
\mathcal L(Z_F,Y^*).
\tag{5}
\]

For a general bounded map `A:P->Q`, weak-star continuous annihilators of `ran A^*` are represented by `ker A`. In the present barycentric setting, however, the declared dual coefficient forces a much stronger conclusion:

\[
\boxed{
R_{F,Y^*}\text{ is surjective for every Banach }F,Y.
}
\tag{6}
\]

Indeed, every dual Banach space is an ultrasummand. AF-091 therefore applies to every canonically Lipschitz-split pushout from AF-093 and forces it to split linearly. Equivalently, every bounded operator

\[
T:Z_F\to Y^*
\tag{7}
\]

extends to a bounded operator

\[
S:\mathcal F(F)\to Y^*.
\tag{8}
\]

Consequently AF-093's complete Lipschitz-versus-linear defect vanishes:

\[
\boxed{
\ker\!\left(
\beta_F^*: \operatorname{Ext}(F,Y^*)
\to
\operatorname{Ext}(\mathcal F(F),Y^*)
\right)=0.
}
\tag{9}
\]

Since `A^*=R_{F,Y^*}` is surjective, the standard adjoint bounded-below/surjectivity theorem gives

\[
\boxed{
i(A):=\inf_{\|u\|_\pi=1}\|Au\|_\pi>0.
}
\tag{10}
\]

Thus `A` is not merely injective: its range is closed and the projective tensor norm on `P` is uniformly controlled by the norm inherited through `Q`.

Define the optimal extension constant

\[
E_{F,Y}
:=
\sup_{0\ne T\in\mathcal L(Z_F,Y^*)}
\frac{
\inf\{\|S\|:S\in\mathcal L(\mathcal F(F),Y^*),\ S|_{Z_F}=T\}
}{\|T\|}.
\tag{11}
\]

Then

\[
\boxed{
E_{F,Y}=\frac1{i(A)}<\infty.
}
\tag{12}
\]

Finally, regard `P^*=\mathcal L(Z_F,Y^*)` with the weak-star topology `\sigma(P^*,P)` induced by the declared predual. Every weak-star continuous linear functional has the form

\[
\Phi_u(T)=\langle T,u\rangle,
\qquad u\in P.
\tag{13}
\]

The general annihilator identity remains

\[
\Phi_u|_{\operatorname{ran}R_{F,Y^*}}=0
\iff
u\in\ker A,
\tag{14}
\]

where the symbol on the right is the same representing tensor `u` from (13). In this specific setting (10) forces `ker A=0`, so

\[
\boxed{
W^{w^*}_{F,Y}
\cong
\ker(j\widehat\otimes_\pi I_Y)
=\{0\}.
}
\tag{15}
\]

More strongly, because `R_{F,Y^*}` is already surjective, the unrestricted AF-095 witness space also vanishes. There is no robust-but-non-normal sector hiding beyond the chosen predual:

\[
\boxed{
\operatorname{ran}R_{F,Y^*}
=
\mathcal L(Z_F,Y^*)
\Longrightarrow
W_{F,Y^*}=0
\quad\text{and}\quad
\rho_{F,Y^*}=0.
}
\tag{16}
\]

The decisive Arithmetic Fidelity conclusion is therefore a no-go result: **using a genuine Banach predual `Y` to make the coefficient `K=Y^*` supplies a natural weak-star observable category only after entering a coefficient class in which the complete Lipschitz-versus-linear quotient defect has already disappeared.** Any nontrivial defect of the AF-092--AF-095 type must have a non-ultrasummand coefficient, and hence cannot be exposed by simply declaring that same coefficient to be a dual Banach space.

## Derivation

### 1. Restriction is the adjoint projective-tensor inclusion

For Banach spaces `X,Y`, the projective tensor product satisfies

\[
(X\widehat\otimes_\pi Y)^*
\cong
\mathcal B(X\times Y)
\cong
\mathcal L(X,Y^*).
\tag{17}
\]

For `S\in\mathcal L(\mathcal F(F),Y^*)` and algebraic

\[
u=\sum_i z_i\otimes y_i,
\tag{18}
\]

one has

\[
\begin{aligned}
\langle A^*S,u\rangle
&=\langle S,Au\rangle\\
&=\sum_i\langle S(jz_i),y_i\rangle\\
&=\langle S|_{Z_F},u\rangle.
\end{aligned}
\tag{19}
\]

Density gives `A^*=R_{F,Y^*}` on the completed tensor products.

### 2. A dual coefficient is automatically an ultrasummand

Put `K=Y^*`. The canonical embedding

\[
J_{Y^*}:Y^*\to Y^{***}
\tag{20}
\]

has the norm-one left inverse

\[
J_Y^*:Y^{***}\to Y^*,
\qquad
J_Y^*J_{Y^*}=I_{Y^*}.
\tag{21}
\]

Therefore

\[
J_{Y^*}J_Y^*:Y^{***}\to J_{Y^*}(Y^*)
\tag{22}
\]

is a norm-one projection. Hence every dual Banach space is an ultrasummand in exactly the sense required by AF-091.

Now fix any `T:Z_F->Y^*`. AF-093 forms the pushout extension

\[
0\to Y^*\to P_T\to F\to0,
\tag{23}
\]

and its Dirac construction gives a canonical global `1`-Lipschitz right inverse. AF-091 applies to (23), because its kernel `Y^*` is an ultrasummand, and forces (23) to split linearly.

AF-093 identifies linear splitting of this pushout with extendability of `T` from `Z_F` to `\mathcal F(F)`. Since `T` was arbitrary, `R_{F,Y^*}` is surjective, proving (6)--(9).

This is stronger than merely saying that a particular weak-star witness cannot be found. The complete extension obstruction itself is zero in the dual-coefficient category.

### 3. Surjectivity of the adjoint gives a quantitative tensor lower bound

For a bounded operator `B:X->Z`, define its injection modulus

\[
i(B)=\inf_{\|x\|=1}\|Bx\|.
\tag{24}
\]

Also define the surjection modulus of `B^*` by

\[
q(B^*)
:=
\sup\{r\ge0:rB_{X^*}\subseteq B^*(B_{Z^*})\}.
\tag{25}
\]

The standard Hahn--Banach argument gives the exact identity

\[
\boxed{q(B^*)=i(B).}
\tag{26}
\]

Indeed, if `i(B)>=r` and `x^*` has norm at most `r`, then

\[
Bx\longmapsto x^*(x)
\tag{27}
\]

is a well-defined norm-at-most-one functional on `ran B`; Hahn--Banach extends it to some `z^*` with `||z^*||<=1`, giving `B^*z^*=x^*`. Conversely, if `rB_{X^*}` lies in `B^*(B_{Z^*})`, choose for each unit `x` a norm-one `x^*` with `x^*(x)=1`; any `z^*` satisfying `B^*z^*=rx^*` gives

\[
r\le\|Bx\|.
\tag{28}
\]

Taking the infimum yields the reverse inequality.

Apply this to `B=A`. Since `A^*=R_{F,Y^*}` is surjective, the open mapping theorem gives `q(A^*)>0`, hence (10).

Moreover the reciprocal of `q(A^*)` is exactly the worst optimal preimage norm under `A^*`. Under the identifications (4)--(5), this is precisely the extension constant (11), proving (12).

Thus the tensor inclusion and operator-extension formulations carry the same quantitative defect:

\[
\boxed{
\inf_{\|u\|_\pi=1}
\|(j\widehat\otimes_\pi I_Y)u\|_\pi
=
\frac1{E_{F,Y}}.
}
\tag{29}
\]

### 4. The formal normal-witness kernel exists abstractly but vanishes here

For any bounded `A:P->Q`, a `\sigma(P^*,P)`-continuous functional on `P^*` is evaluation at some `u\in P`. Using `R=A^*`,

\[
\Phi_u(RS)
=
\langle A^*S,u\rangle
=
\langle S,Au\rangle.
\tag{30}
\]

Because `Q^*` separates points of `Q`, this vanishes for every `S` iff `Au=0`. Hence the abstract identity

\[
W^{w^*}_{F,Y}\cong\ker A
\tag{31}
\]

is correct. But (10) yields the stronger fact

\[
\ker A=0,
\tag{32}
\]

so the normal witness space is always trivial for the declared dual coefficient.

The completion phenomenon that projective tensor products need not respect arbitrary subspaces therefore does not create a kernel for this particular barycentric inclusion when the second factor is being used as a predual of the coefficient. AF-091 closes that possibility before any witness analysis begins.

## Exact controls

### Arbitrary dual coefficient

No separability, reflexivity, finite-dimensionality, approximation property, or complementability assumption on `F` or `Y` is needed. The only special input is that the coefficient is exactly `Y^*`. That alone makes the kernel of every AF-093 pushout an ultrasummand and forces all fiber operators to extend.

### Finite-dimensional coefficient

Finite-dimensional coefficients are a special case of the dual/ultrasummand gate, not a separate phenomenon. Their previously observed absence of tensor-kernel witnesses is therefore subsumed by the stronger surjectivity result (6).

### Non-dual non-ultrasummand coefficient

A genuine Lipschitz-but-not-linear defect can still exist when the coefficient `K` is not an ultrasummand; AF-091 identifies this as a necessary escape. The Aharoni--Lindenstrauss control with kernel `c_0` remains the canonical example. The present result does not claim that every non-ultrasummand coefficient produces a defect.

### No robust-but-not-normal dual-coefficient regime

For the setup `K=Y^*`, one cannot have

\[
\overline{\operatorname{ran}R}^{\,\|\cdot\|}
\subsetneq
\overline{\operatorname{ran}R}^{\,w^*}
=P^*.
\tag{33}
\]

because `ran R=P^*` already. Thus neither an unrestricted AF-095 separator nor a weak-star discontinuous escape survives. Any such regime must be sought with a coefficient category not covered by the ultrasummand theorem, rather than by choosing a different predual for a dual coefficient.

### Tensor distortion may remain although the defect is zero

Surjectivity of `R` gives `i(A)>0`, but it need not give `i(A)=1`. The projective tensor inclusion can therefore retain all information while changing norms by a bounded factor. Equation (29) identifies that factor with the optimal uniform extension cost.

This separates **exact fidelity** from **metric distortion**: all fiber operators are recoverable, yet recovery may have a nontrivial condition number.

## Prior art and novelty assessment

The underlying mathematics is classical, and **no novelty is claimed** for dual-space bidual complementability, ultrasummands, projective-tensor duality, operator extension, injection/surjection moduli, or the adjoint bounded-below/surjectivity theorem.

- Nigel J. Kalton, **“The nonlinear geometry of Banach spaces,”** *Revista Matemática Complutense* 21(1) (2008), 7--60, DOI `10.5209/rev_REMA.2008.v21.n1.16426`. Role: the Lipschitz-retract/local-complementation mechanism used by AF-091 before ultrasummand descent.
- Félix Cabello Sánchez and Jesús M. F. Castillo, ***Homological Methods in Banach Space Theory***, Cambridge Studies in Advanced Mathematics 203, Cambridge University Press (2023), especially the local-splitting and `Ext` chapters. Role: classical statement that locally split exact sequences with ultrasummand kernel split, and the homological language used in AF-091--AF-093.
- Raymond A. Ryan, ***Introduction to Tensor Products of Banach Spaces***, Springer Monographs in Mathematics, Springer London (2002), DOI `10.1007/978-1-4471-3903-4`, Chapter 2. Role: projective-tensor duality and the classical relation between preservation of a subspace under projective tensoring and extension of operators into a dual coefficient.
- Eve Oja, **“Operators that are nuclear whenever they are nuclear for a larger range space,”** *Proceedings of the Edinburgh Mathematical Society* 47 (2004), 679--694, DOI `10.1017/S0013091502001165`. Theorems 3.1 and 3.3 explicitly connect projective-tensor inclusions, extension operators, and the injection modulus, including reciprocal quantitative extension bounds.
- Eve Oja and Vaiki Randala, **“Into isomorphisms in tensor products of Banach spaces,”** *Quaestiones Mathematicae* 32(2) (2009), 269--279, DOI `10.2989/QM.2009.32.2.9.802`. Role: quantitative projective-tensor prior art formulated directly in terms of injection modulus, extension operators, and local/projection constants.

The decisive correction supplied here is internal rather than a novelty claim. The general tensor identity `W^{w^*}\cong\ker A` is valid, but when it is specialized to the AF-093 barycentric defect with coefficient `K=Y^*`, AF-091 already forces `A^*=R` to be surjective. Therefore the nonzero-kernel and robust-but-non-normal branches are not live possibilities in this category.

## Boundaries and failure modes

- The conclusion concerns the **complete quotient-repair defect** classified by AF-092--AF-093. A discriminator-specific observable may fail or survive even when the complete extension quotient is zero.
- The result does not say that projective tensor products respect every Banach subspace for every second factor. It uses the special barycentric kernel `Z_F\subset\mathcal F(F)` together with the AF-093 canonical Lipschitz splitting and the fact that `Y^*` is an ultrasummand.
- `i(A)>0` does not mean `A` is isometric. Metric distortion and exact information loss are separate.
- A Banach coefficient that is not an ultrasummand need not possess any canonical predual. Introducing an arbitrary ambient dual representation after the fact would change the category rather than reveal an intrinsic normal witness.
- No arithmetic provenance, locality, positivity, equivariance, computability, prime specificity, or RH conclusion follows from the extension theorem.

## Consequences for Arithmetic Fidelity

AF-093 identifies complete Lipschitz nonlinear-repair defects with nonextendable operators on the forgotten barycentric fiber. AF-094 and AF-095 then distinguish algebraic, robust, and continuously witnessable defects. The dual-coefficient specialization now supplies an exact category gate:

\[
\boxed{
K=Y^*
\Longrightarrow
K\text{ ultrasummand}
\Longrightarrow
\operatorname{ran}R_{F,K}=\mathcal L(Z_F,K)
\Longrightarrow
\text{no AF-093 defect at all}.
}
\tag{34}
\]

So the attempt to obtain a more intrinsic witness merely by demanding weak-star normality from a declared predual is self-defeating for this quotient-repair model: the declaration places the coefficient in a class where the nonlinear defect vanishes before the witness category is consulted.

The live problem therefore moves one layer outward. A source-natural admissibility theory for a genuinely non-ultrasummand coefficient must be justified **without** first turning that coefficient into a dual Banach space. More generally, whenever a proposed observable category supplies extra regularity or duality, Arithmetic Fidelity must first check whether that category itself collapses the obstruction it was introduced to detect.