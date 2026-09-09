# FD-014 — coherent dyadic horizons have a uniform GCD-duality saturation gap

**Status:** `EXACT-DERIVED + SOURCE-COHERENCE + TWO-HORIZON-DUAL-GAP + DYADIC-BLOCK-NONSATURATION`. `FD-003` proves that the normalized square-GCD form gives the sharp unrestricted one-horizon dual constant for extracting the first staircase coordinate, while `FD-004`--`FD-008` show that several increasingly arithmetic one-horizon relaxations still approach that constant. Those optimizations are horizon-dependent. Requiring the **same cumulative sequence** to generate the staircase at `N` and `2N` changes the geometry: the second coordinate at `N` is simultaneously the fourth coordinate at `2N`, but the unrestricted GCD equality ray wants its second coordinate near `-1/2` of the first and its fourth coordinate exactly zero.

This incompatibility gives a uniform finite gap. Let

\[
Z:=\zeta(2)=\frac{\pi^2}{6},
\qquad
\kappa:=\left(\frac1Z+\frac1{100Z^2}\right)^{-1}
=1.6349944922\ldots < Z.
\tag{1}
\]

For **every** real sequence `A` on the positive integers, define at horizon `H`

\[
m_d^{(H)}:=A(\lfloor H/d\rfloor),
\qquad
E_H:=(m^{(H)})^TK_Hm^{(H)},
\qquad
K_H(d,e):=\frac{\gcd(d,e)^2}{de},
\tag{2}
\]

and put

\[
R_H:=\frac{A(H)^2}{E_H}
\tag{3}
\]

when `E_H>0`, with `R_H:=0` for the zero vector. Then

\[
\boxed{
\min\{R_N,R_{2N}\}<\kappa
\qquad(N\ge101).
}
\tag{4}
\]

Thus the one-horizon constant `Z` cannot be jointly saturated at two coherent dyadic horizons. For the physical choice `A=\mathbf M`, where `\mathbf M` is the Mertens function, `FD-003` gives

\[
E_H=12\left(M_H\mathfrak F_H+\frac1{12}\right),
\tag{5}
\]

so for every `N>=101` at least one `H in {N,2N}` satisfies

\[
\boxed{
|\mathbf M(H)|^2
<12\kappa\left(M_H\mathfrak F_H+\frac1{12}\right).
}
\tag{6}
\]

The coefficient `12 kappa=19.6199339065...` is strictly below the unrestricted leading constant `12Z=2 pi^2=19.7392088021...`. This is a genuine source-coherence improvement, but only by a constant and only at an unspecified member of each dyadic pair. It does not improve the RH-critical exponent.

## 1. The equality ray has an exact zero fourth coordinate and a stable minus-one-half second coordinate

Retain the factorization of `FD-003` and write

\[
u^{(H)}:=K_H^{-1}e_1,
\qquad
C_H:=u_1^{(H)}=(K_H^{-1})_{11},
\qquad
v^{(H)}:=\frac{u^{(H)}}{C_H}.
\tag{7}
\]

`FD-003` gives

\[
C_H\le Z,
\qquad
0\le Z-C_H\le\frac ZH.
\tag{8}
\]

The inverse divisor-incidence factorization gives, for `1<=d<=H`,

\[
\boxed{
 u_d^{(H)}
=d\sum_{\substack{k\le H\\d\mid k}}
\frac{\mu(k/d)\mu(k)}{J_2(k)},
}
\tag{9}
\]

and

\[
\boxed{
(K_H^{-1})_{dd}
=d^2\sum_{\substack{k\le H\\d\mid k}}
\frac{\mu(k/d)^2}{J_2(k)}\le Z^2.
}
\tag{10}
\]

For (10), use `J_2(k)>=k^2/Z`, write `k=dl`, and bound the remaining sum by `zeta(2)=Z`.

Equation (9) immediately gives

