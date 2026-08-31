# PF-131 — the PF-121 split-ray trace mismatch is summable on bounded height

**Status:** `EXACT-DERIVED + NEGATIVE/BOUNDARY`. PF-119 showed that the canonical scalar cusp-split offset differentiates the nonsummable single-cuff shift mode, PF-121 supplied explicit one-parameter Lambert maps with hidden strong-`L^1` localization later extracted in PF-130, and PF-124 showed that their finite-cuff traces are already exactly zero-twist coherent. A remaining interface concern was more functional: the independently chosen left/right PF-121 maps need not induce the same parametrization of their common artificial split ray. The present calculation identifies those two traces exactly in a common physical Busemann coordinate and proves that their complete mismatch on every fixed bounded-height slab is summable in a natural `L^infinity + W^{1,1}` trace norm. Thus the reciprocal-prime common mode does not reappear merely by keeping the full nonlinear split-ray boundary trace. No two-dimensional extension, global strong-`L^1` marking, Schatten class, wave operator, scattering, determinant, or RH conclusion is claimed.

## Claim

Use the PF-119 normalized ideal Lambert quadrilateral

\[
Q(a)=\{\text{between }x=0,\ x=1,\ |z|=\tanh a,\ |z-1|=\operatorname{sech}a\}
\]

and let `a'>=a` be its matched shift-clone half-cuff. Parameterize the artificial split ray `x=1` by Busemann height from its finite endpoint:

\[
\boxed{
z_a(\tau)=1+i\operatorname{sech}(a)e^\tau,\qquad \tau\ge0.}
\tag{1}
\]

Let `F_{a,a'}` be the explicit PF-121 map, interpreted in this normalization. There is an increasing piecewise-smooth trace function

