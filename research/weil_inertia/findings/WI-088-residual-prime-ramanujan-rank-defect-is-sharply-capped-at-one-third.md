# WI-088 — residual prime Ramanujan pairwise rank defect is sharply capped at one third

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion and does not certify or repair the Yang--Yang one-sided fourth-moment candidate. It closes the remaining universal **prime pairwise-rank** question left by WI-081, WI-086 and WI-087: once the nearest-LCM boundary has passed both prime Ramanujan dimensions, the cross Gram can lose rank, but it can never lose asymptotically more than one third of the smaller primitive-frequency space. The exact Loewner--Bezout family of WI-087 attains this ceiling asymptotically, so the prime pairwise rank interface is quantitatively sharp.

Let `p<q` be distinct odd primes and let

\[
G_{p,q}^{(N)}=(U_p^{(N)})^*U_q^{(N)}
\]

be the finite-window primitive-frequency cross Gram of WI-081. Put

\[
\delta=\delta_N(p,q)
\]

for the distance from `N` to the nearest multiple of `pq`. In the genuinely residual regime

\[
\boxed{\delta>q-1,}
\tag{1}
\]

one has the universal lower bound

\[
\boxed{
\operatorname{rank}G_{p,q}^{(N)}
\ge
\min\left\{p-1,\left\lceil\frac{p+q}{3}\right\rceil\right\}.
}
\tag{2}
\]

Equivalently, with WI-086's residual transversality defect

\[
\tau_{p,q}(\delta)=(p-1)-\operatorname{rank}G_{p,q}^{(N)},
\]

one has

\[
\boxed{
\tau_{p,q}(\delta)
\le
\max\left\{0,
\left\lfloor\frac{2p-q-3}{3}\right\rfloor
\right\}.
}
\tag{3}
\]

The residual hypothesis (1) is essential. For smaller boundary length the rank itself can be at most `delta`, so (2) is not a statement about arbitrary finite windows.

WI-087 shows that (2)--(3) are asymptotically best possible. For its prime family

\[
p\equiv2\pmod3,\qquad q\equiv1\pmod3,\qquad q<2p,
\]

at the special boundary

\[
\delta=\frac{pq+p-q}{3},
\]

the exact rank is

\[
\operatorname{rank}G_{p,q}^{(\delta)}=\frac{p+q}{3},
\qquad
\tau_{p,q}(\delta)=\frac{2p-q-3}{3}.
\tag{4}
\]

Along the unconditional WI-087 sequence with `q/p -> 1`, therefore,

\[
\frac{\operatorname{rank}G}{p-1}\to\frac23,
\qquad
\frac{\tau}{p-1}\to\frac13.
\tag{5}
\]

Thus the `1/3` residual-defect scale is not proof slack: it is simultaneously a universal ceiling and an attained asymptotic obstruction.

## 1. Only the close-prime exceptional strip needs analysis

WI-081 already proves that if

\[
q\ge2p,
\]

then for every window

\[
\operatorname{rank}G_{p,q}^{(N)}
=\min\{\delta,p-1\}.
\tag{6}
\]

Under (1), this is simply full rank `p-1`, so (2) follows immediately. We may therefore assume

\[
p<q<2p.
\tag{7}
\]

Write

\[
d=q-p,
\qquad
\delta=kq+s,
\qquad
0\le s<q.
\tag{8}
\]

Because `p,q` are odd primes, `d` is a positive even integer. Condition (1) forces `k>=1`; and since by definition `delta<=pq/2`,

\[
1\le k\le\frac{p-1}{2}.
\tag{9}
\]

WI-081 proves full rank unless the remainder lies in the close-prime exceptional strip

\[
\boxed{d<s<p.}
\tag{10}
\]

Hence only (10) can contribute to the residual defect. The proof below works inside this strip and deliberately uses only a subset of the exact row-kernel equations, so every dimension bound obtained from it is safe for the true kernel.

## 2. The prime row-kernel equations force `d` exact zeros

