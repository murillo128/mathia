# PF-180 — Lambert split synchronization can be made exactly area preserving

**Status:** `EXACT-DERIVED + CLASSICAL-HAMILTONIAN + POSITIVE/BOUNDARY`. PF-179 gives exact area-preserving, degeneration-uniform `1+O(d)` transports for the individual Lambert bodies, but their split-ray traces still depend on the one-parameter body and therefore do not agree automatically when the two halves of one physical pentagon are reassembled. PF-139 previously removed the analogous split mismatch for the non-area-preserving comparison by a two-sided variable-width extension. The area gauge does **not** reopen that obstruction. In the exact area coordinate `x=sinh rho`, a small split-boundary reparametrization can be extended by a compactly supported Hamiltonian flow, hence with Jacobian exactly one, while retaining the same width-relative cancellation that made PF-139 summable. Applied to the PF-179 traces, this produces area-preserving self-corrections of the two target Lambert halves which agree pointwise on the artificial split through the canonical cusp entry `y=1`, taper to the identity in the next fixed Busemann slab, preserve every genuine opposite-boundary trace, have tail bilipschitz constants tending to one, and add a summable strong-`L^1` metric cost. Consequently the independent PF-179 body maps can be made split-coherent below the standard cusp without sacrificing `rho=1`. The remaining PF-175 gate is now the **external/global interface problem**: area-preserving zero-twist cuff compatibility, the full-cusp handoff, compatibility with all PF-177/PF-138 true short-collar gauges, and the final two-sided inverse-unit-ball weighted budget. No global Schatten, scattering, determinant, or RH conclusion is claimed.

## Claim

In the `n`th physical one-cusp pentagon, let the two source Lambert parameters be

\[
a_n,\qquad a_{n+1},
\]

with shift-clone targets

\[
a_n^+=a_n+\delta_n,\qquad
a_{n+1}^+=a_{n+1}+\delta_{n+1}.
\tag{1}
\]

Let

\[
\Theta_n(\tau):=\Theta_{a_n,a_n^+}(\tau),
\qquad
\Theta_{n+1}(\tau):=\Theta_{a_{n+1},a_{n+1}^+}(\tau)
\tag{2}
\]

be PF-179's normalized split traces, expressed in the common physical source parameter

\[
y=R_n e^\tau,
\qquad
R_n=(\cosh a_n+\cosh a_{n+1})^{-1}.
\tag{3}
\]

Put

\[
D_n^{\mathrm{vol}}(\tau):=
\Theta_n(\tau)-\Theta_{n+1}(\tau),
\qquad
T_n^{\mathrm{cusp}}
:=\log(\cosh a_n+\cosh a_{n+1}).
\tag{4}
\]

After choosing PF-179's fixed-corner interpolation with one fixed smooth cutoff, the traces may be taken so that

\[
\boxed{
\sum_n\int_0^{T_n^{\mathrm{cusp}}+1}
\left(
|D_n^{\mathrm{vol}}|
+|(D_n^{\mathrm{vol}})'|
+|(D_n^{\mathrm{vol}})''|
\right)d\tau<\infty.
}
\tag{5}
\]

Moreover the same effective-width choice as PF-139 can be made in the exact area coordinate on the two target halves. If `m_{L,n},m_{R,n}` are those capped support widths and

\[
M_n(\tau)=m_{L,n}(\tau)+m_{R,n}(\tau),
\tag{6}
\]

then

\[
\boxed{
\sup_{0\le\tau\le T_n^{\mathrm{cusp}}+1}
\frac{|D_n^{\mathrm{vol}}(\tau)|}{M_n(\tau)}
\longrightarrow0,
}
\tag{7}
\]

and the first two derivative mismatches tend uniformly to zero as well.

There are smooth area-preserving self-diffeomorphisms

\[
K_{L,n},\qquad K_{R,n}
\tag{8}
\]

of the two **target** Lambert halves such that, after postcomposing the PF-179 body maps:

1. the corrected left/right maps induce exactly the same split trace for every `0<=tau<=T_n^{cusp}`;
2. each `K_{j,n}` is the identity near the genuine opposite boundary of its Lambert half, hence it changes neither the induced finite-cuff trace nor the physical outer-cusp boundary trace;
3. each correction tapers to the identity within one fixed Busemann unit after `T_n^{cusp}` and is identically the identity deeper in the cusp;
4. each correction preserves hyperbolic area exactly;
5. on the tail,
   \[
   \boxed{
   \operatorname{Bilip}(K_{L,n})+
   \operatorname{Bilip}(K_{R,n})-2\longrightarrow0;
   }
   \tag{9}
   \]
