# ANF-138 — slow diagonalization absorbs all finite-depth conditioning losses

**Status:** `EXACT-DERIVED + CLASSICAL-DIAGONAL-SELECTION + UNBOUNDED-DEPTH-POSITIVE-CASCADE + SUBEXPONENTIAL-SOURCE-PREFACTOR + AUTOMATIC-OMEGA-WINDOW + SOURCE-HEAVY-MARGIN + FIXED-NOTCH-RESIDUAL-SLACK-GATE`. `ANF-133` constructs the same-profile positive saddle-annihilator cascade through every fixed finite depth. `ANF-134`--`ANF-137` then quantify several ways in which the constants of those fixed-depth statements can deteriorate when the depth is allowed to grow with the packet scale `A`. The latest local obstruction is encoded by

\[
\Omega_d
=\max_{1\le k\le d}
J_{k-1}\left(1+\frac{T_{k,d}}{s_k}\right),
\]

because `ANF-137` proves that `Omega_d=o(A)` excludes a fixed positive exponential source loss caused by historical-zero pinching.

For the **existential** question of whether some diagonal depth `D(A)->infinity` can be taken, no quantitative bound on `Omega_d` as a function of `d` is needed. Every finite stage of one recursively chosen `ANF-133` cascade has finite source-comparison constants, finitely many critical cells, finite shifts, positive slack, and finite `Omega_d`. A standard slow diagonal selection can absorb all of those stage-dependent constants simultaneously.

More precisely, there exists a nondecreasing integer function

\[
\boxed{D(A)\longrightarrow\infty}
\tag{1}
\]

such that, for the physical depth-`D(A)` prefix `X_A^{(D(A))}` of one nested `ANF-133` cascade,

\[
\boxed{
D(A)^2\log(D(A)+2)=o(\log A),
\qquad
\Omega_{D(A)}=o(A),
}
\tag{2}
\]

and

\[
\boxed{
\log\frac{E_0(X_A^{(D(A))})}{E_A}=o(A).
}
\tag{3}
\]

Consequently the quantitative conclusions of `ANF-135`--`ANF-137` hold on this diagonal:

\[
\delta_{D(A)}=A^{-o(1)},
\qquad
J_{D(A)}=A^{o(1)},
\qquad
\max_j\tau_{j,D(A)}=A^{o(1)},
\tag{4}
\]

\[
\operatorname{Span}_{\rm ann}(D(A),A)=A^{1+o(1)},
\tag{5}
\]

and every current critical point `xi` lies in a zero-free cell satisfying

\[
\boxed{
\operatorname{dist}(\xi,\partial I_{D(A)}(\xi))
=e^{-o(A)},
\qquad
\sup_{I^{1/2}_{D(A)}(\xi)}|G_{D(A)}''|
=e^{o(A)}.
}
\tag{6}
\]

Thus **historical zero pinching and fixed-depth Laplace constants are not independent existential obstructions**. They can obstruct an explicit or prescribed depth law, but they cannot force failure along every unbounded diagonal.

The non-diagonalizable issue is different. Let

\[
\delta_\infty:=\inf_{d\ge0}\delta_d
=\lim_{d\to\infty}\delta_d.
\tag{7}
\]

If `delta_infinity>0`, then `ANF-134` supplies a genuinely fixed central notch, independent of depth. For every fixed

\[
0<\eta<\delta_\infty,
\]

the same diagonal satisfies

\[
\boxed{
\limsup_{A\to\infty}
\frac1A
\log\frac{E_\eta(X_A^{(D(A))})}
{E_0(X_A^{(D(A))})}
\le \eta-\delta_\infty<0.
}
\tag{8}
\]

If instead `delta_d->0`, slow diagonalization can make that collapse arbitrarily slow but cannot turn a depth-dependent notch `|alpha|<delta_{D(A)}/2` into a fixed positive-width notch. Therefore the same-profile existential frontier separates cleanly into two classes: **finite conditioning constants are diagonalizable; a fixed positive residual slack is not**.

## 1. One infinite recursive cascade exists before any diagonal limit is taken

The construction in `ANF-133` is stagewise. At every finite source-critical stage, the current critical skeleton is finite and nondegenerate; its positive binomial annihilator is defined; the first positive critical density exists strictly before origin saturation; and the output is again a finite nondegenerate source-critical stage to which the same operation applies.

Choose one such continuation recursively once and for all. This produces stage data

\[
\left(
\delta_d,
J_d,
K_d,
\{\tau_{j,d}\}_{j=1}^{J_d},
\theta_{d+1}
\right)_{d\ge0}
\tag{9}
\]

with every entry finite at every finite `d`, and with

\[
\delta_d>0,
\qquad
s_{d+1}=2\theta_{d+1}J_d\log2>0.
\tag{10}
\]

No uniform-in-`d` assertion is used here. This is only a countable recursive choice of finite stages. In particular, for every fixed `d`, `ANF-133` gives constants

\[
0<c_d\le C_d<\infty,
\qquad
A_d^{\rm src}<\infty,
\tag{11}
\]

such that for all sufficiently large `A`,

