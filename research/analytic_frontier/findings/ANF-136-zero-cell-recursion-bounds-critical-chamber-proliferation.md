# ANF-136 — zero-cell recursion bounds critical chamber proliferation

**Status:** `EXACT-DERIVED + DEPTH-QUANTITATIVE-INVARIANT + POSITIVE-TRANSLATION-CASCADE + ZERO-CELL-COUNT + CHAMBER-PROLIFERATION-BOUND + FLOOR-RATE-SEPARATION + PREFATOR-CONDITIONING-GATE`. `ANF-135` leaves two explicitly depth-sensitive quantities outside its factorial slack control: the unweighted number `J_d` of critical chambers and the finite-`A` floor/Laplace prefactor. The chamber count is not free. In the fixed-`q` `ANF-129`--`ANF-135` cascade, every critical chamber lies in a zero-free cell of an explicit product of one digit factor and the historical binomial annihilators, and the pressure is strictly concave on each such cell. Because `ANF-134` forces every stage-`d` critical point to satisfy `xi >= delta_d`, a binomial targeting that point has at most `1/delta_d` zeros in `(0,1)`. This gives the recursion

\[
\boxed{
C_d\le C_{d-1}\left(1+\frac1{\delta_{d-1}}\right),
\qquad J_d\le C_d,
}
\tag{1}
\]

where `C_d` is the number of zero-free cells of the stage-`d` limiting pressure. Combining (1) with the factorial-scale slack lower bound of `ANF-135` yields

\[
\boxed{
J_d\le C_d\le \exp\!\bigl(O_q(d^2\log(d+2))\bigr).
}
\tag{2}
\]

The cumulative number of binomial factors through depth `d` obeys the same scale. Hence every diagonal depth satisfying

\[
\boxed{
D(A)^2\log(D(A)+2)=o(\log A)
}
\tag{3}
\]

has only `A^{o(1)}` critical chambers and historical annihilator factors. In that regime the global copy-rate error caused by replacing every ideal repetition `theta_k A` by `floor(theta_k A)` is only `A^{-1+o(1)}`, and at any point where all active factors are nonzero the floor replacement changes the squared modulation by at worst an `exp[-A^{o(1)}]` factor. Thus **raw chamber proliferation and coefficient-mass rounding are not the remaining diagonal obstruction**.

The unresolved source-prefactor gate becomes more specific. A stage can still place its active maximum arbitrarily close to a zero of a very low-density historical factor, creating a badly conditioned and potentially extremely narrow critical cell. Neither the weighted copy-rate budget nor (1)--(3) lower-bounds that zero distance. A complete diagonal source theorem therefore needs a local conditioning statement—such as a lower bound on critical-cell width, a usable Hessian bound, or an equivalent finite-`A` integral estimate—not another bound on the mere number of chambers.

## 1. Every critical chamber occupies a distinct zero-free cell

Fix `gamma>0` and a sufficiently large fixed digit arity `q` from `ANF-129`. Use the stage notation of `ANF-135`. The seed pressure is

\[
B_q(\alpha)
=F_\gamma(\alpha)-f_\gamma
+2r_q\log|D_q(d_q\alpha)|,
\tag{4}
\]

and after `d` first-critical retunings the limiting pressure is

\[
G_d(\alpha)
=B_q(\alpha)
+2\sum_{k=1}^{d}\theta_k
\sum_{j=1}^{J_{k-1}}
\log\left|
1+e^{-2\pi i\tau_{j,k-1}\alpha}
\right|,
\tag{5}
\]

with

\[
\tau_{j,k-1}=\frac1{2\xi_{j,k-1}}.
\tag{6}
\]

Let `Z_d` be the union in `(0,1)` of the zero set of the fixed digit factor in (4) and the zeros of every binomial appearing in (5). Let

\[
C_d:=\#\pi_0\bigl((0,1)\setminus Z_d\bigr)
\tag{7}
\]

be the number of connected zero-free cells. The seed contributes only a fixed finite number `C_0=O_q(1)` because `q`, `gamma`, and `d_q` are fixed.

On every zero-free cell, `G_d` is smooth and strictly concave. The base curvature is strictly negative,

\[
F_\gamma''(\alpha)
=-\frac{\gamma\pi^2}{2}
\sec^2\frac{\pi\alpha}{2}<0.
\tag{8}
\]

For the digit factor, `ANF-133` records on every zero-free cell

\[
\frac{d^2}{dx^2}\log|D_q(x)|
=-\pi^2q^2\csc^2(\pi qx)
+\pi^2\csc^2(\pi x)<0,
\tag{9}
\]

and composition with `d_q alpha` preserves the sign. Each binomial contributes

\[
\frac{d^2}{d\alpha^2}
\log\left|1+e^{-2\pi i\tau\alpha}\right|
=-\pi^2\tau^2\sec^2(\pi\tau\alpha)<0
\tag{10}
\]

where finite. Therefore

\[
\boxed{G_d''(\alpha)<0}
\tag{11}
\]

