# FD-241 — Density-one point sampling is the sharp macroscopic signed-coercivity threshold

- **Date:** 2026-09-21
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response sampling / sharp density-one endpoint / signed linear capacity / quantitative inverse
- **Depends on:** FD-225, FD-238, FD-240
- **Classification:** `EXACT-DERIVED + SHARP-DENSITY-ONE-THRESHOLD + SIGNED-COERCIVITY + POINT-SAMPLING`

## Claim

FD-240 shows that every point-sampling density uniformly bounded below full density leaves a macroscopic signed nullspace for the divisor-response operator

\[
(\mathscr A b)(m)
=
\sum_{d\le m}b_d
M\!\left(\left\lfloor\frac md\right\rfloor\right).
\tag{1}
\]

The remaining density-one endpoint has the opposite behavior at the natural linear-capacity scale.

Let `S subset N` be a prescribed sampling set and let

\[
E=\mathbb N\setminus S,
\qquad
B_k=(2^{k-1},2^k]\cap\mathbb N,
\qquad
\delta_k=\frac{|E\cap B_k|}{|B_k|}.
\tag{2}
\]

For a real sequence `b=(b_n)` assume the linear envelope

\[
|b_n|\le Cn
\qquad(n\ge1)
\tag{3}
\]

for some fixed `C`, and suppose its response vanishes at every sampled point:

\[
(\mathscr A b)(m)=0
\qquad(m\in S).
\tag{4}
\]

Then

\[
\boxed{
\delta_k\to0
\quad\Longrightarrow\quad
\frac{\sum_{n\in B_k}|b_n|}
     {\sum_{n\in B_k}n}
\to0.
}
\tag{5}
\]

More quantitatively, if

\[
R(N)=|E\cap[1,N]|,
\tag{6}
\]

then for dyadic `N=2^k`,

\[
\boxed{
\frac{\sum_{N/2<n\le N}|b_n|}
     {\sum_{N/2<n\le N}n}
\ll
C\sqrt{\frac{R(N)+1}{N}}.
}
\tag{7}
\]

The implied constant is absolute.

Conversely, if `delta_k` does **not** tend to zero, then the pairwise construction of FD-240 gives an integer signed sequence with

\[
|b_n|\le n,
\qquad
(\mathscr A b)(m)=0\quad(m\in S),
\tag{8}
\]

and with macroscopic capacity on an infinite subsequence of octaves. In fact, writing

\[
\delta_*:=\limsup_{k\to\infty}\delta_k>0,
\tag{9}
\]

one may arrange

\[
\boxed{
\limsup_{k\to\infty}
\frac{\sum_{n\in B_k}|b_n|}
     {\sum_{n\in B_k}n}
\ge
\frac{\delta_*^2}{6C_\varphi}>0,
}
\tag{10}
\]

where

\[
C_\varphi
=
\sum_{d\ge1}\frac{\mu(d)^2}{d\varphi(d)}
<\infty.
\tag{11}
\]

Thus octave sample density tending to one is **exactly** the threshold at which exact point samples become coercive against macroscopic signed linear-capacity profiles. A proper density-one sampling set may still have a nontrivial exact kernel; what disappears is capacity-scale mass, not necessarily every nonzero coefficient.

## Exact response increments localize to omitted samples

Use the exact divisor inversion from FD-225. Define

\[
g=\mu*b.
\tag{12}
\]

Then `b=1*g`, and the response has first difference

\[
(\mathscr A b)(m)-(\mathscr A b)(m-1)=g(m).
\tag{13}
\]

With `Y(0)=0` and

\[
Y(m):=(\mathscr A b)(m),
\]

we therefore have

\[
Y(m)=\sum_{n\le m}g(n).
\tag{14}
\]

If both `m-1` and `m` lie in `S`, then (4) gives

\[
g(m)=Y(m)-Y(m-1)=0.
\]

Hence, apart from the harmless initial endpoint,

\[
\boxed{
\operatorname{supp}(g)
\subseteq
T:=E\cup(E+1).
}
\tag{15}
\]

