# FD-009 — consecutive divisor-horizon compatibility exactly recovers the Möbius prefix

**Status:** `CLASSICAL-IDENTITY + EXACT-DERIVED + TRIANGULAR-RECOVERY + INFORMATION-BOUNDARY + NEGATIVE/OBSTRUCTION`. `FD-005` isolates the exact fixed-horizon Möbius identity

\[
\sum_{d\le N} M(\lfloor N/d\rfloor)=1,
\]

and `FD-008` shows that imposing one such horizon simultaneously with the exact squarefree support and unit-sign constraints still does not improve the leading Franel--Mertens GCD-energy dual constant. One apparent next cumulative route is to impose this divisor compatibility at more and more horizons. There is a sharp boundary: **the complete consecutive hierarchy is not an intermediate source condition at all. It is a lossless triangular encoding of the Möbius increments themselves.**

For any finite real sequence `a_1,...,a_N`, define

\[
H_a(m):=\sum_{n\le m}a_n\left\lfloor\frac mn\right\rfloor,
\qquad 1\le m\le N,
\qquad H_a(0):=0.
\tag{1}
\]

Then for every `K<=N`,

\[
\boxed{
H_a(m)=1\ \text{for every }1\le m\le K
\iff
a_n=\mu(n)\ \text{for every }1\le n\le K.
}
\tag{2}
\]

No squarefree-support, sign, multiplicativity, or integrality hypothesis is needed. More generally, the first `K` horizon values determine the first `K` increments by the exact inverse

\[
\boxed{
a_n
=\sum_{d\mid n}\mu(n/d)
\bigl(H_a(d)-H_a(d-1)\bigr),
\qquad n\le K.
}
\tag{3}
\]

Thus a proposed cumulative argument that enforces the physical floor identity at **every consecutive horizon** through a growing cutoff is progressively revealing the actual Möbius sequence, rather than extracting new coercivity from Farey discrepancy. This does not rule out sparse/nonconsecutive horizon constraints, compressed growing-depth summaries, multiplicative relations that do not invert pointwise, or ordered Farey information before denominator-shell collapse.

## 1. One discrete derivative converts the floor hierarchy into divisor sums

For every positive integer `m`,

\[
\begin{aligned}
H_a(m)-H_a(m-1)
&=\sum_{n\le m}a_n
\left(
\left\lfloor\frac mn\right\rfloor
-\left\lfloor\frac{m-1}{n}\right\rfloor
\right).
\end{aligned}
\tag{4}
\]

The bracket is exactly one when `n|m` and zero otherwise. Hence

\[
\boxed{
H_a(m)-H_a(m-1)=\sum_{n\mid m}a_n.
}
\tag{5}
\]

In Dirichlet-convolution notation, if

\[
g(m):=H_a(m)-H_a(m-1),
\]

then

\[
\boxed{g=a*\mathbf 1.}
\tag{6}
\]

The constant-one arithmetic function has Dirichlet inverse `mu`, so

\[
a=\mu*g.
\tag{7}
\]

Equation (3) is simply (7) written coefficientwise. This proves that the finite map

\[
(a_1,\ldots,a_K)
\longmapsto
(H_a(1),\ldots,H_a(K))
\tag{8}
\]

is invertible and lower triangular. The floor-quotient hierarchy therefore loses no information about the increment prefix.

## 2. The physical constant hierarchy is equivalent to the Möbius prefix

Suppose

\[
H_a(m)=1
\qquad(1\le m\le K).
\tag{9}
\]

Since `H_a(0)=0`, equation (5) gives

\[
\sum_{n\mid 1}a_n=1,
\qquad
\sum_{n\mid m}a_n=0\quad(2\le m\le K).
\tag{10}
\]

Equivalently,

\[
a*\mathbf1=\varepsilon
\qquad\text{through index }K,
\tag{11}
\]

where `varepsilon(1)=1` and `varepsilon(m)=0` for `m>1`. Uniqueness of the triangular Dirichlet inverse gives

\[
\boxed{a_n=\mu(n)\qquad(n\le K).}
\tag{12}
\]

Conversely, the elementary identity

\[
\sum_{d\mid m}\mu(d)=\varepsilon(m)
\tag{13}
\]

and summation of (5) from `1` through `m` give

\[
H_\mu(m)=1
\qquad(m\ge1),
\tag{14}
\]

recovering the physical floor identity of `FD-005`. Thus (2) is an exact equivalence, not merely a one-way rigidity statement.

A useful recursive version is visible without convolution notation:

\[
\boxed{
a_m=-\sum_{\substack{d\mid m\\d<m}}a_d
\qquad(m>1),
}
\tag{15}
\]

