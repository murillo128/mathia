# RE-108 — quantitative Robin peaks force inter-block normalization corridors

**Status:** `EXACT-DERIVED + INTER-BLOCK + QUANTITATIVE-RH-FAILURE + NORMALIZATION-CORRIDOR + BLOCK-SPACING + DYADIC-PACKING + MATCHED-SHARPNESS + COUNTEREXAMPLE-NARROWING + PRIOR-ART-AUDITED`.

`RE-107` closes the whole-fan problem internally: every sufficiently late common false-RH fan transports a positive power-scale raw Chebyshev deficit from its left selected endpoint to its right selected endpoint. The remaining question in `RESEARCH_LINES.md` is genuinely inter-block: what can happen before a later positive Robin block is seeded?

There is an exact first answer which does not use any prime-number-theorem estimate. A positive colossally abundant state cannot return to the Robin threshold immediately, because the numerator `rho(n)=sigma(n)/n` is strictly increasing along later colossally abundant numbers. The only mechanism available for reducing the Robin ratio is therefore growth of the `log log n` normalization. Quantitatively, that alone forces a macroscopic **normalization corridor** after every positive state.

Let `C<D` be colossally abundant numbers and write

\[
Y:=\log C,
\qquad
V:=\log D,
\qquad
h(C):=\log G(C)-\gamma,
\qquad
R_C:=e^{h(C)}-1=\frac{G(C)}{e^\gamma}-1.
\tag{1}
\]

Assume

\[
h(C)>0,
\qquad
h(D)\le0.
\tag{2}
\]

Then

\[
\boxed{V>Y^{1+R_C}.}
\tag{3}
\]

In particular,

\[
\boxed{V-Y\ge R_C\,Y\log Y.}
\tag{4}
\]

Thus the excess height of one positive CA state already prices the minimum logarithmic distance to **any later nonpositive CA state**.

Now assume RH is false, put

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12,
\tag{5}
\]

and fix

\[
J=[b_0,b_1]\Subset(1-\Theta,1/2).
\tag{6}
\]

On the infinite family of common quantitative positive blocks supplied by `RE-038`--`RE-040`, every selected fan state `C_b` satisfies

\[
A_b(C_b)
:=Y_b^bR_{C_b}
\ge c_0
\tag{7}
\]

for one block-independent `c_0>0`. Let `D_\mathcal B` be the first CA state after such a positive block with `h(D_B)<=0`, and set

\[
V_\mathcal B:=\log D_\mathcal B.
\tag{8}
\]

Then for **every** `b in J`,

\[
\boxed{
V_\mathcal B-Y_b
\ge
c_0Y_b^{1-b}\log Y_b.
}
\tag{9}
\]

Writing `X_B` and `W_B` for the minimum and maximum fan scales as in `RE-106`--`RE-107`, the two endpoint consequences are

\[
\boxed{
V_\mathcal B-X_\mathcal B
\ge
c_0X_\mathcal B^{1-b_0}\log X_\mathcal B,
}
\tag{10}
\]

and

\[
\boxed{
V_\mathcal B-W_\mathcal B
\ge
c_0W_\mathcal B^{1-b_1}\log W_\mathcal B.
}
\tag{11}
\]

The left-endpoint estimate is especially important inter-block. If the quantitative common blocks are ordered by increasing CA scale and `X_k` is the left fan scale of block `k`, then

\[
\boxed{
X_{k+1}-X_k
\gg_J
X_k^{1-b_0}\log X_k.
}
\tag{12}
\]

Consequently the number `N_J(T)` of these forced quantitative blocks with `X_k<=T` satisfies

\[
\boxed{
N_J(T)
\ll_J
\frac{T^{b_0}}{\log T}.
}
\tag{13}
\]

Equivalently, after reindexing the late blocks,

\[
\boxed{
X_k
\gg_J
(k\log k)^{1/b_0}.
}
\tag{14}
\]

Since `b_0` may be chosen arbitrarily close to `1-Theta` from above, for every fixed

\[
0<\eta<\Theta-\frac12
\tag{15}
\]

one may choose a compact fan with `b_0=1-Theta+eta` and obtain an infinite quantitative witness family with

\[
N_\eta(T)
\ll_\eta
\frac{T^{1-\Theta+\eta}}{\log T}.
\tag{16}
\]

This is not a contradiction to false RH. It is a new constraint on how the quantitative Robin excursions supplied by Robin's theorem can recur: **the same power-scale height that seeds a common fan forces a still larger normalization corridor before that block can end.**

## 1. The corridor inequality is exact

Recall

