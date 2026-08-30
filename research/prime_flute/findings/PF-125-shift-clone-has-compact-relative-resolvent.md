# PF-125 — the all-composite shift clone has compact relative resolvent

**Status:** `EXACT-DERIVED + LITERATURE-BACKED + NEGATIVE/DECISIVE`. The project-specific part is an explicit marked comparison between the exact prime flute and the exact all-composite shift clone `p_n -> p_n+1`. A necessary properness point is built into the construction below: every individual cusp is made **exactly isometric sufficiently deep**, so the transported metric coefficients vanish at infinity in the ordinary Fréchet sense required by Georgescu--Golénia. The final operator implication is established prior art already audited in PF-123. The result closes the shift-clone comparison at the level of the essential Laplace spectrum. No trace-class, wave/scattering, resonance, determinant, discrete-spectrum, Selberg/Ruelle, or RH conclusion is claimed.

## Claim

Let `X` be the exact zero-twist prime flute and let `X_+` be the exact all-composite shift clone of PF-106, obtained from

\[
q_n=p_n+1
\]

for odd primes `p_n`, followed by the harmless hyperbolic translation used there. Let

\[
P_n=P(2a_n,2a_{n+1},0),
\qquad
P_n^+=P(2a_n^+,2a_{n+1}^+,0)
\]

be the matched one-cusp pants, where `2a_n=\ell_n` and `2a_n^+=\ell_n^+`. PF-107 gives, on the tail,

\[
\delta_n:=a_n^+-a_n>0,
\qquad
\delta_n\longrightarrow0,
\qquad
a_n\longrightarrow\infty.
\tag{1}
\]

There is a marked homeomorphism

\[
\boxed{F:X\longrightarrow X_+}
\tag{2}
\]

which is globally bilipschitz and for which, after choosing the cusp normalization in Section 5,

\[
\boxed{
\operatorname{Bilip}(F|_{P_n})\longrightarrow1
}
\tag{3}
\]

on the escaping pants, while on **every fixed cusp** the map becomes an exact hyperbolic isometry above a finite Busemann height. More quantitatively, after discarding a finite head,

\[
\operatorname{Bilip}(F|_{P_n})
\le
1+C\max(\delta_n,\delta_{n+1})
\tag{4}
\]

for an absolute tail constant `C`.

Transport the clone metric to the prime surface,

\[
g_+:=F^*g_{X_+}.
\]

Then, in the ordinary Fréchet topology of `X`,

\[
\boxed{
\|g_+-g_X\|_{g_X}\longrightarrow0,
\qquad
\frac{d\operatorname{vol}_{g_+}}
     {d\operatorname{vol}_{g_X}}
\longrightarrow1
\qquad (x\to\infty).
}
\tag{5}
\]

The transported metric is piecewise smooth and locally bounded measurable across the canonical seam/cuff and interpolation loci, within the coefficient class audited in PF-123. Therefore Georgescu--Golénia's compact-perturbation theorem gives

\[
\boxed{
(\Delta_X+1)^{-1}
-
J(\Delta_{g_+}+1)^{-1}J^{-1}
\in\mathcal K,
}
\tag{6}
\]

where `J` is the bounded identity identification between the two `L^2` realizations, and hence

\[
\boxed{
\sigma_{\mathrm{ess}}(\Delta_X)
=
\sigma_{\mathrm{ess}}(\Delta_{X_+}).
}
\tag{7}
\]

Thus the essential Laplace spectrum, and any invariant determined only by the compact-resolvent class, cannot distinguish this exact prime flute from this exact all-composite control.

## 1. A Fermi normal form for the PF-119 Lambert piece

PF-119 splits the normalized one-cusp pentagon `P(2a,2b,0)` along its canonical artificial ray into two one-parameter ideal Lambert quadrilaterals. Write the left one as

\[
Q(a),
\]

in the upper half-plane normalization bounded by

\[
x=0,\qquad x=1,\qquad |z|=\tanh a,\qquad |z-1|=\operatorname{sech}a.
\tag{8}
\]

The side `x=1` is the artificial split ray. Put

\[
s=\operatorname{sech}a.
\]

Use Fermi coordinates around `x=1`, with `rho>=0` pointing into the quadrilateral and `tau>=0` measuring hyperbolic arclength/Busemann height from the lower endpoint `1+i s` of that ray:

\[
\boxed{
x=1-s e^\tau\tanh\rho,
\qquad
y=s e^\tau\operatorname{sech}\rho.
}
\tag{9}
\]

