# PC-226 — fixed-base fresh-prime leakage has finite residue-class limits

**Status:** `EXACT-DERIVED` + `DECISIVE-BOUNDARY` for the scalar cyclotomic variance profile left open by PC-224 and the fixed-coarse-base growing-fresh-prime limit left open by PC-225. Fix a coarse level `N>1`, let `q\nmid N` be prime, and use the normalized coefficient mask of `Phi_{Nq}` in the canonical refinement `H_N -> H_{Nq}`. Once the positive-square compression of PC-224 is taken, the dependence on a growing fresh prime is not an expanding mixed-conductor spectrum. For each residue class `r=q mod N`, all folded first and second coefficient moments are affine in `m=(q-r)/N`; consequently the complete conditional-variance profile is an explicit rational function of `m` and converges at rate `O_N(1/q)` to one of only finitely many profiles indexed by `r in U(N)`.

There is also an exact selection rule before that scalar compression: multiplication by the source coefficient mask carries the exact-order `N` Fourier sector to the pure exact-order `q` sector with **zero** amplitude. The new-prime leakage can therefore live only in mixed `q`-containing conductor sectors. This does not make those intermediate mixed vectors trivial, and it does not classify simultaneous limits in which the coarse base `N` also grows. It does close the specific escape in which one fixes `N`, lets one fresh prime tend to infinity, and hopes that the singular/positive-square spectrum itself acquires unbounded new structure.

## 1. The coefficient pattern is finite-state for fixed `N` and `q mod N`

Write

\[
\Phi_N(x)=\sum_{j=0}^{d}\alpha_jx^j,
\qquad d=\varphi(N),
\tag{1}
\]

and introduce the inverse cyclotomic polynomial

\[
\Psi_N(x):=\frac{x^N-1}{\Phi_N(x)}.
\tag{2}
\]

Since `deg Psi_N=N-d<N`, write

\[
\Psi_N(x)=\sum_{u=0}^{N-1}\psi_u x^u
\tag{3}
\]

with zero padding, and set `beta_u=-psi_u`. As a formal power series at the origin,

\[
\frac1{\Phi_N(x)}
=\frac{\Psi_N(x)}{x^N-1}
=-\frac{\Psi_N(x)}{1-x^N},
\tag{4}
\]

so its coefficients are exactly `N`-periodic:

\[
\boxed{
[x^k]\frac1{\Phi_N(x)}=\beta_{k\bmod N}
\qquad(k\ge0).
}
\tag{5}
\]

For a prime `q\nmid N`, the standard cyclotomic recursion gives

\[
\Phi_{Nq}(x)=\frac{\Phi_N(x^q)}{\Phi_N(x)}.
\tag{6}
\]

Put

\[
q=Nm+r,
\qquad 1\le r<N,
\qquad (r,N)=1.
\tag{7}
\]

The degree of `Phi_{Nq}` is `d(q-1)`. Assume `q>d`, which excludes only finitely many fresh primes for fixed `N`. For a coefficient index

\[
k=y+sN,
\qquad 0\le y<N,
\tag{8}
\]

inside the support, let

\[
t=\left\lfloor\frac{k}{q}\right\rfloor,
\qquad 0\le t\le d-1.
\tag{9}
\]

Combining (5) and (6) gives

\[
\begin{aligned}
[x^k]\Phi_{Nq}(x)
&=\sum_{j=0}^{t}\alpha_j\,
\beta_{(k-qj)\bmod N}\\
&=\sum_{j=0}^{t}\alpha_j\,
\beta_{(y-rj)\bmod N}.
\end{aligned}
\tag{10}
\]

Hence for fixed `N`, `r`, `y`, and band `t`, every coefficient in that residue/band is the same number

\[
\boxed{
c_{t,r}(y):=
\sum_{j=0}^{t}\alpha_j\beta_{(y-rj)\bmod N}.
}
\tag{11}
\]

The apparent coefficient growth as `q` increases is therefore only repetition of a finite table of at most `N d` integers. No asymptotic approximation has been used.

## 2. Every folded first and second moment is affine in `m`

Let `nu_{t,r,y}(m)` be the number of indices `k=y+sN` in the `t`-th band of `Phi_{Nq}`. For `0<=t<d-1`, that band is

\[
tq\le k\le(t+1)q-1,
\tag{12}
\]

whereas the last band is truncated at the polynomial degree,

\[
(d-1)q\le k\le d(q-1).
\tag{13}
\]

Counting one residue class modulo `N` in these intervals gives exactly

\[
\boxed{
\nu_{t,r,y}(m)=m+\varepsilon_{t,r,y},
}
\tag{14}
\]

