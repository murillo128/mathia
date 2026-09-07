# WP-188 — The exact Gamma phase is not an ordinary trace-class Birman–Krein scattering determinant

**Status:** `LITERATURE+DERIVED + TRACE-CLASS-SCATTERING-NO-GO + SPECTRAL-SHIFT-L1-OBSTRUCTION + ARCHIMEDEAN-GAMMA + POSITIVE-PERTURBATION-ROUTE-CLOSED + REGULARIZED-SCATTERING-BOUNDARY + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION + NOT-WEIL-POSITIVITY`.

`WP-169` identifies the exact real-place relative phase

\[
R_\infty(t)
=\pi^{it}
\frac{\Gamma(\tfrac14-\tfrac{it}{2})}
     {\Gamma(\tfrac14+\tfrac{it}{2})},
\qquad |R_\infty(t)|=1,
\tag{1}
\]

whose logarithmic phase velocity is the archimedean Weil digamma symbol. `WP-170` rules out realizing this phase as an ordinary scalar passive inner response, and `WP-187` rules out obtaining its signed orientation directly from the canonical Hardy self-commutator. A different operator-positive route is nevertheless natural: realize the phase as the scattering determinant of a self-adjoint pair

\[
H_1=H_0+B,
\tag{2}
\]

with `B >= 0`. The order `B >= 0` supplies an independent geometric/operator theorem of sign, while the Birman–Krein formula converts the pair into a scattering phase. This is exactly the kind of mechanism the research mandate asks us to test rather than merely postulating a positive kernel.

In the ordinary trace-class Birman–Krein regime this route is impossible for a stronger reason than the sign of `B`:

\[
\boxed{
R_\infty\text{ is not, even up to a constant unitary factor, the scattering determinant of any pair whose Krein spectral shift lies in }L^1(\mathbb R).
}
\tag{3}
\]

More precisely, for every `c in T` and every sufficiently large `T`,

\[
\boxed{
\int_T^\infty |cR_\infty(t)-1|\,dt=\infty.
}
\tag{4}
\]

But if `H_1-H_0` is trace class, Krein's spectral shift function satisfies `xi in L^1(R)`, and the Birman–Krein formula gives

\[
\det S(t)=e^{-2\pi i\xi(t)}
\quad\text{a.e.}
\tag{5}
\]

on the absolutely continuous scattering spectrum. Hence

\[
|\det S(t)-1|
\le 2\pi |\xi(t)|,
\tag{6}
\]

so every ordinary trace-class Birman–Krein determinant is `L^1`-close to `1`. Equation (4) therefore excludes (1) on any full scattering tail. The same argument excludes `cR_infty` for every fixed phase normalization `c`; no branch choice for the scattering phase can repair the obstruction because (6) is written directly at determinant level.

Thus even the most attractive sign-definite version, `B >= 0` trace class, fails before its positivity theorem can be used. A viable scattering realization of the exact Gamma carrier must leave the ordinary `L^1` spectral-shift category — for example through a genuinely generalized/renormalized scattering theory, a non-trace-class/domain-changing comparison, or a nonseparable finite–archimedean construction in which `R_infty` is not itself a separated scattering determinant. Such a category change does not automatically inherit the sign of an ordinary positive perturbation; its renormalization and coercivity would have to be forced independently.

## 1. Ordinary Birman–Krein determinants have an `L^1` tail defect

For self-adjoint operators with trace-class difference, the classical Krein trace formula provides a real spectral shift function

\[
\xi\in L^1(\mathbb R).
\tag{7}
\]

In the scattering setting the Birman–Krein identity is (5). Therefore the elementary inequality

\[
|e^{ix}-1|\le |x|
\tag{8}
\]

immediately yields

\[
\int_{\mathbb R}|\det S(t)-1|\,dt
\le 2\pi\|\xi\|_{L^1}
<\infty.
\tag{9}
\]

No sign hypothesis on the perturbation is used here. In particular, (9) is a necessary condition for *every* ordinary trace-class scattering determinant, not only for a positive perturbation.

For the specifically attractive positive route, let

\[
H_s=H_0+sB,
\qquad B\ge0,
\qquad B\in\mathcal S_1.
\tag{10}
\]

