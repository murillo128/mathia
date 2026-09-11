# RE-059 — fixed threshold cells freeze the adjusted standard and reciprocal prime sources

**Status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + FIXED-CHAMBER-SOURCE-INVARIANCE + BINARY-FRINGE-LAW + ADAPTIVE-FAN-INFORMATION-COMPRESSION + COUNTEREXAMPLE-NARROWING + PRIOR-ART-CLASSIFIED`.

`RE-040` upgrades hypothetical false-RH behavior to a whole compact threshold fan on common positive CA counterexample blocks, and `RE-036`--`RE-037` place every selected tangent parameter on a coupled standard/reciprocal prime-race curve. It is tempting to regard the continuum of threshold parameters inside one exposed cell as a continuum of independent arithmetic samples. That interpretation is false.

Fix one exposed regular CA state `C` and let

\[
Y:=\log C,
\qquad
h:=\log G(C)-\gamma>0,
\qquad
a:=1-e^{-h}.
\tag{1}
\]

Let `I_C` be any positive-width threshold cell on which `C` is the selected state, and for `b\in I_C^\circ` let `Z=Z_C(b)` be the adaptive tangent parameter,

\[
g(Z)=g(Y)-\frac{ba}{Y},
\qquad
g(x)=\frac1{x\log x}.
\tag{2}
\]

By `RE-040`, every such `Z` lies in the same open genuine CA support chamber of `C`. Put

\[
P_C:=\Phi_{\ge2}(Z),
\tag{3}
\]

which is independent of `Z` throughout that chamber, and retain the finite-exponent tail

\[
T(C):=-\sum_{p\mid C}\log(1-p^{-(a_p+1)}).
\tag{4}
\]

Let `\delta_\vartheta(Z)` and `\delta_\ell(Z)` be the common-source first-layer endpoint corrections of `RE-036` and `RE-045`: if an ordinary prime `r\le Z` has been crossed before its delayed first-layer CA event `\eta_r`, then

\[
\delta_\vartheta(Z)=\log r,
\qquad
\delta_\ell(Z)=-\log(1-r^{-1}),
\tag{5}
\]

and otherwise both are zero. Define

\[
M(Z):=\sum_{p\le Z}-\log(1-p^{-1}).
\tag{6}
\]

Then throughout the entire selected cell one has the two **exact source invariants**

\[
\boxed{
\vartheta(Z)-\delta_\vartheta(Z)=Y-P_C,
}
\tag{7}
\]

and

\[
\boxed{
M(Z)-\delta_\ell(Z)
=\gamma+h+T(C)+\log\log Y.
}
\tag{8}
\]

Equivalently, the adjusted standard-prime mass and adjusted reciprocal-prime mass do not change at all as `b` moves through a fixed threshold cell. They are simply the two first-layer statistics of the fixed active prime set of `C`:

\[
Y-P_C
=\sum_{p\mid C}\log p,
\tag{9}
\]

\[
\gamma+h+T(C)+\log\log Y
=\sum_{p\mid C}-\log(1-p^{-1}).
\tag{10}
\]

`RE-052` implies that the whole support chamber contains at most one ordinary prime. Hence there is at most one optional fringe prime `r_C` for the cell, and the **raw** source pair itself has at most two values:

\[
\boxed{
(\vartheta(Z),M(Z))
=(Y-P_C,\,\gamma+h+T(C)+\log\log Y)
+\chi_C(Z)\,
(\log r_C,-\log(1-r_C^{-1})),
}
\tag{11}
\]

where `\chi_C(Z)\in\{0,1\}` and, because `Z_C(b)` is increasing, `\chi_C(Z_C(b))` can switch at most once as `b` crosses the cell.

Thus a positive-width threshold cell does **not** supply a continuum of new prime-source observations. Once the fixed state is known, the entire continuum is a deterministic reparameterization of one frozen source vector, with at most one binary unmatched-prime correction. The continuously varying normalized coordinates `U(Z)` and `V(Z)` of `RE-036` do not contradict this: their variation comes from the changing external coordinate `Z`, its normalization, and the adaptive tangent map, not from new prime atoms entering the adjusted source.

This materially narrows the use of the compact false-RH fan. Any contradiction that treats many `b` values inside one cell as independent standard/reciprocal prime-race constraints is counting the same arithmetic data repeatedly. New prime-source information can enter only when the fan crosses a genuine CA support boundary, or through the single transient fringe bit already isolated in `RE-045`--`RE-050`. Therefore the live source-sensitive problem is necessarily **cross-cell**: control the number, ordering, cumulative mass, or mutual dependence of the genuine event updates, rather than amplify the continuum inside one fixed chamber.

## 1. The standard prime source is exactly constant after the endpoint correction

The exact source decomposition used in `RE-036` and `RE-045` is

\[
q-q_0
=\frac{P_C-\delta_\vartheta(Z)}{Z\log Z},
\tag{12}
\]

where

\[
q:=\frac{Z-\vartheta(Z)}{Z\log Z},
\qquad
q_0:=\frac{Z-Y}{Z\log Z}.
\tag{13}
\]

Multiplying (12) by `Z\log Z` gives

\[
Y-\vartheta(Z)=P_C-\delta_\vartheta(Z),
\tag{14}
\]

which is exactly (7).

There is also a direct event interpretation. Inside one open support chamber no CA event fires, so the exponent vector of `C` is fixed. The total active event mass is

\[
Y=\Phi(Z)
=\sum_{j\ge1}\sum_{\eta_j(p)\le Z}\log p.
\tag{15}
\]

Its depth-at-least-two part is `P_C`, so the active first-layer mass is `Y-P_C`. An ordinary prime can enter the raw Chebyshev sum before its first-layer CA event only during the delay interval `(p,\eta_p)`. Subtracting `\delta_\vartheta` removes precisely that unmatched atom. Hence the adjusted Chebyshev source equals the fixed first-layer mass of `C` identically, not merely asymptotically.

This argument is insensitive to whether the chamber boundaries themselves are first-layer, higher-layer, or tied events. Only the open chamber matters, and there are no event coordinates in its interior by definition.

## 2. The reciprocal prime source is frozen by the same active set

Write the logarithmic Mertens-product error as in `RE-036`,

\[
E(Z)=M(Z)-\gamma-\log\log Z.
\tag{16}
\]

For every selected pair `(C,Z)`, the exact Euler-product factorization is

\[
h
=E(Z)-\delta_\ell(Z)-T(C)
+\log\frac{\log Z}{\log Y}.
\tag{17}
\]

Substituting (16) into (17), the two `\log\log Z` terms cancel exactly:

\[
\begin{aligned}
h
&=M(Z)-\gamma-\log\log Z
-\delta_\ell(Z)-T(C)\\
&\qquad+\log\log Z-\log\log Y.
\end{aligned}
\tag{18}
\]

Therefore

\[
M(Z)-\delta_\ell(Z)
=\gamma+h+T(C)+\log\log Y,
\tag{19}
\]

which proves (8).

Again there is a direct factorization check. Since

\[
\frac{\sigma(C)}C
=\prod_{p\mid C}
\frac{1-p^{-(a_p+1)}}{1-p^{-1}},
\tag{20}
\]

we have

\[
\log\frac{\sigma(C)}C
=\sum_{p\mid C}-\log(1-p^{-1})-T(C).
\tag{21}
\]

Using

\[
\log G(C)=\log\frac{\sigma(C)}C-\log\log Y
=\gamma+h,
\tag{22}
\]

immediately yields (10). Thus the adjusted reciprocal source is the reciprocal-prime statistic of exactly the same fixed active first-layer set that appears in (9).

The cancellation in (18) explains why moving the tangent parameter through a prime-free part of the chamber cannot create new Mertens information. `E(Z)` changes smoothly because its normalization contains `-\log\log Z`, while the exact Robin factorization contains the opposite `+\log\log Z` change. The physical state has not changed, so those two coordinate effects must cancel.

## 3. One support chamber carries at most one binary source update

`RE-052` proves that for sufficiently large states the open support chamber `(\xi_-,\xi_+)` of `C` contains no ordinary prime in

\[
(\xi_-,\xi_+-1/2],
\tag{23}
\]

and therefore contains at most one ordinary prime in total. Call it `r_C` if it exists. Since the first-layer event coordinate obeys

\[
r_C<\eta_{r_C}<r_C+\frac12,
\tag{24}
\]

an ordinary-source contribution can be present without its CA first-layer contribution only after `Z` crosses `r_C` and before the corresponding event fires. Inside the fixed support chamber this is exactly the endpoint correction (5).

Consequently equations (7)--(8) give the raw two-valued law (11). If the chamber contains no fringe prime, `\chi_C\equiv0`. If it contains one, then

\[
\chi_C(Z)=\mathbf 1_{\{r_C\le Z\}}
\tag{25}
\]

through the part of the chamber sampled by the cell. The selector speed from `RE-052` satisfies

\[
Z_C'(b)>0,
\tag{26}
\]

so the bit changes at most once as `b` increases.

This is stronger than merely saying that the chamber is mostly prime-free. After the paired endpoint correction, **both** prime-source coordinates are exactly frozen across the whole chamber, including across the possible raw ordinary-prime jump. Without the correction the only remaining source variation is one quantized prime atom, simultaneously visible in the standard and reciprocal coordinates.

The binary law is the fixed-cell analogue of the adjacent-switch phenomenon in `RE-045`. There the selected residual difference across a first-layer state change loses the generating prime and detects only a possible upper fringe prime. Here the state does not change at all, so there is not even a generating-event update: the only possible first-layer source change is the same unmatched fringe mechanism.

## 4. The continuum nonlinear race curve is a reparameterization, not independent arithmetic data

The exact nonlinear normal form of `RE-036` may make the family of selected points look richer because both normalized coordinates vary with `Z`:

\[
U(Z)=\frac{Z-\vartheta(Z)}{\sqrt Z},
\qquad
V(Z)=E(Z)\sqrt Z\log Z.
\tag{27}
\]

But equations (7)--(8) show that, inside a fixed cell, these are determined explicitly by `Z`, the fixed constants `Y`, `P_C`, `h`, `T(C)`, and the single bit `\chi_C(Z)`. Indeed,

\[
\vartheta(Z)=Y-P_C+\delta_\vartheta(Z),
\tag{28}
\]

and

\[
E(Z)
=h+T(C)+\delta_\ell(Z)
-\log\frac{\log Z}{\log Y}.
\tag{29}
\]

Meanwhile `b` itself is already determined by `Z` through (2):

\[
\boxed{
b
=\frac{Y}{a}\bigl(g(Y)-g(Z)\bigr).}
\tag{30}
\]

Thus the map

\[
b\longmapsto (Z,U(Z),V(Z))
\tag{31}
\]

contains no additional continuously varying source degree of freedom once the state and its fixed CA summaries are specified. The nonlinear `\Psi_{b,\log Z}` relation is an exact compatibility law for this reparameterization; sampling it at more values of `b` inside the same cell does not repeatedly interrogate new primes.

The same point can be read from the source-separated residual expansion in `RE-045`: inside one chamber `P_C` and `T(C)` are fixed, while all first-layer variation is carried by the paired endpoint corrections. Continuous changes of the coefficients multiplying these fixed quantities are geometric normalization effects, not new independent arithmetic inputs.

This distinction matters for any proposed compact-fan contradiction. A proof cannot gain strength proportional to the cardinality or continuum size of `I_C` by treating each threshold as an independent prime-race constraint. The arithmetic information content of one cell is finite: one fixed active first-layer set, fixed higher-layer mass/tail summaries, and at most one fringe atom.

## 5. Consequence for the near-critical false-RH program

`RE-039` shows that the adaptive amplitude envelope is algebraically programmable without arithmetic. `RE-040` restores genuine CA support and a uniform standard/reciprocal race law. `RE-052` then converts physical cell width into ordinary-prime-free selector length, while `RE-054`--`RE-058` progressively show that all-layer synchronization and integer labels can be faked until the ordinary `sigma` response forces the labels back to genuine primes.

The present result isolates what the **continuum inside one genuine-prime cell** can and cannot contribute. Genuine primality does not make different `b` values inside that cell new source samples. The active prime set is frozen until a CA support event occurs. Hence a source-specific continuation must obtain leverage from at least one of the following genuinely cross-cell objects: the number of exposed cells, the ordering and type of their boundary events, cumulative first- and higher-layer mass across those boundaries, or a dependence between successive updates of the standard and reciprocal prime statistics.

This does not weaken the capacity results. A wide cell still forces a wide physical selector image and therefore a long prime-free interval by `RE-052`. What it rules out is a different hoped-for amplification: **continuum threshold width cannot be converted into continuum prime-race independence inside the same chamber.** The width is geometric capacity; the source only updates at events.

The result also leaves the mixed-race height route of `RE-008`--`RE-022` open. The fixed constants `P_C` and `T(C)` and the historical value encoded by the active prime set may still carry decisive global information. Equation (11) says only that varying `b` while holding `C` fixed does not reveal additional history. Any successful height/selector splice must therefore compare different selected states or control an accumulated source integral, not re-sample one state at many thresholds.

## 6. Prior-art boundary and limitations

The underlying structural pieces are classical or already line-internal. Alaoglu--Erdos gives the prime-exponent threshold description of colossally abundant numbers, so constancy of the exponent vector between adjacent parameter events is not a novelty claim. Mantovanelli's 2026 prime-layer workload framework explicitly organizes CA states by discrete event gaps, and Kalyabin's 2026 work is neighboring prior art for relations between Gronwall extrema and modified Mertens remainders. A targeted literature audit found those boundaries but no external theorem whose claimed content is the specific joint information-compression statement (7)--(11) for Mathia's adaptive threshold cells.

No new external theorem is load-bearing here. Equations (7)--(8) are exact consequences of the source decompositions already established in `RE-036` and made concrete in `RE-045`, plus the one-prime support-chamber fact of `RE-052`. Accordingly `SOURCES.md` is unchanged, and no priority claim is made for the elementary identities themselves. The useful delta is their consequence for the research strategy: the compact threshold continuum has only finite first-layer source information inside each fixed CA chamber.

Several boundaries are essential. The normalized coordinates `U(Z)` and `V(Z)` are **not** constant; only the endpoint-corrected underlying prime sums are. The higher-layer quantity `P_C` and exponent tail `T(C)` are frozen only while the selected state remains `C`; they can change at the next CA event and may carry genuine arithmetic information. The theorem does not bound the number of cells, does not exclude the near-critical fan, and does not prove any new prime-gap theorem. It also does not assert statistical independence or dependence between different cells.

Finally, the possible fringe bit is not a nuisance that may simply be discarded. `RE-045`--`RE-050` show that its recurrence can encode sharp event-edge information. The present theorem says precisely where such information lives: **at a discrete unmatched prime/event boundary, not in the continuous interior of a threshold cell.**