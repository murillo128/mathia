# FD-093 — dyadic terminal obstruction collapses to the single row-two head atom

**Status:** `CORRECTION + EXACT-DERIVED + DYADIC-HEAD-ATOM + DETERMINISTIC-SQUAREFREE-PREFIX + ROW-ADAPTIVE-ODD-PRIME-REPAIR + FOUR-ADIC-REEMBEDDING + FALSE-RH-FRONTIER + RECURSION-FRONTIER`.

`FD-092` correctly classified the first dyadic deflation but its quarter-scale identity omitted one coordinate. At `D=1`, the physical vector `V_(B,1)` has rows `m>1`; the terminal dyadic mask always contains `m=1`, coming from the parent row `r=4`. Thus the claimed identity for the **entire** terminal mask was false by the explicit missing amount

\[
\frac34\,|\mathcal H(B)|^2.
\]

This is material rather than cosmetic: `FD-046` shows that `mathcal H` itself carries the full zeta-zero growth exponent, so one fixed source atom cannot be discarded by cardinality. `FD-092` is therefore withdrawn and replaced by the corrected decomposition below.

The correction also exposes substantially more structure. Apart from that one head atom, the terminal dyadic support is not an arbitrary adaptive squarefree mask. It is the complete odd-squarefree prefix forced by the deterministic smallest-repeated-prime assignment. Every nonhead row in that prefix has an odd prime divisor. Stripping that divisor and reembedding four-adically gives an **exact** nonsquarefree physical mask at a genuinely lower horizon, with the quotient-shell source argument unchanged and with a uniform Jordan-weight factor.

Consequently the only dyadic terminal coordinate that cannot be repaired by this mechanism is the half-scale row `s=2` itself. All rows `s=2m` with odd squarefree `m>1` admit an exact lower nonsquarefree repair. The remaining global difficulty is therefore sharper: either a frontier block concentrates a fixed fraction on the single source value `|mathcal H(B)|^2`, or one obtains the same kind of lower nonsquarefree frontier-normalized packet already present in the odd-prime branch. The latter still does **not** by itself prove a fixed occupation fraction inside the complete lower state.

## 1. The omitted coordinate in the quarter-scale identity

Retain the canonical false-RH block notation of `FD-088`--`FD-091`. Thus

\[
\Theta>\frac12,
\qquad
L_H=\lfloor H^{\Theta-\delta}\rfloor,
\qquad
R_H=\left\lfloor\frac{H}{L_H+1}\right\rfloor,
\tag{1}
\]

with `delta>0` chosen so that

\[
R_H=H^{1-\Theta+\delta+o(1)}=o(L_H).
\tag{2}
\]

For the dyadic channel put

\[
A:=\left\lceil\frac H2\right\rceil,
\qquad
B:=\left\lfloor\frac A2\right\rfloor
=\frac H4+O(1).
\tag{3}
\]

The deterministic assignment of `FD-089` sends a nonsquarefree core row `r` to the smallest prime `p` for which `p^2|r`. Hence the rows assigned to `p=2` whose first deflation `s=r/2` is squarefree are **exactly**

\[
r=4m,
\qquad
s=2m,
\qquad
m\le M_H:=\left\lfloor\frac{R_H}{4}\right\rfloor,
\qquad
m\text{ odd and squarefree}.
\tag{4}
\]

Both directions are immediate. If the first-deflated row is squarefree and even, then `s=2m` with `m` odd squarefree, hence `r=4m`. Conversely, for every odd squarefree `m` with `4m<=R_H`, the only squared prime dividing `4m` is `2^2`, so the deterministic assignment is `p(r)=2` and the lower row `2m` is squarefree.

Thus the terminal support after removing the dyadic factor is the complete prefix

\[
\boxed{
T_H=\{m\le M_H:\ m\text{ odd and squarefree}\}.
}
\tag{5}
\]

It always contains `m=1` for large `H`. For every `m in T_H`, floor composition and oddness give

\[
\left\lfloor\frac{A}{2m}\right\rfloor
=
\left\lfloor\frac{B}{m}\right\rfloor,
\qquad
w(2m)=\frac34 w(m),
\tag{6}
\]

where

\[
w(n)=\frac{J_2(n)}{n^2}=\prod_{q\mid n}(1-q^{-2}).
\tag{7}
\]

However `V_(B,1)` starts at row `m=2`. Define the genuine nonhead physical mask

\[
T_H^+
:=
\{m:\ 3\le m\le M_H,\ m\text{ odd and squarefree}\},
\tag{8}
\]

\[
Q_{B,H}^+
:=
\|P_{T_H^+}V_{B,1}\|_2^2
=
\sum_{m\in T_H^+}
w(m)\mathcal H\!\left(\left\lfloor\frac Bm\right\rfloor\right)^2.
\tag{9}
\]

Then the correct terminal identity is

\[
\boxed{
M_{2,H}^{\rm term}
=
\frac34|\mathcal H(B)|^2
+
\frac34 Q_{B,H}^+.
}
\tag{10}
\]

