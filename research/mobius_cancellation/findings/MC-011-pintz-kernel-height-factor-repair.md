# MC-011 — Pintz kernel bound drops a shifted-height factor, but Theorem 6.1 survives

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `PARTIAL-AUDIT`.

## Claim

The proof of Theorem 6.1 in the recent Pintz preprint `MC-S19` contains a second repairable gap, distinct from the endpoint localization issue isolated in `MC-010`.

In equation (6.23), Pintz estimates the Mellin kernel

\[
r_\lambda(H)=\frac{1}{2\pi i}\int_{(0)}e^{s^2/\lambda+Hs}g(s)\,ds,
\]

where

\[
g(s)=\frac{(s+\rho_0-\kappa-1)\zeta(s+\rho_0-\kappa)}{(s-\kappa)(s+1)^4},
\qquad
\rho_0=1-\eta_0+i\gamma_0.
\]

Writing

\[
\delta=\eta_0+\kappa,
\qquad
T=\gamma_0+t,
\qquad
z=1-\delta+iT,
\]

the integrand on `s=it` contains

\[
(z-1)\zeta(z)=(-\delta+iT)\zeta(1-\delta+iT).
\tag{1}
\]

Pintz's first displayed bound in (6.23) retains the size of this numerator through a factor `gamma_0+2 lambda`, but the next displayed inequality removes that linear shifted-height factor and keeps only the Korobov–Vinogradov exponent `C delta^(3/2)`. The cited Ford bound (`MC-S20`) does not justify that deletion: for `|T|>=3`, it gives

\[
|\zeta(1-\delta+iT)|
\le A|T|^{B\delta^{3/2}}\log^{2/3}|T|,
\qquad A=76.2,\ B=4.45,
\tag{2}
\]

so direct absolute-value control of (1) has one additional factor of order `|T|`.

However, this does **not** invalidate Theorem 6.1. Keeping the missing factor gives a corrected uniform kernel bound of the form

\[
|r_\lambda(H)|
\ll
\frac{1}{\kappa}
(1+\gamma_0)^{1+B\delta^{3/2}}
\log^C(2+\gamma_0),
\tag{3}
\]

and the theorem's weighted integral already contains a compensating factor `gamma_0`. Consequently (3) still yields the lower bound stated in Theorem 6.1, after enlarging the generic logarithmic constant:

\[
\int_1^{Ye^3}
\frac{|M(x)|\,dx}{x^{1-\kappa+\beta_0}/\gamma_0}
\gg
\frac{\kappa Y^\kappa}
{\gamma_0^{C(\eta_0+\kappa)^{3/2}}(\log \gamma_0Y)^C}.
\tag{4}
\]

Thus the **printed kernel estimate is too strong for the argument given**, but the theorem-level lower bound survives with the same stated asymptotic shape. Together with `MC-010`, this further narrows rather than eliminates the remaining audit burden behind `MC-009`.

## 1. The missing factor in equation (6.23)

On the line `s=it`, equation (1) gives exactly

\[
|g(it)|
=
\frac{|(-\delta+iT)\zeta(1-\delta+iT)|}
{|it-\kappa|(1+t^2)^2}.
\tag{5}
\]

Since `|it-kappa|>=kappa`, the cited Korobov–Vinogradov estimate controls only the zeta factor. For `|T|>=3`, Ford's explicit theorem (`MC-S20`) therefore gives

\[
|g(it)|
\ll
\frac{|T|^{1+B\delta^{3/2}}\log^{2/3}|T|}
{\kappa(1+t^2)^2}.
\tag{6}
\]

The exponent `1+B delta^(3/2)` is forced by the explicit numerator in (5). In particular, applying (2) to the preceding line of Pintz's (6.23) cannot turn

\[
(\gamma_0+2\lambda)\,
\max_{|t|\le2\lambda}|\zeta(1-\delta+i(\gamma_0+t))|
\]

into a bound with only `(gamma_0+lambda)^(C delta^(3/2))`. The linear factor has simply disappeared between the two displayed inequalities.

This observation does not assert that no sharper estimate for `r_lambda` could exist through cancellation in the Fourier integral. It says that the **absolute-value argument actually written in (6.23)** does not prove the displayed stronger bound.

## 2. The low-height region is also outside the literal Ford hypothesis, but is harmless

Ford's estimate (2) is stated for `|T|>=3`. Since `T=gamma_0+t`, the integration in (6.23) can pass through `|T|<3`, so invoking (2) uniformly without a separate case is not literal.

