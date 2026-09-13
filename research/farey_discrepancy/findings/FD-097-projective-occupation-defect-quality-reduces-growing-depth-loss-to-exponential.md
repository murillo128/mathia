# FD-097 — projective occupation-defect quality reduces growing-depth loss to exponential

**Status:** `EXACT-DERIVED + PROJECTIVE-CERTIFICATE + MULTISTEP-COMPOSITION + EXPONENTIAL-LOSS + DIAGONAL-GROWING-DEPTH + FALSE-RH-FRONTIER + NO-RH-CONTRADICTION`.

`FD-094`--`FD-096` leave growing-depth composition as the active obstruction. Their one-step statements track two quantities separately: a lower bound for nonsquarefree occupation and an upper bound for the backward normalized-energy record defect. Iterating those two coarse bounds independently makes the constants appear capable of deteriorating extremely rapidly.

That deterioration is mostly an artifact of forgetting a common scale ratio. At every predecessor step, the lower occupation and the inherited record defect are both multiplied by the **same** factor

\[
\frac{F_\sigma(H)}{F_\sigma(C)}.
\]

If they are tracked projectively, this factor cancels. Consequently the natural certificate quality

\[
q=\frac{\eta}{K}
\]

for an occupation lower bound `eta` and defect upper bound `K` loses only a fixed branch factor at each step. Starting from the source-record states of `FD-096`, an `m`-step chain therefore has

\[
q_m\ge q_0 b_\sigma^m
\]

for a fixed `b_sigma>0`. In particular, occupation need decay at worst exponentially in depth and the defect need grow at worst exponentially. A diagonal choice of increasingly large entry records then gives chains whose depth tends to infinity while all occupation losses and defect growth remain subpower in every scale on the chain.

This is a genuine improvement over the fixed-depth conclusion of `FD-096`, but it is not yet an RH contradiction. The theorem is existential and gives no effective relation between achievable depth and the starting horizon. Moreover an all-head scalar control can satisfy the currently proved projective bounds while making only `O(H^Theta)` guaranteed additive progress from a scale `H`. The remaining issue is therefore no longer uncontrolled constant blow-up: it is **physical descent versus depth**, together with quantitative control of the asymptotic transport errors.

## 1. Historical normalization and projective certificate quality

Fix throughout

\[
\frac12<\sigma<\Theta
\tag{1}
\]

in the false-RH regime `Theta>1/2`, and retain

\[
F_\sigma(N):=\frac{E_{N,1}}{N^{2\sigma}}.
\tag{2}
\]

It is convenient to include the current horizon in the historical maximum:

\[
P_\sigma(H):=\max_{2\le N\le H}F_\sigma(N).
\tag{3}
\]

The backward defect of `FD-094` is then exactly

\[
\boxed{
\mathfrak R_\sigma(H)=\frac{P_\sigma(H)}{F_\sigma(H)}.
}
\tag{4}
\]

Indeed its definition is `max(1,sup_(N<H)F_sigma(N)/F_sigma(H))`, which is precisely (4).

Call a pair `(eta,K)` a valid occupation-defect certificate at `H` if

\[
\frac{U_{H,1}}{E_{H,1}}\ge\eta>0,
\qquad
\mathfrak R_\sigma(H)\le K<\infty.
\tag{5}
\]

Define its **projective quality** by

\[
\boxed{q(\eta,K):=\frac\eta K.}
\tag{6}
\]

The best possible value at a fixed horizon is the intrinsic quantity

\[
\boxed{
\mathcal Q_\sigma(H)
:=
\frac{U_{H,1}/E_{H,1}}{\mathfrak R_\sigma(H)}
=
\frac{U_{H,1}}{H^{2\sigma}P_\sigma(H)}.
}
\tag{7}
\]

Thus `mathcal Q_sigma` is simply nonsquarefree Schur energy normalized by the largest complete normalized Schur energy seen anywhere in the entire previous history. It packages the two quantities that were tracked separately in `FD-094`--`FD-096`.

## 2. The common destination factor cancels exactly

Suppose `H` has a valid certificate `(eta,K)` and one of the repairable predecessor branches produces a genuine lower state `C<H` together with a nonsquarefree mask energy `M_C<=U_(C,1)` satisfying

\[
\boxed{
\frac{M_C}{C^{2\sigma}}
\ge a\eta F_\sigma(H)
}
\tag{8}
\]

for some fixed branch coefficient `a>0`.

Put

\[
x:=\frac{F_\sigma(H)}{F_\sigma(C)}.
\tag{9}
\]

The transported mask immediately gives

\[
\frac{U_{C,1}}{E_{C,1}}
\ge
\frac{M_C/C^{2\sigma}}{F_\sigma(C)}
\ge a\eta x.
\tag{10}
\]

On the other hand, because `C<H`, every horizon contributing to `P_sigma(C)` also contributes to `P_sigma(H)`. Hence

\[
P_\sigma(C)\le P_\sigma(H)
\le K F_\sigma(H),
\]

