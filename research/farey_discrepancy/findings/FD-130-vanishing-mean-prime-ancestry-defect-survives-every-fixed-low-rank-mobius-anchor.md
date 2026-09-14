# FD-130 — vanishing mean prime-ancestry defect survives every fixed low-rank Möbius anchor

**Status:** `EXACT-DERIVED + APPROXIMATE-ANCESTRY + PRIME-EDGE-GRAPH + FIXED-RANK-ANCHOR + VANISHING-MEAN-DEFECT + MACROSCOPIC-MOBIUS-DISAGREEMENT + NEGATIVE/OBSTRUCTION`.

`FD-129` shows that exact ancestry through a growing complete prime prefix, together with a uniform prefix envelope, stops being a free synthetic relaxation because it literally recovers the physical Möbius prefix. That leaves approximate or aggregate ancestry as one of the natural ways to weaken the condition without immediately rebuilding `mu` coefficient by coefficient.

There is an immediate obstruction to the most naive aggregate version. Even if one imposes **all prime directions available at the active scale**, agrees exactly with Möbius through any fixed multiplicative depth, and uses one common infinite squarefree-unit source, the unweighted mean ancestry defect can still tend to zero while the source disagrees with Möbius on a positive proportion of integers.

For `H>=2`, let

\[
\mathcal E_H
:=
\{(p,n): p\text{ prime},\ n\le H/p\text{ squarefree},\ p\nmid n\}.
\tag{1}
\]

Thus `(p,n)` records the complete prime-ancestry edge `n -> pn` available below `H`. For a squarefree-supported sign source `a`, define, for fixed `1<=r<infinity`,

\[
\mathfrak A_{r,H}(a)
:=
\frac1{|\mathcal E_H|}
\sum_{(p,n)\in\mathcal E_H}
|a_{pn}+a_n|^r.
\tag{2}
\]

Exact Möbius ancestry makes every summand zero. Fix any integer `K>=0`. There is one common infinite source `a^(K)` satisfying

\[
a^{(K)}_1=1,
\qquad
a^{(K)}_n=0\quad(n\text{ nonsquarefree}),
\qquad
a^{(K)}_n\in\{-1,+1\}\quad(n\text{ squarefree}),
\tag{3}
\]

such that

\[
\boxed{
a^{(K)}_n=\mu(n)
\quad\text{whenever }\omega(n)\le K,
}
\tag{4}
\]

but nevertheless

\[
\boxed{
\mathfrak A_{r,H}(a^{(K)})\longrightarrow0
\qquad(H\to\infty)
}
\tag{5}
\]

while, for an explicit constant `c_K>0`,

\[
\boxed{
\liminf_{H\to\infty}
\frac1H
\#\{n\le H:a^{(K)}_n\ne\mu(n)\}
\ge c_K>0.
}
\tag{6}
\]

In fact the ancestry defect is supported on a **single multiplicative-rank interface**. Hence no dimension-free stability estimate can bound coefficient disagreement from the unweighted mean defect (2). The problem is not insufficient prime breadth: the edge set already contains every prime direction below `H`. The problem is dilution of the low-rank anchor inside a graph whose number of ancestry edges is superlinear in `H`.

## 1. A fixed-rank gauge flip

On squarefree integers write

\[
b(n):=\mu(n)a(n).
\tag{7}
\]

Since `mu(pn)=-mu(n)` when `p` is prime, `n` is squarefree and `p\nmid n`, the ancestry law becomes simply

\[
a_{pn}=-a_n
\quad\Longleftrightarrow\quad
b(pn)=b(n).
\tag{8}
\]

The physical Möbius source is therefore the constant gauge `b\equiv1` on the squarefree prime-edge graph.

Fix `K>=0` and define

\[
 b_K(n)
 =
 \begin{cases}
 1,&n\text{ squarefree and }\omega(n)\le K,\\
 -1,&n\text{ squarefree and }\omega(n)>K.
 \end{cases}
\tag{9}
\]

Set

\[
a^{(K)}_n=
\begin{cases}
\mu(n)b_K(n),&n\text{ squarefree},\\
0,&n\text{ nonsquarefree}.
\end{cases}
\tag{10}
\]

Then (3)--(4) are immediate. Moreover an edge `n -> pn` changes `omega` by exactly one. Thus `b_K(pn)=b_K(n)` unless

\[
\omega(n)=K,
\tag{11}
\]

in which case the edge crosses from rank `K` to rank `K+1` and the gauge changes sign.

