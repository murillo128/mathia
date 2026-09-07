# PF-192 — generic strong `L^1` geometric rigidity fails at the endpoint

**Status:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE/ROUTE-BOUNDARY`. PF-191 proves that the exact-area Lambert/body transport retains a summable strong-`L^1` metric-defect budget, but that integrability does **not** license an `r=1` version of the generic geometric-rigidity step used above the endpoint. Conti--Faraco--Maggi prove that the geometrically nonlinear Friesecke--James--Müller rigidity estimate fails in strong `L^1` on a fixed Euclidean cube, while a weak-`L^1` substitute survives. Their counterexample does not impose the prime-flute's exact-area, reflection, zero-flux, or canonical-germ constraints, so it does **not** refute the endpoint PF-183 splice itself. It does rule out treating that splice as a routine `r downarrow 1` continuation of PF-185/PF-188 or of unconstrained compact-manifold rigidity. Any strong endpoint splice must exploit additional PF structure; otherwise the natural generic endpoint is weak rather than strong.

## Claim

For every `k>0` and every dimension `n>=2`, Conti--Faraco--Maggi, Theorem 5, construct

\[
v_k\in W^{1,\infty}((0,1)^n;\mathbb R^n)
\]

such that for every `Q in SO(n)`,

\[
\boxed{
\int_{(0,1)^n}|\nabla v_k-Q|\,dx
\ge
k\int_{(0,1)^n}\operatorname{dist}(\nabla v_k,SO(n))\,dx .
}
\tag{1}
\]

Consequently there is no universal constant `C` for the strong endpoint estimate

\[
\inf_{Q\in SO(n)}\|\nabla v-Q\|_{L^1}
\le
C\,\|\operatorname{dist}(\nabla v,SO(n))\|_{L^1}
\tag{2}
\]

on a fixed cube. The same paper recalls the parallel failure of Korn's inequality in `L^1` and explicitly notes that both the linear and geometrically nonlinear estimates retain weak-`L^1` substitutes.

For the prime-flute program the durable implication is narrower:

\[
\boxed{
\text{summable strong-`L^1` metric strain}
\not\Rightarrow
\text{strong-`W^{1,1}` marked rigidity by generic endpoint theory}.
}
\tag{3}
\]

Equation (3) is a **route boundary**, not a counterexample to the canonical prime/shift maps. PF-191's endpoint mass remains valuable, but the conversion of that mass into an energy-linear exact-area splice must use structure that is absent from the generic theorem class.

## 1. The endpoint singularity is genuine, not a missing interpolation estimate

PF-185 gives, for every `1<r<infinity`, a uniform marked Korn estimate on the normalized short-collar slab and then a nonlinear `W^{1,r}` estimate once the map is in a fixed `C^1` generating neighborhood. PF-187 and PF-188 likewise use `r>1` Riemannian Reshetnyak compactness to obtain qualitative marked Sobolev branch selection.

It is tempting after PF-191 to set `r=1`: the exact-area Lambert stage now has finite strong-`L^1` defect, and the relevant transition slabs are fixed and uniformly nondegenerate. Conti--Faraco--Maggi show why that inference is not available from generic rigidity. Their nonlinear theorem is already posed on one fixed, perfectly regular domain. For arbitrarily large `k`, the distance of the gradient from every single rotation can exceed the integrated pointwise distance from the rotation group by the factor `k`. Thus no compactness of the domain, smoothness of its metric, or ordinary fixed-domain localization can by itself supply the missing strong endpoint estimate.

The obstruction is also present at the linearized level: the same paper reconstructs Ornstein's `L^1` non-inequality for Korn. Therefore PF-185's use of `r>1` is not merely a technical choice of exponent that can be closed by taking a limit of its constants. A proof at `r=1` requires a new input.

## 2. Why this does not kill the canonical exact-area route

The Conti--Faraco--Maggi theorem controls arbitrary Lipschitz maps. Its statement does **not** require

- `det dH=1` or exact symplecticity;
- zero annular flux;
- the PF-142 reflection marking;
- fixed-germ target confinement of the kind isolated by PF-188;
- boundary identity or the specific canonical PF-179--PF-184 construction.

Those omissions are decisive for interpretation. PF-184 already proves exactness of the actual relative collar germ, PF-142 fixes the angular marking, and PF-186 shows separately that even exactness plus reflection and vanishing metric strain do not force `C^1` chart entry. The new literature boundary says something different: **even if one abandons `C^1` entry and works directly at Sobolev regularity, strong `L^1` geometric rigidity is false without further structure.**

Accordingly, no claim is made here that an exact-area reflection-marked `W^{1,1}` estimate is impossible. The point is that such an estimate, if true, would be a genuinely constrained theorem that must use the PF hypotheses rather than an endpoint specialization of Friesecke--James--Müller / Conti--Dolzmann--Müller style rigidity.

## 3. The weak endpoint matches the operator frontier more naturally

After proving their strong-`L^1` counterexample, Conti--Faraco--Maggi note that Korn and geometric rigidity still hold in weak `L^1`: one can control a suitable weak-`L^1` norm of the distance from one affine/rotational branch by the strong-`L^1` strain quantity.

This is structurally consistent with the independent PF endpoint picture, without proving any operator theorem. PF-189 places the complete decoupled short-collar central sector in `S_{1,infinity}` rather than `S_1`, while PF-190 shows that extrapolating the global `S_r`, `r>1`, estimates only gives a logarithmically weaker singular-value envelope. PF-191 then removes strong-`L^1` **coefficient mass** as the obvious body obstruction. PF-192 shows that one should nevertheless not demand a generic strong-`W^{1,1}` rigidity theorem as the default geometric bridge.

There are therefore two honest endpoint routes left:

1. prove a **PF-specific strong endpoint splice** using exact symplecticity, reflection marking, canonical target control, or another special property of the actual prime/shift germ; or
2. formulate the collar localization and operator factorization directly in the appropriate **weak/Lorentz endpoint scale**, proving that the weaker geometric control is sufficient for weak-`S_1` reassembly without recreating PF-190's logarithmic loss.

Neither route is established by this finding.

## Prior art and novelty assessment

**S. Conti, D. Faraco, F. Maggi**, *A new approach to counterexamples to `L^1` estimates: Korn's inequality, geometric rigidity, and regularity for gradients of separately convex functions*, Archive for Rational Mechanics and Analysis **175** (2005), 287--300. DOI `10.1007/s00205-004-0350-5`. An open author/institute preprint is MPI MIS Preprint 93/2003.

Theorem 5 is the exact source for (1). The paper's closing remark after its proof records the weak-`L^1` endpoint substitute. No novelty is claimed for either theorem. The project-specific contribution is the placement of this classical endpoint failure against the now-sharp PF-191 geometry: **finite strong-`L^1` exact-area body mass is not enough to justify the generic strong endpoint rigidity step that the current weak-trace program might otherwise silently assume.**

A targeted audit did not identify an authoritative theorem in the searched rigidity/Korn literature that upgrades the Conti--Faraco--Maggi endpoint to the exact combination of area preservation, PF reflection marking, zero flux, and normalized-annulus geometry required here. Absence from that audit is not a novelty claim; it leaves the constrained endpoint as an explicit open gate.

## Falsification and boundary checks

This finding would be overclaimed if read as any of the following, none of which is asserted:

- strong `W^{1,1}` rigidity fails for every exact-area annulus diffeomorphism;
- the actual PF-179--PF-184 canonical germ realizes the laminate counterexample;
- weak-`L^1` geometric rigidity automatically yields weak-`S_1` relative resolvent control;
- PF-191's strong-`L^1` endpoint budget is useless;
- the `S_r`, `r>1`, program or the endpoint conservative splice is false.

A positive constrained theorem can defeat the route boundary by proving, uniformly for `0<=L,L'<=mu_*`, an estimate on the actual admissible PF class such as

