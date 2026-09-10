# RE-027 — quantitative Robin thresholds force super-square-root prime-layer defects

**Status:** `LITERATURE+DERIVED + QUANTITATIVE-RH-FAILURE + TILTED-TANGENT-CA + PRIME-LAYER-DEFECT-OMEGA + BLOCK-STRETCH-BYPASS + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`. `RE-026` transfers Robin's quantitative false-RH witnesses to ordinary self-tangent maxima of the same counterexample blocks. That creates a genuine dichotomy: either the selected mixed race grows, or the quantitative witness may sit at logarithmic size much farther to the right than the ordinary `G`-maximum. The stretch is not necessary if the variational selection is made against Robin's **quantitative moving barrier itself** rather than against the constant barrier `e^gamma`.

Assume RH is false and put

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12.
\tag{1}
\]

Fix

\[
1-\Theta<b<\frac12.
\tag{2}
\]

By Robin's Proposition 1 in Section 4, there is a constant `c_b>0` and infinitely many colossally abundant integers `N` such that, with `X=log N`,

\[
G(N)\ge e^\gamma\left(1+c_bX^{-b}\right).
\tag{3}
\]

Define

\[
\tau_b(x):=\log\left(1+c_bx^{-b}\right),
\qquad
H_b(x):=\log\log x+\tau_b(x),
\tag{4}
\]

and on colossally abundant states

\[
\mathcal J_b(C)
:=
\log G(C)-\gamma-\tau_b(\log C).
\tag{5}
\]

Then there are infinitely many colossally abundant states `C` with

\[
Y:=\log C
\tag{6}
\]

such that

\[
\boxed{\mathcal J_b(C)\ge0}
\tag{7}
\]

and `C` is a **regular threshold-tangent state**: if `epsilon_-` and `epsilon_+` are its adjacent CA supporting slopes, then

\[
\boxed{
\varepsilon_+
< H_b'(Y)
<\varepsilon_-.
}
\tag{8}
\]

Since

\[
H_b'(Y)
=
\frac1{Y\log Y}
-
\frac{b c_b}{Y(Y^b+c_b)},
\tag{9}
\]

let `Z>Y` be the unique point satisfying

\[
\boxed{
\frac1{Z\log Z}=H_b'(Y).
}
\tag{10}
\]

Using the prime-layer event measure `Phi` of `RE-001`, regularity in (8) means that the CA state selected by the ordinary event parameter `g(Z)=1/(Z log Z)` is exactly `C`. Hence

\[
\boxed{
Y=\Phi(Z),
\qquad
D(Z):=Z-\Phi(Z)=Z-Y>0.
}
\tag{11}
\]

Moreover the displacement is not merely positive. It has the asymptotic size

\[
\boxed{
D(Z)
\sim
b c_b\,Y^{1-b}\log Y
\sim
b c_b\,Z^{1-b}\log Z.
}
\tag{12}
\]

Because `b<1/2`, this is super-square-root:

\[
\boxed{
\frac{D(Z)}{\sqrt Z}
\sim
b c_b\,Z^{1/2-b}\log Z
\longrightarrow+\infty.
}
\tag{13}
\]

Thus hypothetical RH failure forces infinitely many **quantitatively selected positive excursions of the exact CA prime-layer discrepancy itself**. This removes the block-stretch escape from `RE-026` at the price of changing the selector: the states in (7)--(13) need not be ordinary self-tangent maxima of `G`, and `D(Z)` is deliberately nonzero. The quantitative Robin witness is instead made tangent to its own moving threshold, and the inverse tangent shift becomes a prescribed source defect.

## 1. A quantitative witness has a threshold-tangent CA maximizer in its block

Robin's false-RH theorem supplies infinitely many CA witnesses satisfying (3). As in `RE-001` and `RE-026`, the CA values above `e^gamma` form infinitely many finite counterexample blocks, because under false RH there are also infinitely many CA values below the constant Robin barrier.

Fix a counterexample block containing a witness of (3). For every state in the block define `mathcal J_b` by (5). At the witness,

\[
\mathcal J_b(N)\ge0.
\tag{14}
\]

At each adjacent CA state outside the block one has `G<=e^gamma`, while `tau_b>0`, hence

\[
\mathcal J_b<0.
\tag{15}
\]

Choose the **rightmost** CA state `C` at which `mathcal J_b` is maximal on the block. Then its immediate CA predecessor `A` and successor `B` satisfy

\[
\mathcal J_b(C)\ge\mathcal J_b(A),
\qquad
\mathcal J_b(C)>\mathcal J_b(B),
\tag{16}
\]

