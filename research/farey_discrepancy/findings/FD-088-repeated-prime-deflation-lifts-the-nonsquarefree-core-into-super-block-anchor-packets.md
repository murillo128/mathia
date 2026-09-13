# FD-088 — repeated-prime deflation lifts the nonsquarefree core into super-block anchor packets

**Status:** `EXACT-DERIVED + FALSE-RH-FRONTIER + REPEATED-PRIME-DEFLATION + SUPER-BLOCK-ANCHOR-PACKETS + MULTIHORIZON-COHERENCE + TERMINAL-SECTOR-ESCAPE + INTER-BLOCK-COMPOSITION-FRONTIER`.

`FD-087` proves a sharp obstruction to the most direct use of the additive frontier blocks from `FD-084`: every exact lower-horizon dilation anchor whose scale is at most the block length lies in a terminal quotient sector carrying only `o(1)` of the normalized near-frontier Jordan energy. The surviving alternatives named there were to force substantially larger anchors, exploit a signed/bulk quantity outside that terminal sector, save the destination denominator, or replace one-anchor transport by a multihorizon composition law.

The physical nonsquarefree core supplies the first two alternatives simultaneously. On a false-RH near-frontier block whose length is a power strictly larger than `H^(1/2)`, every nonsquarefree Jordan row in the nonterminal core can be moved to its **next multiple inside the same block**. Removing one copy of a repeated prime factor from that row produces a genuine lower horizon, and because the Jordan weight depends only on the radical, this prime deflation has **exactly unit weight distortion**. The resulting lower anchors are not of block scale: uniformly over the whole core they satisfy

\[
 a_r \gg \sqrt{H L_H} \gg L_H.
\tag{1}
\]

At the minimal fixed Schur head `D=1`, the nonsquarefree coordinates obtained in this way carry a fixed positive fraction of the near-frontier energy. Moreover all destination horizons used by the construction lie in the original additive block, so `FD-086` makes their complete normalized Jordan states asymptotically collinear. Thus the terminal-sector obstruction does **not** say that bulk exact anchors are unavailable. It says that they cannot be obtained as one small common divisor. The physical object instead supplies a row-adaptive packet of mesoscopic exact anchors.

This still does not close the inter-block problem. The anchors depend on the Jordan row and need not coincide between different blocks, so no existing GCD-duality identity sums them into one physical lower-horizon energy. The new exact structure is a multihorizon carrier that any successful composition theorem may try to exploit.

## 1. The false-RH block has a bulk nonterminal nonsquarefree core

Retain the zero-extended Jordan vector

\[
V_{N,D}(r)
:=
\sqrt{w(r)}\,
\mathcal H\!\left(\left\lfloor\frac Nr\right\rfloor\right),
\qquad
w(r)=\frac{J_2(r)}{r^2}
=
\prod_{p\mid r}(1-p^{-2}),
\tag{2}
\]

from `FD-086`--`FD-087`, with

\[
\|V_{N,D}\|_2^2=E_{N,D},
\qquad
\|P_{\rm ns}V_{N,D}\|_2^2=U_{N,D}.
\tag{3}
\]

Assume

\[
\Theta:=\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}>\frac12.
\tag{4}
\]

Choose

\[
0<\delta<\Theta-\frac12,
\qquad
L_H:=\lfloor H^{\Theta-\delta}\rfloor.
\tag{5}
\]

Using the seed extraction behind `FD-084`, choose the recurrent occupied block

\[
I_H=[H,H+L_H]
\tag{6}
\]

with an arbitrarily small fixed near-frontier energy loss `kappa>0`, so that

\[
E_{H,D}>H^{2\Theta-\kappa}
\tag{7}
\]

and, for a fixed occupation threshold `eta>0`,

\[
U_{N,D}>\eta E_{N,D}
\qquad(N\in I_H).
\tag{8}
\]

For example, with the four-adic seed mechanism one may take any fixed `eta<3/64`. As in `FD-087`, the exact numerical threshold is not important here; only a fixed positive occupation level is used.

Put

\[
R_H:=\left\lfloor\frac{H}{L_H+1}\right\rfloor.
\tag{9}
\]

Then

\[
R_H=H^{1-\Theta+\delta+o(1)}.
\tag{10}
\]

The choice (5) gives

\[
1-\Theta+\delta<\Theta-\delta,
\tag{11}
\]

so

\[
\boxed{R_H=o(L_H).}
\tag{12}
\]

At horizon `H`, the rows `r>R_H` are exactly the terminal sector with

