# WI-105 — Full-packed defect kernels can be asymptotically parallel

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion and does not certify or repair the Yang--Yang one-sided fourth-moment candidate. It sharply limits the quantitative use of WI-104: although two distinct positive-defect fully packed target interactions at one source prime and one observation length have trivial common source kernel, that transversality is not uniform. There are infinitely many valid simultaneous full-packing configurations for which the smallest principal angle between the two source defect kernels tends to zero.

Equivalently, the exact incidence theorem

\[
K_1\cap K_2=\{0\}
\]

from WI-104 cannot by itself be upgraded to a fixed quantitative covariance gain through a uniform principal-angle bound. Any such gain must use additional information not contained in bare kernel incidence, such as singular-value/operator weights, arithmetic separation between the target moduli, positive-slack structure away from full packing, or a different aggregation invariant.

More precisely, there is an infinite sequence of odd source primes `p`, distinct odd target primes

\[
p<q_1<q_2<\frac{4p}{3},
\tag{1}
\]

and common observation lengths `N` for which both `(p,q_i,N)` lie in the genuinely residual positive-defect full-packing regime of WI-096/WI-102/WI-104. Writing

\[
t_i=2p-q_i
\tag{2}
\]

and

\[
K_i=\ker_{\rm left}\bigl((U_p^{(N)})^*U_{q_i}^{(N)}\bigr)
\subset\mathbf C^{p-1},
\tag{3}
\]

one has simultaneously

\[
K_1\cap K_2=\{0\}
\tag{4}
\]

and

\[
\boxed{
\|P_{K_1}P_{K_2}\|
\ge
\sqrt{\frac{t_2}{t_1}}.
}
\tag{5}
\]

The targets may moreover be chosen with

\[
q_2-q_1=O(\log p).
\tag{6}
\]

If `theta_p` denotes the smallest principal angle, defined by

\[
\cos\theta_p
=
\sup_{\substack{u\in K_1,\ v\in K_2\\
\|u\|=\|v\|=1}}
|\langle u,v\rangle|,
\tag{7}
\]

then

\[
\boxed{
\sin^2\theta_p
\le
\frac{q_2-q_1}{t_1}
=O\!\left(\frac{\log p}{p}\right)
\longrightarrow0.
}
\tag{8}
\]

Thus exact trivial intersection and asymptotically vanishing angle coexist inside the same full-packing arithmetic model.

## 1. A fixed modulus-three family forces a common quotient character

Take source primes

\[
p\equiv1\pmod3.
\tag{9}
\]

For each sufficiently large such `p`, the prime number theorem in arithmetic progressions for the fixed modulus `3` gives

\[
\#\left\{q:\ p<q<\frac{4p}{3},\ q\equiv2\pmod3\right\}
\sim\frac{p}{6\log p}.
\tag{10}
\]

Hence two such primes can be chosen with

\[
q_1<q_2,
\qquad
\Delta:=q_2-q_1=O(\log p)
\tag{11}
\]

by pigeonholing consecutive primes of that residue class inside an interval of length `p/3`. Because the `q_i` are odd and congruent modulo `3`,

\[
6\mid\Delta.
\tag{12}
\]

Put

\[
d_i=q_i-p,
\qquad
t_i=p-d_i=2p-q_i.
\tag{13}
\]

Then

\[
d_i\equiv1\pmod3,
\qquad
3\mid t_i,
\qquad
t_i>\frac{2p}{3}.
\tag{14}
\]

Since `d_2-d_1=Delta` and `6|Delta`, one also has

\[
3\mid\frac{d_2-d_1}{2}.
\tag{15}
\]

Choose an integer center `c` satisfying

\[
\frac{d_2}{2}<c<p-\frac{d_2}{2}
\tag{16}
\]

and

\[
c\equiv\frac{d_1}{2}\pmod3.
\tag{17}
\]

The interval in (16) has length `t_2>2p/3`, so for all sufficiently large `p` it contains an integer in the required residue class. Define

\[
\boxed{
\rho_i=c-\frac{d_i}{2}.
}
\tag{18}
\]

Then

\[
0<\rho_i<t_i,
\qquad
3\mid\rho_i,
\tag{19}
\]

where the second assertion for `i=2` uses (15). Consequently

\[
\boxed{
g_i:=\gcd(\rho_i,t_i)\ge3.}
\tag{20}
\]

The intervals

\[
C_i=\{\rho_i,\ldots,\rho_i+d_i-1\}
\tag{21}
\]

have the same center `c`, and since `d_1<d_2` they satisfy

\[
C_1\subsetneq C_2.
\tag{22}
\]

This is exactly the concentric-hole geometry identified in WI-104.

## 2. The two full-packed boundaries occur at one actual observation length

It remains to show that the data above are not merely abstract kernel charts: they can be realized simultaneously by one observation length `N` with the correct nearest-boundary convention.

For each `i`, `d_i` is nonzero modulo the prime `p`, so choose the unique

\[
k_i\in\{0,\ldots,p-1\}
\tag{23}
\]

such that

