# AF-518 — Uniform vanishing-relative tail transport is curvature-invisible

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `QUANTITATIVE-OBSTRUCTION` · `DIRICHLET-SOURCE` · `UNIFORM-RELATIVE-TAIL-TRANSPORT` · `GLOBAL-RELATIVE-PROFILE` · `THRESHOLD-CLOSURE` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
P(s)=\sum_{p\in\mathbb P}p^{-s},
\qquad
\kappa_P(s)=\frac{d^2}{ds^2}\log P(s),
\qquad s>1.
\]

For each cutoff `A`, retain every prime `p\le A`. For each prime `p>A`, choose a pairwise distinct positive atom `q_{p,A}\ge p`, and put

\[
\varepsilon_A
:=
\sup_{p>A}\log\frac{q_{p,A}}p.
\tag{1}
\]

Assume

\[
\varepsilon_A\longrightarrow0.
\tag{2}
\]

Define

\[
R_A
=
\{p\in\mathbb P:p\le A\}
\cup
\{q_{p,A}:p\in\mathbb P,\ p>A\},
\tag{3}
\]

and let `\kappa_A` be the log-curvature of its Dirichlet sum. Then there is an absolute constant `C<\infty` such that, for all sufficiently large `A`,

\[
\boxed{
\sup_{s>1}
\frac{|\kappa_A(s)-\kappa_P(s)|}{\kappa_P(s)}
\le C\varepsilon_A.
}
\tag{4}
\]

Consequently,

\[
\boxed{
\sup_{s>1}
|\log\kappa_A(s)-\log\kappa_P(s)|
\longrightarrow0.
}
\tag{5}
\]

Thus the weighted transport criterion of AF-514 is not close to necessary. A whole cofinite tail may move by an additive distance far beyond every fixed power `p^\alpha`, `\alpha<1`, while remaining uniformly invisible to the complete relative-curvature profile, provided only that the displacement is **uniformly sublinear in relative scale**:

\[
\sup_{p>A}\frac{q_{p,A}-p}{p}\longrightarrow0
\tag{6}
\]

is a sufficient equivalent formulation of `(2)` for outward additive transports.

A concrete ordinary-integer control lies strictly outside AF-514. For every sufficiently large odd prime `p`, put

\[
h(p)
=2\left\lfloor\frac{p}{2\log p}\right\rfloor+1,
\qquad
q_p=p+h(p).
\tag{7}
\]

Then every `q_p` is an even composite integer, `p\mapsto q_p` is eventually strictly increasing, and

\[
h(p)\asymp\frac{p}{\log p},
\qquad
\sup_{p>A}\log\frac{q_p}{p}
=O\!\left(\frac1{\log A}\right).
\tag{8}
\]

Hence the corresponding cofinite composite-tail controls satisfy

\[
\boxed{
\sup_{s>1}
\frac{|\kappa_A(s)-\kappa_P(s)|}{\kappa_P(s)}
=O\!\left(\frac1{\log A}\right)
\longrightarrow0.
}
\tag{9}
\]

By contrast, their AF-514 weighted budget is infinite for every cutoff:

\[
\sum_{p>A}
\frac{h(p)(1+\log^2p)}{p^2}
=\infty.
\tag{10}
\]

So `(4)` genuinely closes part of the unresolved gap between AF-514's sufficient weighted sublinear regime and AF-515--AF-516's visible nonzero-ratio regime.

## Derivation

Write

\[
Q_A(s)=\sum_{q\in R_A}q^{-s},
\qquad
D_A(s)=Q_A(s)-P(s),
\qquad
\eta_A(s)=\frac{D_A(s)}{P(s)}.
\tag{11}
\]

Then

\[
Q_A=P(1+\eta_A)
\]

and

\[
\kappa_A-\kappa_P
=(\log(1+\eta_A))''.
\tag{12}
\]

