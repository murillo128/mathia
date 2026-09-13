# PL-295 — `H^log`/subcritical Sobolev continuity and eventual positivity cannot transport the localized-Weil ground-state sign

**Evidence:** `EXACT-DERIVED + NEGATIVE/ROUTE-RESTRICTION + MATCHED-CONTROL`

**Status:** `SIGN-CONE-NONOPEN-THROUGH-HHALF + EVENTUAL-POSITIVITY-CONTAINS-GROUND-SIGN + SOURCE-SPECIFIC-GATE`

## Claim

The sign problem left open by `PL-293`--`PL-294` cannot be solved merely by improving continuity of the certified simple localized-Weil ground branch in the currently natural Hilbert topologies, nor by replacing positivity preservation of the full semigroup with eventual/asymptotic positivity.

There are two exact obstructions.

First, let `I=(-1,1)` and let `u` be a real, nonnegative, continuous Dirichlet profile with `u(1)=0` and `u>0` somewhere in the interior. Even after restricting to the **even** subspace when `u` is even, fixed sign is not an open property in the logarithmic form topology `H^log(I)`. More strongly, whenever the zero extension `Eu` belongs to `H^s(R)`, fixed sign is not open at `u` in `H^s` for any

\[
0\le s\le \frac12.
\]

There exist smooth compactly supported real perturbations `b_epsilon`, chosen even when required, such that

\[
\|b_\varepsilon\|_{H^{\log}}\to0,
\]

and, for every fixed `s<=1/2` for which the statement is posed,

\[
\|b_\varepsilon\|_{H^s(\mathbb R)}\to0,
\]

while `u-b_epsilon` takes both positive and negative values. The same remains true after renormalizing `u-b_epsilon` to unit `L^2` norm. Hence neither the `H^log`-continuous simple branch from `PL-287` nor any future `H^s` branch continuity with `s<=1/2` can, **by topology alone**, propagate a ground-state sign from a small aperture to `a=0.8`.

Second, let `A` be a real self-adjoint lower-bounded operator with a simple isolated bottom eigenvalue `lambda_0`, normalized real ground vector `phi_0`, and spectral gap `g>0`. Then

\[
T(t):=e^{-t(A-\lambda_0)}\longrightarrow P_0
\quad\text{in operator norm},
\qquad
P_0f=\langle f,\phi_0\rangle\phi_0,
\]

with error at most `e^{-gt}`. If `T(t)` is positivity preserving for every sufficiently large `t`, or even if `T(t)f` merely approaches the positive cone for every `f>=0`, then `P_0` is a positive operator. For a rank-one self-adjoint projection this is equivalent to `phi_0` having fixed sign. Thus an eventual/asymptotic-positivity theorem strong enough to apply to the localized-Weil semigroup already **contains the missing ground-sign theorem**; it is not a weaker generic substitute for the Beurling--Deny route eliminated by `PL-294`.

The durable consequence is that the current sign gate is genuinely source-specific. A continuation theorem must control a boundary-weighted sign quantity, prove a source-specific maximum/oscillation principle, or exploit the exact arithmetic eigen-equation/absolute-value defect. Simplicity, a spectral gap, `H^log` continuity, and even a gain of Sobolev regularity up through the critical half-order do not by themselves prevent sign loss.

## 1. Boundary bumps destroy sign while vanishing in `H^log`

Choose a fixed nonnegative `psi in C_c^infinity((1/4,3/4))` with `max psi=1`. For `epsilon>0`, put

\[
M_\varepsilon
:=\max_{1-\varepsilon\le x\le1}u(x),
\qquad
A_\varepsilon:=2M_\varepsilon+\varepsilon.
\]

Continuity and `u(1)=0` give `A_epsilon -> 0`. Define the one-sided interior bump

\[
b_\varepsilon^+(x)
=A_\varepsilon\,\psi\!\left(\frac{1-x}{\varepsilon}\right).
\]

