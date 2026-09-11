# AF-264 — Balanced zero replacement preserves the first endpoint jet

**Status:** `EXACT-DERIVED`, `ARITHMETIC-FIDELITY`, `MATCHED-CONTROL`, `ZERO-SURGERY`, `NEGATIVE/OBSTRUCTION`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-263 shows that order one, Riemann reflection/conjugation symmetry, endpoint values, critical-strip zero location, and the leading Riemann--von Mangoldt zero count do not control the Keiper phase strongly enough: a finite symmetric zero insertion can realize any prescribed positive profinite cancellation level. Its main untested escape was local normalization beyond the endpoint values.

The first endpoint derivative still does not close that escape once the matched-control class allows **balanced replacement** rather than addition-only surgery.

Let

\[
\tau=\frac12+iT,
\qquad T>0,
\tag{1}
\]

be any nontrivial zero of `xi` on the critical line, and set

\[
Q_\tau(s)=(s-\tau)(s-\overline\tau).
\tag{2}
\]

For an off-critical point

\[
\rho=\beta+i\gamma,
\qquad \frac12<\beta<1,
\qquad \gamma>0,
\tag{3}
\]

write

\[
P_\rho(s)
=(s-\rho)(s-\overline\rho)
(s-(1-\rho))(s-(1-\overline\rho)).
\tag{4}
\]

Define the positive endpoint charges

