# RE-042 — first-layer prime/event staggering is below the current race resolution

**Status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + FIRST-LAYER-EVENT-QUANTIZATION + LOCAL-PRIME-RACE-JUMP + RESOLUTION-BOUNDARY + PRIOR-ART-BOUNDED`. `RE-041` isolates the first genuinely arithmetic interface left after the abstract-support controls: a physical CA atom is not a free mass/slope pair, but is quantized by one prime-power label `(p,j)`, while the same primes generate the standard and reciprocal prime-race coordinates entering the uniform `RE-040` calibration. The most immediate way to spend that information would be to compare the first-layer CA event attached to a prime `p` with the ordinary prime-race discontinuity at `p` itself.

That local mismatch is exact, but **it lives strictly below the resolution currently supplied by `RE-040`**. If `eta_p:=eta_{p,1}` is the first-layer CA event coordinate, then

\[
\boxed{
\eta_p
=
p+\frac{\log p}{2(\log p+1)}+O(p^{-1})
=
p+\frac12-\frac1{2(\log p+1)}+O(p^{-1}).
}
\tag{1}
\]

Hence, for every sufficiently large prime,

\[
\boxed{p<\eta_p<p+\frac12.}
\tag{2}
\]

The CA selector therefore jumps by `log p` a half-unit after the prime that generates the atom, whereas the Chebyshev and logarithmic-Mertens coordinates jump at `p`. In the square-root normalization used by `RE-037`--`RE-040`, however, one prime contributes only

\[
\asymp \frac{\log p}{\sqrt p}=o(1).
\tag{3}
\]

More precisely, if

\[
U(x):=\frac{x-\vartheta(x)}{\sqrt x},
\qquad
E(x):=\sum_{q\le x}-\log(1-q^{-1})-\gamma-\log\log x,
\qquad
V(x):=E(x)\sqrt x\log x,
\tag{4}
\]

and `p^-` denotes the left limit at the prime, then

\[
\boxed{
U(\eta_p)-U(p^-)
=-\frac{\log p}{\sqrt p}
+o\!\left(\frac{\log p}{\sqrt p}\right),
}
\tag{5}
\]

\[
\boxed{
V(\eta_p)-V(p^-)
=\frac{\log p}{\sqrt p}
+o\!\left(\frac{\log p}{\sqrt p}\right).
}
\tag{6}
\]

The same scale persists after inserting the exact nonlinear target. For a compact threshold interval

\[
J=[b_0,b_1]\Subset(0,1/2),
\tag{7}
\]

put, with `L=log x`,

\[
\mathcal R_b(x)
:=
V(x)
-
\sqrt x\,L\,
\Psi_{b,L}\!\left(
\frac{U(x)}{\sqrt x\,L}
\right)
-
\sqrt2\,\frac{2b-1}{b},
\tag{8}
\]

where `Psi` is the exact adaptive nonlinear function of `RE-036`. Uniformly for `b in J`, the jump at a large prime is

\[
\boxed{
\mathcal R_b(p^+)-\mathcal R_b(p^-)
=
\frac{\log p}{b\sqrt p}\,(1+o_J(1)).
}
\tag{9}
\]

Thus the physical common-source coupling does leave a local signature: the nonlinear residual has a positive prime jump, while the associated first-layer CA event occurs at the distinct point `eta_p=p+1/2+o(1)` where the prime-race coordinates themselves are continuous. But the signature in (9) tends to zero. `RE-040` currently gives only a uniform **unspecified `o(1)`** residual on the selected compact fan. That statement cannot by itself resolve the individual-prime staggering in (1)--(9).

This does not refute the prime-event quantization route. It identifies its first quantitative floor. A contradiction based on one first-layer atom would need, in addition to selector placement that actually samples the relevant two sides, residual control finer than the `log Z/sqrt(Z)` jump scale; alternatively it must aggregate many atoms or use deeper common-source structure so that the arithmetic signal survives the present normalization.

## 1. The first-layer CA event is asymptotically one half-unit after its prime

The CA event data of `RE-001`, `RE-013`, and `RE-041` are

\[
\lambda_{p,j}
:=
\log\frac{1-p^{-(j+1)}}{1-p^{-j}},
\qquad
m_{p,j}:=\frac{\lambda_{p,j}}{\log p},
\qquad
\frac1{\eta_{p,j}\log\eta_{p,j}}=m_{p,j}.
\tag{10}
\]

For the first layer,

\[
\lambda_{p,1}
=
\log\frac{1-p^{-2}}{1-p^{-1}}
=
\log(1+p^{-1}).
\tag{11}
\]

Writing `L=log p`, the defining equation becomes

\[
\eta_p\log\eta_p
=
\frac{L}{\log(1+p^{-1})}.
\tag{12}
\]

The elementary reciprocal-log expansion gives

\[
\frac1{\log(1+p^{-1})}
=
p+\frac12-\frac1{12p}+O(p^{-2}),
\tag{13}
\]

so

\[
\frac{L}{\log(1+p^{-1})}
=
pL+\frac L2+O\!\left(\frac Lp\right).
\tag{14}
\]

Put `eta_p=p+delta_p`. Since the right side differs from `pL` by `O(L)`, monotonicity of `x log x` first gives `delta_p=O(1)`. Taylor expansion at `p` then yields

\[
(p+\delta_p)\log(p+\delta_p)
=
pL+(L+1)\delta_p+O(p^{-1}).
\tag{15}
\]

Comparing (14) and (15),

\[
\delta_p
=
\frac{L}{2(L+1)}+O(p^{-1}),
\tag{16}
\]

which is (1). In particular `delta_p->1/2` from below; (2) follows for all sufficiently large `p`. Since every sufficiently large prime is odd, `p+1` is composite, so the whole interval `(p,eta_p]` is prime-free.

The critical value (11) is classical CA structure going back to Alaoglu--Erdos; no novelty is claimed for it. The half-unit inversion is an elementary asymptotic consequence used here only to compare the physical event lattice with the current prime-race normalization.

## 2. One prime produces an opposite-sign race jump of size `log p / sqrt(p)`

Use right-continuous prime sums. At `x=p` the Chebyshev function has the exact jump

\[
\vartheta(p^+)-\vartheta(p^-)=L,
\tag{17}
\]

while the logarithmic prime product has the exact jump

\[
E(p^+)-E(p^-)
=-\log(1-p^{-1}).
\tag{18}
\]

Because the normalization point is the same on both sides,

\[
\boxed{
U(p^+)-U(p^-)
=-\frac L{\sqrt p}.
}
\tag{19}
\]

Also

\[
\begin{aligned}
V(p^+)-V(p^-)
&=
-\log(1-p^{-1})\sqrt p\,L\\
&=
\frac L{\sqrt p}\left(1+O(p^{-1})\right).
\end{aligned}
\tag{20}
\]

There is no prime in `(p,eta_p]`. The prime number theorem gives `vartheta(p)=p+o(p)`, so on this bounded interval

\[
U(\eta_p)-U(p^+)=O(p^{-1/2})
=o(Lp^{-1/2}).
\tag{21}
\]

Mertens' product theorem gives `E(p)=o(1)`. The prime-product sum is constant on `(p,eta_p]`, and only the smooth `-log log x` term and the factor `sqrt(x) log x` vary. Since `eta_p-p=O(1)`, elementary differentiation gives

\[
V(\eta_p)-V(p^+)
=o(Lp^{-1/2}).
\tag{22}
\]

Adding (19)--(22) proves (5)--(6). The local common-source signature is therefore the asymptotic vector

\[
\boxed{
(U,V)(\eta_p)-(U,V)(p^-)
=
\frac{\log p}{\sqrt p}\,(-1,1)+
o\!\left(\frac{\log p}{\sqrt p}\right).
}
\tag{23}
\]

The unnormalized prime atom is not small; its disappearance is a consequence of the square-root prime-race normalization required by the false-RH threshold reduction.

## 3. The exact nonlinear residual has a uniform positive jump, but it still vanishes

At the fixed point `x=p`, set

\[
q^\pm
:=
\frac{U(p^\pm)}{\sqrt p\,L}.
\tag{24}
\]

Equation (19) gives the exact relation

\[
\boxed{q^+-q^-=-p^{-1}.}
\tag{25}
\]

The PNT gives

\[
Lq^\pm
=
\frac{p-\vartheta(p^\pm)}p
=o(1).
\tag{26}
\]

From `RE-036`, uniformly for `b` in a fixed compact subinterval of `(0,1/2)` and `|Lq|=o(1)`,

\[
\Psi'_{b,L}(q)
=
\frac{1-b}{b}+o_J(1);
\tag{27}
\]

here the explicit `1/(bL)` correction in `Psi'_{b,L}(0)` is absorbed by `o_J(1)`. The mean-value theorem and (25) therefore give

