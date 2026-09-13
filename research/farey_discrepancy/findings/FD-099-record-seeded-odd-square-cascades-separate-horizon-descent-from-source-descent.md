# FD-099 — record-seeded odd-square cascades separate horizon descent from source descent

**Status:** `EXACT-DERIVED + FALSE-RH-FRONTIER + SOURCE-RECORD-SLOWDOWN + ODD-SQUARE-CASCADE + GROWING-DEPTH + FIXED-RATIO-PREDECESSORS + SUBPOWER-QUALITY-DIAGONAL + SOURCE-QUOTIENT-INVARIANT + ROUTE-OBSTRUCTION`.

`FD-097` reduces the growing-depth composition problem to two conceptually different losses: projective occupation/record-defect quality and physical descent. `FD-098` improves the source-head branch by a logarithmic corridor but still leaves only additive retreat on that branch. A natural remaining hope is therefore that forcing a positive density of genuinely multiplicative predecessor steps would by itself make the growing-depth argument coercive.

That hope is too weak. Under the same false-RH source-record input used by `FD-096`, one can construct, for every fixed depth `m`, an **exact chain of `m` multiplicative predecessors**, each contracting the physical horizon by exactly `4/9`, while preserving the same source sample `mathcal H(X)` at every step. All states in the chain are frontier-sharp, have nonsquarefree occupation bounded below by a positive constant depending only on `m` and `sigma`, and have bounded normalized record defect with the same dependence. After diagonalizing `m -> infinity`, the occupation and defect losses are only subpower and the total relative horizon contraction tends to zero exponentially.

The catch is exact and arithmetic: the chain is prepaid by the row

\[
9^m=3^{2m}.
\]

Each predecessor step replaces one factor `3^2` by the universal four-adic repair factor `2^2`, so the row evolves as

\[
9^m,
\ 4\,9^{m-1},
\ 4^2 9^{m-2},
\ldots,
\ 4^m,
\]

while the quotient sampled by every row remains identically `X`. Thus **horizon descent is not source descent**. A growing density of multiplicative steps can be financed entirely by pre-existing repeated-prime inventory without ever exposing a smaller source scale. Any decisive composition theorem must therefore control source-scale refresh or charge this arithmetic inventory; counting contractive predecessor steps alone cannot close the false-RH route.

## 1. Source-record slowdown holds at every fixed dilation

Assume

\[
\Theta>\frac12
\]

and fix

\[
\frac12<\sigma<\Theta.
\tag{1}
\]

As in `FD-096`, write

\[
Q_\sigma(n):=\frac{|\mathcal H(n)|}{n^\sigma},
\qquad
P_\sigma(Y):=\max_{1\le n\le Y}Q_\sigma(n).
\tag{2}
\]

A strict `sigma`-record is an integer `X` satisfying

\[
Q_\sigma(X)=P_\sigma(X)>P_\sigma(X-1).
\tag{3}
\]

The doubling argument of `FD-096` is not dyadic in substance. For every fixed real `L>1`,

\[
\boxed{
\liminf_{\substack{X\to\infty\\X\;\mathrm{strict\ }\sigma\mathrm{-record}}}
\frac{P_\sigma(LX)}{P_\sigma(X)}
\le L^{\Theta-\sigma}.
}
\tag{4}
\]

Indeed, fix `K>L^(Theta-sigma)` and choose

\[
\Theta<\tau<\sigma+\log_LK.
\tag{5}
\]

If every sufficiently large strict record obeyed

\[
P_\sigma(LX)>K P_\sigma(X),
\tag{6}
\]

then iteration through successive records would give records `X_j` with

\[
X_j\le L^jX_0,
\qquad
P_\sigma(X_j)>K^jP_\sigma(X_0).
\tag{7}
\]

But the global source frontier used in `FD-096` gives

\[
P_\sigma(Y)\ll_\tau Y^{\tau-\sigma},
\tag{8}
\]

and (7)--(8) contradict `K>L^(tau-sigma)`. This proves (4).

Now fix an integer depth `m>=1` and take

\[
L_m:=9^m.
\tag{9}
\]

Because `Theta<=1` and `sigma>1/2`,

\[
\Theta-\sigma<\frac12,
\]

