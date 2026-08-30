# PF-125 — the all-composite shift clone has compact relative resolvent

**Status:** `EXACT-DERIVED + LITERATURE-BACKED + NEGATIVE/DECISIVE`. The local hyperbolic-coordinate construction below is project-specific; the final operator implication is established prior art already audited in PF-123. The result closes the accepted `p_n -> p_n+1` relative-operator clue at the level of the essential Laplace spectrum: the exact prime flute and an exact flute built only from composite labels admit a marked global bilipschitz comparison whose metric distortion tends uniformly to `1` at infinity. Consequently their first resolvents differ by a compact operator under the canonical common-manifold identification, and their essential Laplace spectra agree. No trace-class, wave/scattering, resonance, determinant, discrete-spectrum, Selberg/Ruelle, or RH conclusion is claimed.

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
\boxed{
F:X\longrightarrow X_+
}
\tag{2}
\]

which is globally bilipschitz and for which

\[
\boxed{
\operatorname{Bilip}(F|_{P_n})\longrightarrow1.
}
\tag{3}
\]

More quantitatively, the construction below gives, after discarding a finite head,

\[
\operatorname{Bilip}(F|_{P_n})
\le
1+C\max(\delta_n,\delta_{n+1})
\tag{4}
\]

for an absolute tail constant `C`. The exact rate is not needed later.

Transport the clone metric to the prime surface,

\[
g_+:=F^*g_{X_+}.
\]

Then (3) implies, uniformly at infinity,

\[
\boxed{
\|g_+-g_X\|_{g_X}\longrightarrow0,
\qquad
\frac{d\operatorname{vol}_{g_+}}
     {d\operatorname{vol}_{g_X}}
\longrightarrow1.
}
\tag{5}
\]

The transported metric is piecewise smooth and locally bounded measurable across the canonical seam/cuff locus, which is within the coefficient class audited in PF-123. Therefore Georgescu--Golénia's compact-perturbation theorem, as specialized there, gives

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
\tanh H_a(\tau)
=
s\cosh\tau,
\qquad
0\le\tau\le T_a,
\tag{11}
\]

and the outer cusp ray `x=0` gives

\[
\tanh H_a(\tau)
=
\cosh(a)e^{-\tau},
\qquad
\tau\ge T_a.
\tag{12}
\]

The two meet at

