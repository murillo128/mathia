# AF-092 — Free-space pullback exactly classifies Lipschitz quotient repair

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `HOMOLOGICAL-REFORMULATION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`

## Claim

Let

\[
0\longrightarrow K\xrightarrow{i}E\xrightarrow{q}F\longrightarrow0
\tag{1}
\]

be a short exact sequence of real Banach spaces, and let

\[
\xi=[(1)]\in \operatorname{Ext}(F,K)
\tag{2}
\]

be its extension class. Write `\mathcal F(F)` for the Lipschitz-free Banach space over the pointed metric space `(F,0)`, let

\[
\delta_F:F\to\mathcal F(F)
\tag{3}
\]

be the Dirac embedding, and let

\[
\beta_F:\mathcal F(F)\to F
\tag{4}
\]

be the barycenter map, characterized by

\[
\beta_F\delta_F=I_F.
\tag{5}
\]

Pullback along `\beta_F` induces the usual contravariant map on extension classes

\[
\beta_F^*:\operatorname{Ext}(F,K)
\longrightarrow
\operatorname{Ext}(\mathcal F(F),K).
\tag{6}
\]

Then the following are equivalent:

1. `q` has a global Lipschitz right inverse `s:F\to E`;
2. there is a bounded linear map `U:\mathcal F(F)\to E` satisfying

   \[
   qU=\beta_F;
   \tag{7}
   \]

3. the pulled-back exact sequence `\beta_F^*(\xi)` splits linearly;
4. `\beta_F^*(\xi)=0` in `\operatorname{Ext}(\mathcal F(F),K)`.

Moreover the correspondence preserves the optimal global Lipschitz cost exactly. If

\[
\lambda_{\mathrm{Lip}}(q)
=
\inf\{\operatorname{Lip}(s):qs=I_F\},
\tag{8}
\]

and

\[
\lambda_{\mathcal F}(q)
=
\inf\{\|U\|:U:\mathcal F(F)\to E\text{ linear},\ qU=\beta_F\},
\tag{9}
\]

then

\[
\boxed{
\lambda_{\mathrm{Lip}}(q)=\lambda_{\mathcal F}(q).
}
\tag{10}
\]

Linear splitting of the original sequence remains the strictly stronger condition

\[
\xi=0.
\tag{11}
\]

Consequently the exact homological location of a **Lipschitz-but-not-linear** quotient repair is

\[
\boxed{
0\ne\xi\in\ker\beta_F^*.
}
\tag{12}
\]

Thus the nonlinear escape left after AF-090 and AF-091 is not merely described by necessary side conditions such as nonseparability or failure of bidual complementability. For a fixed extension it is exactly the part of `\operatorname{Ext}(F,K)` annihilated when the quotient target is replaced by its universal Lipschitz linearization.

AF-087 upgrades the same classification to the line's local-neighborhood category. A right inverse that is Lipschitz on one nontrivial ball globalizes to an `E`-valued global Lipschitz section, while a global section trivially restricts locally. Hence

\[
\boxed{
\text{one-ball Lipschitz repair exists}
\iff
\beta_F^*(\xi)=0.
}
\tag{13}
\]

The factor `3` from AF-087 affects only a quantitative comparison between local and global constants; it does not affect the qualitative kernel criterion.

## Derivation

### 1. Lipschitz-free linearization turns a nonlinear section into a linear pullback section

First normalize any Lipschitz right inverse `s:F\to E` at the base point. Since `qs(0)=0`, one has `s(0)\in K`; replacing `s` by

\[
s_0(y)=s(y)-s(0)
\tag{14}
\]

preserves the right-inverse identity and the Lipschitz constant and gives `s_0(0)=0`.

The defining universal property of `\mathcal F(F)` says that every basepoint-preserving Lipschitz map from `F` into a Banach space has a unique bounded linearization. Therefore there is a unique bounded linear

\[
\widehat s:\mathcal F(F)\to E
\tag{15}
\]

such that

\[
\widehat s\,\delta_F=s_0,
\qquad
\|\widehat s\|=\operatorname{Lip}(s_0).
\tag{16}
\]

