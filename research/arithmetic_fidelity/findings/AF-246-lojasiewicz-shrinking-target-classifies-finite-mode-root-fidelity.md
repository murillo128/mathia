# AF-246 — Łojasiewicz shrinking targets classify finite-mode root fidelity

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `CLASSICAL-STRUCTURE`, `RH-SUFFICIENT-QUOTIENT`, `OUTPUT-SAMPLING`, `RATE-SENSITIVE-OBSERVABILITY`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-245 classifies the stronger requirement that a retained index set observe every finite unit-circle exponential mode with a positive asymptotic amplitude. For preserving an exponential **root rate**, positive amplitude is more than is needed. The exact mode-specific condition is only that the retained orbit not approach the mode's zero set at an exponential rate along every surviving subsequence.

Let

\[
F(n)=\sum_{j=1}^m c_j u_j^n,
\qquad |u_j|=1,
\tag{1}
\]

with distinct `u_j` and not all `c_j` zero. Put

\[
\Phi_U(n)=(u_1^n,\ldots,u_m^n)\in\mathbb T^m,
\qquad
H_U=\overline{\Phi_U(\mathbb Z)},
\tag{2}
\]

and let

\[
P_U(z_1,\ldots,z_m)=\sum_{j=1}^m c_jz_j.
\tag{3}
\]

Then `H_U` is a compact Lie subgroup of the torus and `F(n)=P_U(\Phi_U(n))`. Define the zero target

\[
Z_F=\{x\in H_U:P_U(x)=0\}.
\tag{4}
\]

Choose any fixed Riemannian or ambient torus metric on `H_U`, and define

\[
\delta_F(n)=
\begin{cases}
\min\{1,\operatorname{dist}(\Phi_U(n),Z_F)\},&Z_F\ne\varnothing,\\
1,&Z_F=\varnothing.
\end{cases}
\tag{5}
\]

For every unbounded `S\subset\mathbb N`, set

\[
\tau_F(S)
:=
\liminf_{\substack{n\to\infty\\n\in S}}
\frac{-\log\delta_F(n)}{n}
\in[0,\infty].
\tag{6}
\]

Then there is a constant `\nu_F\ge1` such that

\[
\tau_F(S)
\le
-\log\!\left(
\limsup_{\substack{n\to\infty\\n\in S}}|F(n)|^{1/n}
\right)
\le
\nu_F\tau_F(S),
\tag{7}
\]

with `-\log 0=+\infty`. In particular,

\[
\boxed{
\limsup_{\substack{n\to\infty\\n\in S}}|F(n)|^{1/n}=1
\iff
\tau_F(S)=0.
}
\tag{8}
\]

Thus finite-mode root fidelity is a **shrinking-target property in the finite torus quotient actually seen by that mode**. The retained indices may drive `F(n)` all the way to zero in ordinary amplitude; root fidelity survives provided the closest retained approaches are only subexponentially small in the index.

More generally, if

\[
a_n=q^nF(n)+r_n,
\qquad q>1,
\qquad
\limsup_{n\to\infty}|r_n|^{1/n}<q,
\tag{9}
\]

then

\[
\boxed{
\limsup_{\substack{n\to\infty\\n\in S}}|a_n|^{1/n}=q
\iff
\tau_F(S)=0.
}
\tag{10}
\]

Consequently, call `S` **universally finite-mode root-observable** when `\tau_F(S)=0` for every nonzero finite unit-circle exponential polynomial `(1)`. AF-244's Li dominant-mode decomposition then gives

> For every universally finite-mode root-observable `S\subset\mathbb N`, RH is equivalent to
> \[
> \limsup_{\substack{n\to\infty\\n\in S}}|\lambda_n|^{1/n}\le1.
> \tag{11}
> \]

This sharpens the output-side question left by AF-245. Bohr density remains a strong sufficient condition, but the root-rate discriminator itself asks only for zero **exponential shrinking exponent** in each finite phase quotient.

## Why it matters

AF-244 showed that ordinary density is not the resource controlling sparse Li output fidelity. AF-245 replaced density by topological/positive-amplitude observability in the Bohr compactification. AF-246 identifies the weaker quantitative structure actually consumed by the `n`th-root decoder.

The distinction is important. A mode can become arbitrarily small along every retained tail, so that the positive-amplitude criterion of AF-245 fails, while its `n`th root still tends to one because the decay is only polynomial or otherwise subexponential. Conversely, exponentially accurate approaches to the same zero set genuinely lower the observed root rate. The relevant compression resource is therefore not retained density and not even a fixed amplitude margin; it is the **exponential recurrence scale relative to the discriminator's zero locus**.

