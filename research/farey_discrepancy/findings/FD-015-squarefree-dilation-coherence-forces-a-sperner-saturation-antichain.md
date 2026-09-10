# FD-015 — squarefree dilation coherence forces a Sperner antichain of near-saturating horizons

**Status:** `EXACT-DERIVED + SOURCE-COHERENCE + SQUAREFREE-DILATION-GAP + REPEATED-PRIME-COLLISION + SPERNER-ANTICHAIN + MULTIHORIZON-BOUNDARY`. `FD-014` proves that one cumulative sequence cannot simultaneously approach the sharp square-GCD equality ray at horizons `N` and `2N`: the equality ray wants one shared coordinate near `-1/2` while a second shared coordinate is exactly zero. The same mechanism extends to every squarefree dilation, but the direct `q` versus `q^2` collision is not optimal when `q` is composite. If a prime `p` divides squarefree `q`, source coherence couples the `p`-coordinate at `H`, the `q`-coordinate at `qH`, and the `pq`-coordinate at `qH`; the equality ray wants the first two near `-1/p` and `mu(q)/q`, while the last is exactly zero because `pq` contains `p^2`.

This repeated-prime collision gives a stronger two-horizon saturation gap. Let

\[
Z:=\zeta(2)=\frac{\pi^2}{6}.
\]

For any real sequence `A` on the positive integers and any integer horizon `H`, define as in `FD-014`

\[
m_d^{(H)}:=A(\lfloor H/d\rfloor),\qquad
E_H:=(m^{(H)})^T K_Hm^{(H)},\qquad
K_H(d,e):=\frac{\gcd(d,e)^2}{de},
\tag{1}
\]

and

\[
R_H:=\frac{A(H)^2}{E_H}
\tag{2}
\]

when `E_H>0`, with `R_H:=0` when the vector is zero.

Let `q>=2` be squarefree and let `p|q` be prime. Put

\[
\epsilon_{q,p}:=\frac{2}{5pq},
\qquad
\kappa_{q,p}:=
\left(
\frac1Z+\frac{\epsilon_{q,p}^2}{Z^2}
\right)^{-1}
=
\left(
\frac1Z+\frac{4}{25p^2q^2Z^2}
\right)^{-1}.
\tag{3}
\]

Then

\[
\boxed{
\min\{R_H,R_{qH}\}<\kappa_{q,p}<Z
\qquad
(q\ {\rm squarefree},\ p\mid q\ {\rm prime},\ H\ge400q^2).
}
\tag{4}
\]

The strongest member of this family is obtained from the least prime factor `p_-(q)`. Write

\[
\kappa_q^\sharp:=\kappa_{q,p_-(q)}.
\tag{5}
\]

For prime `q` this is exactly the `q`/`q^2` scale proved previously. For composite squarefree `q`, (4) is strictly stronger: its certified deficit from `Z` is of order `(p_-(q)^2q^2)^{-1}` rather than `q^{-4}`.

The divisor-lattice consequence also sharpens. Fix distinct primes `p_1,...,p_k`, let

\[
P:=\prod_{i=1}^k p_i,
\qquad
d_S:=\prod_{i\in S}p_i
\quad(S\subseteq\{1,\ldots,k\}),
\tag{6}
\]

and define

\[
B(P):=
\max_{\substack{q\mid P\\q>1}}
q\,p_-(q),
\qquad
\epsilon_P^\sharp:=\frac{2}{5B(P)},
\qquad
\kappa_P^\sharp:=
\left(
\frac1Z+\frac{4}{25B(P)^2Z^2}
\right)^{-1}.
\tag{7}
\]

Assume `N>=400P^2` and set

\[
\mathcal A_N^\sharp(P)
:=
\left\{
S\subseteq\{1,\ldots,k\}:
R_{Nd_S}\ge\kappa_P^\sharp
\right\}.
\tag{8}
\]

Then

\[
\boxed{\mathcal A_N^\sharp(P)\ {\rm is\ an\ antichain}.}
\tag{9}
\]

Consequently Sperner's theorem gives