Equation (10) is the exact correction to the quarter-scale formula in `FD-092`. The first term is the lower row `s=2` at horizon `A`; after the second dyadic deflation it would become row `m=1`, which is outside the `D=1` physical tail.

## 2. Every nonhead terminal coordinate has an exact odd-prime repair

Fix `m in T_H^+`. Since `m>1` is odd and squarefree, let

\[
p=p(m)
:=
\min\{q:q\text{ prime and }q\mid m\},
\qquad
m=pt.
\tag{11}
\]

Then `p>=3`, `p` does not divide `t`, and `t` is odd and squarefree. Partition `T_H^+` by this deterministic prime label. For each occurring `p`, define

\[
C_p:=4\left\lfloor\frac Bp\right\rfloor,
\qquad
u:=4t=\frac{4m}{p}.
\tag{12}
\]

The map `m -> nu` is injective inside a fixed `p`-packet, and every destination row is divisible by `4`, hence nonsquarefree. More importantly, the quotient-shell argument is preserved exactly:

\[
\boxed{
\left\lfloor\frac{C_p}{\nu}\right\rfloor
=
\left\lfloor
\frac{\lfloor B/p\rfloor}{t}
\right\rfloor
=
\left\lfloor\frac{B}{pt}\right\rfloor
=
\left\lfloor\frac Bm\right\rfloor.
}
\tag{13}
\]

There is therefore no source approximation, no one-step Lipschitz loss, and no rowwise horizon error.

The Jordan factor is also explicit. Since `p` does not divide `t`,

\[
w(m)=(1-p^{-2})w(t),
\qquad
w(\nu)=w(4t)=\frac34w(t).
\tag{14}
\]

Hence

\[
\boxed{
\frac{w(\nu)}{w(m)}
=
\gamma_p
:=
\frac{3/4}{1-p^{-2}},
\qquad
\frac34<\gamma_p\le\frac{27}{32}.
}
\tag{15}
\]

Let `T_(p,H)^+` be the packet of `m` having smallest prime divisor `p`, let

\[
Q_{p,H}
:=
\sum_{m\in T_{p,H}^+}
w(m)\mathcal H\!\left(\left\lfloor\frac Bm\right\rfloor\right)^2,
\tag{16}
\]

and let `N_(p,H)` be the energy of its image on the genuine physical state `V_(C_p,1)`. Equations (13)--(15) give the exact packet identity

\[
\boxed{
N_{p,H}=\gamma_p Q_{p,H},
\qquad
N_{p,H}\le U_{C_p,1}.
}
\tag{17}
\]

Since the packets partition `T_H^+`,

\[
\boxed{
\frac34Q_{B,H}^+
<
\sum_p N_{p,H}
\le
\frac{27}{32}Q_{B,H}^+,
}
\tag{18}
\]

whenever the nonhead mask is nonempty. Thus every nonhead part of the purported terminal squarefree carrier has been converted back into lower nonsquarefree physical energy.

## 3. The repaired horizons are genuinely earlier and retain summable frontier entropy

The secondary primes obey

\[
3\le p\le M_H\le\frac{R_H}{4}.
\tag{19}
\]

Because `R_H=o(H)`, uniformly over every occurring packet,

\[
\frac{p}{B}=o(1).
\tag{20}
\]

Consequently

\[
\boxed{
C_p
=\frac Hp(1+o(1))
}
\tag{21}
\]

uniformly over the whole repaired family. In particular,

\[
\boxed{
H^{\Theta-\delta+o(1)}
\ll C_p
\le
\left(\frac13+o(1)\right)H.
}
\tag{22}
\]

The lower bound follows from `p<=R_H/4` and `H/R_H=L_H+O(1)`. Even when `m` itself is prime, so `t=1` and the destination row is simply `4`, the repaired horizon still tends polynomially to infinity.

The predecessor family again has bounded effective entropy after frontier normalization. Fix `sigma>1/2` and put

\[
Z_{p,H}^{(\sigma)}
:=
\frac{N_{p,H}}{C_p^{2\sigma}}.
\tag{23}
\]

By (21),

\[
N_{p,H}
=(1+o(1))H^{2\sigma}p^{-2\sigma}Z_{p,H}^{(\sigma)}
\tag{24}
\]

uniformly, while

\[
\sum_p p^{-2\sigma}<\infty.
\tag{25}
\]

Therefore any fixed raw lower bound

\[
\sum_p N_{p,H}\ge cE_{H,1}
\tag{26}
\]

implies

\[
\boxed{
\max_p
\frac{N_{p,H}}{C_p^{2\sigma}}
\ge
\left(
\frac{c}{\zeta(2\sigma)-1}-o(1)
\right)
\frac{E_{H,1}}{H^{2\sigma}}.
}
\tag{27}
\]

Thus, under false RH, one may again set `sigma=Theta`. Along sharp frontier seeds with loss tending to zero, if the repaired nonhead family carries a fixed parent-energy fraction then one selected nonsquarefree lower mask has the full frontier exponent