on every cell. There is at most one maximizer in each cell. Since an active zero has pressure `-infinity`, no source-critical point lies in `Z_d`. Hence the stage-`d` critical skeleton satisfies

\[
\boxed{J_d\le C_d.}
\tag{12}
\]

This uses only the exact product architecture. No generic zero-count theorem for arbitrary exponential sums is needed.

## 2. Slack bounds the number of new zeros introduced by one layer

Consider a stage-`d-1` critical point `xi=xi_{j,d-1}`. Its annihilator factor is

\[
1+e^{-2\pi i\alpha/(2\xi)}
=1+e^{-\pi i\alpha/\xi}.
\tag{13}
\]

Its positive zeros are exactly

\[
\alpha=(2n+1)\xi,
\qquad n=0,1,2,\ldots.
\tag{14}
\]

The number lying in `(0,1)` is therefore

\[
N(\xi)
:=\#\{n\ge0:(2n+1)\xi<1\}
\le \frac1\xi.
\tag{15}
\]

`ANF-134` gives the stagewise geometric lower bound

\[
\xi_{j,d-1}\ge\delta_{d-1}.
\tag{16}
\]

Consequently every factor in the new annihilator contributes at most `1/delta_{d-1}` zeros to `(0,1)`. Coincident zeros only reduce the number of new cells, so

\[
C_d
\le C_{d-1}
+\frac{J_{d-1}}{\delta_{d-1}}.
\tag{17}
\]

Using (12),

\[
\boxed{
C_d
\le
C_{d-1}
\left(1+\delta_{d-1}^{-1}\right),
}
\tag{18}
\]

which is (1). Notice what repetition does **not** do: the density `theta_d` and the physical multiplicity `floor(theta_d A)` change the order of the existing zeros but create no new zero locations. Chamber complexity is charged once per distinct annihilator factor, not once per physical copy.

This recursion is deliberately coarse. It counts every zero of every binomial even when several factors share zeros and even when many zero-free cells contain no critical point. That is useful here because it requires no transversality or separation hypothesis between regenerated saddles.

## 3. Factorial slack turns the cell recursion into an `exp(O(d^2 log d))` bound

Set, as in `ANF-135`,

\[
L_d:=\log\frac{\delta_0}{\delta_d}.
\tag{19}
\]

That finding proves

\[
L_d\le K_q(d+1)\log(d+2)
\tag{20}
\]

for a fixed seed-dependent constant `K_q`. Iterating (18) gives

\[
\log C_d
\le
\log C_0
+\sum_{k=0}^{d-1}
\log\left(1+\delta_k^{-1}\right).
\tag{21}
\]

Since

\[
\delta_k^{-1}=\delta_0^{-1}e^{L_k},
\]

there is a fixed constant `K_q'` such that

\[
\log\left(1+\delta_k^{-1}\right)
\le
K_q'\bigl(1+(k+1)\log(k+2)\bigr).
\tag{22}
\]

Summing,

\[
\boxed{
\log C_d
\le
K_q''(d+1)^2\log(d+2),
}
\tag{23}
\]

and (2) follows from (12).

Let

\[
H_d:=1+\sum_{k=0}^{d-1}J_k
\tag{24}
\]

count the seed plus all historical binomial factors, without their repetition multiplicities. Because `J_k<=C_k` and `C_k` is nondecreasing,

\[
H_d\le1+dC_d,
\]

so after enlarging the constant,

\[
\boxed{
H_d
\le
\exp\!\bigl(O_q(d^2\log(d+2))\bigr).
}
\tag{25}
\]

Therefore (3) implies

\[
\boxed{
C_{D(A)}=A^{o(1)},
\qquad
J_{D(A)}=A^{o(1)},
\qquad
H_{D(A)}=A^{o(1)}.
}
\tag{26}
\]

This diagonal window is stricter than the pressure-only window `D log D=o(log A)` in `ANF-135`, but it is still unbounded and completely explicit. In particular, the mere number of regenerated chambers does not have to become polynomial, let alone exponential, in the physical scale `A` before the depth tends to infinity.

## 4. Global floor-rate error is negligible in the same diagonal window

The ideal copy-count rate through depth `d` is

\[
R_d
=r_q\log q
+\sum_{k=1}^{d}
\theta_kJ_{k-1}\log2.
\tag{27}
\]

At finite `A`, implement exactly the physical repetitions used in `ANF-129` and `ANF-133`,

\[
h_A=\lfloor r_qA\rfloor,
\qquad
m_{k,A}=\lfloor\theta_kA\rfloor.
\tag{28}
\]

The actual logarithmic coefficient/copy-mass rate is

\[
R_{d,A}^{\rm phys}
=\frac{h_A}{A}\log q
+\sum_{k=1}^{d}
\frac{m_{k,A}}A J_{k-1}\log2.
\tag{29}
\]

Hence exactly

\[
0\le R_d-R_{d,A}^{\rm phys}
<\frac{\log q+H_d\log2}{A}.
\tag{30}
\]