\[
\boxed{
|\mathcal A_N^\sharp(P)|
\le
\binom{k}{\lfloor k/2\rfloor}.
}
\tag{10}
\]

Thus at least

\[
2^k-\binom{k}{\lfloor k/2\rfloor}
\tag{11}
\]

of the `2^k` coherent horizons `Nd_S` satisfy `R_{Nd_S}<kappa_P^sharp`. The common gap is

\[
\boxed{
0<Z-\kappa_P^\sharp
=
\frac{\frac{4Z}{25B(P)^2}}
{Z+\frac{4}{25B(P)^2}}
<
\frac{4}{25B(P)^2}.
}
\tag{12}
\]

In the natural case where `P` is the product of the first `k` primes, `B(P)=2P`, so

\[
\boxed{
\kappa_P^\sharp
=
\left(
\frac1Z+\frac{1}{25P^2Z^2}
\right)^{-1},
\qquad
0<Z-\kappa_P^\sharp<\frac1{25P^2}.
}
\tag{13}
\]

The earlier direct all-dilation threshold decayed like `P^{-4}`. The repeated-prime compatibility therefore recovers two powers of multiplicative breadth for this family. This is a genuine quantitative strengthening, but it still does not bootstrap the constant-level coherence obstruction into an RH-critical exponent estimate.

## 1. The GCD equality ray remembers the Möbius squarefree pattern coordinatewise

Retain the inverse notation from `FD-003` and `FD-014`:

\[
u^{(H)}:=K_H^{-1}e_1,\qquad
C_H:=u_1^{(H)},\qquad
v^{(H)}:=\frac{u^{(H)}}{C_H}.
\tag{14}
\]

Those findings give

\[
1\le C_H\le Z,
\qquad
0\le Z-C_H\le\frac ZH,
\tag{15}
\]

together with the exact inverse-column formula

\[
 u_d^{(H)}
=d\sum_{\substack{r\le H\\d\mid r}}
\frac{\mu(r/d)\mu(r)}{J_2(r)}
\tag{16}
\]

and the coordinate-evaluation bound

\[
(K_H^{-1})_{dd}\le Z^2.
\tag{17}
\]

If `d` is squarefree, write `r=d\ell` in (16). Nonzero terms require `ell` squarefree and coprime to `d`, and then

\[
\mu(\ell)\mu(d\ell)=\mu(d)\mu(\ell)^2,
\qquad
J_2(d\ell)=J_2(d)J_2(\ell).
\]

Hence

\[
\boxed{
 u_d^{(H)}
=
\frac{d\mu(d)}{J_2(d)}
\sum_{\substack{\ell\le H/d\\(\ell,d)=1}}
\frac{\mu(\ell)^2}{J_2(\ell)}.
}
\tag{18}
\]

The complete coprime Euler product is

\[
\sum_{\substack{\ell\ge1\\(\ell,d)=1}}
\frac{\mu(\ell)^2}{J_2(\ell)}
=
\prod_{r\nmid d}
\left(1+\frac1{r^2-1}\right)
=
Z\prod_{r\mid d}(1-r^{-2})
=
Z\frac{J_2(d)}{d^2},
\tag{19}
\]

where the product index `r` in the middle expression ranges over primes. Therefore

\[
\boxed{
 u_d^{(H)}\longrightarrow \frac{Z\mu(d)}d,
\qquad
v_d^{(H)}\longrightarrow\frac{\mu(d)}d.
}
\tag{20}
\]

The convergence has a uniform elementary error sufficient here. Since `J_2(n)>=n^2/Z`,

\[
\left|
 u_d^{(H)}-\frac{Z\mu(d)}d
\right|
\le
\frac{Z^2}{H-d}.
\tag{21}
\]

Using (15), if `H>=400d^2`, then

\[
\boxed{
\left|
v_d^{(H)}-\frac{\mu(d)}d
\right|
\le
\frac{Z^2}{H-d}+\frac{Z}{dH}
<\frac4H.
}
\tag{22}
\]