\[
\Phi_{a,a'}:[0,\infty)\to[0,\infty)
\]

such that

\[
\boxed{
F_{a,a'}(z_a(\tau))
=1+i\operatorname{sech}(a')e^{\Phi_{a,a'}(\tau)}.
}
\tag{2}
\]

Write

\[
\epsilon=\log\frac{\cosh a'}{\cosh a}.
\tag{3}
\]

For every fixed `H>0`, define the limiting trace family

\[
G_\epsilon(\tau)=
\begin{cases}
\alpha(\epsilon)\tau,&0\le\tau\le1,\\[4pt]
\operatorname{arcosh}(e^\epsilon\cosh\tau),&1\le\tau\le H,
\end{cases}
\qquad
\alpha(\epsilon)=\operatorname{arcosh}(e^\epsilon\cosh1).
\tag{4}
\]

On a sufficiently far tail there is a constant `C_H` such that

\[
\boxed{
\|\Phi_{a,a'}-G_\epsilon\|_{L^\infty(0,H)}
+
\int_0^H|\Phi_{a,a'}'(\tau)-G_\epsilon'(\tau)|\,d\tau
\le C_H e^{-2a}.
}
\tag{5}
\]

The derivatives are taken almost everywhere; both traces have only the single PF-121 splice.

Now specialize to the exact prime/shift-clone pant chain. Put

\[
a_n=\frac{\ell_n}{2},\qquad a_n^+=\frac{\ell_n^+}{2},\qquad
\epsilon_n=\log\frac{\cosh a_n^+}{\cosh a_n},
\tag{6}
\]

and abbreviate

\[
\Phi_n=\Phi_{a_n,a_n^+}.
\]

PF-119 proves

\[
\sum_n|\epsilon_n-\epsilon_{n+1}|<\infty,
\tag{7}
\]

while PF-114's exact collar conversion and square-summable logarithmic mesh imply

\[
\sum_n e^{-2a_n}<\infty.
\tag{8}
\]

Consequently, for every fixed `H>0`,

\[
\boxed{
\sum_n\left(
\|\Phi_n-\Phi_{n+1}\|_{L^\infty(0,H)}
+
\int_0^H|\Phi_n'-\Phi_{n+1}'|\,d\tau
\right)<\infty.
}
\tag{9}
\]

Equation (9) is exactly the mismatch between the **left and right PF-121 traces on the same physical split ray** of the `n`th one-cusp pentagon. It is therefore stronger than the scalar offset cancellation of PF-119: the whole bounded-height nonlinear boundary parametrization has summable adjacent defect.

## 1. The PF-121 log-polar coordinate has an exact split-ray Busemann formula

Put

\[
r=\tanh a,\qquad s=\operatorname{sech}a.
\]

The real Möbius isometry

\[
\boxed{
M_a(z)=e^a\frac{z-r}{z+r}
}
\tag{10}
\]

sends the PF-119 model to the PF-121 log-polar normalization. Indeed the finite-cuff geodesic has endpoints `+-r` and is sent to the imaginary axis, while the split ray has endpoints `1,infinity` and is sent to the geodesic with endpoints

\[
M_a(1)=e^{-a},\qquad M_a(\infty)=e^a,
\]

which is precisely the graph boundary in PF-121.

Write

\[
M_a(z_a(\tau))=e^{u+i\theta}.
\]

A direct modulus calculation gives

\[
e^{2u}
=
\frac{1+e^{2(a+\tau)}}{e^{2a}+e^{2\tau}},
\tag{11}
\]

and hence the exact identity

\[
\boxed{
\tanh u=\tanh a\,\tanh\tau.
}
\tag{12}
\]

Thus

\[
\boxed{
u_a(\tau)=\operatorname{artanh}(\tanh a\,\tanh\tau)}
\tag{13}
\]

is the PF-121 log-radial coordinate of the point whose normalized split-ray Busemann height is `tau`. In particular `u_a(0)=0` and `u_a(\tau)->a` as `tau->infinity`.

## 2. The PF-121 split trace is explicit

PF-121 maps the log-radial coordinate by

\[
T_{a,a'}(u)=
\begin{cases}
 u_1u,&0\le u\le1,\\[4pt]
 \operatorname{arcosh}(c\cosh u),&1\le u\le a,
\end{cases}
\tag{14}
\]

where

\[
c=\frac{\cosh a'}{\cosh a}=e^\epsilon,
\qquad
u_1=\operatorname{arcosh}(c\cosh1).
\tag{15}
\]

The same `u`-map occurs on the graph boundary, so converting back with (12) gives the exact trace

\[
\boxed{
\Phi_{a,a'}(\tau)
=
\operatorname{artanh}
\left(
\frac{\tanh T_{a,a'}(u_a(\tau))}{\tanh a'}
\right).
}
\tag{16}
\]

On the tail branch `u_a(\tau)>=1`, (16) simplifies further. Since

\[
\cosh T_{a,a'}(u)=c\cosh u,
\]

substitution of (12) and elementary hyperbolic algebra give

\[
\operatorname{sech}^2\Phi_{a,a'}(\tau)
=
\left(\frac{\sinh a}{\sinh a'}\right)^2
\operatorname{sech}^2\tau.
\tag{17}
\]

Therefore

\[
\boxed{
\Phi_{a,a'}(\tau)
=
\operatorname{arcosh}
\left(
\frac{\sinh a'}{\sinh a}\cosh\tau
\right)
\qquad (u_a(\tau)\ge1).
}
\tag{18}
\]

This formula exposes a useful cancellation. The tail Busemann shift tends to

\[
\log\frac{\sinh a'}{\sinh a},
\]

but the Euclidean scale at the bottom of the normalized split ray changes by `sech(a')/sech(a)`. Their product is only

\[
\frac{\tanh a'}{\tanh a},
\]

so the apparent additive half-cuff displacement is largely a coordinate scale rather than a physical split-ray mismatch.

## 3. Restoring the physical pant removes every neighboring chart-scale factor

For a physical one-cusp pentagon `P(2a,2b,0)`, PF-119 writes

\[
A=\cosh a,\qquad B=\cosh b,
\qquad
t=\frac{A}{A+B},
\qquad R=\frac1{A+B}.
\tag{19}
\]

The left Lambert normalization is `z->z/t`. Hence a physical point on the common split ray at height

\[
\boxed{
y=Re^\tau}
\tag{20}
\]

has normalized height

\[
\frac yt
=\frac1A e^\tau
=\operatorname{sech}(a)e^\tau,
\]

exactly as in (1). After applying PF-121 and restoring the target chart,

\[
y_L^+
=t^+\operatorname{sech}(a^+)e^{\Phi_{a,a^+}(\tau)}
=R^+e^{\Phi_{a,a^+}(\tau)}.
\tag{21}
\]

The right normalization gives, independently,

\[
y_R^+
=R^+e^{\Phi_{b,b^+}(\tau)}.
\tag{22}
\]

Thus all physical placement factors cancel identically. The two independently chosen Lambert maps disagree on their common physical split ray **if and only if** their one-parameter trace functions disagree:

\[
\boxed{
\log\frac{y_L^+}{y_R^+}
=
\Phi_{a,a^+}(\tau)-\Phi_{b,b^+}(\tau).
}
\tag{23}
\]

For the `n`th prime/shift pant, `(a,b)=(a_n,a_{n+1})`, so (23) identifies the interface defect exactly with `Phi_n-Phi_{n+1}`. Extreme neighboring gap ratios do not introduce an additional `t^{-1}` or `(1-t)^{-1}` amplification.

## 4. Finite-`a` traces are summably close to a one-parameter limiting family

Fix `H`. On `[0,H]`,

\[
\tanh a=1+O(e^{-2a}),
\qquad
\tanh a'=1+O(e^{-2a}),
\tag{24}
\]

uniformly for the small positive prime/shift displacement. Equation (13) therefore gives

\[
u_a(\tau)=\tau+O_H(e^{-2a}).
\tag{25}
\]

The PF-121 splice `u=1` occurs at

\[
\tau_a^*
=
\operatorname{artanh}
\left(\frac{\tanh1}{\tanh a}\right)
=1+O(e^{-2a}).
\tag{26}
\]

On the base branch, (16), (24), and (25) converge with first derivatives to

\[
G_\epsilon(\tau)=\alpha(\epsilon)\tau.
\]

On the tail branch, put

\[
\beta=\log\frac{\sinh a'}{\sinh a}.
\]

Then

\[
\beta-\epsilon
=
\log\tanh a'-\log\tanh a
=O(e^{-2a}),
\tag{27}
\]

and (18) converges with first derivatives on every bounded tail interval to

\[
G_\epsilon(\tau)=\operatorname{arcosh}(e^\epsilon\cosh\tau).
\]

Away from the splice these are ordinary smooth-parameter estimates with denominators uniformly separated from zero. The two splice locations differ by only `O(e^-2a)`; on the intervening interval both one-sided derivatives remain uniformly bounded. Therefore the derivative error accumulated there is also `O_H(e^-2a)`. This proves (5), including the `W^{1,1}` interpretation appropriate to the piecewise-smooth PF-121 trace.

The limiting family itself is Lipschitz in `epsilon` in the same norm. For `epsilon` in a fixed small tail interval,

\[
\boxed{
\|G_\epsilon-G_{\tilde\epsilon}\|_{L^\infty(0,H)}
+
\int_0^H|G_\epsilon'-G_{\tilde\epsilon}'|\,d\tau
\le C_H|\epsilon-\tilde\epsilon|.
}
\tag{28}
\]

On `[0,1]` this is smooth dependence of `alpha(epsilon)`. On `[1,H]`, the denominator in derivatives of `arcosh(e^epsilon cosh tau)` is bounded below by `sinh(1)`, so the parameter derivatives are uniformly bounded.

## 5. Prime/shift summation differentiates the common mode once more

PF-119 proves exactly the finite-variation input (7). For the finite-`a` remainder, PF-114 gives

\[
\sinh a_n\,\sinh\frac{h_n}{2}=1,
\qquad
\sum_n h_n^2<\infty.
\tag{29}
\]

Since `h_n->0`,

\[
e^{-2a_n}
\le C\sinh^{-2}a_n
=C\sinh^2\frac{h_n}{2}
\le C'h_n^2
\tag{30}
\]

on a tail, proving (8).

Now insert `epsilon_n,epsilon_{n+1}` into (5) and (28):

\[
\begin{aligned}
&\|\Phi_n-\Phi_{n+1}\|_\infty
+
\|\Phi_n'-\Phi_{n+1}'\|_{L^1(0,H)}\\
&\qquad\le
C_H\left(
|\epsilon_n-\epsilon_{n+1}|
+e^{-2a_n}+e^{-2a_{n+1}}
\right).
\end{aligned}
\tag{31}
\]

Summing (31) and using (7)--(8) proves (9).

The mechanism is the same differential cancellation seen in PF-114/PF-119, but at a stronger boundary-data level:

```text
single-cuff chart scale epsilon_n ~ 1/p_n        not l1
adjacent scalar split offset Delta epsilon_n     l1
full bounded-height PF-121 trace mismatch        l1 in Linf + W11
```

So retaining the nonlinear split-ray parametrization does not resurrect the nonsummable reciprocal-prime mode.

## 6. Consequence for the operator/scattering frontier

PF-130 left a specific concern: its strong-`L^1` Lambert-body maps were constructed independently, whereas PF-125 achieved exact global boundary coherence using a different comparison whose recorded integrated cost was only coarse. PF-131 removes one part of that gap. The **raw PF-121 left/right boundary discrepancy itself already has a summable budget on every fixed Busemann-height slab**.

This is useful, but it is not yet the desired global theorem. A future construction must still show that correcting this trace mismatch through a two-dimensional neighborhood can be done with a comparably summable metric-deviation cost while preserving the finite-cuff trace, and must reconcile that bounded-height correction with PF-129's exact deep-cusp synchronization. Even after that, the Güneysu--Thalmaier wave criterion retains its inverse-unit-ball-volume weight in non-cusp thin regions, and the sharp-Schatten clue retains its operator-level interface/commutator problem.

Accordingly PF-131 rules out only the cheap obstruction

\[
\boxed{
\text{PF-121 strong-}L^1\text{ pieces}
\Longrightarrow
\text{nonsummable split-ray trace mismatch}.}
\]

Any surviving obstruction must arise from the **two-dimensional extension cost, thin-part weighting, noncanonical thin channels, or operator assembly**, not from an unsummable boundary parametrization already present before extension.

## 7. Prior art and novelty audit

No novelty is claimed for Möbius normalization, Busemann coordinates, ideal Lambert quadrilaterals, or elementary `W^{1,1}` estimates. Vuorinen--Wang, *Hyperbolic Lambert quadrilaterals and quasiconformal mappings* (Ann. Acad. Sci. Fenn. Math. 38 (2013), DOI `10.5186/aasfm.2013.3845`), study hyperbolic Lambert quadrilaterals and their quasiconformal images. Minsky's pants/degenerate-hexagon comparison and the general Lipschitz-pants literature already audited in PF-119--PF-124 provide broader geometric context. None of those sources supplies the PF-121 explicit trace or the prime/shift finite-variation specialization used here.

Directed searches by structure -- Lambert-quadrilateral boundary maps, prescribed geodesic-side parametrizations, Busemann traces of hyperbolic pants maps, and asymptotically conformal flute comparisons -- found general distortion and boundary-correspondence results but no theorem identifying (16)--(18) or yielding the summation (9). Absence of matching wording is not treated as novelty evidence. The durable Mathia content is the project-specific composition

\[
\boxed{
\text{PF-121 explicit Lambert map}
+\text{PF-119 adjacent finite variation}
+\text{PF-114 square-summable mesh}
\Longrightarrow
\text{summable full split-trace mismatch on bounded height}.}
\]

This is a boundary lemma for the accepted shift-clone operator program, not a new theorem about general infinite-type Teichmuller theory and not evidence for RH.

## 8. Audit / falsification core

A later adversary can check PF-131 through the following finite chain:

1. verify that the Möbius map (10) sends the PF-119 normalized `Q(a)` to the PF-121 log-polar model, in particular `1,infinity -> e^-a,e^a`;
2. substitute `z_a(tau)` into (10) and derive the exact relation `tanh u=tanh a tanh tau`;
3. restrict the two PF-121 formulas to the graph boundary and convert back with (12), obtaining (16);
4. on the tail branch, derive (17)--(18) algebraically from `cosh u'=c cosh u`;
5. restore the physical PF-119 chart and verify the exact cancellation `t sech(a)=R`, giving (21)--(23) on both sides;
6. check the bounded-height finite-`a` estimate (5): `u_a-tau=O_H(e^-2a)`, the splice shift is `O(e^-2a)`, and `beta-epsilon=O(e^-2a)`;
7. verify the uniform parameter-Lipschitz estimate (28) for the fixed-splice limiting family;
8. import only PF-119's `sum |epsilon_n-epsilon_{n+1}|<infinity` and PF-114's `sum h_n^2<infinity` plus the exact collar identity to sum (31);
9. do **not** infer a globally coherent two-dimensional map, the Güneysu--Thalmaier weighted integral, Schatten membership, wave/scattering equivalence, relative determinants, resonance equality, or any RH statement from the trace estimate alone.

A refutation must break one of the explicit coordinate identities, the bounded-height stability estimate, or the two already-persisted summability inputs. Failure of a later two-dimensional extension or operator theorem would not refute PF-131; it would identify precisely the remaining mechanism that this result leaves open.