\[
\left\lfloor\frac Hr\right\rfloor\le L_H.
\tag{13}
\]

`FD-087` proves, after taking `kappa` sufficiently small relative to `delta`, that this entire sector has vanishing normalized energy:

\[
\sum_{r>R_H}|V_{H,D}(r)|^2=o(E_{H,D}).
\tag{14}
\]

Consequently the nonsquarefree part of the complementary core satisfies

\[
\boxed{
\sum_{\substack{D<r\le R_H\\\mu(r)=0}}
|V_{H,D}(r)|^2
\ge
(\eta-o(1))E_{H,D}.
}
\tag{15}
\]

Thus the same theorem that makes every block-scale exact anchor negligible also forces the actual nonsquarefree occupation to live almost entirely on rows `r<=R_H`. Since `R_H=o(L_H)`, every such row has enough room to reach a multiple before the additive block ends.

## 2. Stitching each core row at its next multiple changes only `o(E)` energy

For every integer row

\[
D<r\le R_H,
\tag{16}
\]

define

\[
m_r:=\left\lceil\frac Hr\right\rceil,
\qquad
N_r:=r m_r.
\tag{17}
\]

Then

\[
H\le N_r<H+r\le H+R_H\le H+L_H
\tag{18}
\]

for all sufficiently large `H`. Hence

\[
\boxed{N_r\in I_H}
\tag{19}
\]

for every core row simultaneously.

Define the stitched core vector `W_H` by

\[
W_H(r)
:=
\sqrt{w(r)}\,\mathcal H(m_r)
\quad(D<r\le R_H),
\tag{20}
\]

and zero outside the core. This is not asserted to be the Jordan vector of one horizon; coordinate `r` is sampled from the physical horizon `N_r` at which that row becomes an exact divisor row:

\[
W_H(r)=V_{N_r,D}(r).
\tag{21}
\]

The quotient arguments at `H` and `N_r` differ by at most one:

\[
0\le
m_r-\left\lfloor\frac Hr\right\rfloor
\le1.
\tag{22}
\]

The physical shell source has the exact increment law from `FD-084`,

\[
\mathcal H(k)-\mathcal H(k-1)
=
\frac{\mu(\operatorname{rad}k)\varphi(\operatorname{rad}k)}k,
\qquad
|\mathcal H(k)-\mathcal H(k-1)|\le1.
\tag{23}
\]

Therefore every stitched coordinate moves by at most one in unweighted source amplitude, and since `w(r)<=1`,

\[
\boxed{
\|W_H-P_{\le R_H}V_{H,D}\|_2^2
\le R_H.
}
\tag{24}
\]

Choose the near-frontier loss `kappa` in (7) so small that

\[
1-3\Theta+\delta+\kappa<0.
\tag{25}
\]

This is possible under (4)--(5). Equations (7), (10), and (24) then give

\[
\boxed{
\frac{\|W_H-P_{\le R_H}V_{H,D}\|_2^2}{E_{H,D}}
\ll
H^{1-3\Theta+\delta+\kappa+o(1)}
\longrightarrow0.
}
\tag{26}
\]

Hence the stitched vector preserves the entire core direction and energy asymptotically. In particular, at the minimal head `D=1`, combining (15) and (26) yields

\[
\boxed{
\|P_{\rm ns}W_H\|_2^2
\ge
(\eta-o(1))E_{H,1}.
}
\tag{27}
\]

The point of (27) is not another occupation estimate. Every coordinate on its left now occurs at a destination horizon specially chosen to expose an exact repeated-prime factorization.

## 3. Repeated-prime deflation gives every nonsquarefree stitched coordinate an exact large lower anchor

Take a nonsquarefree core row `r`. Choose any prime `p_r` satisfying

\[
p_r^2\mid r
\tag{28}
\]

and put

\[
s_r:=\frac{r}{p_r}.
\tag{29}
\]

Because `p_r` still divides `s_r`, removing one copy of `p_r` does not change the radical:

\[
\operatorname{rad}(s_r)=\operatorname{rad}(r).
\tag{30}
\]

The Jordan weight in (2) therefore satisfies the exact identity

\[
\boxed{w(s_r)=w(r).}
\tag{31}
\]

Now define the lower horizon

\[
a_r:=s_r m_r=\frac{N_r}{p_r}.
\tag{32}
\]

At head `D=1`, one has `s_r>=2`, so the anchor coordinate survives the Schur head. Since

\[
\left\lfloor\frac{a_r}{s_r}\right\rfloor=m_r,
\tag{33}
\]