\[
\mathcal J_2(T)
:=-\frac{Q_\tau'(0)}{Q_\tau(0)}
=\frac{1}{T^2+1/4},
\tag{5}
\]

and

\[
\mathcal J_4(\beta,\gamma)
:=-\frac{P_\rho'(0)}{P_\rho(0)}
=2\left(
\frac{\beta}{\beta^2+\gamma^2}
+
\frac{1-\beta}{(1-\beta)^2+\gamma^2}
\right)>0.
\tag{6}
\]

Then for every fixed `beta in (1/2,1)`, every prescribed

\[
c\in[0,+\infty],
\tag{7}
\]

and every height threshold `H`, one can choose a target quartet `rho=beta+i gamma` with

\[
\gamma>H,
\qquad
K_{\mathrm{pc}}(\alpha_\rho)=c,
\qquad
\alpha_\rho=\frac{\theta_\rho}{\pi},
\tag{8}
\]

and an auxiliary off-critical quartet

\[
\eta=\beta_0+i u,
\qquad \beta_0\in(1/2,1),
\tag{9}
\]

such that

\[
\boxed{
\mathcal J_4(\beta,\gamma)
+
\mathcal J_4(\beta_0,u)
=
\mathcal J_2(T).
}
\tag{10}
\]

Consequently the function

\[
\boxed{
F(s)
=
\frac{Q_\tau(0)}{P_\rho(0)P_\eta(0)}
P_\rho(s)P_\eta(s)
\frac{\xi(s)}{Q_\tau(s)}
}
\tag{11}
\]

is entire of order one, satisfies

\[
F(1-s)=F(s),
\qquad
F(\overline s)=\overline{F(s)},
\tag{12}
\]

has all of its zeros in the open critical strip, and preserves not only the endpoint values but the full first endpoint jets:

\[
\boxed{
F(0)=\xi(0),
\quad
F'(0)=\xi'(0),
\quad
F(1)=\xi(1),
\quad
F'(1)=\xi'(1).
}
\tag{13}
\]

Its zero divisor differs from that of `xi` by removing one copy of the critical-line pair `tau, overline(tau)` and adding the two off-critical quartets attached to `rho` and `eta`. Hence

\[
N_F(Y)=N_\xi(Y)+O(1),
\tag{14}
\]

with the same leading Riemann--von Mangoldt asymptotic.

The target quartet retains the arbitrarily prescribed AF-261 profinite cancellation obstruction `(8)`. For every finite `c>0`, the target can additionally be placed so high that

\[
\boxed{c>\log q_\rho,}
\tag{15}
\]

so its periodically-complete one-pair root rate remains strictly subunit:

\[
q_\rho e^{-c}<1.
\tag{16}
\]

Thus **endpoint value plus first derivative is still too compressed to exclude the dangerous Keiper phases**. The local first jet detects pure zero addition, but it can be neutralized exactly by replacing a small amount of existing critical-line zero charge with off-critical charge.

## Why it matters

AF-263 left open a concrete possibility: perhaps one or a few local derivatives of the completed function carry enough extra information to distinguish the true `xi` source from its finite symmetric zero-insertion controls. Equation `(13)` rules out the first nontrivial version of that idea.

There is a useful structural distinction. For addition-only surgery, the endpoint logarithmic derivative has a strict sign: every inserted quartet contributes the positive charge `(6)`, so after normalization at `s=0` the derivative necessarily moves. In that restricted control class, one extra scalar really does detect the surgery.

But that apparent rigidity is not intrinsic to the first jet. Once the control is allowed to remove one already-present symmetric critical-line pair and add two off-critical quartets, the observable sees only the **net reciprocal-zero charge**. Equation `(10)` makes that scalar exactly zero while leaving one target phase free to carry any AF-261 profinite cancellation level.

This is the same fidelity pattern in a sharper arithmetic setting: a low-dimensional local observable can reject a one-sided perturbation cone yet remain non-faithful on the natural signed replacement fiber. The next source restriction cannot be justified merely by saying that AF-263 failed to preserve derivatives; it has to consume more than this first reciprocal-zero moment.

## Exact derivation

### 1. Endpoint charge of a symmetric critical-line pair

Because `tau=1/2+iT` lies on the critical line,

\[
1-\tau=\overline\tau,
\tag{17}
\]

so `Q_tau(1-s)=Q_tau(s)` and `Q_tau` is conjugation-invariant. Its logarithmic derivative at zero is

\[
\frac{Q_\tau'(0)}{Q_\tau(0)}
=-\left(\frac1\tau+\frac1{\overline\tau}\right).
\tag{18}
\]

Since

\[
\frac1\tau+\frac1{\overline\tau}
=2\Re\frac1\tau
=\frac{1}{T^2+1/4},
\tag{19}
\]

we obtain `(5)`.

Hardy's theorem gives infinitely many nontrivial zeros on the critical line, so at least one such pair is available without assuming RH or simplicity. If its multiplicity exceeds one, division by `Q_tau` below removes only one copy.

### 2. Every off-critical quartet carries a strictly positive endpoint charge

For the quartet polynomial `(4)`, symmetry of the root set gives

\[
P_\rho(1-s)=P_\rho(s),
\qquad
P_\rho(\overline s)=\overline{P_\rho(s)}.
\tag{20}
\]

At zero,

\[
-\frac{P_\rho'(0)}{P_\rho(0)}
=
\sum_{z\in\{\rho,\overline\rho,1-\rho,1-\overline\rho\}}
\frac1z,
\tag{21}
\]

and pairing conjugates gives exactly `(6)`. Both terms are positive for `0<beta<1`, so

\[
\mathcal J_4(\beta,\gamma)>0.
\tag{22}
\]

For fixed `beta`, it is continuous and strictly decreasing in `gamma>0`, because

\[
\frac{\partial}{\partial\gamma}
\mathcal J_4(\beta,\gamma)
=-4\gamma\left(
\frac{\beta}{(\beta^2+\gamma^2)^2}
+
\frac{1-\beta}{((1-\beta)^2+\gamma^2)^2}
\right)<0.
\tag{23}
\]

Moreover

\[
\mathcal J_4(\beta,\gamma)
<\frac{2}{\gamma^2}
\longrightarrow0.
\tag{24}
\]

This already shows the addition-only statement. If

\[
M(s)=\prod_{j=1}^m\frac{P_{\rho_j}(s)}{P_{\rho_j}(0)},
\tag{25}
\]

then `M(0)=1` but

\[
\frac{M'(0)}{M(0)}
=-\sum_{j=1}^m\mathcal J_4(\rho_j)<0
\tag{26}
\]

for every nonempty finite family. So the first endpoint derivative does detect pure finite addition inside the strip.

### 3. Put an arbitrarily dangerous target above the charge scale

Fix the critical-line pair `(1)` and hence the positive budget `J_2(T)`. AF-261 supplies irrational phases with every prescribed value `c` in `(7)`, and AF-263 pulls those phases back to off-critical zero coordinates at arbitrarily large height while keeping any fixed `beta in (1/2,1)`.

Choose the target height so large that

\[
\gamma
>
\max\left\{H,\sqrt{\frac{2}{\mathcal J_2(T)}}\right\}.
\tag{27}
\]

Then `(24)` gives

\[
0<\mathcal J_4(\beta,\gamma)<\mathcal J_2(T).
\tag{28}
\]

For finite `c>0`, AF-263 also allows the height to be increased until `log q_rho<c`, because `q_rho->1` as `gamma->infinity` at fixed `beta`. This gives `(15)`--`(16)` without changing the prescribed profinite exponent.

### 4. One auxiliary quartet balances the first reciprocal-zero moment

Let

\[
R:=\mathcal J_2(T)-\mathcal J_4(\beta,\gamma)>0.
\tag{29}
\]

Fix, for definiteness,

\[
\beta_0=\frac34.
\tag{30}
\]

The map

\[
u
\mapsto
\mathcal J_4\left(\frac34,u\right)
\tag{31}
\]

is continuous and strictly decreasing from

\[
\mathcal J_4\left(\frac34,0\right)
=2\left(\frac{4}{3}+4\right)
=\frac{32}{3}
\tag{32}
\]

to zero. On the other hand every `T>0` gives

\[
0<R<\mathcal J_2(T)<4<\frac{32}{3}.
\tag{33}
\]

The intermediate value theorem therefore gives a unique `u>0` such that

\[
\mathcal J_4\left(\frac34,u\right)=R.
\tag{34}
\]

With `eta=3/4+i u`, equations `(29)` and `(34)` prove the balance law `(10)`.

### 5. The balanced quotient is entire and preserves the first endpoint jet

Because `tau` and `overline(tau)` are zeros of `xi`, each with multiplicity at least one,

\[
\frac{\xi(s)}{Q_\tau(s)}
\tag{35}
\]

is entire. Removing and adding finitely many polynomial factors does not change order one. Every factor in `(11)` is invariant under `s -> 1-s` and under conjugation in the appropriate real-entire sense, so `(12)` follows.

At the endpoints, reflection gives

\[
Q_\tau(1)=Q_\tau(0),
\qquad
P_\rho(1)=P_\rho(0),
\qquad
P_\eta(1)=P_\eta(0).
\tag{36}
\]

The scalar prefactor in `(11)` therefore makes

\[
F(0)=\xi(0),
\qquad
F(1)=\xi(1).
\tag{37}
\]

Near `s=0`, the quotient `F/xi` is analytic and nonzero. Its logarithmic derivative is

\[
\frac{d}{ds}\log\frac{F}{\xi}
=
\frac{P_\rho'}{P_\rho}
+
\frac{P_\eta'}{P_\eta}
-
\frac{Q_\tau'}{Q_\tau}.
\tag{38}
\]

At zero, equations `(5)`, `(6)`, and `(10)` give

\[
\left.\frac{d}{ds}\log\frac{F}{\xi}\right|_{s=0}
=-\mathcal J_4(\rho)-\mathcal J_4(\eta)+\mathcal J_2(T)
=0.
\tag{39}
\]

Since `F(0)=xi(0) != 0`, equation `(39)` implies

\[
F'(0)=\xi'(0).
\tag{40}
\]

Reflection differentiates to `F'(1-s)=-F'(s)` and likewise for `xi`; hence `(40)` also gives

\[
F'(1)=\xi'(1).
\tag{41}
\]

This proves the full first-jet identity `(13)`.

### 6. The zero-set and counting controls remain coarse-equivalent

Division by `Q_tau` removes one copy of the pair `tau, overline(tau)`. The two numerator quartet factors add eight zeros, four in the upper half-plane and four in the lower half-plane, all with real parts strictly between zero and one. No poles are introduced because the denominator was canceled by genuine `xi` zeros.

Thus the zero-count difference is bounded uniformly in height and eventually equals `+3` in the upper half-plane: one upper critical-line zero was removed and four upper off-critical zeros were added. In particular the leading Riemann--von Mangoldt asymptotic is unchanged, establishing `(14)`.

The target zero `rho` itself is untouched by the balancing operation, so its AF-261 invariant remains exactly `c`. This completes the construction.

## Prior-art audit

The analytic ingredients are classical. G. H. Hardy, **“Sur les Zéros de la Fonction zeta(s) de Riemann,”** *Comptes Rendus de l'Académie des Sciences de Paris* 158 (1914), 1012--1014, proved that infinitely many nontrivial zeta zeros lie on the critical line. This supplies the sacrificial pair `tau, overline(tau)` without any RH assumption.

The order-one entire nature of `xi`, its reflection and conjugation symmetries, and its Hadamard zero-product framework are standard; the line's source ledger already records Titchmarsh--Heath-Brown and the *Encyclopedia of Mathematics* xi entry for these facts under AF-018. Finite insertion or removal of known polynomial zero factors, and the identity between logarithmic derivatives and reciprocal-root power sums, are elementary consequences of polynomial/Hadamard factorization. No novelty is claimed for any of those ingredients.

The new content is deliberately narrower. AF-263 produced a matched analytic control with arbitrary profinite Keiper cancellation but left all endpoint derivatives unconstrained. AF-264 shows that the **first** such derivative does not repair fidelity once one moves from a positive insertion cone to a signed replacement fiber: one existing critical-line pair supplies a positive reciprocal-zero budget, and one auxiliary off-critical quartet balances that budget exactly while an independently chosen target quartet retains arbitrary AF-261 cancellation.

This is not a converse theorem and does not compete with Hamburger/Hecke/Weil rigidity. Those theories add substantially stronger Dirichlet-series or automorphic input. The result instead identifies why one extra local scalar is still below that source-information boundary.

## Boundaries

**Not an L-function control.** The function `F` need not be the completion of an ordinary Dirichlet series, Euler product, or arithmetic local-factor system. As in AF-263, the theorem rules out a proposed analytic/local normalization layer, not the stronger arithmetic categories that may ultimately constrain the real zeta phases.

**Only the first endpoint jet is matched.** No claim is made that `F''(0)=xi''(0)` or that an arbitrary finite jet can be preserved. Higher reciprocal-zero moments may impose additional independent constraints. The present theorem says only that the first derivative is not the missing discriminator.

**Replacement is essential.** Addition-only finite surgery cannot preserve the first derivative because of the strict positivity `(22)`--`(26)`. The failure appears when the admissible source class contains signed divisor changes: removing an existing pair releases exactly the scalar charge needed to hide new quartets.

**The removed zero need not be simple.** Division by `Q_tau` removes one copy from each conjugate critical-line zero. Multiplicity greater than one leaves the remaining copies intact.

**The auxiliary quartet is not claimed arithmetic.** Its sole role is to balance the first reciprocal-zero moment. The theorem intentionally tests whether the retained observable distinguishes the source; an arbitrary matched control is legitimate at this analytic layer precisely because no stronger arithmetic category has yet been imposed.

**One-pair cancellation only.** The dangerous inequality `(16)` concerns the target conjugate Keiper pair in the AF-258/AF-261 sense. It does not assert the full Li sequence of `F` has a particular asymptotic after all zero contributions interact.

## Research consequence

AF-263 showed that the coarse completed-function layer is non-faithful. AF-264 now closes its most immediate local repair: preserving `xi(0)` and `xi'(0)` (and therefore the reflected data at `1`) still leaves matched functions containing an arbitrarily dangerous off-critical Keiper phase.

The next useful source condition must therefore be genuinely stronger than a first local jet. Two qualitatively different possibilities remain live:

1. a richer family of reciprocal-zero moments/local jets whose admissible replacement fibers can be shown to exclude AF-261 phase engineering; or
2. nonlocal arithmetic structure -- Dirichlet-series coefficients, Euler-product positivity/local factors, explicit-formula coefficient identities, or an equivalent source constraint -- that is not reproducible by balanced finite divisor surgery.

The decisive test remains quantitative: the retained structure must imply

\[
K_{\mathrm{pc}}(\alpha_\rho)<\log q_\rho
\]

for every hypothetical off-critical **actual zeta zero**, not merely distinguish one convenient surgery model.