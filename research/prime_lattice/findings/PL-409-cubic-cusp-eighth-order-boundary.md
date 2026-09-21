# PL-409 — The Abel cusp gives an eighth-order Ramanujan boundary law and a sharp `25/28` zero-layer crossover

**Evidence/status:** `EXACT-DERIVED + INTERNAL-SHARPENING + ROUTE-ADVANCE + KERNEL-CUSP-OBSTRUCTION`.

**Parent findings:** `PL-404`, `PL-405`, `PL-408`.

## Claim

`PL-408` used the safe bound

\[
\widehat K_\eta(\xi)=O_\eta(|\xi|^{-7})
\]

for the cubic Abel kernel

\[
K_\eta(x)=|x|e^{-\eta|x|^3}\sin\!\left(\frac{\pi}{6}|x|^3\right),
\qquad \eta>0,
\tag{1}
\]

and consequently located the `H^{-7/4}` source layer outside every fixed Ramanujan range `q\le H^{7/8-\varepsilon}`. That decay estimate is valid but not sharp. The first nonsmooth term of `K_eta` at the origin is the explicit cusp

\[
K_\eta(x)
=\frac\pi6 x^4
-\frac{\pi\eta}{6}|x|^7
+O_\eta(x^{10}),
\tag{2}
\]

so the jump of the seventh derivative determines an **eighth-order** Fourier tail:

\[
\boxed{
\widehat K_\eta(\xi)
=-\frac{105\eta}{16\pi^7}\,|\xi|^{-8}
+O_\eta(|\xi|^{-14})
\qquad(|\xi|\to\infty).
}
\tag{3}
\]

The gap from order `8` to order `14` is not an assumption: after the `|x|^7` cusp, the next nonsmooth term in the Taylor expansion occurs at `|x|^{13}`; the intervening powers `x^4,x^{10}` are smooth across the origin.

Insert (3) into the exact single-denominator Poisson formula of `PL-408`,

\[
B_{q,\eta}(H)
=\sum_{r\mid q}\mu(q/r)
\sum_{m\in\mathbb Z}\widehat K_\eta(Hm/r).
\tag{4}
\]

Uniformly for `q\le H`, this gives

\[
\boxed{
B_{q,\eta}(H)
=\mathbf 1_{q=1}\widehat K_\eta(0)
-\frac{\pi\eta}{720}\frac{J_8(q)}{H^8}
+O_\eta\!\left(\frac{q^{14}}{H^{14}}\right),
}
\tag{5}
\]

where

\[
J_8(q)=\sum_{r\mid q}\mu(q/r)r^8
=q^8\prod_{p\mid q}(1-p^{-8})
\tag{6}
\]

is the eighth Jordan totient. In particular, the first nonzero aliasing correction has the **same negative sign for every Ramanujan denominator**. The absolute-value estimate in `PL-408` therefore did not merely miss possible cancellation: at the true leading order there is no denominator cancellation to recover.

For

\[
A_{\eta,\le Q}^{[2]}(H)
=\frac12\sum_{q\le Q}
\frac{\mu(q)^2}{\phi(q)^2}B_{q,\eta}(H),
\tag{7}
\]

put

\[
S_8(Q)
:=\sum_{q\le Q}
\frac{\mu(q)^2J_8(q)}{\phi(q)^2}.
\tag{8}
\]

Then, uniformly for `2\le Q\le H`,

\[
\boxed{
A_{\eta,\le Q}^{[2]}(H)
=W_{1,\eta}
-\frac{\pi\eta}{1440H^8}S_8(Q)
+O_\eta\!\left(
H^{-14}Q^{13}\{\log\log(3Q)\}^2
\right).
}
\tag{9}
\]

The coefficients in (8) are nonnegative and have a standard Dirichlet-series pole at `s=7`. More precisely,

\[
\sum_{q\ge1}
\frac{\mu(q)^2J_8(q)}{\phi(q)^2q^s}
=\zeta(s-6)G_8(s),
\tag{10}
\]

