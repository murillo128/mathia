# FD-071 — Later frontier spikes can squarefree-dilute every earlier persistent packet

**Status:** `EXACT-DERIVED + SOURCE-SPECIFIC + NEGATIVE/OBSTRUCTION + ZERO-FRONTIER-PAIRED-SPIKES + ARBITRARY-HORIZON-PACKET + SAME-HORIZON-DENOMINATOR + FIXED-SQUAREFREE-ROW + EPISODE-DILUTION`.

`FD-070` shows that a physical quotient-shell spike does not disappear after its reciprocal capture scale: at every sufficiently later horizon it expands into a growing packet of nonsquarefree Jordan rows. The remaining hope was that this persistent packet might force the denominator `E_(T,D)` to be unusually small on the same horizons, improving the normalized Schur defect beyond the generic zero-frontier envelope.

There is a source-specific obstruction to any such **all-later-horizon** inference. The complete Jordan energy carried by one fixed captured source episode is only linear in the later horizon `T`. If `Theta>1/2`, the same physical source has arbitrarily later zero-frontier spikes. Sampling one of those later spikes on any fixed squarefree row gives denominator energy of order `T^(2Theta-o(1))`. Hence the earlier episode, despite occupying a growing four-adic packet at that same horizon, can be made an arbitrarily small fraction of the total denominator.

More precisely, fix `D>=1` and define

\[
w(r):=\frac{J_2(r)}{r^2},
\qquad
E_{T,D}:=\sum_{r>D}w(r)\mathcal H\!\left(\left\lfloor\frac Tr\right\rfloor\right)^2.
\tag{1}
\]

Let `X` be a source point with

\[
A_X:=|\mathcal H(X)|\ge4,
\qquad
L_X:=\left\lfloor\frac{A_X}{2}\right\rfloor<X,
\tag{2}
\]

and isolate the **whole** Jordan block sampling the automatic backward coherent episode,

\[
\mathcal P_{T,D}(X)
:=
\sum_{\substack{r>D\\
X-L_X\le \lfloor T/r\rfloor\le X}}
 w(r)\mathcal H\!\left(\left\lfloor\frac Tr\right\rfloor\right)^2.
\tag{3}
\]

Whenever `D<T/(X+1)`, `A_X=o(X)`, and

\[
\frac{T A_X}{X^2}\to\infty,
\tag{4}
\]

the exact one-Lipschitz law for `mathcal H` gives the two-sided packet scale

\[
\boxed{
\left(\frac1{8\zeta(2)}-o(1)\right)
\frac{T A_X^3}{X^2}
\le
\mathcal P_{T,D}(X)
\le
\left(\frac98+o(1)\right)
\frac{T A_X^3}{X^2}.
}
\tag{5}
\]

Thus `FD-070`'s forced nonsquarefree subpacket is not merely bounded below by a cubic expression: the **entire source episode**, including all squarefree and nonsquarefree rows that sample it, has exactly that order. For fixed `X`, its contribution grows only linearly in `T`.

Now let

\[
\Theta
:=
\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}
\tag{6}
\]

and assume the false-RH regime

\[
\frac12<\Theta<1.
\tag{7}
\]

Fix any prime `p>D`. By `FD-046`, there are arbitrarily large `N` with

\[
|\mathcal H(N)|\ge N^{\Theta-\varepsilon}
\tag{8}
\]

for every fixed `epsilon>0`. At the horizon

\[
T=pN,
\tag{9}
\]

the single row `r=p` contributes

\[
\boxed{
E_{pN,D}
\ge
w(p)|\mathcal H(N)|^2
\ge
w(p)N^{2\Theta-2\varepsilon}.
}
\tag{10}
\]

The diluting witness is squarefree because `p` is prime. Combining (5) and (10), and taking `epsilon<(2Theta-1)/2`, shows that for every fixed episode `X`, one can choose arbitrarily late frontier spikes `N` such that

\[
\boxed{
\frac{\mathcal P_{pN,D}(X)}{E_{pN,D}}
\ll_{p,X}
N^{1-2\Theta+2\varepsilon}
\longrightarrow0.
}
\tag{11}
\]

The obstruction can be diagonalized so that the **earlier episodes themselves move out the zero frontier**. There exist zero-frontier spikes `X_j->infinity`, later zero-frontier spikes `N_j->infinity`, and horizons `T_j=pN_j` for which

\[
A_{X_j}=X_j^{\Theta+o(1)},
\qquad
\frac{T_jA_{X_j}}{X_j^2}\to\infty,
\tag{12}
\]

while