WI-081 gives a concrete row-kernel model. A vector in the `p`-frequency row kernel can be represented by a `p`-periodic sequence

\[
f=(f_0,\ldots,f_{p-1}),
\qquad
\sum_{r\bmod p}f_r=0.
\tag{11}
\]

Orthogonality to every nontrivial `q`-frequency is equivalent to all `q` residue-class sums being equal. Since `q\equiv d\pmod p`, define

\[
S_j=
\begin{cases}
\displaystyle\sum_{\ell=0}^{k} f_{j+\ell d},&0\le j<s,\\[3mm]
\displaystyle\sum_{\ell=0}^{k-1} f_{j+\ell d},&s\le j<q,
\end{cases}
\tag{12}
\]

with the subscripts of `f` read modulo `p`. Then every kernel vector satisfies

\[
S_0=S_1=\cdots=S_{q-1}.
\tag{13}
\]

There are `d=q-p` pairs of `q`-residue classes which become the same class modulo `p`: `j` and `j+p`, for `0<=j<d`. In the exceptional strip, `j<s` while `j+p>=p>s`; hence the first member uses the long sum in (12) and the second the short sum. Subtracting their equal values gives

\[
\boxed{f_{j+kd}=0\qquad(0\le j<d).}
\tag{14}
\]

Thus every true row-kernel vector vanishes on the translated interval

\[
\boxed{
Z:=kd+\{0,1,\ldots,d-1\}\pmod p,
\qquad |Z|=d.
}
\tag{15}
\]

These forced zeros are the source of the quantitative defect ceiling.

## 3. Adjacent residue sums define a partial permutation

Subtract equal sums in (13) at indices separated by `d`.

If

\[
0\le j<s-d,
\]

then both `j` and `j+d` are in the long region of (12), so telescoping gives

\[
\boxed{f_{j+(k+1)d}=f_j.}
\tag{16}
\]

If instead

\[
s\le j<p,
\]

then `j,j+d<q` and both are in the short region, giving

\[
\boxed{f_{j+kd}=f_j.}
\tag{17}
\]

Introduce the intervals

\[
A=\{0,\ldots,s-d-1\},
\quad
C=\{s-d,\ldots,s-1\},
\quad
B=\{s,\ldots,p-1\}.
\tag{18}
\]

Thus `C` has exactly `d` elements and the domain

\[
D:=A\cup B=(\mathbf Z/p\mathbf Z)\setminus C
\]

has size `p-d`. Define a partial map

\[
g:D\longrightarrow\mathbf Z/p\mathbf Z
\]

by

\[
g(j)=
\begin{cases}
j+(k+1)d,&j\in A,\\
j+kd,&j\in B,
\end{cases}
\pmod p.
\tag{19}
\]

Equations (16)--(17) say exactly that

\[
f(g(j))=f(j)\qquad(j\in D).
\tag{20}
\]

The key finite identity is that `g` is not an arbitrary partial map. Its two images are

\[
g(A)=kd+\{d,d+1,\ldots,s-1\},
\]

\[
g(B)=kd+\{s,s+1,\ldots,p-1\}
\]

modulo `p`. They are disjoint and their union is

\[
\boxed{
g(D)=(\mathbf Z/p\mathbf Z)\setminus Z.}
\tag{21}
\]

Hence

\[
\boxed{
g:D\to(\mathbf Z/p\mathbf Z)\setminus Z
\text{ is a bijection}.}
\tag{22}
\]

View (19) as a directed graph with one edge `j -> g(j)` for each `j in D`. Every vertex has indegree one except the `d` vertices in `Z`, which have indegree zero; every vertex has outdegree one except the `d` vertices in `C`, which have outdegree zero. Therefore every connected component is either a directed cycle or a directed path starting in `Z` and ending in `C`.