If instead `d` is nonsquarefree, every multiple of `d` is nonsquarefree, so `mu(r)=0` termwise in (16). Thus, whenever `d<=H`,

\[
\boxed{u_d^{(H)}=v_d^{(H)}=0.}
\tag{23}
\]

Equations (20)--(23) identify the underlying compatibility rule. For fixed squarefree `q` and squarefree `d`, simultaneous equality-ray behavior at `H` and `qH` would ask source ratios to satisfy both

\[
\frac{A(\lfloor H/d\rfloor)}{A(H)}\approx\frac{\mu(d)}d,
\qquad
\frac{A(H)}{A(qH)}\approx\frac{\mu(q)}q,
\tag{24}
\]

while the single `qd`-coordinate at `qH` asks

\[
\frac{A(\lfloor H/d\rfloor)}{A(qH)}
\approx
\frac{\mu(qd)}{qd}.
\tag{25}
\]

The limiting compatibility defect is therefore

\[
\boxed{
\frac{\mu(qd)-\mu(q)\mu(d)}{qd}.
}
\tag{26}
\]

For coprime squarefree `q,d`, Möbius multiplicativity makes (26) vanish. If `d=p` is a prime divisor of `q`, then `qp` is nonsquarefree and the absolute defect is exactly `1/(pq)`. The original `d=q` choice detects the same phenomenon with defect `1/q^2`; choosing a small repeated prime is stronger.

## 2. Repeating one prime factor gives the stronger two-horizon gap

For any nonzero horizon vector with first coordinate `t=m_1`, `FD-014` records the exact equality-ray projection identity

\[
\frac{\|m-tv^{(H)}\|_{K_H}^2}{t^2}
=
\frac1R-\frac1{C_H},
\tag{27}
\]

where `R=t^2/(m^TK_Hm)`. By (17), coordinate evaluation gives

\[
\left|
\frac{m_d}{t}-v_d^{(H)}
\right|
\le
Z\sqrt{\frac1R-\frac1{C_H}}.
\tag{28}
\]

If `R>=kappa_{q,p}`, then `C_H<=Z` and (3) imply

\[
\boxed{
\left|
\frac{m_d}{t}-v_d^{(H)}
\right|
\le\epsilon_{q,p}=\frac{2}{5pq}.
}
\tag{29}
\]

Assume `H>=400q^2` and suppose for contradiction that

\[
R_H\ge\kappa_{q,p},
\qquad
R_{qH}\ge\kappa_{q,p}.
\tag{30}
\]

If `A(H)` or `A(qH)` is zero, its ratio is already zero, so both are nonzero under (30). Put

\[
t:=A(H),\qquad
T:=A(qH),\qquad
s:=A(\lfloor H/p\rfloor).
\tag{31}
\]

The same source sequence supplies the exact shared coordinates

\[
\boxed{
 m_p^{(H)}=s,
\qquad
m_q^{(qH)}=t,
\qquad
m_{pq}^{(qH)}=s.
}
\tag{32}
\]

The first two equality-ray coordinates satisfy, by (22) and `H>=400q^2`,

\[
\left|v_p^{(H)}+\frac1p\right|
\le\frac4H
\le\frac1{100pq},
\tag{33}
\]

and

\[
\left|v_q^{(qH)}-\frac{\mu(q)}q\right|
\le\frac4{qH}
\le\frac1{100pq}.
\tag{34}
\]

Apply (29) to these two coordinates. Since `p,q>=2`,

\[
\begin{aligned}
\left|\frac st\right|
&\ge
\frac1p-\frac1{100pq}-\frac{2}{5pq}
>
\frac{3}{4p},\\
\left|\frac tT\right|
&\ge
\frac1q-\frac1{100pq}-\frac{2}{5pq}
>
\frac{3}{4q}.
\end{aligned}
\tag{35}
\]

Therefore

\[
\left|\frac sT\right|
=
\left|\frac st\right|
\left|\frac tT\right|
>
\frac9{16pq}.
\tag{36}
\]

But `pq` is nonsquarefree because `p|q`. Equation (23) and the same near-saturation bound (29), now at coordinate `pq` of the `qH` horizon, give