where `G_8` is analytic in a neighborhood of `Re(s)\ge7` and

\[
C_8:=G_8(7)
=\prod_p
\left(1-\frac1p\right)
\left(
1+\frac{p^8-1}{p^7(p-1)^2}
\right)
>0.
\tag{11}
\]

Hence

\[
\boxed{
S_8(Q)\sim \frac{C_8}{7}Q^7.
}
\tag{12}
\]

Consequently, for every fixed `0<\kappa<1` and `Q=\lfloor H^\kappa\rfloor`,

\[
\boxed{
A_{\eta,\le H^\kappa}^{[2]}(H)
=W_{1,\eta}
-\frac{\pi\eta C_8}{10080}
H^{-8+7\kappa}
\{1+o(1)\}.
}
\tag{13}
\]

This replaces the method-relative `7/8` localization from `PL-408` by a sharp leading law for every fixed fractional interior. Relative to the already-fixed zero-sensitive scale `H^{-7/4}`, the exact crossover is

\[
-8+7\kappa=-\frac74
\quad\Longleftrightarrow\quad
\boxed{\kappa=\frac{25}{28}}.
\tag{14}
\]

Thus

\[
\boxed{
\kappa<\frac{25}{28}
\Longrightarrow
A_{\eta,\le H^\kappa}^{[2]}(H)-W_{1,\eta}
=o(H^{-7/4}),
}
\tag{15}
\]

whereas at `\kappa=25/28` the truncated Ramanujan interior itself contributes a deterministic nonzero term of order `H^{-7/4}`. For `25/28<\kappa<1` that deterministic aliasing term is larger than the zero-sensitive layer while remaining `o(H^{-1})`.

The `25/28` value is therefore **not a new RH-critical exponent**. It is the point at which the unavoidable Fourier tail created by the Abel regulator's `|x|^7` cusp reaches the same scale as the `PL-404` zero layer. Any use of denominator truncation near that scale must subtract or otherwise account for this regulator-induced background before interpreting an `H^{-7/4}` signal as zero-sensitive.

## 1. The origin cusp fixes the Fourier tail

Write `a=pi/6`. For `r=|x|`,

\[
r e^{-\eta r^3}\sin(ar^3)
=ar^4-a\eta r^7
+\left(\frac{a\eta^2}{2}-\frac{a^3}{6}\right)r^{10}
+O_\eta(r^{13}).
\tag{16}
\]

The powers `r^4=x^4` and `r^{10}=x^{10}` are smooth. The coefficient of the first nonsmooth term is `-a eta`, and therefore

\[
K_\eta^{(7)}(0+)-K_\eta^{(7)}(0-)
=-2a\eta\,7!
=-1680\pi\eta.
\tag{17}
\]

With the Fourier convention of `PL-408`,

\[
\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi ix\xi}\,dx,
\]

the distributional eighth derivative of `K_eta` has the decomposition

\[
K_\eta^{(8)}
=-1680\pi\eta\,\delta_0+R_8,
\tag{18}
\]

where, after subtracting a smooth cutoff times the `|x|^7` cusp, the remainder has its next derivative jump only at order `13`; equivalently its Fourier contribution is `O_eta(|xi|^-14)`. Hence

\[
(2\pi i\xi)^8\widehat K_\eta(\xi)
=-1680\pi\eta+O_\eta(|\xi|^{-6}),
\]

which is (3), since

\[
\frac{-1680\pi\eta}{(2\pi)^8}
=-\frac{105\eta}{16\pi^7}.
\tag{19}
\]

This also shows that eighth-order decay is sharp for every fixed `eta>0`: the leading constant is nonzero.

## 2. Poisson turns the cusp into `J_8(q)`

For `q>1`, the zero Fourier mode in (4) cancels exactly as in `PL-408`. For every divisor `r|q` and `q\le H`, all nonzero arguments satisfy `|Hm/r|\ge1`, so (3) may be inserted uniformly:

