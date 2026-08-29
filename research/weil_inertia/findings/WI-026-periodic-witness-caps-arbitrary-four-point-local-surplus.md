# WI-026 — the period-33 witness caps arbitrary same-pressure four-point block surplus below `0.673604`

**Status:** `EXACT-DERIVED + COMPUTATIONAL-INTERVAL + DECISIVE-NEGATIVE`. This is a strict barrier for the continuation left open in WI-025: keep the Montgomery--Taylor single-profile Gram defect, keep the same four-point span pressure `p=1/2500`, allow an arbitrarily strong universal local lower bound `D+P >= C_m` at every block length, and pass it through the same shifted-block assembly. The interval-certified period-33 countermodel from WI-019 forces every such block constant to be small enough that the final certified proportion remains strictly below `0.673604`. No optimality claim is made for the witness, and the result does not constrain multiple independent profiles, a different pressure ledger/global assembly, zeta-specific spacing input, the uncollapsed exceptional block, or support greater than one.

## 1. Statement

Retain the Montgomery--Taylor Gram defect

\[
D(G)=\operatorname{tr}\Psi(G),
\qquad
\Psi(t)=
\begin{cases}
(t-1)^2,&0\le t\le2,\\
2t-3,&t\ge2,
\end{cases}
\]

and, for an ordered `m`-point gap block `g_1,\ldots,g_{m-1}`, the same summed four-point pressure used in WI-009--WI-025,

\[
P_m(g)
:=p\sum_{i=1}^{m-3}(g_i+g_{i+1}+g_{i+2}),
\qquad
p=\frac1{2500},
\qquad m\ge4.
\tag{1}
\]

Suppose `C_m` is **any universal local constant** such that every ordered Montgomery--Taylor translation Gram block satisfies

\[
\boxed{D(G)+P_m(g)\ge C_m.}
\tag{2}
\]

No assumption is made about how `C_m` was proved; it may include arbitrary realizability surplus beyond the four-point certificate energy `A_m`. If the same shifted-block assembly as WI-025 is then used, the resulting proportion has the form

\[
R_m(C_m)
=
\frac{mH_{\rm MT}-3p(m-3)}{m-C_m}.
\tag{3}
\]

Then for every `m>=4`,

\[
\boxed{R_m(C_m)<\frac{673604}{10^6}=0.673604.}
\tag{4}
\]

Thus the `local surplus above A_m` escape explicitly listed in WI-025 cannot cross `0.673604` **while the local observable remains exactly `D+P_m` and the global pressure cancellation remains (3)**.

The bound is slightly stronger than the rounded `0.67361` collapsed-interface obstruction in WI-019 because the exact certified finite-sum and tail bounds from that witness leave a nonzero rational margin.

## 2. Certified period-33 input from WI-019

WI-019 supplies a positive periodic point configuration with `33` atoms per period and exact retained density

\[
r=\frac{67361}{100000}.
\tag{5}
\]

Its normalized period length is `L=33/r`. For the Montgomery--Taylor pair weight `w=k_{\rm MT}^2`, let

\[
d=\frac1{33}\sum_{a,b=1}^{33}\sum_{q\in\mathbb Z}'
 w\!\left(|x_b-x_a+qL|\right)
\tag{6}
\]

be the full directed quadratic energy per atom.

The directed MPFR replay in WI-019 proves

\[
d_{10000}<\frac{1637}{10^6},
\]

and its exact analytic tail estimate is

\[
d-d_{10000}
\le
\frac{45379580714321}{74507812500000000000}.
\]

Hence the durable exact upper bound is

\[
\boxed{
d<d_*:=
\frac{1637}{10^6}
+
\frac{45379580714321}{74507812500000000000}.
}
\tag{7}
\]

WI-019 also records the exact baseline enclosure

\[
H_{\rm MT}<H_*:=\frac{672500704}{10^9}.
\tag{8}
\]

The crucial self-consistency margin is therefore

\[
\delta
:=r(1-d_*)-H_*.
\tag{9}
\]

Direct rational reduction gives