\[
\left|\frac sT\right|
\le
\frac{2}{5pq}.
\tag{37}
\]

Since `9/16>2/5`, (36)--(37) contradict each other. This proves (4).

The certified deficit is explicitly

\[
\boxed{
0<Z-\kappa_{q,p}
=
\frac{\frac{4Z}{25p^2q^2}}
{Z+\frac{4}{25p^2q^2}}
<
\frac4{25p^2q^2}.
}
\tag{38}
\]

The theorem uses no multiplicativity, sign condition, integrality, or Möbius-specific hypothesis on the source `A`. Möbius enters only through the exact inverse geometry of the GCD matrix. The squarefreeness of `q` and the repeated prime `p|q` are load-bearing: they make the first two equality coordinates nonzero but force the product coordinate to the square-killed zero stratum.

For `q=2`, choosing `p=2` recovers the same asymptotic defect scale as the dyadic argument, although `FD-014` keeps its sharper finite threshold `H>=101` and its original conservative constant.

## 3. The stronger pair gap yields a stronger Sperner threshold

Take the squarefree product `P` and divisor-indexed horizons from (6). Suppose `S` is a proper subset of `T` and put

\[
q:=\frac{d_T}{d_S}.
\tag{39}
\]

Then `q` is a squarefree divisor of `P` with `q>=2`. Let `p=p_-(q)`. The base horizon obeys

\[
Nd_S\ge N\ge400P^2\ge400q^2.
\tag{40}
\]

Moreover, by definition of `B(P)`,

\[
qp\le B(P),
\qquad
\epsilon_{q,p}\ge\epsilon_P^\sharp,
\qquad
\kappa_{q,p}\le\kappa_P^\sharp.
\tag{41}
\]

If both `S` and `T` belonged to `A_N^sharp(P)`, then both endpoint ratios would be at least `kappa_P^sharp`, hence at least `kappa_{q,p}`. Equation (4) applied at `H=Nd_S` would contradict this. Thus no two members of `A_N^sharp(P)` are comparable, proving (9). Sperner's theorem then gives (10)--(11).

Since the unrestricted one-horizon bound gives `R_H<=Z`, there is also the scalar average consequence

\[
\boxed{
\frac1{2^k}
\sum_{S\subseteq[k]}R_{Nd_S}
<
\kappa_P^\sharp+
\beta_k(Z-\kappa_P^\sharp),
\qquad
\beta_k:=
2^{-k}\binom{k}{\lfloor k/2\rfloor}.
}
\tag{42}
\]

This is an exact finite multihorizon bound. It should not be mistaken for a superior replacement of the fixed dyadic average in `FD-014`: if the divisor family contains `2`, pairing vertices along the `2` direction already supplies a fixed pair deficit. The Sperner statement contributes a different structural restriction—near-saturators above one common all-comparability threshold must lie in a single antichain-type layer.

For completeness, suppose now that

\[
P=p_1p_2\cdots p_k,
\qquad
2=p_1<p_2<\cdots<p_k
\tag{43}
\]

is the product of the first `k` primes. If a divisor `q` has least prime factor `p_j`, then `q p_-(q)` is maximized by taking

\[
q=p_jp_{j+1}\cdots p_k,
\]

so the candidate maximum is

\[
B_j=p_j^2\prod_{i>j}p_i.
\tag{44}
\]

Bertrand's postulate gives `p_{j+1}<2p_j<=p_j^2`, hence

\[
\frac{B_{j+1}}{B_j}=\frac{p_{j+1}}{p_j^2}<1.
\tag{45}
\]

Thus the maximum occurs at `j=1` and

\[
\boxed{B(P)=2P.}
\tag{46}
\]

Substitution into (7) proves (13). This improves the old common Boolean-lattice gap from order `P^{-4}` to order `P^{-2}`. It still tends to zero rapidly because the common threshold must handle arbitrarily broad comparable divisor ratios.

## 4. Transport back to the Farey/Franel normalization

