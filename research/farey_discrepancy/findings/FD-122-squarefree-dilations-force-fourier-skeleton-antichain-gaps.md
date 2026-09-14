# FD-122 — squarefree dilations force Fourier-skeleton antichain gaps

**Status:** `EXACT-DERIVED + FLOOR-QUOTIENT-FOURIER-SKELETON + CROSS-HORIZON-COHERENCE + SQUAREFREE-DILATION-GAP + SPERNER-ANTICHAIN + REPRESENTATION-AWARE + ROUTE-NARROWING`.

`FD-121` proves that one common source cannot jointly approach the separate Fourier-skeleton equality rays at the dyadic horizons `N` and `2N`. The dyadic choice is not essential. The same mechanism extends to **every fixed squarefree dilation**, because Möbius inversion makes small skeleton excess control individual quotient coordinates, while multiplying a squarefree ratio by one of its own prime factors creates a repeated-prime coordinate on which the equality ray vanishes.

Let `Y` be any real source on the positive integers. For a horizon `H`, retain the notation

\[
\mathcal Q_H
=
\left\{\left\lfloor\frac Hm\right\rfloor:1\le m\le H\right\},
\qquad
x_H(k)
:=Y\!\left(\left\lfloor\frac Hk\right\rfloor\right),
\tag{1}
\]

\[
A_H(k)
:=
\sum_{d\mid k}d\,x_H(d),
\qquad
\mathcal E_H^{\mathcal Q}(Y)
:=
\sum_{k\in\mathcal Q_H}\frac{|A_H(k)|^2}{k^2},
\tag{2}
\]

and

\[
\Delta_H(Y)
:=
\mathcal E_H^{\mathcal Q}(Y)-|Y(H)|^2
=
\sum_{\substack{k\in\mathcal Q_H\\k>1}}
\frac{|A_H(k)|^2}{k^2}.
\tag{3}
\]

For every fixed squarefree integer `r>1` there is an explicit constant `c_r>0` such that, for all sufficiently large `N`,

\[
\boxed{
\Delta_N(Y)+\Delta_{rN}(Y)
\ge
c_r\bigl(|Y(N)|^2+|Y(rN)|^2\bigr).
}
\tag{4}
\]

More precisely, any chosen prime `p|r` gives an explicit positive constant `c_{r,p}` below, and one may take `c_r=max_{p|r}c_{r,p}`. Thus the pairwise coherence penalty of `FD-121` is not a peculiarity of doubling: **no squarefree dilation edge can have both endpoints track their own Möbius equality rays at vanishing relative error**.

Across a fixed finite prime cube this becomes a combinatorial obstruction. Horizons whose relative excess lies below one common threshold form an antichain under squarefree divisibility, hence occupy at most a Sperner layer. This does not yet yield a pointwise RH-scale bound—the constants deteriorate as the prime family grows, and repeated-prime/nonsquarefree transitions remain outside the present argument—but it rules out the simplest alternating-near-extremizer escape simultaneously in every squarefree direction of any fixed prime family.

## 1. Skeleton excess controls individual equality-ray coordinates

`FD-118` proves that `Q_H` is divisor-closed. Therefore Möbius inversion of (2) stays entirely inside the same skeleton:

\[
k\,x_H(k)
=
\sum_{d\mid k}\mu(k/d)A_H(d),
\qquad k\in\mathcal Q_H.
\tag{5}
\]

Since `A_H(1)=Y(H)`, subtracting the equality-ray coordinate gives

\[
x_H(k)-\frac{\mu(k)}kY(H)
=
\frac1k
\sum_{\substack{d\mid k\\d>1}}
\mu(k/d)A_H(d).
\tag{6}
\]

Cauchy--Schwarz against the energy weights in (3) yields the exact coordinate-stability bound

\[
\boxed{
\left|x_H(k)-\frac{\mu(k)}kY(H)\right|^2
\le
C_k\,\Delta_H(Y),
}
\tag{7}
\]

where

\[
C_k
:=
\sum_{\substack{d\mid k\\d>1}}
\mu(k/d)^2\left(\frac dk\right)^2
=
\sum_{\substack{e\mid k\\e<k}}
\frac{\mu(e)^2}{e^2}.
\tag{8}
\]

Thus `Delta_H` is not merely a global energy defect: it quantitatively controls the distance of every visible quotient coordinate from the `FD-119` Möbius equality ray.

A small membership lemma makes fixed coordinates available uniformly. If `k^2<=H`, then `k in Q_H`. Indeed, with `m=floor(H/k)` one has `m>=k` and

\[
km\le H<k(m+1)\le(k+1)m,
\tag{9}
\]

so `floor(H/m)=k`. This elementary observation is enough for all fixed-dilation statements below.

## 2. Every fixed squarefree dilation has a uniform pairwise gap