\[
\sum_{m\ne0}\widehat K_\eta(Hm/r)
=
-\frac{105\eta}{16\pi^7}
\frac{r^8}{H^8}
\sum_{m\ne0}\frac1{m^8}
+O_\eta\!\left(\frac{r^{14}}{H^{14}}\right).
\tag{20}
\]

Using

\[
\sum_{m\ne0}m^{-8}=2\zeta(8)=\frac{\pi^8}{4725}
\tag{21}
\]

gives

\[
-\frac{105\eta}{16\pi^7}\,2\zeta(8)
=-\frac{\pi\eta}{720}.
\tag{22}
\]

The leading divisor sum in (4) is exactly `J_8(q)`, while the error is bounded by

\[
\sum_{r\mid q}r^{14}
\le \zeta(14)q^{14}.
\tag{23}
\]

This proves (5). The same formula includes `q=1` after retaining its uncancelled zero mode `widehat K_eta(0)`.

The sign is important. `J_8(q)>0` for every `q`, so the first nonzero Poisson alias of every denominator points in the same direction. The improved threshold below is therefore not obtained by hypothesizing arithmetic cancellation between Ramanujan modes.

## 3. Summing denominators gives an exact fractional-interior law

Insert (5) into (7). The leading term gives (9). For the remainder,

\[
\sum_{q\le Q}
\frac{\mu(q)^2q^{14}}{\phi(q)^2}
\ll
Q^{13}\{\log\log(3Q)\}^2,
\tag{24}
\]

using the same elementary `q/phi(q)` estimate as `PL-408`.

For the main coefficient, define

\[
g_8(q)=\frac{\mu(q)^2J_8(q)}{\phi(q)^2}.
\]

It is nonnegative and multiplicative, with

\[
g_8(p)=\frac{p^8-1}{(p-1)^2}.
\tag{25}
\]

Its Dirichlet series factors as (10), because

\[
G_8(s)
=\prod_p
\left(1+\frac{p^8-1}{(p-1)^2p^s}\right)
\left(1-p^{6-s}\right).
\tag{26}
\]

After cancellation of the `p^{6-s}` term, the local factor differs from `1` by `O(p^{5-Re(s)}+p^{12-2Re(s)})`; hence the product is absolutely convergent in a neighborhood of `s=7`. At `s=7` it is the positive convergent product (11). The standard Tauberian consequence for the nonnegative coefficients is (12).

If `Q=H^kappa` with `kappa<1`, the error in (9) divided by its main correction is

\[
\ll_η
\left(\frac QH\right)^6
\{\log\log(3Q)\}^2=o(1),
\tag{27}
\]

which proves (13).

## 4. Relation to `PL-408`

There is no contradiction with the `PL-408` estimate. Its seventh-order Fourier bound was deliberately a safe consequence of seven weak `L^1` derivatives and gave

\[
A_{\eta,\le Q}^{[2]}(H)-W_{1,\eta}
=O_\eta(H^{-7}Q^6\{\log\log Q\}^2).
\]

Equation (3) uses one extra fact not exploited there: the seventh derivative has a **finite jump**, rather than arbitrary `L^1` behavior. That jump can be differentiated once distributionally, and its atom gives the exact eighth-order Fourier coefficient. The next cusp then supplies enough separation to control the remainder uniformly.

The deterministic `H^{-1}` conclusion of `PL-408` is unchanged: for every fixed `kappa<1`, (13) is still `o(H^-1)`. The zero-layer statement is sharpened from the sufficient range `kappa<7/8` to the exact fractional-interior crossover `kappa=25/28` for this declared kernel and truncation.

The distinction between the two thresholds is substantive. `7/8` was a consequence of a nonsharp decay inequality; `25/28` comes with a nonzero asymptotic coefficient and cannot be improved by taking absolute values more carefully while keeping the same `q\le H^kappa` truncation and fixed `eta>0`.

## 5. Prime-exponent interpretation

Because `mu(q)^2` restricts the Ramanujan spectrum to square-free denominators,

