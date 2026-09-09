# FD-015 — squarefree dilation coherence forces a Sperner antichain of near-saturating horizons

**Status:** `EXACT-DERIVED + SOURCE-COHERENCE + SQUAREFREE-DILATION-GAP + SPERNER-ANTICHAIN + MULTIHORIZON-BOUNDARY`. `FD-014` proves that one cumulative sequence cannot simultaneously approach the sharp square-GCD equality ray at horizons `N` and `2N`: the equality ray wants one shared coordinate near `-1/2` while a second shared coordinate is exactly zero. That mechanism is not peculiar to the prime `2`. For every squarefree dilation `q`, the normalized equality ray has its `q`-th coordinate asymptotic to `mu(q)/q` and its `q^2`-th coordinate exactly zero.

This gives a uniform two-horizon saturation gap for every fixed squarefree dilation. More importantly, putting many such dilations into one squarefree divisor lattice makes the set of simultaneously near-saturating horizons an antichain. Sperner's theorem then bounds how many horizons in that sparse multiplicative family can lie arbitrarily close to the unrestricted GCD-duality optimum.

Let

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

when `E_H>0`, with `R_H:=0` when the vector is zero. For every squarefree integer `q>=2`, put

\[
\epsilon_q:=\frac{2}{5q^2},
\qquad
\kappa_q:=
\left(
\frac1Z+\frac{\epsilon_q^2}{Z^2}
\right)^{-1}
=
\left(
\frac1Z+\frac{4}{25q^4Z^2}
\right)^{-1}.
\tag{3}
\]

Then

\[
\boxed{
\min\{R_H,R_{qH}\}<\kappa_q<Z
\qquad
(q\ {\rm squarefree},\ q\ge2,\ H\ge400q^2).
}
\tag{4}
\]

For `q=2`, the threshold `kappa_2` is exactly the constant `kappa` of `FD-014`; the earlier finding has the better finite range `H>=101`, while (4) is a deliberately uniform squarefree-dilation statement.

Now fix distinct primes `p_1,...,p_k`, let

\[
P:=\prod_{i=1}^k p_i,
\qquad
d_S:=\prod_{i\in S}p_i
\quad(S\subseteq\{1,\ldots,k\}),
\tag{5}
\]

and assume `N>=400P^2`. Define the near-saturating subset family

\[
\mathcal A_N(P)
:=
\left\{
S\subseteq\{1,\ldots,k\}:
R_{Nd_S}\ge\kappa_P
\right\}.
\tag{6}
\]

Then

\[
\boxed{\mathcal A_N(P)\ {\rm is\ an\ antichain}.}
\tag{7}
\]

Consequently Sperner's theorem gives

\[
\boxed{
|\mathcal A_N(P)|
\le
\binom{k}{\lfloor k/2\rfloor}.
}
\tag{8}
\]

Thus at least

\[
2^k-\binom{k}{\lfloor k/2\rfloor}
\tag{9}
\]

of the `2^k` coherent horizons `Nd_S` have `R_{Nd_S}<kappa_P`. The result is a genuine multi-horizon coherence restriction, but it also exposes a quantitative limitation: the explicit common threshold satisfies

\[
0<Z-\kappa_P
=
\frac{\frac{4Z}{25P^4}}
{Z+\frac{4}{25P^4}}
<
\frac{4}{25P^4}.
\tag{10}
\]

So this direct squarefree-dilation/Sperner amplification does not bootstrap the constant-level `FD-014` gap into an RH-critical exponent estimate. Increasing the multiplicative breadth forces more horizons away from exact saturation, but the common certified distance from `Z` becomes rapidly smaller.

## 1. Squarefree coordinates of the GCD equality ray

Retain the inverse notation from `FD-003` and `FD-014`:

\[
u^{(H)}:=K_H^{-1}e_1,\qquad
C_H:=u_1^{(H)},\qquad
v^{(H)}:=\frac{u^{(H)}}{C_H}.
\tag{11}
\]

Those findings give

