# WI-383 — The fixed-scale remainder has an unconditional negative recurrence floor

**Status:** `EXACT-DERIVED + CLASSICAL-ALMOST-PERIODICITY + LITERATURE-BACKED + DECISIVE-ROUTE-BARRIER + PRIOR-ART-AUDITED`.

## Claim

WI-382 shows that eventual one-sided boundedness of the fixed-profile Chebyshev remainder already implies RH. For the exact cosine-convolution kernel selected by WI-380/WI-381, one can say more: the limiting unperforated arithmetic-polar layer cannot supply a nonnegative reserve even in the RH world.

Fix `L>0` and retain the WI-382 definitions

\[
g(s)=\sqrt{\frac2L}\cos\!\left(\frac{\pi s}{L}\right)
\mathbf 1_{|s|\le L/2},
\qquad
q=g*g,
\]

\[
Q(z)=\int_{-L}^{L}q(t)e^{zt}\,dt,
\]

and

\[
R_L(x)=
2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
q\!\left(\log\frac n x\right)
-2Q(1/2)\sqrt x.
\tag{1}
\]

For a critical-line zero `rho=1/2+i gamma`, let `m_gamma` be its multiplicity and define

\[
\boxed{
A_L:=4\sum_{\substack{\gamma>0\\
\zeta(1/2+i\gamma)=0}}
m_\gamma Q(i\gamma).
}
\tag{2}
\]

Then `0<A_L<\infty`, and the following dichotomy holds.

- If RH is false, WI-382 gives

\[
\liminf_{k\to\infty}R_L(k+1)=-\infty.
\tag{3}
\]

- If RH is true, then

\[
\boxed{
\liminf_{x\to\infty}R_L(x)
=
\liminf_{k\to\infty}R_L(k+1)
=-A_L<0.
}
\tag{4}
\]

Moreover, in the RH case the near-floor returns are relatively dense on logarithmic scale: for every `epsilon>0` there is `H=H(L,epsilon)` such that every sufficiently large interval `[U,U+H]` contains a `u` with

\[
R_L(e^u)<-A_L+\epsilon.
\tag{5}
\]

After rounding `e^u` to the nearest integer, the same statement holds for an integer sample `k+1` lying in the corresponding fixed multiplicative interval, with an additional `o(1)` error.

Consequently, without assuming or denying RH,

\[
\boxed{
\liminf_{k\to\infty}R_L(k+1)<0.
}
\tag{6}
\]

In particular no eventual inequality

\[
R_L(k+1)\ge0
\tag{7}
\]

can be true. More sharply, for every `delta>0`, an eventual lower bound

\[
R_L(k+1)\ge -A_L+\delta
\tag{8}
\]

is impossible.

This closes the possibility that the **limiting unperforated fixed-width critical prime-polar remainder by itself** pays a positive gamma tariff uniformly. Any successful direct Gate-II repair must use information absent from that limiting layer — in particular the genuinely `k`-dependent source-perforation / rooted-domain correction left as `O_L(1)` in WI-382 — or must exclude the source-zero trial before the old--old form is evaluated.

## 1. The Fourier weights are nonnegative and summable

WI-382 computes

\[
G(z)=\int_{-L/2}^{L/2}g(s)e^{zs}\,ds
=
\sqrt{\frac2L}\,
\frac{2a\cosh(zL/2)}{z^2+a^2},
\qquad a=\frac\pi L,
\tag{9}
\]

with removable nonzero values at `z=\pm ia`, and

\[
Q(z)=G(z)^2.
\tag{10}
\]

For real `gamma`, `G(i gamma)` is real. Hence

\[
\boxed{Q(i\gamma)=G(i\gamma)^2\ge0.}
\tag{11}
\]

Away from the removable points,

\[
Q(i\gamma)
=
\frac{8a^2}{L}
\frac{\cos^2(\gamma L/2)}{(a^2-\gamma^2)^2},
\tag{12}
\]

so `Q(i gamma)=O_L((1+|gamma|)^{-4})`. The classical zero count `N(T)=O(T log T)` therefore gives absolute convergence of (2).

The sum is strictly positive. The zeros of `G(i gamma)` form, apart from the two removable points, an arithmetic set of cardinality `O_L(T)` up to height `T`. By the established positive-density theorem for simple critical-line zeros (in particular the Alpöge--Furman theorem anchoring this research line), there are `\gg T\log T` distinct simple critical ordinates up to height `T`. Thus infinitely many critical ordinates avoid the zero set of `G`, and at least one term in (2) is strictly positive.

