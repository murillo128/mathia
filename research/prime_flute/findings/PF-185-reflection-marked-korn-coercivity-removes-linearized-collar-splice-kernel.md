# PF-185 — reflection marking gives uniform Korn coercivity on normalized short-collar slabs

**Status:** `LITERATURE+DERIVED + EXACT-LOCAL + POSITIVE/BOUNDARY`. PF-183 reduces the remaining prime/shift Schatten-above-trace-endpoint geometry to one energy-local exact-area splice on the fixed thick slabs `1<=|x|<=5/4`, and PF-184 proves that the canonical relative annular germ has zero flux/action and is therefore exact symplectic. A possible hidden obstruction was still left implicit: metric strain controls a map only modulo infinitesimal isometries, so a fixed-width generating-function cutoff would not be energy-local if the normalized collar carried an uncontrolled rigid mode. The zero-twist reflection marking removes that kernel **uniformly all the way to the cusp limit `L=0`**. For every `1<r<infinity`, reflection-equivariant vector fields on the normalized slab satisfy a Korn--Poincare estimate with a constant independent of the short core length. Consequently, whenever the exact relative germ lies in one fixed `C^1` generating neighborhood of the identity, the PF-184 primitive can be cut off with `L^r` first-derivative cost controlled by the already-counted body strain plus the collar-length mismatch. Thus the local PF-183 splice estimate has no linearized/Killing-field obstruction. What is **not** yet proved is that the actual PF-179--PF-182 relative germ on every true PF-138 short-collar slab enters that fixed `C^1` generating neighborhood from the presently persisted `L^r` energy information alone. No complete `S_r` classification or wave/scattering conclusion is claimed.

## Claim

Put

\[
A^+:=[1,5/4]\times \mathbb R/\mathbb Z,
\qquad
a_L(x):=L^2+x^2,
\]

and equip `A^+` with the normalized hyperbolic collar metric

\[
\boxed{
g_L=\frac{dx^2}{a_L(x)}+a_L(x)\,d\theta^2,
\qquad 0\le L\le \mu_*,
}
\tag{1}
\]

where `mu_*=2 asinh(1)` is the PF-183 short-collar threshold. Let

\[
R(x,\theta)=(x,-\theta)
\tag{2}
\]

be the zero-twist reflection.

For `1<r<infinity` there is a constant `C_r`, independent of `L in [0,mu_*]`, such that every reflection-equivariant vector field

\[
u=f\,\partial_x+q\,\partial_\theta,
\qquad
u(Rz)=DR_z\,u(z),
\tag{3}
\]

satisfies

\[
\boxed{
\|u\|_{W^{1,r}(A^+,g_L)}
\le
C_r\,
\|\operatorname{Def}_{g_L}u\|_{L^r(A^+,g_L)}.
}
\tag{4}
\]

Here `Def_g u=(1/2) L_u g`. The identical estimate holds on the negative slab by the isometry `x -> -x`.

There is also a nonlinear local consequence. Fix `r>1`. For a sufficiently small, `L`-independent `C^1` neighborhood of the identity, every smooth reflection-equivariant diffeomorphism `H` in that neighborhood satisfies

\[
\boxed{
\|H-\operatorname{id}\|_{W^{1,r}}
\le
C_r\,
\|\delta_{g_L,H^*g_L}\|_{L^r}.
}
\tag{5}
\]

If the target collar length is `L^+=e^t L`, then on the same fixed slab

\[
\boxed{
\|H-\operatorname{id}\|_{W^{1,r}}
\le
C_r\left(
\|\delta_{g_L,H^*g_{L^+}}\|_{L^r}
+|t|
\right).
}
\tag{6}
\]

Finally suppose `H` is exact symplectic for the area form `dx wedge dtheta` and lies in a fixed generating-function neighborhood of the identity on a slightly larger annulus. Then one may choose an exact-area, reflection-equivariant cutoff `K` which is the identity near `x=1`, equals `H` near `x=5/4`, and obeys

\[
\boxed{
\|K-\operatorname{id}\|_{W^{1,r}}
\le
C_r\left(
\|\delta_{g_L,H^*g_{L^+}}\|_{L^r}
+|t|
\right).
}
\tag{7}
\]

Applied to the PF-184 relative germ

\[
H_\eta=G_\eta^{-1}\circ F_{\rm body},
\tag{8}
\]

equation (7) gives the PF-183 energy-local estimate