we obtain

\[
V_{a_r,1}(s_r)
=
\sqrt{w(s_r)}\,\mathcal H(m_r)
=
\sqrt{w(r)}\,\mathcal H(m_r)
=W_H(r).
\tag{34}
\]

Equivalently, using the exact dilation operator of `FD-087`,

\[
(\mathscr D_{p_r}V_{a_r,1})(r)
=
\sqrt{\frac{w(r)}{w(s_r)}}V_{a_r,1}(s_r)
=W_H(r),
\tag{35}
\]

and

\[
P_{p_r}V_{N_r,1}
=
\mathscr D_{p_r}V_{a_r,1}.
\tag{36}
\]

Thus every nonsquarefree coordinate in the stitched core is an **exact, unit-distortion dilation witness from a genuine lower physical horizon**. No inequality or asymptotic approximation is used in (31)--(36).

The anchor scale is the important point. Since `p_r<=sqrt(r)` and `r<=R_H`,

\[
a_r
=
\frac{N_r}{p_r}
\ge
\frac{H}{p_r}
\ge
\frac{H}{\sqrt{R_H}}.
\tag{37}
\]

From the definition of `R_H`,

\[
\frac{H}{\sqrt{R_H}}
\ge
\sqrt{H(L_H+1)},
\tag{38}
\]

up to the harmless integer endpoints. Hence

\[
\boxed{
a_r\gg\sqrt{H L_H}.}
\tag{39}
\]

On the other hand `p_r>=2` and `N_r<H+R_H`, so

\[
\boxed{
a_r\le\frac{H+R_H}{2}=(1+o(1))\frac H2.}
\tag{40}
\]

Therefore these are genuinely earlier, mesoscopic horizons. Most importantly,

\[
\boxed{
\frac{a_r}{L_H}
\gg
\sqrt{\frac{H}{L_H}}
=
H^{(1-\Theta+\delta)/2+o(1)}
\longrightarrow\infty.
}
\tag{41}
\]

They lie polynomially beyond the exact-anchor scale ruled negligible by `FD-087`. In exponent form,

\[
a_r
\ge
H^{(1+\Theta-\delta)/2+o(1)},
\qquad
L_H=H^{\Theta-\delta+o(1)}.
\tag{42}
\]

The gap between the exponents is `(1-Theta+delta)/2>0`.

Combining (27) and (34)--(41), at `D=1` a fixed positive share of the near-frontier Jordan energy can be assigned coordinatewise to exact lower anchors satisfying `a_r/L_H->infinity` uniformly across the packet.

## 4. The destination packet is not only large; it stays inside one coherent Schur direction

The destinations `N_r` in (17) all lie in the same block `I_H`. `FD-086` proves uniformly on that block that

\[
\left\|
\frac{V_{N,1}}{\|V_{N,1}\|_2}
-
\frac{V_{H,1}}{\|V_{H,1}\|_2}
\right\|_2
\longrightarrow0.
\tag{43}
\]

Consequently

\[
\boxed{
\sup_{2\le r\le R_H}
\left\|
\widehat V_{N_r,1}-\widehat V_{H,1}
\right\|_2
\longrightarrow0.
}
\tag{44}
\]

The row-adaptive exact anchors therefore do not arise by sending each coordinate to an unrelated future state. Their destination states all lie in the same vanishing angular cap, and (26) shows directly that stitching the selected divisor coordinates back together changes the core state by only `o(sqrt(E_H))`.

This gives an exact multihorizon representation of the occupied nonsquarefree core:

\[
\boxed{
W_H(r)
=
(\mathscr D_{p_r}V_{a_r,1})(r),
\qquad
N_r=p_r a_r\in I_H,
\qquad
\|P_{\rm ns}W_H\|_2^2
\ge(\eta-o(1))E_{H,1},
}
\tag{45}
\]

with the uniform anchor lower bound (39). It is the first bulk exact transport statement after `FD-087` whose participating lower horizons are all parametrically larger than the block length.

For a general fixed head `D`, the same construction works unchanged on every nonsquarefree row

\[
r>D^2,
\tag{46}
\]

because `p_r|s_r` implies `p_r<=s_r`, and therefore `s_r<=D` would force `r=p_rs_r<=D^2`. The only obstruction is the finite band

\[
D<r\le D^2.
\tag{47}
\]

Thus the general fixed-head statement is a clean dichotomy: either this finite nonsquarefree band carries a nonvanishing fraction of the normalized frontier energy, or the remaining nonsquarefree core admits the same super-block exact-anchor packet. No growing family of head exceptions appears.