By (14) and (20), every path component starting in `Z` is identically zero. A component not meeting `Z` cannot be a path, because every path source has indegree zero and therefore lies in `Z`; it is a directed cycle. Consequently the solution space of the **selected** equations (14), (16), (17) is parametrized by one constant for each directed cycle not meeting `Z`.

If there are `c` such free cycles, imposing the genuine row-kernel condition (11) removes one further dimension whenever `c>0`: the mean is the nonzero linear functional

\[
\sum_{i=1}^{c}|\mathcal C_i|a_i
\]

on the cycle constants. Since the full equations (13) can only shrink the space further,

\[
\boxed{
\tau_{p,q}(\delta)
=\dim\ker_{\rm row}G
\le\max\{0,c-1\}.
}
\tag{23}
\]

## 4. Every free cycle has length at least three

The graph has no fixed point. On `A`, a fixed point would require

\[
(k+1)d\equiv0\pmod p,
\]

and on `B` it would require

\[
kd\equiv0\pmod p.
\]

But `0<d<p`, so `d` is invertible modulo the prime `p`, while (9) gives

\[
1\le k< p,
\qquad
1<k+1<p.
\]

Thus neither congruence is possible.

There is also no directed 2-cycle. If both vertices lie in `A`, a 2-cycle would imply

\[
2(k+1)d\equiv0\pmod p;
\]

if both lie in `B`, it would imply

\[
2kd\equiv0\pmod p.
\]

Both are impossible because `p` is odd and the multipliers lie strictly between `0` and `p` in the relevant range.

For a mixed `A/B` 2-cycle, the total translation around the cycle is

\[
(2k+1)d\equiv0\pmod p.
\tag{24}
\]

Using (9), this forces

\[
2k+1=p,
\qquad
k=\frac{p-1}{2}.
\tag{25}
\]

Write `d=2e`, possible because `p,q` are odd. Then modulo `p`,

\[
kd\equiv-e,
\qquad
(k+1)d\equiv e.
\tag{26}
\]

But for every `j in A`,

\[
0\le j\le s-d-1=s-2e-1,
\]

so the `A` edge is the ordinary, non-wrapping shift

\[
g(j)=j+e\le s-e-1<s.
\tag{27}
\]

It therefore cannot land in `B={s,\ldots,p-1}`. A mixed 2-cycle would necessarily contain an `A -> B` edge, contradiction.

Hence

\[
\boxed{\text{every free cycle has at least three vertices}.}
\tag{28}
\]

## 5. Counting cycle vertices gives the exact universal ceiling

No free cycle meets `Z`, and `|Z|=d`. Therefore at most

\[
p-d=2p-q
\]

vertices are available to all free cycles. By (28),

\[
\boxed{
c\le\left\lfloor\frac{2p-q}{3}\right\rfloor.}
\tag{29}
\]

Combining (23) and (29),

\[
\tau_{p,q}(\delta)
\le
\max\left\{0,
\left\lfloor\frac{2p-q}{3}\right\rfloor-1
\right\}
=
\max\left\{0,
\left\lfloor\frac{2p-q-3}{3}\right\rfloor
\right\},
\]

which proves (3).

To rewrite it as a rank statement, set `t=2p-q`. The elementary identity

\[
\left\lceil\frac{p+q}{3}\right\rceil
=p-\left\lfloor\frac{t}{3}\right\rfloor
\tag{30}
\]

shows that

\[
p-1-
\max\left\{0,\left\lfloor\frac{t}{3}\right\rfloor-1\right\}
=
\min\left\{p-1,\left\lceil\frac{p+q}{3}\right\rceil\right\}.
\]

This is exactly (2).

The proof uses only consequences of the exact kernel equations; it does not assume generic position, random phases, a large-sieve estimate, or a conjectural prime correlation.

## 6. WI-087 saturates the bound and closes the rank-only scale

For the WI-087 congruence family, `2p-q` is divisible by `3` and (4) gives

\[
\tau=\frac{2p-q}{3}-1
=\left\lfloor\frac{2p-q-3}{3}\right\rfloor.
\tag{31}
\]

