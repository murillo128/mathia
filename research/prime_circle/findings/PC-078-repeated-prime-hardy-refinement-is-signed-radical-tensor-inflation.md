# PC-078 — repeated-prime Hardy refinement is signed radical tensor inflation

**Status:** `EXACT-DERIVED` + `CLASSICAL-IDENTITY` + `NEGATIVE/OBSTRUCTION` + `PRIOR-ART-REDIRECTION`. The Ramanujan prime-power identity used below is classical. The exact tensor factorization of the Prime-Circle Hardy/Hilbert operator and of its canonical trace-class remainder is derived here. No theorem-level novelty is claimed for the general arithmetic or tensor-product ingredients.

PC-075 introduced the canonical nonlocal Hardy coupling

\[
(\Gamma_n)_{jk}=-\frac{c_n(j+k+1)}{j+k+1},\qquad j,k\ge0,
\]

and decomposed it into universal Hilbert channels plus a trace-class arithmetic remainder `T_n`. PC-076 and PC-077 then showed that the first two relative moments collapse respectively to parity-twisted von Mangoldt data and radical/divisor harmonic data. The natural remaining question is whether higher relative data can recover genuinely new information from **repeated-prime depth**.

For that part of the question there is an exact operator-level answer. If `p|n`, then after splitting Hardy indices modulo `p`,

\[
\boxed{\Gamma_{pn}\cong J_p\otimes\Gamma_n,}
\]

where `J_p` is the `p x p` reversal matrix. Under the compatible two-stage residue decomposition used in PC-075, the canonical trace-class remainder satisfies the equally exact identity

\[
\boxed{T_{pn}\cong J_p\otimes T_n.}
\]

Thus adding another copy of a prime already present in the conductor does not create a new Hardy/Hilbert operator shape. It only makes signed finite-dimensional copies of the previous level. Iterating to `rho=rad(n)` shows that the entire repeated-prime tower is a universal finite tensor inflation of the squarefree radical level.

## 1. Classical Ramanujan lifting identity

Let `p|n`. Write

\[
n=p^a r,\qquad p\nmid r.
\]

The standard prime-power formula for Ramanujan sums gives

\[
c_{p^{a+1}}(m)=0\qquad(p\nmid m),
\]

while, if `m=pm'`,

\[
c_{p^{a+1}}(pm')=p\,c_{p^a}(m').
\]

Because `p` is invertible modulo `r`,

\[
c_r(pm')=c_r(m').
\]

Multiplicativity in the modulus therefore yields the exact lifting law

\[
\boxed{
c_{pn}(m)=
\begin{cases}
p\,c_n(m/p),&p\mid m,\\
0,&p\nmid m.
\end{cases}}
\]

This identity is classical Ramanujan-sum arithmetic. Its role here is not a novelty claim; it is the arithmetic input that makes the full Hardy operator factor.

## 2. Splitting Hardy indices modulo the repeated prime

Define the unitary residue decomposition

\[
W_p:\ell^2(\mathbb Z_{\ge0})
\longrightarrow
\bigoplus_{r=0}^{p-1}\ell^2(\mathbb Z_{\ge0}),
\qquad
(W_px)_r(a)=x_{pa+r}.
\]

For

\[
j=pa+r,\qquad k=pb+s,
\qquad 0\le r,s<p,
\]

put

\[
m=j+k+1=p(a+b)+(r+s+1).
\]

Since

\[
1\le r+s+1\le2p-1,
\]

we have

\[
p\mid m
\quad\Longleftrightarrow\quad
r+s+1=p.
\]

If this condition fails, the Ramanujan lifting identity gives

\[
(\Gamma_{pn})_{pa+r,pb+s}=0.
\]

If `r+s+1=p`, then `m=p(a+b+1)` and

\[
\begin{aligned}
(\Gamma_{pn})_{pa+r,pb+s}
&=-\frac{c_{pn}(p(a+b+1))}{p(a+b+1)}\\
&=-\frac{c_n(a+b+1)}{a+b+1}\\
&=(\Gamma_n)_{ab}.
\end{aligned}
\]

Let

\[
(J_p)_{rs}=\mathbf1_{r+s=p-1}.
\]

Then `J_p` is the reversal/exchange matrix, so the preceding entrywise calculation proves

\[
\boxed{W_p\Gamma_{pn}W_p^*=J_p\otimes\Gamma_n.}
\]

This is an equality of bounded self-adjoint operators, not an asymptotic relation or a statement only about traces.

## 3. The PC-075 Hilbert core and trace-class remainder factor too

PC-075 groups indices modulo the conductor and writes