\[
\boxed{
E_r(\operatorname{splice}_\eta;T_\eta)
\le
C_r\left(
E_r^{\rm body}(T_\eta)+|t_\eta|^r
\right)
}
\tag{9}
\]

**provided** the canonical `H_eta` lies in that one fixed generating neighborhood. PF-185 proves the uniform coercivity and the local cutoff implication; it does not silently promote the still-unproved chart-entry condition.

## 1. The normalized thick slab is a compact metric family

The point of PF-183's area coordinate is that the degenerating geodesic has disappeared from the transition geometry. On `1<=x<=5/4`,

\[
1\le a_L(x)\le \mu_*^2+(5/4)^2,
\tag{10}
\]

and all `x`-derivatives of the coefficients of `g_L` are bounded uniformly for `0<=L<=mu_*`. Thus the family (1) is uniformly elliptic and precompact in every fixed `C^k` norm on the **fixed** cylinder `A^+`. At `L=0` it converges smoothly to

\[
g_0=\frac{dx^2}{x^2}+x^2d\theta^2,
\tag{11}
\]

the standard cusp metric on this bounded horocyclic slab. Nothing degenerates metrically on the transition domain.

Classical `L^r` Korn's second inequality on a bounded Lipschitz cylinder, transferred through this compact family of coefficients, therefore gives a uniform constant

\[
\|u\|_{W^{1,r}}
\le
C_r\left(
\|\operatorname{Def}_{g_L}u\|_{L^r}
+\|u\|_{L^r}
\right).
\tag{12}
\]

The only issue in removing the zeroth-order term is the Killing-field kernel.

## 2. The only periodic Killing field is angular translation

The kernel can be computed directly, including the cusp limit. Write

\[
u=f(x,\theta)\partial_x+q(x,\theta)\partial_\theta,
\qquad
a=a_L(x).
\tag{13}
\]

The `xx`, `theta theta`, and `x theta` components of `L_u g_L=0` give

\[
f_x=\frac{x}{a}f,
\qquad
q_\theta=-\frac{x}{a}f,
\qquad
q_x=-\frac{f_\theta}{a^2}.
\tag{14}
\]

The first equation yields

\[
f(x,\theta)=c(\theta)\sqrt a.
\tag{15}
\]

Substituting into the other two gives