This also localizes the geometry. A finite mode does not require the full Bohr compactification to measure its rate defect. It factors through the compact finite-dimensional orbit closure `H_U`, and the root-fidelity question becomes a shrinking-target problem there. That gives a concrete geometric object on which quantitative Diophantine or recurrence information can act.

## Derivation / evidence

### 1. The finite mode factors through a compact analytic phase space

The map `n\mapsto\Phi_U(n)` is a homomorphism from `\mathbb Z` into `\mathbb T^m`. Its closure `H_U` is therefore a closed subgroup of a finite-dimensional torus, hence a compact abelian Lie group with finitely many connected components. Equivalently, it is cut out by the integer character relations among the phases `u_j`.

The restriction of `(3)` to `H_U` is real analytic. Because the integer orbit is dense in `H_U`, `P_U|_{H_U}` cannot vanish identically unless `F(n)` is identically zero. The latter is excluded by distinctness of the `u_j` and the usual Vandermonde argument.

This finite quotient is representation-exact for the mode: no information relevant to evaluating `F(n)` is added by replacing the integer sequence with the orbit `\Phi_U(n)` in `H_U`.

### 2. Łojasiewicz converts amplitude decay into distance-to-zero decay

Assume first that `Z_F` is nonempty. Apply the classical Łojasiewicz distance inequality on the compact analytic set `H_U` to the nonnegative real-analytic function

\[
g(x)=|P_U(x)|^2.
\tag{12}
\]

There exist constants `A>0` and `\nu>0` such that

\[
|P_U(x)|\ge A\,\operatorname{dist}(x,Z_F)^\nu
\tag{13}
\]

for `x` sufficiently close to `Z_F`. Increasing `\nu` if necessary lets us take `\nu\ge1`, and compactness lets the constant be adjusted so that, after truncating distance at one as in `(5)`,

\[
|P_U(x)|\ge A'\delta(x)^\nu
\qquad(x\in H_U).
\tag{14}
\]

On the other hand `P_U|_{H_U}` is Lipschitz on the compact Lie group, and it vanishes on `Z_F`, so

\[
|P_U(x)|\le B\operatorname{dist}(x,Z_F)
\le B'\delta(x)
\tag{15}
\]

for suitable constants after the same compact adjustment away from the zero set.

If `Z_F` is empty, compactness gives `\min_{H_U}|P_U|>0`; with `\delta\equiv1`, the same two-sided form holds trivially.

Evaluating `(14)`--`(15)` on `x=\Phi_U(n)` gives

\[
A'\delta_F(n)^\nu
\le |F(n)|\le
B'\delta_F(n).
\tag{16}
\]

Take logarithms, divide by `n`, and then take the lower limit along `S`. Since the constants disappear after division by `n`, `(16)` yields exactly `(7)`. In particular the amplitude root has no exponential defect if and only if the orbit has no exponential shrinking-target defect, proving `(8)`.

The zero/nonzero conclusion is independent of the chosen smooth ambient metric: on compact `H_U`, any two such metrics are bi-Lipschitz equivalent, and fixed multiplicative constants vanish at the `1/n` logarithmic scale.

### 3. Root-observable modes exactly preserve a separated dominant exponential rate

Let

\[
\theta_S(F)
:=
\limsup_{\substack{n\to\infty\\n\in S}}|F(n)|^{1/n}
\le1.
\tag{17}
\]

If `\theta_S(F)<1`, choose `\eta` with

\[
\limsup|r_n|^{1/n}<\eta<q.
\tag{18}
\]

Then the two terms in `(9)` have restricted root rates at most `q\theta_S(F)<q` and `\eta<q`, respectively, so

\[
\limsup_{\substack{n\to\infty\\n\in S}}|a_n|^{1/n}<q.
\tag{19}
\]

If `\theta_S(F)=1`, fix arbitrarily small `\varepsilon>0` with `qe^{-\varepsilon}>\eta`. Infinitely many `n\in S` satisfy

\[
|F(n)|\ge e^{-\varepsilon n}.
\tag{20}
\]

Along those indices, for all sufficiently large `n`,

\[
|a_n|
\ge q^ne^{-\varepsilon n}-\eta^n
\ge \frac12(qe^{-\varepsilon})^n.
\tag{21}
\]

Hence the restricted root limsup is at least `qe^{-\varepsilon}`. Letting `\varepsilon\downarrow0` gives the lower bound `q`; boundedness of `F` and `(9)` give the matching upper bound. Combining this with `(8)` proves `(10)`.

