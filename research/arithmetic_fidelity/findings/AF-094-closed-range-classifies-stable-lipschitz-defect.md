# AF-094 — Closed range classifies stability of the Lipschitz-versus-linear defect

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `STABILITY-REFINEMENT`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`

## Claim

Let

\[
0\longrightarrow Z_F\xrightarrow{j}\mathcal F(F)\xrightarrow{\beta_F}F\longrightarrow0,
\qquad Z_F=\ker\beta_F,
\tag{1}
\]

be the canonical Lipschitz-free exact sequence of a real Banach space `F`, and let `K` be a real Banach space. Write

\[
R_{F,K}=j^*:\mathcal L(\mathcal F(F),K)\longrightarrow\mathcal L(Z_F,K),
\qquad R_{F,K}(S)=S|_{Z_F}.
\tag{2}
\]

AF-093 gives the algebraic identification

\[
\ker\!\left(\beta_F^*: \operatorname{Ext}(F,K)\to\operatorname{Ext}(\mathcal F(F),K)\right)
\cong
\frac{\mathcal L(Z_F,K)}{\operatorname{ran}R_{F,K}}.
\tag{3}
\]

Equip the right-hand side with its quotient seminorm

\[
\rho_{F,K}([T])
:=
\operatorname{dist}\!\left(T,\operatorname{ran}R_{F,K}\right)
=
\inf_{S\in\mathcal L(\mathcal F(F),K)}
\|T-S|_{Z_F}\|.
\tag{4}
\]

Then:

1. **The zero-seminorm classes are exactly closure-only extension defects.**
   \[
   \boxed{
   \rho_{F,K}([T])=0
   \iff
   T\in\overline{\operatorname{ran}R_{F,K}}.
   }
   \tag{5}
   \]
   Hence a nonzero algebraic class may have zero stability radius precisely when its fiber operator is nonextendable but arbitrarily well approximable by extendable operators.

2. **Hausdorffization is exactly quotienting by the closed extendable-operator space.**
   \[
   \boxed{
   \left(\mathcal L(Z_F,K)/\operatorname{ran}R_{F,K}\right)_{\rm Haus}
   \cong
   \mathcal L(Z_F,K)/\overline{\operatorname{ran}R_{F,K}}.
   }
   \tag{6}
   \]
   The right-hand side is a Banach space. The seminorm in (4) is a genuine norm on the algebraic defect space if and only if `R_{F,K}` has closed range.

3. **The seminorm is the exact operator-parameter distance from a canonical Lipschitz-split pushout to linear splitting.** For `T\in\mathcal L(Z_F,K)`, let `P_T` be the pushout extension from AF-093. It has a canonical `1`-Lipschitz right inverse, while it splits linearly exactly when `T\in\operatorname{ran}R_{F,K}`. Therefore
   \[
   \boxed{
   \rho_{F,K}([T])
   =
   \inf\{\|\Delta\|:\ P_{T+\Delta}\text{ splits linearly}\}.
   }
   \tag{7}
   \]
   This distance is taken inside the canonical pushout parameterization `T\mapsto P_T`; no metric on arbitrary representatives of an `Ext` class is asserted.

4. **Positive seminorm is exactly robust nonlinear repair in that parameterization.** If
   \[
   r=\rho_{F,K}([T])>0,
   \tag{8}
   \]
   then every perturbation `\Delta:Z_F\to K` with `\|\Delta\|<r` leaves `P_{T+\Delta}` nonsplit linearly, although every such pushout remains canonically Lipschitz-split. Conversely, if `[T]\neq0` algebraically but `\rho_{F,K}([T])=0`, there are perturbations `\Delta_n\to0` for which `P_{T+\Delta_n}` splits linearly. Thus **algebraic nontriviality and stable nontriviality are different gates**.

5. **Closed range is equivalent to a uniform extension-cost bound on the operators that are already extendable.** Define
   \[
   C_{F,K}
   :=
   \sup_{\substack{0\ne T\in\operatorname{ran}R_{F,K}}}
   \frac{
   \inf\{\|S\|:S\in\mathcal L(\mathcal F(F),K),\ S|_{Z_F}=T\}
   }{\|T\|}
   \in[1,\infty].
   \tag{9}
   \]
   Then
   \[
   \boxed{
   \operatorname{ran}R_{F,K}\text{ is closed}
   \iff
   C_{F,K}<\infty.
   }
   \tag{10}
   \]
   Equivalently, closed range means that extendability cannot require arbitrarily large ambient operator norm relative to the norm of the fiber operator being extended.

6. **The previous zero-defect gates remain stronger than closed range.** If `F` has the Lipschitz lifting property, or if `K` is an ultrasummand, AF-093 gives surjectivity of `R_{F,K}` and the defect space itself is zero. Outside those regimes, merely producing a nonextendable `T` proves only an algebraic Lipschitz-versus-linear gap. A stable gap additionally requires
   \[
   T\notin\overline{\operatorname{ran}R_{F,K}}.
   \tag{11}
   \]

The reusable Arithmetic Fidelity conclusion is therefore

\[
\boxed{
\text{nonrecoverability is algebraic; robust nonrecoverability lives beyond the closure of recoverable fiber data.}
}
\tag{12}
\]

In this category, the extra gate between the two is exactly the Hausdorff/closed-range gate.

## Derivation

### 1. The quotient seminorm detects closure, not merely range membership

Both operator spaces in (2) are Banach spaces and `R_{F,K}` is bounded with norm at most `1`. For any linear subspace `M` of a normed space `X`, the formula

\[
\|x+M\|_q=\inf_{m\in M}\|x-m\|
\tag{13}
\]

defines a seminorm on the algebraic quotient `X/M`. Its null space is exactly `\overline M/M`. Applying this with

\[
X=\mathcal L(Z_F,K),
\qquad
M=\operatorname{ran}R_{F,K}
\tag{14}
\]

proves (5). Quotienting the seminormed space by its null space yields

\[
\frac{X/M}{\overline M/M}
\cong
X/\overline M,
\tag{15}
\]

which proves (6). Since `\overline M` is a closed subspace of the Banach space `X`, the Hausdorffized quotient is Banach.

Thus AF-093's warning that its quotient is only algebraic is not cosmetic. If `\operatorname{ran}R_{F,K}` is nonclosed, there are genuinely nonzero extension classes in (3) that are invisible to the quotient seminorm.

### 2. Pushout perturbations turn the quotient seminorm into an exact stability radius

AF-093 associates to every `T:Z_F\to K` the pushout

\[
P_T=
\bigl(K\oplus_1\mathcal F(F)\bigr)
\Big/
\{(Tz,-jz):z\in Z_F\},
\tag{16}
\]

which represents the connecting class of `T`. Every `P_T\to F` has a canonical `1`-Lipschitz section induced by `\delta_F`, while

\[
P_T\text{ splits linearly}
\iff
T\in\operatorname{ran}R_{F,K}.
\tag{17}
\]

Perturbing the fiber datum by `\Delta` replaces `P_T` by `P_{T+\Delta}`. Therefore

\[
\begin{aligned}
\inf\{\|\Delta\|:P_{T+\Delta}\text{ splits linearly}\}
&=
\inf\{\|\Delta\|:T+\Delta\in\operatorname{ran}R_{F,K}\}\\
&=
\operatorname{dist}(T,\operatorname{ran}R_{F,K}),
\end{aligned}
\tag{18}
\]

which is (7).

If this distance is positive, no smaller perturbation can enter the linearly split set. If it is zero, choose extendable `T_n\to T` and put `\Delta_n=T_n-T`; then `\Delta_n\to0` and every `P_{T+\Delta_n}=P_{T_n}` splits linearly. This proves the two directions of statement 4 without assuming that the nearest extendable operator exists.

The distinction from AF-044 is instructive. In AF-044 the stable-fidelity failure set was explicitly closed by passing from actual secants to the closed secant carrier. Here the exact linear-splitting set in the operator parameter space need not be closed. The correct stable failure boundary is therefore its closure, not the algebraic set itself.

### 3. Closed range is exactly uniform control of extension cost

Let

\[
N=\ker R_{F,K}
\tag{19}
\]

and let `\widetilde R` be the induced bijection

\[
\widetilde R:
\mathcal L(\mathcal F(F),K)/N
\longrightarrow
\operatorname{ran}R_{F,K}.
\tag{20}
\]

The quotient on the left is Banach because `N` is closed. If `\operatorname{ran}R_{F,K}` is closed, it is Banach in the inherited norm, so the bounded inverse theorem gives

\[
\|S+N\|_q
\le
C\,\|R_{F,K}S\|
\tag{21}
\]

for some finite `C`. But

\[
\|S+N\|_q
=
\inf\{\|S'\|:R_{F,K}S'=R_{F,K}S\},
\tag{22}
\]

so (21) is exactly finiteness of (9).

Conversely, if (9) is finite, then `\widetilde R^{-1}` is bounded. A Cauchy sequence in `\operatorname{ran}R_{F,K}` therefore pulls back to a Cauchy sequence in the Banach quotient `\mathcal L(\mathcal F(F),K)/N`, and its limit maps back to the original operator-space limit. Hence the range is closed. This proves (10).

Notice what (10) does and does not say. It controls only fiber operators that are already extendable. It does not assert surjectivity of `R_{F,K}`. Thus a nonzero **Hausdorff** defect is possible in principle: the extendable operators may form a proper closed subspace of `\mathcal L(Z_F,K)`.

## Exact controls

### Lifting-property target

If `F` has the Lipschitz lifting property, AF-093 gives a bounded projection `\mathcal F(F)\to Z_F`. Every `T:Z_F\to K` then extends by composition with that projection, so `R_{F,K}` is surjective for every `K`. Consequently both the algebraic defect and its Hausdorffization vanish. In particular this holds for separable `F` by the Godefroy--Kalton theorem used in AF-092 and AF-093.

### Ultrasummand coefficient

If `K` is an ultrasummand, AF-093 shows that every `T:Z_F\to K` extends to `\mathcal F(F)`. Again `R_{F,K}` is surjective for every `F`, so there is no algebraic or stable defect.

### Nonlifting target

If `F` fails the Lipschitz lifting property, `I_{Z_F}` is nonextendable by AF-093 and gives a nonzero algebraic class. AF-094 does **not** infer

\[
\operatorname{dist}(I_{Z_F},\operatorname{ran}R_{F,Z_F})>0.
\tag{23}
\]

That would require a separate closed-range or quantitative nonapproximation argument. Failure of exact lifting alone therefore does not certify robust failure.

### Nonclosed-range regime

If `\operatorname{ran}R_{F,K}` is not closed, choose

\[
T\in
\overline{\operatorname{ran}R_{F,K}}
\setminus
\operatorname{ran}R_{F,K}.
\tag{24}
\]

Then `[T]\ne0` in AF-093's algebraic quotient but `\rho_{F,K}([T])=0`. The corresponding pushout is Lipschitz-split and not linearly split, yet arbitrarily small fiber-operator perturbations make it linearly split. This is the exact matched control separating existence of a recovery gap from stability of that gap.

### Proper closed-range regime

If `\operatorname{ran}R_{F,K}` is proper and closed, every nonzero class has positive seminorm, and the quotient is a nonzero Banach space. Thus the theory does not force the dichotomy “zero defect or unstable defect”; a genuinely robust nonlinear-versus-linear defect is exactly the proper-closed-range possibility.

## Prior art and novelty assessment

The quotient-seminorm, non-Hausdorff `Ext`, closed-range, and uniform extension-cost mechanisms are classical. **No novelty is claimed** for them.

- Félix Cabello Sánchez and Jesús M. F. Castillo, **“Stability constants and the homology of quasi-Banach spaces,”** *Israel Journal of Mathematics* 198(1) (2013), 347–370, DOI `10.1007/s11856-013-0026-7`, arXiv:`1307.4382`. Their projective-presentation model of `Ext` carries precisely a quotient seminorm by extendable kernel operators; they emphasize that the restriction-map image need not be closed, identify Hausdorffness with closed range, and express closed range as a uniform bound on the norm of extensions of already extendable operators.
- Félix Cabello Sánchez and Jesús M. F. Castillo, **“The Long Homology Sequence for Quasi-Banach Spaces, with Applications,”** *Positivity* 8(4) (2004), 379–394, DOI `10.1007/s11117-002-2465-y`. Role: the long homology sequence and topological-vector-space `Ext` framework from which operator restriction, connecting morphisms, and non-Hausdorff behavior arise.
- Félix Cabello Sánchez and Jesús M. F. Castillo, ***Homological Methods in Banach Space Theory***, Cambridge Studies in Advanced Mathematics 203, Cambridge University Press (2023), Chapter 4, DOI `10.1017/9781108778312.006`. Role: modern authoritative treatment of `Ext`, homology sequences, pushouts, and operator-extension obstructions.

The 2013 paper is especially decisive prior art. It already contains the general mathematical mechanism that the present live question suggests, so Arithmetic Fidelity should **not** treat “distance to extendable operators,” “Hausdorff `Ext`,” or the closed-range/uniform-extension equivalence as a new theory. The derived value of AF-094 is narrower: it specializes that classical stability mechanism to AF-093's canonical barycentric kernel and identifies exactly what stability means for the Lipschitz-versus-linear recovery gap inside the canonical pushout family.

A targeted search for the specific restriction map

\[
\mathcal L(\mathcal F(F),K)\to\mathcal L(Z_F,K)
\tag{25}
\]

and its closed-range behavior did not locate a general theorem making its range automatically closed or classifying the pairs `(F,K)` for which it is proper closed. This absence is not a novelty claim. It identifies the remaining falsifiable boundary after incorporating the classical homological prior art.

## Boundaries and failure modes

- `\rho_{F,K}` is the quotient seminorm induced by the concrete operator presentation (3). AF-094 does not assert without further work that this is identical to every previously defined natural topology on `\operatorname{Ext}(F,K)` or to a metric on arbitrary exact-sequence representatives.
- Equation (7) measures perturbations of the **fiber operator `T` in the canonical pushout parameterization**. Equivalent extensions may have very different ambient norms or section constants.
- Positive `\rho_{F,K}` is sufficient and necessary for robustness against small perturbations of `T`; it is not automatically robustness under perturbing `F`, `K`, the quotient map, the Lipschitz-free construction, or extra source structure.
- Closed range does not imply surjectivity. It separates stable from zero-radius algebraic defect, not existence from nonexistence of defect.
- Nonclosed range does not make every nonzero class zero-radius. It guarantees at least one nonzero class in `\overline{\operatorname{ran}R}\setminus\operatorname{ran}R`; classes outside the closure still have positive distance.
- The finding is Banach/Lipschitz specific. Analogous quotient-seminorm ideas in other compression categories require an exact presentation and a declared topology/norm on admissible fiber data before the same stability language is meaningful.
- No prime-specific or RH conclusion follows.

## Consequences for Arithmetic Fidelity

AF-093 resolved the qualitative defect as “fiber operators modulo extendable fiber operators.” AF-094 adds the missing stability layer: **the robust defect is fiber data modulo the closure of extendable data**, and the obstruction to turning the algebraic quotient into a genuine normed defect space is exactly closed range of the restriction operator.

This sharpens a general audit rule for the line. Whenever a compression/recovery category produces an algebraic obstruction quotient, do not infer stable structural survival from a nonzero class alone. First identify the topology carried by the admissible data and ask whether the recoverable subspace is closed. If it is not, exact nonrecoverability can disappear under arbitrarily small admissible perturbations.

For the current Lipschitz-free branch, the next nonclassical question is correspondingly narrower and concrete: determine whether the barycentric restriction map `R_{F,K}` has proper closed range for natural nonseparable `F` and non-ultrasummand `K`, or prove that the canonical barycentric geometry forces the alternative “surjective or nonclosed.” Either result would materially classify when nonlinear quotient repair carries a genuinely stable Arithmetic Fidelity obstruction rather than only an algebraic one.