Fix squarefree `r>1` and a prime `p|r`. Assume `N>=r p^2`, which ensures

\[
p\in\mathcal Q_N,
\qquad
r,rp\in\mathcal Q_{rN}.
\tag{10}
\]

Write

\[
t:=Y(N),
\qquad
T:=Y(rN),
\qquad
s:=Y\!\left(\left\lfloor\frac Np\right\rfloor\right),
\tag{11}
\]

and

\[
a:=\sqrt{\Delta_N(Y)},
\qquad
b:=\sqrt{\Delta_{rN}(Y)}.
\tag{12}
\]

Applying (7) at horizon `N` with `k=p` gives, because `C_p=1` and `mu(p)=-1`,

\[
\left|s+\frac tp\right|\le a.
\tag{13}
\]

At horizon `rN`, the coordinate `k=r` sees the old endpoint exactly, `x_{rN}(r)=t`, so

\[
\left|t-\frac{\mu(r)}rT\right|
\le
\sqrt{C_r}\,b.
\tag{14}
\]

The repeated-prime collision is the decisive third coordinate. Since `p|r`, the integer `rp` is divisible by `p^2`, hence `mu(rp)=0`; and

\[
x_{rN}(rp)
=
Y\!\left(\left\lfloor\frac Np\right\rfloor\right)
=s.
\tag{15}
\]

Therefore (7) gives

\[
|s|\le\sqrt{C_{rp}}\,b.
\tag{16}
\]

Equations (13) and (16) imply

\[
|t|
\le
p\,a+p\sqrt{C_{rp}}\,b,
\tag{17}
\]

while (14) then gives

\[
|T|
\le
rp\,a
+r\left(p\sqrt{C_{rp}}+\sqrt{C_r}\right)b.
\tag{18}
\]

Let

\[
L_{r,p}
:=
\begin{pmatrix}
p & p\sqrt{C_{rp}}\\
rp & r\left(p\sqrt{C_{rp}}+\sqrt{C_r}\right)
\end{pmatrix}.
\tag{19}
\]

The coordinatewise bounds (17)--(18) imply

\[
|t|^2+|T|^2
\le
\|L_{r,p}\|_2^2(a^2+b^2).
\tag{20}
\]

Hence

\[
\boxed{
\Delta_N(Y)+\Delta_{rN}(Y)
\ge
c_{r,p}\bigl(|Y(N)|^2+|Y(rN)|^2\bigr),
\qquad
c_{r,p}:=\|L_{r,p}\|_2^{-2}>0.
}
\tag{21}
\]

If a formula avoiding the operator norm is preferred, the weaker but fully explicit choice

\[
c_{r,p}
=
\left[
 p^2+p^2C_{rp}+r^2p^2
 +r^2\left(p\sqrt{C_{rp}}+\sqrt{C_r}\right)^2
\right]^{-1}
\tag{22}
\]

also follows from the Frobenius norm. For squarefree `r`, the constants in (8) simplify to

\[
C_r
=
\prod_{q\mid r}(1+q^{-2})-r^{-2},
\qquad
C_{rp}
=
\prod_{q\mid r}(1+q^{-2}).
\tag{23}
\]

No arithmetic law of the source was used. The gap comes entirely from reusing the same source values at two horizons inside a reversible representation whose separate equality rays are incompatible.

## 3. Prime dilations admit a sharp three-mode constant

For a prime dilation `r=p`, one can avoid the coordinatewise estimates and minimize the three relevant modes exactly. For `N>=p^3`, the modes `p in Q_N` and `p,p^2 in Q_{pN}` are visible. With the notation (11),

\[
A_N(p)=t+ps,
\qquad
A_{pN}(p)=T+pt,
\qquad
A_{pN}(p^2)=T+pt+p^2s.
\tag{24}
\]

Consequently

\[
\Delta_N+\Delta_{pN}
\ge
\frac{(t+ps)^2}{p^2}
+
\frac{(T+pt)^2}{p^2}
+
\frac{(T+pt+p^2s)^2}{p^4}.
\tag{25}
\]

Minimizing over `s` gives

\[
\boxed{
\Delta_N+\Delta_{pN}
\ge
 t^2+\frac{2}{p}tT
 +\frac{2p^2+1}{2p^4}T^2.
}
\tag{26}
\]

The least eigenvalue of this quadratic form is

\[
\boxed{
c_p
=
\frac{
2p^4+2p^2+1
-
\sqrt{4p^8+8p^6+4p^2+1}
}{4p^4}
>0.
}
\tag{27}
\]

For `p=2`, (27) is exactly

\[
c_2
=
\frac{41-\sqrt{1553}}{64}
=0.0248731095238\ldots,
\tag{28}
\]

