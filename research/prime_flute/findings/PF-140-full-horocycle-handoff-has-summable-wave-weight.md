# PF-140 — the full standard-horocycle handoff has summable wave weight

**Status:** `EXACT-DERIVED + LITERATURE-BACKED + NEGATIVE/BOUNDARY`. PF-139 constructs a single split-coherent lower-pentagon comparison with summable strong-`L^1` metric defect all the way to the canonical standard cusp entry `y=1`, but deliberately leaves its full horocycle trace unmatched to the optimized cusp comparison of PF-129. The present finding closes that external handoff. The exact PF-121 Lambert map is exponentially closer, on the whole standard-cusp region, to a hyperbolic dilation than its coarse `1+O(delta)` estimate suggests. After restoring the physical pant charts, the only leading horocycle mismatch is precisely the adjacent first-difference mode already shown summable in PF-119/PF-122; the PF-139 split correction adds only its own summable scalar tail mode. Consequently the actual PF-139 trace on `y=1` is summably close to the identity in a piecewise `W^{1,infinity}` trace norm and can be cut off to exact identity through one fixed Busemann-height slab with finite total Güneysu--Thalmaier inverse-unit-ball weighted cost. This removes the **full standard-horocycle/cusp handoff** from the wave-operator obstruction. It does not yet fit the optimized PF-128 collar maps for every PF-138 closed thin core into the same global marking, and therefore does not prove complete wave operators, scattering equivalence, Schatten membership, determinants, resonance equality, or any RH statement.

## Claim

For the `n`th exact prime/shift-clone one-cusp pant, put

\[
a_n=\frac{\ell_n}{2},\qquad a_n^+=a_n+\delta_n,
\tag{1}
\]

and write

\[
\epsilon_n:=\log\frac{\cosh a_n^+}{\cosh a_n},
\qquad
d_n:=|\epsilon_n-\epsilon_{n+1}|.
\tag{2}
\]

PF-119/PF-122 give

\[
\boxed{\sum_n d_n<\infty.}
\tag{3}
\]

Let `Gamma_n` be the trace on the source horocycle `y=1` of the **PF-139 corrected lower-pentagon map**, after the left/right Lambert halves have been made exactly split-coherent. In the target standard cusp coordinates

\[
r=\log y,
\qquad 0\le x\le1,
\tag{4}
\]

write, away from the harmless piecewise-smooth split point,

\[
\Gamma_n(x)=(U_n(x),V_n(x)).
\tag{5}
\]

After discarding a finite head, there is a summable nonnegative sequence `eta_n` such that

\[
\boxed{
\begin{aligned}
&\|U_n-\operatorname{id}\|_{L^\infty(0,1)}
+\operatorname*{ess\,sup}_{x\in(0,1)}|U_n'(x)-1|\\
&\qquad
+\|V_n\|_{L^\infty(0,1)}
+\operatorname*{ess\,sup}_{x\in(0,1)}|V_n'(x)|
\le C\eta_n,
\qquad
\sum_n\eta_n<\infty.
\end{aligned}
}
\tag{6}
\]

One explicit admissible budget is

\[
\boxed{
\eta_n
:=
 d_n
 +\delta_n e^{-2a_n}
 +\delta_{n+1}e^{-2a_{n+1}}
 +|c_n|,
}
\tag{7}
\]

where `c_n` is PF-139/PF-134's centered Lambert split-tail scalar mode. PF-134 gives

\[
\sum_n(1+\log p_n)|c_n|<\infty,
\tag{8}
\]

while PF-114 gives `sum e^{-2a_n}<infinity` and PF-107 gives `delta_n->0`, so (7) is indeed in `ell^1`.

Fix one absolute `L>0` and a smooth cutoff `chi:[0,L]->[0,1]` equal to `0` near `0` and `1` near `L`. On the standard cusp slab define

\[
\boxed{
F_n(x,r)
=
\left(
(1-\chi(r))U_n(x)+\chi(r)x,
\;
r+(1-\chi(r))V_n(x)
\right).
}
\tag{9}
\]