\[
c_d
\le
\frac{E_0(X_A^{(d)})}{E_A}
\le C_d.
\tag{12}
\]

Likewise, `Omega_d` from `ANF-137` is finite for every fixed `d`, because it is the maximum of finitely many expressions with `s_k>0`.

The point is that a diagonal argument needs only finiteness of each row. It does **not** require a prior growth law for the sequence of row constants.

## 2. Threshold selection absorbs every fixed-depth constant

For each positive integer `d`, choose a threshold `A_d` so large that all of the following hold whenever `A>=A_d`:

\[
\left|\log\frac{E_0(X_A^{(d)})}{E_A}\right|
\le \frac{A}{d},
\tag{13}
\]

\[
\frac{\Omega_d}{A}\le\frac1d,
\tag{14}
\]

and

\[
\frac{d^2\log(d+2)}{\log A}\le\frac1d.
\tag{15}
\]

Equation (13) is possible from (12): after entering the fixed-depth asymptotic range, enlarge the threshold until

\[
\max\{\log C_d,\log(c_d^{-1}),0\}\le A/d.
\]

Equations (14)--(15) are possible because `Omega_d` and `d` are fixed while `A` is free to grow. Make the thresholds strictly increasing and define

\[
D(A):=\max\{d:A\ge A_d\}.
\tag{16}
\]

Then `D(A)->infinity`. If `D(A)=d`, monotonicity in `A` preserves (13)--(15), and hence

\[
\frac1A
\left|\log\frac{E_0(X_A^{(D(A))})}{E_A}\right|
\le\frac1{D(A)}\to0,
\]

\[
\frac{\Omega_{D(A)}}A
\le\frac1{D(A)}\to0,
\]

and

\[
\frac{D(A)^2\log(D(A)+2)}{\log A}
\le\frac1{D(A)}\to0.
\]

This proves (1)--(3).

The threshold can absorb any additional **finite collection of finite stage constants** without changing the argument. For example, if `H_d` is the maximum of the stage-`d` shift, chamber count, inverse nondegenerate Hessian, fixed-depth Laplace constants, or normalized span coefficient, one may additionally require

\[
\log(1+H_d)\le\frac1d\log A
\tag{17}
\]

for `A>=A_d`. Then `H_{D(A)}=A^{o(1)}`. This is the precise sense in which fixed-depth conditioning is diagonalizable.

## 3. The quantitative depth theorems then apply automatically

The abstract threshold argument by itself already gives (3). Its value for the existing quantitative cascade theory is that it automatically enters the hypotheses of the latest depth estimates.

From (2), `ANF-135`--`ANF-136` give

\[
\delta_{D(A)}=A^{-o(1)},
\qquad
J_k=A^{o(1)}\quad(k\le D(A)),
\tag{18}
\]

and the shift/span estimates in (4)--(5). The additional condition required by `ANF-137` is now automatic from (14). Its critical-cell radius and curvature bounds therefore give exactly (6).

This changes the interpretation of the spend-ratio obstruction in `ANF-137`. A sequence of first-critical retunings may well contain layers for which

\[
\frac{T_{k,d}}{s_k}
\]

becomes astronomically large with `d`; nothing here bounds that growth. But for every **fixed** `d` the resulting `Omega_d` is still finite. By taking `A` beyond that finite constant before increasing the depth, one prevents the corresponding pinching exponent from occupying a positive fraction of the `A` scale.

Hence the vanishing-spend mechanism remains relevant to any **explicit** choice such as `D(A)` near the full `ANF-136` window. It is not, however, an obstruction to the existence of *some* unbounded diagonal.

## 4. Subexponential source loss still leaves an exponential affine margin

The weaker two-sided source statement (3) is enough to preserve the large source-to-cardinality separation built into the packet architecture.

At every stage, `ANF-133` gives the strict copy-rate ceiling

\[
R_d<\frac{f_\gamma}{2}.
\tag{19}
\]

The base packet cardinality has exponential rate `gamma log 2`, whereas

\[
E_A
=\exp\!\left((2\gamma\log2+f_\gamma)A+o(A)\right).
\tag{20}
\]

Floors can only reduce the translation copy count, so along the diagonal

\[
\limsup_{A\to\infty}
\frac1A
\log\frac{|X_A^{(D(A))}|}{E_A}
\le
-\gamma\log2-\frac{f_\gamma}{2}<0.
\tag{21}
\]

Combining (3) and (21),

\[
\boxed{
\limsup_{A\to\infty}
\frac1A
\log\frac{|X_A^{(D(A))}|}
{E_0(X_A^{(D(A))})}
\le
-\gamma\log2-\frac{f_\gamma}{2}<0.
}
\tag{22}
\]

Thus losing a depth-uniform `asymp` constant does not by itself destroy the source-heavy character of the construction. Any stagewise prefactor deterioration that is merely finite at each fixed depth can be hidden inside `e^{o(A)}` while the physical affine/cardinality margin stays genuinely exponential.

This is the main reason the diagonal statement is more than bookkeeping: it removes the need to prove a depth-uniform positive Laplace constant merely to keep the block source-heavy on the exponential scale.

## 5. A fixed notch is different: it is controlled by the limit of the slack