For the physical sequence `A=\mathbf M`, the Mertens function, `FD-003` identifies at every horizon

\[
E_H
=
12\left(M_H\mathfrak F_H+\frac1{12}\right).
\tag{47}
\]

Hence for every squarefree `q>=2`, every prime `p|q`, and every `H>=400q^2`, at least one `X in {H,qH}` satisfies

\[
\boxed{
|\mathbf M(X)|^2
<
12\kappa_{q,p}
\left(
M_X\mathfrak F_X+\frac1{12}
\right).
}
\tag{48}
\]

Taking `p=p_-(q)` gives the strongest form `kappa_q^sharp`. Likewise, under `N>=400P^2`, at least the number of divisor-lattice horizons in (11) obey the same inequality with the common coefficient `12kappa_P^sharp`.

This is a genuine restriction on coherent physical horizons that is invisible to separate one-horizon optimization. It is nevertheless still a **ratio** estimate: it does not bound the absolute size of the Franel energies on those horizons and therefore does not imply `M(x)=O(x^{1/2+\varepsilon})`, an improved Franel exponent, or RH.

The stronger collision does sharpen the live cumulative question. A successful growing-depth program cannot merely count many horizons that fail exact saturation. It must couple cross-horizon nonsaturation to the **size or transport of the energies themselves**, or use arithmetic/source restrictions that prevent the interpolation mechanism of `FD-016`, while remaining compressed enough not to reconstruct the Möbius prefix as in `FD-009`.

## 5. Prior art, novelty boundary, and falsification controls

The GCD-matrix factorization, inverse divisor-incidence formula, Jordan-totient identity, and unrestricted equality-ray geometry are the classical ingredients already sourced in `FD-003` and `SOURCES.md`. The antichain bound is Sperner's classical 1928 theorem. The coordinate limit `v_d^(H)->mu(d)/d` is an immediate specialization of that existing inverse formula, not a new arithmetic theorem. A targeted search of the GCD-matrix and Farey-discrepancy literature did not identify a pre-existing theorem with this source-coherent repeated-prime horizon collision, but absence from that search is not a broad novelty claim.

The Mathia-specific derived content is the compatibility chain

\[
v_p^{(H)}\sim-1/p,
\qquad
v_q^{(qH)}\sim\mu(q)/q,
\qquad
v_{pq}^{(qH)}=0
\quad\Longrightarrow\quad
\min(R_H,R_{qH})<\kappa_{q,p},
\tag{49}
\]

and its application to the Franel--Mertens staircase across one coherent squarefree divisor family. The general defect formula (26) explains why the collision is specifically a failure of Möbius multiplicativity after the two equality-ray demands attempt to reuse a prime factor.

Several boundaries are load-bearing. First, the finite threshold `H>=400q^2` and constants in (3) are conservative, not optimized. Better decimals matter only if they expose a new transport mechanism.

Second, (4) is universal over real cumulative sources. It does not use exact Möbius floor identities or squarefree increments, so it remains safely below the source-reconstruction boundary of `FD-009`. Conversely, precisely because it is universal, it cannot supply the missing arithmetic cancellation by itself.

Third, the earlier `q^{-4}` common-gap scale was an artifact of choosing the `q^2` square-killed coordinate. For composite `q`, the repeated-prime coordinate `p_-(q)q` gives the stronger scale `(p_-(q)^2q^2)^{-1}`. This removes two powers for first-prime divisor lattices but **does not remove decay with multiplicative breadth**. The sparse interpolation theorem `FD-016` remains a complementary obstruction: when horizons are separated enough to plant fresh equality-ray prefixes, common-source consistency alone cannot force a scale-independent deficit.

Finally, (10) constrains only the set of horizons whose normalized coordinate ratio lies above `kappa_P^sharp`. It is not a bound on Mertens values, Franel energies, or a density of zeta zeros. The surviving target is a quantitative coupling between cross-horizon nonsaturation and energy size, or a genuinely Farey-specific chronology/ancestry invariant, strong enough to affect the critical scale without becoming a disguised reconstruction of the Möbius source.