## 5. Why this evades `FD-087` without contradicting it

`FD-087` controls exact lower anchors `a<=L_H`. Such copies necessarily live on rows with source quotient at most `L_H`, and their entire coordinate union has `o(1)` normalized energy. Here the construction starts from the complementary rows

\[
r\le R_H\asymp\frac{H}{L_H},
\tag{48}
\]

where the source quotient is larger than `L_H`. The additive block is used only to move each such row to its next divisor-compatible destination `N_r`; repeated-prime deflation then produces the lower anchor `a_r=N_r/p_r`.

The scale conversion is therefore

\[
r\lesssim\frac{H}{L_H}
\quad\Longrightarrow\quad
p_r\lesssim\sqrt{\frac{H}{L_H}}
\quad\Longrightarrow\quad
 a_r\gtrsim\sqrt{H L_H}.
\tag{49}
\]

This is exactly outside the hypothesis of the small-anchor capacity theorem. There is no hidden amplification: (31) makes the relevant Jordan-weight ratio equal to one, stronger than the uniform `zeta(2)` conditioning bound of `FD-087`.

The construction is also genuinely arithmetic. A generic row mask with the same nonsquarefree density would not supply (30)--(31), and a generic additive block would not supply the divisor-compatible horizons (17)--(19). Both the repeated-prime structure of nonsquarefree Jordan rows and the exact floor-quotient sampling are load-bearing.

## 6. Stress tests, remaining obstruction, and prior-art boundary

The main limitation is composability. The horizons `a_r` depend on `r`. Equation (45) is a stitched vector identity indexed by distinct destination rows; it does **not** assert that all witnesses are coordinates of one lower-horizon state, nor that their squared magnitudes can be summed as one physical `E_{a,D}`. Different rows can produce the same or arithmetically incompatible anchor horizons, and no current GCD-duality formula converts the packet into one scalar lower-horizon energy. Treating (45) as such a formula would be an invalid normalization step.

Likewise, the construction does not yet connect two separated frontier blocks. `FD-085` still permits those blocks to be multiplicatively hostile. What changes is the available object: each block now carries, in addition to one coherent Jordan direction, a constant-energy family of exact predecessor witnesses on scales `a_r>>L_H`. A future inter-block theorem can therefore ask whether these mesoscopic anchor packets overlap, correlate, admit a signed aggregate, or force a finite-entropy common structure. The small-anchor terminal obstruction no longer rules out that route.

The condition `delta<Theta-1/2` is essential for the present next-multiple construction because it is exactly what makes `R_H=o(L_H)`. At the critical frontier `Theta=1/2`, or for block exponents at most `1/2`, the block need not be long enough to reach a multiple of every nonterminal core row. The result is deliberately false-RH-facing and does not provide an RH proof or a pointwise Schur gap.

A targeted prior-art audit covered Farey/Mertens discrepancy transforms, Smith/Jordan GCD-matrix structure, Jordan-totient multiplicativity, and floor-quotient/divisor-order formulations. The individual ingredients `w(n)=prod_(p|n)(1-p^(-2))`, radical invariance under removing one repeated prime, and next-multiple arithmetic are elementary or classical. No located source states the resulting false-RH block theorem: that a constant-energy nonsquarefree core can be stitched through nearby divisor horizons into exact lower anchors all polynomially larger than the block length while the destinations remain projectively coherent. No priority claim beyond this specific derived organization is made, and no new external theorem is load-bearing, so `SOURCES.md` requires no new dependency.

## 7. Research consequence

After `FD-087`, the natural interpretation was that additive blocks fail to expose enough normalized exact lower-horizon state because every anchor they guarantee as a **common divisor** is too small. `FD-088` separates that statement from a stronger one that is false. Additive thickness plus the actual nonsquarefree factorization already exposes a bulk family of exact predecessor states at the much larger scale

\[
\boxed{
\sqrt{H L_H}
\lesssim a_r
\lesssim H/2.
}
\tag{50}
\]

The live inter-block problem is therefore no longer merely “find an anchor larger than the block.” Such anchors exist in bulk, row by row. The missing theorem is to **compose the row-adaptive anchor packet**: either show that packets from separated coherent blocks must share enough mesoscopic predecessor structure, construct a signed multihorizon functional that sums (45) without false scalarization, or prove that the packet itself is too dispersed to help. That is a narrower and more source-specific frontier than the terminal-sector obstruction alone.