so

\[
L_m^{\Theta-\sigma}<3^m.
\tag{10}
\]

Equation (4) therefore supplies infinitely many strict records `X` for which

\[
\boxed{
P_\sigma(9^mX)\le3^mP_\sigma(X).
}
\tag{11}
\]

Put

\[
A:=|\mathcal H(X)|.
\tag{12}
\]

Since `X` is a strict source record, `FD-076` gives, for all sufficiently large such records,

\[
\boxed{A=X^{\Theta+o(1)}.}
\tag{13}
\]

Equation (11) yields the uniform source envelope

\[
\boxed{
|\mathcal H(y)|
\le
3^m A\left(\frac yX\right)^\sigma
\qquad(1\le y\le9^mX).
}
\tag{14}
\]

For fixed `m`, every constant here is independent of the chosen large record `X`.

## 2. One record controls an entire multiplicative staircase

Define, for `0<=j<=m`,

\[
q_j:=4^j9^{m-j},
\qquad
H_j:=q_jX.
\tag{15}
\]

Then

\[
\boxed{
H_{j+1}=\frac49H_j
\qquad(0\le j<m),
}
\tag{16}
\]

so the horizons form a strictly decreasing geometric chain

\[
9^mX=H_0>H_1>\cdots>H_m=4^mX.
\tag{17}
\]

Recall the complete Jordan-Schur energy

\[
E_{N,1}
=
\sum_{1<r\le N}
 w(r)\,
\mathcal H\!\left(\left\lfloor\frac Nr\right\rfloor\right)^2,
\qquad
w(r)=\frac{J_2(r)}{r^2},
\tag{18}
\]

and put

\[
S_\sigma:=\sum_{r=2}^{\infty}\frac{w(r)}{r^{2\sigma}}<\infty.
\tag{19}
\]

For every `N<=H_0`, every complete row `r>=2` samples at

\[
\left\lfloor\frac Nr\right\rfloor
\le\frac{H_0}{2}
<9^mX,
\]

so (14) gives uniformly over the whole history below `H_0`

\[
\boxed{
E_{N,1}
\le
9^m S_\sigma A^2
\left(\frac NX\right)^{2\sigma}.
}
\tag{20}
\]

At the special horizon `H_j`, the row `r=q_j` divides the horizon exactly and samples the **same source record**:

\[
\boxed{
\left\lfloor\frac{H_j}{q_j}\right\rfloor=X.
}
\tag{21}
\]

The corresponding Jordan weights are explicit:

\[
w(q_0)=\frac89,
\qquad
w(q_j)=\frac23\quad(0<j<m),
\qquad
w(q_m)=\frac34.
\tag{22}
\]

In particular,

\[
\boxed{w(q_j)\ge\frac23}
\tag{23}
\]

for every step, and every `q_j` is nonsquarefree. Hence

\[
\boxed{
U_{H_j,1}
\ge\frac23A^2,
\qquad
E_{H_j,1}
\ge\frac23A^2.
}
\tag{24}
\]

Combining (20) and (24) gives a simultaneous occupation bound for every state in the staircase:

\[
\boxed{
\frac{U_{H_j,1}}{E_{H_j,1}}
\ge
\frac{2}
{3\,9^mS_\sigma q_j^{2\sigma}}
\ge
\frac1{D_m},
}
\tag{25}
\]

where one may take

\[
D_m
:=
\frac32 S_\sigma 9^{m(1+2\sigma)}.
\tag{26}
\]

The same estimate controls the normalized record defect. With

\[
F_\sigma(N):=\frac{E_{N,1}}{N^{2\sigma}},
\]

(20) gives

\[
F_\sigma(N)
\le
9^mS_\sigma\frac{A^2}{X^{2\sigma}}
\qquad(N\le H_0),
\tag{27}
\]

whereas (24) gives

\[
F_\sigma(H_j)
\ge
\frac23\frac{A^2}{(q_jX)^{2\sigma}}.
\tag{28}
\]

Therefore, for the defect from `FD-094`,

\[
\boxed{
\mathfrak R_\sigma(H_j)
\le
\frac32\,9^mS_\sigma q_j^{2\sigma}
\le D_m.
}
\tag{29}
\]