\[
\boxed{u_4^{(H)}=0}
\tag{11}
\]

because every summation index is divisible by four and hence has `mu(k)=0`.

For the second coordinate, put `k=2l`. Nonzero terms require `l` odd and squarefree, and then

\[
\mu(l)\mu(2l)=-1,
\qquad
J_2(2l)=3J_2(l).
\]

Therefore

\[
\lim_{H\to\infty}u_2^{(H)}
=-\frac23
\sum_{\substack{l\ge1\\l\ \mathrm{odd}}}
\frac{\mu(l)^2}{J_2(l)}.
\tag{12}
\]

The Euler product is

\[
\sum_{l\ \mathrm{odd}}\frac{\mu(l)^2}{J_2(l)}
=\prod_{p>2}\left(1+\frac1{p^2-1}\right)
=\frac34 Z,
\tag{13}
\]

so

\[
\boxed{u_2^{(H)}\longrightarrow-\frac Z2.}
\tag{14}
\]

The elementary tail estimate from `J_2(l)>=l^2/Z` gives the deliberately coarse finite bound

\[
\left|u_2^{(H)}+\frac Z2\right|\le\frac{2Z}{H}.
\tag{15}
\]

Combining (8) and (15),

\[
\boxed{
\left|v_2^{(H)}+\frac12\right|
\le\frac{5}{2(H-1)}
\le\frac1{40}
\qquad(H\ge101),
}
\tag{16}
\]

while `v_4^{(H)}=0` exactly.

## 2. Near saturation forces coordinatewise proximity to the equality ray

Let `m` be any nonzero real vector at horizon `H`, put `t=m_1`, and assume

\[
R:=\frac{t^2}{m^TK_Hm}>0.
\tag{17}
\]

Since `K_Hu^{(H)}=e_1`, the `K_H`-orthogonal projection of `m` onto the equality ray `span(u^{(H)})` is `t v^{(H)}`. Hence

\[
\boxed{
\frac{\|m-tv^{(H)}\|_{K_H}^2}{t^2}
=\frac1R-\frac1{C_H}.
}
\tag{18}
\]

Coordinate evaluation in the `K_H` norm has squared norm `(K_H^{-1})_{dd}`. Using (10) in (18) therefore gives

\[
\boxed{
\left|\frac{m_d}{t}-v_d^{(H)}\right|
\le
Z\sqrt{\frac1R-\frac1{C_H}}.
}
\tag{19}
\]

This inverse-diagonal factor is load-bearing; replacing it by the unit diagonal of `K_H` would be the wrong dual norm.

By the definition (1) of `kappa`, if `R>=kappa`, then `C_H<=Z` yields

\[
\frac1R-\frac1{C_H}
\le
\frac1\kappa-\frac1Z
=\frac1{100Z^2},
\]

and thus

\[
\boxed{
\left|\frac{m_d}{t}-v_d^{(H)}\right|\le\frac1{10}.
}
\tag{20}
\]

No arithmetic hypothesis has entered: (18)--(20) are the exact stability geometry of the unrestricted GCD coordinate inequality.

## 3. Coherence between `N` and `2N` contradicts simultaneous near saturation

For one underlying sequence `A`, set

\[
t:=A(N),
\qquad
T:=A(2N),
\qquad
s:=A(\lfloor N/2\rfloor).
\tag{21}
\]

The two staircase vectors satisfy the exact shared-coordinate identities

\[
m_1^{(N)}=t,
\qquad
m_2^{(N)}=s,
\tag{22}
\]

and

\[
m_1^{(2N)}=T,
\qquad
m_2^{(2N)}=t,
\qquad
m_4^{(2N)}=s.
\tag{23}
\]

If either `t` or `T` vanishes, the corresponding ratio in (4) is zero and there is nothing to prove. Suppose instead, for contradiction, that

\[
R_N\ge\kappa,
\qquad
R_{2N}\ge\kappa.
\tag{24}
\]