Its support lies strictly inside `I`, at distance comparable to `epsilon` from the endpoint. At a point where `psi=1`, one has

\[
u(x)\le M_\varepsilon<A_\varepsilon=b_\varepsilon^+(x),
\]

so `u-b_epsilon^+<0` there. Since `u` is positive somewhere away from that shrinking layer and the bump vanishes there, the perturbed state changes sign.

For an even reference state use instead

\[
b_\varepsilon(x)
=b_\varepsilon^+(x)+b_\varepsilon^+(-x).
\]

The two supports are disjoint for small `epsilon`, the perturbation is even, and the same sign change occurs simultaneously near both endpoints. Thus parity of the certified `a=0.8` state from `PL-284` does not protect the sign.

The logarithmic form norm used throughout `PL-285`--`PL-292` is controlled by

\[
\|b\|_2^2+
\int_{\mathbb R}\log(2+|\xi|)|\widehat b(\xi)|^2\,d\xi.
\]

For a single scaled bump, Fourier scaling gives

\[
\widehat{b_\varepsilon^+}(\xi)
=A_\varepsilon\varepsilon e^{-ix_\varepsilon\xi}
\widehat\psi(\varepsilon\xi)
\]

for an irrelevant phase `x_epsilon`. Hence

\[
\int\log(2+|\xi|)|\widehat{b_\varepsilon^+}(\xi)|^2d\xi
=A_\varepsilon^2\varepsilon
\int\log\!\left(2+\frac{|\eta|}{\varepsilon}\right)
|\widehat\psi(\eta)|^2d\eta.
\]

Because `psi` is smooth,

\[
\int\log\!\left(2+\frac{|\eta|}{\varepsilon}\right)
|\widehat\psi(\eta)|^2d\eta
=O(\log(1/\varepsilon)),
\]

so

\[
\boxed{
\|b_\varepsilon\|_{H^{\log}}^2
=O\!\left(A_\varepsilon^2\varepsilon\log(1/\varepsilon)\right)
\to0.
}
\]

The even two-bump version obeys the same bound up to a constant by the triangle inequality. In fact the logarithmic topology is so weak near a shrinking boundary layer that the amplitude need not tend to zero for the norm to vanish; the choice `A_epsilon -> 0` is made only to guarantee sign reversal for an arbitrary continuous Dirichlet profile.

Therefore the `H^log`-continuity of the simple ground branch proved in `PL-287` does **not** make its sign locally topologically stable. A sign change need not be accompanied by an eigenvalue collision, loss of simplicity, or a visible `H^log` discontinuity.

## 2. The same obstruction persists through the critical Sobolev half-order

For `0<s<1`, the homogeneous one-dimensional Sobolev scaling of the same bump is exact up to the fixed profile constant:

\[
[b_\varepsilon^+]_{\dot H^s(\mathbb R)}^2
=A_\varepsilon^2\varepsilon^{1-2s}
[\psi]_{\dot H^s(\mathbb R)}^2,
\]

while

\[
\|b_\varepsilon^+\|_2^2
=A_\varepsilon^2\varepsilon\|\psi\|_2^2.
\]

Consequently, for every `s<1/2`, even a bounded bump amplitude would be invisible asymptotically in `H^s`; with the present `A_epsilon -> 0` one also obtains at the endpoint

\[
[b_\varepsilon^+]_{\dot H^{1/2}}^2
=A_\varepsilon^2[\psi]_{\dot H^{1/2}}^2
\to0.
\]

Thus

\[
\boxed{
\|b_\varepsilon\|_{H^s(\mathbb R)}\to0
\quad\text{for every fixed }0\le s\le\frac12.
}
\]

If `Eu` itself lies in the corresponding `H^s`, then `E(u-b_epsilon)` gives sign-changing states arbitrarily close to `Eu` in that topology. Since `||b_epsilon||_2->0`, normalizing the perturbed vector back to the `L^2` unit sphere changes it by another `o(1)` term and preserves the negative boundary layer. Hence normalization of the ground branch does not alter the conclusion.

