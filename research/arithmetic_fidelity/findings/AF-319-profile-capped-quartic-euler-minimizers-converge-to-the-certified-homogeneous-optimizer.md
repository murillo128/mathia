# AF-319 — Profile-capped quartic Euler minimizers converge to the certified homogeneous optimizer

**Status:** `EXACT-DERIVED`, `COMPUTER-ASSISTED-INPUT`, `SOURCE-COERCIVITY`, `VARIATIONAL-TRANSFER`, `QUANTITATIVE-RECOVERY`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

Fix

\[
x>0,\qquad \sigma>0,\qquad T<\infty,
\]

and consider the five-node quartic minimal-support source class of AF-195/AF-199. A projective source shape is represented by four positive consecutive gaps

\[
q=[a:b:c:d],
\]

and carries the scale-free quartic profile

\[
Q(q)=\frac{M_4}{W_1^4}
\]

from AF-198. For each shape and each target separation `\delta>0`, rescale the four gaps uniquely so that the induced mutually singular probability pair has

\[
W_1(\mu_+,\mu_-)=\delta,
\]

while the left endpoint remains anchored at `x`.

Write

\[
F_s(u)=-\log(1-e^{-su}),\qquad s=\sigma+i\tau,
\]

and define the normalized fixed-band Euler objective

\[
J_\delta(q)
:=
\frac1{\delta^4}
\sup_{|\tau|\le T}
\left|
\int F_{\sigma+i\tau}(u)\,d(\mu_+-\mu_-)(u)
\right|.
\tag{1}
\]

Let

\[
M_4^{\rm band}
:=
\sup_{|\tau|\le T}
\left|F_{\sigma+i\tau}^{(4)}(x)\right|>0,
\qquad
c_{x,\sigma,T}:=\frac{M_4^{\rm band}}{24}.
\tag{2}
\]

The computer-assisted certificate returned by GitHub issue #131 establishes for the exact AF-198 objective that

\[
Q(q)\ge Q_*,
\tag{3}
\]

with equality only, modulo common scale, at

\[
q_*=[1:t_*:t_*:1],
\qquad
9t_*^3-5t_*^2-7t_*-1=0,
\tag{4}
\]

and also supplies the exact boundary separator

\[
Q(q)\ge3
\tag{5}
\]

whenever one largest gap is normalized to `1` and at least one of the other three gaps is at most `1/2`. The same certificate gives

\[
Q_*<\frac{2891}{1000}<3.
\tag{6}
\]

Choose any fixed

\[
Q_*<C<3
\tag{7}
\]

and let

\[
\mathcal K_C:=\{q:Q(q)\le C\}
\tag{8}
\]

be the corresponding projective profile-capped source class. Then:

1. `\mathcal K_C` is compact in projective four-gap shape space;
2. the full Euler objective converges **uniformly** on this class to the homogeneous quartic objective,
   \[
   \boxed{
   \sup_{q\in\mathcal K_C}
   \left|J_\delta(q)-c_{x,\sigma,T}Q(q)\right|
   \le
   \frac{L_5(x,\sigma,T)}8 C^2\delta,
   }
   \tag{9}
   \]
   where
   \[
   L_5(x,\sigma,T)
   :=
   \sup_{u\ge x,\ |\tau|\le T}
   |F_{\sigma+i\tau}^{(5)}(u)|<\infty;
   \]
3. for every `\delta>0`, `J_\delta` has a minimizer on `\mathcal K_C`; and if `q_\delta` is any such minimizer, then
   \[
   \boxed{q_\delta\longrightarrow q_*}
   \tag{10}
   \]
   projectively as `\delta\downarrow0`;
4. the homogeneous profile excess obeys the explicit bound
   \[
   \boxed{
   0\le Q(q_\delta)-Q_*
   \le
   \frac{6L_5(x,\sigma,T)C^2}{M_4^{\rm band}}\,\delta;
   }
   \tag{11}
   \]
5. using AF-198's positive-definite projective Hessian at `q_*`, any smooth local projective coordinate `\xi=(r,x_1,y_1)` of the AF-198 type satisfies
   \[
   \boxed{\|\xi(q_\delta)-\xi(q_*)\|=O(\sqrt\delta).}
   \tag{12}
   \]

Thus the optimizer-transfer component of the accepted quartic localization clue has a concrete positive answer: **a cap on the already-defined homogeneous quartic source profile, chosen below the certified boundary level `3`, simultaneously supplies projective compactness and the physical localization needed to transfer the unique homogeneous optimizer to genuine fixed-band Euler minimizers.**

The profile cap is an additional source resource. AF-200 still rules out the corresponding unrestricted statement: normalized full-Euler sublevels alone admit escaping shapes with `Q\to\infty` and vanishing Euler objective.