Apply (16) and (20) at horizon `N` to coordinate two. Since `|v_2^{(N)}|>=19/40`,

\[
\left|\frac{s}{t}\right|
\ge\frac{19}{40}-\frac1{10}
=\frac38.
\tag{25}
\]

Apply the same argument at horizon `2N` to coordinate two:

\[
\left|\frac{t}{T}\right|\ge\frac38.
\tag{26}
\]

But coordinate four at horizon `2N` has `v_4^{(2N)}=0`, so (20) gives

\[
\left|\frac{s}{T}\right|\le\frac1{10}.
\tag{27}
\]

Equations (25)--(26) instead imply

\[
\left|\frac{s}{T}\right|
=\left|\frac{s}{t}\right|
 \left|\frac{t}{T}\right|
\ge\frac9{64}
>\frac1{10},
\tag{28}
\]

contradicting (27). This proves (4).

The argument explains the mechanism more sharply than the numerical constant: one horizon wants the shared value `s` to be approximately `-t/2`, the next wants `t` approximately `-T/2`, but the same next-horizon equality geometry wants `s/T` approximately zero. A coherent cumulative source cannot satisfy all three requirements simultaneously.

## 4. The legitimate dyadic transport is additive, not multiplicative

The unrestricted one-horizon inequality in `FD-003` gives

\[
R_H\le C_H\le Z
\tag{29}
\]

for every horizon. Combining this with (4), each coherent dyadic pair satisfies

\[
\boxed{R_N+R_{2N}<Z+\kappa.}
\tag{30}
\]

Consequently, for any integer `m>=1` and `N>=101`, pairing the horizons

\[
N,2N,4N,\ldots,2^{2m-1}N
\]

into disjoint adjacent pairs gives

\[
\boxed{
\frac1{2m}\sum_{j=0}^{2m-1}R_{2^jN}
<\frac{Z+\kappa}{2}
=1.6399642795\ldots < Z.
}
\tag{31}
\]

In particular at least one member of every adjacent dyadic pair has `R<kappa`, so at least half of the horizons in every even-length dyadic block obey the improved constant (6).

This is the correct repeated consequence. It is a block-average saturation gap for the normalized dual ratios. It is **not** a multiplicative contraction, does not identify which parity of dyadic scale is good, and does not bound the Mertens values independently of the corresponding Franel energies. Alternating near-good and forced-worse scales remain compatible with (31).

## 5. Prior art, falsification controls, and boundary

The load-bearing matrix factorization, inverse formula, Jordan-totient identity and unrestricted equality ray are the classical GCD/Smith-matrix ingredients already audited and sourced in `FD-003` and `SOURCES.md`. The present derivation adds only the exact two-horizon floor-quotient compatibility (22)--(23) and its quantitative collision with that equality geometry. A targeted check of the current Farey-discrepancy and GCD-matrix literature found no additional theorem needed for this finite argument; no claim is made that generic multiscale quadratic compatibility is a novel concept.

Several boundaries are essential. The theorem holds for every real cumulative sequence `A`, so it does not use squarefree signs, multiplicativity, or specifically Möbius cancellation. Conversely, it uses only three shared coordinates and therefore does not exhaust the stronger full-horizon coherence that eventually reconstructs the source in `FD-009`. The constant `kappa` is conservative, not asserted optimal. Improving it is not by itself RH-relevant unless the stronger gap can be transported into a scale-sensitive estimate.

The strict inequality in (4) is a saturation statement, not an exponent theorem. Even the dyadic average (31) improves only a bounded constant. It cannot be converted into `M(x)=O(x^{1/2+epsilon})`, a stronger Franel exponent, or RH without a new argument coupling the **size** of the energies across scales. The natural next question is whether a growing but compressed hierarchy of coherent horizons yields such a quantitative transport before reaching the exact source reconstruction boundary of `FD-009`.
