# RE-013 — clean selector has a logarithmic prime-layer resolution barrier

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + FIXED-LAYER-FRONTIER-ASYMPTOTIC + FIXED-DEPTH-NONRESOLUTION + TWO-ADIC-DEPTH-BARRIER + LOGARITHMIC-RESOLUTION-SCALE + EXACT-MAXIMAL-LAYER-DEPTH + DEEP-TAIL-QUANTIZATION + ADDITIVE-UNIT-RESOLUTION + NEGATIVE/OBSTRUCTION + PRIOR-ART-BOUNDED`. `RE-006` shows that a clean regular self-tangent CA local peak is selected inside a prime gap by the exact higher-layer mass

\[
\Phi_{\ge2}(X)
=\sum_{\substack{r\ \mathrm{prime},\ j\ge2\\
                  \eta_{r,j}\le X}}\log r,
\qquad X=\log C,
\]

through

\[
X-p=\Phi_{\ge2}(X)-\bigl(p-\vartheta(p)\bigr),
\qquad p<X<q.
\tag{1}
\]

The admissible clean-peak window in `RE-006` has width on the logarithmic scale. `RE-007` extracts only the dominant second layer

\[
\Phi_2(X)=\sqrt{2X}+o(\sqrt X),
\]

which is enough for its square-root dichotomy but too coarse for the exact selector (1). The question is how many prime-power layers must be retained before the omitted selector mass is smaller than the scale being tested.

For each fixed layer `j>=2`, define

\[
\Phi_j(X)
:=\sum_{\substack{r\ \mathrm{prime}\\\eta_{r,j}\le X}}\log r,
\qquad
R_J(X):=\Phi_{\ge2}(X)-\sum_{j=2}^{J}\Phi_j(X).
\tag{2}
\]

Then, for every fixed `j>=2`,

\[
\boxed{
\Phi_j(X)=(jX)^{1/j}(1+o(1)).
}
\tag{3}
\]

Consequently every fixed truncation depth satisfies

\[
\boxed{
R_J(X)\ge\Phi_{J+1}(X)
=((J+1)X)^{1/(J+1)}(1+o(1))
\gg\log X.
}
\tag{4}
\]

Thus no fixed finite prime-layer frontier can determine the clean CA selector at the logarithmic resolution consumed by `RE-006`.

The variable-depth barrier is sharper and essentially discrete. Put

\[
J_X:=\left\lfloor\frac{\log X}{\log2}\right\rfloor.
\tag{5}
\]

For all sufficiently large `X`, no prime `r>=3` has an active layer above `J_X`. The remaining deep tail is therefore entirely `2`-adic. Moreover the prime `2` has the earliest event in every fixed layer, so its last active layer is the **global maximal active layer**. It is given exactly by

\[
\boxed{
J_*(X)
=
\left\lfloor
\log_2\!\left(
2+\frac1{\exp((\log2)/(X\log X))-1}
\right)
\right\rfloor-1.
}
\tag{6}
\]

Hence

\[
J_*(X)=\log_2X+\log_2\log X+O(1),
\tag{7}
\]

and, for every integer `J>=J_X`, the omitted selector mass has the exact quantized form

\[
\boxed{
R_J(X)=\bigl(J_*(X)-J\bigr)_+\log2.
}
\tag{8}
\]

The previous `J_X` boundary follows immediately:

\[
R_{J_X}(X)=\log\log X+O(1)=o(\log X).
\tag{9}
\]

But (8) gives the finer additive-resolution frontier that the earlier version of this finding left open. A uniformly bounded selector error requires

\[
J=J_*(X)-O(1)
=\log_2X+\log_2\log X+O(1),
\tag{10}
\]

while any error strictly smaller than `log 2` forces **exact recovery** of the higher-layer selector. In particular,

\[
\boxed{
R_{J(X)}(X)=o(1)
\quad\Longrightarrow\quad
R_{J(X)}(X)=0
\text{ eventually},
}
\tag{11}
\]

provided `J(X)>=J_X` eventually. Thus there is no nontrivial asymptotic regime of arbitrarily accurate but inexact depth truncation once the deep tail has become purely `2`-adic.

## 1. Every fixed prime-power layer has its own polynomial frontier

Retain the exact CA event definition from `RE-001`--`RE-007`. For a prime `r` and layer `j>=1`,

\[
\lambda_{r,j}
:=\log\frac{1-r^{-(j+1)}}{1-r^{-j}},
\qquad
\frac1{\eta_{r,j}\log\eta_{r,j}}
=\frac{\lambda_{r,j}}{\log r}.
\tag{12}
\]

The abundance increment is exactly

\[
\lambda_{r,j}
=\log\!\left(
1+\frac{r-1}{r(r^j-1)}
\right).
\tag{13}
\]

For fixed `j` and `r->infinity`,

\[
\frac{r-1}{r(r^j-1)}
=r^{-j}(1+O(r^{-1})),
\]

and therefore

\[
\lambda_{r,j}=r^{-j}(1+O(r^{-1})).
\tag{14}
\]

A layer is active at `X` exactly when

\[
\frac{\lambda_{r,j}}{\log r}
\ge\frac1{X\log X}.
\tag{15}
\]

If `y_j(X)` is the boundary prime for one fixed layer, (14)--(15) give

\[
y_j(X)^j\log y_j(X)
=X\log X\,(1+o(1)).
\tag{16}
\]

Since `log y_j(X)=(1/j)log X+O(1)`,

\[
\boxed{
y_j(X)=(jX)^{1/j}(1+o(1)).
}
\tag{17}
\]

The prime number theorem `vartheta(y)~y` then gives (3). Equation (4) follows from positivity because `R_J` contains the whole `(J+1)`st layer. Every positive power of `X` dominates `log X`, so adding any fixed number of layers cannot approximate (1) at its natural selector scale.

The fixed-`j` asymptotic is not used below when `j` grows with `X`.

## 2. The prime `2` forces logarithmically many active layers

At `r=2`, (13) becomes

\[
\lambda_{2,j}
=\log\!\left(1+\frac1{2(2^j-1)}\right)
=\log\!\left(1+\frac1{2^{j+1}-2}\right).
\tag{18}
\]

For `j>=2`, elementary logarithm bounds give

\[
\frac37\,2^{-j}<\lambda_{2,j}\le2^{-j}.
\tag{19}
\]

Thus if `j_2(X)` denotes the last active `2`-adic layer,

\[
j_2(X)=\log_2(X\log X)+O(1).
\tag{20}
\]

Every active `2`-layer contributes exactly `log2` to `Phi_(>=2)`. Hence for every `J<j_2(X)`,

\[
R_J(X)
\ge(j_2(X)-J)\log2
=\log X+\log\log X-J\log2+O(1).
\tag{21}
\]

In particular, `J=o(log X)` leaves `(1-o(1))log X` mass, and for every fixed `delta>0`,

\[
J\le(1-\delta)\frac{\log X}{\log2}
\quad\Longrightarrow\quad
R_J(X)\ge\delta\log X+\log\log X+O(1).
\tag{22}
\]

This lower bound uses one fixed prime only; no prime-distribution theorem enters it.

## 3. Depth `log_2 X` leaves only the `2`-adic tail

From (13) and `log(1+u)<=u`,

\[
\lambda_{r,j}\le r^{-j}.
\tag{23}
\]

If `(r,j)` is active at `X`, equations (15) and (23) imply

\[
\boxed{
r^j\log r\le X\log X.
}
\tag{24}
\]

Suppose `r>=3` and `j>J_X`. Since `j>log_2X`,

\[
r^j\log r
\ge3^j\log3
>X^{\log3/\log2}\log3,
\]

which eventually exceeds `X log X`, contradicting (24). Therefore every active layer above `J_X` belongs to `r=2` for all sufficiently large `X`.

Because the active `2`-layers are consecutive in `j`,

\[
R_{J_X}(X)
=(j_2(X)-J_X)\log2
=\log\log X+O(1),
\]

proving (9). This identifies the first coarse compression scale: depth asymptotic to `log_2 X` is sufficient to make the omitted selector `o(log X)`, while (21)--(22) show that a smaller fixed proportion of this depth is insufficient.

## 4. Prime `2` is the exact deepest layer and quantizes the additive tail

The deep-tail statement can be made exact because the prime `2` is not merely a convenient lower-bound witness. Rewrite (13) as

\[
\boxed{
\lambda_{r,j}
=\log\!\left(
1+\frac1{r+r^2+\cdots+r^j}
\right).
}
\tag{25}
\]

For fixed `j`, the denominator in (25) strictly increases with `r`, so `lambda_(r,j)` strictly decreases with `r`. At the same time `log r` strictly increases. Therefore

\[
\frac{\lambda_{r,j}}{\log r}
\]

strictly decreases with `r`. Since `g(x)=1/(x log x)` is strictly decreasing and

\[
g(\eta_{r,j})=\frac{\lambda_{r,j}}{\log r},
\]

the event coordinate `eta_(r,j)` strictly **increases** with `r`. Thus, for every layer `j`, its earliest possible event is the `2`-adic event. A layer is present anywhere at coordinate `X` if and only if its prime-`2` event has already occurred. Consequently

\[
\boxed{J_*(X)=j_2(X)}
\tag{26}
\]

is the global maximal active layer.

The exact formula (18) now determines `J_*` without asymptotic inversion. Put

\[
a_X:=\frac{\log2}{X\log X}.
\]

The layer `j` is active exactly when

\[
\lambda_{2,j}\ge a_X,
\]

or equivalently

\[
2^{j+1}
\le2+\frac1{e^{a_X}-1}.
\tag{27}
\]

Taking the largest integer `j` gives (6). Since

\[
\frac1{e^{a_X}-1}
=\frac{X\log X}{\log2}+O(1),
\]

(7) follows.

Combine (26) with the conclusion of Section 3. Once `J>=J_X`, every omitted active layer is a `2`-adic layer, and every such layer has the same selector weight `log2`. Therefore

\[
R_J(X)
=\#\{j:J<j\le J_*(X)\}\log2
=\bigl(J_*(X)-J\bigr)_+\log2,
\]

which is (8).

For a fixed tolerance `epsilon>=0`, the least sufficiently deep truncation satisfying `R_J(X)<=epsilon` is, for all sufficiently large `X`,

\[
\boxed{
J_{\min,\varepsilon}(X)
=J_*(X)-\left\lfloor\frac{\varepsilon}{\log2}\right\rfloor.
}
\tag{28}
\]

Here `X` is large enough that the right side exceeds `J_X`; for fixed `epsilon` this follows from `J_*(X)-J_X~log_2log X`. Thus `O(1)` additive accuracy costs the additional `log_2log X` layer depth hidden by the coarse `J_X` boundary. If `epsilon<log2`, (28) gives `J_min=J_*`, so the truncation is already exact. This proves (10)--(11).

## 5. Why this matters after the local-jet closure

`RE-012` proves that once the exact selector `(X,Phi_(>=2)(X))` is known, the entire smooth mixed-race profile inside the surrounding prime-free chamber is determined by one value `mathscr Y(X)` plus that selector. A natural compression attempt is therefore to replace the exact higher-layer mass by a finite layer expansion and hope that local value/slope data repairs the missing correction.

Equations (4) and (21) rule this out at fixed or subcritical depth: the missing selector mass is at least as large as the complete logarithmic clean-peak window. Equation (9) gives the first useful positive boundary: depth `J_X~log_2X` reduces the error to `log log X+O(1)`, which is enough for some coarse mean-gap-scale questions but not for exact self-tangency.

The exact deep-tail law (8) closes the remaining additive-resolution ambiguity. To make the selector error bounded one must retain essentially all layers through the global maximum, missing only `O(1)` of them. To make the error `o(1)` one eventually cannot omit even one active deep layer. Thus a depth-truncated selector has no smoothly improving subunit regime: its final uncertainty arrives in indivisible quanta of `log2`.

The second-layer normal form of `RE-007` remains useful at square-root scale, where all higher layers are lower order. The present result says only that the same finite-depth approximation cannot later be reused as though it were accurate on logarithmic or additive-unit selector scales.

## 6. Prior art and novelty boundary

The individual ingredients are classical or already represented in this line's sources. Alaoglu--Erdos supplies the CA exponent-threshold framework; the exact event normalization and prime-layer workload are closest to Mantovanelli's August 2026 preprint; the prime number theorem converts a fixed layer's boundary prime into its weighted mass. No novelty is claimed for the existence of many exponent layers, for classical CA exponent asymptotics, or for the square-root prime frontier.

A targeted audit of the current CA/Robin source record and the public Mantovanelli companion did not identify the specific selector-resolution statements proved here: fixed depth cannot reach the logarithmic window; depth `J_X~log_2X` leaves exactly a `log log X+O(1)` deep tail; the prime `2` is the exact maximal active layer; and the remaining tail above `J_X` is quantized as (8), making sub-`log2` accuracy equivalent to exact depth recovery. These are elementary consequences once the exact event representation is admitted and should be read as Mathia-specific selector bookkeeping, not as a blanket novelty claim about colossally abundant numbers.

No new source anchor is required. All non-elementary inputs are already recorded in `SOURCES.md`; equations (25)--(28) are elementary consequences of the exact layer threshold.

## 7. Falsification boundaries and research consequence

Several quantifiers are load-bearing. Equation (3) is a fixed-layer asymptotic and must not be used with `j~log X`; the growing-depth results use only exact event inequalities. The exact tail formula (8) applies in the sufficiently deep regime `J>=J_X` and for sufficiently large `X`, after Section 3 has eliminated every prime `r>=3` from deeper layers. It does not say that prime `2` dominates the selector at shallow depths.

The additive quantization is specific to **layer-depth truncation**. It does not rule out a different compressed representation of the exact selector, nor an independent arithmetic theorem that controls discarded layers without enumerating them. Likewise, `o(1)` in (11) concerns selector mass, not the selected mixed-race value or the Robin height.

Most importantly, this finding does not bound the selected mixed race `mathscr Y`, prove that high mixed-race values avoid self-tangent coordinates, or control the exceptional higher-layer/tied boundary chamber of `RE-004`. It therefore does not prove Robin's inequality or RH.

Its durable effect is to close the finite-layer compression hierarchy after `RE-012`. The nonlocal CA selector is genuinely multiscale: fixed depth fails at logarithmic resolution, `Theta(log X)` depth reaches `o(log X)`, and additive-unit resolution requires the sharper depth `log_2X+log_2log X+O(1)`, with subunit accuracy collapsing to exact recovery. A future selected-race theorem may use a compressed selector only if it carries this growing-depth information or supplies an independent theorem controlling what was discarded.