The same argument cannot diagonalize a requirement that is itself **uniform in depth**. The fixed-notch problem is exactly of that type.

The slack sequence is monotone decreasing and positive, so the limit (7) exists. If `delta_infinity>0`, choose any fixed `eta<delta_infinity`. Every diagonal stage then has

\[
R_{D(A)}
=\frac{f_\gamma-\delta_{D(A)}}2
\le
\frac{f_\gamma-\delta_\infty}{2}.
\tag{23}
\]

Apply the exact finite-`A` positive-cloud estimate of `ANF-134` with `delta_*=delta_infinity`. It gives

\[
\limsup_{A\to\infty}
\frac1A
\log\frac{E_\eta(X_A^{(D(A))})}{E_A}
\le\eta-\delta_\infty.
\tag{24}
\]

Subtracting (3) proves (8). Therefore a positive residual slack simultaneously freezes a positive notch width and makes its exposure exponentially negligible relative to the actual diagonal source.

If instead `delta_d->0`, no threshold choice can turn the bound

\[
G_d(\alpha)\le\alpha-\delta_d
\tag{25}
\]

into a fixed positive-width notch for all large diagonal depths. This is a limitation of the present proof architecture, not a converse theorem asserting that the true notch exposure must become large.

There is nevertheless no **rate** obstruction. Given any prescribed decreasing function `epsilon(A)->0`, the thresholds can be enlarged further so that

\[
\boxed{
\delta_{D(A)}\ge\varepsilon(A)
}
\tag{26}
\]

for all sufficiently large `A`: for each fixed `d`, wait until `epsilon(A)<=delta_d` before allowing the diagonal to enter depth `d`. Hence even when the slack tends to zero, it may be forced to do so arbitrarily slowly along an existential diagonal. What cannot be manufactured this way is a positive limiting width.

This separates the two concepts that had become entangled in the recent depth analysis:

\[
\boxed{
\text{finite local conditioning}
\quad\text{is diagonalizable, while}\quad
\text{fixed-notch width}
\quad\text{requires a genuinely uniform invariant.}
}
\tag{27}
\]

## 6. Adversarial controls and exact boundary

The diagonal is intentionally non-effective. It may grow so slowly that no explicit formula for `D(A)` follows, and it does not improve the quantitative window of `ANF-136`. Any argument that needs a prescribed depth, polynomially many layers, or a uniform rate in `d` still needs genuine spend-ratio and chamber-conditioning estimates.

Equation (3) is also weaker than a depth-uniform statement

\[
E_0(X_A^{(D(A))})\asymp E_A.
\]

The ratio may tend to zero or infinity subexponentially. What survives uniformly is the exponential source-to-cardinality margin (22).

No interchange of limits is being made. The construction first fixes a finite stage `d`, uses the actual fixed-depth asymptotic threshold supplied by `ANF-133`, and only then chooses how large `A` must be before the diagonal is permitted to advance to that stage. This avoids the invalid inference that pointwise-in-`d` asymptotics are automatically uniform.

The argument also does not prove `delta_infinity>0`. `ANF-135` allows `delta_d->0` at a factorial-type rate, and the diagonal lemma does not strengthen that recurrence. Therefore it does not settle the fixed frozen-notch envelope in `ANF-099`, does not resolve `CLUE-near-extremizer-notch-exposure-envelope.md`, and does not by itself construct a fatal Montgomery--Taylor near-extremizer.

Finally, (6) should not be read as a new local analytic estimate. The local zero-separation and Hessian laws are exactly those of `ANF-137`; the new content is the quantifier conversion showing that their additional `Omega=o(A)` hypothesis can always be met on some unbounded diagonal.

## 7. Prior-art boundary and consequence for `analytic_frontier`

The selection mechanism is the classical diagonal-sequence principle: finitely many requirements at stage `d` can be enforced by waiting long enough before advancing to stage `d+1`. Diagonal extraction is standard throughout real/functional analysis and compactness arguments. A directed prior-art search found no reason to import a named theorem here; the threshold construction (13)--(16) is the complete proof. No external result is load-bearing, so `SOURCES.md` is unchanged and no novelty is claimed for the diagonal principle itself.

The Mathia-specific consequence is structural. `ANF-134` left copy-rate slack and source prefactors as coupled arbitrary-depth gates; `ANF-135`--`ANF-137` progressively quantified the latter through chamber counts and spend-ratio conditioning. For **existence of an unbounded-depth same-profile cascade**, the prefactor/conditioning side is now closed on the exponential scale: one can always choose a slow diagonal with subexponential source distortion, subexponential local conditioning, and preserved exponential affine margin.

The remaining same-profile question that cannot be removed by slower scheduling is therefore the genuinely uniform one:

\[
\boxed{
\delta_\infty>0\ ?
}
\tag{28}
\]

A positive answer would freeze a fixed dark central notch on the unbounded diagonal by (8). A zero limit would leave the current architecture without a uniform fixed-notch certificate even though every finite-depth and local-conditioning constant remains absorbable. The next decisive analysis should therefore target the **residual slack limit itself**, unless an explicit-depth theorem rather than existential diagonalization is required.