For each fixed `m`, (13), (20), and (24) also imply uniformly in `j`

\[
\boxed{
E_{H_j,1}=H_j^{2\Theta+o(1)}.
}
\tag{30}
\]

Thus every member of the staircase is frontier-sharp, nonsquarefree-occupied, and bounded-defect. The constants deteriorate exponentially in `m`, but not in the source record `X`.

## 3. Every staircase edge is the exact odd-prime repair from `FD-091`

The states in (15) are not merely a collection of unrelated good horizons. For every `j<m`, the designated row `q_j` contains another repeated factor `3^2`:

\[
9\mid q_j.
\tag{31}
\]

Choose the repeated prime `p=3`, which is permitted by the row-adaptive repeated-prime deflation of `FD-088`. Since the row already divides its horizon exactly, no stitching is needed. The first deflation sends

\[
(H_j,q_j)
\longmapsto
\left(\frac{H_j}{3},\frac{q_j}{3}\right),
\tag{32}
\]

and stripping the second copy of `3` followed by the universal four-adic reembedding of `FD-091` gives

\[
\left(\frac{H_j}{9},\frac{q_j}{9}\right)
\longmapsto
\left(\frac{4H_j}{9},\frac{4q_j}{9}\right).
\tag{33}
\]

But by (15),

\[
\boxed{
\frac{4H_j}{9}=H_{j+1},
\qquad
\frac{4q_j}{9}=q_{j+1}.
}
\tag{34}
\]

The quotient-shell argument is preserved exactly:

\[
\boxed{
\left\lfloor\frac{H_{j+1}}{q_{j+1}}\right\rfloor
=
\left\lfloor\frac{H_j}{q_j}\right\rfloor
=X.
}
\tag{35}
\]

Thus (17) is an actual chain of `m` exact physical predecessor moves of the already-canonical odd-prime type. Every edge contracts the horizon by the same fixed factor `4/9`, every destination row remains nonsquarefree, and the transported coordinate continues to carry the same frontier source amplitude `A`.

The arithmetic bookkeeping is especially transparent:

\[
q_j=4^j9^{m-j}.
\tag{36}
\]

Each contractive step consumes one stored factor `3^2` and replaces it by one factor `2^2`. After exactly `m` steps all odd-square inventory has been exhausted and the designated row is

\[
q_m=4^m,
\tag{37}
\]

which is purely dyadic. This is precisely where the odd-prime repair mechanism stops supplying another `4/9` step.

## 4. Growing depth survives with only subpower projective loss

The construction is nonuniform in `m`: equation (11) is obtained separately for each fixed dilation `9^m`. That is enough, however, to diagonalize the finite cascades.

For each `m`, choose one of the infinitely many records satisfying (11) so large that, in addition to all asymptotic thresholds above,

\[
\log X_m\ge m^2.
\tag{38}
\]

Then

\[
D_m
=
\exp(O_\sigma(m))
=
H_{j,m}^{o(1)}
\tag{39}
\]

uniformly for `0<=j<=m`. Equations (25) and (29) therefore become

\[
\boxed{
\frac{U_{H_{j,m},1}}{E_{H_{j,m},1}}
\ge H_{j,m}^{-o(1)},
\qquad
\mathfrak R_\sigma(H_{j,m})
\le H_{j,m}^{o(1)}.
}
\tag{40}
\]

The intrinsic projective quality of `FD-097` consequently obeys

\[
\boxed{
\mathcal Q_\sigma(H_{j,m})
\ge H_{j,m}^{-o(1)}
}
\tag{41}
\]

throughout the whole chain. At the same time,

\[
\boxed{
\frac{H_{m,m}}{H_{0,m}}
=\left(\frac49\right)^m
\longrightarrow0.
}
\tag{42}
\]

So false RH itself supplies growing-depth chains with **100% multiplicative predecessor density**, exponentially strong relative horizon descent, and only subpower occupation/defect degradation.

Nevertheless the source scale never moves. For every `m` and every `j`,

\[
\boxed{
\frac{H_{j,m}}{q_{j,m}}=X_m.
}
\tag{43}
\]

The entire cascade is a factorization transport of one source spike, not a sequence of new source events. Its terminal horizon is