Now `q\widehat s` and `\beta_F` are bounded linear maps `\mathcal F(F)\to F`, and on every Dirac vector

\[
q\widehat s\,\delta_F(y)
=qs_0(y)
=y
=\beta_F\delta_F(y).
\tag{17}
\]

The linear span of `\delta_F(F)` is dense in `\mathcal F(F)`, so

\[
q\widehat s=\beta_F.
\tag{18}
\]

Thus every Lipschitz right inverse gives a linear solution of (7) with exactly the same norm.

Conversely, if `U` satisfies (7), then

\[
s:=U\delta_F:F\to E
\tag{19}
\]

is Lipschitz and

\[
qs=qU\delta_F=\beta_F\delta_F=I_F.
\tag{20}
\]

Because `\delta_F` is an isometric embedding of the pointed metric space,

\[
\operatorname{Lip}(s)\le\|U\|.
\tag{21}
\]

Applying the linearization construction back to `s` gives an admissible operator of norm exactly `\operatorname{Lip}(s)`. Taking infima in both directions proves (10).

### 2. Equation `qU=beta_F` is exactly a splitting of the pullback extension

The pullback of (1) along `\beta_F` is

\[
P_{\beta}
=
\{(e,m)\in E\times\mathcal F(F):q(e)=\beta_F(m)\},
\tag{22}
\]

with exact sequence

\[
0\to K\to P_{\beta}\xrightarrow{\pi_2}\mathcal F(F)\to0.
\tag{23}
\]

A bounded linear right inverse of `\pi_2` must have the form

\[
m\longmapsto(U m,m)
\tag{24}
\]

for a bounded linear `U:\mathcal F(F)\to E`; membership in `P_\beta` is precisely the equation `qU=\beta_F`. Therefore (7), linear splitting of (23), and `\beta_F^*(\xi)=0` are identical statements.

This proves (1)--(4) without any separability, reflexivity, local-complementation, or kernel hypothesis.

### 3. The kernel of pullback is the exact nonlinear repair defect

By definition of `\operatorname{Ext}`, the original extension splits linearly exactly when `\xi=0`. Combining this with the preceding equivalence gives

\[
\begin{array}{ccl}
\xi=0
&\Longleftrightarrow&
\text{linear quotient repair},\\[1mm]
\beta_F^*(\xi)=0
&\Longleftrightarrow&
\text{Lipschitz quotient repair}.
\end{array}
\tag{25}
\]

Hence the difference between the two admissible recovery categories is measured exactly by

\[
\ker\beta_F^*.
\tag{26}
\]

This is stronger than saying that nonlinearity can sometimes help. It identifies which **extension obstructions are forgotten by the category change** from bounded linear sections to Lipschitz sections.

### 4. Universal target-side fidelity is equivalent to splitting the barycenter map itself

Put

\[
Z_F:=\ker\beta_F.
\tag{27}
\]

Consider the canonical free-space exact sequence

\[
0\to Z_F\to\mathcal F(F)\xrightarrow{\beta_F}F\to0.
\tag{28}
\]

The following are equivalent:

1. `\beta_F` has a bounded linear right inverse `A:F\to\mathcal F(F)`;
2. for every Banach space `K`, the map

   \[
   \beta_F^*: \operatorname{Ext}(F,K)
   \to
   \operatorname{Ext}(\mathcal F(F),K)
   \tag{29}
   \]

   is injective;
3. it suffices to require injectivity in (29) for the single kernel `K=Z_F` and the single canonical class represented by (28).

Indeed, if `\beta_F A=I_F`, contravariance of pullback gives

\[
A^*\beta_F^*
=(\beta_F A)^*
=I,
\tag{30}
\]

so `\beta_F^*` is injective for every coefficient space `K`.

Conversely, pull (28) back along `\beta_F`. The resulting sequence over `\mathcal F(F)` has the diagonal linear section

\[
m\longmapsto(m,m),
\tag{31}
\]

so its class is zero. If `\beta_F^*` is injective for `K=Z_F`, the class of (28) must itself be zero; hence `\beta_F` has a bounded linear right inverse.

