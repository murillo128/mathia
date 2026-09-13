# FD-091 — odd-prime square reembedding localizes recursive eligibility failure to the dyadic channel

**Status:** `EXACT-DERIVED + FALSE-RH-FRONTIER + PRIME-SQUARE-REEMBEDDING + NONSQUAREFREE-LOWER-MASK + DYADIC-BOTTLENECK + CRITICAL-NORMALIZATION-SURVIVES + RECURSIVE-ELIGIBILITY-FRONTIER`.

`FD-090` removes the predecessor-count entropy from the canonical prime contractions of `FD-089`, but leaves a sharper obstruction: after one repeated-prime deflation, the selected lower mask need not remain nonsquarefree. That obstruction is not symmetric in the prime label.

For every **odd** repeated-prime channel, the second copy of the repeated prime can be stripped and the resulting rows reembedded four-adically. This sends the mask to a genuine lower physical horizon whose selected coordinates are all divisible by `4`, hence nonsquarefree, with only the universal Jordan conditioning loss. The construction is exact at the floor-quotient level. The only prime for which this four-adic reembedding fails to produce a multiplicatively earlier horizon is `p=2`.

Consequently every sufficiently sharp occupied false-RH frontier block obeys a dichotomy. Either the dyadic channel already transports a fixed raw fraction of the parent energy to the half-scale predecessor `A_2=ceil(H/2)`, or the odd channels produce a lower horizon `C<= (4/9+o(1))H` carrying a **nonsquarefree mask** with fixed-strength frontier-normalized energy. Moreover the natural odd-channel normalization uses weights `p^(-4 sigma)`, so its entropy threshold is `sigma>1/4`; in particular there is no logarithmic degeneration at the critical normalization `sigma=1/2`.

This does not yet prove a fixed occupation fraction at the lower horizon: the nonsquarefree mask and the total lower energy can have the same frontier exponent while their ratio still tends to zero subpolynomially. What it does prove is that the generic recursive-eligibility failure left by `FD-090` can be confined to one arithmetic channel: the repeated prime `2`.

## 1. Start from the actual canonical masks of `FD-089`--`FD-090`

Retain the false-RH frontier setup with

\[
\Theta>\frac12,
\qquad
E_{H,1}>H^{2\Theta-\kappa},
\]

and fix an admissible constant `alpha` small enough for `FD-089`, with in addition

\[
0<\alpha<\frac12.
\tag{1}
\]

For each prime `p<=H^alpha`, that finding supplies the canonical lower horizon

\[
A_p:=\left\lceil\frac Hp\right\rceil
\tag{2}
\]

and a lower-coordinate mask `S_(p,H)` with energy

\[
M_{p,H}:=
\left\|P_{S_{p,H}}V_{A_p,1}\right\|_2^2.
\tag{3}
\]

The masks come from the deterministic assignment of each occupied parent row `r` to a repeated prime `p=p(r)` satisfying `p^2|r`, followed by the first deflation

\[
s=\frac rp.
\tag{4}
\]

Hence every selected lower row in `S_(p,H)` still satisfies

\[
\boxed{p\mid s.}
\tag{5}
\]

The compressed packet has the exact positive-energy recurrence from `FD-089`, retained explicitly in `FD-090`:

\[
\boxed{
\sum_{p\le H^\alpha} M_{p,H}
\ge (\eta-o(1))E_{H,1},
}
\tag{6}
\]

where `eta>0` is the fixed occupation level supplied by the preceding frontier construction.

Split (6) into the dyadic and odd-prime channels. For all sufficiently large selected blocks, at least one of the following holds:

\[
\boxed{M_{2,H}\ge \frac\eta2 E_{H,1}}
\tag{7}
\]

or

\[
\boxed{
\sum_{\substack{3\le p\le H^\alpha\\p\ {m prime}}}
M_{p,H}
\ge \left(\frac\eta2-o(1)\right)E_{H,1}.
}
\tag{8}
\]

Equation (7) is already a fixed **raw** transport statement to

\[
A_2=\left\lceil\frac H2\right\rceil.
\tag{9}
\]

The issue is that the rows in `S_(2,H)` are only known to be even, not nonsquarefree. The odd branch admits a stronger transformation.

## 2. An odd channel can be stripped by `p^2` and reembedded on rows divisible by `4`

Fix an odd prime `p` from the packet. By (5), write every selected row as

\[
s=pt,
\qquad t\ge1.
\tag{10}
\]

Define

\[
B_p:=\left\lfloor\frac{A_p}{p}\right\rfloor,
\qquad
C_p:=4B_p,
\tag{11}
\]

and send the selected row `s=pt` to

\[
u:=4t.
\tag{12}
\]