and therefore

\[
\mathfrak R_\sigma(C)
=\frac{P_\sigma(C)}{F_\sigma(C)}
\le Kx.
\tag{11}
\]

Equations (10)--(11) show that `(a eta x,Kx)` is a valid lower/upper certificate at `C`. Its projective quality is

\[
\boxed{
\frac{a\eta x}{Kx}
=a\frac\eta K.
}
\tag{12}
\]

The unknown ratio `x` cancels **exactly**. This is the piece of information lost when (10) and (11) are weakened separately before iteration.

There is no hidden assumption that `x` is close to one. In fact the parent defect and the carrier inequality themselves only imply the broad interval

\[
\frac1K\le x\le\frac1{a\eta},
\tag{13}
\]

up to the already recorded asymptotic transport errors. Using the two endpoints of (13) independently gives the coarse bounds

\[
\eta_C\gtrsim\frac{a\eta}{K},
\qquad
K_C\lesssim\frac{K}{a\eta},
\tag{14}
\]

whose ratio is quadratic in `eta/K`. Those two worst cases cannot occur simultaneously: both are parametrized by the same `x`. Equation (12) keeps that correlation and replaces the apparent squaring by a linear projective loss.

## 3. Every current predecessor branch has a fixed projective coefficient

The one-step mechanisms already proved in `FD-091`, `FD-093`, `FD-094`, and `FD-095` all fit (8), after fixing the source-head backstep parameter. Take for definiteness

\[
\lambda=\frac12
\tag{15}
\]

in the head construction of `FD-095`.

For the odd repeated-prime branch, `FD-094` gives the coefficient

\[
c_{\rm odd}(\sigma)
=
\frac1{2\zeta(2)\,4^{2\sigma}(\zeta(4\sigma)-1)}.
\tag{16}
\]

For the already-eligible dyadic half-scale branch, the coefficient tends to

\[
c_{\rm elig}(\sigma)=2^{2\sigma-2}.
\tag{17}
\]

For the repaired dyadic nonhead family, the prime-weighted normalization gives

\[
c_{\rm term}(\sigma)
=
\frac1{8(\zeta(2\sigma)-1)}.
\tag{18}
\]

Finally the source-head backstep of `FD-095`, with `lambda=1/2`, gives

\[
\frac{U_{C,1}}{C^{2\sigma}}
\ge
\left(\frac{\eta}{32}-o(1)\right)
\left(\frac HC\right)^{2\sigma}
F_\sigma(H).
\tag{19}
\]

Since `C<H`, the extra factor `(H/C)^(2 sigma)` is at least one, so the head branch has the same form as (8) with asymptotic coefficient `1/32` or better.

Define the fixed positive safety coefficient

\[
\boxed{
b_\sigma
:=
\frac12\min\left\{
 c_{\rm odd}(\sigma),
 2^{2\sigma-2},
 c_{\rm term}(\sigma),
 \frac1{32}
\right\}>0.
}
\tag{20}
\]

For any **fixed** certificate `(eta,K)` with `eta>0`, all `o(1)` terms in the existing transport theorems can be made smaller than half the corresponding main term by taking the parent horizon sufficiently large. Hence every sufficiently large sharp state carrying that certificate has a sharp predecessor `C<H` with a valid certificate `(eta',K')` satisfying

\[
\boxed{
\frac{\eta'}{K'}
\ge b_\sigma\frac\eta K.
}
\tag{21}
\]

The required largeness threshold may depend on `eta` and on the fixed packet parameters. No uniform-in-depth error estimate is being smuggled into (21).

The sharp false-RH exponent is preserved by the same predecessors, as already established in `FD-094`--`FD-096`. The point of (21) is only that the two composition constants have a much better **joint** evolution than their separate one-step bounds suggest.

## 4. Composition loses at most exponentially in depth

`FD-096` supplies infinitely many sharp entry horizons with fixed constants

\[
\frac{U_{H_0,1}}{E_{H_0,1}}\ge\eta_0>0,
\qquad
\mathfrak R_\sigma(H_0)\le K_0<\infty,
\tag{22}
\]

where `eta_0,K_0` depend only on the chosen `sigma`. Put

\[
q_0:=\frac{\eta_0}{K_0}>0.
\tag{23}
\]

For a fixed integer `m`, start sufficiently far along the `FD-096` entry sequence that the one-step asymptotic errors are absorbable at every one of the first `m` predecessor steps. Applying (21) inductively gives a chain

\[
H_0>H_1>\cdots>H_m
\tag{24}
\]

of sharp physical states with valid certificates `(eta_j,K_j)` satisfying

\[
\boxed{
\frac{\eta_j}{K_j}
\ge q_0 b_\sigma^j
\qquad(0\le j\le m).
}
\tag{25}
\]

Every valid certificate has `K_j>=1` and may be chosen with `eta_j<=1`. Hence (25) separately implies

\[
\boxed{
\eta_j\ge q_0 b_\sigma^j,
\qquad
K_j\le q_0^{-1}b_\sigma^{-j}.
}
\tag{26}
\]