\[
k_i d_i\equiv\rho_i\pmod p.
\tag{24}
\]

Set

\[
r_i=k_iq_i+d_i+\rho_i.
\tag{25}
\]

Since `q_i=p+d_i`, equations (18), (24), and (25) give

\[
r_i
\equiv k_id_i+d_i+\rho_i
\equiv2\rho_i+d_i
=2c
\pmod p.
\tag{26}
\]

Hence

\[
r_1\equiv r_2\pmod p.
\tag{27}
\]

Because

\[
\gcd(pq_1,pq_2)=p,
\tag{28}
\]

the generalized Chinese remainder theorem gives an integer `N` satisfying

\[
\boxed{
N\equiv r_i\pmod{pq_i}
\qquad(i=1,2).
}
\tag{29}
\]

Also `0<r_i<pq_i`. If `r_i<=pq_i/2`, the nearest boundary is directly

\[
\delta_i=r_i=k_iq_i+s_i,
\qquad
s_i=d_i+\rho_i,
\tag{30}
\]

with

\[
s_i-d_i=\rho_i=[k_id_i]_p.
\tag{31}
\]

This is the full-packing identity of WI-104, with canonical `R_i=rho_i`.

If instead `r_i>pq_i/2`, use the complementary nearest boundary. An exact rearrangement gives

\[
pq_i-r_i
=(p-1-k_i)q_i+d_i+(t_i-\rho_i),
\tag{32}
\]

and

\[
(p-1-k_i)d_i
\equiv t_i-\rho_i
\pmod p.
\tag{33}
\]

Thus the complement is again in exact full packing, now with canonical start `R_i'=t_i-rho_i`. WI-104's source-side phase correction translates this complementary chart back to the **actual** deleted-interval start

\[
t_i-R_i'=\rho_i.
\tag{34}
\]

Therefore both signs of the nearest boundary realize the same actual hole (21), and (20) gives positive defect in either case. The construction is consequently a genuine simultaneous `(p,q_1,q_2,N)` configuration to which WI-104 applies.

In particular, WI-104 yields (4) for every member of this family.

## 3. A shared order-three character makes the kernels almost parallel

WI-104 identifies every full-packed source kernel exactly. Its unwrapped complement interval is

\[
I_i=[\rho_i-t_i,\rho_i-1],
\qquad |I_i|=t_i,
\tag{35}
\]

and every kernel vector has the form

\[
f(j)=0\quad(j\in C_i),
\qquad
f(w\bmod p)=F(w\bmod g_i)\quad(w\in I_i),
\tag{36}
\]

where `F` is a zero-mean function on `Z/g_i Z`. Because `3|g_i`, the nontrivial quotient character

\[
F_i(x)=e(x/3)
\tag{37}
\]

is available for both kernels. Thus define

\[
f_i(j)=0\quad(j\in C_i),
\qquad
f_i(w\bmod p)=e(w/3)\quad(w\in I_i).
\tag{38}
\]

The character has zero mean on `Z/g_i Z`, so

\[
f_i\in K_i.
\tag{39}
\]

The concentric geometry makes the overlap exact. Put

\[
r=\frac{d_2-d_1}{2}=\frac{\Delta}{2}.
\tag{40}
\]

The interval identity from WI-104 is

\[
I_2=[L_1+r,U_1-r]\subset I_1=[L_1,U_1].
\tag{41}
\]

On the common interval `I_2`, both vectors use the **same unwrapped integer `w`** in (38), hence

\[
f_1=f_2\quad\text{pointwise on }I_2.
\tag{42}
\]

Outside `I_2`, `f_2` vanishes. Therefore, with the standard inner product on source-residue functions,

\[
\boxed{
\langle f_1,f_2\rangle=t_2,
\qquad
\|f_i\|^2=t_i.
}
\tag{43}
\]

After normalization,

\[
\boxed{
\left|
\left\langle
\frac{f_1}{\sqrt{t_1}},
\frac{f_2}{\sqrt{t_2}}
\right\rangle
\right|
=
\sqrt{\frac{t_2}{t_1}}.
}
\tag{44}
\]

The residue-function parametrization used in WI-104 is a discrete Fourier transform of the row-coefficient vector:

\[
f(j)=\sum_{a=1}^{p-1}\lambda_a e(-aj/p).
\tag{45}
\]

Parseval gives

\[
\sum_{j\bmod p}|f(j)|^2
=p\sum_{a=1}^{p-1}|\lambda_a|^2,
\tag{46}
\]

and the same identity for cross inner products. Thus the common scalar factor `p` cancels under normalization, so (44) is the actual angle in the row-kernel subspaces `K_i subset C^(p-1)`.

By the variational definition (7), (44) gives

\[
\cos\theta_p\ge\sqrt{\frac{t_2}{t_1}},
\tag{47}
\]

and equivalently the product of orthogonal projections satisfies (5). Hence

\[
\sin^2\theta_p
\le1-\frac{t_2}{t_1}
=\frac{t_1-t_2}{t_1}
=\frac{q_2-q_1}{t_1}.
\tag{48}
\]

