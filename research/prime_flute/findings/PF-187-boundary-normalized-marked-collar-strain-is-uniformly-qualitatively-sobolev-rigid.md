# PF-187 — boundary-normalized marked collar strain is uniformly qualitatively Sobolev-rigid

**Status:** `LITERATURE+DERIVED + EXACT-QUALITATIVE + POSITIVE/BOUNDARY`. PF-186 shows that small metric strain, exact symplecticity, zero annular flux, and the zero-twist reflection do not force a normalized short-collar germ into any fixed `C^1` neighborhood of the identity: localized Hamiltonian half-turns can have vanishing pointwise strain while retaining derivative `-I` on shrinking disks. At `W^{1,r}` scale, however, there is no analogous qualitative obstruction once the germ has been normalized as a boundary-preserving map of the fixed thick annulus. Kupferman--Maor--Shachar's Riemannian Reshetnyak theorem applies to compact manifolds with `C^1` boundary and gives strong `W^{1,r}` convergence to an isometry when differential distance to the orientation-preserving isometries tends to zero. Applied by compactness to the full family

\[
g_L=\frac{dx^2}{L^2+x^2}+(L^2+x^2)d\theta^2,
\qquad 0\le L\le\mu_*,
\]

this yields a **uniform qualitative modulus through the cusp limit `L=0`**. Reflection leaves only the identity and half-turn as possible limiting isometries, and the ordered PF-142 reflection marking removes the half-turn. Thus a boundary-normalized canonical germ with vanishing strain cannot stay a fixed positive `W^{1,r}` distance from the marked identity. The remaining PF-183 gate is genuinely quantitative: the argument gives no linear modulus in the strain, does not itself boundary-normalize the raw PF-179--PF-184 annular germ, and does not construct the exact-symplectic cutoff whose cost must be charged linearly to local body energy.

## Claim

Let

\[
A=[1,5/4]\times\mathbb R/\mathbb Z,
\qquad
R(x,\theta)=(x,-\theta),
\tag{1}
\]

and for `0<=L<=mu_*` put

\[
 g_L=\frac{dx^2}{L^2+x^2}+(L^2+x^2)d\theta^2.
\tag{2}
\]

Write

\[
\Gamma_0=[1,5/4]\times\{0\}
\tag{3}
\]

for the reflection-fixed component selected by the ordered PF-142 marking. Fix `1<r<infinity`. For an orientation-preserving diffeomorphism