This is exactly the topology relevant to the current regularity frontier. `PL-293` showed that the canonical logarithmic-Laplacian Hopf profile

\[
u(1-t)\asymp \ell(t)^{1/2},
\qquad
\ell(t)=\frac1{|\log t|}
\]

is incompatible with zero-extension `H^{1/2}` when its coefficient is nonzero, while leaving `H^s`, `s<1/2`, open. The present result says that even if a zeta-specific estimate were to gain such subcritical Sobolev regularity and continuity, that gain would help the moving-prime **translation modulus** but would not itself solve the independent sign problem needed to invoke the Hopf lower law.

The half-order is also the sharp scaling boundary of this generic bump argument. For `s>1/2`, the factor `epsilon^{1-2s}` grows. At the natural Hopf amplitude `A_epsilon ~ ell(epsilon)^{1/2}`, the power divergence beats the logarithmic decay, so this construction no longer gives a small `H^s` sign-flipping perturbation. No claim is made that `H^s`, `s>1/2`, automatically preserves sign; only that the universal shrinking-layer counterexample ceases to be available there.

## 3. Eventual positivity collapses to the same missing ground projection

Now let `A` be self-adjoint with

\[
\lambda_0<\inf(\sigma(A)\setminus\{\lambda_0\})
=\lambda_0+g,
\qquad g>0,
\]

and let `P_0` be the orthogonal projection onto the simple ground eigenspace. The spectral theorem gives

\[
T(t)=e^{-t(A-\lambda_0)}
=P_0+e^{-t(A-\lambda_0)}(I-P_0)
\]

and therefore

\[
\boxed{
\|T(t)-P_0\|\le e^{-gt}.
}
\]

Suppose first that `T(t)` is positivity preserving for all `t>=t_0`. The positive cone of `L^2(I)` is norm closed, so for every `f>=0`,

\[
P_0f=\lim_{t\to\infty}T(t)f\ge0.
\]

Hence `P_0` is positive. The same argument works under the weaker assumption

\[
\operatorname{dist}(T(t)f,L^2_+)\to0
\qquad\text{for every }f\ge0,
\]

because `T(t)f->P_0f` in norm. Thus even asymptotic positivity of positive trajectories forces positivity of the ground projection.

For a real normalized ground vector,

\[
P_0f=\langle f,\phi_0\rangle\phi_0.
\]

If `phi_0` has both positive and negative parts of nonzero measure, take `f=(phi_0)_+`. Then

\[
\langle f,\phi_0\rangle=\|(\phi_0)_+\|_2^2>0,
\]

so `P_0f` has the same sign changes as `phi_0`, contradicting positivity. Conversely, if `phi_0` has fixed sign then `P_0` is positive. Therefore

\[
\boxed{
P_0\ge0
\iff
\phi_0\text{ can be chosen nonnegative or nonpositive a.e.}
}
\]

and every eventual/asymptotic positivity statement of the preceding type implies exactly the sign property that is missing at `a=0.8`.

A two-dimensional matched control shows why the simple gap itself gives no help. On `R^2` with the coordinatewise cone let

\[
\phi_0=\frac1{\sqrt2}(1,-1),
\qquad
\phi_1=\frac1{\sqrt2}(1,1),
\qquad
A=P_{\phi_1}.
\]

Then `A` is real self-adjoint, its ground eigenvalue `0` is simple with gap `1`, but

\[
e^{-tA}
=P_{\phi_0}+e^{-t}P_{\phi_1}
=\frac12
\begin{pmatrix}
1+e^{-t}&-1+e^{-t}\\
-1+e^{-t}&1+e^{-t}
\end{pmatrix}.
\]