This positivity is specific and important. For a generic signed smoothing transform, the zero coefficients need not have one sign and the exact floor below would not follow merely from almost periodicity.

## 2. Under RH the explicit formula is an absolutely convergent trigonometric series plus a vanishing tail

For `c>1/2`, bilateral Mellin inversion gives

\[
R_L(x)
=
\frac{1}{2\pi i}
\int_{c-i\infty}^{c+i\infty}
2Q(s)\left(-\frac{\zeta'}{\zeta}(s+1/2)\right)x^s\,ds
-2Q(1/2)\sqrt x.
\tag{13}
\]

The zeta pole at `s=1/2` has residue `+2Q(1/2)\sqrt x` and cancels the displayed main term. Assume RH and shift the remaining contour to `Re s=-1`. The crossed nontrivial poles are exactly

\[
s=i\gamma,
\]

with residue

\[
-2m_\gamma Q(i\gamma)x^{i\gamma}.
\tag{14}
\]

No trivial-zero pole is crossed: the first one occurs at `s=-5/2`. On `Re s=-1`, the functional equation gives the standard logarithmic bound for `\zeta'/\zeta(-1/2+it)`, while WI-382's transform estimate gives `Q(-1+it)=O_L((1+|t|)^{-4})`. The shifted integral is therefore absolutely convergent and `O_L(x^{-1})`.

Pairing conjugate zeros yields the sharpened RH explicit formula

\[
\boxed{
R_L(x)
=
F_L(\log x)+O_L(x^{-1}),
}
\tag{15}
\]

where

\[
\boxed{
F_L(u)
=-4\sum_{\gamma>0}m_\gamma Q(i\gamma)\cos(\gamma u).
}
\tag{16}
\]

Because `\sum m_gamma Q(i gamma)<\infty`, (16) converges absolutely and uniformly. Thus `F_L` is a Bohr uniformly almost-periodic function.

## 3. The almost-periodic function has an exact global minimum

Every coefficient in (16) is nonnegative. Therefore, term by term,

\[
F_L(u)\ge
-4\sum_{\gamma>0}m_\gamma Q(i\gamma)
=-A_L.
\tag{17}
\]

At `u=0`, all cosines equal one, so equality holds:

\[
F_L(0)=-A_L.
\tag{18}
\]

Uniform almost periodicity now does more than give a subsequence. For every `epsilon>0`, the set of `epsilon`-almost periods of `F_L` is relatively dense. If `tau` is such an almost period, then in particular

\[
|F_L(\tau)-F_L(0)|<\epsilon,
\]

hence

\[
F_L(\tau)<-A_L+\epsilon.
\tag{19}
\]

There are therefore arbitrarily large, relatively densely spaced logarithmic times at which `F_L` returns as close as desired to its exact global minimum. Combining (15), (17), and (19) gives

\[
\boxed{
\liminf_{x\to\infty}R_L(x)=-A_L.
}
\tag{20}
\]

No linear-independence hypothesis on zeta ordinates is used. Recurrence to the already attained phase configuration `u=0` is a generic property of a uniformly almost-periodic function; rational relations among the frequencies do not obstruct it.

## 4. Integer sampling preserves the floor

WI-382 proves unconditionally that

\[
R_L'(x)=O_L(x^{-1/2}),
\tag{21}
\]

and consequently

\[
\sup_{x\in[k+1,k+2]}
|R_L(x)-R_L(k+1)|=O_L(k^{-1/2}).
\tag{22}
\]

Take any sequence of logarithmic recurrences from Section 3 and round `e^u` to the nearest integer. Equation (22) changes the value by `o(1)`. Conversely, (17) and (15) bound every sufficiently large real point below by `-A_L-o(1)`. Hence under RH

\[
\boxed{
\liminf_{k\to\infty}R_L(k+1)=-A_L.
}
\tag{23}
\]

The relative-density statement also survives: a bounded gap in `u=log x` becomes a bounded multiplicative gap in `x`, and rounding changes the value by `o(1)`.

## 5. Removing the RH case split

WI-382 already establishes

\[
\neg\mathrm{RH}
\Longrightarrow
\liminf_{k\to\infty}R_L(k+1)=-\infty.
\tag{24}
\]

Section 4 establishes the complementary implication

\[
\mathrm{RH}
\Longrightarrow
\liminf_{k\to\infty}R_L(k+1)=-A_L<0.
\tag{25}
\]

Equations (24)--(25) prove the unconditional negative-floor statement (6). This is a proof by exhaustive cases, not a conditional RH claim.

The same dichotomy shows that for every `delta>0`, (8) fails eventually: under RH the sequence recurrently approaches `-A_L`, while under RH failure it is unbounded below.

## 6. Consequence for the rooted Gate-II route

WI-381/WI-382 isolate the actual source-perforated arithmetic-polar layer as

\[
Q_k^{\rm arith}+Q_k^{\rm pol}
=R_L(k+1)+O_L(1).
\tag{26}
\]

The present result says that the stationary limiting term in (26) has **no positive uniform reserve to spend**. Under RH it recurrently returns to a strictly negative floor; under RH failure it has arbitrarily deep negative excursions.

Therefore the remaining `O_L(1)` term in (26) is not harmless bookkeeping if one wants a positive Gate-II tariff. It is now the only possible direct-repair carrier inside this trial family. A successful arithmetic proof must extract a structured, sign-coherent order-one effect from the exact source perforations / rooted construction that compensates the recurrent floor at the relevant `k`, rather than replacing them by an `O(1)` error. The alternative is the other live branch already identified in WI-382: prove that these source-zero gamma-negative trials are excluded by the actual graph/domain relation before the old--old quadratic form is tested.

This is a genuine route barrier rather than an RH proof. Equation (26) permits an order-one correction, and `A_L` is itself order one. Nothing here proves that the correction has the wrong sign or insufficient size.

## 7. Prior-art and novelty audit

The harmonic-analysis mechanism is classical. Absolutely convergent trigonometric zero sums are uniformly almost periodic, and values of a uniformly almost-periodic function recur relatively densely. The use of zeta-zero explicit formulas to obtain oscillation and almost-periodicity statements is also established territory; see for example J. Kaczorowski and O. Ramaré, *Almost periodicity of some error terms in prime number theory*, Acta Arith. 106 (2003), 277--297, DOI `10.4064/aa106-3-6`, and the Landau--Pintz oscillation literature already audited in WI-382.

A particularly close recent analogue is R. A. Mittermeier, *Deep Episodes in the Prime-Power Checkpoint Program: An Unconditional Terminal-Episode Theorem, an Exact Chebyshev Bridge, and Sharp Recovery Recurrence -- Part 5*, Zenodo 22076088 (26 Aug 2026), DOI `10.5281/zenodo.22076088`. That unrefereed preprint studies a different Suzuki/checkpoint weighted-Chebyshev functional and explicitly reports uniform almost periodicity under RH, recurrent approach to its comparison level, and the conclusion that no positive uniform reserve floor can close its tail. This materially constrains novelty: the general strategy “explicit formula + almost periodic recurrence closes a positive reserve floor” is not new here.

The Mathia-specific content is the exact specialization to the WI-380/WI-381 cosine-convolution remainder, the positivity `Q(i gamma)=G(i gamma)^2>=0`, the exact floor `-A_L`, preservation on the `x=k+1` lattice, and the resulting identification of the `O_L(1)` source-perforation/rooted correction in (26) as the only remaining direct-repair carrier for this trial family. No priority claim is made.

## 8. Boundaries and falsification

- The exact minimum uses `Q(i gamma)>=0`. A different profile whose zero coefficients have mixed signs need not have its minimum at the all-zero phase and requires a separate hull optimization.
- No linear independence of the zeta ordinates is assumed. The recurrence used here is recurrence to the phase configuration already attained at `u=0`, not simultaneous approximation to a prescribed unattained phase.
- The positive constant `A_L` uses the established existence of `\gg T log T` distinct simple critical ordinates to rule out the `O_L(T)` zero set of `G(i gamma)`. Multiplicities are otherwise retained throughout.
- The RH contour shift is used only inside the RH branch of the dichotomy. Off the critical line, WI-382 supplies the stronger `liminf=-infinity` alternative through the Landau--Pintz argument.
- Equation (26) is only an `O_L(1)` comparison. The present finding does **not** transfer the exact floor to the fully perforated rooted layer and does not rule out an order-one positive correction there.
- The result does not alter the Montgomery/Weil proportion bound. It addresses the current individual-defect Gate-II branch of the canonical research mandate.

The decisive next test is therefore no longer whether the limiting fixed-scale Chebyshev remainder can be made uniformly positive. It cannot. The live direct-repair question is whether the exact `k`-dependent source-perforation/rooted correction in (26) has a forced positive component large enough to overcome the recurrent floor and the fixed gamma tariff, or whether the graph/domain relation excludes the trial instead.