\[
\boxed{
T_a=\frac12\log\cosh(2a).
}
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

This nonzero limiting Fermi width is the key point: the only kink in the boundary graph occurs inside a uniformly nondegenerate strip, despite the collapsing Euclidean `sech(a)` scale.

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

Away from a fixed neighborhood of `T_a`, source and target graphs are on the same branch. There the map

\[
(\rho,\tau)
\longmapsto
\left(
\frac{H_{a'}(\tau)}{H_a(\tau)}\,\rho,\,
\tau
\right)
\tag{17}
\]

is uniformly `1+O(delta)` bilipschitz. Indeed, on the finite branch the only parameter is `s=sech(a)` and on the outer branch it is `cosh(a)`; after staying a fixed distance from the corner, the corresponding `atanh` arguments are uniformly bounded away from `1`. Hence

\[
\frac{H_{a'}(\tau)}{H_a(\tau)}
=
1+O(\delta),
\qquad
H_a(\tau)
\partial_\tau
\left(
\frac{H_{a'}(\tau)}{H_a(\tau)}
\right)
=
O(\delta)
\tag{18}
\]

uniformly, including the regions where `H_a(tau)->0`. In the metric (10), (18) gives the claimed distortion.

It remains to pass through the corner where the derivative of `H_a` jumps because the finite cuff meets the outer cusp ray.

Set

\[
r=\tau-T_a.
\]

The two branches recenter exactly as

\[
\tanh H_a(T_a+r)
=
\frac12
\left(
\sqrt{2-s^2}\,e^r
+
\frac{s^2}{\sqrt{2-s^2}}\,e^{-r}
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

For `|r|<=L` with fixed small `L`, these two pieces and their one-sided derivatives vary by `O(s^2 delta)` when `a` is replaced by `a'`, once the corner is translated by `Delta`. In particular, for large `a` the whole corner neighborhood has a uniform lower Fermi width

\[
H_a(T_a+r)\ge h_L>0.
\tag{21}
\]

Choose a smooth cutoff `beta(r)` equal to `1` near `r=0` and supported in `|r|<L`, and a radial cutoff `eta(rho)` which is `0` near `rho=0` and `1` before `rho=h_L/2`. The shear

\[
\boxed{
S(\rho,\tau)
=
\bigl(
\rho,\,
\tau+\Delta\,
\beta(\tau-T_a)\eta(\rho)
\bigr)
}
\tag{22}
\]

fixes the split ray pointwise in `tau`, moves the opposite-boundary corner from `T_a` to `T_{a'}`, and has differential

\[
DS=I+O(\delta)
\tag{23}
\]

uniformly in the metric (10), because the cutoffs live in a fixed-width Fermi region.

After (22), equations (19)--(20) show that the image opposite boundary differs from the target opposite boundary by `O(delta)` in `C^1` on each smooth side and by `O(s^2 delta)` at the aligned corner. A boundary-normal correction supported away from `rho=0` therefore maps it exactly to the target graph with differential `I+O(delta)`. Equivalently, one may triangulate a fixed Fermi neighborhood of the aligned right-angle corner and move the finitely many boundary vertices by `O(delta)`; uniform nondegeneracy from (21) gives the same `1+O(delta)` piecewise-smooth bilipschitz bound.

Blending this corner correction with (17) gives a label-preserving homeomorphism

\[
\boxed{
G_{a,a'}:Q(a)\longrightarrow Q(a')
}
\tag{24}
\]

such that

\[
\operatorname{Bilip}(G_{a,a'})
\le1+C\delta
\tag{25}
\]

and, crucially,

\[
\boxed{
G_{a,a'}(0,\tau)=(0,\tau)
\quad
\text{for every }\tau\ge0.
}
\tag{26}
\]

Equation (26) is the extra boundary control not supplied by PF-121: in the natural Fermi/Busemann coordinate of the artificial split ray, the trace is exactly the identity.

The finite-cuff trace induced by (24) depends only on the matched pair `(a,a')`, because the entire construction of `Q(a)` is one-parameter. Its bilipschitz constant also tends to one. It need not equal the particular PF-121 trace isolated in PF-124; that exact trace was a convenient coherence device, not an intrinsic datum. Reflecting the present half-cuff trace by the same construction as PF-124 produces a full-cuff trace which commutes exactly with the zero-twist orientation reversal.

## 3. The two Lambert maps now agree exactly on the artificial split ray

Return to the physical PF-119 pentagon with finite half-cuffs `a,b`. Put

\[
A=\cosh a,\qquad B=\cosh b.
\]

Its canonical split location and common-perpendicular radius are

\[
t=\frac{A}{A+B},
\qquad
R=\frac1{A+B}.
\tag{27}
\]

For the target `(a',b')`, use `A',B',t',R'`.

On the left Lambert piece, the PF-119 isometry to `Q(a)` is `z->z/t`. Along the physical split ray, a point of height `y` therefore has normalized height `y/t`. Since the Fermi coordinate in (9) satisfies

\[
y_{\rm norm}
=
\operatorname{sech}(a)e^\tau,
\]

the exact trace (26) sends normalized height by the factor

\[
\frac{\operatorname{sech}a'}
     {\operatorname{sech}a}
=
\frac A{A'}.
\]

Restoring the target physical scale gives

\[
\frac{t'}t\frac A{A'}
=
\boxed{
\frac{A+B}{A'+B'}
=
\frac{R'}R.
}
\tag{28}
\]

The right Lambert piece is normalized by `z->(1-z)/(1-t)`. Repeating the same calculation with `b` gives

\[
\frac{1-t'}{1-t}\frac B{B'}
=
\boxed{
\frac{A+B}{A'+B'}
=
\frac{R'}R.
}
\tag{29}
\]

Thus the two independently constructed one-parameter maps agree **pointwise**, not merely asymptotically, on their shared artificial split ray:

\[
\boxed{
t+iy
\longmapsto
t'+i\frac{R'}R\,y.
}
\tag{30}
\]

No factor involving `t^{-1}` or `(1-t)^{-1}` survives. Therefore arbitrarily extreme neighboring prime-gap ratios do not create a hidden split-ray amplification.

Equations (28)--(30) are the exact compatibility identity that the accepted clue was missing.

## 4. From one pentagon to the complete zero-twist flute

Apply (24) to the left and right Lambert pieces of every tail pentagon. Equation (30) glues them to a single pentagon homeomorphism with

\[
\operatorname{Bilip}
\le
1+C\max(|a'-a|,|b'-b|).
\tag{31}
\]

Reflect across the canonical seams to obtain a map of the full one-cusp pant. On each finite half-cuff the induced trace depends only on the matched cuff pair `(a,a')`. If `T_{a,a'}^{\rm new}` denotes that half-cuff trace, define on the full cuff exactly as in PF-124,

\[
\widehat T_{a,a'}^{\rm new}(s)
=
\begin{cases}
T_{a,a'}^{\rm new}(s),&0\le s\le a,\\
2a'-T_{a,a'}^{\rm new}(2a-s),&a\le s\le2a.
\end{cases}
\tag{32}
\]

Then, purely algebraically,

\[
\widehat T_{a,a'}^{\rm new}\circ J_a
=
J_{a'}\circ
\widehat T_{a,a'}^{\rm new},
\tag{33}
\]

where `J_a(s)=-s mod 2a` is the canonical zero-twist gluing involution. Hence adjacent pants induce identical quotient maps on every shared cuff. The exact PF-124 formula for its earlier trace is not required; only neighbor-independence and the reflection rule are, and both hold here.

For the exact prime/shift-clone sequence, (1) and (31) imply

\[
K_n:=
\operatorname{Bilip}(P_n\to P_n^+)
\longrightarrow1.
\tag{34}
\]

A finite initial collection of pants can be matched by any marked bilipschitz maps agreeing with the first tail cuff trace. Gluing the finite head and the tail gives the global map (2). Since only finitely many head constants are involved,

\[
\sup_nK_n<\infty,
\]

so `F` is globally bilipschitz, while (34) gives asymptotic bilipschitzity.

## 5. Compact relative resolvent and equal essential spectra

On a pant where `F` is `K_n`-bilipschitz, the eigenvalues of the transported metric endomorphism `g_X^{-1}g_+` lie between powers of `K_n` tending to `1`. Thus (34) gives the first limit in (5) uniformly outside finite pant unions. In dimension two the volume-density ratio is the square root of the determinant of that endomorphism, so it also tends uniformly to `1`.

Across reflected seams and glued cuffs, the map is continuous and piecewise smooth. The derivative may jump on the one-dimensional seam/cuff set, but the transported quadratic form is locally bounded measurable and uniformly positive. PF-123 audited Georgescu--Golénia precisely in this coefficient category.

Therefore all hypotheses of PF-123 are now realized rather than conditional, and (6)--(7) follow.

This resolves the accepted clone-operator clue at the compact-resolvent level:

\[
\boxed{
\text{exact prime flute}
\quad\sim_{\text{compact resolvent}}\quad
\text{exact all-composite shift clone}.
}
\tag{35}
\]

The notation in (35) means compact difference of the transported first resolvents, not equality of operators and not that either Laplacian itself has compact resolvent.

## 6. Prior-art and novelty audit

None of the general geometric ingredients is claimed as new. Fermi coordinates around a geodesic, small bilipschitz extensions across a uniformly thick region, doubling pants, and zero-twist gluing are standard hyperbolic-surface techniques.

The closest coarse comparison located is Yair Minsky, *Bounded geometry for Kleinian groups*, Invent. Math. 146 (2001), 143--192, DOI `10.1007/s002220100163`. Lemmas 8.2--8.3 compare hyperbolic pants/right-angled hexagons whose corresponding boundary lengths differ by a bounded additive amount, including degenerate cusp limits. They provide a uniform bilipschitz constant on the appropriate non-collar part, but the stated theorem does not provide the present `K_n->1` conclusion for unbounded cuffs, the prescribed artificial-split trace (26), or the exact two-Lambert compatibility (30).

Dragomir Saric, *Fenchel-Nielsen coordinates for asymptotically conformal deformations*, Ann. Acad. Sci. Fenn. Math. 41 (2016), 167--176, DOI `10.5186/aasfm.2016.4112`, gives an asymptotically conformal Fenchel--Nielsen characterization under an **upper-bounded geodesic pants decomposition**. That hypothesis is absent here: the distinguished prime-flute cuffs tend to infinity. The same hypothesis mismatch was already part of the accepted clue's audit.

The operator implication is not novel. PF-123 pins it to Georgescu--Golénia, *Compact perturbations and stability of the essential spectrum of singular differential operators*, J. Operator Theory 59 (2008), 115--155.

Directed searches for bilipschitz comparisons of one-cusp pants with unbounded cuffs, prescribed Lambert-quadrilateral boundary traces, and asymptotic equivalence of the exact cotangent prime flute to the `p_n+1` composite clone found no statement containing the project-specific compatibility identity (30) or the resulting essential-spectrum no-go. The durable Mathia content is therefore narrow:

\[
\boxed{
\text{Fermi split gauge}
\Longrightarrow
\text{exact left/right trace match}
\Longrightarrow
K_n\to1
\Longrightarrow
\text{compact relative resolvent}.
}
\tag{36}
\]

This is a decisive negative control for one natural spectral class, not a claim of a new general Teichmuller theorem.

## 7. Boundary of the conclusion and falsification core

The result deliberately stops at compact-resolvent equivalence. It does **not** imply:

- trace-class first-resolvent difference; PF-112 gives the opposite generic local result;
- any specific higher Schatten class;
- equality of discrete eigenvalues or embedded eigenvalues;
- wave-operator existence/completeness or equality of scattering matrices;
- equality of resonances;
- trace-class heat differences or a relative determinant;
- equality of Selberg/Ruelle-type objects or primitive-orbit data;
- any statement about the zeros of `zeta`.

The finding has seven direct falsification gates:

1. substitute (9) into the upper-half-plane metric and verify the Fermi metric (10);
2. substitute (9) into the two opposite-boundary equations and recover (11)--(13);
3. check the recentered corner formulas (19)--(20), the positive width limit (15), and the corner displacement bound (16);
4. verify that the shear (22) fixes `rho=0`, aligns the unique boundary kink, and has `DS=I+O(delta)` in a fixed-width region;
5. verify that the away-from-corner radial map (17) and the aligned-corner boundary correction have uniform `1+O(delta)` distortion, including `H_a->0`;
6. restore the two PF-119 physical chart scales and check the exact algebraic coincidence (28)--(30);
7. only after the global zero-twist gluing, apply PF-123's already-audited metric/density hypotheses to obtain (6)--(7).

Failure of gates 1--6 reopens the geometric clue. Failure of gate 7 would require a correction to PF-123 or a mismatch with Georgescu--Golénia's hypotheses. Passing all seven gates establishes only the compact-resolvent/essential-spectrum no-go stated above.

## Consequence

The all-composite control now reaches an intrinsic Laplace invariant, not just endpoints, cross-ratios, lengths, collars, or local arc spectra:

\[
\boxed{
\sigma_{\mathrm{ess}}(\Delta_{\mathrm{prime}})
=
\sigma_{\mathrm{ess}}(\Delta_{\mathrm{shift\ clone}}).
}
\]

Accordingly, a prime-specific/RH mechanism in this construction cannot live solely in the essential spectral class of the Laplacian. Any surviving mechanism must use finer data not invariant under compact resolvent perturbation: discrete spectral information, genuinely quantitative operator ideals, scattering/resonance data under stronger hypotheses, or another nonlocal invariant that can distinguish the prime flute from this exact all-composite clone.
