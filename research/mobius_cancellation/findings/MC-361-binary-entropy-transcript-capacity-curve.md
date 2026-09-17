# MC-361 — Binary posterior entropy sharpens the transcript-capacity curve

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-340` converts the reciprocal endpoint's source-phase predictability into a global mutual-information lower bound by two routes: a Pinsker/chi-square estimate for fixed nontrivial dephasing and a Fano estimate near the matched-filter energy floor. Both routes are valid, but neither uses the exact fact that each source variable is binary. The binary posterior entropy gives a single sharper curve that contains both regimes.

Continue the reciprocal endpoint notation

\[
G=\mathbf F_2^R,
\qquad
\Xi=G\setminus\{0\},
\qquad
m=2^R-1,
\]

with `A` uniform on `Xi`, source phases

\[
X_i\in\{-1,+1\},
\qquad
X=(X_1,\ldots,X_R),
\]

source observations `Y_i`, complete transcript `Y=(Y_1,\ldots,Y_R)`, and

\[
b_i(Y_i):=\mathbf E[X_i\mid Y_i],
\qquad
\rho_i^2:=\mathbf E\,b_i(Y_i)^2,
\qquad
\rho^2:=\frac1R\sum_{i=1}^R\rho_i^2.
\tag{1}
\]

Let

\[
h(p):=-p\log p-(1-p)\log(1-p)
\]

be binary entropy in nats, and define

\[
g(z):=h\!\left(\frac{1+\sqrt z}{2}\right),
\qquad 0\le z\le1.
\tag{2}
\]

Then `g` is decreasing and concave, and every admitted architecture satisfies the exact entropy-capacity inequality

\[
\boxed{
H(X\mid Y)\le R\,g(\rho^2)
=R\,h\!\left(\frac{1+\rho}{2}\right).
}
\tag{3}
\]

Equivalently,

\[
\boxed{
I(X;Y)
\ge
H(X)-R\,h\!\left(\frac{1+\rho}{2}\right).
}
\tag{4}
\]

This uses no independence assumption on the source coordinates and no discreteness assumption on the transcript.

Combining `(4)` with the independently derived endpoint inequality of `MC-338`,

\[
\delta(W)\ge
\bigl(1-\rho\sqrt{\mathcal E(W)}\bigr)_+,
\tag{5}
\]

gives a nonlinear information tariff for every bounded-energy dephasing architecture. If

\[
\mathcal E(W)\le C,
\qquad
\delta(W)\le1-\eta,
\qquad C<\infty,
\quad \eta>0,
\tag{6}
\]

then consistency already forces `eta/sqrt(C)<=1`, and with

\[
\tau:=\max\!\left\{\frac1m,\frac{\eta}{\sqrt C}\right\}
\tag{7}
\]

we have

\[
\boxed{
I(X;Y)
\ge
H(X)-R\,h\!\left(\frac{1+\tau}{2}\right).
}
\tag{8}
\]

Writing the exact total-correlation identity from `MC-340` as

\[
H(X)=R h(p_R)-\operatorname{TC}(X),
\qquad
p_R=\frac{m-1}{2m},
\tag{9}
\]

and observing that

\[
h(p_R)=g(m^{-2}),
\]

equation `(8)` becomes

\[
\boxed{
I(X;Y)
\ge
R\bigl(g(m^{-2})-g(\tau^2)\bigr)
-\operatorname{TC}(X).
}
\tag{10}
\]

This strictly sharpens the quadratic/Pinsker floor of `MC-340` whenever the required predictability is non-infinitesimal. Indeed

\[
g'(z)\le-\frac12
\qquad(0\le z<1),
\tag{11}
\]

so for `tau>=1/m`,

\[
g(m^{-2})-g(\tau^2)
\ge
\frac12\left(\tau^2-\frac1{m^2}\right),
\tag{12}
\]

which recovers `MC-340` equation (8) and shows exactly where its Pinsker constant is the tangent approximation to the stronger binary-entropy curve.

At the matched-filter energy floor the improvement is especially simple. If

\[
\mathcal E(W)\le1,
\qquad
\delta(W)\le\varepsilon,
\qquad 0\le\varepsilon\le1,
\tag{13}
\]

then `(5)` gives `rho>=1-epsilon`, and hence

\[
\boxed{
I(X;Y)
\ge
H(X)-R\,h\!\left(\frac{\varepsilon}{2}\right).
}
\tag{14}
\]

`MC-340` obtained instead the valid Fano penalty

\[
R h\!\left(\varepsilon-\frac{\varepsilon^2}{2}\right).
\]

For every `0<epsilon<1`,

\[
\frac\varepsilon2
<
\varepsilon-\frac{\varepsilon^2}{2}
\le\frac12,
\]

so `(14)` is strictly stronger. In the small-error regime the missing-information allowance is asymptotically cut by a factor of two at leading logarithmic order:

\[
h(\varepsilon/2)
\sim
\frac\varepsilon2\log\frac{2e}{\varepsilon},
\qquad
h\!\left(\varepsilon-\frac{\varepsilon^2}{2}\right)
\sim
\varepsilon\log\frac e\varepsilon.
\tag{15}
\]

At `epsilon=0`, `(14)` again gives `I(X;Y)=H(X)`: exact unit-energy dephasing determines the complete source state.

For a discrete transcript with at most `K_R` values, the same argument yields

\[
\boxed{
\log K_R
\ge
H(X)-R\,h\!\left(\frac{1+\tau}{2}\right),
}
\tag{16}
\]

and at unit energy with dephasing error at most `epsilon`,

\[
\boxed{
\log K_R
\ge
H(X)-R h(\varepsilon/2).
}
\tag{17}
\]

No estimate for `M(x)` follows. The result is a finite reciprocal-endpoint admission theorem. Its value is that the endpoint's dephasing error and coefficient energy now determine the strongest transcript-information lower curve obtainable from the already-defined average squared posterior predictability by a purely binary entropy argument, rather than through a local Pinsker or Fano relaxation.

## 1. Conditional entropy is an exact function of the posterior mean

For a binary random variable `X_i in {-1,+1}`, conditioning on `Y_i=y` gives

\[
\mathbf P(X_i=+1\mid Y_i=y)
=
\frac{1+b_i(y)}2.
\]

Therefore

\[
H(X_i\mid Y_i)
=
\mathbf E\,h\!\left(\frac{1+b_i(Y_i)}2\right).
\tag{18}
\]

Binary entropy is symmetric around `1/2`, so the integrand depends only on `b_i^2`:

\[
h\!\left(\frac{1+b}2\right)
=
g(b^2).
\tag{19}
\]

The relevant shape of `g` can be checked directly. Put `r=sqrt(z)`. For `0<z<1`,

\[
g'(z)
=-\frac{\operatorname{artanh}(r)}{2r},
\tag{20}
\]

and

\[
g''(z)
=-\frac{1}{4r^3}
\left(
\frac{r}{1-r^2}-\operatorname{artanh}(r)
\right).
\tag{21}
\]

The bracket is positive for `0<r<1`, because its derivative is

\[
\frac{2r^2}{(1-r^2)^2}>0
\]

and it vanishes at `r=0`. Hence `g''(z)<0`: `g` is strictly concave. Equation `(20)` also gives `g'(0)=-1/2` by continuity and `g'(z)<=-1/2`, proving `(11)`.

Jensen applied to `(18)`--`(19)` now gives

\[
H(X_i\mid Y_i)
\le
 g\!\left(\mathbf E b_i(Y_i)^2\right)
=g(\rho_i^2).
\tag{22}
\]

This scalar inequality is sharp given only the prior mean and `rho_i^2`: whenever `rho_i>=|\mathbf E X_i|`, a two-valued posterior mean `b_i in {+rho_i,-rho_i}` can be mixed with probabilities chosen so that `E b_i=E X_i`. Then `b_i^2=rho_i^2` almost surely and equality holds in Jensen. Thus no stronger scalar entropy upper bound can follow from `rho_i^2` alone.

## 2. The complete transcript obeys the global binary-entropy curve

Since the complete transcript `Y` contains each `Y_i`, conditioning reduces entropy and subadditivity gives

\[
H(X\mid Y)
\le
\sum_{i=1}^R H(X_i\mid Y)
\le
\sum_{i=1}^R H(X_i\mid Y_i).
\tag{23}
\]

Using `(22)` and then concavity of `g`,

\[
H(X\mid Y)
\le
\sum_i g(\rho_i^2)
\le
R g\!\left(\frac1R\sum_i\rho_i^2\right)
=R g(\rho^2),
\]

which proves `(3)` and `(4)`.

The finite source bias is already accounted for. Every source coordinate has mean `-1/m`, so Jensen gives

\[
\rho_i^2\ge\frac1{m^2},
\qquad
\rho\ge\frac1m.
\tag{24}
\]

That is why `(7)` uses the maximum of the intrinsic baseline `1/m` and the dephasing-forced value `eta/sqrt(C)`. No fictitious independence or exactly balanced prior is inserted.

For even `R`, `TC(X)->0`; for odd `R`, `TC(X)->log 2` by `MC-340`. Thus for fixed `C,eta` the parity/puncturing dependence remains only an `O(1)` correction to the linear binary-entropy tariff.

## 3. The Pinsker floor is the small-predictability tangent

The exact finite-rank comparison to `MC-340` is visible without asymptotics. Since

\[
h(p_R)=g(m^{-2}),
\]

substituting `(9)` into `(8)` gives `(10)`. Equation `(11)` then yields `(12)`, and therefore

\[
I(X;Y)
\ge
\frac R2
\left(
\tau^2-\frac1{m^2}
\right)
-\operatorname{TC}(X).
\tag{25}
\]

When `tau=eta/sqrt(C)`, `(25)` is exactly the transcript-information floor previously obtained from the binary chi-square identity plus Pinsker. The new curve keeps all higher even powers of posterior predictability rather than truncating at the quadratic tangent.

Indeed the Taylor expansion at `z=0` is

\[
g(z)
=
\log2-rac z2-rac{z^2}{12}-\frac{z^3}{30}-\cdots,
\tag{26}
\]

so every higher term strengthens the information tariff once `rho` is not infinitesimal.

This also explains why the improvement is largest near exact dephasing. Pinsker is locally sharp around an uninformative posterior, whereas the endpoint approaches posterior means of magnitude one.

## 4. The Fano step is unnecessary once squared posterior predictability is known

`MC-340` converted `rho_i^2` first into a Bayes-error bound using `|b|>=b^2` and then converted average Bayes error into conditional entropy with binary Fano. Both relaxations discard information already present in the posterior mean.

Equation `(18)` bypasses both steps. If `E(W)<=1` and `delta(W)<=epsilon`, then `rho>=1-epsilon`; monotonicity of `g` and `(3)` give

\[
H(X\mid Y)
\le
R g((1-\varepsilon)^2)
=R h(\varepsilon/2),
\]

which proves `(14)`.

The gain does not depend on a special decoder, a memoryless channel, or independent source coordinates. It is entirely a consequence of binary source alphabets plus the same squared posterior predictability already forced by the coefficient-energy/dephasing geometry.

## Prior art and novelty boundary

The ingredients are classical. The representation of binary conditional entropy as the expectation of the entropy of the posterior Bernoulli parameter is immediate from the definition of conditional entropy; Jensen's inequality and entropy subadditivity are standard. Classical work on equivocation versus decision/estimation quality includes Hellman and Raviv, *Probability of Error, Equivocation, and the Chernoff Bound*, IEEE Transactions on Information Theory **16** (1970), 368--372, DOI `10.1109/TIT.1970.1054466`. `MC-340` already cites Cover and Thomas for the entropy identities, data processing and Fano machinery.

A targeted literature search on 17 September 2026 found a broad classical literature relating conditional entropy, Bayes error and estimation quality, but no external theorem is load-bearing for `(18)`--`(26)`: the needed posterior-mean identity and the concavity calculation for `g` are proved above. No novelty is claimed for those abstract information-theoretic facts or inequalities.

The durable Mathia-specific delta is their specialization to the reciprocal endpoint after `MC-338`/`MC-340`: the same energy/dephasing geometry now yields the nonlinear transcript-capacity curve `(8)`--`(10)`, strictly strengthens the previous Pinsker floor away from zero predictability, and halves the leading near-exact conditional-entropy allowance compared with the Fano route.

## Boundaries and falsification tests

- **Binary source phases are load-bearing.** Equation `(18)` uses `X_i in {-1,+1}`. A larger alphabet needs a different entropy-versus-posterior-moment extremal problem.
- **The theorem consumes the same posterior statistic as `MC-338`.** It does not create a new arithmetic observation or prove that any Möbius-derived architecture has small `rho`.
- **The complete transcript is required.** The step `(23)` assumes `Y` contains every admitted `Y_i`, exactly as in `MC-340`.
- **The scalar curve is sharp, but the global composition can have slack.** Subadditivity and the final Jensen step need not be equalities for the punctured dependent source. The theorem does not claim an exact rate-distortion function for the full source law.
- **Energy remains an escape.** If normalized coefficient energy grows, `(5)` can permit the same dephasing with smaller `rho`, and the information lower bound weakens accordingly.
- **Analog precision remains an escape from state counting.** Equations `(16)`--`(17)` apply only to finite transcripts; the invariant statement is `(8)` in mutual information.
- **No arithmetic source-edge upper theorem is supplied.** `MC-359`--`MC-360` still identify the current architecture-facing task: upper-bound the necessary source separation/information for an actual Möbius-derived transcript.
- **No `M(x)` estimate or zero-free result follows.** All arguments are finite endpoint probability and coefficient geometry; no reciprocal-zeta continuation, contour shift or RH-equivalent estimate is imported.

## Consequence for the research line

The global transcript gate is now calibrated by the exact binary posterior entropy rather than only its quadratic Pinsker tangent or a Fano surrogate. For fixed bounded energy and fixed nontrivial dephasing, the required information rate is the explicit entropy deficit in `(8)`; near the matched-filter energy floor, error `epsilon` permits at most `R h(epsilon/2)` nats of conditional source uncertainty.

This does not change the main frontier exposed by `MC-359`--`MC-360`: the missing theorem is still an **architecture-specific arithmetic upper bound** on the source information or source-edge separation available to a natural Möbius-derived transcript. What changes is the lower target that such an upper theorem must beat: it is now the full binary-entropy capacity curve, not just the earlier Pinsker/Fano relaxations.