If

\[
t(N)=|T\cap[1,N]|,
\]

then

\[
t(N)\le2R(N)+1.
\tag{16}
\]

This is the decisive distinction between density one and every fixed subfull density: exact sampled zeros force the Möbius-inverted response increments onto the omitted locations and their immediate successors.

## The linear coefficient envelope controls the sparse increments

From (12),

\[
g(n)
=
\sum_{d\mid n}\mu(d)b_{n/d}.
\]

Using (3),

\[
|g(n)|
\le
Cn\sum_{d\mid n}\frac1d
=
Cn\,\sigma_{-1}(n),
\tag{17}
\]

where

\[
\sigma_{-1}(n)=\sum_{d\mid n}\frac1d.
\]

The reciprocal-divisor sum has bounded mean square. Indeed,

\[
\begin{aligned}
\sum_{n\le x}\sigma_{-1}(n)^2
&=
\sum_{a,b\le x}\frac1{ab}
\left\lfloor\frac{x}{\operatorname{lcm}(a,b)}\right\rfloor\\
&\le
x\sum_{a,b\ge1}
\frac{\gcd(a,b)}{a^2b^2}.
\end{aligned}
\tag{18}
\]

Writing `a=ru`, `b=rv` and discarding the coprimality restriction on `u,v`,

\[
\sum_{a,b\ge1}
\frac{\gcd(a,b)}{a^2b^2}
\le
\sum_{r\ge1}\frac1{r^3}
\sum_{u,v\ge1}\frac1{u^2v^2}
=
\zeta(3)\zeta(2)^2.
\tag{19}
\]

Consequently, with

\[
C_2:=\zeta(3)\zeta(2)^2,
\]

Cauchy--Schwarz gives for every subset `A subset [1,N]`

\[
\boxed{
\sum_{d\in A}\sigma_{-1}(d)
\le
\sqrt{C_2N|A|}.
}
\tag{20}
\]

So a zero-density support cannot hide linear total reciprocal-divisor weight even if it is chosen adversarially among unusually divisor-rich integers.

## Quantitative capacity bound

Let `N=2^k`. Since `b=1*g`,

\[
|b_n|
\le
\sum_{d\mid n}|g(d)|.
\]

Summing over the octave `(N/2,N]` and using the support restriction (15),

\[
\sum_{N/2<n\le N}|b_n|
\le
\sum_{\substack{d\le N\\d\in T}}
|g(d)|
\#\{n\in(N/2,N]:d\mid n\}.
\tag{21}
\]

For `d<=N`,

\[
\#\{n\in(N/2,N]:d\mid n\}
\le
\frac{N}{2d}+1
\le
\frac{2N}{d}.
\tag{22}
\]

Combining (17), (20), and (22),

\[
\begin{aligned}
\sum_{N/2<n\le N}|b_n|
&\le
2CN
\sum_{\substack{d\le N\\d\in T}}
\sigma_{-1}(d)\\
&\le
2C\sqrt{C_2}\,N^2
\sqrt{\frac{t(N)}N}\\
&\le
2C\sqrt{C_2}\,N^2
\sqrt{\frac{2R(N)+1}{N}}.
\end{aligned}
\tag{23}
\]

Since

\[
\sum_{N/2<n\le N}n
=
\frac38N^2+O(N),
\tag{24}
\]

this proves (7).

Now octave density one means precisely

\[
\delta_k\to0.
\]

The dyadic decomposition gives

\[
R(2^k)
=
O(1)+
\sum_{j\le k}|E\cap B_j|,
\]

and the geometric weighting implies

\[
\delta_k\to0
\quad\Longrightarrow\quad
\frac{R(2^k)}{2^k}\to0.
\tag{25}
\]

Conversely,

\[
\delta_k
\le
2\frac{R(2^k)}{2^k},
\tag{26}
\]

so these two density-one formulations are equivalent. Equations (7) and (25) prove (5).

## Sharpness from the FD-240 pair construction