## Derivation

### 1. The certified boundary gap makes the profile sublevel compact

Because `Q` is invariant under common rescaling, normalize a projective shape by setting one largest gap equal to `1`. There are only four possible max charts.

Issue #131's exact rational Bernstein boundary certificate covers every chart region in which at least one of the remaining normalized gaps is at most `1/2` and proves `(5)` there. Therefore every shape in `\mathcal K_C` with `C<3` has all four normalized gaps in the interval

\[
(1/2,1].
\tag{13}
\]

Hence `\mathcal K_C` is contained in the finite union of the four compact chart boxes with the three free normalized gaps in `[1/2,1]`. On those boxes the rational formula for `Q` from AF-198 has no vanishing denominator, so it is continuous. The condition `Q\le C` is closed there. This proves compactness of `(8)`.

This is the missing projective equicoercivity. It is stronger than the physical knot localization of AF-203: it prevents the projective shape itself from escaping toward a collision face while `\delta` shrinks.

### 2. Bounded profile gives uniform full-band transfer

For a source of shape `q`, let `D(q,\delta)` denote the anchored physical knot diameter after scaling to `W_1=\delta`. AF-203 proves the universal coercive estimate

\[
D(q,\delta)\le3Q(q)\delta.
\tag{14}
\]

It also proves, using the positive Peano carrier and the uniform fifth-derivative bound, that the normalized Euler profile

\[
E_{\delta,q}(\tau)
:=
\frac1{\delta^4}
\int F_{\sigma+i\tau}(u)\,d(\mu_+-\mu_-)(u)
\tag{15}
\]

satisfies

\[
\sup_{|\tau|\le T}
\left|
E_{\delta,q}(\tau)
-
\frac{Q(q)}{24}F_{\sigma+i\tau}^{(4)}(x)
\right|
\le
\frac{L_5}{24}Q(q)D(q,\delta).
\tag{16}
\]

Combining `(14)` and `(16)` gives

\[
\sup_{|\tau|\le T}
\left|
E_{\delta,q}(\tau)
-
\frac{Q(q)}{24}F_{\sigma+i\tau}^{(4)}(x)
\right|
\le
\frac{L_5}{8}Q(q)^2\delta.
\tag{17}
\]

On `\mathcal K_C`, the right-hand side is bounded by `(L_5/8)C^2\delta` uniformly in shape.

The reverse triangle inequality for the sup norm gives

\[
\left|
\|E_{\delta,q}\|_{L^\infty[-T,T]}
-
\left\|\frac{Q(q)}{24}F_{\sigma+i\tau}^{(4)}(x)\right\|_{L^\infty[-T,T]}
\right|
\le
\left\|E_{\delta,q}
-
\frac{Q(q)}{24}F_{\sigma+i\tau}^{(4)}(x)
\right\|_\infty.
\tag{18}
\]

The first norm in `(18)` is `J_\delta(q)` and the second is exactly `c_{x,\sigma,T}Q(q)`. Equation `(9)` follows.

AF-204 identifies the sharper intrinsic transfer gate as `QD\to0`. Here `(14)` shows uniformly that

\[
QD\le3Q^2\delta\le3C^2\delta\to0,
\tag{19}
\]

so the profile cap supplies that exact gate automatically.

### 3. Uniform convergence plus compactness transfers minimizers

Continuity of the exact finite-source Euler expression in the positive gap variables implies continuity of `J_\delta` on `\mathcal K_C`. Compactness therefore gives at least one minimizer `q_\delta` for every `\delta>0`.

Let

\[
\varepsilon_\delta:=\frac{L_5}{8}C^2\delta.
\tag{20}
\]

Since `q_*\in\mathcal K_C`, minimality and `(9)` give

\[
\begin{aligned}
c_{x,\sigma,T}Q(q_\delta)-\varepsilon_\delta
&\le J_\delta(q_\delta)\\
&\le J_\delta(q_*)\\
&\le c_{x,\sigma,T}Q_*+\varepsilon_\delta.
\end{aligned}
\tag{21}
\]

Therefore

\[
0\le Q(q_\delta)-Q_*
\le
\frac{2\varepsilon_\delta}{c_{x,\sigma,T}}
=
\frac{6L_5C^2}{M_4^{\rm band}}\delta,
\tag{22}
\]

which is `(11)`.

Every sequence `\delta_n\downarrow0` has, by compactness, a subsequence for which `q_{\delta_n}` converges projectively to some `\bar q\in\mathcal K_C`. Equation `(22)` and continuity give

\[
Q(\bar q)=Q_*.
\tag{23}
\]

The issue-#131 certificate says the equality shape is unique modulo scale, so `\bar q=q_*`. Since every convergent subsequence has the same limit, the full family converges as in `(10)`.