\[
\begin{aligned}
&\sqrt p\,L
\left(
\Psi_{b,L}(q^+)-\Psi_{b,L}(q^-)
\right)\\
&\qquad=
-\frac L{\sqrt p}
\left(
\frac{1-b}{b}+o_J(1)
\right).
\end{aligned}
\tag{28}
\]

The translated second-layer constant in (8) has no `x`-jump. Combining (20) and (28) yields

\[
\begin{aligned}
\mathcal R_b(p^+)-\mathcal R_b(p^-)
&=
\frac L{\sqrt p}
\left(
1+\frac{1-b}{b}+o_J(1)
\right)\\
&=
\frac L{b\sqrt p}(1+o_J(1)),
\end{aligned}
\tag{29}
\]

proving (9). The sign is rigid and the estimate is uniform on `J`, but its magnitude tends to zero.

At `eta_p` there is no ordinary-prime discontinuity, so `U`, `V`, and the residual (8) are continuous in the `Z` variable there. The CA event selector, by contrast, jumps by exactly `log p` at `eta_p`. Thus the two manifestations of the same prime are genuinely staggered:

\[
p
\quad\text{(prime-race jump)}
\qquad<\qquad
\eta_p=p+\frac12+o(1)
\quad\text{(CA selector jump)}.
\tag{30}
\]