The quotient-shell argument is preserved **exactly**. Since floor division by positive integers composes,

\[
\begin{aligned}
\left\lfloor\frac{C_p}{u}\right\rfloor
&=
\left\lfloor\frac{B_p}{t}\right\rfloor\\
&=
\left\lfloor
\frac{\lfloor A_p/p\rfloor}{t}
\right\rfloor\\
&=
\left\lfloor\frac{A_p}{pt}\right\rfloor
=
\left\lfloor\frac{A_p}{s}\right\rfloor.
\end{aligned}
\tag{13}
\]

Thus the source amplitude on the old masked coordinate and on its new coordinate is identical; there is no one-step shell error and no stitching error in this second transformation.

Only the Jordan weight changes. Recall

\[
w(n)=\prod_{q\mid n}(1-q^{-2}).
\tag{14}
\]

Every finite Euler subproduct satisfies

\[
\frac1{\zeta(2)}\le w(n)\le1,
\tag{15}
\]

so for every `t`

\[
\boxed{
\frac1{\zeta(2)}
\le
\frac{w(4t)}{w(pt)}
\le
\zeta(2).
}
\tag{16}
\]

Let

\[
T_{p,H}:=
\left\{\frac{4s}{p}:s\in S_{p,H}\right\}
\tag{17}
\]

and define the new physical mask

\[
N_{p,H}:=
\left\|P_{T_{p,H}}V_{C_p,1}\right\|_2^2.
\tag{18}
\]

The map `s -> 4s/p` is injective for fixed `p`; (13)--(16) therefore give the coordinatewise comparison

\[
\boxed{
\frac1{\zeta(2)}M_{p,H}
\le N_{p,H}
\le \zeta(2)M_{p,H}.
}
\tag{19}
\]

Most importantly, every row in `T_(p,H)` is divisible by `4`. Hence the entire new mask lies in the nonsquarefree sector:

\[
\boxed{
N_{p,H}
\le U_{C_p,1}.
}
\tag{20}
\]

This is the eligibility information that was absent after the first prime deflation.

## 3. Odd reembedding is genuinely lower; the dyadic channel is uniquely critical

Uniformly for `p<=H^alpha`,

\[
A_p=\frac Hp+O(1),
\qquad
B_p=\frac{H}{p^2}+O(1),
\]

and therefore

\[
\boxed{
C_p=\frac{4H}{p^2}+O(1).
}
\tag{21}
\]

Because `alpha<1/2`, all such horizons tend to infinity and the relative error in (21) is uniform. For every odd prime `p>=3`,

\[
\boxed{
H^{1-2\alpha+o(1)}
\ll C_p
\le \left(\frac49+o(1)\right)H.
}
\tag{22}
\]

Thus the square stripping followed by four-adic reembedding produces a genuine multiplicative predecessor.

For `p=2`, the same formula gives

\[
4\left\lfloor\frac{A_2}{2}\right\rfloor
=H+O(1).
\tag{23}
\]

There is no multiplicative descent. This is not an artifact of choosing the number `4`: after stripping the repeated square `2^2`, the smallest universal square multiplier capable of forcing every destination row to be nonsquarefree is again `2^2`. Its scale factor exactly cancels the square contraction. For every odd repeated prime, the same universal square is strictly smaller than `p^2`.

Hence the failure to convert the first-deflated mask into a lower nonsquarefree physical mask is localized to the dyadic channel.

## 4. The odd branch has summable frontier entropy already for `sigma>1/4`

Assume the odd alternative (8). Summing (19) gives

\[
\boxed{
\sum_{\substack{3\le p\le H^\alpha\\p\ {m prime}}}
N_{p,H}
\ge
\left(\frac{\eta}{2\zeta(2)}-o(1)\right)E_{H,1}.
}
\tag{24}
\]

Fix any

\[
\sigma>\frac14
\tag{25}
\]

and normalize at the new physical scale,

\[
Z_{p,H}^{(\sigma)}
:=
\frac{N_{p,H}}{C_p^{2\sigma}}.
\tag{26}
\]

By (21), uniformly over the packet,

\[
N_{p,H}
=
(1+o(1))\,4^{2\sigma}H^{2\sigma}p^{-4\sigma}
Z_{p,H}^{(\sigma)}.
\tag{27}
\]

Since

\[
\sum_p p^{-4\sigma}
\le \zeta(4\sigma)-1<\infty
\qquad(\sigma>1/4),
\tag{28}
\]

(24)--(28) imply that at least one odd prime in the packet satisfies