\[
\boxed{
\delta
=
\frac{46091743024440123119}
{7450781250000000000000000}
>\frac6{10^6}.
}
\tag{10}
\]

The last comparison has exact positive difference

\[
\delta-\frac6{10^6}
=
\frac{1387055524440123119}
{7450781250000000000000000}>0.
\tag{11}
\]

No decimal evaluation of the period-33 energy is used below.

## 3. Phase averaging bounds every universal block constant

The key point is that the period-33 witness can be cut at all `33` possible phases. For a starting phase `a`, let `B_a` be the block of `m` consecutive periodic points starting there, with Gram `G_a`, quadratic energy

\[
E_a:=\operatorname{tr}(G_a-I)^2,
\]

defect `D_a:=D(G_a)`, and pressure `P_a:=P_m(B_a)`.

For one atom of phase `b`, let `e_b` be its directed interaction with **all** other atoms of the infinite periodic configuration. Positivity of `w` gives

\[
E_a
\le
\sum_{x\in B_a}e_{\operatorname{phase}(x)}.
\tag{12}
\]

As `a` runs through the `33` starts, each fixed relative position in the `m`-point block runs once through every phase. Therefore

\[
\frac1{33}\sum_{a=1}^{33}E_a
\le
\frac m{33}\sum_{b=1}^{33}e_b
=md.
\tag{13}
\]

Since `Psi(t)<=(t-1)^2` for every `t>=0`, every PSD Gram satisfies `D_a<=E_a`; hence

\[
\boxed{
\frac1{33}\sum_{a=1}^{33}D_a\le md.
}
\tag{14}
\]

The pressure averages just as cleanly. In (1) there are exactly `3(m-3)` gap occurrences. For any fixed relative gap position, averaging over the `33` start phases gives the mean periodic gap

\[
\frac L{33}=\frac1r.
\]

Consequently

\[
\boxed{
\frac1{33}\sum_{a=1}^{33}P_a
=
\frac{3p(m-3)}r.
}
\tag{15}
\]

Combining (14)--(15), at least one phase cut satisfies

\[
D_a+P_a
\le
md+\frac{3p(m-3)}r
<
md_*+\frac{3p(m-3)}r.
\tag{16}
\]

Any universal constant in (2) must hold on that block. Therefore, for **every** `m>=4`,

\[
\boxed{
C_m
<
md_*+\frac{3p(m-3)}r.
}
\tag{17}
\]

This is the finite-block form of the periodic-orbit obstruction. There is no boundary `O(1)` loss: averaging all phase cuts exactly removes it.

## 4. The local pressure cancels the global pressure tax exactly

The numerator in (3) is positive; for example WI-024 gives `H_MT>2/3` while `3p<1/800`. Hence `R_m(C)` is increasing in `C` throughout the relevant range. From (17), (8), and `a_m:=(m-3)/m`,

\[
R_m(C_m)
<
U_m
:=
\frac{
H_*-3p a_m
}{
1-d_*-(3p/r)a_m
}.
\tag{18}
\]

The denominator is positive: `d_*<819/500000` by WI-019 and `3p/r=120/67361<1/500`, so it is larger than `0.996`.

Now subtract (18) from the witness density `r`. The pressure terms cancel **exactly**:

\[
\begin{aligned}
r-U_m
&=
\frac{
r\bigl(1-d_*-(3p/r)a_m\bigr)
-igl(H_*-3p a_m\bigr)
}{
1-d_*-(3p/r)a_m
}\\[1mm]
&=
\boxed{
\frac{r(1-d_*)-H_*}
{1-d_*-(3p/r)a_m}
}
=
\frac{\delta}
{1-d_*-(3p/r)a_m}.
\end{aligned}
\tag{19}
\]

Because the denominator in (19) is strictly less than `1`, equations (10)--(11) imply

\[
r-U_m>\delta>\frac6{10^6}.
\tag{20}
\]

Using `r=0.673610` gives

\[
\boxed{U_m<0.673604}
\tag{21}
\]

uniformly for every block length `m>=4`. Equations (18)--(21) prove (4).