This is source-specific information absent from the abstract staircase of `RE-041`; that control can place its event mass and any external race discontinuity independently.

## 4. Why the current uniform `o(1)` tube cannot use this staggering by itself

`RE-040` proves on the genuine compact false-RH threshold fan that

\[
\sup_{b\in J}
|\mathcal R_b(Z_b)|\longrightarrow0.
\tag{31}
\]

Equation (29) shows that the full nonlinear residual change contributed by crossing one prime is itself

\[
\frac{\log p}{b\sqrt p}(1+o_J(1))=o(1).
\tag{32}
\]

Therefore (31), without a quantitative rate, is compatible with either side of an individual first-layer prime discontinuity. In particular, one cannot turn the geometric fact `p!=eta_p` into a contradiction merely by substituting the current vanishing-width tube: the arithmetic mismatch vanishes inside that tube's unresolved scale.

There are two separate missing ingredients, and neither is supplied here. First, the selected `Z_b` values would have to be shown to sample the relevant sides of the same prime jump; an arbitrary threshold cell need not straddle every prime. Second, the residual would need a rate fine enough to distinguish a jump of order `log Z/sqrt(Z)`, or the argument would have to combine many prime atoms into a nonvanishing cumulative invariant before comparing with the CA events. A deeper-layer coupling could also evade this local first-layer resolution floor.

Accordingly, (32) is a **negative resolution result**, not a lower bound on the true `RE-040` error and not a claim that the quantization route is impossible. It rules out only the naive version in which the half-unit spatial offset of one prime/event pair is expected to be visible at unspecified `o(1)` prime-race accuracy.

## 5. Prior-art boundary and research consequence

The CA critical-epsilon formula `F(p,1)=log(1+1/p)/log p` is classical Alaoglu--Erdos structure, already anchored in `SOURCES.md`; standard expositions of colossally abundant numbers use the same first-layer threshold. The PNT and Mertens-product inputs in (21)--(22) are classical and already part of the line's source environment. The current joint standard/reciprocal prime-race literature, including Bhattacharya--Martin--Simpson, studies correlations of the global error coordinates but does not supply the CA event selection or the prime/event staggering used here.

A targeted search found no need for a new load-bearing external theorem. No novelty is claimed for the reciprocal-log expansion, for the single-prime jumps, or for the critical-epsilon formula separately. The line-specific delta is their combination with `RE-036`--`RE-041`: **the first local arithmetic feature that survives the abstract support controls has a precisely identifiable normalized size, `log Z/sqrt(Z)`, and the present uniform selector theorem is still coarser than that size.**

This sharpens the post-`RE-041` frontier. Prime-power quantization remains the correct place to spend arithmetic information, but first-layer event location alone is insufficient at the current precision. A successful continuation must obtain a genuinely finer selector/race calibration with a placement theorem, or find a multi-atom/deeper-layer common-source constraint whose signal does not disappear at the square-root normalized scale.