where the intercept is independent of `m`. Explicitly, for `t<d-1`,

\[
\varepsilon_{t,r,y}
=
\left\lfloor\frac{(t+1)r-1-y}{N}\right\rfloor
-
\left\lceil\frac{tr-y}{N}\right\rceil+1,
\tag{15}
\]

and for `t=d-1`,

\[
\varepsilon_{d-1,r,y}
=
\left\lfloor\frac{dr-d-y}{N}\right\rfloor
-
\left\lceil\frac{(d-1)r-y}{N}\right\rceil+1.
\tag{16}
\]

Let `a_{Nq}(k)=[x^k]Phi_{Nq}(x)`, padded by zero to a full period of length `Nq`, and define the folded statistics from PC-224,

\[
S_{N,q}(y)=\sum_{s=0}^{q-1}a_{Nq}(y+sN),
\qquad
T_{N,q}(y)=\sum_{s=0}^{q-1}a_{Nq}(y+sN)^2.
\tag{17}
\]

Equations (11) and (14) imply the exact affine laws

\[
\boxed{
S_{N,q}(y)=mC_{r,y}+D_{r,y},
\qquad
T_{N,q}(y)=mA_{r,y}+B_{r,y},
}
\tag{18}
\]

with finite-state constants

\[
C_{r,y}=\sum_{t=0}^{d-1}c_{t,r}(y),
\qquad
D_{r,y}=\sum_{t=0}^{d-1}\varepsilon_{t,r,y}c_{t,r}(y),
\tag{19}
\]

\[
A_{r,y}=\sum_{t=0}^{d-1}c_{t,r}(y)^2,
\qquad
B_{r,y}=\sum_{t=0}^{d-1}\varepsilon_{t,r,y}c_{t,r}(y)^2.
\tag{20}
\]

The cyclotomic coefficient energy is therefore affine as well:

\[
\boxed{
h_{Nq}:=\sum_k a_{Nq}(k)^2=mH_r+K_r,
}
\tag{21}
\]

where

\[
H_r=\sum_{y\bmod N}A_{r,y},
\qquad
K_r=\sum_{y\bmod N}B_{r,y}.
\tag{22}
\]

Thus the scalar statistics that survived PC-224 do not acquire an ever larger state space as the fresh prime grows. For fixed `N`, their entire dependence on `q` is one integer `m` plus the finite residue label `r`.

## 3. The PC-224 variance is rational in `q` and has finitely many limits

For the normalized source coefficient mask

\[
g_{Nq}(k)=\sqrt{\frac{Nq}{h_{Nq}}}\,a_{Nq}(k),
\tag{23}
\]

PC-224 proved

\[
L_{N,q}(g_{Nq})^*L_{N,q}(g_{Nq})
=M_{v_{N,q}},
\tag{24}
\]

with

\[
v_{N,q}(y)
=\frac{N}{h_{Nq}}
\left(
T_{N,q}(y)-\frac{S_{N,q}(y)^2}{q}
\right).
\tag{25}
\]

Substituting (7), (18), and (21) gives the exact formula

\[
\boxed{
v_{N,q}(y)=
\frac{N}{mH_r+K_r}
\left[
 mA_{r,y}+B_{r,y}
-
\frac{(mC_{r,y}+D_{r,y})^2}{Nm+r}
\right].
}
\tag{26}
\]

Consequently, along fresh primes in a fixed residue class `q congruent r (mod N)`, the limit exists and is

\[
\boxed{
V_{N,r}(y)
=
\frac{N}{H_r}
\left(
A_{r,y}-\frac{C_{r,y}^2}{N}
\right),
}
\tag{27}
\]

with

\[
\boxed{
\max_{y\bmod N}|v_{N,q}(y)-V_{N,r}(y)|
=O_N(q^{-1}).
}
\tag{28}
\]

There are at most `phi(N)` such accumulation profiles. If `P_N` denotes the exact-order `N` Fourier projector on the coarse space, then

\[
(L_{N,q}P_N)^*(L_{N,q}P_N)
=P_NM_{v_{N,q}}P_N,
\tag{29}
\]

so

\[
\boxed{
\left\|
P_NM_{v_{N,q}}P_N-P_NM_{V_{N,r}}P_N
\right\|
=O_N(q^{-1}).
}
\tag{30}
\]

Thus even after the source primitive sector is retained on the input side, the complete fixed-base positive-square/singular data has only finitely many operator-norm limits as the new prime tends to infinity. Increasing the fresh prime does not create an unbounded spectral packet in this architecture.