Let

\[
N_j(H):=
\#\{m\le H:m\text{ squarefree},\ \omega(m)=j\}.
\tag{12}
\]

Every squarefree `m` of rank `K+1` has exactly `K+1` prime parents `m/p`, and every defective edge arises uniquely in this way. Therefore the number of defective ancestry equations is **exactly**

\[
\boxed{
B_K(H)=(K+1)N_{K+1}(H).
}
\tag{13}
\]

On each such edge `|a_{pn}+a_n|=2`; on every other edge it is zero. Consequently

\[
\boxed{
\mathfrak A_{r,H}(a^{(K)})
=
2^r\frac{(K+1)N_{K+1}(H)}{|\mathcal E_H|}.
}
\tag{14}
\]

The point is that the numerator is at most linear in `H`, whereas the complete ancestry graph has `H` times a divergent prime-harmonic factor worth of edges.

## 2. The complete prime-edge graph has superlinear edge volume

Put

\[
c_0:=2-\zeta(2)-\frac13
=\frac53-\zeta(2)>0.
\tag{15}
\]

For an odd prime `p` and an integer `X>=1`, the number of squarefree `n<=X` is at least

\[
X-\sum_{q\text{ prime}}\left\lfloor\frac{X}{q^2}\right\rfloor
\ge
X\left(1-\sum_{m=2}^{\infty}\frac1{m^2}\right)
=(2-\zeta(2))X.
\tag{16}
\]

Discarding the multiples of `p` removes at most `X/p<=X/3`. Hence

\[
\#\{n\le X:n\text{ squarefree},\ p\nmid n\}
\ge c_0X.
\tag{17}
\]

For every odd prime `p<=sqrt(H)`, take `X=floor(H/p)`. Since `floor(H/p)>=H/(2p)` for large `H`, equations (1) and (17) give

\[
\boxed{
|\mathcal E_H|
\ge
\frac{c_0}{2}H
\sum_{3\le p\le\sqrt H}\frac1p.
}
\tag{18}
\]

The prime harmonic sum diverges. For completeness, this is the elementary Euler argument: if `sum_p 1/p` converged, then

\[
\prod_{p\le x}(1-1/p)^{-1}
\]

would stay bounded because `-log(1-1/p)=1/p+O(1/p^2)`, while expanding the product includes every `1/n` with `n<=x`, so it is at least `sum_(n<=x)1/n`, which diverges. Therefore

\[
\boxed{
\frac{|\mathcal E_H|}{H}\longrightarrow\infty.
}
\tag{19}
\]

Since `N_(K+1)(H)<=H`, (14) and (19) prove (5) for every fixed `K` and every fixed finite `r>=1`.

This estimate deliberately uses no distribution theorem for almost-primes. The boundary layer may itself contain many vertices; it still occupies a vanishing fraction of the **edge volume** because the average number of available prime directions grows without bound.

## 3. The source remains macroscopically non-Möbius

The vanishing edge-average defect is not accompanied by coefficient recovery. Let

\[
P_K:=\prod_{j=1}^{K+1}p_j,
\tag{20}
\]

where `p_j` is the `j`-th prime. Every squarefree integer divisible by `P_K` has at least `K+1` prime factors, so (9)--(10) give

\[
a^{(K)}_n=-\mu(n)
e\mu(n).
\tag{21}
\]

There are a positive proportion of such integers. A self-contained lower bound is enough. Put `X=floor(H/P_K)` and restrict to integers

\[
m\le X,
\qquad
m\equiv1\pmod{P_K}.
\tag{22}
\]

They are automatically coprime to `P_K`. Remove those divisible by `q^2` for some prime `q\nmid P_K`. For each such `q`, the Chinese remainder theorem places the excluded integers in one residue class modulo `P_Kq^2`, so a union bound gives

\[
\begin{aligned}
\#\{m\le X:m\equiv1\!\!\pmod{P_K},\ m\text{ squarefree}\}
&\ge
\frac{X}{P_K}
\left(1-\sum_{q\text{ prime}}\frac1{q^2}\right)
-O(\sqrt X)\\
&\ge
(2-\zeta(2))\frac{X}{P_K}-O(\sqrt X).
\end{aligned}
\tag{23}
\]

For every retained `m`, the integer `n=P_Km` is squarefree, at most `H`, and satisfies (21). Thus

