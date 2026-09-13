# FD-093 — dyadic terminal obstruction collapses to the single row-two head atom

**Status:** `CORRECTION + EXACT-DERIVED + DYADIC-HEAD-ATOM + DETERMINISTIC-SQUAREFREE-PREFIX + ROW-ADAPTIVE-ODD-PRIME-REPAIR + FOUR-ADIC-REEMBEDDING + FALSE-RH-FRONTIER + RECURSION-FRONTIER`.

`FD-092` correctly classified the first dyadic deflation but its quarter-scale identity omitted one coordinate. At `D=1`, the physical vector `V_(B,1)` has rows `m>1`, whereas the dyadic terminal mask always contains `m=1`, coming from the parent row `r=4`. Thus the claimed identity for the **entire** terminal mask was false by the explicit missing amount

\[
\frac34|\mathcal H(B)|^2.
\]

This is material rather than cosmetic: `FD-046` shows that `\mathcal H` itself carries the full zeta-zero growth exponent, so a single fixed source atom cannot be discarded by cardinality. `FD-092` is therefore withdrawn and replaced by the corrected decomposition below.

The correction also exposes more structure. Apart from that one head atom, the terminal dyadic support is not an arbitrary adaptive squarefree mask. It is the complete odd-squarefree prefix forced by the deterministic smallest-repeated-prime assignment. Every nonhead row in that prefix has an odd prime divisor. Stripping that divisor and reembedding four-adically gives an **exact** nonsquarefree physical mask at a genuinely lower horizon, with the quotient-shell source argument unchanged and with a uniform Jordan-weight factor.

Consequently the only dyadic terminal coordinate that cannot be repaired by this mechanism is the half-scale row `s=2` itself. All rows `s=2m` with odd squarefree `m>1` admit an exact lower nonsquarefree repair. The remaining global difficulty is sharper: either a frontier block concentrates a fixed fraction on the single source value `|\mathcal H(B)|^2`, or one obtains the same kind of lower nonsquarefree frontier-normalized packet already present in the odd-prime branch. The latter still does **not** by itself prove a fixed occupation fraction inside the complete lower state.

## 1. Correct terminal decomposition

Retain the false-RH block notation of `FD-088`--`FD-091`:

\[
\Theta>\frac12,
\qquad
L_H=\lfloor H^{\Theta-\delta}\rfloor,
\qquad
R_H=\left\lfloor\frac{H}{L_H+1}\right\rfloor,
\qquad
R_H=H^{1-\Theta+\delta+o(1)}=o(L_H).
\tag{1}
\]

For the dyadic channel put

\[
A:=\left\lceil\frac H2\right\rceil,
\qquad
B:=\left\lfloor\frac A2\right\rfloor
=\frac H4+O(1).
\tag{2}
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
\tag{3}
\]

Indeed, if the first-deflated row is squarefree and even then `s=2m` with `m` odd squarefree, hence `r=4m`. Conversely, for every odd squarefree `m` with `4m<=R_H`, the only squared prime dividing `4m` is `2^2`, so the assigned prime is `2`.

Thus after removing the dyadic factor the support is the complete prefix

\[
T_H=\{m\le M_H:m\text{ odd and squarefree}\}.
\tag{4}
\]

For every `m in T_H`, floor composition and oddness give

\[
\left\lfloor\frac{A}{2m}\right\rfloor
=
\left\lfloor\frac{B}{m}\right\rfloor,
\qquad
w(2m)=\frac34w(m),
\qquad
w(n):=\frac{J_2(n)}{n^2}.
\tag{5}
\]

But `V_(B,1)` begins at row `m=2`. Define the genuine nonhead physical mask

\[
T_H^+:=\{3\le m\le M_H:m\text{ odd and squarefree}\},
\]

\[
Q_{B,H}^+
:=
\|P_{T_H^+}V_{B,1}\|_2^2
=
\sum_{m\in T_H^+}
w(m)\mathcal H\!\left(\left\lfloor\frac Bm\right\rfloor\right)^2.
\tag{6}
\]

The exact terminal identity is therefore

\[
\boxed{
M_{2,H}^{\rm term}
=
\frac34|\mathcal H(B)|^2
+
\frac34Q_{B,H}^+.
}
\tag{7}
\]

The first term is the lower row `s=2` at horizon `A`; after a second dyadic deflation it would become row `m=1`, which is outside the `D=1` physical tail.