## 4. The pure fresh-prime exact-order channel vanishes identically

The scalarization above occurs only after retaining the whole new-`q` complement. Before that compression, one might hope that the pure exact-order `q` sector itself carries a distinguished cross-level channel. It does not.

Inside `H_{Nq}`, an exact-order `N` Fourier frequency has the form `qu` with `(u,N)=1`, while an exact-order `q` frequency has the form `Nv` with `(v,q)=1`. A matrix coefficient of multiplication by `g_{Nq}` between those frequencies is proportional to

\[
\Phi_{Nq}\!\left(
\zeta_{Nq}^{Nv-qu}
\right).
\tag{31}
\]

The exponent `Nv-qu` is nonzero modulo `q`, and for every prime `p|N` it is nonzero modulo `p`, because `u` and `q` are units modulo `N`. Hence

\[
\gcd(Nv-qu,Nq)=1.
\tag{32}
\]

The root in (31) is therefore primitive of exact order `Nq`, so it is a zero of `Phi_{Nq}`. If `P_N^{(Nq)}` and `P_q^{(Nq)}` denote the exact-order `N` and `q` projectors inside the refined space, equivalently using the canonical pullback `J_{N,qN}`, then

\[
\boxed{
P_q^{(Nq)}M_{g_{Nq}}J_{N,qN}P_N=0.
}
\tag{33}
\]

This is stronger than saying that the full leakage eventually scalarizes. The source primitive sector cannot jump directly into the pure new-prime sector at all. Any nonzero new-prime information must pass through mixed conductor sectors whose order is divisible by `q` and by a nontrivial divisor of `N`.

Equation (33) is consistent with PC-212's same-level fact that the cyclotomic coefficient mask has zero Fourier mass in its own exact-order sector, but it is a distinct cross-level selection rule for the post-PC-225 refinement architecture.

## 5. Exact control at `N=6`

For `N=6`,

\[
\Phi_6(x)=x^2-x+1,
\qquad
\Psi_6(x)=x^4+x^3-x-1,
\tag{34}
\]

so the periodic reciprocal coefficient packet in (5) is

\[
(1,1,0,-1,-1,0).
\tag{35}
\]

There are only two prime residue classes. For `q congruent 1 (mod 6)`, equation (27) gives

\[
\boxed{
V_{6,1}=
\left(1,\frac58,\frac58,1,\frac58,\frac58\right),
}
\tag{36}
\]

whereas for `q congruent 5 (mod 6)`,

\[
\boxed{
V_{6,5}=
\left(\frac58,1,\frac58,\frac58,1,\frac58\right).
}
\tag{37}
\]

The two limits differ, so the theorem is not claiming that the residue-class information disappears. What disappears is growth of the fixed-base state space: all sufficiently large fresh primes fall onto one of these finitely many rational asymptotic profiles, with only `O(1/q)` finite-size correction.

## 6. Prior-art audit and RH boundary

The algebraic ingredients are classical. Equation (6) is the standard prime-extension recursion for cyclotomic polynomials, and `Psi_N=(x^N-1)/Phi_N` is the ordinary inverse cyclotomic polynomial. The broad arithmetic of cyclotomic coefficients, including families with varying prime factors, is established territory; Carlo Sanna's 2022 survey already recorded in `research/prime_circle/SOURCES.md` is the line's current general boundary for coefficient arithmetic. The exact derivation above needs no unproved coefficient theorem: periodicity (5), the finite band table (11), and the affine counts (14) follow directly from the two polynomial identities.

Accordingly no novelty is claimed for inverse cyclotomic polynomials, the recursion (6), residue-class coefficient formulas, or fixed-prime-family coefficient theory. The durable content is the project-specific reduction of the **specific PC-224 conditional-variance operator** and the cross-level selection rule (33). A directed prior-art audit around inverse cyclotomic coefficients, fixed old factors with one free prime, and residue-class coefficient behavior did not supply an independent RH mechanism that would alter this classification.

The RH consequence is negative but bounded. At fixed `N`, letting a fresh prime `q` grow cannot by itself turn the PC-224/PC-225 leakage positive square into a Hilbert-Polya-type carrier: there are only finitely many residue-class limit operators, no new complex spectral parameter, no functional-equation symmetry, and no zero set. This does **not** classify the internal mixed-conductor vector before left-unitary compression, exact-order projectors inserted between several noncommuting source operations, chord/cotangent operators that genuinely mix coarse residues, or simultaneous limits with `N -> infinity`. Those are the admissible ways to evade the theorem; merely taking `q -> infinity` at a fixed coarse base is now closed.