\[
G(n)=\frac{\rho(n)}{\log\log n},
\qquad
\rho(n)=\frac{\sigma(n)}n.
\tag{17}
\]

With `Y=log C`,

\[
h(C)
=
\log\rho(C)-\gamma-\log\log Y.
\tag{18}
\]

Likewise

\[
h(D)
=
\log\rho(D)-\gamma-\log\log V.
\tag{19}
\]

For `C<D` both colossally abundant, `rho(D)>rho(C)`. This follows directly from the CA variational definition: if `D` is CA for some `epsilon>0`, then

\[
\frac{\rho(D)}{D^\varepsilon}
\ge
\frac{\rho(C)}{C^\varepsilon},
\tag{20}
\]

hence

\[
\rho(D)
\ge
\rho(C)\left(\frac DC\right)^\varepsilon
>
\rho(C).
\tag{21}
\]

If `h(D)<=0`, equations (18)--(21) give

\[
\log\log V
\ge
\log\rho(D)-\gamma
>
\log\rho(C)-\gamma
=
\log\log Y+h(C).
\tag{22}
\]

Exponentiating once,

\[
\log V
>
e^{h(C)}\log Y
=(1+R_C)\log Y,
\tag{23}
\]

which proves (3). Therefore

\[
V-Y
>
Y\bigl(Y^{R_C}-1\bigr)
=
Y\bigl(e^{R_C\log Y}-1\bigr)
\ge
R_CY\log Y,
\tag{24}
\]

proving (4).

There is no asymptotic replacement in this argument. Equation (3) is exact, and (4) uses only `e^u-1>=u`.

## 2. The common false-RH amplitude converts the exact corridor into a power law

`RE-038` fixes a quantitative left threshold `b_0` and extracts infinitely many finite positive CA blocks carrying a witness with

\[
A_{b_0}=Y^{b_0}R_C\ge c_0.
\tag{25}
\]

`RE-040` upgrades the same blocks to a common fan over every `b in J`: a blockwise maximizer `C_b` obeys

\[
A_b(C_b)
\ge
A_b(N)
\ge c_0,
\tag{26}
\]

where `N` is the original `b_0` witness. Hence

\[
R_{C_b}\ge c_0Y_b^{-b}.
\tag{27}
\]

Because the whole block is positive and finite, Robin's above/below CA behavior supplies a later CA state `D_B` with `h(D_B)<=0`; choosing the first such state merely makes the corridor minimal. Applying (4) to each selected `C_b<D_B` gives

\[
V_B-Y_b
\ge
R_{C_b}Y_b\log Y_b
\ge
c_0Y_b^{1-b}\log Y_b,
\tag{28}
\]

which is (9).

The fan orientation of `RE-038`/`RE-106` makes the selected scale nondecreasing with `b`; thus `Y_(b0)=X_B` and `Y_(b1)=W_B` up to the harmless convention when an endpoint cell persists. Equations (10)--(11) follow.

Two points are worth separating. First, the bound does not use `RE-102`'s local first-layer normal form, the prime-gap second moment, fringe classification, or the Chebyshev/Mertens fan Lyapunov coordinates. It survives arbitrary fan complexity. Second, the exponent in the left corridor is `1-b_0`, not `1-b_1`. The original quantitative witness therefore gives a stronger inter-block distance than the worst-threshold amplitude floor used for the internal whole-fan debt.

## 3. Quantitative witness blocks have a packing law

Order the common quantitative blocks in increasing CA order. Let `D_k` be the first nonpositive CA state after block `k`, with logarithmic scale `V_k`. Every selected state in any later common block lies beyond `D_k`, so

\[
X_{k+1}\ge V_k.
\tag{29}
\]

Applying (10) to block `k`,

\[
X_{k+1}-X_k
\ge
V_k-X_k
\ge
c_0X_k^{1-b_0}\log X_k,
\tag{30}
\]

which proves (12).

For a dyadic shell `T<=X_k<2T`, two consecutive block starts in that shell are therefore separated by at least

\[
\gg_J T^{1-b_0}\log T.
\tag{31}
\]

A shell of length `T` contains at most

\[
O_J\!\left(\frac{T^{b_0}}{\log T}\right)
\tag{32}
\]

such starts. Summing over dyadic shells up to `T` is dominated by the final shells because `b_0>0`, which proves (13). Standard inversion gives (14).

The dependence on `Theta` in (16) is only the dependence already present in Robin's quantitative false-RH theorem. For fixed `eta>0`, choose `b_0=1-Theta+eta` and then any `b_1` with