\[
\boxed{
\frac{\mathcal P_{T_j,D}(X_j)}{E_{T_j,D}}	o0.
}
\tag{13}
\]

At the same horizons the four-adic nonsquarefree packet forced by `FD-070` has cardinality tending to infinity and absolute energy tending to infinity. Equation (13) says that even the **full** reciprocal image of that earlier coherent source interval, not merely the four-adic subset used in the lower bound, can nevertheless become negligible after same-horizon normalization.

The conclusion is negative but sharp for the current frontier: arbitrary-horizon persistence is an absolute statement, not a relative-denominator statement. A denominator saving useful for the scalar Schur defect must be tied to a horizon near the episode being exploited, or must control interference from later source spikes. It cannot follow solely from the fact that the earlier packet remains present at all later horizons.

## 1. The complete coherent episode has cubic-linear energy

The exact one-Lipschitz identity used in `FD-036`, `FD-048`, `FD-069`, and `FD-070` is

\[
|\mathcal H(n)-\mathcal H(m)|\le |n-m|.
\tag{14}
\]

For `0<=h<=L_X`, equations (2) and (14) give both sides

\[
\frac{A_X}{2}
\le
|\mathcal H(X-h)|
\le
\frac{3A_X}{2}.
\tag{15}
\]

The rows whose floor quotient lies in this complete source block are exactly

\[
\left\lfloor\frac{T}{X+1}\right\rfloor
<r\le
\left\lfloor\frac{T}{X-L_X}\right\rfloor.
\tag{16}
\]

Their number is

\[
N_{T,X}
=
\left\lfloor\frac{T}{X-L_X}\right\rfloor
-
\left\lfloor\frac{T}{X+1}\right\rfloor.
\tag{17}
\]

If `A_X=o(X)`, then

\[
N_{T,X}
=
\frac{T(L_X+1)}{(X-L_X)(X+1)}+O(1)
=
\left(\frac12+o(1)\right)
\frac{T A_X}{X^2}+O(1).
\tag{18}
\]

Condition (4) makes the additive rounding error negligible. Since

\[
\frac1{\zeta(2)}\le w(r)\le1,
\tag{19}
\]

inserting (15), (18), and (19) into (3) yields exactly (5).

Moreover, every interval of `N_(T,X)` consecutive rows contains `N_(T,X)/4+O(1)` multiples of four. Therefore the nonsquarefree portion of (3) satisfies

\[
\boxed{
\mathcal P^{\rm ns}_{T,D}(X)
\ge
\left(\frac1{32\zeta(2)}-o(1)\right)
\frac{T A_X^3}{X^2},
}
\tag{20}
\]

recovering the `FD-070` packet inside the larger two-sided localization. Equations (5) and (20) are useful together: the forced four-adic component already has the correct order of the complete episode, but that order is still only linear in the future horizon.

## 2. A later frontier spike supplies a squarefree denominator witness

Fix a prime `p>D`. At `T=pN`, equation (1) contains the term

\[
w(p)\mathcal H(\lfloor pN/p\rfloor)^2
=w(p)\mathcal H(N)^2.
\tag{21}
\]

`FD-046` proves

\[
\limsup_{N\to\infty}
\frac{\log(1+|\mathcal H(N)|)}{\log N}
=\Theta.
\tag{22}
\]

Hence for every `epsilon>0` there are arbitrarily large `N` satisfying (8). Since all Jordan energies are nonnegative, retaining only (21) proves (10).

For a fixed earlier episode `X`, (5) at `T=pN` gives

\[
\mathcal P_{pN,D}(X)
\ll_X N.
\tag{23}
\]

Dividing by (10),

\[
\frac{\mathcal P_{pN,D}(X)}{E_{pN,D}}
\ll_{p,X}
N^{1-2\Theta+2\varepsilon}.
\tag{24}
\]

Because `Theta>1/2`, choose `epsilon<(2Theta-1)/2`. The exponent in (24) is negative, so the ratio tends to zero along a suitable unbounded frontier subsequence. Conditions `D<T/(X+1)` and (4) are automatic there. Thus a packet can be fully developed and still be relatively erased by a later physical spike sampled on one squarefree row.

The use of a prime row is deliberate. The denominator witness in (21) is not itself part of `U_(T,D)`, so the argument does not hide the dilution inside an already-nonsquarefree row. It also does not claim that the **total** nonsquarefree occupation `U_(T,D)/E_(T,D)` tends to zero: other source episodes can contribute to `U`. The theorem is specifically about the inability of one persistent episode to control its own same-horizon normalization indefinitely.