Using `t_1>2p/3` from (14) and `Delta=O(log p)` from (11) proves (8).

Notice the qualitative contrast: WI-104 still says `theta_p>0` for each finite member of the family because `K_1 cap K_2={0}`, but the sequence has no positive angle lower bound independent of `p`.

## 4. An exact mixed-sign finite instance

A small instance also checks that the complementary-boundary phase normalization is load-bearing rather than cosmetic. Take

\[
p=37,
\qquad q_1=41,
\qquad q_2=47,
\qquad c=8.
\tag{49}
\]

Then

\[
(d_1,d_2)=(4,10),
\quad
(t_1,t_2)=(33,27),
\quad
(\rho_1,\rho_2)=(6,3),
\quad
(g_1,g_2)=(3,3).
\tag{50}
\]

The solutions of `k_i d_i=rho_i (mod p)` are

\[
k_1=20,
\qquad k_2=4.
\tag{51}
\]

Equation (25) gives

\[
r_1=830,
\qquad r_2=201.
\tag{52}
\]

The generalized CRT has, for example,

\[
N=64544
\pmod{37\cdot41\cdot47}
=
64544\pmod{71299}.
\tag{53}
\]

For `(37,41)`, `r_1>37*41/2`, so the nearest boundary is the complement

\[
1517-830=687
=16\cdot41+4+27,
\tag{54}
\]

with canonical complement start `27=t_1-rho_1`; the WI-104 phase correction restores the actual start `rho_1=6`. For `(37,47)`, the direct boundary is

\[
201=4\cdot47+10+3,
\tag{55}
\]

with actual start `rho_2=3`. Both are therefore positive-defect full-packed interactions at the same `N`.

The common order-three characters satisfy exactly

\[
\langle f_1,f_2\rangle=27,
\qquad
\|f_1\|^2=33,
\qquad
\|f_2\|^2=27,
\tag{56}
\]

so their normalized overlap is

\[
\boxed{
\sqrt{\frac{27}{33}}
=\sqrt{\frac9{11}}.
}
\tag{57}
\]

This finite instance is only a stress test of the general derivation; no finite enumeration is used in the proof.

## 5. Prior art and novelty boundary

The language of principal angles and canonical correlations between subspaces is classical; see A. Björck and G. H. Golub, **Numerical methods for computing angles between linear subspaces**, *Mathematics of Computation* 27:123 (1973), 579--594, DOI `10.1090/S0025-5718-1973-0348991-3`. For complex spaces, the same projector/canonical-correlation viewpoint is standard. Equation (7) is used only as terminology for the elementary normalized-overlap calculation above.

The existence step (10)--(11) uses only the classical prime number theorem in arithmetic progressions for the fixed modulus `3`; no modern distribution-in-short-interval or large-sieve input is required. Because the interval has fixed relative length and contains asymptotically `p/(6 log p)` primes in the chosen residue class, the `O(log p)` neighboring gap follows by averaging rather than by a theorem on individual prime gaps.

The Ramanujan-subspace background and exact-period character coordinates are classical in signal processing; the surrounding source file already records P. P. Vaidyanathan's 2014 Ramanujan-subspace papers. Those works provide the general exact-period subspace framework, not the shared-source full-packing geometry derived in WI-096--WI-104.

A targeted search around principal angles of finite Ramanujan subspaces, finite-window nonorthogonality, canonical correlations, and exact-period subspace overlap did not locate the specialized statement (5)--(8) or the modulus-three simultaneous full-packing construction above. That negative search is **not** a claim of priority. The durable claim here is the exact consequence of the Mathia full-packing normal form plus classical fixed-modulus prime distribution.

## 6. Evidence boundary and program consequence

The obstruction is deliberately narrow. It proves that **kernel incidence alone** cannot supply a uniform transversality constant after WI-104. It does **not** prove that the smallest singular value of the concatenated cross Gram `[G_1 G_2]` tends to zero, nor that the corresponding weighted Yang covariance has no fixed lower bound. Near-parallel nullspaces can coexist with quantitatively strong action on their complements, and the arithmetic coefficients multiplying different target blocks may carry information that the unweighted principal-angle calculation discards.

Accordingly, WI-104 remains an exact source-labelled consistency law, but its next quantitative use must retain more than

\[
K_1\cap K_2=\{0\}.
\tag{58}
\]

A viable bridge must exploit at least one of: singular-value profiles of the cross Grams, coefficient-weighted target aggregation, quantitative separation of the quotient characters after the actual phase normalization, positive-slack layers beyond exact full packing, or a multi-target invariant that sees the operators rather than only their kernels.

This rules out a natural but too-weak route:

\[
\boxed{
\text{pairwise trivial source-kernel intersections}
\not\Longrightarrow
\text{uniform quantitative transversality}.
}
\tag{59}
\]

The decisive falsification test for any future covariance argument that cites WI-104 is therefore explicit: evaluate it on the fixed-modulus-three family above. If its quantitative gain depends only on a lower bound for principal angles or on an abstract direct-sum constant for the defect subspaces, the gain must collapse along this family.