\[
N_{p,H}=C_p^{2\Theta-o(1)}.
\tag{28}
\]

No cardinality loss arises from the potentially growing family of secondary prime labels.

## 4. The false-RH dyadic branch reduces to three explicit alternatives

Use the dyadic alternative of `FD-091`,

\[
M_{2,H}\ge\frac\eta2E_{H,1},
\tag{29}
\]

and split

\[
M_{2,H}
=M_{2,H}^{\rm elig}+M_{2,H}^{\rm term}.
\tag{30}
\]

If

\[
M_{2,H}^{\rm elig}\ge\frac\eta4E_{H,1},
\tag{31}
\]

then the genuine half-scale state already contains that much nonsquarefree masked energy:

\[
U_{A,1}\ge\frac\eta4E_{H,1}.
\tag{32}
\]

Otherwise `M_(2,H)^term>=eta E_(H,1)/4`. Apply (10). Either the single head contribution is at least half of that terminal energy, giving

\[
\boxed{
|\mathcal H(B)|^2
\ge\frac\eta6E_{H,1},
\qquad
B=\frac H4+O(1),
}
\tag{33}
\]

or the nonhead part contributes at least half, giving

\[
\frac34Q_{B,H}^+
\ge\frac\eta8E_{H,1}.
\tag{34}
\]

In the latter case (18) yields

\[
\boxed{
\sum_pN_{p,H}
\ge\frac\eta8E_{H,1},
}
\tag{35}
\]

and (27)--(28) produce a frontier-normalized nonsquarefree predecessor at scale at most `(1/3+o(1))H`.

Hence the dyadic branch is no longer an undifferentiated squarefree-sector obstruction. Apart from already-eligible half-scale energy, it has only two outcomes:

- a fixed fraction is concentrated on the single half-scale row `s=2`, equivalently on the source spike `|mathcal H(B)|^2`; or
- a fixed fraction passes through exact lower nonsquarefree packets with summable prime entropy.

The second outcome still inherits the composition problem already isolated by `FD-090`--`FD-091`: a frontier-sized nonsquarefree mask need not occupy a fixed fraction of the **complete** lower-state energy. The new statement is only that failure of lower nonsquarefree **representability** in the dyadic terminal channel is localized to one coordinate.

## 5. Why the remaining head atom cannot be discarded generically

The residual `m=1` is the lower row `s=2` at horizon `A`. Its source argument is exactly `B`. A quotient-preserving reembedding to a destination row `u` would require a horizon near `uB`. The smallest nonsquarefree row is `u=4`, which returns to

\[
4B=H+O(1).
\tag{36}
\]

Thus the universal square-multiplier minimality observed in `FD-092` survives **only for this atom**: forcing nonsquarefree support while preserving `mathcal H(B)` exactly destroys the multiplicative descent.

Nor can the atom be declared negligible because it is only one coordinate. `FD-046` proves

\[
\limsup_{N\to\infty}
\frac{\log(1+|\mathcal H(N)|)}{\log N}
=\Theta,
\tag{37}
\]

so a single fixed source sample has the same polynomial frontier as the full construction. A successful next step must therefore use additional source coherence to rule out (33), absorb that spike into another recurrent structure, or solve the fixed-fraction composition problem for the repaired packets.

## 6. Stress tests and exact audit

The correction is falsifiable at the smallest possible coordinate. Include the parent row `r=4`. It is assigned to `p=2`, first-deflates to `s=2`, and belongs to the squarefree terminal part. Its contribution is

\[
w(2)\mathcal H(\lfloor A/2\rfloor)^2
=\frac34|\mathcal H(B)|^2,
\]

but the proposed quarter-scale destination would be `m=1`, excluded from `V_(B,1)`. Any identity claiming that the **entire** terminal energy is a mask of `V_(B,1)` therefore fails by exactly this amount.

For every `m>1`, the repair has no corresponding boundary defect: `p(m)>=3`, the destination row `4m/p>=4` lies in the physical tail, (13) is an exact floor identity, and (15) is an exact Euler-factor identity. No asymptotic estimate enters the coordinate transport itself; asymptotics are used only to compare the repaired horizons with `H` and to perform the frontier normalization.

## 7. Prior art and research boundary

The algebra above is internal to the Mathia Jordan-row representation. Literature on Farey fractions with squarefree or `k`-free denominators studies complete denominator families and their discrepancy; it does not supply the head-corrected deflation/reembedding mechanism here. No external theorem is load-bearing for (4)--(35), so `SOURCES.md` does not require a new dependency.

The durable frontier is now narrower than the one stated in the withdrawn `FD-092`. The dyadic terminal support is deterministic, and every nonhead coordinate can be repaired exactly. What remains is to decide whether the single row-two/source-head alternative (33) can persist on the same sharp occupied frontier, or whether source coherence forces enough mass into the repairable tail; separately, even a repaired frontier-sized nonsquarefree mask still needs a mechanism that upgrades normalized size to a fixed occupation fraction in its lower state.
