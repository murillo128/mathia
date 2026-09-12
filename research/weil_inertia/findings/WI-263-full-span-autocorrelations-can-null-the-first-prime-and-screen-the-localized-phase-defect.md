# WI-263 — full-span autocorrelations can null the first prime and screen the localized phase defect

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + SOURCE-SPECIFIC-BARRIER + PRIOR-ART-AUDITED`.

`WI-258` and `WI-259` isolate a tempting first-prime continuation of the first-crossing program. If finite-scale positivity at `L=7/20` is eventually certified, then any hypothetical first crossing satisfies `a_*>7/20`, so the localized phase correction at `r=7/20` contains exactly the `n=2` von-Mangoldt atom. One might then hope that the exact zeta source, compact support, and positive-definiteness of the autocorrelation already force

\[
\inf_t J_v(7/20,t)<0.
\]

They do not. There is an explicit family of normalized real functions whose support spans the full aperture, whose autocorrelation is positive-definite, and whose **exact one-prime Suzuki source has the favorable sign at every lag**: the `n=2` atom is killed exactly by an autocorrelation gap, while the continuous archimedean density is paired with the autocorrelation with the same sign on the short-lag bump and the opposite sign on the long-lag cross term. For these models

\[
\mathcal M_v(t)\ge0,
\qquad
J_v(r,t)\ge0
\]

for every frequency `t` and every `0<r<a` for which the source contains only `n=2`.

This is not a first-crossing zero mode and is not claimed to satisfy the quantitative lower envelope `\mathcal F_v(r)\ge r\lambda_r`. The result is instead a sharp logical barrier: **source factorization + full support span + positive-definite autocorrelation cannot by themselves force a negative localized cosine defect at the first-prime scale.** Any successful continuation of `WI-258` after the FP-0.35 gate must use information that this construction does not satisfy, such as the quantitative firstness inequalities or the actual zero-mode equation for Suzuki's operator.

## 1. The archimedean source has one exact sign change

`WI-258` uses Suzuki's continuous source density

\[
w(h)=\frac{e^{-5h/2}}{1-e^{-2h}}-e^{h/2},
\qquad h>0.
\tag{1}
\]

Multiplying by the positive factor `e^{5h/2}(1-e^{-2h})` gives

\[
\operatorname{sgn} w(h)
=
\operatorname{sgn}\bigl(1+e^h-e^{3h}\bigr).
\tag{2}
\]

Let `rho>1` be the unique real root of

\[
\rho^3-\rho-1=0
\]

and put

\[
h_0:=\log\rho=0.2811995743\ldots.
\tag{3}
\]

Because `x^3-x-1` is strictly increasing for `x>1`, (2) gives the exact sign pattern

\[
\boxed{
 w(h)>0\ (0<h<h_0),\qquad
 w(h_0)=0,\qquad
 w(h)<0\ (h>h_0).
}
\tag{4}
\]

Also `rho<2`, hence

\[
h_0<\log2<\frac7{10}.
\tag{5}
\]

The last inequality is the same elementary threshold inequality already used in `WI-259`.

## 2. A two-bump full-span autocorrelation

Fix any

\[
\frac7{20}<a<\frac{\log3}{2}.
\tag{6}
\]

Choose

\[
0<\varepsilon<\min\left(h_0,a-\frac7{20}\right)
\tag{7}
\]

and a nonnegative smooth function `phi` supported on `[0,\varepsilon]`, normalized by `||phi||_2=1`. Define two reflected endpoint bumps

\[
u_-(x)=\phi(x+a),
\qquad
u_+(x)=\phi(a-x),
\tag{8}
\]

and the normalized antisymmetric combination

\[
v(x)=\frac{u_-(x)-u_+(x)}{\sqrt2}.
\tag{9}
\]

The supports of `u_-` and `u_+` are `[ -a,-a+\varepsilon ]` and `[a-\varepsilon,a]`. Thus `v` has support closure spanning the full interval `[-a,a]`; it is not a vector that could be placed in a strictly shorter aperture merely by translating its support. Choosing `phi` to vanish to infinite order at its endpoints puts `v` in the usual smooth/H_0^1 core and hence in the localized Weil form domain used in `WI-257`.

Let

\[
C_v(h)=\int_{\mathbb R}v(x+h)v(x)\,dx.
\tag{10}
\]

For `h\ge0`, the two self-overlaps are nonnegative and are supported in `[0,\varepsilon]`. The only possible positive-lag cross-overlap is from the left bump to the right bump; it carries the minus sign from (9) and is supported in

\[
[2a-2\varepsilon,2a].
\]

Consequently

\[
\boxed{
\begin{array}{ll}
C_v(h)\ge0,&0\le h\le\varepsilon,\\[1mm]
C_v(h)=0,&\varepsilon<h<2a-2\varepsilon,\\[1mm]
C_v(h)\le0,&2a-2\varepsilon\le h\le2a.
\end{array}}
\tag{11}
\]

The choice (7) implies

\[
2a-2\varepsilon>\frac7{10}.
\tag{12}
\]

Combining (5), (7), and (12), `log 2` lies strictly inside the zero gap in (11), so

\[
\boxed{C_v(\log2)=0.}
\tag{13}
\]

Because `C_v` is an autocorrelation, it is automatically positive-definite; equivalently its Fourier transform is `|\widehat v|^2\ge0`. Also `C_v(0)=1` by normalization.

## 3. The exact one-prime source is sign-screened

Condition (6) gives

\[
\log2<2a<\log3,
\tag{14}
\]

so the finite von-Mangoldt part of Suzuki's source on `[0,2a]` contains exactly the single atom `n=2`. By (13), that atom contributes zero after multiplication by `C_v`.

For the continuous part, (7) and (4) show that on the self-overlap region

\[
w(h)>0,\qquad C_v(h)\ge0,
\]

whereas (12) and (4) show that on the cross-overlap region

\[
w(h)<0,\qquad C_v(h)\le0.
\]

Everywhere between those regions `C_v(h)=0`. Hence

\[
\boxed{w(h)C_v(h)\ge0\qquad(0<h<2a),}
\tag{15}
\]

and the only discrete source coefficient is identically screened by (13).

The source density has the familiar `1/(2h)` singularity at the origin, so it should not be treated as a finite Radon measure there. What matters here is that all of the convergent weighted integrals used by `WI-254` and `WI-258` have nonnegative integrands. In particular, for every real `t`,

\[
\boxed{
\mathcal M_v(t)
=\int_0^{2a}(1-\cos(th))\,d\mu_v(h)
\ge0,
}
\tag{16}
\]

and for every `0<r<a`,

\[
\boxed{
J_v(r,t)
=\int_0^{2r}(2r-h)(1-\cos(th))\,d\mu_v(h)
\ge0.
}
\tag{17}
\]

The scalar aperture transform is likewise nonnegative,

\[
\mathcal F_v(r)=\int_0^{2a}\min(h,2r)\,d\mu_v(h)\ge0,
\tag{18}
\]

although (18) is deliberately **not** promoted to the first-crossing inequality `\mathcal F_v(r)\ge r\lambda_r`.

At the radius singled out by `WI-259`, equation (17) gives directly

\[
\boxed{
J_v(7/20,t)\ge0\qquad(t\in\mathbb R).
}
\tag{19}
\]

Thus no choice of modulation frequency can extract a negative first-prime defect from this admissible positive-definite autocorrelation model.

## 4. What this rules out and what it does not

The construction closes a specific weak continuation of the accepted phase clue. Once `lambda_{7/20}>0` is available, it is **not enough** to argue that a first crossing has full support span, that `C_v` is a positive-definite compact-support autocorrelation, and that the exact source at `r=7/20` consists of the `n=2` atom plus the Suzuki archimedean continuum. Those facts allow exact screening: `C_v(log2)` can vanish while the sign change of `w` is matched by the sign change between self- and cross-correlations.

This sharpens the warning already present in `WI-259` that no nonzero lower bound for `C_v(log2)` is known. The obstruction is not merely that the coefficient might be small: even with support spanning past the prime threshold, positive-definiteness allows the first-prime coupling to be **exactly zero**.

The result does **not** construct a null vector of the actual localized Weil operator. In particular it does not show

\[
Q_W^a(v)=0
\]

and does not verify the quantitative firstness lower envelope

\[
\mathcal F_v(r)\ge r\lambda_r.
\]

Those are precisely the surviving sources of rigidity. Therefore `WI-263` does not refute the full `WI-258`/`WI-259` program; it proves that any successful argument must actually consume first-crossing information beyond support and autocorrelation positivity. A proof based only on the sign pattern of the explicit source and Bochner-type constraints on `C_v` cannot work.

The restriction `a<\log3/2` is essential to the clean one-prime statement. At larger first crossings additional prime-power atoms appear and require separate screening or coupling. That does not weaken the barrier at the FP-0.35 gate: certifying `lambda_{7/20}>0` only forces `a_*>7/20`, so a hypothetical first crossing in the nonempty interval `(7/20,\log3/2)` remains admissible until further finite-scale information is proved.

## Prior-art and novelty assessment

The localized Weil source, the archimedean density (1), the finite von-Mangoldt translation terms, and the first-crossing framework are from Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v2 (17 Aug 2026), and the persisted Mathia derivations `WI-253`--`WI-259`.

Positive-definiteness of an autocorrelation and the two-bump sign construction are elementary harmonic analysis. No novelty is claimed for those ingredients. A targeted search around Suzuki's localized Weil form, phase modulation, compact-support autocorrelations, and first-prime screening located the Suzuki framework but no source stating this source-specific two-bump obstruction. Search absence is audit context only and is not a priority claim.

The Mathia contribution is the exact specialization: identify the single sign-change threshold of Suzuki's `w`, place same-sign self-correlation below it and opposite-sign cross-correlation above `7/10`, null the `n=2` atom in the intervening autocorrelation gap, and thereby exhibit a full-span positive-definite autocorrelation for which every localized cosine defect is nonnegative.

## Falsification and audit test

The exact part is falsified by any error in one of three elementary claims: the sign reduction (2)--(4), the support/sign decomposition (11), or the prime-window statement (14). These can be checked independently without numerics.

The logical boundary is equally important. Do **not** use this finding as a counterexample to the actual first-crossing zero-mode equation. To overturn the research consequence, it would be enough to prove that the quantitative firstness inequalities or Suzuki's exact null-vector equation forbid every autocorrelation with the screening pattern (11)--(15). Such a theorem would be new information not assumed here and would be precisely the kind of rigidity the phase program now needs.

## Research consequence

The current first-prime gate remains worth closing, and the independent exact recertification delegated from `WI-260`--`WI-262` is still the immediate computational target. But after that gate, the phase program should **not** spend effort trying to force `C_v(log2)` away from zero or `J_v(7/20,t)` negative using only compact support and positive-definiteness.

The next analytic question is narrower and stronger: can the actual first-crossing constraints — especially `\mathcal F_v(r)\ge r\lambda_r` across radii or the exact equation `A_{a_*}v=0` with the zeta-specific translation operator — exclude the two-bump screening geometry or quantitatively force overlap at `h=\log2`? If not, the one-prime phase-defect route cannot bootstrap toward zero defect on its own.