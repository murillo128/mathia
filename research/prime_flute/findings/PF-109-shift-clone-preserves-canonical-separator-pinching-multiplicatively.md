# PF-109 — shift clone preserves canonical separator pinching multiplicatively

**Status:** `EXACT-DERIVED + NEGATIVE/BOUNDARY`. This strengthens PF-106 and narrows the accepted prime/composite relative-operator clue. The exact all-composite shift clone `p_n -> p_n+1`, after the canonical translation normalization, does not merely keep every PF-004 canonical separator close in **absolute** length: it keeps the length ratio uniformly close to one, even when the separator itself pinches to zero. Thus zero systole and canonical multi-gap pinching do not provide a length-spectrum amplification mechanism capable of separating the prime flute from this clone. No statement is made about all simple closed curves, quasiconformal equivalence, resolvent compactness, Schatten class, or scattering equivalence.

## Claim

Let

\[
V(x)=\pi\cot\frac{\pi}{x},
\qquad
W(x)=V(x+1)-1,
\]

and consider any four ordered prime labels

\[
P\le a<b<c<d.
\]

Let `chi_E` be the PF-004 cross-ratio for the exact prime endpoints `V(a),V(b),V(c),V(d)`, and `chi_+` the corresponding cross-ratio for the normalized all-composite shift-clone endpoints `W(a),W(b),W(c),W(d)`.

PF-106 proves the all-span bound

\[
\boxed{
\left|\log\frac{\chi_E}{\chi_+}\right|
\le C P^{-3}}
\tag{1}
\]

for an absolute constant `C`, uniformly with no restriction on the four-point span or on the size of either cross-ratio.

The canonical separating geodesic determined by a positive cross-ratio `chi` has exact length

\[
L(\chi)=4\operatorname{arsinh}\sqrt\chi.
\tag{2}
\]

Then

\[
\boxed{
\left|\log\frac{L(\chi_E)}{L(\chi_+)}\right|
\le \frac12
\left|\log\frac{\chi_E}{\chi_+}\right|
\le \frac{C}{2}P^{-3}.}
\tag{3}
\]

Equivalently,

\[
\boxed{
\frac{L(\chi_E)}{L(\chi_+)}
=1+O(P^{-3})}
\tag{4}
\]

uniformly over **all** PF-004 canonical multi-gap separators in the tail beginning at `P`, including sequences for which either length tends to zero.

Thus the shift clone preserves canonical separator pinching multiplicatively. In particular, the small-separator mechanism underlying PF-005 and the fixed-topology tangent degenerations of PF-045/PF-046 cannot produce a quasiconformal/length-spectrum obstruction merely by exploiting the fact that the prime flute has arbitrarily short canonical separators: the matched clone has the same pinching scale up to a relative error tending uniformly to zero.

## 1. Exact logarithmic Lipschitz bound for the separator coordinate

Put

\[
\Phi(t)=\log L(e^t)
=\log\left(4\operatorname{arsinh}e^{t/2}\right).
\]

Writing `u=e^{t/2}=sqrt(chi)`, direct differentiation gives

\[
\boxed{
\Phi'(t)
=
\frac{u}
{2\sqrt{1+u^2}\,\operatorname{arsinh}u}.}
\tag{5}
\]

For `u>0`,

\[
\operatorname{arsinh}u
\ge
\frac{u}{\sqrt{1+u^2}}.
\tag{6}
\]

Indeed both sides vanish at `u=0`, while their derivatives are respectively

\[
\frac1{\sqrt{1+u^2}}
\quad\text{and}\quad
\frac1{(1+u^2)^{3/2}}.
\]

Therefore