\[
1\le C_H\le Z,
\qquad
0\le Z-C_H\le\frac ZH,
\tag{12}
\]

together with the exact inverse-column formula

\[
u_d^{(H)}
=
d\sum_{\substack{r\le H\\d\mid r}}
\frac{\mu(r/d)\mu(r)}{J_2(r)}
\tag{13}
\]

and the coordinate-evaluation bound

\[
(K_H^{-1})_{dd}\le Z^2.
\tag{14}
\]

Let `q>=2` be squarefree. In (13), write `r=q\ell`. A nonzero term requires `ell` squarefree and coprime to `q`; then

\[
\mu(\ell)\mu(q\ell)=\mu(q)\mu(\ell)^2,
\qquad
J_2(q\ell)=J_2(q)J_2(\ell).
\]

Hence

\[
\boxed{
u_q^{(H)}
=
\frac{q\mu(q)}{J_2(q)}
\sum_{\substack{\ell\le H/q\\(\ell,q)=1}}
\frac{\mu(\ell)^2}{J_2(\ell)}.
}
\tag{15}
\]

The complete coprime Euler product is

\[
\begin{aligned}
\sum_{\substack{\ell\ge1\\(\ell,q)=1}}
\frac{\mu(\ell)^2}{J_2(\ell)}
&=
\prod_{p\nmid q}
\left(1+\frac1{p^2-1}\right)\\
&=
Z\prod_{p\mid q}(1-p^{-2})
=
Z\frac{J_2(q)}{q^2}.
\end{aligned}
\tag{16}
\]

Therefore

\[
\boxed{
u_q^{(H)}\longrightarrow \frac{Z\mu(q)}q.
}
\tag{17}
\]

The convergence has a uniform elementary error sufficient here. Since `J_2(n)>=n^2/Z`, and since for `x>1`

\[
\sum_{\ell>x}\ell^{-2}\le\frac1{x-1},
\]

one obtains

\[
\begin{aligned}
\left|
u_q^{(H)}-\frac{Z\mu(q)}q
\right|
&\le
\frac q{J_2(q)}
Z\sum_{\ell>H/q}\frac1{\ell^2}\\
&\le
\frac{Zq^2}{J_2(q)(H-q)}
\le
\frac{Z^2}{H-q}.
\end{aligned}
\tag{18}
\]

Using (12) and `C_H>=1`, and now assuming `H>=400q^2`, gives the convenient uniform bound

\[
\boxed{
\left|
v_q^{(H)}-\frac{\mu(q)}q
\right|
\le
\frac{Z^2}{H-q}+\frac{Z}{qH}
<
\frac4H.
}
\tag{19}
\]

For the final inequality, use `Z<5/3`, `q>=2`, and `q/H<=1/800`; after multiplication by `H` the left-hand coefficient is at most
`(25/9)(800/799)+5/6<4`.

The complementary coordinate is exact rather than asymptotic:

\[
\boxed{
u_{q^2}^{(H)}=v_{q^2}^{(H)}=0
}
\tag{20}
\]

whenever `q^2<=H`, because every summation index in (13) is then divisible by a square and therefore has `mu(r)=0`.

Equations (19)--(20) are the squarefree-dilation pattern behind the special coordinates `v_2~-1/2` and `v_4=0` used in `FD-014`.

## 2. A uniform two-horizon gap for every squarefree dilation

For any nonzero horizon vector with first coordinate `t=m_1`, `FD-014` records the exact equality-ray projection identity

\[
\frac{\|m-tv^{(H)}\|_{K_H}^2}{t^2}
=
\frac1R-\frac1{C_H},
\tag{21}
\]

where `R=t^2/(m^TK_Hm)`. By (14), coordinate evaluation gives

\[
\left|
\frac{m_d}{t}-v_d^{(H)}
\right|
\le
Z\sqrt{\frac1R-\frac1{C_H}}.
\tag{22}
\]

If `R>=kappa_q`, then `C_H<=Z` and (3) imply