\[
q_\theta=-\frac{x}{\sqrt a}c(\theta),
\qquad
q_x=-\frac{c'(\theta)}{a^{3/2}}.
\tag{16}
\]

Equality of mixed derivatives forces

\[
\boxed{c''(\theta)=L^2 c(\theta).}
\tag{17}
\]

For `L>0` there is no nonzero periodic solution of (17), so `c=0`. For `L=0`, periodicity makes `c` constant, but then (16) gives `q_theta=-c`, and periodicity of `q` again forces `c=0`. Hence in every case

\[
f=0,
\qquad
q=\text{constant},
\tag{18}
\]

so the full periodic Killing kernel is exactly the one-dimensional angular-translation mode `q partial_theta`.

PF-142's marking is precisely what removes this mode. Equation (3) is equivalent to

\[
f(x,-\theta)=f(x,\theta),
\qquad
q(x,-\theta)=-q(x,\theta).
\tag{19}
\]

A constant `q` satisfying (19) is zero. Therefore the reflection-equivariant subspace has **no nonzero Killing field**, uniformly for the geodesic-cylinder regime `L>0` and the cusp limit `L=0`.

## 3. Compactness upgrades Korn's second inequality to the uniform marked estimate

Suppose (4) failed for some fixed `r in (1,infinity)`. Then there would be `L_j in [0,mu_*]` and reflection-equivariant fields `u_j` with

\[
\|u_j\|_{W^{1,r}(g_{L_j})}=1,
\qquad
\|\operatorname{Def}_{g_{L_j}}u_j\|_{L^r}\longrightarrow0.
\tag{20}
\]

After a subsequence, `L_j -> L_infinity`. Uniform equivalence of the metrics and Rellich compactness on the fixed cylinder give

\[
u_j\rightharpoonup u_\infty\quad\text{in }W^{1,r},
\qquad
u_j\to u_\infty\quad\text{in }L^r.
\tag{21}
\]

The smooth convergence `g_{L_j}->g_{L_infinity}` implies

\[
\operatorname{Def}_{g_{L_\infty}}u_\infty=0.
\tag{22}
\]

Reflection equivariance is closed under this convergence, so Section 2 forces `u_infinity=0`. Applying the uniform second inequality (12) back to `u_j` now gives

\[
1
\le
C_r\left(
\|\operatorname{Def}_{g_{L_j}}u_j\|_{L^r}
+\|u_j\|_{L^r}
\right)
\longrightarrow0,
\tag{23}
\]

a contradiction. This proves (4).

This is the exact linearized statement needed by the PF-183 route: there is no family of marked, reflection-compatible infinitesimal near-isometries whose metric strain tends to zero while its `W^{1,r}` displacement stays macroscopic.

## 4. Near the identity, metric strain controls the full marked displacement

Work in one fixed coordinate lift and write a reflection-equivariant `C^1`-small map as

\[
H=\operatorname{id}+u.
\tag{24}
\]

Because the metric family is uniformly `C^2` on the fixed slab, Taylor expansion of the pullback metric gives

\[
\frac12(H^*g_L-g_L)
=
\operatorname{Def}_{g_L}u
+\mathcal R_L(u,Du),
\tag{25}
\]

with a uniform bound

\[
|\mathcal R_L(u,Du)|
\le
C\|u\|_{C^1}\bigl(|u|+|Du|\bigr).
\tag{26}
\]

For `||u||_{C^1}` below one fixed threshold, (4) absorbs this remainder. On a fixed quasi-isometry neighborhood, the Güneysu--Thalmaier multiplicative deviation `delta` is uniformly equivalent to the norm of the relative metric tensor. Hence

\[
\|u\|_{W^{1,r}}
\le
C_r\|\delta_{g_L,H^*g_L}\|_{L^r},
\tag{27}
\]

which is (5).

For `L^+=e^tL`, direct differentiation of (1) gives on the slab

\[
|g_{L^+}-g_L|_{g_L}
\le
C\frac{L^2}{L^2+x^2}|t|
\le C|t|
\tag{28}
\]

for tail `|t|` bounded. Inserting this harmless parameter change before (27) proves (6).

The reflection hypothesis is essential. Without it, the exact rotations

\[
H_\tau(x,\theta)=(x,\theta+\tau)
\tag{29}
\]

have zero metric strain for every `tau` while remaining a nonzero distance from the marked identity. PF-142 is therefore not cosmetic normalization: it is exactly the gauge condition that makes an energy-local rigidity estimate possible.

## 5. Exactness plus marked Korn control gives an energy-local cutoff inside one generating chart

PF-184 supplies the other local compatibility condition: for the canonical relative germ `H_eta`, the one-form measuring annular action has zero period, so the germ is exact symplectic.

For a general exact symplectic `H` lying in a fixed `C^1` generating neighborhood of the identity, its graph is represented in a fixed Weinstein chart around the diagonal by

\[
\alpha=dS.
\tag{30}
\]

The chart and its inverse have uniformly bounded first two derivatives on a smaller fixed neighborhood. After fixing the additive constant of `S`,

\[
\|S\|_{W^{2,r}}
\le
C_r\|H-\operatorname{id}\|_{W^{1,r}}.
\tag{31}
\]

Choose once and for all a radial cutoff `chi(x)` which is zero near `x=1` and one near `x=5/4`. Put

\[
S_{\rm cut}=\chi S.
\tag{32}
\]

Because the transition width is fixed,

\[
\|S_{\rm cut}\|_{W^{2,r}}
\le C_r\|S\|_{W^{2,r}},
\tag{33}
\]

with no inverse collapsing-length factor. For a sufficiently small fixed generating neighborhood, the graph of `dS_cut` again defines an exact symplectic diffeomorphism `K`. It is the identity near the inner boundary and equals `H` near the outer boundary. Equations (31), (33), and smooth dependence of the graph chart give

\[
\|K-\operatorname{id}\|_{W^{1,r}}
\le
C_r\|H-\operatorname{id}\|_{W^{1,r}}.
\tag{34}
\]

If `H` commutes with the zero-twist reflection, the generating chart may be chosen reflection compatible. The exact one-form then has the induced odd parity; after fixing the additive constant, `S` has the corresponding parity. Since `chi` is radial, the cutoff retains that parity and `K` remains reflection equivariant.

Combining (6) and (34) proves (7). On the fixed thick slab, `g_L`, `g_{L^+}`, and their inverse-unit-ball weights are uniformly controlled. The metric deviation of the final map

\[
F_{\rm splice}=G\circ K
\tag{35}
\]

is therefore bounded in `L^r` by the right-hand side of (7). Applying the same construction to the inverse relative germ gives the target-side estimate. Raising to the `r`th power gives (9).

This is the energy-local version of the generating-function localization mechanism already used qualitatively in PF-182. The new point is that the marked Korn estimate charges the cutoff to the **actual local strain**, rather than to an independent worst-case per-collar `C^1` bound.

## 6. What remains open for the canonical prime/shift germ

Equation (9) would close PF-183 if the canonical

\[
H_\eta=G_\eta^{-1}\circ F_{\rm body}
\]

were known to lie, after a finite head, in one fixed `C^1` generating neighborhood on every normalized true-short-collar slab.

The current corpus does not yet establish that implication at the needed level. PF-179--PF-182 give near-isometric tail body modules and finite global `L^r` strain; PF-183 shows that the energies on the disjoint true-collar slabs are summable; PF-142 removes the constant angular phase; PF-184 removes annular flux. But `L^r` metric strain by itself does not automatically provide a **uniform `C^1` graph-chart bound** for the assembled relative germ. Classical Riemannian Reshetnyak rigidity gives the correct qualitative zero-strain limit, and `L^p` geometric rigidity/Korn theory gives strong Sobolev control modulo isometries, but neither source may be silently upgraded to the required pointwise derivative chart entry.

Thus PF-185 rules out a hidden infinitesimal/Killing obstruction and proves the desired splice estimate once chart entry is available. The next decisive test is sharper than PF-183's original broad pasting problem: prove a uniform generating-chart/low-regularity exact-localization theorem for the **actual** reflection-marked PF-184 germs from their persisted local strain control, or construct a sequence of such canonical germs showing that this upgrade fails.

A failure here would be a genuine nonlinear concentration/localization obstruction, not a phase, flux, multiplicity, or linearized rigidity mode.

## Prior art and novelty assessment

The mechanism behind (4) is classical. Korn--Poincare inequalities control vector fields modulo Killing fields; Lewicka--Muller make this kernel dependence explicit in a uniform geometric setting, while Conti--Dolzmann--Muller record `L^p` geometric rigidity for every `1<p<infinity`. Kupferman--Maor--Shachar extend the qualitative Reshetnyak rigidity principle to maps between Riemannian manifolds. PF-182 already used the standard Lagrangian-graph/generating-function cutoff for a boundary-fixed exact-area germ.

The project-specific derived content is the exact normalized family (1), the explicit periodic Killing calculation (14)--(18), the observation that PF-142 reflection marking annihilates the **entire** kernel uniformly through `L=0`, and the consequent placement of the PF-183/PF-184 splice problem: inside a fixed generating chart, its `L^r` energy-local estimate follows from standard Korn plus exact symplectic localization. No novelty is claimed for Korn's inequality, geometric rigidity, Reshetnyak rigidity, Weinstein neighborhoods, or generating functions themselves.

Closest audited literature:

- Marta Lewicka and Stefan Muller, *The uniform Korn--Poincare inequality in thin domains*, Ann. Inst. H. Poincare C Anal. Non Lineaire 28 (2011), 443--469, DOI `10.1016/j.anihpc.2011.03.003`.
- Sergio Conti, Georg Dolzmann, and Stefan Muller, *Korn's second inequality and geometric rigidity with mixed growth conditions*, Calc. Var. PDE 50 (2014), 437--454, DOI `10.1007/s00526-013-0641-5`, arXiv:1203.1138.
- Raz Kupferman, Cy Maor, and Asaf Shachar, *Reshetnyak Rigidity for Riemannian Manifolds*, Arch. Ration. Mech. Anal. 231 (2019), 367--408, DOI `10.1007/s00205-018-1282-9`, arXiv:1701.08892.

## Consequences for the research line

1. The fixed normalized short-collar slab has no degeneration of its Korn constant as `L->0`.
2. Zero-twist reflection is exactly the gauge that kills the only periodic Killing mode; without it an energy-local estimate is false even at zero strain.
3. PF-184's zero-flux result and PF-185's marked coercivity eliminate the **topological and linearized** branches of the local splice problem.
4. The remaining geometric question is genuinely nonlinear: obtain chart entry or an equally quantitative low-regularity exact localization for the canonical assembled germ.
5. The trace endpoint is untouched. All estimates here use `1<r<infinity`, matching the current `S_r`, `r>1` frontier and making no `S_1` claim.