Thus the occupation floor and record-defect ceiling deteriorate at worst **exponentially** in predecessor depth. The double-exponential behavior suggested by iterating the decoupled estimates (14) is not a real consequence of the transport geometry.

This conclusion uses no new analytic-number-theory input. It is an algebraic consequence of the fact that the destination normalized energy `F_sigma(C)` appears once in the occupation denominator and once in the record-defect denominator with the same power.

## 5. A diagonal sequence has genuinely growing depth with only subpower quality loss

The fixed-depth statement in `FD-096` can now be diagonalized quantitatively in the certificate quality.

For each positive integer `m`, first regard `m` as fixed. The one-step predecessor maps already have the property used in `FD-096` that, after any fixed number of steps, every intermediate horizon tends to infinity with the starting entry horizon. Therefore choose an `FD-096` entry horizon so far out that:

1. all first `m` transport errors are small enough for (21);
2. the resulting last horizon satisfies `H_m>=exp(m^2)`.

This produces a sequence of finite chains with depths `m->infinity`. For every state on the `m`-th chain, (25)--(26) give

\[
\eta_j\ge \exp(-O_\sigma(m)),
\qquad
K_j\le \exp(O_\sigma(m)).
\tag{27}
\]

Because every `H_j>=H_m>=exp(m^2)`, these losses are subpower in the physical scale:

\[
\boxed{
\eta_j=H_j^{-o(1)},
\qquad
K_j=H_j^{o(1)}
\quad\text{uniformly for }0\le j\le m
}
\tag{28}
\]

along the chosen diagonal family.

So the current machinery **does** produce predecessor chains whose depth tends to infinity with the starting horizon. What it does not provide is an effective lower bound for that depth as a specified function of the horizon, because the thresholds needed to dominate the stepwise `o(1)` errors were never made uniform in the shrinking certificate.

This distinction sharpens the frontier after `FD-096`: growing depth itself is no longer excluded by constant degradation. The unresolved quantitative question is whether enough physical descent can be forced before the projective quality becomes too small, with error control uniform enough to compare depth to the starting scale.

## 6. Why exponential quality control still does not close false RH

The source-head branch shows why (28) is not yet a contradiction. On a sharp head step, `FD-095` gives

\[
H-C\asymp |\mathcal H(B)|
\]

for the chosen fixed backstep fraction, while the head alternative only forces

\[
|\mathcal H(B)|^2\gg \eta E_{H,1}.
\tag{29}
\]

With `E_(H,1)=H^(2Theta-o(1))`, the guaranteed additive progress is therefore only of the scale

\[
H-C\gg \eta^{1/2}H^{\Theta-o(1)}.
\tag{30}
\]

A scalar matched control of the **currently proved inequalities** may take

\[
\eta_j\asymp b_\sigma^j,
\qquad
H_j-H_{j+1}\asymp b_\sigma^{j/2}H_j^\Theta.
\tag{31}
\]

If `H_j` stays comparable to a large initial `H`, the total guaranteed retreat allowed by (31) is only

\[
O_\sigma(H^\Theta)
\sum_{j\ge0}b_\sigma^{j/2}
=O_\sigma(H^\Theta)
=o(H)
\qquad(\Theta<1).
\tag{32}
\]

This is not a construction of the true Farey/Mertens source; it is a control showing that the present inequalities, even with the improved projective bookkeeping, do not by themselves force a macroscopic scale collapse. A successful final descent needs extra information: recurrent re-recording, a better progress-versus-quality law, a forced positive density of multiplicative contraction steps, or a quantitative uniformization of the transport errors strong enough to reach a decisive depth.

At the endpoint `Theta=1` the simple comparison in (32) no longer gives `o(H)`, so that boundary must be treated separately rather than inferred from the sublinear case.

## 7. Prior-art boundary and research consequence

The algebraic ingredients behind the Schur energy remain the classical Farey--Mertens bridge and Smith/Jordan GCD-matrix factorization already recorded in `SOURCES.md`. A targeted literature audit also checked recent recursive formulas for Farey local discrepancy and the modern local/average-discrepancy literature. Those works organize Farey discrepancy recursively or by gap statistics, but no located source contains the Mathia-specific quantity (7), the predecessor certificate cancellation (12), or the diagonal growing-depth consequence (28).

No external theorem is load-bearing for the present result, so `SOURCES.md` requires no change. The novelty claim is correspondingly narrow: the new content is the projective bookkeeping of the already-derived Mathia predecessor transports and its multistep consequence, not a new classical Farey identity or a new theorem about the Mertens function.

The research frontier should therefore no longer be phrased as merely "control deterioration of occupation and defect constants with depth." Their coupled deterioration is at worst exponential and admits subpower-quality chains of unbounded depth by diagonalization. The remaining obstruction is quantitative **descent efficiency**: relate the number/type of predecessor steps to actual scale reduction before projective quality and transport errors become decisive.