## 2. Every nonhead coordinate has an exact odd-prime repair

Fix `m in T_H^+` and let

\[
p=p(m):=\min\{q:q\text{ prime},\ q\mid m\},
\qquad
m=pt.
\tag{8}
\]

Then `p>=3`, `p` does not divide `t`, and `t` is odd and squarefree. Partition `T_H^+` by this prime and define

\[
C_p:=4\left\lfloor\frac Bp\right\rfloor,
\qquad
u:=4t=\frac{4m}{p}.
\tag{9}
\]

For a fixed `p`, the map `m -> nu` is injective and every destination row is divisible by `4`, hence nonsquarefree. The quotient-shell argument is preserved exactly:

\[
\boxed{
\left\lfloor\frac{C_p}{\nu}\right\rfloor
=
\left\lfloor\frac{\lfloor B/p\rfloor}{t}\right\rfloor
=
\left\lfloor\frac{B}{pt}\right\rfloor
=
\left\lfloor\frac Bm\right\rfloor.
}
\tag{10}
\]

There is no source approximation and no rowwise horizon error. The Jordan factor is also exact:

\[
w(m)=(1-p^{-2})w(t),
\qquad
w(\nu)=w(4t)=\frac34w(t),
\]

so

\[
\boxed{
\gamma_p:=\frac{w(\nu)}{w(m)}
=
\frac{3/4}{1-p^{-2}},
\qquad
\frac34<\gamma_p\le\frac{27}{32}.
}
\tag{11}
\]

Let `Q_(p,H)` be the contribution of the `p`-packet to `Q_(B,H)^+`, and let `N_(p,H)` be the energy of its image in the genuine physical state `V_(C_p,1)`. Then

\[
\boxed{
N_{p,H}=\gamma_pQ_{p,H},
\qquad
N_{p,H}\le U_{C_p,1}.
}
\tag{12}
\]

Since these packets partition `T_H^+`,

\[
\boxed{
\frac34Q_{B,H}^+
\le
\sum_pN_{p,H}
\le
\frac{27}{32}Q_{B,H}^+.
}
\tag{13}
\]

Thus every nonhead part of the purported terminal squarefree carrier is converted exactly into lower nonsquarefree physical energy.

## 3. The repaired horizons are genuinely lower

The secondary primes satisfy

\[
3\le p\le M_H\le\frac{R_H}{4}.
\tag{14}
\]

Since `R_H=o(H)`, uniformly over the whole packet family `p/B=o(1)`, and hence

\[
\boxed{
C_p=\frac Hp(1+o(1)).
}
\tag{15}
\]

In particular,

\[
\boxed{
C_p\gg H^{\Theta-\delta+o(1)},
\qquad
C_p\le\left(\frac13+o(1)\right)H.
}
\tag{16}
\]

Even when `m` itself is prime, so `t=1` and the destination row is simply `4`, the repaired horizon still tends polynomially to infinity.

The predecessor family also retains the prime-weighted summability mechanism of `FD-090`. Fix `sigma>1/2` and set

\[
Z_{p,H}^{(\sigma)}:=\frac{N_{p,H}}{C_p^{2\sigma}}.
\tag{17}
\]

By (15), uniformly over the occurring primes,

\[
N_{p,H}
=(1+o(1))H^{2\sigma}p^{-2\sigma}Z_{p,H}^{(\sigma)},
\qquad
\sum_pp^{-2\sigma}<\infty.
\tag{18}
\]

Therefore any fixed raw bound

\[
\sum_pN_{p,H}\ge cE_{H,1}
\tag{19}
\]

implies

\[
\boxed{
\max_p\frac{N_{p,H}}{C_p^{2\sigma}}
\ge
\left(\frac{c}{\zeta(2\sigma)-1}-o(1)\right)
\frac{E_{H,1}}{H^{2\sigma}}.
}
\tag{20}
\]

Under false RH one may set `sigma=Theta`. Along sharp frontier seeds, if the repaired nonhead family carries a fixed parent-energy fraction, some selected nonsquarefree lower mask therefore has full frontier exponent

\[
N_{p,H}=C_p^{2\Theta-o(1)}.
\tag{21}
\]

No cardinality loss arises from the growing family of secondary prime labels.

## 4. The dyadic branch reduces to three alternatives