This step also shows why positive-amplitude observability is unnecessarily strong. The dominant term need only beat the exponentially separated remainder along an infinite retained subsequence; any subexponential loss in its phase amplitude is harmless to the final root rate.

### 4. A concrete mode loses every fixed amplitude margin but keeps full root rate

Let

\[
\alpha=\frac{\sqrt5-1}{2},
\qquad
u=e^{2\pi i\alpha},
\qquad
F(n)=1-u^n.
\tag{22}
\]

Let `q_k` be the Fibonacci denominators of the continued-fraction convergents of `\alpha`, so `q_k=F_k` in the usual Fibonacci notation. The exact continued-fraction relation gives

\[
\|q_k\alpha\|\asymp q_k^{-1},
\tag{23}
\]

and therefore

\[
|1-e^{2\pi iq_k\alpha}|\asymp q_k^{-1}.
\tag{24}
\]

For the retained set

\[
S=\{q_k:k\ge1\},
\tag{25}
\]

we have

\[
|F(q_k)|\longrightarrow0,
\tag{26}
\]

so this mode has no positive asymptotic amplitude along `S`. Nevertheless

\[
|F(q_k)|^{1/q_k}\longrightarrow1,
\tag{27}
\]

because `\log q_k/q_k\to0`. In the one-dimensional phase quotient, the orbit approaches the zero target `{1}` only at polynomial scale, hence `\tau_F(S)=0`.

Thus the positive-amplitude condition used in AF-245 is genuinely stronger than needed for this root-rate decoder at the level of an individual finite mode. This example does **not** claim that the Fibonacci index set is universally finite-mode root-observable; it isolates the rate distinction for one exact mode.

### 5. Exponential recurrence is the actual failure mechanism

The converse geometry is equally concrete. If a retained subsequence satisfies

\[
\delta_F(n)\le e^{-cn}
\tag{28}
\]

for all sufficiently large retained `n` and some `c>0`, then `(15)` gives an exponential amplitude loss. More generally `(7)` shows that any positive shrinking exponent `\tau_F(S)>0` forces

\[
\limsup_{\substack{n\to\infty\\n\in S}}|F(n)|^{1/n}<1.
\tag{29}
\]

Such behavior is possible for irrational rotations with sufficiently extreme Diophantine approximation: continued-fraction partial quotients can be chosen so that selected denominators approach a target at exponentially small scales. Therefore topological recurrence alone cannot guarantee root fidelity for arbitrary phase systems; the recurrence rate must be controlled.

Exact zeros are the limiting case `\delta_F(n)=0`. For finite exponential modes their index set is governed by the classical Skolem--Mahler--Lech theorem: the exact zero indices form a finite set plus finitely many arithmetic progressions. AF-245's periodic-aliasing audit captures this exact-zero obstruction, while AF-246 adds the distinct near-zero obstruction at exponential scale.

## Li-coefficient consequence

AF-244 establishes the analytic input needed here. If RH is false, the nearest poles in the open unit disk of the Keiper--Li generating function produce

\[
\lambda_n=q^nF(n)+r_n,
\qquad q>1,
\qquad
\limsup |r_n|^{1/n}<q,
\tag{30}
\]

for one fixed nonzero finite unit-circle exponential mode `F` determined by the finitely many nearest pole phases.

For that actual off-RH dominant mode, `(10)` says precisely:

\[
\boxed{
\text{the sampled Li sequence retains the off-RH root rate }q
\iff
\tau_F(S)=0.
}
\tag{31}
\]

Because the off-RH phases are not known in advance, a phase-agnostic sufficient condition on `S` is universal finite-mode root observability. Under that condition an off-RH dominant mode cannot be hidden by the sampling geometry, whereas under RH the unrestricted Li root limsup is at most one and every subsequence inherits that upper bound. This proves `(11)`.

The theorem therefore separates three output-sampling levels:

\[
\text{Bohr/positive-amplitude observability}
\Longrightarrow
\text{subexponential root observability}
\Longrightarrow
\text{preservation of the separated Li dominant root rate}.
\tag{32}
\]

The first implication is strict for individual modes by `(22)`--`(27)`. Whether a clean, substantially weaker **universal** sampling class can be characterized without quantifying over all finite modes remains open.

## Prior-art audit

The mathematical ingredients behind the new rate formulation are classical or have close established analogues.

Stanisław Łojasiewicz, **“Sur le problème de la division,”** *Studia Mathematica* 18 (1959), 87--136, DOI `10.4064/sm-18-1-87-136`, is a primary source for the analytic inequalities that underlie distance-to-zero power bounds. Standard modern real-algebraic treatments include Jacek Bochnak, Michel Coste, and Marie-Françoise Roy, ***Real Algebraic Geometry***, Springer (1998), DOI `10.1007/978-3-662-03718-8`.