After the routine local smoothing of the split kink, preserving the same first-derivative scale, the tail maps are diffeomorphisms, agree exactly with `Gamma_n` at the lower boundary, preserve the two outer cusp rays, and are the identity near `r=L`. Extend them by the identity for `r>= L`. If `h_n=F_n^*g` on the standard cusp strip, then

\[
\boxed{
\int_{\{0\le r\le L\}}
\mu_g(B_g(z,1))^{-1}
\delta_{g,h_n}(z)\,d\mu_g(z)
\le C_L\eta_n.
}
\tag{10}
\]

Consequently

\[
\boxed{
\sum_n
\int_{\text{handoff slab }n}
\mu_g(B_g(z,1))^{-1}
\delta_{g,h_n}(z)\,d\mu_g(z)
<\infty.
}
\tag{11}
\]

Thus PF-139 can be handed directly to an **exactly isometric deep cusp** with finite total wave weight. The particular PF-129 boundary trace is no longer a compatibility gate: PF-140 cuts the actual PF-139 trace itself to the identity through a fixed slab. The remaining global wave-operator problem is the simultaneous insertion of the PF-128 optimized collar comparisons for the complete PF-138 family of true closed Margulis-thin cores, together with compatible smoothing at their interfaces.

## 1. The PF-121 map has an exponentially small defect from a cusp dilation on `y>=1`

Use PF-131's real Möbius normalization of the PF-119 Lambert quadrilateral,

\[
M_a(z)=e^a\frac{z-\tanh a}{z+\tanh a}.
\tag{12}
\]

Write

\[
M_a(z)=e^{u+i\theta},
\qquad
v:=a-u.
\tag{13}
\]

For every point `z=x+iY` of the normalized standard cusp strip

\[
0\le x\le1,
\qquad Y\ge1,
\tag{14}
\]

a direct modulus calculation gives

\[
\boxed{
 e^{2(u-a)}
 =
 \frac{(x-\tanh a)^2+Y^2}
      {(x+\tanh a)^2+Y^2}.
}
\tag{15}
\]

The numerator is at least `1`, the denominator is at most `5` times the numerator under (14), and the ratio is at most `1`. Hence

\[
\boxed{
0\le v\le C_0:=\tfrac12\log5.
}
\tag{16}
\]

For sufficiently large `a`, the whole region (14) therefore lies on PF-121's exact tail branch. Put `a'=a+delta`,

\[
c:=\frac{\cosh a'}{\cosh a},
\qquad
f(u):=\operatorname{arcosh}(c\cosh u).
\tag{17}
\]

PF-121 proves

\[
f(a)=a'
\tag{18}
\]

and the exact derivative identity

\[
1-f'(u)^2
=
\frac{c^2-1}{c^2\cosh^2u-1}.
\tag{19}
\]

On `a-C_0<=u<=a`, bounded small `delta` gives

\[
\boxed{
|f'(u)-1|
\le C\delta e^{-2a}.
}
\tag{20}
\]

Define the target cusp-depth coordinate

\[
v':=a'-f(a-v).
\tag{21}
\]

Since `v'(0)=0` and `dv'/dv=f'(a-v)`, equation (20) yields the sharper anchored estimate