6. for the corresponding metric-deviation scalar,
   \[
   \boxed{
   \sum_n\sum_{j\in\{L,R\}}
   \int \delta_{g,K_{j,n}^*g}\,d\mu_g<\infty.
   }
   \tag{10}
   \]

Because the corrections are exactly area preserving, composing them with PF-179 leaves

\[
\boxed{\rho\equiv1}
\tag{11}
\]

on the corrected Lambert pieces. Equation (10) also implies a summable correction cost in every unweighted `L^r`, `r>=1`, after a finite head. Combining this with PF-179's body estimate gives, for every fixed `r>1`, a finite unweighted `L^r` metric budget for the **split-coherent Lambert-body stage**. This remains strictly weaker than PF-175's two-sided inverse-unit-ball weighted hypothesis.

## 1. PF-179's area traces have the stronger growing-height budget needed for synchronization

PF-179 writes

\[
\Theta_j(\tau)
=\psi_{\beta_j}(\tau)+e_j(\tau),
\qquad
\psi_\beta(\tau)
=\operatorname{arsinh}(e^\beta\sinh\tau),
\tag{12}
\]

where

\[
\beta_j=
\log\frac{\sinh a_j^+}{\sinh a_j}
\tag{13}
\]

and

\[
\|e_j\|_{L^\infty}
+\int_0^\infty|e_j'|d\tau
\le C\delta_j e^{-2a_j}.
\tag{14}
\]

The finite and outer traces which PF-179 splices across its fixed corner patch differ there by `O(delta_j e^{-2a_j})` in every fixed derivative order. Choosing one fixed smooth interpolation therefore strengthens (14), for the same PF-179 construction, to

\[
\int_0^\infty |e_j''(\tau)|d\tau
\le C\delta_j e^{-2a_j}.
\tag{15}
\]

No new volume-form theorem is used here; (15) is only the fixed-scale smooth-cutoff estimate implicit in PF-179's corner splice.

For bounded small `beta`, direct differentiation gives

\[
\partial_\beta\psi_\beta
=\frac{e^\beta\sinh\tau}
{\sqrt{1+e^{2\beta}\sinh^2\tau}},
\qquad
|\partial_\beta\psi_\beta|\le1,
\tag{16}
\]

and PF-179 already records

\[
\partial_\beta\psi_\beta'
=\frac{e^\beta\cosh\tau}
{(1+e^{2\beta}\sinh^2\tau)^{3/2}}.
\tag{17}
\]

Differentiating (17) once more in `tau` shows, uniformly for the tail parameter range,

\[
\int_0^\infty
|\partial_\beta\psi_\beta''(\tau)|d\tau
\le C.
\tag{18}
\]

Hence, with the PF-136/PF-139 scalar mode

\[
c_n:=\beta_n-\beta_{n+1},
\tag{19}
\]

the mean-value theorem gives

\[
\int_0^{T_n^{\mathrm{cusp}}+1}
\left(
|\psi_{\beta_n}-\psi_{\beta_{n+1}}|
+|\psi_{\beta_n}'-\psi_{\beta_{n+1}}'|
+|\psi_{\beta_n}''-\psi_{\beta_{n+1}}''|
\right)d\tau
\le
C(1+T_n^{\mathrm{cusp}})|c_n|.
\tag{20}
\]

PF-134 proves

\[
\sum_n(1+T_n^{\mathrm{cusp}})|c_n|<\infty.
\tag{21}
\]

The error terms are also summable after multiplication by `1+T_n^{cusp}`: PF-107 gives `delta_n=O(p_n^{-1})`, PF-131/PF-114 give `sum e^{-2a_n}<infinity`, and `(1+log p_n)/p_n` is bounded on the tail. Equations (14)--(21) prove (5).

Thus exact area preservation changes the one-body trace, but it does not destroy the **growing-height** summability PF-139 needed for a two-dimensional split correction.

## 2. The area-trace mismatch is still small relative to the available two-sided width

Use the exact PF-179 area coordinate

\[
\boxed{x=\sinh\rho,\qquad d\mu=dx\,d\tau.}
\tag{22}
\]

Choose smooth effective support widths `m_{j,n}` in this `x` coordinate, capped by a fixed small constant and contained in a fixed fraction of the available half-width. The exact Lambert branch formulas permit the same bounds as PF-139, now with two derivatives after fixed corner smoothing:

\[
|m_{j,n}'|+|m_{j,n}''|\le C m_{j,n}.
\tag{23}
\]

Before the first Lambert corner, (16) gives

\[
|\psi_{\beta_n}-\psi_{\beta_{n+1}}|
\le C|c_n|\min\{\sinh\tau,1\}.
\tag{24}
\]

For the wider finite-branch half, PF-136 gives width at least `cosh(tau)/M_n^*`, where `M_n^*=min(cosh a_n,cosh a_{n+1})`, and proves