For orientation only, the limiting value of the rational upper envelope obtained from the certified `d_*` and `H_*` is

\[
\frac{H_*-3p}{1-d_*-3p/r}
=0.6736037926141771\ldots,
\tag{22}
\]

but the durable headline is the exact rational ceiling (4), not the decimal in (22).

## 5. What this closes relative to WI-025

WI-025 proves that merely recovering the original four-point energy `C_m=A_m` has the much lower asymptotic ceiling `0.6728549987...`. It correctly lists a stronger local inequality

\[
D+P_m\ge A_m+\sigma_m
\]

as a way to escape **that particular full-recovery ceiling**.

Equation (17) now quantifies how far such surplus can go inside the same universal single-profile block functional, while (19) shows why it cannot defeat the period-33 countermodel after the existing shifted assembly: the exact same span pressure added locally is subtracted globally at its periodic mean. Thus even an oracle returning the optimal universal value

\[
C_m^{\rm opt}
:=\inf_{\text{ordered }m\text{-point MT blocks}}(D+P_m)
\]

for every `m` cannot push (3) to `0.673604`.

This is stronger than saying that one particular packing proof has been exhausted. It closes **all universal local-surplus optimizations of the scalar `D+P_m` block constant under the same pressure ledger and same global assembly**.

## 6. Prior art and novelty audit

The general mechanism is classical in spirit and is not claimed as a new periodic-orbit principle:

- WI-014 already uses the standard fact that coboundary corrections have zero mean on periodic orbits to cap a Bellman retuning;
- Devine's August 2026 preprint publicly claims a `0.6736` wall for the fixed Montgomery--Taylor pure-Gram architecture;
- WI-019 supplies the stronger Mathia ingredient used here: an explicit period-33 off-lattice witness with a directed-interval certificate and exact tail bound.

A targeted search for the exact `0.673604` ceiling or the phase-averaged identity (17)--(19) in the four-point shifted-block setting found no matching public statement. Absence of a search hit is not a priority claim.

The durable new deduction is the exact bridge between WI-019 and the post-WI-025 local-surplus program: averaging all `33` phase cuts simultaneously controls Gram defect and span pressure with no boundary loss, and the local pressure then cancels the global pressure tax algebraically.

## 7. Boundaries and falsification tests

The obstruction is intentionally specific.

- **Universal gap-local inequalities only.** A theorem using a genuine zeta-specific spacing/correlation restriction may exclude the period-33 configuration and is outside (2).
- **Single Montgomery--Taylor profile.** Several genuinely independent bandlimited profiles retain information absent from one MT Gram and are not bounded by (17). Devine's `0.673399` claim uses exactly that escape and remains `NEEDS-AUDIT` in `SOURCES.md`.
- **Same pressure ledger and assembly.** Changing the local pressure coefficients or using a global Fenchel/Bellman construction whose bookkeeping is not (3) requires a new periodic-orbit calculation; the cancellation (19) cannot simply be assumed.
- **Collapsed simple-critical Gram contribution.** Nothing here prices the exceptional indefinite block or distinguishes critical-line multiplicity from screened off-line pairs.
- **Support greater than one.** New arithmetic information beyond the current support-one regime is outside the witness interface.

The decisive falsification test is finite and exact: produce some `m>=4` and a claimed universal constant `C_m` violating (17). Evaluating that claim on all `33` phase cuts of the WI-019 periodic witness and averaging must then contradict either the nonnegative-energy estimate (13), the exact pressure average (15), or the interval-certified bound (7).

## 8. Consequence for `weil_inertia`

After WI-025, `local surplus above A_m` looked like the nearest way to keep improving the same four-point block architecture. WI-026 shows that it is not a route to a qualitatively larger bound. Even perfect optimization of the universal local `D+P_m` constant at arbitrary block size remains below

\[
\boxed{67.3604\%}.
\]

A material next step must retain information the period-33 averaging discards: multiple independent profiles, a genuinely different global spectral coupling, an observable involving the exceptional block, or new zeta-specific/support-`>1` input. Merely strengthening the same scalar local block constant is now a closed route above this ceiling.