Under (3), (25) gives

\[
\boxed{
R_d-R_{d,A}^{\rm phys}=A^{-1+o(1)}.
}
\tag{31}
\]

Moreover `ANF-135` gives in this stricter window

\[
\delta_d=f_\gamma-2R_d=A^{-o(1)},
\tag{32}
\]

so the floor-rate discrepancy is negligible compared with the remaining ideal slack:

\[
\frac{R_d-R_{d,A}^{\rm phys}}{\delta_d}\longrightarrow0.
\tag{33}
\]

Because flooring only decreases `R`, the actual positive coefficient mass has at least as much global copy-rate slack as the ideal limiting cascade. Thus the finite-`A` obstruction identified after `ANF-135` is not a failure of the total coefficient-mass budget.

There is also a pointwise one-sided control. Let

\[
\mathcal M_{d,A}^{\rm ideal}(\alpha)
:=D_q(d_q\alpha)^{r_qA}
\prod_{k=1}^{d}Q_{k-1}(\alpha)^{\theta_kA}
\tag{34}
\]

be understood only through its modulus, and let `mathcal M_phys` use the integer exponents (28). At any `alpha` where all active factors are nonzero,

\[
\frac{|\mathcal M_{d,A}^{\rm phys}(\alpha)|^2}
{|\mathcal M_{d,A}^{\rm ideal}(\alpha)|^2}
=
|D_q(d_q\alpha)|^{-2\{r_qA\}}
\prod_{k=1}^{d}
|Q_{k-1}(\alpha)|^{-2\{\theta_kA\}}.
\tag{35}
\]

Since `|D_q|<=q` and `|Q_{k-1}|<=2^{J_{k-1}}`, each factor with modulus below one only increases the ratio, while a factor above one loses at most the square of its coefficient mass. Therefore

\[
\boxed{
\frac{|\mathcal M_{d,A}^{\rm phys}(\alpha)|^2}
{|\mathcal M_{d,A}^{\rm ideal}(\alpha)|^2}
\ge
q^{-2}4^{-\sum_{k<d}J_k}.
}
\tag{36}
\]

At a current ideal critical chamber every active factor is nonzero, so (25)--(26) imply that flooring changes its **pointwise exponential rate** by only

\[
\frac1A O(H_d)=A^{-1+o(1)}.
\tag{37}
\]

This is not an integral source lower bound. It isolates what flooring can and cannot be blamed for.

## 5. Adversarial boundary: the remaining problem is local conditioning, not cell count

The estimates above do **not** prove

\[
E_0(X_A^{(D(A))})\asymp E_A.
\tag{38}
\]

There are two reasons not to promote (26) or (36) to that conclusion.

First, (36) is pointwise at a zero-free location. A point contributes no mass by itself. To obtain an integral lower bound one needs a neighborhood on which the pressure remains close to its maximum. The strict concavity in (11) proves uniqueness within a cell but gives no depth-uniform lower bound on the cell width or upper bound on the magnitude of the Hessian at its maximizer.

Second, the weighted budget does not control distance from a maximum to every historical zero. A layer with extremely small density can put a zero extremely close to a later critical point while paying very little in `theta_k J_{k-1}`. Its logarithmic term can then have very large local curvature even though its contribution to copy rate and to the zero **count** is small. Equations (18)--(26) do not exclude this mechanism.

This also explains why a generic trigonometric-polynomial degree bound would not close the problem. Classical finite Riesz products and zero-count bounds control how many oscillatory cells can occur, but they do not supply the Mathia-specific lower bound on the width or source mass of the particular cell selected by repeated first-critical pressure retuning. The exact binomial zero formula (14), rather than an external zero-count theorem, is load-bearing here. A directed prior-art audit against classical Riesz-product constructions, trigonometric-polynomial zero counts, and Laplace asymptotics with multiple saddles did not identify a theorem that supplies the missing depth-uniform critical-cell conditioning for this architecture. No new `SOURCES.md` dependency is introduced.

The next same-profile gate is therefore sharper than the boundary stated in `ANF-135`: prove one of the following equivalent-in-purpose controls along an unbounded diagonal depth—(i) a lower bound on the distance from an active critical point to every relevant historical zero strong enough for integration, (ii) an upper bound on the negative Hessian/conditioning of the active cell, or (iii) a direct finite-`A` lower bound for the source mass carried by at least one active cell. A counterexample showing superexponentially narrowing cells despite (2) would instead identify the genuine failure mechanism.

**Bottom line.** `ANF-135` showed that copy-rate slack cannot collapse faster than factorial scale. The same slack also prevents uncontrolled *combinatorial* chamber explosion: `J_d` is at most `exp(O_q(d^2 log d))`, so a depth `D(A)->infinity` with `D(A)^2 log D(A)=o(log A)` has only `A^{o(1)}` chambers and annihilator factors, and ordinary floor rounding is negligible at the global rate and pointwise exponential levels. What remains is not how many chambers exist, but whether the source-carrying chamber can become too thin to retain macroscopic mass.