The lower direction does not require a new construction. In the notation of FD-240, the number `r_k` of disjoint consecutive pairs available inside the sample cells satisfies bandwise

\[
2r_k
\ge
|B_k|-|S\cap B_k|-1
=
\delta_k|B_k|-1.
\tag{27}
\]

With `N=2^k` and `|B_k|=N/2`,

\[
r_k\ge\frac{\delta_kN}{4}-\frac12.
\tag{28}
\]

FD-240 orients those pairs without changing any prescribed response zero and proves

\[
\sum_{n\in B_k}|b_n|
\ge
\frac{r_k^2}{C_\varphi}.
\tag{29}
\]

Dividing by (24) gives

\[
\frac{\sum_{n\in B_k}|b_n|}
     {\sum_{n\in B_k}n}
\ge
\frac{\delta_k^2}{6C_\varphi}+o(1)
\tag{30}
\]

along every subsequence on which `delta_k` stays bounded away from zero. Taking a subsequence approaching `delta_*` proves (10).

The same FD-240 sequence also has integer coefficients, exact zeros at all prescribed samples and dyadic endpoints, and all-integer response `O(m)`. Hence the upper threshold is sharp within the same source-side envelope used by the countermodels.

## Consequence for the response-sampling frontier

FD-238 showed that dyadic switched samples have a large exact signed kernel. FD-239 and FD-240 then showed that adding any point-sampling pattern with a fixed positive omitted fraction still leaves macroscopic signed capacity. The present result closes the remaining exact point-sampling density endpoint:

\[
\boxed{
\text{macroscopic signed kernel capacity survives}
\iff
\limsup_{k\to\infty}\delta_k>0.
}
\tag{31}
\]

Equivalently, sample density tending to one is necessary and sufficient for every exact-kernel profile satisfying `|b_n|=O(n)` to become capacity-negligible on dyadic octaves.

This is a quantitative coercivity statement, not injectivity. Omitting one point per octave, for example, leaves a proper infinite sampling set and may leave nonzero exact-kernel directions, but (7) forces all such linear-envelope directions to have normalized octave variation tending to zero. Full all-integer response remains the threshold for literal injectivity.

The response-side question is therefore no longer whether a density-one proper set can carry **macroscopic** signed capacity: it cannot. Any further exact point-sampling refinement must ask for a finer-than-capacity norm, approximate/noisy response stability, or extra source-side structure such as positivity or arithmetic coherence. None of those consequences supplies an RH estimate by itself.

## Stress tests and boundaries

The proof uses only exact sampled zeros. If sampled values are merely small rather than zero, `g(m)=Y(m)-Y(m-1)` is no longer supported on `E union (E+1)`, so (15) fails and a separate stability argument is required.

The linear envelope is also load-bearing. It enters through (17); without some coefficient-size control, arbitrarily large increments can be concentrated on a zero-density omitted set and then spread by divisor summation.

No positivity is assumed. The theorem is therefore genuinely about the signed response kernel and complements, rather than replaces, the positive-cone coercivity of FD-230--FD-233.

Finally, density one is meant octave-by-octave. A sampling set that is nearly full on some octaves but omits a fixed fraction on infinitely many others has `limsup delta_k>0` and remains noncoercive by (10).

## Prior-art and novelty boundary

A targeted literature check covered Möbius/Dirichlet inversion, support-density results for Dirichlet convolutions, sparse sampling, and Farey/Mertens discrepancy transforms. The standard ingredients behind (12)--(20) are classical, and general support-density theorems for Dirichlet convolutions exist, but no result located in that search matches the present statement: exact zeros on an arbitrary sampling set, a linear coefficient envelope, and a sharp density-one threshold for normalized divisor-response kernel capacity.

No external theorem is load-bearing. Möbius inversion, the support localization, the mean-square estimate (18)--(19), and the quantitative capacity bound are all derived here, while the converse construction is already canonical in FD-240. Accordingly no new `SOURCES.md` entry is required, and no broad novelty claim is made beyond this exact Farey/Mertens divisor-response formulation.