\[
\boxed{0<\Phi'(t)\le\frac12}
\tag{7}
\]

for every real `t`. The mean-value theorem applied between `log chi_E` and `log chi_+` yields the first inequality in (3).

The constant `1/2` is sharp in the pinching limit: as `chi -> 0`,

\[
L(\chi)\sim4\sqrt\chi,
\qquad
\frac{d\log L}{d\log\chi}\to\frac12.
\]

For large `chi` the logarithmic sensitivity decreases further. Thus there is no hidden singularity in the change of coordinate `chi -> L` that could amplify PF-106's uniform logarithmic cross-ratio control.

## 2. Pinching cannot defeat the all-composite control

PF-106 stated the separator consequence as an absolute estimate

\[
|L_E-L_+|=O(P^{-3}).
\]

By itself, an absolute estimate leaves an apparent loophole: if `L_E` tends to zero much faster than `P^-3`, then a tiny absolute perturbation could in principle produce an unbounded length ratio and therefore a genuine length-spectrum or quasiconformal obstruction.

Equation (3) closes exactly that loophole. It implies

\[
\boxed{
\sup_{\substack{P\le a<b<c<d\\a,b,c,d\ \mathrm{prime}}}
\left|\log\frac{L_E(a,b,c,d)}{L_+(a,b,c,d)}\right|
=O(P^{-3}).}
\tag{8}
\]

No lower bound on `L_E` or `L_+` is required. Arbitrarily short canonical geodesics are therefore mirrored by arbitrarily short clone geodesics at the same multiplicative scale.

This is particularly relevant to the zero-systole/right-limit branch. PF-005 and PF-046 construct canonical separating lengths that become arbitrarily small because of extreme multi-gap ratios. PF-099 already showed that the projective tangent patterns themselves are primality-blind. PF-109 now shows that passing back to the **exact finite-scale cotangent surfaces** does not restore a pinching amplification: the prime and all-composite exact separators remain multiplicatively indistinguishable in the tail.

## 3. Relation to the distinguished cuffs

The distinguished cuffs behave differently in additive coordinates. PF-107 proves for consecutive primes with left endpoint `p` that

\[
\ell_n^+-\ell_n\sim\frac2p,
\]

so their additive defect lies in `ell^2` but not `ell^1`. Nevertheless PF-107 also proves

\[
\sum_n\frac{|\ell_n^+-\ell_n|}{\ell_n}<\infty,
\]

and hence in particular

\[
\log\frac{\ell_n^+}{\ell_n}\to0.
\]

PF-108 then shows that the absolute standard-collar widths, canonical seam/spine distances, collar areas, and an unweighted integrated collar distortion are summable.

Together with (8), the current canonical geometric coordinates therefore show no pinching-based discontinuity:

\[
\boxed{
\begin{array}{c}
\text{distinguished cuffs: relative defect }\to0,\\
\text{canonical multi-gap separators: uniform log-length defect }O(P^{-3}),\\
\text{collar/spine transverse defects: summable.}
\end{array}}
\tag{9}
\]

This combination strengthens the perturbative side of the accepted relative-operator clue, but it does not settle it.

## 4. Consequence for the relative-operator clue

One adversarial route for rejecting the prime/composite comparison was a pinching amplification:

\[
\text{small endpoint deformation}
\longrightarrow
\text{arbitrarily short prime separator}
\longrightarrow
\text{order-one or unbounded relative length defect}
\longrightarrow
\text{Weyl/right-limit obstruction}.
\]

PF-109 rules out the middle implication for the entire PF-004 canonical separator family. The shift-clone cross-ratio control is already logarithmic, and the hyperbolic separator coordinate is globally `1/2`-Lipschitz in that logarithmic variable.

Therefore any genuine obstruction to a controlled quotient-surface or relative-Laplacian comparison must come from something not captured by these canonical pinching lengths, for example:

- closed-curve/word classes outside the PF-004 separator family;
- failure to glue local pants maps equivariantly;
- weighted metric deviation in globally thin regions not controlled by PF-108;
- or a nonlocal operator effect that survives despite the multiplicative length matching.

Conversely, (8) is not enough to prove quasiconformal equivalence. On an infinite-type surface, control of one distinguished family of simple geodesics is weaker than a bound over **all** essential simple closed curves, and neither is by itself a compact/Schatten resolvent theorem.

## 5. Prior art and novelty audit

No novelty is claimed for the universal inequality (7). It is an elementary consequence of the standard exact relation

\[
L=4\operatorname{arsinh}\sqrt\chi
\]

between the relevant four-point cross-ratio and the corresponding separating length. Likewise, the general principle that quasiconformal maps control hyperbolic length ratios is classical and is not invoked as a converse here.

The durable project-specific content is the composition with PF-106's unusually strong **uniform all-span logarithmic cross-ratio estimate** for the exact `p_n -> p_n+1` all-composite clone. That composition removes a concrete loophole left by the earlier absolute-length wording: even the zero-systole canonical sector cannot amplify the clone defect into an order-one relative length change.

Directed prior-art checks around infinite-type Fenchel-Nielsen, shear, and quasisymmetric parameterizations do not supply the missing operator theorem. In particular, existing upper-bounded-pants results cannot simply be imported to the prime flute, while the accepted clue records Minsky's local unbounded-cuff comparison as a possible geometric bridge. PF-109 is therefore a project-level boundary result, not a new theorem about general infinite-type Teichmuller theory.

## 6. Audit / falsification core

The finite reusable checks are:

1. take PF-106's proved estimate `|log(chi_E/chi_+)| <= C P^-3` as the only clone input;
2. differentiate `Phi(t)=log(4 asinh(exp(t/2)))` and verify (5);
3. prove `asinh(u) >= u/sqrt(1+u^2)` by comparing derivatives from zero;
4. conclude `0<Phi'(t)<=1/2` and apply the mean-value theorem to obtain (3);
5. keep the quantifiers from PF-106: the bound is uniform over arbitrary four-point span and arbitrary positive `chi`;
6. do not extend the conclusion from PF-004 canonical separators to all simple closed curves, the full length spectrum, a quasiconformal conjugacy, or any relative operator class without an additional theorem.

A refutation would have to break PF-106's logarithmic cross-ratio estimate or the elementary global derivative bound above. A failure of the broader operator-comparison program would not refute PF-109; it would identify information carried outside this canonical separator sector.