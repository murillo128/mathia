# AF-095 — Dual witnesses exactly certify robust Lipschitz-versus-linear defect

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `DUAL-CERTIFICATE-REFINEMENT`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`

## Claim

Let

\[
0\longrightarrow Z_F\xrightarrow{j}\mathcal F(F)\xrightarrow{\beta_F}F\longrightarrow0,
\qquad Z_F=\ker\beta_F,
\tag{1}
\]

be the canonical Lipschitz-free exact sequence of a real Banach space `F`, let `K` be a real Banach space, and write

\[
R_{F,K}=j^*:\mathcal L(\mathcal F(F),K)\longrightarrow\mathcal L(Z_F,K),
\qquad R_{F,K}(S)=S|_{Z_F}.
\tag{2}
\]

Set

\[
X_{F,K}:=\mathcal L(Z_F,K),
\qquad
M_{F,K}:=\operatorname{ran}R_{F,K}.
\tag{3}
\]

AF-093 identifies the algebraic Lipschitz-versus-linear quotient-repair defect with

\[
D_{F,K}^{\rm alg}
:=X_{F,K}/M_{F,K},
\tag{4}
\]

and AF-094 equips it with the stability seminorm

\[
\rho_{F,K}([T])
=\operatorname{dist}(T,M_{F,K}).
\tag{5}
\]

Define the continuous annihilator of the extendable fiber operators by

\[
W_{F,K}
:=M_{F,K}^{\perp}
=\{\Phi\in X_{F,K}^*: \Phi(T)=0\text{ for every }T\in M_{F,K}\}.
\tag{6}
\]

Then:

1. **The stability radius is exactly the optimal dual witness margin.** For every `T\in X_{F,K}`,

   \[
   \boxed{
   \rho_{F,K}([T])
   =
   \sup_{\substack{\Phi\in W_{F,K}\\ \|\Phi\|\le1}}
   |\Phi(T)|.
   }
   \tag{7}
   \]

   If `\rho_{F,K}([T])>0`, the supremum is attained by a norm-one witness after the harmless sign normalization:

   \[
   \Phi(T)=\rho_{F,K}([T]).
   \tag{8}
   \]

2. **Robust nonlinear repair is equivalent to continuous separability from all linearly recoverable fiber data.**

   \[
   \boxed{
   \rho_{F,K}([T])>0
   \iff
   \exists\,\Phi\in X_{F,K}^*
   \text{ with }
   \Phi|_{M_{F,K}}=0,
   \ \Phi(T)\ne0.
   }
   \tag{9}
   \]

   Thus a robust Lipschitz-but-not-linear defect always has a bounded linear certificate that vanishes on every exactly extendable fiber operator.

3. **Closure-only defects are invisible to every bounded linear certificate.** If

   \[
   T\in\overline{M_{F,K}}\setminus M_{F,K},
   \tag{10}
   \]

   then `[T]\ne0` algebraically but

   \[
   \boxed{
   \Phi(T)=0
   \quad\text{for every }\Phi\in W_{F,K}.
   }
   \tag{11}
   \]

   Hence the unstable defects isolated by AF-094 are not merely small. They are **continuously dual-indistinguishable from zero** in the canonical operator parameterization.

4. **The full bounded witness space is exactly the dual of the Hausdorffized defect.** Since annihilators do not distinguish a subspace from its norm closure,

   \[
   M_{F,K}^{\perp}
   =\overline{M_{F,K}}^{\perp},
   \tag{12}
   \]

   and standard quotient duality gives the isometric identification

   \[
   \boxed{
   \left(
   X_{F,K}/\overline{M_{F,K}}
   \right)^*
   \cong
   W_{F,K}.
   }
   \tag{13}
   \]

   Thus passing from AF-093's algebraic defect to AF-094's Hausdorffized defect removes **exactly** the classes that no bounded linear observable can detect.

5. **Witnesses are the kernel of the adjoint restriction map.** The Banach-space adjoint

   \[
   R_{F,K}^*:
   X_{F,K}^*
   \longrightarrow
   \mathcal L(\mathcal F(F),K)^*
   \tag{14}
   \]

   satisfies

   \[
   \boxed{
   W_{F,K}=\ker R_{F,K}^*.
   }
   \tag{15}
   \]

   Consequently

   \[
   \boxed{
   \text{a robust Lipschitz-versus-linear defect exists}
   \iff
   \ker R_{F,K}^*\ne\{0\}
   \iff
   \overline{\operatorname{ran}R_{F,K}}
e X_{F,K}.
   }
   \tag{16}
   \]

6. **There are four logically distinct recovery regimes.** The operator range can be:

   - **surjective:** no algebraic defect exists;
   - **proper dense:** algebraic defects exist, but every one has zero stability radius and every bounded dual witness vanishes;
   - **nonclosed with proper closure:** unstable and robust algebraic defects coexist;
   - **proper closed:** every nonzero algebraic defect is robust and has a norm-one separating witness.

   AF-094's closed-range gate therefore characterizes when **all** algebraic defects are stable. Equation (16) gives the weaker and different gate for whether **any** stable defect exists.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{robust information loss is exactly loss that admits a continuous separating witness;}
}
\tag{17}
\]

whereas purely algebraic loss inside the closure of recoverable data is invisible to every bounded linear discriminator on the canonical defect parameter space.

## Derivation

### 1. Hahn--Banach dualizes distance from the recoverable subspace

For any normed space `X`, linear subspace `M\subset X`, and `x\in X`, one has

\[
\operatorname{dist}(x,M)
=
\operatorname{dist}(x,\overline M).
\tag{18}
\]

The quotient `X/\overline M` is normed by

\[
\|x+\overline M\|_q
=
\operatorname{dist}(x,\overline M).
\tag{19}
\]

If the quotient vector `x+\overline M` is nonzero, Hahn--Banach supplies a norm-one functional `\psi` on `X/\overline M` satisfying

\[
\psi(x+\overline M)
=
\|x+\overline M\|_q
\tag{20}
\]

in the real case after changing sign if necessary. Pulling `\psi` back along the quotient map gives `\Phi\in X^*` with

\[
\Phi|_{\overline M}=0,
\qquad
\|\Phi\|=1,
\qquad
\Phi(x)=\operatorname{dist}(x,M).
\tag{21}
\]

Conversely, every `\Phi\in X^*` with `\Phi|_M=0` satisfies, for every `m\in M`,

\[
|\Phi(x)|
=|\Phi(x-m)|
\le\|\Phi\|\,\|x-m\|.
\tag{22}
\]

Taking the infimum over `m` and then the supremum over unit witnesses proves

\[
\operatorname{dist}(x,M)
=
\sup_{\substack{\Phi\in M^\perp\\\|\Phi\|\le1}}
|\Phi(x)|.
\tag{23}
\]

Applying (23) to `X=X_{F,K}`, `M=M_{F,K}`, and `x=T` proves (7)--(9).

### 2. Continuous witnesses see closure and therefore kill every unstable class

Every continuous functional vanishing on `M` also vanishes on `\overline M`, so

\[
M^\perp=\overline M^\perp.
\tag{24}
\]

If `T\in\overline M\setminus M`, then the algebraic coset `T+M` is nonzero, but every `\Phi\in M^\perp` satisfies `\Phi(T)=0`. This proves (11).

This is stronger than merely restating that `\rho([T])=0`. It identifies what zero radius means observationally: no bounded linear functional on the full fiber-operator space can separate that defect from the linearly recoverable set.

Conversely, if `T\notin\overline M`, Hahn--Banach produces a witness. Thus bounded linear witnessability and robust separation are not two independent requirements; in this normed category they are exactly the same requirement.

### 3. Quotient duality identifies the complete witness space

For a Banach space `X` and closed subspace `N`, the standard quotient-dual theorem identifies

\[
(X/N)^*\cong N^\perp
\tag{25}
\]

isometrically by composition with the quotient map. Taking

\[
N=\overline{M_{F,K}}
\tag{26}
\]

gives (13). Therefore the Hausdorffized defect does not merely have some separating functionals: its entire continuous dual is canonically the annihilator of all extendable fiber data.

This gives a clean interpretation of AF-094's Hausdorffization. The quotient

\[
X_{F,K}/M_{F,K}
\tag{27}
\]

remembers exact algebraic nonextension, while

\[
X_{F,K}/\overline{M_{F,K}}
\tag{28}
\]

remembers exactly the portion of nonextension visible to continuous linear tests.

### 4. The adjoint map makes existence of robust defects a density question

By definition of the adjoint,

\[
(R_{F,K}^*\Phi)(S)
=
\Phi(R_{F,K}S).
\tag{29}
\]

Hence

\[
R_{F,K}^*\Phi=0
\iff
\Phi\text{ vanishes on }\operatorname{ran}R_{F,K},
\tag{30}
\]

which proves (15). Hahn--Banach also gives the standard density criterion

\[
\overline{\operatorname{ran}R_{F,K}}=X_{F,K}
\iff
(\operatorname{ran}R_{F,K})^\perp=\{0\}.
\tag{31}
\]

Combining (15) and (31) proves (16).

This separates two questions that AF-094 left adjacent but not identical:

- `\operatorname{ran}R_{F,K}` is closed iff every algebraically nonzero defect has positive radius;
- `\operatorname{ran}R_{F,K}` is not dense iff at least one positive-radius defect exists.

Nonclosed range alone decides neither whether robust classes exist nor whether all nonzero classes are unstable.

## Exact controls

### Surjective range

If `F` has the Lipschitz lifting property, or if `K` is an ultrasummand, AF-093 gives

\[
M_{F,K}=X_{F,K}.
\tag{32}
\]

Then `D_{F,K}^{\rm alg}=0`, `W_{F,K}=0`, and no Lipschitz-versus-linear defect exists. In particular, separable `F` lies in this regime by the Godefroy--Kalton lifting theorem.

### Proper dense range

If

\[
M_{F,K}\subsetneq X_{F,K},
\qquad
\overline{M_{F,K}}=X_{F,K},
\tag{33}
\]

then AF-093's algebraic quotient is nonzero, yet

\[
W_{F,K}=0.
\tag{34}
\]

Every Lipschitz-but-not-linear pushout defect in this regime can be destroyed by arbitrarily small operator-parameter perturbations, and none can be certified by a bounded linear witness. This regime is a conditional control; the present finding does not assert that a particular barycentric pair `(F,K)` realizing it is known.

### Nonclosed range with proper closure

If

\[
M_{F,K}\subsetneq\overline{M_{F,K}}\subsetneq X_{F,K},
\tag{35}
\]

then there are both closure-only classes in `\overline M/M` and robust classes in `X/\overline M`. Thus “nonclosed range” must not be used as shorthand for “all nonlinear defects are unstable.” The continuous dual annihilates the first family and separates the second.

Again, this is an exact regime classification, not an assertion that every regime is realized by a currently known barycentric example.

### Proper closed range

If `M_{F,K}` is proper and closed, AF-094 shows every nonzero algebraic class has positive radius. Equation (7) now says every such class also has an exact norm-one Hahn--Banach certificate. This is the cleanest regime for a robust recovery obstruction: algebraic nonextension, metric stability, and continuous witnessability coincide.

### Nonzero `Ext` is not enough

A nonzero ambient `\operatorname{Ext}(F,K)` does not by itself imply `W_{F,K}\ne0`. AF-093 classifies only the kernel of the barycentric pullback `\beta_F^*`, not every extension class. Thus classical examples of nonzero or even Hausdorff `Ext(F,K)` cannot be promoted to robust Lipschitz-versus-linear defects without checking that the relevant class lies in the barycentric defect sector.

## Prior art and novelty assessment

The mathematical mechanism in this finding is classical functional analysis. **No novelty is claimed** for Hahn--Banach separation, annihilators, quotient duality, adjoint kernels, or the density criterion.

- Walter Rudin, ***Functional Analysis***, 2nd ed., McGraw--Hill, 1991, especially Theorem 4.9 on duals of subspaces and quotient spaces. Role: standard isometric identification `(X/M)^*\cong M^\perp` for closed `M`, based on Hahn--Banach.
- Félix Cabello Sánchez and Jesús M. F. Castillo, **“Stability constants and the homology of quasi-Banach spaces,”** *Israel Journal of Mathematics* 198(1) (2013), 347--370, DOI `10.1007/s11856-013-0026-7`, arXiv:`1307.4382`. Role: the classical homological stability framework behind AF-094, including quotient seminorms, Hausdorffness, and closed-range/operator-extension criteria.
- Félix Cabello Sánchez and Jesús M. F. Castillo, ***Homological Methods in Banach Space Theory***, Cambridge Studies in Advanced Mathematics 203, Cambridge University Press, 2023, Chapter 4. Role: authoritative modern background for the `Ext` and operator-extension framework in AF-092--AF-094.

A targeted prior-art search found the standard quotient-dual and Hahn--Banach statements, but no reason to regard their specialization here as a new functional-analytic theorem. The durable result is the exact Arithmetic Fidelity interpretation: AF-094's robust recovery radius is not merely a metric distance; it is precisely the largest margin seen by bounded discriminators that annihilate all linearly recoverable fiber data.

## Boundaries and failure modes

- The witnesses `\Phi\in W_{F,K}` are arbitrary bounded linear functionals on the Banach space `\mathcal L(Z_F,K)`. Hahn--Banach proves existence, not **canonicity**, locality, arithmetic provenance, positivity, equivariance, computability, or another application-specific admissibility property.
- Consequently an abstract witness is not yet a prime-specific discriminator and gives no RH conclusion. A concrete application must show that an admissible witness class is rich enough to contain a separating functional for the relevant defect.
- Equation (7) concerns perturbations measured in the operator norm on the canonical fiber parameter `T`. It does not define a metric on arbitrary equivalent representatives of an `Ext` class.
- `W_{F,K}=0` means absence of bounded linear witnesses in this operator parameterization. It does not rule out discontinuous algebraic functionals, nonlinear observables, or witnesses in a different topology; those belong to different fidelity categories and require separate analysis.
- Proper dense, nonclosed/proper-closure, and proper-closed regimes are logically possible for a bounded restriction operator. This finding does not claim that all four regimes are realized by barycentric restriction maps `R_{F,K}`.
- The real Banach-space convention follows AF-092--AF-094. In the complex case the distance formula uses the usual phase normalization rather than only a sign change.

## Consequences for Arithmetic Fidelity

AF-093 identified the forgotten data as fiber operators modulo extension. AF-094 separated exact algebraic nonextension from robust nonextension by taking norm closure. AF-095 now gives the dual interpretation of that closure step:

\[
\text{algebraic defect}
\supset
\text{robust/Hausdorff defect}
\longleftrightarrow
\text{bounded separating witnesses}.
\tag{36}
\]

This yields a reusable test beyond the present Lipschitz-free setting. Whenever a compression/recovery problem can be parameterized by a normed data space `X` with recoverable subspace `M`, the quotient `X/M` records exact algebraic loss, but only `X/\overline M` is visible to bounded linear discriminators. The annihilator `M^\perp` is then the exact witness space for stable loss.

For future arithmetic applications this sharpens the gate again: showing that a prime-specific datum is merely outside an exactly recoverable set is not enough for stable fidelity. One should seek an **intrinsically admissible continuous witness with a positive separation margin**. If no such witness exists in the declared category, the putative discriminator can be arbitrarily approximated by recoverable controls even though an exact algebraic distinction remains.