## 3. Both source episodes can lie on the zero frontier

To avoid a fixed-episode artifact, choose a zero-frontier spike sequence `X_j->infinity` with

\[
A_{X_j}=X_j^{\Theta+o(1)}.
\tag{25}
\]

After choosing `X_j`, select `epsilon_j->0` with eventually

\[
0<\varepsilon_j<\frac{2\Theta-1}{4}.
\tag{26}
\]

Equation (22) supplies arbitrarily large later points `N` satisfying

\[
|\mathcal H(N)|\ge N^{\Theta-\varepsilon_j}.
\tag{27}
\]

Because

\[
1-2\Theta+2\varepsilon_j
\le
-\frac{2\Theta-1}{2}<0
\tag{28}
\]

eventually, `N_j` can be chosen so large that simultaneously

\[
\frac{pN_jA_{X_j}}{X_j^2}\ge j
\tag{29}
\]

and

\[
\frac{A_{X_j}^3}{X_j^2}
N_j^{1-2\Theta+2\varepsilon_j}
\le\frac1j.
\tag{30}
\]

Put `T_j=pN_j`. Equation (29) gives the growing-packet condition in (12). Equations (5), (10), and (30) give (13). Since `A_(X_j)->infinity`, (20) also shows that the absolute four-adic packet energy diverges.

Thus the phenomenon is not caused by preserving an ancient bounded source feature. One can pair an earlier **frontier-sized** spike with a later frontier-sized spike so that the first has already expanded into an unbounded persistent packet while the second, seen through one fixed squarefree Jordan row, makes the first episode asymptotically negligible in the denominator.

## 4. Consequence for the post-`FD-070` denominator program

`FD-070` left a precise next target: improve the generic same-horizon denominator bound on horizons carrying the forced packet. The present result separates two possible meanings of that target.

A theorem asserting a denominator saving on **every sufficiently late horizon that still contains a given packet** is impossible at the level of the current source-specific frontier data. Later zero-frontier spikes themselves provide infinitely many packet-carrying horizons with a denominator contribution of frontier size on a fixed squarefree row. In that sense, onset-optimality in `FD-070` is not merely an artifact of using a crude global upper bound: sufficiently late physical horizons can genuinely become hostile to the earlier packet.

What remains viable is an **episode-adapted capture theorem**. One must locate a horizon near the reciprocal onset of the spike, before an unrelated later frontier episode can dominate, or prove arithmetic control that couples the denominator contributions from those later quotients back to the original spike. Equivalently, the missing theorem must contain temporal/source-location information; absolute persistence alone has now been falsified as a route to uniform relative control.

This also clarifies the role of a moving Schur head. Raising `D` toward `T/X` can excise rows sampling source values beyond `X`, but `FD-065` and `FD-070` show that the resulting Schur leverage loss pays for that localization. The fixed-head optimum therefore leaves precisely the later-source channel exhibited above. The obstruction is not an accidental choice of the four-adic packet; it is the causal geometry of reciprocal sampling plus the existence of later physical frontier spikes.

## 5. Prior-art boundary and falsification checks

The load-bearing inputs are internal except for the already anchored zeta-zero frontier behind `FD-046`: the exact quotient-shell source, its one-Lipschitz law, the Jordan energy (1), and the Littlewood--Titchmarsh power frontier transferred to `mathcal H`. No new external theorem is required, so `SOURCES.md` is unchanged.

A targeted search across Farey discrepancy, Mertens/floor-quotient sampling, Jordan-totient energies, and recent local Farey discrepancy work did not locate the paired-spike statement (11)--(13). No novelty is claimed for floor-hyperbola sampling or for the fact that a fixed row can realize the zero-frontier exponent separately; `FD-046` already proves the latter. The line-specific content is the two-sided localization (5) of an earlier persistent episode and its deliberate pairing with a later **squarefree** frontier witness on the same horizon.

The boundaries are strict. The conclusion requires `Theta>1/2`; at `Theta=1/2` the linear packet scale and the fixed-row denominator scale have the same power and (24) gives no decay. Equation (13) concerns the localized episode energy `mathcal P`, not the total `U/E`, so it does not resolve `CLUE-joint-nonsquarefree-jordan-energy-occupation`. The theorem also does not say that packet-onset horizons have a large denominator, because the later spike is chosen after the earlier episode. Finally, no claim is made for `Theta=1`, where the `A_X=o(X)` packet asymptotic used in (5) need not hold. Within `1/2<Theta<1`, however, the result exactly rules out turning arbitrary-horizon persistence into an all-later-horizon denominator saving.