\[
\left|
\frac{m_d}{t}-v_d^{(H)}
\right|
\le\epsilon_q=\frac{2}{5q^2}.
\tag{23}
\]

Assume now that `H>=400q^2` and suppose for contradiction that

\[
R_H\ge\kappa_q,
\qquad
R_{qH}\ge\kappa_q.
\tag{24}
\]

If `A(H)` or `A(qH)` is zero, its ratio is already zero, so both are nonzero under (24). Put

\[
t:=A(H),\qquad
T:=A(qH),\qquad
s:=A(\lfloor H/q\rfloor).
\tag{25}
\]

The same cumulative sequence supplies the exact shared coordinates

\[
m_q^{(H)}=s,
\qquad
m_q^{(qH)}=t,
\qquad
m_{q^2}^{(qH)}=s.
\tag{26}
\]

By (19) and `H>=400q^2`,

\[
\left|
v_q^{(H)}-\frac{\mu(q)}q
\right|
\le\frac1{100q^2},
\qquad
\left|
v_q^{(qH)}-\frac{\mu(q)}q
\right|
\le\frac1{100q^2}.
\tag{27}
\]

Apply (23) to the `q` coordinate at both horizons. Since `q>=2`,

\[
\begin{aligned}
\left|\frac st\right|,
\left|\frac tT\right|
&\ge
\frac1q-\frac1{100q^2}-\frac{2}{5q^2}\\
&=
\frac1q-\frac{41}{100q^2}
>
\frac{3}{4q}.
\end{aligned}
\tag{28}
\]

Therefore

\[
\left|\frac sT\right|
=
\left|\frac st\right|
\left|\frac tT\right|
>
\frac9{16q^2}.
\tag{29}
\]

But (20) and (23), now at coordinate `q^2` of the `qH` horizon, give

\[
\left|\frac sT\right|
\le
\frac{2}{5q^2}.
\tag{30}
\]

Since `9/16>2/5`, (29)--(30) contradict each other. This proves (4).

The proof uses no multiplicativity, sign condition, integrality, or Möbius-specific input. It is a compatibility theorem for one cumulative sequence evaluated through the exact GCD-energy geometry. The squarefreeness of `q` is load-bearing: it produces the nonzero `mu(q)/q` equality coordinate while `q^2` lands exactly in the square-killed coordinate.

## 3. Sparse squarefree horizon families have an antichain of near-saturators

Take the squarefree product `P` and the divisor-indexed horizons from (5). The thresholds in (3) are monotone:

\[
q\le P
\quad\Longrightarrow\quad
\kappa_q\le\kappa_P.
\tag{31}
\]

Suppose `S` is a proper subset of `T`. Then

\[
q:=\frac{d_T}{d_S}
\tag{32}
\]

is a squarefree integer at least two and at most `P`, while

\[
Nd_T=q(Nd_S).
\tag{33}
\]

The base horizon satisfies

\[
Nd_S\ge N\ge400P^2\ge400q^2.
\tag{34}
\]

If both `S` and `T` belonged to `A_N(P)`, then both endpoint ratios would be at least `kappa_P`, hence at least `kappa_q`, contradicting (4). Thus no two members of `A_N(P)` are comparable, proving (7).

For a Boolean lattice on `k` elements, Sperner's theorem says that every antichain has size at most the central binomial coefficient. This gives (8)--(9) immediately.

There is also a scalar average consequence. Since the unrestricted one-horizon bound gives `R_H<=Z` for every horizon,

\[
\boxed{
\frac1{2^k}
\sum_{S\subseteq[k]}R_{Nd_S}
<
\kappa_P+
\beta_k(Z-\kappa_P),
\qquad
\beta_k:=
2^{-k}\binom{k}{\lfloor k/2\rfloor}.
}
\tag{35}
\]

This is an exact finite multihorizon bound. It should not be mistaken for a superior replacement of the dyadic average in `FD-014`. In particular, when the divisor family contains the prime `2`, pairing every divisor not containing `2` with twice that divisor already recovers the fixed `q=2` pair deficit on half the vertices. The Sperner statement contributes a different structural fact—only a central layer can remain above the common all-dilation threshold—but its common threshold `kappa_P` approaches `Z` as the breadth `P` increases.