\[
q\le H^\kappa
\quad\Longleftrightarrow\quad
v(q)\in\{0,1\}^{(\mathcal P)},
\qquad
\langle v(q),(\log p)_p\rangle\le\kappa\log H.
\tag{28}
\]

Equation (13) therefore gives more than a support statement. It computes the first coherent spectral leakage from every fixed fractional interior of that square-free energy ball. The leakage is generated by the **archimedean regularizer cusp**, pushed through Poisson summation into the positive arithmetic weight `J_8(q)`.

At the `PL-404` resolution, the energy geometry has three regimes. Interiors below `25/28` are invisible at `H^-7/4`; the `25/28` interior produces a universal regulator background exactly at that scale; larger fixed interiors produce a still-sub-`H^-1` background that swamps the zero layer. Thus any future moving-boundary comparison with actual prime spectral mass must distinguish the arithmetic zero-sensitive correction from this explicitly computable cusp background.

## 6. Novelty and adversarial audit

The analytic ingredients are standard: Taylor expansion at a cusp, distributional differentiation, Riemann--Lebesgue decay after subtracting the singular jet, Poisson summation, Jordan totients, and a one-pole Tauberian argument. None is claimed as new.

A targeted literature search for this specific cubic Abel kernel, its `|x|^7` cusp, Ramanujan-denominator Poisson decomposition, the `J_8` coefficient, and the resulting `25/28` crossover located no direct occurrence. A repository audit of the live `PL-404`--`PL-408` chain likewise finds only the safe seventh-order estimate in `PL-408`. The durable delta is therefore the **line-specific sharpening** (3)--(15), not a new Fourier-analysis theorem.

The following boundaries are essential.

1. **`eta>0` is fixed.** The leading coefficient is proportional to `eta`. Sending the Abel regulator to zero jointly with `H` changes the balance and is not covered by (13). At `eta=0` the local cusp structure changes completely and the kernel also loses exponential decay.

2. **The asymptotic fractional-interior law requires `kappa<1`.** At `Q\asymp H`, the error hierarchy in (27) no longer separates. Nothing here computes the full boundary layer that produces the `H^-1` term of `PL-404`.

3. **`25/28` is regulator geometry, not RH geometry.** Its equality with the zero-layer scale comes from `8-7kappa=7/4`. It must not be read as a natural exponent selected by zeta zeros.

4. **The `H^-7/4` term at the crossover is a contaminant, not the zero term.** The coefficient in (13) is explicit, negative, and present without any RH input. Any numerical or analytic experiment at `Q\asymp H^{25/28}` must remove it before testing the zero-sensitive coefficient from `PL-404`.

5. **No actual-prime source replacement is proved.** This remains a theorem about the singular-series/Ramanujan model. The live arithmetic bridge in `PL-406`--`PL-407` is untouched.

6. **No cancellation upgrade is hidden.** The first denominator corrections are all same-sign because `J_8(q)>0`. A route that beats this model background must use a different subtraction, a joint endpoint limit, or structure from the actual prime spectral measure rather than hoping for cancellation among these low-energy Ramanujan modes.

## Consequence for the line

The model-side moving boundary is now quantitatively sharper. The cubic filter does not merely suppress finite Ramanujan energy: its first leakage from a fractional square-free energy ball is explicitly

\[
-\frac{\pi\eta C_8}{10080}H^{-8+7\kappa}.
\]

This pushes the certified invisibility range for the `H^{-7/4}` layer from `kappa<7/8` to `kappa<25/28`, and shows that the new threshold is sharp for the declared fixed-`eta` truncation because the coefficient is nonzero.

The live arithmetic fork remains the one in `PL-407`--`PL-408`, but with an extra guardrail: a signed prime/model spectral comparison near the moving rational-frequency boundary must first remove the universal eighth-order cusp leakage. Otherwise the regulator itself creates a signal at exactly the zero-sensitive scale before the true `q\asymp H` source boundary has been reached.