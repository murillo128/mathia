# PF-139 — full pre-cusp split mismatch has a summable two-sided extension

**Status:** `EXACT-DERIVED + NEGATIVE/BOUNDARY`. PF-136 constructs a summable strong-`L^1` correction for the long pre-first-corner part of the left/right PF-121 split-ray mismatch, while PF-135 shows that the corridor between unequal Lambert corner heights has only a square-root aspect penalty and that this penalty is summable against the surviving scalar mode. PF-137--PF-138 then move the wave-operator obstruction away from fictitious chart narrowing and onto true Margulis-thin geometry plus global assembly. The present finding closes the remaining **two-dimensional split-ray extension** below the canonical standard cusp horocycle. By distributing the exact left/right trace correction over the available Fermi width on both Lambert halves, one obtains corrections that preserve every finite-cuff and outer-cusp boundary trace, make the two Lambert maps agree pointwise on their artificial split ray up to `y=1`, have tail bilipschitz constants tending to `1`, and have summable unweighted strong-`L^1` metric defect. This does not yet match the resulting `y=1` horocycle trace to the PF-129 cusp synchronization map and does not prove the inverse-unit-ball weighted criterion, wave operators, Schatten membership, scattering equivalence, determinants, or any RH statement.

## Claim

Use the exact PF-125/PF-131 Fermi description of the two Lambert halves in the `n`th one-cusp pentagon. Write

\[
A_n:=\cosh a_n,
\qquad
T_n:=\frac12\log\cosh(2a_n),
\tag{1}
\]

and let

\[
H_n(\tau):=H_{a_n}(\tau),
\qquad
H_{n+1}(\tau):=H_{a_{n+1}}(\tau)
\tag{2}
\]

be the two source Fermi half-widths about the common artificial split ray. In physical coordinates the split ray is

\[
y=R_n e^\tau,
\qquad
R_n=\frac1{A_n+A_{n+1}},
\tag{3}
\]

so the standard horocycle `y=1` occurs at

\[
\boxed{
T_n^{\rm cusp}
:=\log(A_n+A_{n+1}).
}
\tag{4}
\]

Let

\[
\Phi_n(\tau),\qquad \Phi_{n+1}(\tau)
\]

be the exact PF-121 target Busemann traces of the two independently mapped Lambert halves and put

\[
D_n(\tau):=\Phi_n(\tau)-\Phi_{n+1}(\tau).
\tag{5}
\]

Then the complete pre-cusp trace budget is summable:

\[
\boxed{
\sum_n
\int_0^{T_n^{\rm cusp}}
\left(|D_n(\tau)|+|D_n'(\tau)|\right)d\tau
<\infty.
}
\tag{6}
\]

After discarding a finite head, there are piecewise-smooth self-corrections of the two Lambert target halves, supported in a fixed small Fermi neighborhood of their common split ray and equal to the identity near every other boundary side, such that:

1. the corrected left and right PF-121 maps induce **exactly the same** split-ray trace for every `0<=tau<=T_n^{cusp}`;
2. the corrections leave the PF-124 finite-cuff traces unchanged and also leave both physical outer cusp rays unchanged;
3. their bilipschitz constants satisfy
   \[
   \boxed{K_n\longrightarrow1;}
   \tag{7}
   \]
4. if `C_n` denotes the union of the two corrections on the truncated Lambert pair, then for the corresponding zeroth-order metric/density deviation,
   \[
   \boxed{
   \sum_n
   \int_{C_n}\delta_{g,C_n^*g}\,d\mu_g
   <\infty.
   }
   \tag{8}
   \]

The finitely many head pieces can be corrected with arbitrary finite bilipschitz cost. Thus the left/right split mismatch is no longer an obstruction to constructing a **single lower-pentagon map with summable strong-`L^1` correction** all the way from the finite split endpoint to the standard cusp entry.

Equation (8) is deliberately unweighted. The correction may still intersect true Margulis collars, where the Güneysu--Thalmaier inverse-unit-ball factor is not controlled by (8). PF-138 supplies a finite local model budget for all such closed thin cores, but compatibility of those optimized collar maps with one global comparison remains separate.

## 1. The full trace mass up to the standard cusp is summable

PF-136 already proves

\[
\sum_n
\int_0^{T_n^*}
\left(|D_n|+|D_n'|\right)d\tau<\infty,
\qquad
T_n^*:=\min(T_n,T_{n+1}).
\tag{9}
\]

For sufficiently large `n`, every `tau>=T_n^*` is also larger than the fixed PF-121 splice height. PF-133 therefore gives the exact tail decomposition

\[
D_n(\tau)=c_n+E_n(\tau),
\qquad
c_n:=\beta_n-\beta_{n+1},
\tag{10}
\]

with

\[
|E_n(\tau)|+|D_n'(\tau)|
\le C|c_n|e^{-2\tau}.
\tag{11}
\]

Hence

\[
\int_{T_n^*}^{T_n^{\rm cusp}}
\left(|D_n|+|D_n'|\right)d\tau
\le
|c_n|T_n^{\rm cusp}+C|c_n|.
\tag{12}
\]

PF-134 proves both

\[
T_n^{\rm cusp}\le C+\log p_n
\tag{13}
\]

and

\[
\sum_n(1+\log p_n)|c_n|<\infty.
\tag{14}
\]

Combining (9), (12), and (14) proves (6). This is stronger than the full-ray trace seminorm of PF-132 for the present purpose: it controls the actual inhomogeneous `L^1` trace cost over the entire **finite but growing** interval that must be traversed before the canonical standard cusp strip begins.

## 2. A two-sided Fermi extension uses the sum of the available widths

The correction problem is local near the artificial split ray. On either Lambert half the Fermi metric is

\[
\boxed{
g=d\rho^2+\cosh^2\rho\,d\tau^2.}
\tag{15}
\]

Choose once and for all a small `h_0>0`. For a half-width `H(\tau)`, let `m(\tau)` be a piecewise-smooth effective support width satisfying

\[
\boxed{
 c\min\{H(\tau),h_0\}
\le m(\tau)
\le C\min\{H(\tau),h_0\},
}
\tag{16}
\]

with support contained in `0<=rho<=H/2`. The exact PF-125 branch formulas imply that whenever `H<h_0`,

\[
|H'(\tau)|\le C H(\tau),
\tag{17}
\]

while `m` can be chosen constant when `H>=h_0`. Thus

\[
\boxed{|m'(\tau)|\le C m(\tau)}
\tag{18}
\]

away from finitely many harmless smoothing intervals around the Lambert corners.

Apply this construction to the two target halves after the independent PF-121 maps and write their effective widths, pulled back to the common source parameter `tau`, as

\[
m_L(\tau),\qquad m_R(\tau),
\qquad M(\tau):=m_L(\tau)+m_R(\tau).
\tag{19}
\]

The PF-121 maps are uniformly bilipschitz on the tail, so source and target effective widths are comparable by absolute constants; all estimates below can therefore be checked with the source widths `H_n,H_{n+1}`.

Choose a common split trace `Psi_n` between `Phi_n` and `Phi_{n+1}` so that the two target boundary displacements are

\[
\boxed{
 s_L(\tau)
=-\frac{m_L(\tau)}{M(\tau)}D_n(\tau),
\qquad
 s_R(\tau)
= \frac{m_R(\tau)}{M(\tau)}D_n(\tau).
}
\tag{20}
\]

Then

\[
\Phi_n+s_L
=\Phi_{n+1}+s_R
=:\Psi_n
\tag{21}
\]

pointwise. Since the trace derivatives are uniformly bounded above and below on a sufficiently far tail, equations (18)--(20) also give

\[
\boxed{
|s_j'|
\le C\left(|D_n'|+|D_n|\right),
\qquad
\frac{|s_j|}{m_j}
\le\frac{|D_n|}{M}.
}
\tag{22}
\]

If one wants the correction written intrinsically as a self-map of the target half rather than as a displacement in the source parameter, define the boundary homeomorphism by

\[
B_j(\Phi_j(\tau))=\Psi_n(\tau).
\tag{23}
\]

Uniform bounds on `Phi_j'` transfer (22) to the target Busemann coordinate without changing its scale.

Let `chi` be a fixed cutoff with `chi(0)=1` and `chi=0` for argument at least `1`. On the target half-strip extend `B_j` by the Fermi interpolation

\[
(\rho,\sigma)
\longmapsto
\left(
\rho,
\sigma+
\chi\!\left(\frac{\rho}{m_j}\right)b_j(\sigma)
\right),
\tag{24}
\]

where `b_j` is the displacement corresponding to (23). For the tail, Section 4 below shows `|b_j|/m_j->0`; hence (24) remains inside the variable-width half-strip. If desired, a boundary-normal correction of the same order can be inserted in the cutoff zone; it is supported where `rho=O(m_j)` and does not change any estimate below.

In the support of (24), `rho<=h_0`, so `cosh rho` is uniformly bounded. Differentiating gives the standard strip estimate

\[
\delta_j
\le C\left(
|b_j'|+|b_j|+rac{|b_j|}{m_j}
\right).
\tag{25}
\]

The Fermi area of the support is `O(m_j d sigma)`. Therefore

\[
\int\delta_j\,d\mu
\le
C\int
\left(
 m_j|b_j'|+m_j|b_j|+|b_j|
\right)d\sigma.
\tag{26}
\]

Summing the two sides and using (20)--(22),

\[
\boxed{
\int(\delta_L+\delta_R)d\mu
\le
C\int
\left(|D_n|+|D_n'|\right)d\tau.
}
\tag{27}
\]

Equation (6) now proves (8). The important cancellation is two-sided:

\[
\boxed{
\text{transverse derivative }
\frac{|D_n|}{m_L+m_R}
\times
\text{available area }(m_L+m_R)
\Longrightarrow
\text{cost }|D_n|.
}
\tag{28}
\]

No individual large-cuff factor survives in the unweighted metric mass.

## 3. The correction preserves every genuine pant boundary trace

The support widths in (16) are strictly smaller than the distance from the split ray to the opposite Lambert boundary. Hence (24) is the identity in a neighborhood of that opposite boundary.

Before the Lambert corner, the opposite boundary is the finite-cuff arc. Therefore the PF-124 finite-cuff trace `T_{a,a^+}` is unchanged exactly. After the corner, the opposite boundary is the physical outer cusp ray, which is likewise unchanged exactly. The correction only changes the artificial internal split parametrization.

Consequently the two corrected Lambert maps glue into one map of the truncated pentagon while retaining all external traces supplied by the independent PF-121 maps. Reflecting the pentagon across its canonical seams still gives the same PF-124 full-cuff map, so the exact zero-twist commuting relation survives unchanged.

This is why the construction is stronger than merely replacing `D_n` by an abstract Sobolev extension: it respects the actual boundaries that later have to glue through the infinite tight-flute chain.

## 4. Extreme neighboring gap ratios do not destroy tail near-isometry

The integral estimate (27) does not by itself guarantee that the correction remains uniformly bilipschitz; pointwise control of `|D_n|/M` is also required. The existing findings provide exactly the needed regional bounds.

### Before the first Lambert corner

PF-136 proves the width-relative estimate for the wider finite-branch half. In its notation the exact trace reparametrization satisfies

\[
\left\|\frac{q_n^{\rm tr}}{H_{*,n}}\right\|_\infty
+\|(q_n^{\rm tr})'\|_\infty
\longrightarrow0
\tag{29}
\]

up to one fixed unit before the first corner, and the trace maps are uniformly bi-Lipschitz. Thus

\[
\frac{|D_n|}{M}\longrightarrow0
\tag{30}
\]

there. In the remaining fixed corner neighborhood at least one Fermi width has an absolute positive lower bound by PF-125, while PF-132 gives `||D_n||_infty->0`.

### Between unequal Lambert corner heights

Assume `T_n<T_{n+1}`; the other ordering is symmetric. PF-135 proves

\[
H_n(\tau)+H_{n+1}(\tau)
\ge
c\kappa_n^{-1},
\qquad
\kappa_n
:=
\left(
\frac{\max(A_n,A_{n+1})}
     {\min(A_n,A_{n+1})}
\right)^{1/2},
\tag{31}
\]

through the middle corridor and

\[
\sum_n\kappa_n|c_n|<\infty.
\tag{32}
\]

For these large Busemann heights PF-133 gives

\[
|D_n(\tau)|\le C|c_n|.
\tag{33}
\]

After replacing `H` by the capped effective widths in (16), either one side already has width at least `h_0` or (31) remains valid up to an absolute factor. Hence

\[
\frac{|D_n|}{M}
\le C(1+\kappa_n)|c_n|
\longrightarrow0.
\tag{34}
\]

This is the point at which PF-135's polynomial-moment estimate is genuinely used: extreme neighboring prime gaps can make the two Lambert corner heights very different, but the resulting square-root aspect loss is still summable against the exact adjacent scalar mode.

### After the second corner and before `y=1`

Once both halves are on their cusp branches,

\[
\tanh H_n=A_n e^{-\tau},
\qquad
\tanh H_{n+1}=A_{n+1}e^{-\tau}.
\tag{35}
\]

For `tau<=T_n^{cusp}=log(A_n+A_{n+1})`,

\[
\tanh H_n+\tanh H_{n+1}
=(A_n+A_{n+1})e^{-\tau}\ge1.
\tag{36}
\]

Thus at least one half has Fermi width at least the absolute constant `artanh(1/2)`. The effective total width `M` is therefore bounded below by a positive constant, while PF-132/PF-133 give `sup|D_n|->0` and `sup|D_n'|->0`. Equations (22), (30), (34), and (36) prove (7).

So the correction remains near-isometric across all three difficult regimes:

```text
long narrow pre-corner sector:
    PF-136 width-relative cancellation

unequal-corner middle corridor:
    PF-135 square-root aspect budget

after both corners up to y=1:
    combined cusp width has an absolute floor
```

No factor depending on an extreme split ratio survives as a uniform tail obstruction.

## 5. What PF-139 closes and what remains open

PF-130 showed that the two **independent** one-parameter Lambert maps have a summable strong-`L^1` metric budget. PF-131--PF-135 showed that their complete split trace contains only summable adjacent modes, and PF-136 constructed a two-dimensional correction on the most visibly narrow pre-corner part. What remained logically open was whether the correction could be carried through unequal corner heights and all the way to the canonical cusp entry without losing either pointwise near-isometry or the strong-`L^1` budget.

PF-139 gives a positive answer:

\[
\boxed{
\text{independent Lambert maps}
+
\text{exact split trace}
\Longrightarrow
\text{one split-coherent lower-pentagon map}
\text{ with summable strong-}L^1\text{ correction}.
}
\tag{37}
\]

The remaining wave-operator gate is narrower but still real. At `y=1`, PF-122/PF-129 provide the preferred cusp-strip trace and then an exactly isometric deep cusp. PF-139 proves only that the two lower Lambert halves agree with **each other** at that interface. It does not prove that their common full horocycle trace equals, or is summably close in the required two-dimensional sense to, the PF-129 boundary map. Separately, PF-138 proves that all closed Margulis-thin cores have a summable family of optimized PF-128 collar model costs, but it does not make those collar maps compatible with the same global marking.

Thus the accepted wave clue is reduced to two genuine assembly questions:

1. **horocycle handoff:** reconcile the split-coherent lower-pentagon map with the PF-129 cusp normalization with summable weighted cost;
2. **closed-thin handoff:** realize the PF-128 collar budgets for all PF-138 short cores inside that same global comparison.

Only after both handoffs are realized in one smooth complete quasi-isometric identification can Güneysu--Thalmaier be invoked.

## 6. Prior-art and novelty audit

No novelty is claimed for Fermi coordinates, cutoff interpolation in a strip, bilipschitz extension of small boundary displacements, or the general theory of quasiconformal/Fenchel--Nielsen deformations. Directed checks recover the standard infinite-type Fenchel--Nielsen literature of Alessandrini--Liu--Papadopoulos--Su and Šarić, general Sobolev/quasiconformal boundary-extension machinery, and the Lambert-quadrilateral comparison literature already anchored in this line. Those results do not directly supply the present estimate because the prime flute has unbounded distinguished cuffs, zero systole, arbitrarily extreme neighboring cuff aspect, and a growing pre-cusp interval; moreover the exact correction must preserve the project-specific PF-124 finite-cuff trace.

The durable Mathia content is therefore narrow and compositional rather than a new general extension theorem:

\[
\boxed{
\text{PF-136 pre-corner control}
+
\text{PF-133/PF-134 full growing-height trace budget}
+
\text{PF-135 combined-width aspect control}
\Longrightarrow
\text{summable two-sided 2D split extension up to }y=1.
}
\tag{38}
\]

This is adverse evidence for prime specificity: another apparently plausible place for the exact prime geometry to amplify the all-composite shift control instead remains summably tame. It does not establish a new scattering theorem and does not connect any spectral datum to RH.

## 7. Audit / falsification core

A later adversary can check PF-139 through the following finite chain:

1. import PF-125's exact Fermi widths and verify the physical identity `T_n^{cusp}=log(A_n+A_{n+1})`;
2. combine PF-136's integral through `T_n^*`, PF-133's exact tail `D_n=c_n+O(c_n e^{-2tau})`, and PF-134's `sum T_n^{cusp}|c_n|<infinity` to prove (6);
3. choose capped support widths satisfying (16)--(18) and verify the split displacements (20) make the two traces agree exactly;
4. differentiate the cutoff extension (24) in the Fermi metric and recover the integrated estimate (27), checking that the support never reaches the finite-cuff or outer-cusp boundaries;
5. use PF-136 before the first corner, PF-135 between corner heights, and (35)--(36) after the second corner to prove `|D_n|/M->0` uniformly and hence (7);
6. reflect through the pentagon seams and verify that PF-124's finite-cuff zero-twist identity is untouched;
7. preserve the evidence boundary: do **not** infer a summable horocycle handoff, the Güneysu--Thalmaier weighted integral, complete wave operators, a Schatten class, scattering/resonance equality, or any RH conclusion from (8).

A refutation would need to break the full trace summability (6), the effective-width lower bounds used in Section 4, or the explicit two-sided strip estimate (27). A failure of the later cusp/collar assembly would not refute PF-139; it would realize exactly the remaining gate that this finding leaves open.