\[
\|H-\iota\|_{W^{1,1}(A_0)}
\le
C\bigl(\|\delta_{g_L,H^*g_{L'}}\|_{L^1(A_1)}+|L-L'|\bigr),
\tag{4}
\]

with the necessary exact-area, marking, target, and canonical-structure hypotheses stated explicitly. Such a result would not contradict Conti--Faraco--Maggi because it restricts the map class.

Conversely, an argument that derives (4) only by citing a generic `L^p` geometric-rigidity theorem and sending `p` to `1` fails this audit. If the constrained strong estimate cannot be proved, the next decisive test is whether a weak-`W^{1,1}`/Lorentz control can be combined with an exact-symplectic cutoff and the localized critical resolvent factorization from `CLUE-weak-trace-reassembly-with-summable-local-mass.md` without an additional logarithmic loss.

## Consequences for the research line

PF-191 moves the endpoint obstruction away from body **integrability**. PF-192 now moves it away from any expectation that generic strong endpoint **rigidity** will automatically convert that integrability into a conservative splice. The endpoint geometry must be treated as a constrained problem in its own right.

For `r>1`, nothing changes: PF-185--PF-188 remain the relevant local rigidity architecture and the accepted sharp-Schatten clue still asks for the energy-linear exact-symplectic splice. At `r=1`, the weak-trace clue should regard strong `W^{1,1}` rigidity as an additional PF-specific theorem to be proved, not as inherited background. The classical weak-`L^1` substitute gives a better-matched analytic scale for the alternative endpoint route, but the exact-area cutoff and operator reassembly remain open.