\[
W_n\Gamma_nW_n^*
=-\frac1n C_n\otimes H+T_n,
\]

where

\[
(C_n)_{uv}=c_n(u+v+1)
\]

and the `(u,v)` block of `T_n` is

\[
-\frac{c_n(u+v+1)}n
\left(H_{(u+v+1)/n}-H_1\right).
\]

At level `pn`, identify a residue `R mod pn` uniquely as

\[
R=pu+r,
\qquad
0\le u<n,
\quad 0\le r<p.
\]

For `R=pu+r` and `S=pv+s`, the lifting identity gives

\[
c_{pn}(R+S+1)=0
\]

unless `r+s+1=p`. On the surviving anti-diagonal,

\[
c_{pn}(R+S+1)=p\,c_n(u+v+1)
\]

and simultaneously

\[
\frac{R+S+1}{pn}=\frac{u+v+1}{n}.
\]

Hence, after the corresponding permutation of the finite residue coordinates,

\[
\boxed{C_{pn}\cong p\,J_p\otimes C_n}
\]

and therefore

\[
\boxed{
-\frac1{pn}C_{pn}\otimes H
\cong
J_p\otimes\left(-\frac1n C_n\otimes H\right).
}
\]

The generalized-Hilbert offsets also agree on every nonzero block, so subtracting the two canonical PC-075 models gives

\[
\boxed{T_{pn}\cong J_p\otimes T_n.}
\]

Thus the factorization is not merely a property of the full Hankel matrix whose universal core might hide a different relative correction. It survives **exactly after the universal Hilbert channels are removed**.

## 4. The whole repeated-prime tower reduces to the squarefree radical

Let

\[
n=\prod_p p^{a_p},
\qquad
\rho=\operatorname{rad}(n)=\prod_{p\mid n}p,
\qquad
m=\frac n\rho.
\]

Starting at the squarefree level `rho` and adjoining the remaining copies of each prime one at a time, the preceding factorization applies at every step because that prime is already present. Consequently there is a finite self-adjoint involution

\[
K_n:=\bigotimes_{p\mid n}J_p^{\otimes(a_p-1)},
\qquad
K_n^2=I_m,
\]

such that, up to the canonical residue permutations,

\[
\boxed{
\Gamma_n\cong K_n\otimes\Gamma_\rho,
\qquad
T_n\cong K_n\otimes T_\rho.
}
\]

The finite factor has dimension `m=n/rho`. Since

\[
\operatorname{tr}J_p=
\begin{cases}
1,&p\text{ odd},\\
0,&p=2,
\end{cases}
\]

we have

\[
\tau_n:=\operatorname{tr}K_n=
\begin{cases}
0,&4\mid n,\\
1,&4\nmid n.
\end{cases}
\]

Its `+1` and `-1` multiplicities are therefore

\[
\boxed{
M_+=\frac{m+\tau_n}{2},
\qquad
M_-=\frac{m-\tau_n}{2}.
}
\]

So the complete single-level Hardy operator at arbitrary prime-power depth consists of `M_+` copies of the radical-level operator and `M_-` copies with the sign reversed.

## 5. All Schatten moments and the Fredholm determinant obey universal inflation laws

Because `T_\rho` is trace class, every integer power `T_\rho^k`, `k>=1`, is trace class. From the tensor factorization,

\[
\operatorname{Tr}(T_n^k)
=\operatorname{tr}(K_n^k)\operatorname{Tr}(T_\rho^k).
\]

Since `K_n^2=I_m`, this gives the all-orders identity

\[
\boxed{
\operatorname{Tr}(T_n^k)=
\begin{cases}
m\,\operatorname{Tr}(T_\rho^k),&k\text{ even},\\
\tau_n\,\operatorname{Tr}(T_\rho^k),&k\text{ odd}.
\end{cases}}
\]

PC-076 and PC-077 are exact low-order controls of this stronger operator statement:

- repeated odd-prime depth leaves the first relative trace unchanged;
- a repeated factor `2` kills every odd relative moment;
- the second relative trace scales by `m=n/rho`, exactly matching the radical-invariance formula of PC-077.

The singular values of `T_n` are those of `T_\rho`, each repeated `m` times. Thus for every Schatten exponent `q>=1`,

\[
\boxed{
\|T_n\|_{\mathcal S_q}^q
=m\,\|T_\rho\|_{\mathcal S_q}^q.
}
\]

The factorization also controls the entire Fredholm determinant, not just its moments. Define

\[
D_n(z)=\det(I-zT_n).
\]

Diagonalizing the finite involution `K_n` gives