\[
\boxed{
\#\{n\le H:a^{(K)}_n\ne\mu(n)\}
\ge
(2-\zeta(2))\frac{H}{P_K^2}-O_K(\sqrt H).
}
\tag{24}
\]

This proves (6), for example with any fixed

\[
0<c_K<\frac{2-\zeta(2)}{P_K^2}.
\tag{25}
\]

More strongly, because every disagreement has magnitude `2`, for each fixed finite `r>=1`,

\[
\liminf_{H\to\infty}
\frac1H\sum_{n\le H}|a^{(K)}_n-\mu(n)|^r
\ge
2^r\frac{2-\zeta(2)}{P_K^2}>0,
\tag{26}
\]

whereas the normalized ancestry `r`-energy tends to zero by (5).

Hence there is no constant `C=C(K,r)` independent of `H` for which every squarefree-unit source obeys an unweighted stability inequality of the form

\[
\frac1H\sum_{n\le H}|a_n-\mu(n)|^r
\le
C\,
\frac1{|\mathcal E_H|}
\sum_{(p,n)\in\mathcal E_H}|a_{pn}+a_n|^r.
\tag{27}
\]

The failure already occurs for one fixed infinite source.

## 4. What this removes from the current frontier

`FD-129` leaves approximate or aggregate multiplicative breadth as a plausible way to add arithmetic information without exact low-prefix reconstruction. Equation (27) shows that **plain edge-averaged ancestry is too weak**, even at maximal prime breadth. The graph has a gauge mode that is constant on each side of one multiplicative-rank cut. A fixed-depth interface contains only `O(H)` bad edges, while the complete ancestry graph has `H\,omega(1)` edges; normalizing by total edge count erases the interface.

The obstruction survives any fixed amount of low-rank anchoring. For `K=0`, only the root-to-prime edges are defective. For `K=1`, the source agrees with Möbius at `1` and at **every prime**, and only the prime-to-semiprime interface carries defect. Arbitrary fixed `K` pushes the same defect to rank `K -> K+1` without changing the conclusion.

Therefore the next aggregate condition, if this route is to become coercive, must prevent precisely this dilution. Natural possibilities are an ancestry norm that gives nonvanishing weight to low multiplicative ranks, a level-by-level or prime-by-prime defect bound instead of one global mean, a uniform/local (`L^infinity`-type) condition, or an anchoring depth that itself grows with the active scale. A direct Fourier-skeleton energy inequality could also bypass coefficient recovery entirely.

This finding does **not** show that approximate ancestry can coexist with Fourier-skeleton saturation, and it does not supply a new square-root-envelope control. Indeed

\[
A_K(x)+M(x)
=
2\sum_{\substack{n\le x\\n\text{ squarefree}\\\omega(n)\le K}}\mu(n),
\tag{28}
\]

so the partial sums of this particular witness remain tied to the physical Mertens function. The conclusion is narrower: any argument that tries to pass from vanishing **unweighted mean ancestry defect** to Möbius-like coefficient recovery has no scale-uniform coercivity, even after finitely many multiplicative ranks are fixed exactly.

## 5. Adversarial checks and prior-art boundary

The main falsification points are built into the statement. The source is one common infinite source, so horizon dependence is not being used. Every available prime direction is included in `mathcal E_H`, so sparse prime coverage is not being used. The exact defect count (13) includes all `K+1` parent edges of each rank-`K+1` child, so no orientation or multiplicity is lost. The proof of (19) needs only the elementary divergence of the prime harmonic series, which is included above, and (24) uses only a square-divisibility union bound and the Chinese remainder theorem.

The result is specific to **unweighted global averaging over ancestry edges**. It says nothing against a supremum defect: the witness has maximum defect `2`. It also does not exclude weighted norms that keep the rank-`K` interface visible, nor does it cover an anchoring depth `K=K(H)` growing with `H`. Those are genuine different hypotheses and should not be inferred from (5).

A targeted literature search found the neighboring literature on multiplicative squarefree-supported sign functions, including Marco Aymone's work on functions resembling Möbius, and general divisor/hypercube graph literature. Those works concern exact multiplicativity, partial sums, or generic graph structure rather than this Mathia-specific stability question. No novelty is claimed for the general graph principle that a small edge boundary obstructs a Poincaré estimate. The line-specific content is the explicit rank-cut gauge witness inside the complete Möbius prime-ancestry graph and its consequence for the `FD-129` aggregate-breadth route. No external theorem is load-bearing, so `SOURCES.md` does not change.