Thus the upper bound (3) is attained exactly on that family at the WI-087 boundary. The earlier witness

\[
(p,q,\delta)=(11,13,47)
\]

has `2p-q=9`, so (3) gives `tau<=2`; WI-081/WI-087 give `tau=2`. Likewise every member of the exact WI-087 family realizes equality in the defect ceiling.

The asymptotic sequence `q/p -> 1` constructed in WI-087 then proves (5). Therefore neither of the following universal prime-pair hopes remains available:

\[
\tau=o(p)
\]

or, at the opposite extreme,

\[
\tau\text{ can consume more than about }p/3.
\]

The residual prime pairwise-rank interface has a sharp asymptotic phase boundary at rank fraction `2/3`.

## 7. Prior art and novelty boundary

The ingredients surrounding this statement are established or classical.

- WI-081 supplies the nearest-LCM boundary factorization, the prime row-kernel residue-sum model, the full-rank region outside the close-prime exceptional strip, and the original `(11,13,47)` defect witness.
- WI-086 identifies the residual defect `tau` exactly with row-kernel/excess-transversality dimension once `delta>q-1`.
- WI-087 supplies the exact Loewner--Bezout family attaining (3), together with the PNT-in-arithmetic-progressions sequence showing asymptotic one-third defect.
- The Ramanujan-subspace and exact-period background remains the classical literature already anchored in `SOURCES.md`, notably Vaidyanathan's 2014 Ramanujan-subspace papers and Ushiroya's 2018 Ramanujan-matrix spectral identities.
- The directed-graph argument above is elementary finite combinatorics: a partial bijection whose indegree and outdegree are at most one decomposes into paths and cycles.

A targeted audit around finite Ramanujan/Fourier cross-Gram rank, consecutive partial Fourier/Vandermonde systems, roots-of-unity divided differences, and the Loewner/rational-interpolation literature used in WI-087 located the neighboring classical structures but no direct theorem matching (2)--(3). This search result is **not** a priority or novelty claim. The durable claim here is the exact deduction from the already-audited prime kernel equations plus elementary finite graph structure.

## 8. Boundary conditions, falsification and research consequence

1. **Residual boundary is load-bearing.** Equation (2) is asserted only under `delta>q-1`. Applying it when `delta` is small is false in general because `rank G<=delta`.
2. **Primality/oddness enter concretely.** The argument uses the prime Fourier row-kernel reduction from WI-081, invertibility of `d mod p`, the bound on `k`, and parity of `d=q-p` in excluding mixed 2-cycles. No composite-modulus extension is asserted.
3. **Only selected kernel equations are used.** The graph omits the `d` transitions crossing the long/short boundary and most pairwise equalities among the `S_j`. Omitting equations enlarges the candidate kernel, so the resulting defect upper bound is one-sided in the safe direction.
4. **The zero-mean condition is essential for the final `-1`.** Without it, the selected graph equations allow one free constant per cycle; zero mean removes one dimension whenever a free cycle exists.
5. **Sharpness is independently anchored.** WI-087 gives exact equality examples, so any proposed improvement of the universal coefficient in (3) is immediately falsified by that family.
6. **This is a pairwise-rank closure, not a signed-inertia theorem.** It does not determine singular values, the weighted sum of several Ramanujan blocks, or the actual Yang coefficient law. WI-083--WI-085 already show that globally saturated scalar combinations can alias or cancel even when individual pairwise ranks are large.

The research consequence is therefore mostly a decisive narrowing. For residual **prime pairs**, rank alone is now understood at the correct scale: every cross Gram retains at least about two thirds of the smaller primitive-frequency dimension, and this is best possible. A useful continuation of the scalar signed-inertia route must exploit information that pairwise rank discards — singular-value magnitudes, source coefficients and signs, simultaneous consistency across several moduli, or source labels/factorizations erased by unlabelled scalarization — rather than seek a stronger universal prime pairwise-rank fraction.