Thus the classical **Lipschitz lifting property** of the target can be read as an Arithmetic Fidelity statement:

\[
\boxed{
F\text{ has the lifting property}
\iff
\beta_F^*\text{ forgets no linear extension class for any }K.
}
\tag{32}
\]

For separable `F`, Godefroy--Kalton prove the lifting property, so (32) immediately recovers AF-082's qualitative conclusion for every kernel.

### 5. AF-091 supplies the complementary kernel-side injectivity theorem

AF-091 proves that whenever `K` is an ultrasummand, any quotient extension with kernel `K` that has a Lipschitz section already splits linearly. Combining that result with (12) gives the universal coefficient-side statement

\[
\boxed{
K\text{ ultrasummand}
\Longrightarrow
\beta_F^*: \operatorname{Ext}(F,K)
\to
\operatorname{Ext}(\mathcal F(F),K)
\text{ is injective for every }F.
}
\tag{33}
\]

The two closure mechanisms are therefore dual in role:

- a target `F` with the Lipschitz lifting property kills the kernel of `\beta_F^*` for **all** coefficient spaces `K`;
- an ultrasummand coefficient `K` kills the kernel of `\beta_F^*` for **all** targets `F`.

A genuinely Lipschitz-but-not-linear exact sequence must evade both universal injectivity mechanisms. AF-091's necessary conditions `F` nonseparable and `K` non-ultrasummand are the visible geometric consequences; (12) is the exact extension-level condition.

## Exact controls

### Split extension

If `\xi=0`, then every pullback is zero, so `\beta_F^*(\xi)=0`. The theorem does not manufacture a nonlinear phenomenon out of an already split sequence. It merely records that linear repair lies inside Lipschitz repair.

### Separable target

For separable `F`, Godefroy--Kalton show that a Lipschitz right inverse of any quotient onto `F` linearizes with no larger norm. Equivalently, `\beta_F` has a bounded linear right inverse. Hence

\[
\ker\beta_F^*=\{0\}
\tag{34}
\]

for every `K`, and the free-space criterion collapses exactly to AF-082.

### Ultrasummand kernel

If `K` is reflexive, a dual Banach space, L-embedded, or otherwise complemented in `K^{**}`, AF-091 applies and again

\[
\ker\beta_F^*=\{0\}
\tag{35}
\]

for that coefficient space and every target. Nonseparability of `F` alone therefore cannot create a nonzero fidelity kernel.

### Aharoni--Lindenstrauss matched escape

The classical nonseparable quotient/lifting phenomenon used in AF-090 and AF-091 gives a quotient with a global Lipschitz right inverse but no bounded linear right inverse. Its extension class therefore supplies an actual element

\[
0\ne\xi\in\ker\beta_F^*.
\tag{36}
\]

In the standard realization the target is nonseparable and the kernel is `c_0`, which is not an ultrasummand, exactly as the two closure gates predict.

### Failure of the target lifting property is existential, not uniform in the kernel

If `F` does not have the Lipschitz lifting property, then the canonical class (28) is a nonzero element killed by `\beta_F^*`; hence at least one Lipschitz-but-not-linear quotient extension exists, with kernel `Z_F`.

This does **not** imply that `\beta_F^*` fails to be injective for every chosen `K`, nor that every nonsplit extension of `F` by `K` has a Lipschitz section. The fixed-extension criterion remains (12).

### Local patch control

AF-087 is essential only if the input hypothesis is local. Without that earlier globalization theorem, vanishing of `\beta_F^*(\xi)` classifies global Lipschitz repair, not arbitrary local regularity. The present result should therefore not be generalized to Hölder, pointwise-Lipschitz, uniformly continuous, or other categories merely by replacing the word “Lipschitz.” Each category needs its own universal linearization or recovery object.

## Prior art and novelty assessment

Every ingredient used above is classical, and **no novelty is claimed for Lipschitz-free spaces, the barycenter map, pullbacks of exact sequences, the functor `Ext`, or the Lipschitz lifting property**.