\[
M_n^*|c_n|\longrightarrow0.
\tag{25}
\]

The PF-179 corner error contributes only

\[
O\!\left(M_n^*(\delta_ne^{-2a_n}+\delta_{n+1}e^{-2a_{n+1}})\right)=o(1).
\tag{26}
\]

Thus the area-trace mismatch divided by the wider available support width tends to zero on the long narrow pre-corner sector.

Between unequal corner heights, PF-135/PF-139 provide the combined-width lower bound with only the already-summable square-root aspect loss, while `D_n^{vol}` differs from the same scalar mode by the exponentially small PF-179 corner error. After both corners and through one unit beyond the standard cusp entry,

\[
\tanh H_n+\tanh H_{n+1}
=(\cosh a_n+\cosh a_{n+1})e^{-\tau}
\ge e^{-1},
\tag{27}
\]

so one side has an absolute width floor. Together with (5) and `c_n->0`, these three regimes prove (7) and the required uniform derivative smallness.

This is the key quantitative point: the Hamiltonian correction below will be exact in area, but its transverse derivative still costs `boundary displacement / support width`. Equations (25)--(27) show that the actual prime/shift mismatch remains below that geometric scale everywhere before the cusp takeover.

## 3. A Hamiltonian strip correction realizes the boundary trace with Jacobian one

For one target Lambert half, write the area coordinates as `(x,sigma)` and let the desired split-boundary map be

\[
B(\sigma)=\sigma+b(\sigma).
\tag{28}
\]

As in PF-139, distribute the mismatch between the two halves according to their available widths:

\[
s_L=-\frac{m_L}{m_L+m_R}D_n^{\mathrm{vol}},
\qquad
s_R=\frac{m_R}{m_L+m_R}D_n^{\mathrm{vol}}.
\tag{29}
\]

For `tau<=T_n^{cusp}` this gives the common trace

\[
\Theta_n+s_L
=
\Theta_{n+1}+s_R.
\tag{30}
\]

Multiply both `s_j` by one fixed smooth cutoff which is `1` through `T_n^{cusp}` and becomes `0` by `T_n^{cusp}+1`. Equation (27) makes this taper occur in a uniformly noncollapsed two-sided region. Pulling (29) through the uniformly bi-Lipschitz natural trace gives `b`; equations (5), (7), and (23) imply the same summable `b,b',b''` budget and

\[
\sup\left(
|b'|+m|b''|+\frac{|b|}{m}
\right)\longrightarrow0.
\tag{31}
\]

Choose a fixed smooth cutoff `chi` supported in `[0,1)` and equal to one near `0`, and the linear boundary isotopy

\[
B_t=(1-t)\operatorname{id}+tB.
\tag{32}
\]

Let

\[
v_t=\partial_tB_t\circ B_t^{-1}.
\tag{33}
\]

On the target half define the time-dependent Hamiltonian

\[
\boxed{
\mathcal H_t(x,\sigma)
=-x\,\chi\!\left(\frac{x}{m(\sigma)}\right)v_t(\sigma).
}
\tag{34}
\]

with respect to the exact area form `dx wedge d sigma`. Its Hamiltonian vector field satisfies, at the split boundary `x=0`,

\[
\dot x=0,
\qquad
\dot\sigma=v_t(\sigma).
\tag{35}
\]

Therefore the time-one flow induces **exactly** the required boundary map `B`. Since every Hamiltonian flow preserves the symplectic two-form,

\[
\boxed{K^*(dx\wedge d\sigma)=dx\wedge d\sigma.}
\tag{36}
\]

The Hamiltonian vanishes where `x>=m(sigma)`, so the flow is the identity near the genuine opposite Lambert boundary. Equation (31), together with `|m'|+|m''|<=Cm`, keeps trajectories inside the chosen support strip and makes the flow a small diffeomorphism on the tail. Because `b` has been tapered to zero, the correction is also the identity on the deep split tail.

This is an explicit local Hamiltonian construction. No abstract Moser estimate on a degenerating pant is being imported.

## 4. The exact-area correction retains PF-139's summable metric budget

On the support of (34), `x` is bounded by one fixed small constant, so the hyperbolic metric

\[
g=\frac{dx^2}{1+x^2}+(1+x^2)d\sigma^2
\tag{37}
\]

is uniformly comparable to the Euclidean metric. Differentiating the Hamiltonian vector field and using the standard variational equation for its flow gives, for the time-one metric strain,

\[
\delta_{g,K^*g}
\le C\left(
|b'|+m|b''|+\frac{|b|}{m}+|b|
\right)
\tag{38}
\]