including the cases where `A` or `B` lies outside the block. Equation (14) also gives (7).

The infinitely many quantitative witnesses cannot be contained in finitely many finite blocks, so this construction produces infinitely many selected states `C`.

## 2. The modified Robin penalty is eventually strictly concave

The ordinary logarithmic penalty from `RE-001` is

\[
H(x)=\log\log x,
\qquad
H'(x)=g(x)=\frac1{x\log x},
\tag{17}
\]

with

\[
H''(x)
=-\frac{\log x+1}{x^2(\log x)^2}.
\tag{18}
\]

For the moving threshold,

\[
\tau_b'(x)
=-\frac{b c_b}{x(x^b+c_b)},
\tag{19}
\]

and direct differentiation gives

\[
\tau_b''(x)
=
\frac{b c_b\bigl((b+1)x^b+c_b\bigr)}
{x^2(x^b+c_b)^2}>0.
\tag{20}
\]

But

\[
\frac{\tau_b''(x)}{|H''(x)|}
=O_b\!\left(x^{-b}\log x\right)
\longrightarrow0.
\tag{21}
\]

Therefore

\[
\boxed{H_b''(x)<0}
\tag{22}
\]

for all sufficiently large `x`. Also

\[
\frac{|\tau_b'(x)|}{g(x)}
=
\frac{b c_b\log x}{x^b+c_b}
\longrightarrow0,
\tag{23}
\]

so `H_b'(x)>0` eventually.

Let `x=log A<Y=log C<y=log B`. The exact consecutive-CA slope identity of `RE-001` gives

\[
\log\rho(C)-\log\rho(A)=\varepsilon_-(Y-x),
\qquad
\log\rho(B)-\log\rho(C)=\varepsilon_+(y-Y).
\tag{24}
\]

Since

\[
\mathcal J_b(C)
=
\log\rho(C)-H_b(Y)-\gamma,
\tag{25}
\]

(16) implies

\[
\varepsilon_-
\ge
\frac{H_b(Y)-H_b(x)}{Y-x}
>H_b'(Y),
\tag{26}
\]

where the last inequality is strict concavity. Similarly,

\[
\varepsilon_+
<
\frac{H_b(y)-H_b(Y)}{y-Y}
<H_b'(Y).
\tag{27}
\]

This proves (8). No prime-number-theorem estimate and no bound on the length of the counterexample block is used.

## 3. Inverting the tangent exposes an exact prime-layer defect

Because `tau_b'(Y)<0`, equation (9) gives

\[
0<H_b'(Y)<g(Y)
\tag{28}
\]

for sufficiently large selected states. The function `g(x)=1/(x log x)` is strictly decreasing, so there is a unique `Z>Y` satisfying (10).

Equation (8) says that `C` is the unique CA maximizer at the parameter `H_b'(Y)=g(Z)`. In the event representation of `RE-001`, away from tied event parameters the unique CA state selected by `g(Z)` has logarithmic size `Phi(Z)`. Therefore `C=C_Z` and (11) follows exactly.

This is the key distinction from the ordinary self-tangent selector. For an ordinary `G`-peak one has `Z=Y` and therefore `D(Y)=0`. For the quantitative threshold selector the derivative of the moving barrier shifts the external CA parameter to the right, and the same state satisfies

\[
D(Z)=Z-Y>0.
\tag{29}
\]

Thus the quantitative excess has been converted into a source-side discrepancy without transporting the witness to a different state in the block.

## 4. The forced defect is of order `Z^(1-b) log Z`

Subtract (10) from `g(Y)` and use (9):

\[
\boxed{
g(Y)-g(Z)
=
\frac{b c_b}{Y(Y^b+c_b)}.
}
\tag{30}
\]

The right side is `o(g(Y))`, because its ratio to `g(Y)` is

\[
\frac{b c_b\log Y}{Y^b+c_b}=o(1).
\tag{31}
\]

Consequently

\[
\frac{g(Z)}{g(Y)}\to1.
\tag{32}
\]

For each fixed `delta>0`,

\[
\frac{g((1+\delta)Y)}{g(Y)}\to\frac1{1+\delta}<1,
\]

so monotonicity of `g` and (32) imply

\[
\boxed{Z/Y\to1.}
\tag{33}
\]

By the mean-value theorem there is `xi` between `Y` and `Z` such that

\[
g(Y)-g(Z)=(-g'(\xi))(Z-Y).
\tag{34}
\]

Now

\[
-g'(x)
=
\frac{\log x+1}{x^2(\log x)^2},
\tag{35}
\]

and (33) gives

\[
-g'(\xi)
\sim
\frac1{Y^2\log Y}.
\tag{36}
\]

Combining (30), (34), and (36),

\[
Z-Y
\sim
\frac{b c_b}{Y^{b+1}}
Y^2\log Y
=
 b c_bY^{1-b}\log Y.
\tag{37}
\]

Equations (11), (33), and (37) prove (12), and (13) follows because `b<1/2`.

A slightly more resolved first-order form, before replacing `-g'(xi)` by its asymptotic, is

\[
Z-Y
=
\frac{b c_bY^{1-b}(\log Y)^2}
{(1+c_bY^{-b})(\log Y+1)}(1+o(1)),
\tag{38}
\]

which is consistent with (37). No claim is made that the displayed `o(1)` has a uniform constant as `b` or `c_b` varies; both are fixed throughout the selection.

## 5. Relation to the self-tangent mixed-race route

`RE-026` keeps the ordinary self-tangent geometry by moving from a quantitative witness `N_B` to a rightmost maximum `C_B` of `G` on the same block. Because the threshold in (3) decays with logarithmic size, that transfer loses the witness scale and creates the race-or-stretch alternative.

The present selection makes the opposite trade. Maximizing `mathcal J_b` preserves the quantitative threshold at the selected state itself, but its intrinsic penalty derivative is not the ordinary Robin tangent `g(Y)`. Inverting that derivative gives `Z>Y`, so the selected state is an ordinary CA state at event coordinate `Z` with a prescribed nonzero workload `D(Z)`.

Therefore the two reductions expose complementary consequences of the same false-RH input:

- ordinary self-tangent selection keeps `D=0` and forces either a growing selected mixed race or large block stretch (`RE-026`);
- quantitative threshold-tangent selection removes block stretch and instead forces the direct source excursion (12).

Neither implication subsumes the other. In particular, (12) is not a statement about the mixed Mertens--Chebyshev coordinate `mathscr Y` at the ordinary self-tangent maxima, and `RE-025`'s local peak depth inequalities cannot be imported automatically because a threshold-tangent state need not be a local maximum of the unmodified `G` functional.

The gain is that the remaining obstruction is now purely source-side: hypothetical failure requires the prime-layer staircase `Phi` to fall below the identity by a prescribed super-square-root amount at infinitely many parameters selected by a quantitative CA extremum.

## 6. Prior-art and novelty boundary

Robin's 1984 Proposition 1 is the only new load-bearing external input beyond the event formalism already anchored by the line. It supplies (3); no novelty is claimed for the inverse-power false-RH excursion. Alaoglu--Erdos supply the CA supporting-slope structure behind (24), and Mantovanelli's August 2026 preprint supplies the closest independent prior art for the event measure `Phi`, discrepancy `D`, and ordinary regular self-tangent zeros.

Zimov's 2025 least-exception analysis also uses Robin's quantitative threshold and studies consecutive CA transitions, while recent work on explicit windows for hypothetical CA counterexamples constrains their largest-prime/size geometry. A targeted prior-art search across Robin's quantitative oscillation, colossally abundant tangent parameters, extremely abundant variants, and the recent prime-layer workload literature did not locate the specific **moving-threshold tangent selection** (4)--(12), nor the consequence that the inverse-power Robin excess forces `D(Z)~b c_b Z^(1-b) log Z` at infinitely many selected CA parameters. The novelty claim is limited to this variational splice and source-defect consequence, not to any constituent CA or Robin theorem.

No new `SOURCES.md` entry is needed: all load-bearing literature is already anchored there.

## 7. Falsification boundaries and research consequence

The result is conditional on hypothetical RH failure because `c_b` and the infinite witness sequence come from Robin's false-RH theorem. It does **not** provide an unconditional upper bound for `D`, and it does not assert that a global `o(Z^(1-b) log Z)` estimate is weaker than RH. Any attempt to close the argument by a generic PNT error estimate must be audited for RH-equivalent strength.

The selected states are ordinary colossally abundant integers, but they are not asserted to be ordinary self-tangent `G`-peaks. Their defining condition is the local maximum of the explicit thresholded functional `mathcal J_b`; consequently `D(Z)>0` is expected rather than contradictory.

The useful new target is narrower than the block-span problem left by `RE-026`: test whether the **same threshold-selected CA states** admit an independent event-ladder, frontier, or prime-source restriction incompatible with (12). A theorem of that form would attack the quantitative false-RH excursion without first proving that strong witnesses remain close to ordinary self-tangent block maxima. Until such a selected-source restriction is proved, (12) is a necessary-condition theorem, not an RH proof.