The proof splits once, at a fixed abscissa, between the convergence-boundary region and a closed right half-line. The boundary estimate uses the relative support displacement directly; the right-half-line estimate combines the remote-tail factor with the fixed `2,3` curvature carrier from AF-511.

### 1. Log-support displacement controls the source through two derivatives near `s=1`

Fix once and for all

\[
\sigma=\frac32.
\]

For a moved prime write

\[
y=\log p,
\qquad
d_{p,A}=\log(q_{p,A}/p),
\qquad 0\le d_{p,A}\le\varepsilon_A.
\tag{13}
\]

For `j=0,1,2`, set

\[
f_{j,s}(y)=\partial_s^j e^{-sy}=(-y)^j e^{-sy}.
\]

If `1<s\le\sigma` and `\varepsilon_A\le1`, the mean-value theorem in the support coordinate gives, uniformly in `p>A`,

\[
|f_{0,s}(y+d)-f_{0,s}(y)|
\le C\varepsilon_A p^{-s},
\tag{14}
\]

\[
|f_{1,s}(y+d)-f_{1,s}(y)|
\le C\varepsilon_A(1+\log p)p^{-s},
\tag{15}
\]

and

\[
|f_{2,s}(y+d)-f_{2,s}(y)|
\le C\varepsilon_A(1+\log^2p)p^{-s}.
\tag{16}
\]

Summing over the moved tail and enlarging to the full prime source yields

\[
|D_A(s)|
\le C\varepsilon_A P(s),
\tag{17}
\]