once the constant horizon hierarchy is imposed. Starting from `a_1=1`, this recursion is precisely the Möbius function.

## 3. Approximate consecutive horizons also recover the prefix quantitatively

The exact identity has a simple stability form. Put

\[
r_m:=H_a(m)-1\quad(m\ge1),
\qquad r_0:=0.
\tag{16}
\]

Subtracting the physical Möbius hierarchy from (5) gives

\[
\sum_{d\mid m}(a_d-\mu(d))
=
\begin{cases}
r_1,&m=1,\\
r_m-r_{m-1},&m\ge2.
\end{cases}
\tag{17}
\]

Möbius inversion therefore yields

\[
\boxed{
a_n-\mu(n)
=\sum_{d\mid n}\mu(n/d)\,\delta_d,
}
\tag{18}
\]

where `delta_1=r_1` and `delta_d=r_d-r_(d-1)` for `d>=2`. If

\[
\max_{1\le m\le K}|r_m|\le\epsilon,
\tag{19}
\]

then for every `n<=K`,

\[
\boxed{
|a_n-\mu(n)|
\le(2\tau(n)-1)\epsilon,
}
\tag{20}
\]

with `tau(n)` the divisor-counting function. The inverse can therefore amplify uniform horizon error by a divisor-count factor, but there is no hidden exponential instability in this exact finite triangular map.

In particular, if the increments are integer-valued and

\[
(2\tau(n)-1)\epsilon<1,
\]

then (20) forces `a_n=mu(n)` exactly at that index. This is only a finite stability observation; it does not supply any new bound for the true Möbius sequence.

## 4. Consequence for the cumulative Farey route

The negative results `FD-004`--`FD-008` progressively test information that survives denominator-shell accumulation: hyperbola block constancy, one exact floor identity, fixed finite Jordan-moment families, squarefree ternary increments, and their one-horizon intersection. Those conditions remain genuine relaxations because they leave many synthetic sequences admissible.

The consecutive divisor-horizon hierarchy is categorically different. If a proposed relaxation requires

\[
H_a(1)=H_a(2)=\cdots=H_a(K)=1,
\tag{21}
\]

then it has not merely added `K` weak consistency conditions: by (2) it has exposed the exact target increments

\[
\mu(1),\ldots,\mu(K).
\tag{22}
\]

As `K` grows, this becomes progressively closer to feeding the Möbius source itself into the argument. Any resulting gain must therefore be audited for target re-encoding rather than interpreted automatically as a new Farey-geometric mechanism.

This does **not** prove that every growing-depth cumulative program is circular. Three materially different possibilities remain open:

1. impose identities only at a sparse or otherwise nonconsecutive set of horizons, for which adjacent differences in (5) are unavailable;
2. retain compressed growing-depth statistics that do not invert to individual Möbius increments;
3. leave the cumulative shell representation and use ordered gaps, adjacency, mediant ancestry, or refinement chronology before the information loss identified in `FD-001`--`FD-003`.

Nor does (2) show that fixing a prefix of length `K=o(N)` is useless for bounding the Franel--Mertens energy at horizon `N`; that is a separate quantitative question. The finding identifies the information content of the constraint family, not the optimal tradeoff between disclosed prefix length and a possible dual-constant gain.

## 5. Prior art and evidence boundary

The mathematical identities used above are classical. The floor identity

\[
\sum_{n\le m}\mu(n)\lfloor m/n\rfloor=1
\]

is a standard consequence of `sum_(d|m) mu(d)=varepsilon(m)` and appears in classical treatments of the Möbius function. The floor-quotient structure is already anchored for this line by Marc Deléglise and Joël Rivat, *Computing the Summation of the Möbius Function*, Experimental Mathematics **5**(4) (1996), 291--295, DOI `10.1080/10586458.1996.10504594`. General Möbius inversion is classical nineteenth-century arithmetic. A targeted literature check found the floor identity and the standard inversion formula as established material; no novelty is claimed for (3), (5), or (7).

The Mathia-specific contribution is the **information-boundary classification**: the natural all-consecutive-horizon strengthening left open after the one-horizon relaxation is lossless for the Möbius prefix and therefore cannot honestly be treated as an intermediate anonymous compatibility class. This is a negative research-program restriction, not a new number-theory theorem.

Nothing here improves the Franel--Landau discrepancy bound, controls `M(N)`, proves a smaller GCD-energy dual constant under sparse horizons, or advances RH directly. The result also does not apply to the proposed ordered Plücker/refinement carrier or to the gap-order spectral-allocation clue, both of which retain information before or outside this consecutive cumulative hierarchy.