Because `Q(q_\delta)\to Q_*<C`, the profile cap is eventually nonbinding at the constrained minimizer. It remains essential globally as an admissibility resource: removing it reintroduces AF-200's mass-escape family.

### 4. AF-198 upgrades objective convergence to a shape rate

AF-198 proves that the Hessian of `Q` in its three scale-free coordinates is positive definite at the stationary point `q_*`. Hence there are a projective neighborhood `U` of `q_*` and `\kappa>0` such that

\[
Q(q)-Q_*
\ge
\kappa\,\|\xi(q)-\xi(q_*)\|^2
\qquad(q\in U).
\tag{24}
\]

Equation `(10)` places `q_\delta` in `U` for all sufficiently small `\delta`. Combining `(22)` and `(24)` yields `(12)`.

The `O(\sqrt\delta)` rate is a local variational consequence of the already-proved Hessian nondegeneracy; it is not a new global convexity claim.

## Why this closes the accepted localization clue

The clue originally asked what extra localization/equicoercivity resource is needed before the globally certified homogeneous optimizer can control actual fixed-band Euler minimizers. AF-200--AF-204 successively separated the relevant resources:

- `W_1` alone is noncoercive;
- `D\to0` is the physical localization topology;
- `QD\to0` is the exact varying-profile full-band transfer gate;
- unrestricted full-Euler sublevels do not force that gate.

The present result adds the missing optimizer step. The source class `Q\le C<3` is mathematically intrinsic to the same homogeneous response already being optimized. On it, AF-203 forces `QD\to0`, while the issue-#131 boundary certificate makes the projective sublevel compact. Uniform convergence then transfers the unique certified `Q` minimizer to actual Euler minimizers.

This does not say the profile cap is the weakest possible source restriction. It gives a clean sufficient class that closes the clue's existence question and isolates what remains outside it: any broader theorem must replace the externally retained profile control by another mechanism that simultaneously prevents projective escape and forces `QD\to0`.

## Prior art and novelty assessment

The variational step is classical. Uniform convergence of continuous objectives on a compact set gives convergence of minimum values, and uniqueness of the limit minimizer gives convergence of minimizers; this is stronger than what is needed from general Gamma-convergence machinery. Standard Gamma-convergence texts treat the more general compactness/equicoercivity framework for convergence of minima and minimizers. No novelty is claimed for that principle.

The new durable content is the exact specialization to the already-established Arithmetic Fidelity source geometry: the issue-#131 boundary certificate supplies projective compactness at the explicit threshold `3`, AF-203/AF-204 supply the physical transfer estimate, and AF-198 supplies local quadratic rigidity. Their combination yields the explicit full-Euler optimizer-transfer theorem `(9)`--`(12)`.

The issue-#131 global optimizer and boundary statements are **computer-assisted inputs**, not silently upgraded to a symbolic proof. The issue records an exact Bernstein boundary certificate together with validated 128-bit Arb branch-and-bound and Hessian coverage of the interior. The analytic transfer from those certified inputs to `(9)`--`(12)` is derived above exactly.

## Boundaries and falsification checks

- **Computer-assisted dependency.** The uniqueness and boundary separator used in `(3)`--`(6)` depend on the certificate recorded in GitHub issue #131. If that certificate is invalidated, the corresponding compactness/identity conclusions here must be revisited; the uniform estimate `(9)` conditional on a profile cap remains an AF-203 consequence.
- **The threshold `3` is not claimed sharp.** It is the exact boundary level certified by issue #131. Larger compact profile sublevels may exist, but they require a separate projective properness proof.
- **The profile cap is an admitted source resource.** It is not inferred from small unrestricted Euler objective. AF-200 proves that such an inference is false.
- **Fixed analytic window.** The constants fix `x>0`, `\sigma>0`, and finite `T`. Growing bands, `\sigma\downarrow0`, or moving anchors require new uniform estimates.
- **Fixed source class.** The theorem concerns the five-node minimal-support quartic divided-difference controls and exact `W_1`. Extra nodes, different cancellation order, different transport metric, or signed/unnormalized source classes are not covered.
- **No rational-prime or RH conclusion.** This is a control-class theorem about when a compressed Euler observation faithfully inherits a local homogeneous optimizer.

## Consequence for the line

The accepted quartic localization clue can be resolved as **supported and narrowed**. A natural profile-capped source class does transfer the certified homogeneous optimizer to the full fixed-band Euler objective, with uniform `O(\delta)` objective control and `O(\sqrt\delta)` projective shape convergence. The unrestricted problem remains negatively settled by AF-200: full-Euler smallness does not itself retain the profile/localization resource needed for optimizer identity.