The required repair is elementary. The function

\[
(z-1)\zeta(z)
\]

extends holomorphically across `z=1`. Under the hypotheses of Theorem 6.1,

\[
0<\delta=\eta_0+\kappa<\frac12,
\]

so the set

\[
\{1-\delta+iT:0\le\delta\le1/2,\ |T|\le3\}
\]

is compact after filling in the removable singularity at `z=1`. Therefore

\[
|(z-1)\zeta(z)|\ll1
\qquad(|T|\le3),
\tag{7}
\]

uniformly in the theorem's parameter range. No factor `1/delta` or hidden pole loss appears.

Thus the low-height sector is not an obstruction; it only needs to be separated from the high-height Ford estimate.

## 3. A corrected kernel estimate

Let

\[
q=1+B\delta^{3/2},\qquad B=4.45.
\]

Because `delta<1/2`,

\[
q<1+4.45\,(1/2)^{3/2}<2.58<3.
\tag{8}
\]

Combining (6) and (7), enlarging harmless logarithmic factors, gives for all real `t`

\[
|(z-1)\zeta(z)|
\ll
(1+|T|)^q\log^C(2+|T|).
\tag{9}
\]

Now

\[
1+|T|
=1+|\gamma_0+t|
\le (1+\gamma_0)(1+|t|).
\tag{10}
\]

On `s=it`, the factor `e^{s^2/lambda+Hs}` has modulus `e^{-t^2/lambda}`. Hence (5), (9), and (10) imply

\[
|r_\lambda(H)|
\ll
\frac{(1+\gamma_0)^q\log^C(2+\gamma_0)}{\kappa}
\int_{-\infty}^{\infty}
\frac{e^{-t^2/\lambda}(1+|t|)^q\log^C(2+|t|)}{(1+t^2)^2}\,dt.
\tag{11}
\]

The last integral is bounded uniformly in `lambda>=1`: by (8), its tail is dominated by `t^(q-4) log^C t`, whose exponent is strictly less than `-1`; the Gaussian only improves convergence. Therefore (11) proves (3).

This route is slightly cleaner than truncating at `|t|<=2 lambda`: it controls the complete vertical integral and shows explicitly why the fourth-order `(s+1)^(-4)` denominator is strong enough to absorb the one missing height factor.

## 4. The weighted `gamma_0` factor repairs Theorem 6.1

The contour computation in Pintz's (6.20) gives

\[
V
=
\left(1-\frac1{\rho_0}\right)(1+\kappa)^{-4}
 e^{\kappa^2/\lambda}Y^\kappa
+O(Y^{-1/3}).
\tag{12}
\]

For the nontrivial zero set with `gamma_0>0`, the factor `|1-1/rho_0|` is bounded away from zero by an absolute constant; after taking `Y` sufficiently large for the fixed theorem parameters,

\[
|V|\gg Y^\kappa.
\tag{13}
\]

The tail `x>=Ye^3` is bounded by Pintz's (6.21)–(6.22). Applying (3) to the remaining integral in (6.20) therefore yields

\[
\int_1^{Ye^3}|M(x)|x^{-1-\beta_0+\kappa}\,dx
\gg
\frac{\kappa Y^\kappa}
{(1+\gamma_0)^{1+B\delta^{3/2}}\log^C(2+\gamma_0)}.
\tag{14}
\]

The left side of Theorem 6.1 is `gamma_0` times (14). Hence

\[
\int_1^{Ye^3}
\frac{|M(x)|\,dx}{x^{1-\kappa+\beta_0}/\gamma_0}
\gg
\frac{\kappa Y^\kappa\gamma_0}
{(1+\gamma_0)^{1+B\delta^{3/2}}\log^C(2+\gamma_0)}.
\tag{15}
\]

Nontrivial zeta zeros have ordinate bounded below by a fixed positive absolute constant. Consequently

\[
\frac{\gamma_0}{(1+\gamma_0)^{1+B\delta^{3/2}}}
\gg
\gamma_0^{-B\delta^{3/2}},
\tag{16}
\]

and `log(2+gamma_0)` is harmlessly bounded by a power of `log(gamma_0 Y)` for large `Y`. Equations (15)–(16) are exactly the shape claimed in (4), with Pintz's generic constant `C` enlarged if necessary.

The apparent missing height factor is therefore compensated **at the theorem level** by the `gamma_0` normalization already built into the weighted Mertens integral. The repair does not require a stronger zeta estimate.