once the tail smallness in (31) is imposed. The support area over `d sigma` is `O(m d sigma)`, hence

\[
\int\delta_{g,K^*g}d\mu
\le C\int
\left(
|b|+|b'|+|b''|
\right)d\sigma.
\tag{39}
\]

Applying this on both sides and using (5) proves (10). The same estimate shows `Bilip(K)->1`, proving (9).

After a finite head the right-hand side of (38) is uniformly below one. Therefore for every fixed `r>=1`,

\[
\delta^r\le\delta,
\tag{40}
\]

and the correction is also summable in unweighted `L^r`. Since PF-179's independent body maps have finite unweighted `L^r` metric budget for every `r>1`, the split-coherent composition retains that same exponent range.

Most importantly, there is no density price at all:

\[
\frac{d\mu_{K^*g}}{d\mu_g}=1
\tag{41}
\]

exactly. The split synchronization therefore does not recreate the volume-identification obstruction that PF-176--PF-179 removed.

## 5. What this closes and what remains open

PF-179 reduced the area-gauge problem to assembly. PF-180 removes one of its explicit assembly bullets:

\[
\boxed{
\text{area-preserving Lambert bodies}
+\text{summable adjacent area traces}
\Longrightarrow
\text{area-preserving split synchronization below }y=1.
}
\tag{42}
\]

The surviving global tasks are narrower and external to the artificial split:

- prove that the **area-preserving** finite-cuff traces can be chosen compatibly with the zero-twist two-sided cuff germs used by the global marking;
- replace the one-unit split taper by one common full-cusp area-preserving handoff which becomes the exact deep-cusp identity;
- splice the body/cuff construction with every PF-177 optimized true short-collar gauge from the PF-138 family without losing quantitative control;
- prove the final source- and target-weighted inverse-unit-ball `delta^r` budget in one complete smooth quasi-isometric marking.

Until those interfaces are controlled simultaneously, PF-175 cannot be invoked. In particular, (10) is **unweighted** and does not license a Schatten conclusion merely because the split correction is area preserving.

## 6. Prior-art and novelty audit

No novelty is claimed for Hamiltonian flows preserving an area form, for symplectic/area-preserving extension techniques on surfaces, or for support-controlled Jacobian correction. Directed searches around Hamiltonian boundary extensions, area-preserving disk/strip extensions, and support-controlled Dacorogna--Moser constructions recover the standard symplectic theory and the Teixeira support-control theorem already audited in PF-178. Those general results do not supply the project-specific estimate here: the support width varies and can collapse, the boundary mismatch is the adjacent prime/shift Lambert trace, and one needs a summable metric cost while leaving the genuine cuff/cusp boundary untouched.

The durable content is therefore the explicit composition

\[
\boxed{
\text{PF-179 area trace}
+\text{PF-134 growing-height arithmetic budget}
+\text{PF-139/PF-136 two-sided width control}
+\text{Hamiltonian area-coordinate extension}
}
\tag{43}
\]

which shows that exact area preservation and split coherence are quantitatively compatible on the Lambert stage. Absence of a literature source for this exact specialization is not treated as a novelty theorem.

## 7. Audit / falsification core

A later adversary can test PF-180 through the following finite chain:

1. import PF-179's representation `Theta=psi_beta+e` and verify the fixed-corner interpolation can be chosen with (15);
2. differentiate `psi_beta` to verify (16)--(18), combine with PF-134's weighted `ell^1` scalar-mode estimate, and obtain (5);
3. use PF-136 before the first corner, PF-135 through unequal corner heights, and the exact cusp-width identity (27) through one unit past `y=1` to prove (7);
4. check that the weighted displacements (29) give exact left/right agreement through `T_n^{cusp}` and can taper in the next fixed unit without a width loss;
5. in `x=sinh rho`, compute the Hamiltonian vector field of (34), verify (35), and use `L_{X_H}(dx wedge d sigma)=0` to prove exact area preservation;
6. differentiate that vector field and its flow to recover the strain estimate (38), then multiply by the `O(m)` support area to obtain (39) and the summability (10);
7. verify that the Hamiltonian support misses the genuine opposite Lambert boundary and is zero on the deep split tail, so no finite-cuff or outer-cusp boundary trace is changed;
8. preserve the evidence boundary: do **not** infer cuff compatibility, full-cusp compatibility, true-collar compatibility, the inverse-unit-ball weighted PF-175 hypothesis, Schatten membership, scattering equivalence, or RH from the unweighted split result.

A refutation would need to break the stronger area-trace budget (5), the width-relative smallness (7), exact Hamiltonian area preservation, or the scale cancellation in (39). Failure of a later cuff/cusp/collar assembly would not refute PF-180; it would realize exactly the remaining boundary recorded above.