Use the dyadic alternative of `FD-091`,

\[
M_{2,H}\ge\frac\eta2E_{H,1},
\tag{22}
\]

and split `M_(2,H)=M_(2,H)^elig+M_(2,H)^term`. If

\[
M_{2,H}^{\rm elig}\ge\frac\eta4E_{H,1},
\tag{23}
\]

then the genuine half-scale state already contains

\[
U_{A,1}\ge\frac\eta4E_{H,1}.
\tag{24}
\]

Otherwise `M_(2,H)^term>=eta E_(H,1)/4`. Applying (7), either the single head contribution is at least half of the terminal energy, giving

\[
\boxed{
|\mathcal H(B)|^2\ge\frac\eta6E_{H,1},
\qquad
B=\frac H4+O(1),
}
\tag{25}
\]

or the nonhead term contributes at least half, giving

\[
\frac34Q_{B,H}^+\ge\frac\eta8E_{H,1}.
\tag{26}
\]

In the latter case (13) yields

\[
\boxed{
\sum_pN_{p,H}\ge\frac\eta8E_{H,1},
}
\tag{27}
\]

and (20)--(21) produce a frontier-normalized nonsquarefree predecessor at scale at most `(1/3+o(1))H`.

Thus, apart from already-eligible half-scale energy, the dyadic branch has only two outcomes: a fixed fraction is concentrated on the single row `s=2` / source spike `|\mathcal H(B)|^2`, or a fixed fraction passes through exact lower nonsquarefree packets with summable prime entropy. The second outcome still inherits the composition problem of `FD-090`--`FD-091`: a frontier-sized nonsquarefree mask need not occupy a fixed fraction of the **complete** lower-state energy. The new statement is only that failure of lower nonsquarefree **representability** in the dyadic terminal channel is localized to one coordinate.

## 5. Why the head atom cannot be discarded generically

The residual `m=1` is the lower row `s=2` at horizon `A`, with source argument exactly `B`. A quotient-preserving reembedding to row `u` requires a horizon near `uB`. The smallest nonsquarefree row is `u=4`, which returns to

\[
4B=H+O(1).
\tag{28}
\]

So forcing nonsquarefree support while preserving `\mathcal H(B)` exactly destroys the multiplicative descent for this one atom.

Nor can it be neglected merely because it is one coordinate. `FD-046` proves

\[
\limsup_{N\to\infty}
\frac{\log(1+|\mathcal H(N)|)}{\log N}
=\Theta,
\tag{29}
\]

so the source itself reaches the full polynomial frontier. A successful next step must use additional source coherence to rule out (25), absorb that spike into another recurrent structure, or solve the fixed-fraction composition problem for the repaired packets.

## 6. Stress test, prior art, and boundary

The correction is falsifiable at the smallest possible coordinate. The parent row `r=4` is assigned to `p=2`, first-deflates to `s=2`, and belongs to the squarefree terminal part. Its contribution is

\[
w(2)\mathcal H(\lfloor A/2\rfloor)^2
=\frac34|\mathcal H(B)|^2,
\]

but the proposed quarter-scale destination is `m=1`, excluded from `V_(B,1)`. Any identity claiming that the **entire** terminal energy is a mask of `V_(B,1)` therefore fails by exactly this amount.

For every `m>1`, there is no analogous boundary defect: `p(m)>=3`, the destination row `4m/p>=4` lies in the physical tail, (10) is an exact floor identity, and (11) is an exact Euler-factor identity. The coordinate transport itself uses no asymptotic estimate; asymptotics enter only in the horizon comparison and frontier normalization.

The algebra is internal to the Mathia Jordan-row representation. Literature on Farey fractions with squarefree or `k`-free denominators studies complete denominator families and their discrepancy; it does not supply the head-corrected deflation/reembedding mechanism here. No external theorem is load-bearing, so `SOURCES.md` requires no new dependency.

The durable frontier is narrower than in the withdrawn `FD-092`: the dyadic terminal support is deterministic, and every nonhead coordinate is exactly repairable. What remains is to decide whether the single row-two/source-head alternative (25) can persist on the same sharp occupied frontier, or whether source coherence forces enough mass into the repairable tail; separately, even a repaired frontier-sized nonsquarefree mask still needs a mechanism upgrading normalized size to a fixed occupation fraction in its lower state.