Equation (10) quantifies that tradeoff explicitly. A naive strategy of adding more squarefree dilation directions and then applying one common near-saturation threshold therefore cannot manufacture an exponent gain from combinatorial breadth alone.

## 4. Transport back to the Farey/Franel normalization

For the physical sequence `A=M`, the Mertens function, `FD-003` gives at every horizon

\[
E_H
=
12\left(M_H\mathfrak F_H+\frac1{12}\right).
\tag{36}
\]

Hence (4) says that for every squarefree `q>=2` and `H>=400q^2`, at least one `X in {H,qH}` satisfies

\[
\boxed{
|\mathbf M(X)|^2
<
12\kappa_q
\left(
M_X\mathfrak F_X+\frac1{12}
\right).
}
\tag{37}
\]

Likewise, under `N>=400P^2`, at least the number of divisor-lattice horizons in (9) obey the same inequality with the common coefficient `12kappa_P`.

This is a genuine restriction on coherent physical horizons that is invisible to separate one-horizon optimization. It is nevertheless still a **ratio** estimate: it does not bound the absolute size of the Franel energies on those horizons, and therefore does not imply `M(x)=O(x^{1/2+\varepsilon})`, an improved Franel exponent, or RH.

The result sharpens the location of the live cumulative question. A successful growing-depth program must do more than show that many coherent horizons fail to saturate the unrestricted scalar GCD constant. It must couple that nonsaturation to the **size or transport of the energies themselves**, or find a weighted/multiscale compatibility whose gain does not disappear as its dilation complexity grows.

## 5. Prior art, novelty boundary, and falsification controls

The GCD-matrix factorization, inverse divisor-incidence formula, Jordan-totient identity, and unrestricted equality-ray geometry are the classical ingredients already sourced in `FD-003` and `SOURCES.md`. The antichain bound is Sperner's classical 1928 theorem. No novelty is claimed for either ingredient separately, nor for the elementary fact that divisors of a squarefree integer form a Boolean lattice.

The Mathia-specific derived content is the exact compatibility chain

\[
u_q^{(H)}\sim Z\mu(q)/q,\qquad
u_{q^2}^{(H)}=0
\quad\Longrightarrow\quad
\min(R_H,R_{qH})<\kappa_q,
\tag{38}
\]

and its application to the Franel--Mertens staircase across one coherent squarefree divisor family. A targeted literature search did not identify a pre-existing Farey-discrepancy theorem with this specific equality-ray/dilation formulation, but absence from that search is not a novelty claim.

Several boundaries are load-bearing.

First, the finite threshold `H>=400q^2` and the constant in (3) are conservative, not optimized. `FD-014` remains the sharper finite theorem for `q=2`. Better constants would matter only if they change the transport mechanism, not merely the decimal coefficient.

Second, (4) is universal over real cumulative sequences. It does not use the exact Möbius floor identity or squarefree signs, so it stays safely below the source-reconstruction boundary of `FD-009`. Conversely, precisely because it is universal, it cannot by itself supply the missing arithmetic cancellation.

Third, the `q^{-4}` scale in the certified saturation gap comes from needing `O(q^{-2})` control of the `q^2` coordinate in order to contradict a product naturally of size `q^{-2}`. The present proof therefore becomes weaker for large dilation even though the combinatorial antichain becomes stronger. A different norm, a weighted threshold, or additional arithmetic structure would need an independently proved stability gain before claiming that this decay has been overcome.

Finally, (8) constrains only the set of horizons whose **normalized coordinate ratio** lies above `kappa_P`. It is not a bound on the values of `M`, on the Franel energies, or on a density of zeta zeros. The surviving target is a quantitative coupling between cross-horizon nonsaturation and energy size that remains compressed enough not to reconstruct the Möbius prefix as in `FD-009`.