so this prime-family calculation recovers the exact `FD-121` three-mode constant. `FD-121` separately proves the slightly sharper low-horizon validity `N>=6` for `p=2`; the uniform membership criterion used here only claims `N>=8`. Equation (28) also corrects the decimal approximation printed in `FD-121`; its exact formula and proof were already correct.

The constants decrease with `p`—for example `c_3=0.0055524553...` and `c_5=0.0007692079...`. Thus the theorem gives a uniform gap for every **fixed** prime or squarefree dilation, but not a prime-uniform gap as the dilation itself grows.

## 4. A finite prime cube forces a Sperner antichain

Fix distinct primes

\[
P=\{p_1,\ldots,p_d\},
\qquad
P_*:=\prod_{j=1}^d p_j,
\qquad
p_*:=\max_j p_j.
\tag{29}
\]

Choose `N_0>=P_* p_*^2`, and for each subset `S subseteq {1,...,d}` set

\[
d_S:=\prod_{j\in S}p_j,
\qquad
H_S:=N_0d_S.
\tag{30}
\]

For each nonempty squarefree ratio `r=d_T/d_S` with `S subsetneq T`, choose one prime divisor `p(r)|r` and the constant `c_{r,p(r)}` from (21). Because the prime cube is finite,

\[
c(P)
:=
\min_{\varnothing\ne R\subseteq\{1,\ldots,d\}}
 c_{d_R,p(d_R)}
>0.
\tag{31}
\]

Call a subset `S` cheap when `Y(H_S) ne 0` and

\[
\frac{\Delta_{H_S}(Y)}{|Y(H_S)|^2}<c(P).
\tag{32}
\]

If two cheap subsets satisfied `S subsetneq T`, then applying (21) with base horizon `H_S` and ratio `d_T/d_S` would give

\[
\Delta_{H_S}+\Delta_{H_T}
\ge
c(P)\left(|Y(H_S)|^2+|Y(H_T)|^2\right),
\tag{33}
\]

contradicting (32) at both endpoints. Therefore the cheap subsets form an antichain in the Boolean lattice. By the finite Sperner bound,

\[
\boxed{
\#\{S:\ S\text{ cheap}\}
\le
\binom{d}{\lfloor d/2\rfloor}.
}
\tag{34}
\]

So the alternating loophole left by the single dyadic chain is substantially narrower than `FD-121` alone suggests. Inside any fixed prime cube, a common source cannot place near-extremizers on a comparable chain of squarefree dilations at all; they can survive only on an antichain layer.

This is not yet an asymptotic density theorem over all horizons. The common threshold `c(P)` deteriorates as the finite prime family grows, and the present repeated-prime collision does not cover nonsquarefree ratios. In particular, (34) should not be read as a pointwise gap for every designated horizon.

## 5. Representation boundary, internal precedent and review

The result adds **no new source coordinate**. By `FD-117`--`FD-118`, the Fourier skeleton is still an invertible carrier of the same quotient-Mertens information. What changes is the cost of asking one source to realize separate same-horizon equality geometries simultaneously. Equation (7) turns small energy excess into closeness to the corresponding equality ray; the squarefree/repeated-prime collision then makes two such approximations incompatible.

There is an important internal precedent. `FD-015` already found the same squarefree repeated-prime collision and Sperner-antichain combinatorics in the earlier GCD-duality geometry. Therefore the squarefree/Sperner idea itself is **not** a new conceptual source for this line. The new content of `FD-122` is the coordinate-stability lemma (7) and the resulting coercive transplant to the current minimal Fourier-skeleton energy after `FD-117`--`FD-121`. This distinction matters because `FD-120` showed that many strong single-horizon source laws can still be asymptotically invisible in this newer geometry.

The owner-role adversarial check targeted the inversion orientation, divisor closure, skeleton membership threshold, the `mu(rp)=0` collision, energy weights in (7), finite-cube thresholding and the scope of the Sperner consequence. All survive directly from (5)--(34). Symbolic minimization verifies (26)--(28), and finite exact/random skeleton evaluations were used only as regression checks, not as evidence for the proof.

No external theorem beyond the already internalized finite Sperner principle is load-bearing. A targeted scan of Farey/Mertens discrepancy, floor-quotient compression and Mertens-matrix literature found no matching Fourier-skeleton squarefree-dilation inequality; no new source dependency is therefore needed in `SOURCES.md`.

The remaining frontier is now sharper. **Cross-horizon coherence is coercive along every fixed squarefree dilation and forces finite-prime near-extremizers into antichains, but it still does not force a prescribed horizon to pay the energy gap.** A continuation must either control the repeated-prime/nonsquarefree transition escape, prevent the constants from collapsing as the prime family grows, or use genuine Möbius correlation/multiplicativity to transfer this network of pairwise gaps into a pointwise endpoint bound. If none of those mechanisms succeeds, cumulative Farey discrepancy has likely exhausted what this representation can provide without genuinely additional arithmetic data.