- Gilles Godefroy and Nigel J. Kalton, **“Lipschitz-free Banach spaces,”** *Studia Mathematica* 159(1) (2003), 121--141, DOI `10.4064/sm159-1-6`. This is the primary source for the universal linearization machinery and the separable lifting theorem. In particular, a quotient onto a separable Banach space with a Lipschitz right inverse has a linear right inverse.
- Félix Cabello Sánchez and Jesús M. F. Castillo, ***Homological Methods in Banach Space Theory***, Cambridge Studies in Advanced Mathematics 203, Cambridge University Press (2023), especially Chapter 2, **“The Language of Homology,”** DOI `10.1017/9781108778312.004`, and Chapter 4 on the functor `Ext`. This is the standard source used here for exact sequences, pullbacks, splitting, and contravariant `Ext` language.
- Ramón J. Aliaga, Camille Noûs, Colin Petitjean, and Antonín Procházka, **“Compact reduction in Lipschitz-free spaces,”** *Studia Mathematica* 260(3) (2021), 341--359, DOI `10.4064/sm200925-18-1`. This modern source explicitly uses the Lipschitz lifting property in the form that the barycenter map admits a bounded linear right inverse.
- Israel Aharoni and Joram Lindenstrauss, **“Uniform equivalence between Banach spaces,”** *Bulletin of the American Mathematical Society* 84(2) (1978), 281--283, DOI `10.1090/S0002-9904-1978-14475-9`, together with the detailed reconstruction in Nigel Kalton's 2008 survey. This supplies the classical nonseparable control where Lipschitz and linear splitting differ.

A targeted search for the exact packaging `\ker(\beta_F^*)` as the classifier of Lipschitz-but-not-linear quotient extensions did not identify a source stating the result in that notation. That absence is **not** a novelty claim: (12) is an immediate diagrammatic consequence of the standard Lipschitz-free universal property and the standard pullback description of `Ext`. Its durable value for Arithmetic Fidelity is organizational and falsifiable: it replaces an open-ended search for “nonlinear escapes” by one exact kernel, and it turns the target-side lifting property and the kernel-side ultrasummand theorem into two injectivity mechanisms for the same map.

This also exposes a reusable pattern beyond this particular Banach category. When a broader recovery class admits a universal linearizing object `L(F)\to F`, the difference between recovery in the broad class and recovery in the original linear category should be sought in the kernel of the induced pullback on extension obstructions. That final sentence is a research heuristic, not a theorem beyond the Lipschitz-free setting proved here.

## Boundaries and failure modes

- The theorem is stated for real Banach spaces, the standard scalar setting of the Lipschitz-free construction used in the cited sources. Complex extensions can be studied by realification or a complex free-space formalism, but no automatic complex `Ext` identification is asserted here.
- `\ker\beta_F^*` classifies **complete representative recovery for linear quotient maps**. A discriminator-specific lift may preserve only a selected property and need not define a right inverse of `q`; such weaker fidelity can lie outside this exact-sequence formalism.
- Equation (12) is qualitative. The exact cost identity (10) compares global Lipschitz sections with linear splittings of the free-space pullback, not with the original linear splitting cost. Quantitative comparison back to `\lambda_{\mathrm{lin}}(q)` requires a controlled linear section of `\beta_F` or other extra structure.
- Vanishing of `\beta_F^*(\xi)` does not make the section canonical, equivariant, measurable relative to extra structure, order preserving, or compatible with arithmetic provenance. Those requirements define smaller admissible repair categories.
- Failure of injectivity of `\beta_F^*` is not itself evidence of a useful arithmetic mechanism. It says only that the Lipschitz category forgets a linear extension obstruction.
- The result does not weaken AF-091's kernel-side obstruction. Instead it identifies exactly what AF-091 annihilates: for ultrasummand `K`, the free-space pullback has no nonzero kernel on `\operatorname{Ext}(F,K)`.
- No rational-prime or RH conclusion follows. The reusable Arithmetic Fidelity lesson is that **changing the admissible recovery category can itself be represented as a compression of obstruction theory, and the information lost by that category change is an exact kernel rather than a metaphor.**