\[
b_0<b_1<\frac12.
\tag{33}
\]

No uniformity as `eta->0` is claimed; the witness constant and the extracted block family may depend on the chosen compact interval.

## 4. The normalization corridor is larger than the internal fan-debt scale

`RE-107` forces, on the same block,

\[
H_\vartheta(Z_R)-H_\vartheta(Z_L)
\gg_J
X_B^{1-b_1}\log X_B.
\tag{34}
\]

Equation (10) now shows that before the block can even return to `h<=0`, the logarithmic CA scale has room

\[
V_B-X_B
\gg_J
X_B^{1-b_0}\log X_B.
\tag{35}
\]

Since `b_0<b_1`,

\[
\frac{X_B^{1-b_0}\log X_B}
     {X_B^{1-b_1}\log X_B}
=
X_B^{b_1-b_0}
\longrightarrow\infty.
\tag{36}
\]

Thus the currently uncontrolled inter-block corridor is **polynomially longer** than the scale of the Chebyshev gain forced inside the fan. This is an important negative control on the next strategy: the positive debts from `RE-107` cannot simply be telescoped across successive positive blocks while ignoring what happens between them. The gaps in which source phase may reorganize are asymptotically larger than the intra-block transport scale we have forced so far.

This does not say that the standard prime source actually performs the required reset. It says that block geometry and the Robin normalization leave more than enough physical scale for such a reset, so an inter-block contradiction must constrain the source **inside these corridors**, not merely count the positive fan increments at their endpoints.

## 5. Matched controls show the spacing exponent is sharp for the present information class

The exact corridor has a simple extremal control. Freeze the numerator after a positive state `C`, formally setting

\[
\rho(t)=\rho(C)
\tag{37}
\]

while allowing the logarithmic scale to increase continuously. Then

\[
h(t)=
\log\rho(C)-\gamma-\log\log t
\tag{38}
\]

hits zero **exactly** at

\[
t=Y^{e^{h(C)}}=Y^{1+R_C}.
\tag{39}
\]

Thus (3) is the equality case of the normalization-only model. Actual CA evolution has strictly increasing `rho`, so it can only postpone the return to the threshold. No stronger exit exponent can be obtained from numerator monotonicity alone.

The packing exponent is equally compatible with an abstract recurrence

\[
x_{k+1}
=x_k+c x_k^{1-b_0}\log x_k.
\tag{40}
\]

Its continuous comparison satisfies

\[
\frac{dk}{dx}
\asymp
\frac1{x^{1-b_0}\log x},
\tag{41}
\]

and therefore

\[
k
\asymp
\frac{x^{b_0}}{b_0\log x}.
\tag{42}
\]

So the order of (13) is sharp for the information used here. Infinitely many quantitative blocks remain perfectly compatible with the corridor law. The theorem narrows recurrence; it does not rule it out.

The control also catches a possible overinterpretation of `RE-107`: even if every positive block contributes a power-scale increase of the raw Chebyshev deficit, the block sequence can be sparse enough, with larger normalization corridors between contributions, that no contradiction follows from accumulation alone.

## 6. Prior-art boundary and research consequence

The load-bearing ingredients are already anchored in `SOURCES.md`: the CA variational definition of Alaoglu--Erdos, Robin's 1984 above/below behavior and quantitative false-RH excursions, and the common-block amplification of `RE-038`--`RE-040`. A directed current search of Robin/CA literature, including work on least CA exceptions, extremal/subsequence formulations, and the recent prime-layer workload, found no theorem pricing the distance from a positive quantitative CA state to a later nonpositive CA state by the exact law `V>Y^(1+R_C)` or deriving the block-packing consequence (13). The closest neighboring results concern existence/localization of CA counterexamples or individual CA transitions rather than recurrence spacing between positive blocks. No new external theorem is used, so `SOURCES.md` requires no change.

The research consequence is sharper than the generic statement that `RE-107` needs inter-block information. We now know the scale on which that information has to act. The quantitative witness at `b_0` forces a source-unknown corridor of length at least

\[
X^{1-b_0}\log X,
\tag{43}
\]

while the whole-fan Chebyshev gain currently forced is only at the smaller

\[
X^{1-b_1}\log X
\tag{44}
\]

scale. Therefore the next useful theorem must control **source phase across the normalization corridor**: for example, couple the reciprocal-Mertens coordinate to the Chebyshev deficit while `h` falls through zero, or show that the standard prime source cannot regenerate the next quantitative `b_0` witness after paying the corridor. A proof that only re-sums the already-positive within-fan transport cannot close the gap exposed here.