\[
\boxed{
\frac{N_{p,H}}{C_p^{2\sigma}}
\ge
\left(
\frac{\eta}
{2\zeta(2)\,4^{2\sigma}\bigl(\zeta(4\sigma)-1\bigr)}
-o(1)
\right)
\frac{E_{H,1}}{H^{2\sigma}}.
}
\tag{29}
\]

Together with (20), the same bound holds with `U_(C_p,1)` on the left.

The threshold is strictly below the RH-critical normalization. In particular, at

\[
\sigma=\frac12,
\tag{30}
\]

the odd-channel prime weight is `p^(-2)` and (29) has an `H`-independent positive constant. The logarithmic endpoint loss in the one-deflation normalization of `FD-090` is therefore not intrinsic to the repeated-prime packet; using both copies of the repeated prime before reembedding moves the summability threshold from `1/2` to `1/4`.

No RH conclusion follows from this observation: the occupied packet itself was obtained in the false-RH frontier setup. The point is structural—the carrier entropy remains bounded even when measured at the critical `E/H` normalization.

## 5. Under false RH the odd branch produces full-frontier nonsquarefree energy

Return to `sigma=Theta`. Along sharp frontier seeds with loss `kappa_j->0`, (29) gives a selected odd prime `p_j` and horizon `C_j=C_(p_j)` such that

\[
N_{p_j,H_j}
\ge
c_{\Theta,\eta}
C_j^{2\Theta}H_j^{-\kappa_j}.
\tag{31}
\]

For fixed `alpha<1/2`, (22) gives

\[
\frac{\log H_j}{\log C_j}
\le
\frac1{1-2\alpha}+o(1).
\tag{32}
\]

Hence

\[
\boxed{
N_{p_j,H_j}=C_j^{2\Theta-o(1)}.
}
\tag{33}
\]

The zero-frontier upper envelope already used in `FD-087`--`FD-090` gives

\[
E_{C_j,1}\le C_j^{2\Theta+o(1)}.
\tag{34}
\]

Using (20),

\[
N_{p_j,H_j}
\le U_{C_j,1}
\le E_{C_j,1},
\]

so

\[
\boxed{
U_{C_j,1}=C_j^{2\Theta-o(1)},
\qquad
E_{C_j,1}=C_j^{2\Theta-o(1)}.
}
\tag{35}
\]

Thus the odd branch does not merely preserve total frontier energy. It produces a genuinely lower physical state whose **nonsquarefree energy itself has the full false-RH frontier exponent**.

Equation (35) is weaker than the fixed occupation estimate

\[
U_{C_j,1}\ge cE_{C_j,1}.
\]

The ratio may still be `C_j^(-o(1))`. Therefore `FD-091` does not yet justify recursively applying the fixed-`eta` block theorem from that exact horizon. It does, however, rule out the much looser interpretation that every prime channel may lose nonsquarefree eligibility completely after one deflation.

## 6. Stress tests, prior-art boundary, and new frontier

The four-adic output in (12) is deliberate. Reembedding merely at row `t` would allow the coordinate `t=1` to fall through the minimal Schur head, and it would not restore nonsquarefree support. Reembedding at `4t` simultaneously keeps every coordinate above the head and forces `mu(4t)=0`. The cost is a fixed scale factor `4`, which is harmless precisely for odd `p` and critical for `p=2`.

No disjointness between masks belonging to different primes is used after reembedding; they live in different physical states `V_(C_p,1)`. Within each state the map is injective, which is all that is needed for (19). Ties or overlaps between the numerical values of different `C_p` can only merge scalar lower states and do not weaken the positive inequalities.

A targeted prior-art audit covered Farey--Mertens discrepancy transforms, Smith/Jordan GCD-matrix structure, Jordan-totient Euler products, square-divisor decompositions, and the classical powerful/squarefree factorization of integers. Those sources contain the separate multiplicative identities used in (14)--(16), but no located source states this source-specific two-stage carrier: canonical repeated-prime masks, exact second floor contraction, universal four-adic reembedding, and the resulting dyadic/odd eligibility dichotomy. No new external theorem is load-bearing, so `SOURCES.md` requires no update.

The live recursive problem is now sharper. From every sharp occupied frontier block, either

\[
\boxed{
M_{2,H}\gg E_{H,1}
\quad\text{at}\quad A_2\sim H/2,
}
\tag{36}
\]

or an odd repeated-prime channel yields a lower horizon `C<= (4/9+o(1))H` with a nonsquarefree frontier-sized mask as in (29)--(35). Therefore a future obstruction to recursive composition no longer has to treat all repeated primes symmetrically. It can focus on two precise residuals: upgrade the odd-branch full-exponent nonsquarefree mask to a fixed occupation fraction, or understand the **dyadic terminal channel** in which stripping `2^2` and universally restoring nonsquarefreeness consumes the entire multiplicative scale gain.