# WI-264 — finite-aperture endpoint autocorrelations can screen every active prime layer

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + SOURCE-SPECIFIC-BARRIER + PRIOR-ART-REDIRECT + PRIOR-ART-AUDITED`.

`WI-263` showed that in the one-prime window an antisymmetric pair of narrow endpoint bumps can make the autocorrelation vanish exactly at `log 2` while matching the sign change of Suzuki's continuous source. That construction is not intrinsically one-prime. At **every fixed finite aperture** there are only finitely many von-Mangoldt lags, all strictly inside `(0,2a)`. Because the last such lag has a positive gap to `2a`, the same two-bump construction can place **all** active prime-power lags inside one open zero interval of the autocorrelation.

For the actual first-crossing program this yields a stronger barrier than `WI-263`: even if a hypothetical first crossing is known to lie beyond many prime thresholds, compact support, full support span, positive-definiteness, the exact finite von-Mangoldt source, and the sign pattern of the archimedean density still do not force any negative phase defect. Adding more finite prime layers does not repair the source-sign/Bochner route. Any surviving argument must consume quantitative first-crossing information such as `F_v(r) >= r lambda_r` or the actual null equation `A_{a_*}v=0`.

This finding also corrects the live dependency recorded in `WI-259`. The finite-scale theorem at `L=0.8` already persisted in `WI-253` gives an unconditional positive margin for the unrestricted complex test space, hence any hypothetical first global crossing satisfies `a_*>0.8`. Therefore an independent `FP-0.35` recertification is **not** needed to guarantee prime activation. `WI-260`--`WI-262` remain valid audits of those external certificate/checker paths, but they are no longer a prerequisite for the phase-defect program.

## 1. The first crossing is already beyond the first several prime thresholds

Let

\[
a_*:=\inf\{a>0:\lambda_a\le0\}
\]

be the first unrestricted localized Weil crossing of `WI-238`. `WI-253` records the certified compact-window theorem

\[
Q(f)\ge 8.9\times10^{-18}\,\|f\|_2^2
\qquad
(\operatorname{supp}f\subset[-0.8,0.8])
\tag{1}
\]

for arbitrary complex tests. Together with the nesting monotonicity of the localized Rayleigh infimum this gives

\[
\boxed{\lambda_{0.8}>0\quad\Longrightarrow\quad a_*>0.8.}
\tag{2}
\]

The primary source was rechecked directly: Xuefeng Zhu, *Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau--Widom decay law*, arXiv:2608.24827v2 (2 Sep 2026), states both the lower bound in (1) and that the odd-sector argument upgrades it to arbitrary complex tests of support `[-0.8,0.8]`: <https://arxiv.org/abs/2608.24827>.

Thus the conditional implication in `WI-259`,

\[
\lambda_{7/20}>0\Longrightarrow a_*>7/20,
\]

is mathematically correct but no longer the operative gate: (1)--(2) already imply the stronger statement. In particular a first-crossing mode necessarily sees the prime-power atoms with `log n<1.6` at radius `0.8`, and potentially many more if `a_*` is larger.

## 2. Every finite aperture has a positive last-prime gap

Fix any finite `a>0` with at least one active von-Mangoldt atom and define

\[
\mathcal P_a
:=\{\log n:\ n\ge2,\ \Lambda(n)>0,\ \log n<2a\}.
\tag{3}
\]

Because `n<e^{2a}`, this set is finite. Put

\[
\ell_a:=\max\mathcal P_a,
\qquad
\delta_a:=2a-\ell_a.
\tag{4}
\]

The strict source cutoff `log n<2a` gives the exact positive gap

\[
\boxed{\delta_a>0.}
\tag{5}
\]

No prime-gap theorem is involved: this is only finiteness of the discrete source at fixed aperture. The smallest active lag is `log 2` whenever `a>(log2)/2`.

For Suzuki's continuous source retain

\[
w(h)=\frac{e^{-5h/2}}{1-e^{-2h}}-e^{h/2}.
\tag{6}
\]

As proved in `WI-263`, if `rho>1` is the real root of

\[
\rho^3-\rho-1=0,
\]

and

\[
h_0:=\log\rho=0.2811995743\ldots,
\tag{7}
\]

then

\[
\boxed{
w(h)>0\ (0<h<h_0),
\qquad
w(h)<0\ (h>h_0).
}
\tag{8}
\]

At the actual hypothetical first crossing, (2) ensures `a_*>0.8>h_0/2`, so the construction below has room at both endpoints.

## 3. One zero interval screens all von-Mangoldt atoms

Set `a=a_*` for the first-crossing application. Choose

\[
0<\varepsilon<
\min\left(
 h_0,
 \log2,
 a-\frac{h_0}{2},
 \frac{\delta_a}{2}
\right).
\tag{9}
\]

All four quantities are positive by (2), (5), and `h_0<log2`. Let `phi` be a nonnegative smooth function supported on `[0,epsilon]`, normalized by `||phi||_2=1`, and define

\[
u_-(x)=\phi(x+a),
\qquad
u_+(x)=\phi(a-x),
\qquad
v(x)=\frac{u_-(x)-u_+(x)}{\sqrt2}.
\tag{10}
\]

Exactly as in `WI-263`, `v` is normalized and its support closure spans the full aperture `[-a,a]`. Its real autocorrelation

\[
C_v(h)=\int_{\mathbb R}v(x+h)v(x)\,dx
\tag{11}
\]

has, for positive lags, the sign/support pattern

\[
\boxed{
\begin{array}{ll}
C_v(h)\ge0,&0\le h\le\varepsilon,\\[1mm]
C_v(h)=0,&\varepsilon<h<2a-2\varepsilon,\\[1mm]
C_v(h)\le0,&2a-2\varepsilon\le h\le2a.
\end{array}}
\tag{12}
\]

The middle interval now contains **every** active prime-power lag. Indeed, from (9),

\[
\varepsilon<\log2\le\log n
\tag{13}
\]

for every `log n in P_a`, while

\[
\log n\le\ell_a=2a-\delta_a<2a-2\varepsilon.
\tag{14}
\]

Therefore

\[
\boxed{
C_v(\log n)=0
\quad\text{for every }n\text{ with }\Lambda(n)>0\text{ and }\log n<2a.
}
\tag{15}
\]

This is the key strengthening of `WI-263`: no matter how many finite prime-power layers are active, all of them can be screened simultaneously by one autocorrelation gap. The construction uses only the positive distance from the largest finite source atom to the aperture endpoint.

## 4. The archimedean continuum can be sign-screened at the same time

The first bound in (9) places the self-correlation support inside the positive region of `w`:

\[
0<h\le\varepsilon<h_0
\quad\Longrightarrow\quad
w(h)>0,\ C_v(h)\ge0.
\tag{16}
\]

The third bound in (9) gives

\[
2a-2\varepsilon>h_0,
\tag{17}
\]

so the endpoint cross-correlation lies entirely in the negative region of `w`:

\[
2a-2\varepsilon\le h\le2a
\quad\Longrightarrow\quad
w(h)<0,\ C_v(h)\le0.
\tag{18}
\]

Between those regions `C_v=0`. Hence

\[
\boxed{w(h)C_v(h)\ge0\qquad(0<h<2a).}
\tag{19}
\]

Combining (15) and (19), the complete source-weighted autocorrelation object

\[
d\mu_v(h)=C_v(h)\left[
\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n}(dh)
+w(h)\,dh
\right]
\tag{20}
\]

has every discrete mass equal to zero and has nonnegative continuous density. The `1/(2h)` singularity of `w` at zero is harmless in the convergent weighted observables below, exactly as in `WI-258` and `WI-263`.

Consequently, for every real `t`,

\[
\boxed{
\mathcal M_v(t)
=\int_0^{2a}(1-\cos(th))\,d\mu_v(h)
\ge0,
}
\tag{21}
\]

and for every `0<r<a`,

\[
\boxed{
J_v(r,t)
=\int_0^{2r}(2r-h)(1-\cos(th))\,d\mu_v(h)
\ge0.
}
\tag{22}
\]

The scalar aperture transform also satisfies

\[
\boxed{
\mathcal F_v(r)
=\int_0^{2a}\min(h,2r)\,d\mu_v(h)
\ge0.
}
\tag{23}
\]

Equations (21)--(23) hold simultaneously for the entire finite prime source at the chosen aperture, not only in a one-prime window.

## 5. Exact logical barrier

The phase-slack identity of `WI-258` says that an **actual first-crossing null mode** satisfies

\[
S_v(r)+J_v(r,t)\ge0,
\qquad
S_v(r)=\mathcal F_v(r)-r\lambda_r\ge0.
\tag{24}
\]

A source-forced value `J_v(r,t)<0` would therefore produce useful strict firstness slack. The construction above proves that such negativity cannot be forced from the following data alone:

- compact support in a finite aperture and full support span;
- positive-definiteness of the autocorrelation;
- the exact complete finite set of active von-Mangoldt atoms;
- the exact sign pattern of Suzuki's continuous source `w`;
- any number of phase frequencies, because (21)--(22) hold for every `t`.

The obstruction is stronger than “one atom might have small overlap.” At any finite aperture **all discrete source atoms can have exactly zero overlap simultaneously** while the continuous source has the favorable sign everywhere the autocorrelation is nonzero.

The result deliberately does **not** construct a first-crossing zero mode. In general the endpoint-bump `v` does not satisfy

\[
A_a v=0
\tag{25}
\]

and (23) does not imply the quantitative firstness envelope

\[
\mathcal F_v(r)\ge r\lambda_r.
\tag{26}
\]

Those are precisely the inputs not reproduced by the countermodel. Therefore the surviving source-side program becomes sharper: any defect-to-zero argument based on `WI-253`/`WI-258` must derive a constraint from (25), (26), or an equivalent first-crossing property that forbids the endpoint-gap geometry. Merely moving to a larger radius so that more prime powers enter cannot work.

## 6. Correction to the first-prime dependency chain

`WI-259` was useful in isolating the exact one-prime formula at `r=7/20` and in auditing the public `telleroutlook/weil-first-prime` artifact. Its research disposition, however, treated positivity past `(log2)/2` as an unresolved prerequisite. That dependency is superseded by the already-persisted theorem used in `WI-253` and independently rechecked here: Zhu's certified theorem gives `lambda_0.8>0` in the unrestricted complex space.

Accordingly:

\[
\boxed{
\text{FP-0.35 recertification is not a gate for prime activation at first crossing.}
}
\tag{27}
\]

The exact conditional algebra and the external-artifact defects in `WI-259`--`WI-262` remain valid facts. What changes is their role in the live program. They are now side audits, not prerequisites. The stronger negative result (15)--(22) also makes the one-prime simplification unnecessary as a source-sign test: arbitrary finite prime layers can be screened at once.

## 7. Prior-art and novelty audit

The source/operator framework is prior art. Masatoshi Suzuki's *Weil's quadratic form via the screw function*, arXiv:2606.09096, supplies the localized Weil form, the finite von-Mangoldt source at fixed support, and the operator setting used by `WI-238`--`WI-258`: <https://arxiv.org/abs/2606.09096>. Xuefeng Zhu's arXiv:2608.24827v2 supplies the certified `L=0.8` positivity used in (1)--(2).

Autocorrelation positive-definiteness and the endpoint-bump support calculation are elementary harmonic analysis. `WI-263` already contained the two-bump construction for a one-prime window. The Mathia deduction here is the finite-aperture quantifier upgrade: use the exact last-atom gap `delta_a>0` to put **all** active prime-power lags in the same autocorrelation zero interval, while simultaneously placing the self/cross pieces on the two favorable sign regions of `w`.

A targeted prior-art search around Suzuki's localized Weil form, compact-support autocorrelations, phase modulation, prime-power lags, and source screening located the established explicit-formula/localized-Weil framework but no source stating this all-finite-prime endpoint-gap obstruction. Search absence is audit context only and is not a priority claim.

## Falsification and audit test

The exact barrier can be checked without numerical optimization. A falsification requires an error in one of four statements:

1. the active set `P_a` is finite and has `ell_a<2a`;
2. the two endpoint bumps give the support/sign decomposition (12);
3. inequalities (13)--(14) place every active `log n` in the zero interval;
4. inequalities (16)--(18) place the continuous source on same-sign autocorrelation pieces.

None uses RH, a zero table, a prime-gap estimate, or an external numerical certificate. The only computational theorem imported into the research redirect is the independent finite-window positivity statement `lambda_0.8>0`; the all-prime screening lemma itself is valid at any finite `a>h_0/2` for which the indicated finite source is nonempty.

The logical boundary must remain explicit. This is **not** a counterexample to Suzuki's first-crossing equation and not evidence for RH failure. To overturn its research consequence one must prove that actual first-crossing constraints forbid every autocorrelation with the endpoint-gap screening pattern. Such a theorem would be exactly the new rigidity this line is seeking.

## Research consequence

The accepted sliding-autocorrelation/phase direction should no longer spend effort on either (i) recertifying `FP-0.35` merely to activate the first prime, or (ii) increasing the aperture solely to gain more finite prime-power atoms and hoping their source signs force `J_v<0`. Both routes are now closed as necessary steps.

The live test is narrower and stronger: **can the quantitative firstness family `F_v(r)>=r lambda_r`, or the exact zero-mode equation `A_{a_*}v=0`, force autocorrelation mass at discrete source lags or otherwise rule out the endpoint-gap geometry?** A positive answer must use genuinely first-crossing information that the construction above does not satisfy. A negative answer with a countermodel satisfying that stronger information would close the current phase-defect route much more deeply.