\[
H:(A,g_L)\longrightarrow(A,g_{L'})
\tag{4}
\]

define the Riemannian differential-distortion energy

\[
\mathcal D_r(H;L,L')
:=
\left(
\int_A
\operatorname{dist}^r
\!\left(
 dH,
 SO(g_L,H^*g_{L'})
\right)
\,d\mu_{g_L}
\right)^{1/r}.
\tag{5}
\]

Here the distance is the Hilbert--Schmidt distance induced by the source and target metrics, exactly as in the Riemannian Reshetnyak theorem.

Choose once and for all a smooth Euclidean embedding of the compact annulus and use its equivalent `W^{1,r}` metric on maps. Then for every `epsilon_0>0` there exists

\[
\delta=\delta(r,\epsilon_0,\mu_*)>0
\tag{6}
\]

such that, for all `L,L' in [0,mu_*]`, if

\[
|L-L'|+\mathcal D_r(H;L,L')<\delta,
\tag{7}
\]

and

\[
HR=RH,
\qquad
H(\Gamma_0)=\Gamma_0,
\tag{8}
\]

then

\[
\boxed{
 d_{W^{1,r}}(H,\operatorname{id}_A)<\epsilon_0.
}
\tag{9}
\]

The marking condition in (8) can be separated from the rigidity statement. If only `HR=RH` is imposed, then the same argument gives

\[
\boxed{
\min\!\left\{
 d_{W^{1,r}}(H,\operatorname{id}),
 d_{W^{1,r}}(H,T_{1/2})
\right\}<\epsilon_0,
}
\tag{10}
\]

where `T_{1/2}(x,theta)=(x,theta+1/2)`. Thus the PF-142 ordered marking is exactly the discrete datum needed to select the identity from the reflection-compatible isometry set.

Equations (9)--(10) are **qualitative uniformity statements**, not linear estimates. They do not assert

\[
 d_{W^{1,r}}(H,\operatorname{id})
\le C_r\bigl(\mathcal D_r(H;L,L')+|L-L'|\bigr),
\tag{11}
\]

and therefore do not by themselves provide the summable PF-183 splice budget.

## 1. The normalized collar metrics form a compact smooth family

On the fixed slab `1<=x<=5/4`, the coefficient

\[
a_L(x)=L^2+x^2
\tag{12}
\]

satisfies uniform two-sided bounds, with all derivatives in `x` and `L` bounded on

\[
[1,5/4]\times[0,\mu_*].
\tag{13}
\]

Consequently `g_L` is a smooth compact family of uniformly equivalent Riemannian metrics all the way to `L=0`. The apparent cusp degeneration of the complete collar is absent on this normalized thick slab. Moreover

\[
\det g_L=1,
\qquad
d\mu_{g_L}=dx\,d\theta,
\tag{14}
\]

so every member of the family has exactly the same annular area.

This compactness is the only ingredient needed to make the qualitative Reshetnyak conclusion uniform in `L`; no injectivity-radius or collar-width constant degenerates on `A`.

## 2. Varying-metric small distortion reduces to one fixed limiting metric

Suppose (9) were false. Then for some `epsilon_0>0` there would be sequences

\[
L_j,L_j'\in[0,\mu_*],
\qquad
H_j:A\to A,
\tag{15}
\]

satisfying (8) and

\[
|L_j-L_j'|+\mathcal D_r(H_j;L_j,L_j')\to0,
\tag{16}
\]

while

\[
d_{W^{1,r}}(H_j,\operatorname{id})\ge\epsilon_0.
\tag{17}
\]

After a subsequence,

\[
L_j\to L_\infty,
\qquad
L_j'\to L_\infty.
\tag{18}
\]

Because the metric family converges smoothly and uniformly, the norms on bundle homomorphisms and the compact sets of orientation-preserving fiber isometries vary uniformly. Hence (16) implies

\[
\left\|
\operatorname{dist}\!\left(
 dH_j,
 SO(g_{L_\infty},H_j^*g_{L_\infty})
\right)
\right\|_{L^r(A,g_{L_\infty})}
\longrightarrow0.
\tag{19}
\]

One can make this reduction quantitative at the elementary linear-algebra level: all source/target inner products lie in one compact set, the corresponding `SO` fibers have uniformly bounded operator norm, and changing the two inner products by `o(1)` changes both the Hilbert--Schmidt norm and the `SO` fiber by `o(1)` uniformly. No hidden bound on `DH_j` is needed beyond the standard estimate `|DH_j|<=dist(DH_j,SO)+C` in these uniformly equivalent frames.

## 3. Riemannian Reshetnyak rigidity forces an isometric limit

Kupferman--Maor--Shachar prove the following form of Riemannian Reshetnyak rigidity: for compact connected oriented Riemannian manifolds, possibly with `C^1` boundary, if the `L^r` distance of `df_j` from the orientation-preserving fiber isometries tends to zero, then a subsequence converges strongly in `W^{1,r}` to a smooth isometric immersion. If the maps carry boundary to boundary and source and target have equal volume, the limit is an isometry; in particular these extra hypotheses hold for diffeomorphisms between equal-volume manifolds.

Apply that theorem to (19) with the fixed source and target

\[
(A,g_{L_\infty}).
\tag{20}
\]

Each `H_j` is a diffeomorphism of the annulus, hence maps boundary to boundary, and (14) gives equal volume. Therefore, after a further subsequence,

\[
\boxed{
H_j\longrightarrow\Phi
\quad\text{strongly in }W^{1,r},
}
\tag{21}
\]

for an orientation-preserving isometry

\[
\Phi:(A,g_{L_\infty})\to(A,g_{L_\infty}).
\tag{22}
\]

This is the nonlinear step that PF-185's infinitesimal Korn argument alone did not provide. It requires no `C^1` chart entry and is fully compatible with the PF-186 microtwists.

## 4. The annulus isometry ambiguity is only rotation, and marking kills it

The two boundary circles of `(A,g_L)` have lengths

\[
\sqrt{L^2+1},
\qquad
\sqrt{L^2+25/16},
\tag{23}
\]

and hence are intrinsically distinct for every `0<=L<=mu_*`. Any annulus isometry therefore preserves each boundary component. The intrinsic distance from the inner boundary is

\[
s_L(x)=\int_1^x\frac{du}{\sqrt{L^2+u^2}},
\tag{24}
\]

which is strictly increasing. An isometry must therefore preserve `x`.

Writing an isometry as `(x,theta)->(x,f(x,theta))`, preservation of (2) then forces

\[
\partial_x f=0,
\qquad
|\partial_\theta f|=1.
\tag{25}
\]

Orientation preservation chooses the positive sign, so every orientation-preserving isometry is

\[
T_c(x,\theta)=(x,\theta+c),
\qquad c\in\mathbb R/\mathbb Z.
\tag{26}
\]

If it commutes with `R`, then

\[
T_cR=RT_c
\quad\Longleftrightarrow\quad
2c=0\pmod1,
\tag{27}
\]

so only

\[
\operatorname{id},
\qquad
T_{1/2}
\tag{28}
\]

remain. This is exactly the half-turn ambiguity already isolated by PF-142.

Finally, `H_j(\Gamma_0)=\Gamma_0`. Strong `W^{1,r}` convergence with `r>1` passes this codimension-one trace condition to the limit, so `\Phi(\Gamma_0)=\Gamma_0`. The half-turn sends `Gamma_0` to the other reflection-fixed component and is excluded. Hence

\[
\boxed{\Phi=\operatorname{id}.}
\tag{29}
\]

Equation (21) now contradicts (17), proving the uniform statement (9). Omitting the marked-axis condition gives (10) by the same compactness contradiction.

## 5. PF-186 is a `C^1` obstruction, not a Sobolev one

PF-186's Hamiltonian microtwists satisfy much more than the hypothesis of the present theorem: their multiplicative metric strain tends to zero even in `L^infinity`, and they are boundary-fixed and canonically reflection paired. Yet the derivative equals `-I` on disks whose radii shrink exponentially.

For every finite `r`, those shrinking disks carry vanishing `L^r` mass. The logarithmic transition annulus also has vanishing strain. Thus the microtwists are consistent with

\[
H_j\to\operatorname{id}
\quad\text{in }W^{1,r}
\tag{30}
\]

while failing every fixed `C^1` neighborhood. The two findings therefore identify a sharp conceptual split:

\[
\boxed{
\text{small strain does not choose a pointwise derivative branch,}
\quad
\text{but it does force a global Sobolev branch modulo isometry.}
}
\tag{31}
\]

The ordered reflection marking then chooses the identity branch.

## 6. Consequence for the PF-183 splice program

PF-187 removes one possible failure mode from the low-regularity route. **There is no qualitative loss of nonlinear Sobolev rigidity caused by the `L->0` collar family itself** once the relative germ has been represented as a marked boundary-preserving diffeomorphism of the normalized slab. In particular, no sequence can have vanishing Riemannian strain and remain a fixed positive `W^{1,r}` distance from the marked identity.

This does not close PF-183 for two separate reasons.

First, PF-184 gives the canonical relative prime/shift map as an exact-symplectic **annular germ** on a common collar neighborhood. PF-187 assumes that the object entering the rigidity theorem has already been normalized to a self-diffeomorphism of the fixed annulus carrying its boundary to boundary. Producing that boundary normalization with the required local energy bookkeeping is part of the splice problem and must not be smuggled into the hypothesis.

Second, compactness supplies only a modulus

\[
\mathcal D_r+|L-L'|\to0
\Longrightarrow
 d_{W^{1,r}}(H,\operatorname{id})\to0,
\tag{32}
\]

not the **linear** estimate required to sum splice costs over infinitely many collars. PF-183 needs a bound charged collar-by-collar to

\[
E_r^{\mathrm{body}}(T_\eta)+|t_\eta|^r.
\tag{33}
\]

An arbitrarily slow qualitative modulus is insufficient even though each individual tail germ becomes Sobolev-small.

The live low-regularity gate is therefore narrower than before: obtain an energy-linear boundary-normalization/rigidity estimate for the canonical germ and then an exact-symplectic localization with the same linear cost. The alternative route remains to prove stronger canonical information that gives PF-185's fixed `C^1` chart entry directly.

## Prior art and novelty assessment

The imported compactness theorem is classical prior art at the level needed here:

- Raz Kupferman, Cy Maor, and Asaf Shachar, *Reshetnyak Rigidity for Riemannian Manifolds*, Archive for Rational Mechanics and Analysis 231 (2019), 367--408, DOI `10.1007/s00205-018-1282-9`, arXiv:1701.08892. Their theorem explicitly allows compact oriented manifolds with `C^1` boundary, gives strong `W^{1,p}` convergence from vanishing differential distance to orientation-preserving isometries, and upgrades the limit to an isometry for boundary-to-boundary equal-volume maps, in particular diffeomorphisms.
- Sergio Conti, Georg Dolzmann, and Stefan Müller, *Optimal Rigidity Estimates for Maps of a Compact Riemannian Manifold to Itself*, SIAM Journal on Mathematical Analysis 56 (2024), 8070--8095, DOI `10.1137/24M1650168`, arXiv:2402.06448. This is the closest quantitative neighbor: it proves the optimal linear `W^{1,p}` rigidity estimate modulo a global isometry for compact manifolds to themselves, but the theorem as currently stated does not provide the boundary version needed here.

No novelty is claimed for Riemannian Reshetnyak rigidity, for the compactness contradiction that upgrades a fixed-metric sequential theorem to a qualitative modulus over a compact metric family, or for the elementary isometry classification of a warped annulus. The project-specific durable content is their combination with the PF-142 marked normalized collar family, including the `L=0` cusp limit, to show that the post-PF-186 obstruction is **quantitative rather than qualitative at Sobolev scale**.

A targeted literature search did not locate a published theorem that simultaneously supplies the missing ingredients: the optimal linear `W^{1,r}` estimate on a compact annulus with boundary, a constant uniform over this metric family, and an energy-linear exact-symplectic localization. PF-187 does not claim such a theorem.

## Adversarial checks and evidence boundary

The conclusion survives the main failure modes only in the stated form.

- **Drop orientation.** Riemannian Reshetnyak rigidity to `SO`, not merely `O`, is essential. Oscillating orientation branches can destroy rigidity.
- **Drop the ordered mark.** Reflection leaves the half-turn `T_{1/2}`. The correct conclusion is then (10), not convergence to the identity.
- **Ask for `C^1`.** PF-186 is an explicit counterexample. Strong `W^{1,r}` convergence permits large derivative rotations on sets of vanishing measure.
- **Ask for a linear constant.** Compactness proves no rate. Equation (11) remains open in the boundary-normalized setting.
- **Apply directly to the raw canonical germ.** PF-184 supplies an annular germ, not the boundary-normalized self-map assumed here. That normalization must be proved with controlled cost.
- **Infer Schatten membership.** Nothing here establishes PF-183 equation (11), the complete PF-175 weighted hypothesis, `S_r` membership, wave/scattering equivalence, or any RH consequence.

Thus PF-187 is a positive boundary result of limited but useful force: **once boundary normalization is available, the normalized collar family has uniform qualitative nonlinear Sobolev rigidity through the cusp limit; the remaining difficulty is the quantitative energy-linear splice.**