The Birman–Solomyak spectral-averaging representation writes the spectral-shift measure as an average of positive measures,

\[
\xi(\lambda)\,d\lambda
=
\int_0^1
\operatorname{Tr}\!\left(
B^{1/2}E_{H_s}(d\lambda)B^{1/2}
\right)ds,
\tag{11}
\]

so `xi >= 0` almost everywhere in the standard orientation. This really would have supplied a sign theorem independently of RH or zero data. The obstruction below shows that the exact Mathia Gamma phase is already incompatible with the trace-class carrier itself, so the sign theorem never reaches the arithmetic target.

## 2. The Gamma phase is not `L^1`-close to any constant phase

Choose the continuous phase branch `theta` with

\[
R_\infty(t)=e^{i\theta(t)},
\qquad \theta(0)=0.
\tag{12}
\]

`WP-170` gives

\[
\theta'(t)
=
\log\pi-
\operatorname{Re}\psi\!\left(\frac14+\frac{it}{2}\right).
\tag{13}
\]

The standard Stirling expansion for `log Gamma` gives, as `t -> +infinity`,

\[
\boxed{
\theta(t)
=-t\log\frac{t}{2\pi e}
+\frac\pi4
+O(t^{-1}),
}
\tag{14}
\]

and differentiating the digamma asymptotic gives

\[
\boxed{
\theta'(t)
=-\log\frac{t}{2\pi}
+O(t^{-2}).
}
\tag{15}
\]

Set

\[
v(t):=-\theta(t).
\tag{16}
\]

For all sufficiently large `t`, `v` is strictly increasing, tends to `+infinity`, and

\[
v'(t)=\log\frac{t}{2\pi}+O(t^{-2}),
\qquad
v''(t)=\frac1t+O(t^{-3}).
\tag{17}
\]

Fix `c=e^{i\alpha}`. Then

\[
|cR_\infty(t)-1|
=
|e^{-i(v(t)-\alpha)}-1|.
\tag{18}
\]

For every sufficiently large integer `n`, let `J_n` be the interval on which

\[
v(t)-\alpha
\in
\left[2\pi n+\frac\pi3,
      2\pi n+\frac{5\pi}3\right].
\tag{19}
\]

On `J_n`,

\[
|cR_\infty(t)-1|\ge1.
\tag{20}
\]

Let `t_n` be any point in the corresponding full phase period. Since `v'` varies by a relative `o(1)` amount across one period — by (17), a period has length `O(1/log t_n)` while `v''(t)=O(1/t)` — the mean-value theorem gives

\[
|J_n|
\asymp \frac1{\log t_n}.
\tag{21}
\]

Moreover (14) implies

\[
v(t_n)\asymp t_n\log t_n\asymp n,
\tag{22}
\]

so `log t_n asymp log n`. Therefore

\[
\sum_n |J_n|
\gtrsim
\sum_n\frac1{\log n}
=\infty.
\tag{23}
\]

Combining (20) and (23) proves (4). Notice that this is stronger than saying that the Gamma phase has no limit at infinity: its oscillations occupy infinite total measure even though their individual periods shrink like `1/log t`.

Equations (9) and (4) are incompatible. Hence no ordinary trace-class Birman–Krein scattering pair can have determinant equal to `cR_infty` on a full high-energy tail.

## 3. The positive-perturbation control is genuinely stronger than a phase-sign heuristic

One might try to use only the sign change of the Gamma phase velocity from `WP-170` against a positive scattering time-delay theorem. That would be too restrictive: time delay need not have a fixed sign for a general self-adjoint scattering problem, and the Birman–Krein determinant sees the spectral shift only modulo integer phase winding.

The present obstruction avoids both issues. It does not differentiate the scattering phase, it does not choose a logarithm branch, and it does not assume monotone time delay. It uses only the determinant identity (5), the canonical `L^1` integrability of the ordinary Krein spectral shift, and the exact Gamma tail. The contradiction therefore survives arbitrary integer branch changes and a constant unitary normalization.

Conversely, the positivity in (11) is a useful matched control. A trace-class positive perturbation really does provide an independent nonnegative spectral-shift density. The failure is not that spectral-shift positivity is circular or artificial; it is that the exact Mathia archimedean carrier is too large at infinity to belong to the ordinary trace-class scattering category at all.

