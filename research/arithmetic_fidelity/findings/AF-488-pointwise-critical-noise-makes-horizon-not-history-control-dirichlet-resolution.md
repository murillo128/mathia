# AF-488 — Pointwise critical noise makes horizon, not history, control Dirichlet resolution

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SAMPLING`, `MINIMAX-RESOLUTION`, `ACCUMULATED-HISTORY`, `SHARP-RATE`, `DETERMINISTIC-LINF`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

For the one-generator local Dirichlet family used in AF-487, accumulating arbitrarily many earlier rightward samples does **not** improve the `Theta(1/t)` minimax resolution of the moving generator when the noise budget is pointwise and scaled to the local generator amplitude.

More precisely, fix

\[
F_q(s)=G(s)+a_J q^{-s},\qquad q\in I=[q_-,q_+],
\]

where `a_J>0`, `I` is compactly contained in `(q_{J-1},q_{J+1})`, all other source data are fixed, and the real sampling half-line lies in the absolute-convergence region. Let

\[
W_t=\{t,t+h,\ldots,t+(2J-2)h\}
\]

be the AF-487 terminal window. For each sufficiently large `t`, let `S_t` be any observation set — finite, growing, countably infinite, or a continuum — satisfying

\[
W_t\subseteq S_t\subseteq [s_*,H_t],
\qquad 0<s_*<t,
\qquad t+(2J-2)h\le H_t\le A t
\]

for one fixed `A<infinity`. The observed datum is

\[
y(s)=F_q(s)+\eta(s),\qquad s\in S_t,
\]

with one coherent error process obeying the pointwise critical-scale budget

\[
|\eta(s)|\le \varepsilon q^{-s}\qquad(s\in S_t).
\]

Let `R_t(S_t)` be the deterministic minimax error for estimating `log q` from this whole observation. Under the same uniform small-noise conditioning hypothesis on `epsilon` used by AF-487 for its terminal-window upper bound, there are constants `0<c<=C<infinity`, independent of `t` and of the cardinality or density of `S_t`, such that

\[
\frac{c}{t}\le R_t(S_t)\le \frac{C}{t}
\]

for all sufficiently large `t`.

Thus a full accumulated prefix, including the continuum experiment `S_t=[s_*,H_t]`, has the same asymptotic resolution order as one terminal `2J-1` sample window whenever its rightmost horizon remains `O(t)`. At this critical noise geometry, **sample history is not an additional asymptotic fidelity resource; the furthest-right horizon is**.

## Upper bound: discard the history

Because `W_t` is contained in `S_t`, an estimator may ignore every earlier sample. For `s=t+kh` in `W_t`,

\[
|\eta(s)|\le \varepsilon q^{-s}\le \varepsilon q^{-t}
\]

since `q>1` and `s>=t`. Therefore the entire AF-487 terminal-window argument applies unchanged. Under its conditioning gate, the moving Hankel/Prony reconstruction gives

\[
|\log \widehat q-\log q|\le \frac{C}{t}
\]

uniformly for `q in I` and all admissible pointwise errors. Hence

\[
R_t(S_t)\le C/t.
\]

No use of the accumulated history is required for this direction.

## Lower bound: one coherent perturbation shadows the whole prefix

Fix an interior point `q_0 in int(I)`. Let `gamma>0` satisfy

\[
a_J(e^\gamma-1)\le \varepsilon.
\]

For example, any

\[
0<\gamma\le \log(1+\varepsilon/a_J)
\]

works. Define the nearby alternative

\[
q_1(t)=q_0\exp(\gamma/H_t).
\]

For all sufficiently large `t`, `q_1(t)` still lies in `I`. Consider the datum with no noise under `q_0`,

\[
y_t(s)=F_{q_0}(s),\qquad s\in S_t.
\]

The same datum can be interpreted under `q_1(t)` with the **single coherent error function**

\[
\eta_t(s)=F_{q_0}(s)-F_{q_1(t)}(s).
\]

Because only the `J`th generator moves,

\[
\eta_t(s)
=a_J q_0^{-s}\left(1-e^{-\gamma s/H_t}\right).
\]

Relative to the admissible budget for the alternative source,

\[
\frac{|\eta_t(s)|}{q_1(t)^{-s}}
=a_J\left(e^{\gamma s/H_t}-1\right).
\]

Every observed abscissa satisfies `0<s<=H_t`, so

\[
a_J\left(e^{\gamma s/H_t}-1\right)
\le a_J(e^\gamma-1)
\le \varepsilon.
\]

Therefore `eta_t` is admissible **simultaneously at every sample in the accumulated history**. The construction does not assign independent errors to overlapping windows; it is one globally defined error process on the entire observation set. In fact the same proof works if every real point of `[s_*,H_t]` is observed.

The two admissible explanations of the identical datum have parameter separation

\[
|\log q_1(t)-\log q_0|=\frac{\gamma}{H_t}.
\]

Any estimator must therefore make error at least half this separation on one of the two explanations:

\[
R_t(S_t)\ge \frac{\gamma}{2H_t}
\ge \frac{\gamma}{2A}\frac1t.
\]

This gives the matching `Omega(1/t)` lower bound.

## Horizon form of the obstruction

The proof isolates a slightly more general resource law. If the rightmost observed abscissa is `H` and the error envelope remains

\[
|\eta(s)|\le \varepsilon q^{-s},
\]

then the same two-point construction with `q_1=q_0 exp(gamma/H)` gives a local minimax obstruction of order `1/H`, regardless of how many samples are placed before `H`.

Consequently, adding denser history inside a fixed horizon cannot defeat the obstruction. To change the order one must change at least one of the actual resources: push the observation horizon farther right, strengthen the noise geometry, add source restrictions/marks, or exploit another channel not contained in the pointwise critical-noise experiment.

For the clue's original expanding prefix `H_t=t+O(1)`, this becomes exactly the `Theta(1/t)` law.

## Why accumulation fails here

The critical envelope tracks the amplitude of the moving atom at **each** observation location. Earlier observations are larger in absolute magnitude, but their allowed perturbations enlarge by the same factor. Moving the generator by `Delta log q=gamma/H_t` changes its contribution at location `s` by the relative factor

\[
e^{\gamma s/H_t}-1,
\]

which remains uniformly bounded across the whole prefix. Thus the extra observations do not create independent constraints against the adversarial perturbation: one analytic difference function shadows all of them at once.

This separates **cardinality/density of observations** from **rightward depth**. The former can grow without changing the minimax exponent in this model; the latter directly controls the largest relative phase/slope separation generated by a fixed perturbation in `log q`.

## Falsification and boundary audit

The conclusion depends on the experiment, not merely on the source family.

- The noise is deterministic and pointwise adversarial. Independent stochastic errors can average with sample count and are a different experiment.
- The budget is local-source-relative, `epsilon q^{-s}`. If every early observation instead had an absolute error floor scaled to the *terminal* depth, such as `epsilon q^{-t}`, then early samples would have much higher effective signal-to-noise ratio and this lower bound would not apply.
- A global norm or total-energy budget couples the errors across samples and may make accumulation useful. The proof uses only separate pointwise bounds.
- The theorem assumes the accumulated horizon is at most a fixed multiple of `t`. If `H_t/t -> infinity`, the lower bound becomes `Omega(1/H_t)` rather than `Omega(1/t)`; extending the horizon is precisely the resource the proof identifies.
- The lower bound itself holds for every `epsilon>0`. The matching `O(1/t)` upper bound retains AF-487's uniform conditioning gate because it is inherited from that reconstruction theorem.
- The theorem concerns the unmarked continuum parameter `q`. As in AF-487, a discrete candidate set or external arithmetic mark can convert a shrinking `O(1/t)` interval into eventual exact identification once candidate spacing dominates that interval.

The error process used in the lower bound is not a collection of unrelated noise values: it is the analytic function `F_{q_0}-F_{q_1}` restricted to the observation set. Therefore merely requiring cross-window consistency, continuity, or analyticity of the perturbation does not kill this particular obstruction. Stronger quantitative regularity or a different norm could.

## Prior-art and novelty audit

The surrounding inverse-problem mathematics is classical.

- Dmitry Batenkov and Yosef Yomdin, **“On the Accuracy of Solving Confluent Prony Systems,”** *SIAM Journal on Applied Mathematics* 73(1), 134–154 (2013), DOI `10.1137/110836584`, studies maximal local accuracy and stability of Prony-type inversion under measurement error. AF-486 and AF-487 already place the moving Dirichlet window inside this classical Prony/Hankel setting.
- David L. Donoho, **“Statistical Estimation and Optimal Recovery,”** *Annals of Statistics* 22(1), 238–270 (1994), develops the classical modulus-of-continuity viewpoint in which indistinguishable nearby objects control minimax estimation difficulty. Its statistical model is not the deterministic pointwise envelope used here, so it is language and methodology prior art rather than a direct theorem for this channel.
- Ankur Moitra, **“Super-resolution, Extremal Functions and the Condition Number of Vandermonde Matrices,”** STOC 2015, 821–830, DOI `10.1145/2746539.2746561`, is neighboring prior art on resolution and conditioning for Vandermonde inversion.

No novelty is claimed for Prony reconstruction, Vandermonde conditioning, or the generic two-point minimax/optimal-recovery argument. The Arithmetic Fidelity contribution is the channel-specific composition: for the AF-486/AF-487 moving Dirichlet source, a single source-relative perturbation shadows **every observation in an arbitrarily dense accumulated rightward prefix**, proving that history cardinality cannot improve the inverse-depth rate while the rightmost horizon remains `Theta(t)`.

## Relationship to AF-486 and AF-487

AF-486 identified the exponentially shrinking **absolute precision** required to retain a fixed Dirichlet depth. AF-487 then showed that, exactly at that critical scale, a fixed terminal window has only `Theta(1/t)` **generator resolution** in logarithmic coordinates.

AF-488 closes the history loophole left explicitly open by AF-487. Once the noise is specified pointwise at the local critical atom scale, retaining all earlier samples — even continuously — does not change the order. The next meaningful escape cannot be “keep more of the same prefix”; it must alter horizon, noise coupling, side information, or source class.