A direct calculation gives the parameter-independent metric

\[
\boxed{
ds^2=d\rho^2+\cosh^2\rho\,d\tau^2.
}
\tag{10}
\]

In these coordinates the split ray is `rho=0`, the common-perpendicular side is `tau=0`, and the opposite boundary is a graph

\[
0\le\rho\le H_a(\tau).
\]

The graph has two exact branches. The finite-cuff circle gives

\[
\tanh H_a(\tau)=s\cosh\tau,
\qquad 0\le\tau\le T_a,
\tag{11}
\]

and the outer cusp ray `x=0` gives

\[
\tanh H_a(\tau)=\cosh(a)e^{-\tau},
\qquad \tau\ge T_a.
\tag{12}
\]

The two meet at

\[
\boxed{T_a=\frac12\log\cosh(2a).}
\tag{13}
\]

At that corner,

\[
\tanh H_a(T_a)
=
\frac1{\sqrt{2-\operatorname{sech}^2a}},
\tag{14}
\]

so

\[
H_a(T_a)\longrightarrow
\operatorname{artanh}\frac1{\sqrt2}>0.
\tag{15}
\]

This nonzero limiting Fermi width is the key local nondegeneracy: the only kink in the boundary graph occurs inside a uniformly thick Fermi strip despite the collapsing Euclidean `sech(a)` scale.

## 2. The moving corner is only an `O(delta)` shear

Let

\[
a'=a+\delta,
\qquad
0<\delta\ll1.
\]

The target corner shift is