## 4. Prior art and novelty boundary

The general ingredients are classical and are not Mathia discoveries.

- M. G. Krein's trace theory gives the real `L^1` spectral shift for self-adjoint trace-class perturbations.
- The Birman–Krein formula identifies the determinant of the scattering matrix with `exp(-2 pi i xi)`. Jussi Behrndt, Mark M. Malamud, and Hagen Neidhardt, *Scattering matrices and Weyl functions*, Proceedings of the London Mathematical Society 97 (2008), 568–598, DOI `10.1112/plms/pdn016`, gives an audit-friendly extension-theoretic formulation and proof.
- Barry Simon, *Spectral averaging and the Krein spectral shift*, Proceedings of the American Mathematical Society 126 (1998), 1409–1413, DOI `10.1090/S0002-9939-98-04261-0`, gives the Birman–Solomyak positive spectral-averaging formula used in (11).
- Colin Guillarmou, *Generalized Krein formula, determinants and Selberg zeta function in even dimension*, American Journal of Mathematics 131 (2009), 1359–1417, DOI `10.1353/ajm.0.0071`, is an important matched boundary: on asymptotically hyperbolic spaces the natural scattering phase requires generalized spectral functions, renormalized traces, and regularized determinants rather than the ordinary trace-class framework.

A targeted literature audit found the ordinary spectral-shift and scattering theorems, and generalized/renormalized scattering theories in which Gamma- and zeta-type determinant factors naturally occur, but not the specific Mathia consequence (4) for the exact `WP-169` Gamma carrier. The durable delta here is therefore not a new Birman–Krein theorem. It is the exact classification of the Mathia archimedean phase as lying outside the ordinary `L^1` spectral-shift scattering category, together with the identification of generalized/renormalized scattering as a genuine category change rather than a harmless reformulation.

## 5. Boundary conditions and surviving routes

The hypotheses matter.

1. The no-go applies whenever the proposed scattering realization has a spectral shift `xi in L^1(R)` and satisfies the ordinary Birman–Krein determinant formula on a full high-energy tail. It therefore includes the standard self-adjoint trace-class perturbation setting and, a fortiori, the sign-definite trace-class route (10).

2. A comparison for which only a **weighted** spectral shift is integrable, a resolvent-comparable pair outside ordinary trace-class difference, a generalized spectral function, or a regularized determinant is not covered. These are real analytic-category changes, not counterexamples to (3).

3. A genuinely nonseparable global construction in which finite primes and the real place are coupled before the scalar scattering determinant is formed is also not excluded. The finding only rules out a separated exact `R_infty` factor carried by an ordinary trace-class scattering determinant.

4. Smooth finite-window phases from `WP-187` are not contradicted by (4): they are arranged to return to `1` outside a compact set and hence have an integrable tail defect. `WP-187` kills their direct oriented Toeplitz-commutator positivity by a different mechanism. This is a matched control showing that the present obstruction is specifically about the exact global Gamma tail rather than every nontrivial unimodular phase.

5. Replacing the ordinary determinant by a regularized determinant can subtract the extensive tail responsible for (4), but then the counterterm is part of the mathematical mechanism. The research mandate requires that counterterm and its sign/coercivity be source-forced; it cannot be inserted merely to make the Gamma factor admissible.

## Consequence for `weil_positivity`

The current archimedean frontier becomes sharper. `WP-170`–`WP-187` show that bounded passive responses, finite/matrix regularizations, bounded-characteristic projective repairs, pointwise PSD lifts, and the direct Hardy oriented commutator do not turn the exact Gamma carrier into the required positivity. `WP-188` now closes the most classical self-adjoint spectral-shift escape in which positivity would have come from an ordered trace-class perturbation.

A surviving scattering/cohomological mechanism must therefore cross an explicit boundary: **ordinary `L^1` Krein spectral shift is too small for the exact Gamma phase**. Any viable route must use a source-forced generalized/renormalized or domain-changing scattering geometry, or assemble the finite and archimedean sectors nonseparably before reduction to a scalar determinant. In those larger categories, positivity is no longer inherited merely from the ordinary Birman–Krein setup and must be proved anew. No global Weil positivity statement, and no RH consequence, is obtained here.