\[
H_{m,m}=4^mX_m,
\tag{44}
\]

which is still exponentially **above** the source record scale `X_m`. Thus the relative physical descent in (42) was prepaid by choosing the initial row `9^m`; it does not constitute descent through the underlying source hierarchy.

## 5. Matched stress test: multiplicative-step density is not the missing invariant

This cascade is an adversarial control for the current composition strategy because it lives inside the actual Jordan-Schur source, uses genuine false-RH records, and satisfies the same occupation/defect conditions that the predecessor machinery is designed to preserve. It therefore rules out the implication

\[
\text{many contractive predecessor steps}
\quad\Longrightarrow\quad
\text{source-scale descent}
\]

without an additional hypothesis.

The obstruction is not a weak constant or an artifact of the head branch. Every step is a fixed `4/9` contraction and the projective losses can be made subpower. What fails is that the geometric horizon `H` carries a second scale, the sampled source quotient `H/r`. Repeated-prime repair can reduce `H` while reducing the row `r` in exactly the same proportion. In the cascade above, that quotient is an exact invariant.

This also sharpens the interpretation of `FD-097`. Its remaining phrase “physical descent versus depth” is too coarse if “physical” means only the horizon. Growing-depth horizon descent can already be manufactured under false RH. A decisive invariant must distinguish **fresh descent** from **factorization-funded descent**. Natural forms of such a theorem would have to force one of the following genuinely stronger events: a decrease or refresh of the sampled source scale, depletion of repeated-square inventory that cannot be replenished by the same carrier, or a quantitative relation between predecessor depth and source-record scale that prevents all depth from being prepaid in the starting row.

No such theorem is proved here. In particular, the result does **not** show that the canonical predecessor chain chosen from an arbitrary occupied packet must follow this staircase, nor does it show that every multiplicative contraction is uninformative. It shows that the existence, positive density, or even full density of contractive steps is not by itself coercive unless the argument also controls what happens to the source quotient or to the arithmetic inventory financing those steps.

## 6. Boundary checks and prior-art audit

The fixed-`m` quantifier in (11) is essential. The record-growth argument proves slow normalized growth for every **fixed** dilation `L`; it gives no uniform statement when `L=9^m` is allowed to grow with the same record `X`. Consequently (38)--(42) are a diagonal family of longer finite chains, not one infinite chain based at a single record. Turning the construction into an RH contradiction would require precisely the missing quantitative relation between admissible depth and source scale.

The four-adic terminal factor is equally essential. Replacing each stripped odd square by `4` is the smallest universal exact reembedding that guarantees nonsquarefree support. Hence after `m` odd repairs the terminal designated row is necessarily `4^m` in this construction. The chain cannot be reinterpreted as descent to `X`; its endpoint remains `4^mX`.

A targeted prior-art audit covered classical Franel--Landau/Mertens transforms, Jordan/GCD-matrix formulations, recent work on local Farey discrepancy and gap structure, and recent Farey families with `k`-free denominator restrictions. The located literature studies discrepancy bounds, rank/gap formulas, restricted-denominator equidistribution, and correlation statistics; no source located states this record-seeded exact `9 -> 4` predecessor cascade or the resulting separation between horizon descent and the invariant source quotient. The derivation above uses no new external theorem beyond the source-frontier/record inputs already canonized and sourced in the line, so `SOURCES.md` requires no new dependency.

## Research consequence

`FD-096` closes the bounded-defect entry gate, `FD-097` shows projective quality can survive growing finite depth, and `FD-098` thickens the additive source-head retreat. The present result removes a tempting next target: merely proving that non-head multiplicative branches occur often is not enough. False RH already permits arbitrarily long finite chains in which **every** step is the strongest available odd-prime multiplicative contraction and yet all steps are copies of one unchanged source event.

The sharper frontier is therefore to control **source-scale progress**. A successful composition invariant must charge the repeated-square inventory used to finance exact reembedding, force a carrier to sample genuinely smaller/new source arguments, or prove a depth-versus-record-scale estimate strong enough that the diagonal nonuniformity above cannot hide the descent. Until one of those mechanisms is obtained, multiplicative horizon contraction and projective quality can coexist indefinitely at growing finite depth without approaching a contradiction.