\[
\boxed{
D_n(z)=D_\rho(z)^{M_+}D_\rho(-z)^{M_-}.
}
\]

Therefore no Fredholm-determinant construction based solely on the canonical single-level remainder can acquire a new zero set from repeated-prime depth. It can only repeat or sign-reflect the squarefree radical-level determinant.

## 6. Prior-art and novelty audit

The arithmetic input is classical. Ramanujan's original sums, the standard prime-power formula, and multiplicativity in the modulus are already anchored in `SOURCES.md`; these immediately imply the lifting law used in Section 1. The Hilbert/Hankel background and the canonical decomposition being refined here are already anchored for PC-075 through Magnus, Rosenblum, Pushnitski--Yafaev, Ushiroya, and related sources.

The tensor-product consequences themselves are elementary once the lifting identity is inserted into the specific Prime-Circle coefficient pattern. They are therefore not presented as a new theorem of Ramanujan-sum or Hankel-operator theory. The durable result is the **exact classification inside this research branch**: the entire repeated-prime part of the PC-075 operator, including its trace-class arithmetic remainder and Fredholm determinant, contains no independent spectral shape beyond the squarefree radical level.

PC-051 is a useful internal comparison but not a duplicate. It found a repeated-prime fiber decomposition for the finite oriented cotangent primitive block, where detail modes become affine copies of a base operator. The present result concerns a different, infinite-dimensional Hardy/Hilbert operator and is sharper in form: repeated-prime refinement is a literal signed tensor copy, with no affine shift and with an exact factorization of the canonical trace-class remainder.

## 7. What this rules out, and what it leaves open

PC-077 left `Tr(T_n^k)` for `k>=3` and the Fredholm determinant as plausible places where higher relative information might survive. This finding does **not** evaluate those invariants at squarefree conductors, but it closes repeated-prime depth as their source of novelty:

\[
\boxed{
\text{repeated-prime Hardy refinement}
\longrightarrow
\text{finite signed tensor inflation of }\operatorname{rad}(n).
}
\]

In particular, no higher moment, Schatten norm, singular-value statistic, or Fredholm determinant of the canonical single-level `T_n` can extract genuinely new information from the exponents `a_p>1`; the exponent data only prescribe universal multiplicities and the elementary `4|n` odd-moment cancellation.

The result does **not** collapse the remaining squarefree problem. It leaves open:

- higher moments and the complete Fredholm determinant of `T_\rho` for squarefree `rho` with several distinct primes;
- cross-level Hardy operators coupling different conductors before the residue split;
- operators in which refinement itself acts dynamically rather than by inspecting one completed level;
- shell-dependent/nonlinear Hardy constructions not equivalent to the PC-075 multiplier block;
- the old/new cotangent coupling of PC-047 and subsequent embedded chord geometry;
- the global nonlinear uniformization/monodromy branch rooted in PC-017.

A viable continuation of the PC-075 branch should therefore concentrate on **squarefree mixed-prime interaction or genuinely cross-level structure**, not on increasing prime-power depth.

## 8. Falsification surface

The factorization has four direct failure points.

1. For every `p|n`, the Ramanujan lifting identity must satisfy
   \[
   c_{pn}(m)=p\,c_n(m/p)\mathbf1_{p\mid m}.
   \]
2. In the residue split `j=pa+r`, `k=pb+s`, divisibility by `p` must occur exactly on the single anti-diagonal `r+s=p-1`.
3. Under the compatible two-stage `pn -> p -> n` residue ordering, the finite channel matrix and generalized-Hilbert offsets must factor as stated, so that the PC-075 reference core and `T_n` both tensorize rather than only their sum.
4. Iterating different repeated primes must commute up to permutation of tensor factors; otherwise the radical-level reduction would depend on refinement order.

Direct exact checks of the Ramanujan identity and finite truncations of the Hardy matrix agree for representative repeated-prime steps including `6 -> 12`, `6 -> 18`, `9 -> 27`, and `10 -> 50`. The identities also recover the previously derived first- and second-trace scaling laws of PC-076 and PC-077. These are falsification controls only; the result rests on the exact derivation above.

## Research consequence

The higher-relative escape left by PC-077 is now sharply localized. Repeated prime powers are not an independent carrier at all for the canonical cyclotomic Hardy/Hilbert operator:

\[
\boxed{
\Gamma_n\cong K_n\otimes\Gamma_{\operatorname{rad}(n)},
\qquad
T_n\cong K_n\otimes T_{\operatorname{rad}(n)}.
}
\]

Any genuinely new Prime-Circle spectral information in this branch must already occur at squarefree mixed-prime level or in a construction that couples levels before this exact tensor decomposition.