\[
\boxed{
|v'-v|
\le C\delta e^{-2a}v,
\qquad
\left|\frac{dv'}{dv}-1\right|
\le C\delta e^{-2a}.
}
\tag{22}
\]

This anchoring at the ideal vertex is important: no fixed Busemann displacement survives as `v->0`.

The inverse Möbius chart is explicit. With `q=e^{-v+i\theta}`,

\[
\boxed{
M_a^{-1}(e^{a-v+i\theta})
=
\tanh a\,\frac{1+q}{1-q}.
}
\tag{23}
\]

The target has the same formula with `a',v'`. If instead one keeps `(v,theta)` fixed, (23) changes only by the hyperbolic dilation

\[
H_{a,a'}(z)=\kappa_{a,a'}z,
\qquad
\kappa_{a,a'}:=\frac{\tanh a'}{\tanh a}.
\tag{24}
\]

Moreover

\[
\boxed{
|\log\kappa_{a,a'}|
\le C\delta e^{-2a}.
}
\tag{25}
\]

Equations (22)--(23), differentiated once, show that on the standard-cusp region the actual PF-121 map differs from this ambient hyperbolic dilation by

\[
\boxed{
q(a,a'):=C\delta e^{-2a}
}
\tag{26}
\]

in the first-derivative hyperbolic scale. There is no hidden amplification at the ideal vertex: because `v'-v=O(qv)`, the apparent pole of `(1-q)^{-1}` in (23) cancels after differentiating the logarithmic fractional-linear expression. Equivalently, in PF-121's parameter-independent `(v,w)` metric the differential is diagonal with entries `f'(a-v),1`, while (23) controls the anchored point displacement.

This is strictly stronger than PF-121's global `1+O(delta)` bilipschitz estimate, but only on the already-standard cusp sector. It does not improve the lower Lambert-body estimate of PF-130.

## 2. Restoring the physical pant leaves only the summable adjacent cusp mode

For one physical pentagon put

\[
A=\cosh a,
\qquad
B=\cosh b,
\qquad
t=\frac{A}{A+B},
\tag{27}
\]

and use primes for the shift-clone target. PF-122's canonical cusp trace has slopes

\[
 m_L=\frac{t'}t,
\qquad
 m_R=\frac{1-t'}{1-t},
\tag{28}
\]

with

\[
\boxed{
|\log m_L|,|\log m_R|
\le
|\epsilon_a-\epsilon_b|.
}
\tag{29}
\]

The left physical Lambert chart is obtained from the normalized one by the dilation `z->z/t`; the right half is its reflected analogue. Restoring physical scale therefore turns the comparison dilation (24) into

\[
 z\longmapsto m_L\kappa_{a,a'}z
\tag{30}
\]

on the left, and into the corresponding dilation about the right cusp ray with factor `m_R\kappa_{b,b'}` on the right.

On the physical source horocycle `y=1`, the PF-122 map is exactly

\[
(x,1)\longmapsto(\phi(x),1),
\tag{31}
\]

where `phi` is its piecewise-affine map with derivatives `m_L,m_R`. Equations (25), (26), and (29) now give, in the standard `(x,r=log y)` trace coordinates,

\[
\boxed{
\|\operatorname{Tr}_{y=1}(F_{\rm PF121})
      - (\phi,0)\|_{W^{1,\infty}_{\rm pw}}
\le
C\left(
 d_n
 +\delta_n e^{-2a_n}
 +\delta_{n+1}e^{-2a_{n+1}}
\right).
}
\tag{32}
\]

Here `W^{1,infinity}_{pw}` means the supremum of the value and first tangential derivative on the two open sides of the split; one point of derivative discontinuity is irrelevant. PF-122 itself gives

\[
\boxed{
\|(\phi,0)-(\operatorname{id},0)\|_{W^{1,\infty}_{\rm pw}}
\le C d_n.
}
\tag{33}
\]

Thus the raw PF-121 full-horocycle trace already has an `ell^1` defect from the identity once the exponentially localized single-Lambert remainder is included.

The summation of that remainder is unconditional from persisted prime-flute evidence. PF-107 gives a bounded tail with `delta_n->0`, while PF-114 gives

\[
\sum_n e^{-2a_n}<\infty.
\tag{34}
\]

Therefore

\[
\boxed{
\sum_n\delta_n e^{-2a_n}<\infty.
}
\tag{35}
\]

No new prime-gap theorem is needed.

## 3. PF-139's split correction preserves the summable horocycle budget

PF-139 changes the two raw PF-121 Lambert maps only in a Fermi neighborhood of their artificial split ray. At the standard cusp entry

\[
\tau=T_n^{\rm cusp}=\log(A_n+A_{n+1}),
\tag{36}
\]

both halves are already on their cusp branches and PF-139 proves that their total available Fermi width is bounded below by an absolute positive constant. Its centered tail decomposition is

\[
D_n(\tau)=c_n+E_n(\tau),
\qquad
|E_n(\tau)|+|D_n'(\tau)|
\le C|c_n|e^{-2\tau}.
\tag{37}
\]

The explicit two-sided correction in PF-139 satisfies, at every height,

\[
|s_j'|
\le C(|D_n'|+|D_n|),
\qquad
\frac{|s_j|}{m_j}
\le\frac{|D_n|}{m_L+m_R}.
\tag{38}
\]

At (36) the denominator in the second estimate has an absolute lower bound. Hence the correction changes the complete `y=1` trace, including its tangential first derivative, by at most

\[
\boxed{C|c_n|.}
\tag{39}
\]

It remains the identity near both physical outer cusp rays, so the endpoint labels in (5) stay fixed. Combining (32), (33), and (39) proves (6) with (7). Equation (8), (3), and (35) prove `sum eta_n<infinity`.

This is the missing compatibility fact: PF-139 did not merely reach `y=1` with finite two-dimensional body cost; its **actual resulting boundary trace** is itself summably close to the canonical standard-cusp gauge.

## 4. A fixed Busemann slab kills the remaining trace with finite total wave weight

The standard width-one cusp metric is

\[
\boxed{
g=dr^2+e^{-2r}dx^2.}
\tag{40}
\]

On the fixed slab `0<=r<=L`, the orthonormal-frame and coordinate norms are uniformly comparable by constants depending only on `L`. From (6), differentiating (9) gives

\[
\boxed{
\|dF_n-I\|_g
+|\operatorname{Jac}_gF_n-1|
\le C_L\eta_n.
}
\tag{41}
\]

For sufficiently large `n`, `eta_n->0`, so (9) is orientation preserving. The finitely many head cusps can be connected to the identity by arbitrary smooth marked maps with finite total cost.

Exactly as in PF-129, every ambient unit ball centered in this fixed-height slab has area bounded below by a constant `c_L>0`, and the slab has uniformly bounded area. The Güneysu--Thalmaier zeroth-order metric deviation is therefore bounded by `C_L eta_n`, proving (10). Summing gives (11).

The piecewise-smooth split trace can be smoothed before applying (9). Its derivative jump is itself `O(eta_n)`, so a monotone smoothing in an arbitrarily small split neighborhood preserves the `C eta_n` first-derivative bound. No second-derivative estimate enters the Güneysu--Thalmaier metric-deviation integral, and the pulled-back metric remains a smooth hyperbolic metric after smoothing.

Above `r=L` the map is exactly the identity. Thus there is no infinite-depth cusp penalty and no need to synchronize a separate asymptotic Busemann shift.

## 5. Consequence for the accepted wave-operator clue

Before PF-140 the accepted wave clue had two explicit external handoffs after PF-139:

```text
PF-139 lower-pentagon map
    -> match its full y=1 trace to the optimized cusp map
    -> insert all optimized short-collar maps
    -> smooth/assemble globally
    -> apply the no-injectivity-radius scattering criterion.
```

The first arrow is now proved with a stronger formulation: the actual PF-139 trace can be sent **directly to exact identity** through a fixed slab with summable weighted cost. The remaining obstruction is therefore confined to the closed Margulis-thin sector and its interfaces. PF-138 identifies every sufficiently short source closed geodesic as a distinguished cuff or a canonical consecutive-block separator; the distinguished cuffs leave the thin spectrum on the tail, while PF-128 supplies a summable local model budget for the canonical short separators.

What is still missing is one common map that realizes those PF-128 collar comparisons while matching the PF-139/PF-140 body-and-cusp traces on every collar boundary. Local model summability does not by itself prove compatible global assembly. Until that final closed-thin interface problem is solved, the Güneysu--Thalmaier theorem cannot be invoked for the complete surface.

Therefore PF-140 is a **negative boundary result** for RH-directed prime-flute research: another natural place where the prime surface might have amplified its exact all-composite shift control instead differentiates the reciprocal-prime mode into an `ell^1` trace defect. If wave equivalence is ultimately proved, it will further show that the absolutely continuous Laplace/scattering class is not a primality selector. PF-140 itself stops before that conclusion.

## 6. Prior art and novelty audit

No novelty is claimed for fixed-slab interpolation in a hyperbolic cusp, for hyperbolic dilations, or for the general scattering theorem. Batu Güneysu and Anton Thalmaier, *Scattering theory without injectivity radius assumptions, and spectral stability for the Ricci flow*, Annales de l'Institut Fourier 70 (2020), 437--456, DOI `10.5802/aif.3316`, provide the general inverse-unit-ball weighted criterion already audited in PF-128/PF-129 and `SOURCES.md` S16. PF-140 does not strengthen that theorem.

Matti Vuorinen and Gendi Wang, *Hyperbolic Lambert quadrilaterals and quasiconformal mappings*, Annales Academiae Scientiarum Fennicae Mathematica 38 (2013), 433--453, DOI `10.5186/aasfm.2013.3845`, study sharp hyperbolic-distance inequalities and quasiconformal images of Lambert quadrilaterals. That is the closest general Lambert-quadrilateral literature already identified by PF-121/PF-130. It does not supply the exact PF-121 tail map, the anchored estimate (22), the prime/shift first-difference cancellation, or the summable full-horocycle handoff.

Directed searches for hyperbolic-cusp boundary interpolation, cusp scattering under metric perturbation, and Lambert-quadrilateral boundary comparison found general cusp scattering/deformation frameworks but no theorem that automatically identifies the PF-139 boundary trace or produces the project-specific `ell^1` estimate (6). Absence of a matching source is not treated as a broad novelty claim. The durable custom content is the finite composition

\[
\boxed{
\text{PF-121 exact tail derivative}
+\text{ ideal-vertex anchoring}
+\text{ PF-122 adjacent first difference}
+\text{ PF-139 centered split correction}
\Longrightarrow
\text{summable full-horocycle wave handoff}.}
\tag{42}
\]

## 7. Audit / falsification core

A later adversary can check PF-140 through the following finite chain:

1. substitute `z=x+iY` into PF-131's exact Möbius map (12) and verify (15)--(16) uniformly for `0<=x<=1`, `Y>=1`;
2. use PF-121's exact derivative identity (19), together with `u>=a-C_0`, to prove (20);
3. anchor at `f(a)=a'` and integrate once to obtain the extra factor `v` in (22);
4. invert the Möbius map as in (23), differentiate the fractional-linear expression once, and verify that the factor `v` in (22) prevents ideal-vertex amplification, yielding the first-derivative cusp estimate (26);
5. restore the physical left/right pant scales and verify that the only leading factors are `m_L,m_R`, whose logarithms are bounded by PF-122's `d_n`, proving (32);
6. use PF-114 and PF-107 to sum the `delta_n e^{-2a_n}` remainder;
7. evaluate PF-139's explicit two-sided correction at `T_n^{cusp}`, use its lower bound on total Fermi width and tail formula (37), and obtain the additional `O(|c_n|)` trace budget;
8. use PF-134 to sum `|c_n|`, giving (6)--(7);
9. differentiate the fixed-slab cutoff (9), use the fixed-height unit-ball lower bound from PF-129, and obtain (10)--(11);
10. **do not** infer complete wave operators until the PF-128 collar comparisons for every PF-138 closed thin core are realized compatibly inside the same smooth global marking.

A refutation would have to break the exact cusp localization (15), the anchored PF-121 estimate (22), the physical chart cancellation leading to (32), PF-139's top-trace estimate (39), or the fixed-slab weighted bound. Failure of the still-open collar/body assembly would not refute PF-140; it is precisely the remaining mechanism excluded from this claim.