\[
\boxed{
\Delta:=T_{a'}-T_a
=
\int_a^{a'}\tanh(2u)\,du,
\qquad
0<\Delta\le\delta.
}
\tag{16}
\]

Away from a fixed neighborhood of `T_a`, source and target graphs are on the same branch. There the radial map

\[
(\rho,\tau)
\longmapsto
\left(
\frac{H_{a'}(\tau)}{H_a(\tau)}\rho,
\tau
\right)
\tag{17}
\]

is uniformly `1+O(delta)` bilipschitz. On the finite branch the only varying parameter is `s=sech(a)`, while on the outer branch it is `cosh(a)`. Staying a fixed distance from the corner gives

\[
\frac{H_{a'}(\tau)}{H_a(\tau)}
=1+O(\delta),
\qquad
H_a(\tau)
\partial_\tau
\left(
\frac{H_{a'}(\tau)}{H_a(\tau)}
\right)
=O(\delta)
\tag{18}
\]

uniformly, including where `H_a(\tau)->0`. In the metric (10), these are the required differential bounds.

Near the corner put `r=\tau-T_a`. The two branches recenter exactly as

\[
\tanh H_a(T_a+r)
=
\frac12
\left(
\sqrt{2-s^2}\,e^r
+
\frac{s^2}{\sqrt{2-s^2}}e^{-r}
\right),
\qquad r\le0,
\tag{19}
\]

and

\[
\tanh H_a(T_a+r)
=
\frac{e^{-r}}{\sqrt{2-s^2}},
\qquad r\ge0.
\tag{20}
\]

For fixed small `L`, the region `|r|<=L` has a uniform positive Fermi width for large `a`, and the corner displacement is `O(delta)`. A cutoff shear supported in this fixed-width region aligns the corners with differential `I+O(delta)`; a boundary-normal correction, also supported away from the split ray, then maps the opposite boundary exactly to its target with the same distortion scale. Thus one obtains a label-preserving homeomorphism

\[
\boxed{G_{a,a'}:Q(a)\longrightarrow Q(a')}
\tag{21}
\]

with

\[
\operatorname{Bilip}(G_{a,a'})\le1+C\delta,
\tag{22}
\]

and, crucially,

\[
\boxed{G_{a,a'}(0,\tau)=(0,\tau)\quad\text{for every }\tau\ge0.}
\tag{23}
\]

The finite-cuff trace induced by this map depends only on `(a,a')`. Reflecting the trace across the two seam feet gives a full-cuff map commuting exactly with the zero-twist orientation reversal, as in PF-124.

## 3. The two Lambert maps agree exactly on the artificial split ray

Return to the physical PF-119 pentagon with finite half-cuffs `a,b`. Put

\[
A=\cosh a,
\qquad B=\cosh b,
\qquad
t=\frac{A}{A+B},
\qquad R=\frac1{A+B}.
\tag{24}
\]

Use primes for the target parameters. On the left Lambert piece the normalization is `z->z/t`; on the right it is `z->(1-z)/(1-t)`. Because (23) preserves the normalized Fermi/Busemann coordinate, restoring the physical chart scales gives on the left

\[
\frac{t'}t\frac A{A'}
=
\boxed{\frac{A+B}{A'+B'}=\frac{R'}R,}
\tag{25}
\]

while on the right

\[
\frac{1-t'}{1-t}\frac B{B'}
=
\boxed{\frac{A+B}{A'+B'}=\frac{R'}R.}
\tag{26}
\]

Hence the two independently constructed one-parameter maps agree pointwise on their common artificial split ray:

\[
\boxed{
t+iy\longmapsto t'+i\frac{R'}R\,y.}
\tag{27}
\]

No factor `t^{-1}` or `(1-t)^{-1}` survives. Arbitrarily extreme neighboring prime-gap ratios therefore do not create a hidden split-ray amplification.

## 4. From one pentagon to the zero-twist chain

Apply the maps of Section 2 to the left and right Lambert pieces of every tail pentagon. Equation (27) glues them into a single pentagon homeomorphism with

\[
\operatorname{Bilip}
\le1+C\max(|a'-a|,|b'-b|).
\tag{28}
\]

Reflect across the canonical seams to obtain a map of the full one-cusp pant. The finite half-cuff trace depends only on the matched cuff pair `(a,a')`; reflecting that trace around the two seam feet gives a full-cuff map satisfying

\[
\widehat T_{a,a'}\circ J_a
=
J_{a'}\circ\widehat T_{a,a'},
\tag{29}
\]

where `J_a(s)=-s mod 2a` is the canonical zero-twist gluing involution. Adjacent pants therefore descend to one continuous marked map across each shared cuff.

For the exact prime/shift-clone sequence, PF-107 and (28) imply

\[
K_n:=\operatorname{Bilip}(P_n\to P_n^+)
\le1+C\max(\delta_n,\delta_{n+1})
\longrightarrow1.
\tag{30}
\]

A finite initial chain can be matched with finite bilipschitz cost. Up to this point the construction gives the required small distortion on pants with index tending to infinity. **That statement alone is not yet enough for Georgescu--Golénia**, because each individual pant contains a noncompact cusp. Section 5 supplies the proper cusp normalization that turns (30) into true convergence at infinity on the complete surface.

## 5. Every cusp can be made exactly isometric sufficiently deep

PF-122 gives a simple fact that is decisive for the properness issue. In the physical normalization of every one-cusp pentagon, all finite boundary arcs lie below `y=1`; therefore

\[
C=\{(x,y):0\le x\le1,\ y\ge1\}
\tag{31}
\]

is literally the same standard hyperbolic cusp strip for the source and target, with metric

\[
ds^2=\frac{dx^2+dy^2}{y^2}.
\tag{32}
\]

Thus the two surfaces carry a canonical isometric deep-cusp model. There is no reason to let the Lambert comparison retain a small anisotropy all the way to infinite Busemann height.

Assemble the complete pant map from Sections 2--4 first. Fix, for example, the horocycle `y=2` and put

\[
r=\log y,
\qquad r_0=\log2.
\]

In `(x,r)` coordinates the cusp metric is

\[
\boxed{ds^2=dr^2+e^{-2r}dx^2.}
\tag{33}
\]

Let the already-constructed pant map have trace on `r=r_0`

\[
h_n(x)=(u_n(x),r_0+v_n(x)).
\tag{34}
\]

The explicit Lambert/Fermi formulas and the exact cancellation (25)--(27) give, uniformly in the split ratio,

\[
\boxed{
\|u_n-\operatorname{id}\|_{C^1}
+
\|v_n\|_{C^1}
\le C\varepsilon_n,
\qquad
\varepsilon_n:=\max(\delta_n,\delta_{n+1}).
}
\tag{35}
\]

This is just the boundary form of the existing `1+C epsilon_n` pantwise estimate on the fixed horocycle; no infinite-depth estimate is being assumed.

Choose a fixed `L>1` and a smooth cutoff

\[
\eta:[0,L]\to[0,1],
\qquad
\eta=0\text{ near }0,
\qquad
\eta=1\text{ near }L.
\]

On the fixed cusp slab `r_0<=r<=r_0+L`, replace the old map by

\[
\boxed{
\widetilde F_n(x,r)=
\left(
(1-\eta(r-r_0))u_n(x)+\eta(r-r_0)x,
\;
 r+(1-\eta(r-r_0))v_n(x)
\right).
}
\tag{36}
\]

At the bottom it agrees with `h_n`. At the top it is exactly the identity. Since the slab has fixed hyperbolic geometry and (35) controls the trace and its tangential derivative, the differential of (36) is `I+O(epsilon_n)` in the orthonormal frame associated with (33). For large `n` it is orientation preserving and

\[
\operatorname{Bilip}(\widetilde F_n)
\le1+C_L\varepsilon_n.
\tag{37}
\]

For

\[
r\ge r_0+L
\]

set

\[
\boxed{\widetilde F_n(x,r)=(x,r).}
\tag{38}
\]

Thus every tail cusp is **exactly isometric above the same fixed normalized Busemann height**. The finitely many head cusps may be normalized in the same way with arbitrary finite interpolation constants; because there are only finitely many, this preserves global bilipschitzity.

The interpolation is performed only after the two Lambert halves have been glued into the physical cusp strip. It therefore need not preserve the artificial split ray. It also lies entirely above `y=2`, so it leaves every finite-cuff trace, pant reflection, and zero-twist gluing relation untouched.

## 6. Why the corrected map really vanishes at Fréchet infinity

This step is essential. Georgescu--Golénia use the ordinary Fréchet filter on the noncompact manifold: `x->infinity` means leaving every relatively compact subset. On an infinite collection of cusped pants there are two independent ways to escape:

1. let the pant index tend to infinity while remaining at bounded cusp depth;
2. keep the pant index fixed and travel arbitrarily deep into one cusp.

Equation (30) controls the first mode. Equation (38) kills the second mode exactly.

Let

\[
E(x)=
\|g_X^{-1}g_+(x)-I\|_{\mathrm{op}}
+
\left|
\frac{d\operatorname{vol}_{g_+}}
     {d\operatorname{vol}_{g_X}}(x)-1
\right|.
\tag{39}
\]

Equations (30) and (37) imply

\[
\sup_{x\in P_n}E(x)\le C\varepsilon_n,
\qquad
\varepsilon_n\to0,
\tag{40}
\]

for all sufficiently large `n`, after the cusp interpolation. Moreover, for each fixed pant the support of `E` in its cusp is bounded in Busemann height by (38).

Given `epsilon>0`, choose `N` so large that

\[
C\varepsilon_n<\epsilon
\qquad(n>N).
\]

For each of the finitely many pants `P_1,...,P_N`, truncate its cusp above the height where (38) starts. The union of these truncated pieces and their finite cuffs is contained in a compact subset `K_epsilon` of the flute. Outside `K_epsilon` there are only two possibilities:

- the point lies deeper in one of those first `N` cusps, where `E=0`;
- or it lies in a pant with index `n>N`, where `E<epsilon` by (40).

Hence

\[
\boxed{E(x)\longrightarrow0\qquad(x\to\infty\text{ in the Fréchet sense}).}
\tag{41}
\]

This is the missing properness argument. Merely knowing `K_n->1` along the pants exhaustion would not imply (41), because a fixed cusp is itself a noncompact escape direction.

## 7. Compact relative resolvent and equal essential spectra

The corrected map is globally bilipschitz. Away from the piecewise-smooth seams, cuffs, and fixed interpolation boundaries, its pullback metric is smooth; across those measure-zero loci it is locally bounded measurable and uniformly positive. Equation (41) gives exactly the asymptotic coefficient condition audited in PF-123, including the volume-density convergence.

Therefore Georgescu--Golénia Theorem 5.3 and Proposition 5.4 apply to the two complete Riemannian structures on the common `C^1` manifold. The first relative resolvent is compact as in (6), and the essential spectra agree as in (7).

The result should be read as

\[
\boxed{
\text{exact prime flute}
\quad\sim_{\text{compact resolvent}}\quad
\text{exact all-composite shift clone}.
}
\tag{42}
\]

This does not mean either Laplacian has compact resolvent. It means only that the transported **difference** of the first resolvents is compact.

## 8. Prior-art and novelty audit

None of the general ingredients is claimed as new. Fermi coordinates around a geodesic, bounded interpolation on a fixed cusp slab, doubling pants, and zero-twist gluing are standard hyperbolic-surface techniques.

The closest coarse comparison remains Yair Minsky, *Bounded geometry for Kleinian groups*, Invent. Math. 146 (2001), 143--192, DOI `10.1007/s002220100163`. Lemmas 8.2--8.3 compare hyperbolic pants/right-angled hexagons whose corresponding boundary lengths differ by a bounded additive amount, including cusp limits. They do not provide the present `K_n->1` conclusion for unbounded cuffs, the prescribed split trace, or the exact left/right compatibility (27).

Dragomir Saric, *Fenchel-Nielsen coordinates for asymptotically conformal deformations*, Ann. Acad. Sci. Fenn. Math. 41 (2016), 167--176, DOI `10.5186/aasfm.2016.4112`, gives an asymptotically conformal Fenchel--Nielsen characterization under an **upper-bounded geodesic pants decomposition**. That hypothesis is absent here because the distinguished prime-flute cuffs tend to infinity.

The operator implication is not novel. PF-123 pins it to V. Georgescu and S. Golénia, *Compact perturbations and stability of the essential spectrum of singular differential operators*, J. Operator Theory 59 (2008), 115--155. Their `B_0` condition is explicitly a vanishing-at-infinity condition for the Fréchet filter, which is why the cusp normalization in Sections 5--6 is logically necessary.

Directed prior-art searches around asymptotic metric equivalence, bilipschitz comparisons of cusped pants with unbounded cuffs, and compact perturbations on singular/infinite-type manifolds found no theorem that supplies the exact project-specific split compatibility or the corrected global map automatically. The durable Mathia content is narrow:

\[
\boxed{
\text{Fermi split gauge}
\Longrightarrow
\text{exact left/right trace match}
\Longrightarrow
K_n\to1
\Longrightarrow
\text{deep-cusp isometric normalization}
\Longrightarrow
\text{Fréchet metric convergence}
\Longrightarrow
\text{compact relative resolvent}.}
\tag{43}
\]

This is a decisive negative control for one natural spectral class, not a new general Teichmüller theorem.

## 9. Boundary of the conclusion and falsification core

The result deliberately stops at compact-resolvent equivalence. It does **not** imply:

- trace-class first-resolvent difference; PF-112 gives the opposite generic local result;
- any specific higher Schatten class;
- equality of discrete eigenvalues or embedded eigenvalues;
- wave-operator existence/completeness or equality of scattering matrices;
- equality of resonances;
- trace-class heat differences or a relative determinant;
- equality of Selberg/Ruelle-type objects or primitive-orbit data;
- any statement about the zeros of `zeta`.

The finding has nine direct falsification gates:

1. substitute (9) into the upper-half-plane metric and verify the Fermi metric (10);
2. substitute (9) into the two opposite-boundary equations and recover (11)--(13);
3. verify the fixed-width corner comparison leading to (21)--(23);
4. restore the two PF-119 physical chart scales and check the exact algebraic coincidence (25)--(27);
5. verify that finite-cuff traces depend only on the matched cuff pair and satisfy the zero-twist reflection identity (29);
6. on the fixed horocycle `y=2`, derive the uniform trace estimate (35) from the explicit pant map, with constants independent of extreme split ratios;
7. differentiate the cusp interpolation (36) in the metric (33) and verify the `1+O(epsilon_n)` bound (37), then check that (38) is exactly isometric;
8. use the two modes of escape to prove the Fréchet limit (41), rather than replacing it by a pants-index limit;
9. only after gate 8, apply PF-123's Georgescu--Golénia theorem bridge to obtain (6)--(7).

Failure of gates 1--7 reopens the geometric construction. Failure of gate 8 invalidates the operator application even if all pantwise constants tend to one. Failure of gate 9 would require a correction to PF-123 or to the stated operator theorem. Passing all nine gates establishes only the compact-resolvent/essential-spectrum no-go stated above.

## Consequence

The all-composite control reaches an intrinsic Laplace invariant, not just endpoints, cross-ratios, lengths, collars, or local arc spectra:

\[
\boxed{
\sigma_{\mathrm{ess}}(\Delta_{\mathrm{prime}})
=
\sigma_{\mathrm{ess}}(\Delta_{\mathrm{shift\ clone}}).
}
\]

Accordingly, a prime-specific/RH mechanism in this construction cannot live solely in the essential spectral class of the Laplacian. Any surviving mechanism must use finer data not invariant under compact resolvent perturbation: discrete spectral information, genuinely quantitative operator ideals, scattering/resonance data under stronger hypotheses, or another nonlocal invariant that can distinguish the prime flute from this exact all-composite clone.