## 5. Other local checks around the kernel do not expose another defect

The nearby algebra in (6.20) is consistent with this repair.

- On the original line `Re(s)=3`, the Mellin identity for `M(x)` is used in its absolute-convergence range, and `|M(x)|<=x` together with the Gaussian factor and rational decay gives the needed interchange.
- The zeta factor then cancels algebraically. After cancellation, shifting to `Re(s)=-1/3` crosses the pole at `s=kappa`; the poles at `s=-1` and `s=kappa-rho_0` remain to the left under the stated parameter inequalities. This produces the residue in (12).
- The shift to `Re(s)=lambda` used for the `x>=Ye^3` tail lies safely in the absolute zeta region for large `lambda`, and the Gaussian estimate supplies the exponential cutoff recorded in (6.22).

These checks support the local Theorem 6.1 mechanism after the correction above. They are **not** a claim that every later use of Theorem 6.1 in Section 7 has now been independently verified.

## Relation to MC-009 and MC-010

`MC-010` found a separate mismatch between the upper endpoint `Ye^3` in Theorem 6.1 and the endpoint `Y` used in Corollary 6.3, and repaired it by applying the theorem with a constant-rescaled parameter. The present finding addresses the remaining load-bearing kernel estimate inside Theorem 6.1 itself.

Taken together, the two audits show that the two concrete defects found so far are repairable without weakening the asymptotic theorem used by `MC-009`:

1. the terminal-window localization can be restored by constant rescaling (`MC-010`);
2. the missing factor in (6.23) can be retained and then canceled against the theorem's `gamma_0` weight (`MC-011`).

`MC-009` should nevertheless remain `NEEDS-AUDIT`. The global assembly in Section 7 leading from the repaired Theorem 6.1/Corollary 6.3 input to Theorems 2.1–2.2 has not been independently reconstructed end-to-end, and this finding makes no claim about omitted dependencies elsewhere in the preprint.

## Prior art and novelty assessment

`MC-S19` is the primary object under audit. `MC-S20` is the primary source for the explicit Korobov–Vinogradov estimate that Pintz cites in equation (3.6): Ford proves

\[
|\zeta(\sigma+it)|\le76.2|t|^{4.45(1-\sigma)^{3/2}}\log^{2/3}|t|
\]

for `1/2<=sigma<=1` and `|t|>=3`.

No novelty is claimed for Ford's theorem, Pintz's kernel construction, or Theorem 6.1. A targeted search found no correction or erratum addressing equation (6.23) in the week-old preprint. The durable Mathia result is the **proof audit**: the cited bound leaves one linear factor unaccounted for in the printed kernel estimate, but exact denominator integrability plus the existing `gamma_0` weight repairs the theorem with no change to its stated exponent shape.

## Boundaries and falsification tests

This finding does not prove RH, improve an unconditional Mertens bound, or independently establish Pintz's Theorems 2.1–2.2. It also does not prove the stronger pointwise kernel estimate printed in (6.23); rather, it shows that this stronger estimate is unnecessary for Theorem 6.1.

The repair can be falsified by any of the following:

- Ford's bound failing in the parameter range `sigma=1-delta` implied by Theorem 6.1;
- the exponent in (8) reaching `3`, which would destroy the uniform integrability used in (11);
- a pole or unbounded low-height contribution of `(z-1)zeta(z)` in the compact region used for (7);
- absence of the compensating `gamma_0` factor in the exact weighted integral of Theorem 6.1;
- a contour pole omitted in the shift producing (12).

The displayed hypotheses rule out each of these failure modes: `delta<1/2`, Ford gives `B=4.45`, `(z-1)zeta(z)` has a removable singularity at `1`, the theorem's left side explicitly contains `gamma_0`, and the post-cancellation rational integrand has the stated pole locations.

## Consequences for the research line

The fresh Pintz result remains viable as a literature bridge for the weaker RH-complete mean-absolute endpoint isolated in `MC-009`, but it should continue to carry an audit warning until the Section 7 assembly is checked.

More generally, this audit illustrates a useful local-to-global bookkeeping principle for the Möbius line: **a loss that appears fatal in an auxiliary kernel norm need not survive after the normalization of the target observable is restored**. Here the missing height factor is real at the kernel level but exactly matched by the zero-height normalization in the weighted Mertens quantity. Future analytic transfer audits should therefore track numerator growth, kernel decay, and target normalization together rather than judging any one intermediate estimate in isolation.