For every `t>0` the off-diagonal entries are negative. The semigroup is never positive and its ground state is sign-changing, despite the perfect simple spectral gap. This is a generic order-theoretic obstruction, not arithmetic information.

## 4. Prior-art and novelty audit

The bump scaling is standard Sobolev/Fourier scaling, and positivity of a rank-one spectral projection is elementary. The general theory of eventually positive semigroups is classical and expresses eventual positivity through Perron--Frobenius-type spectral data; a targeted literature audit found no reason to regard any of those abstract ingredients as new. The proof above is deliberately self-contained and requires no new external theorem beyond the already-stored localized-Weil inputs.

The line-specific mathematical delta is the combination of these standard facts with the exact current frontier:

- `PL-284` supplies a certified simple even ground state and gap at `a=0.8` but no sign;
- `PL-287` supplies local `H^log` continuity of the actual simple branch;
- `PL-293` identifies `H^{1/2}` as the generic boundary obstruction and leaves subcritical Sobolev gains open;
- `PL-294` proves that ordinary positivity preservation has already failed at `a_BD=0.140599787...`, long before `a=0.8`.

Together with the present two lemmas, these facts rule out two natural generic repairs: **topological sign continuation in every currently accessible regularity class through the half-order, and delayed/eventual semigroup positivity as a weaker substitute for immediate positivity.** A structure-based search did not locate this exact localized-Weil route restriction stated in the literature; no broad originality claim is made for its elementary ingredients. No new durable literature dependency is introduced, so `SOURCES.md` is unchanged.

## 5. Adversarial boundaries and decisive audit tests

This result is intentionally a route restriction, not evidence that the `a=0.8` ground state changes sign.

1. **The perturbations are not eigenfunctions.** They prove only that continuity in `H^log` or `H^s`, `s<=1/2`, cannot by itself protect sign. The actual eigen-equation could constrain the branch to a much thinner subset on which sign is rigid.
2. **Parity and normalization are already controlled.** The perturbations can be chosen even and the states renormalized, so neither certified evenness nor unit `L^2` normalization repairs the topological gap.
3. **No converse eventual-positivity theorem is asserted.** Fixed sign of `phi_0` makes `P_0` positive, but by itself need not make the whole semigroup eventually positive without additional smoothing/order hypotheses. Only the implication needed for the obstruction is used.
4. **No claim is made above the half-order.** The shrinking-layer construction stops being small at the natural logarithmic boundary amplitude once `s>1/2`. A stronger weighted or supercritical topology could in principle make sign stable when combined with a quantitative boundary lower profile.
5. **The obstruction is universal.** The bump construction and spectral-projection argument work for matched non-arithmetic Dirichlet models. They therefore cannot themselves supply rational-prime rigidity.

A decisive escape must add information absent from these controls. Examples include an eigen-equation estimate controlling the ratio to the canonical boundary profile, a source-specific maximum or nodal theorem, a direct inequality forcing the absolute-value defect of the actual ground state to have the correct sign, or another invariant that prevents the rank-one ground projection from rotating out of the positive cone. Any such theorem would materially change the present conclusion because it would restrict the actual eigenbranch rather than merely strengthen its ambient Hilbert topology.

## Consequence for the research line

The sign task at the certified `a=0.8` window should no longer be phrased as “obtain enough continuity/regularity to keep the simple ground state positive” or “recover positivity only for large semigroup time.” Those formulations omit the hard step.

The surviving target is sharper: **prove a source-specific order constraint on the actual localized-Weil eigenfunction.** Subcritical Sobolev gain remains valuable for quantitative aperture transport of eigenvalues and prime-shift correlations, but it is logically separate from ground-state sign. Likewise, eventual positivity can be used only after establishing enough order structure to force the ground projection positive, which is already the missing theorem. The next useful sign mechanism must therefore enter through the rational-prime Weil equation or a boundary-weighted/nodal structure that the generic logarithmic form and spectral gap do not provide.