Cătălin I. Cârstea, **“Hölder Stability from Exact Uniqueness for Finite-Dimensional Analytic Inverse Problems,”** arXiv:`2605.06354` (2026), uses a Łojasiewicz distance inequality to convert exact uniqueness of finite-dimensional analytic measurements into Hölder stability. This is particularly close prior art for the general principle that analytic recoverability upgrades to a power-law quantitative relation. No novelty is claimed here for that principle.

The language of exponentially shrinking targets is established in dynamics. Richard Hill and Sanju L. Velani, **“The Shrinking Target Problem for Matrix Transformations of Tori,”** *Journal of the London Mathematical Society* 60 (1999), 381--398, DOI `10.1112/S0024610799007681`, studies toral shrinking targets with the exponential scale measured by `\liminf -\log r_n/n`. Their dynamical setting is different -- expanding toral endomorphisms rather than a retained subsequence of a compact rotation orbit approaching an analytic zero locus -- but the rate parameter is structurally the same one appearing in `(6)`.

Christer Lech, **“A Note on Recurring Series,”** *Arkiv för Matematik* 2 (1953), 417--421, DOI `10.1007/BF02590997`, supplies the characteristic-zero zero-set theorem now known as Skolem--Mahler--Lech. It governs exact zeros of the finite recurrence `(1)` but does not by itself control exponentially small nonzero values.

The Keiper--Li generating-function and off-RH dominant-mode asymptotics are inherited from AF-244 and AF-245 and are not claimed as new here.

A targeted search for Li/Keiper criteria stated through shrinking-target exponents of finite phase quotients, Łojasiewicz distance to the zero loci of dominant Li modes, and equivalent rate-sensitive sparse-subsequence formulations did not locate this exact synthesis. This is not an exhaustive novelty proof. The present result should be read narrowly: **classical analytic distance inequalities identify the exact geometric rate condition consumed by the sparse Li `n`th-root discriminator once the finite dominant mode of AF-244 is fixed.**

## Boundaries / caveats

**Mode-specific versus universal.** Equation `(8)` is exact for each fixed finite mode. The phase-agnostic Li statement `(11)` uses the stronger universal quantifier over all such modes because hypothetical off-RH dominant phases are unknown. AF-246 does not yet characterize that universal class by a simpler intrinsic property of `S`.

**The Łojasiewicz exponent is not the root defect.** Equation `(7)` gives a power-equivalence between amplitude and zero-set distance, enough to decide whether the exponential defect is zero. It does not generally identify the numerical amplitude exponent with `\tau_F(S)` because singular zeros can have higher order.

**Finite-dimensional dominant mode remains essential.** The compact Lie quotient and Łojasiewicz argument apply to a fixed finite exponential polynomial. Infinite co-dominant frequency families, continuous spectral mass, or a mode dimension increasing with `n` require new control.

**Output compression only.** As in AF-244--AF-245, the sampled Li coefficients are assumed already formed. Nothing here lowers the source depth or restores the global cancellation destroyed by the truncated-source mechanisms ruled out in AF-238--AF-243.

**Exact zeros and near-zeros are different obstructions.** Skolem--Mahler--Lech controls the first. Arbitrarily strong Diophantine approximation can create the second even when exact zeros are absent. Any proposed sparse sampling rule must therefore audit both periodic aliasing and exponential near-aliasing.

**No claim that Bohr density is necessary.** AF-245 already avoids that claim. AF-246 further shows that fixed positive amplitude is not necessary for an individual mode's root fidelity, but it does not prove the existence of a non-Bohr-dense set that is root-faithful for every possible finite mode.

## Consequence

The output-side frontier is now more precise. Instead of asking for retained density, thickness, or even positive-amplitude uniqueness as the final resource, one can ask:

> Which sparse index sets have zero exponential shrinking exponent against every zero locus arising from a finite unit-circle exponential polynomial?

That is the exact universal sampling question for the finite dominant modes relevant to the off-RH Li root decoder. It naturally invites quantitative recurrence and Diophantine tools in finite torus quotients rather than further density heuristics.

At the same time, this result reinforces the separation already visible in the line: **output sampling has become geometrically well characterized, while source-access compression remains the harder RH-facing obstruction**. The next valuable advance should either give a genuinely weaker intrinsic sufficient condition for universal root observability, or return to the source side and find a cancellation-coherent way to form enough Li information without essentially linear source depth.