\[
|D_A'(s)|
\le C\varepsilon_A\bigl(P(s)+|P'(s)|\bigr),
\tag{18}
\]

and

\[
|D_A''(s)|
\le C\varepsilon_A\bigl(P(s)+|P'(s)|+P''(s)\bigr).
\tag{19}
\]

Put

\[
u(s)=\frac{P'(s)}{P(s)},
\qquad
\kappa(s)=\kappa_P(s).
\tag{20}
\]

Since

\[
\frac{P''}{P}=\kappa+u^2,
\tag{21}
\]

equations `(17)`--`(19)` imply

\[
|\eta_A|\le C\varepsilon_A,
\tag{22}
\]

\[
|\eta_A'|
\le C\varepsilon_A(1+|u|),
\tag{23}
\]

and, after differentiating `\eta_A=D_A/P`,

\[
|\eta_A''|
\le
C\varepsilon_A\bigl(1+|u|+u^2+\kappa\bigr).
\tag{24}
\]

The only issue is whether division by prime curvature remains uniform as `s\downarrow1`. The classical prime-zeta boundary asymptotics used in AF-512--AF-517 give, with `s=1+t` and `L(t)=\log(1/t)`,

\[
P(1+t)\sim L(t),
\qquad
u(1+t)\sim-\frac1{tL(t)},
\qquad
\kappa(1+t)\sim\frac1{t^2L(t)}.
\tag{25}
\]

Therefore

\[
\frac1\kappa\to0,
\qquad
\frac{|u|}{\kappa}\to0,
\qquad
\frac{u^2}{\kappa}\to0
\qquad(s\downarrow1).
\tag{26}
\]

Away from `1`, all three ratios are continuous and `\kappa>0`, because log-curvature is the variance of `\log p` under the positive tilted prime weights. Hence

\[
\sup_{1<s\le\sigma}
\frac{1+|u(s)|+u(s)^2}{\kappa(s)}
<\infty
\tag{27}
\]

and also

\[
\sup_{1<s\le\sigma}
\frac{(1+|u(s)|)^2}{\kappa(s)}
<\infty.
\tag{28}
\]

Equations `(23)`--`(28)` now give

\[
\boxed{
\sup_{1<s\le\sigma}
\frac{|\eta_A''(s)|}{\kappa(s)}
\le C\varepsilon_A,
}
\tag{29}
\]

and

\[
\boxed{
\sup_{1<s\le\sigma}
\frac{|\eta_A'(s)|^2}{\kappa(s)}
\le C\varepsilon_A^2.
}
\tag{30}
\]

For large `A`, `(22)` gives `|\eta_A|\le1/2`. Hence

\[
(\log(1+\eta_A))''
=
\frac{\eta_A''}{1+\eta_A}
-
\frac{(\eta_A')^2}{(1+\eta_A)^2},
\tag{31}
\]

and `(29)`--`(31)` imply

\[
\boxed{
\sup_{1<s\le\sigma}
\frac{|\kappa_A(s)-\kappa(s)|}{\kappa(s)}
\le C\varepsilon_A.
}
\tag{32}
\]

Unlike AF-514, no summable generator-space transport budget is needed. Near the convergence boundary, uniformly small displacement in **log-support** is already the correct first-order control.

### 2. The remote cutoff controls the entire right half-line

For `s\ge\sigma`, the same mean-value calculation keeps the `s` factor that was harmless on the bounded interval. For `j=0,1,2`,

\[
|D_A^{(j)}(s)|
\le
C\varepsilon_A(s+1)
\sum_{p>A}(1+\log^2p)p^{-s}.
\tag{33}
\]

Bounding the prime tail by the integer tail and integrating gives, uniformly for `s\ge\sigma`,

\[
\sum_{p>A}(1+\log^2p)p^{-s}
\le
C_\sigma(1+\log^2A)A^{1-s}.
\tag{34}
\]

Since `P(s)\ge2^{-s}`, while `u=P'/P` and `\kappa` are bounded on `[\sigma,\infty)`, quotient differentiation of `\eta_A=D_A/P` yields

\[
|\eta_A^{(j)}(s)|
\le
C_\sigma\varepsilon_A
(s+1)^2(1+\log^2A)
A\left(\frac2A\right)^s,
\qquad j=0,1,2.
\tag{35}
\]

AF-511 supplies the fixed-pair curvature lower envelope

\[
\kappa(s)
\ge
c_\sigma\left(\frac23\right)^s,
\qquad s\ge\sigma.
\tag{36}
\]

Combining `(31)`, `(35)`, and `(36)`, and using `|\eta_A|\le1/2` for large `A`, gives

\[
\frac{|\kappa_A(s)-\kappa(s)|}{\kappa(s)}
\le
C\varepsilon_A(1+\log^2A)A(s+1)^2
\left(\frac3A\right)^s
\tag{37}
\]

\[
\hspace{1.8cm}
+
C\varepsilon_A^2(1+\log^2A)^2A^2(s+1)^4
\left(\frac6{A^2}\right)^s.
\]

For all sufficiently large `A`, both exponential bases are below a fixed number strictly smaller than `1`. The supremum over `s\ge\sigma=3/2` of each polynomial-times-exponential factor is therefore controlled, up to an absolute constant, by its value at `s=\sigma`. Consequently,

\[
\sup_{s\ge\sigma}
\frac{|\kappa_A(s)-\kappa(s)|}{\kappa(s)}
\le
C\varepsilon_A
\frac{1+\log^2A}{\sqrt A}
+
C\varepsilon_A^2
\frac{(1+\log^2A)^2}{A}.
\tag{38}
\]

In particular, because `\varepsilon_A\to0`, the right side is at most `C\varepsilon_A` for large `A`. Combining `(32)` and `(38)` proves `(4)`.

Once the relative error is below `1/2`, both curvatures remain positive and the elementary bound `|\log(1+x)|\le2|x|` proves `(5)`.

### 3. The `p/log p` composite transport is invisible but violates AF-514's budget

For `(7)`, the function `x/(2\log x)` is increasing for `x>e`. Hence `h(p)` is eventually nondecreasing, and therefore `p\mapsto p+h(p)` is strictly increasing on the odd primes. Since both `p` and `h(p)` are odd, `q_p=p+h(p)` is even; for large `p` it exceeds `2`, so it is composite.

Also

\[
0<\frac{h(p)}p
\le
\frac1{\log p}+\frac1p
\le
\frac2{\log p}
\tag{39}
\]

for sufficiently large `p`. Thus

\[
0\le
\log\frac{q_p}{p}
=
\log\left(1+\frac{h(p)}p\right)
\le
\frac{h(p)}p
\le
\frac2{\log A}
\tag{40}
\]

uniformly for `p>A`, proving `(8)` and then `(9)` from `(4)`.

On the other hand,

\[
h(p)\asymp\frac{p}{\log p},
\]

so the AF-514 transport summand satisfies

\[
\frac{h(p)(1+\log^2p)}{p^2}
\asymp
\frac{\log p}{p}.
\tag{41}
\]

The classical prime sum

\[
\sum_{p\le x}\frac{\log p}{p}
=\log x+O(1)
\tag{42}
\]

in particular diverges. Every tail of `(41)` therefore diverges, proving `(10)`.

This is not merely a new example within AF-514: its hypothesis `B_A\to0` fails maximally, while the global relative-curvature distance still tends to zero.

## Fidelity and matched-control audit

AF-514 established a weighted sufficient condition for cofinite tail invisibility and exhibited composite shifts of size `p^\alpha`, `\alpha<1`. AF-515 then found a nonzero mesoscopic defect for a coherent proportional tail shift, and AF-516 showed that this defect survives uniformly sublinear jitter around every fixed ray `q_p\sim cp`, `c>1`.

AF-518 closes the most immediate gap between those statements. For a full cofinite tail, the curvature representation is blind to **every uniformly vanishing relative displacement**, not just to transports with finite AF-514 budget. The explicit `p/\log p` control is useful because it sits well beyond every fixed `p^\alpha`, `\alpha<1`, and because its old weighted budget diverges.

Together with AF-515--AF-516, this gives a sharp qualitative boundary for two large coherent classes:

- if the whole moved tail satisfies `q_p/p\to1` uniformly beyond the cutoff, its global relative-curvature distance from the prime source tends to zero;
- if the whole moved tail satisfies `q_p/p\to c>1` with uniformly sublinear additive jitter around `cp`, a fixed mesoscopic curvature gap survives.

This is still not a necessary-and-sufficient classification for arbitrary variable relative displacement. In particular, oscillatory ratios, nonuniform convergence, sparse linear excursions, blockwise transports, and scale-dependent selected sets can mix the two behaviors. AF-517 already shows that participation density is an independent resource for proportional moves.

The control family in `(7)` is especially strong for provenance testing. It retains every prime below the cutoff, replaces **every** sufficiently large prime by a distinct ordinary composite integer, and moves each generator an unbounded distance `\asymp p/\log p`; nevertheless the complete relative-curvature carrier converges uniformly to the prime carrier.

## Representation audit

The tested representation is exactly the same full relative log-curvature carrier as in AF-511--AF-517:

\[
\|Q-\mathbb P\|_{\mathrm{rel}\,\kappa}
=
\sup_{s>1}
\frac{|\kappa_Q(s)-\kappa_P(s)|}{\kappa_P(s)}.
\tag{43}
\]

The theorem identifies **log-support displacement** as a natural local modulus for this representation near the convergence boundary. That is representation-specific: source-aware data such as atom labels, parity, divisibility, congruence classes, or an atom-indexed transport metric immediately separates the composite controls.

The important fidelity statement is therefore not that sublinear transport is intrinsically small. It is that this particular compression turns a uniformly vanishing relative support move into a uniformly vanishing output move even when the absolute source displacement tends to infinity and the earlier generator-space transport norm is infinite.

This sharpens the design requirement for any repair. A lift that merely refines the same unmarked curvature profile at more values of `s` cannot help, because `(4)` already controls the entire domain `s>1`. Recovering robust rational-prime provenance against these controls requires either a stronger source-sensitive topology or extra arithmetic/relational marks that do not collapse under log-support-near-identity transport.

## Prior art and novelty assessment

No novelty is claimed for the analytic ingredients.

- C.-E. Fröberg, **“On the prime zeta function,”** *BIT* 8 (1968), 187–202, DOI `10.1007/BF01933420`, supplies the classical prime-zeta boundary behavior used in AF-512--AF-517 and in `(25)`.
- The fixed-pair lower envelope `(36)` is the internal AF-511 estimate obtained directly from the variance representation of log-curvature.
- AF-514 supplies the earlier weighted support-transport theorem; AF-515--AF-517 supply the complementary visible proportional/density regimes.
- General instability and regularization of inverse Laplace/exponential-sum recovery were already audited in AF-511; the present theorem is a direct forward-stability estimate for one specialized positive Dirichlet carrier, not a new general inverse-Laplace theorem.

A focused search for prime-zeta log-curvature stability under uniformly vanishing relative support transport did not locate a standard theorem matching `(4)`. The proof is nevertheless elementary once the representation and the correct log-support modulus are chosen, so the result is deliberately classified `NO-NOVELTY-CLAIM`. Its durable value is the threshold closure and the explicit composite family beyond AF-514's budget, not a literature novelty assertion.

## Boundaries and failure modes

1. **Outward transport is assumed.** The proof uses `q_{p,A}\ge p`, which preserves convergence and simplifies the support mean-value bounds. Uniformly small inward log-displacements should admit analogous estimates when all atoms remain comparable, but that extension is not claimed here.
2. **Uniform relative control is essential.** Condition `(2)` is a tail supremum. Pointwise `q_p/p\to1` for one fixed sequence implies that tail-supremum condition, but an `A`-dependent family with rare order-one excursions need not satisfy it.
3. **This is an invisibility theorem, not a converse.** Failure of `(2)` does not imply visibility. AF-517 shows that density and scale localization also matter.
4. **No exact collision is produced.** The transformed curvature profiles approach the prime profile but do not equal it; AF-509/AF-510 exact quotient fidelity remains intact.
5. **No RH consequence is asserted.** The result concerns robust provenance of one prime-derived compression, not equality of Euler products, zeta zeros, or RH-equivalent data.
6. **The integer corollary uses a standard prime-sum asymptotic only to show strict separation from AF-514's hypothesis.** The main stability theorem `(4)` itself uses no PNT density input beyond the previously established prime-zeta boundary behavior.

## Dependencies

- `AF-509`: exact curvature equality classifies simple positive Dirichlet sources up to common dilation.
- `AF-510`: the dilation quotient has an explicit canonical inverse.
- `AF-511`: remote replacement gives the fixed `2,3` curvature lower envelope and the first zero-margin control.
- `AF-512`: the prime-zeta convergence boundary does not restore a provenance margin and supplies the boundary-scale asymptotics used here.
- `AF-514`: weighted cofinite tail transport is a sufficient invisibility criterion; `(7)`--`(10)` show that AF-518 is strictly stronger.
- `AF-515`: coherent proportional full-tail transport leaves a nonzero mesoscopic curvature gap.
- `AF-516`: that proportional gap survives uniformly sublinear rounding around every fixed nonzero dilation ratio.
- `AF-517`: partial proportional transport shows that participation density is another independent visibility parameter.

## Consequence for the line

The cofinite-tail transport frontier is now substantially cleaner. The old gap between “weighted-small sublinear” and “fixed proportional” transport was partly an artifact of AF-514's generator-space norm. In the curvature representation's native log-support coordinate, **uniformly vanishing relative displacement is enough for complete global invisibility**, even for all-composite tails at distance `p/\log p` whose AF-514 budget diverges.

The next unresolved transport question is therefore not whether slower-than-linear full-tail drift can eventually become visible merely because its absolute displacement is large. It cannot under the uniform condition `(2)`. The live boundary is instead nonuniform relative displacement: sparse or blockwise order-one excursions, oscillatory ratios, and scale-dependent participation where the tail supremum does not vanish but the Laplace probe may still average the excursions away. Those cases can now be tested against the two calibrated endpoints supplied by AF-518 and AF-515--AF-517.