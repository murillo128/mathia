# FD-118 — floor-quotient frequencies form a minimal linear Fourier skeleton for Farey discrepancy

**Status:** `EXACT-DERIVED + REPRESENTATION-CLASSIFICATION + FINITE-FOURIER-SKELETON + LINEAR-MINIMALITY + NEGATIVE/ROUTE-RESTRICTION`.

`FD-117` showed that the complete cumulative Farey discrepancy field at horizon `N` is invertibly equivalent to the quotient-Mertens staircase, but its explicit inverse used the first `N` positive Fourier modes. Most of that spectral bandwidth is redundant. The distinct floor quotients themselves index a square, exact and linearly minimal Fourier carrier for the same source.

For `N>=2`, put

\[
\mathcal Q_N
:=
\left\{
\left\lfloor\frac Nm\right\rfloor:
1\le m\le N
\right\},
\qquad
\tau_N(k):=\left\lfloor\frac Nk\right\rfloor,
\tag{1}
\]

and retain the normalized Fourier coordinate of `FD-117`,

\[
A_N(k)
:=
1+2\pi i k\,\widehat D_N(k).
\tag{2}
\]

Then `\tau_N` is an involution of `\mathcal Q_N`, the set `\mathcal Q_N` is closed downward under ordinary divisibility, and for every `k\in\mathcal Q_N`,

\[
A_N(k)
=
\sum_{d\mid k}
d\,M\!\left(\tau_N(d)\right).
\tag{3}
\]

All divisors in (3) remain inside `\mathcal Q_N`. Ordinary divisor Möbius inversion therefore stays entirely inside this floor-quotient set and gives

\[
\boxed{
M\!\left(\tau_N(k)\right)
=
\frac1k
\sum_{d\mid k}
\mu(k/d)A_N(d),
\qquad k\in\mathcal Q_N.
}
\tag{4}
\]

Because `\tau_N` permutes `\mathcal Q_N`, the positive Fourier modes with frequencies in `\mathcal Q_N` recover every distinct quotient-Mertens value `M(r)`, `r\in\mathcal Q_N`, and hence recover the full discrepancy field through `FD-117`. Every Fourier coefficient at every frequency outside this skeleton is consequently an explicit linear functional of the skeleton as well.

Moreover, this carrier has the exact formal source dimension. If the source vector is allowed to range over arbitrary real values indexed by `\mathcal Q_N`, the real-linear map from that vector to `(A_N(k))_{k\in\mathcal Q_N}` has determinant, up to sign,

\[
\boxed{
\prod_{k\in\mathcal Q_N}k\ne0.
}
\tag{5}
\]

Thus no family of fewer than `|\mathcal Q_N|` real linear measurements can be injective on the full formal source space. Since

\[
|\mathcal Q_N|
=
2\lfloor\sqrt N\rfloor+O(1),
\tag{6}
\]

indeed exactly either `2 floor(sqrt(N))` or `2 floor(sqrt(N))-1`, an explicit `2\sqrt N+O(1)` set of positive Fourier frequencies contains all same-horizon cumulative Farey-discrepancy information.

This is a representation theorem, not a new discrepancy estimate. It rules out **additional Fourier bandwidth** as a source of independent arithmetic information after `FD-117`; it does not rule out a stronger inequality obtained by exploiting the divisor/floor-quotient geometry of this finite skeleton.

## 1. The floor-quotient set is self-dual and divisor-closed

Take `k\in\mathcal Q_N`. By definition there is an integer `m>=1` with

\[
k=\left\lfloor\frac Nm\right\rfloor,
\qquad
\frac N{k+1}<m\le\frac Nk.
\tag{7}
\]

Set `j=\tau_N(k)=floor(N/k)`. Since `j>=m`, (7) gives `j>N/(k+1)`, while the definition of `j` gives `j<=N/k`. Hence

\[
k\le\frac Nj<k+1,
\tag{8}
\]

so

\[
\boxed{\tau_N(\tau_N(k))=k.}
\tag{9}
\]

Thus `\tau_N` is an involution, hence a permutation, of `\mathcal Q_N`.

Now write

\[
N=kj+r,
\qquad
0\le r<j,
\tag{10}
\]

where again `j=\tau_N(k)`. If `d\mid k`, write `k=ad`. Then

\[
\left\lfloor\frac N{aj}\right\rfloor
=
\left\lfloor d+\frac r{aj}\right\rfloor
=d,
\tag{11}
\]

because `0<=r<j<=aj`. Therefore

\[
\boxed{k\in\mathcal Q_N,\ d\mid k\quad\Longrightarrow\quad d\in\mathcal Q_N.}
\tag{12}
\]

The involution and floor-quotient order are known objects in the floor-quotient literature; the elementary proofs above are included so no external result is load-bearing here. The point needed for the Farey representation is the combination of self-duality with ordinary divisor closure.

## 2. Möbius inversion closes on the skeleton

`FD-001` and `FD-117` give, for every positive integer `k`,

\[
A_N(k)
=
\sum_{\substack{d\mid k\\d\le N}}
d\,M\!\left(\left\lfloor\frac Nd\right\rfloor\right).
\tag{13}
\]

If `k\in\mathcal Q_N`, then `k<=N`, so every divisor of `k` is at most `N`. Equation (13) reduces to (3). By (12), its entire divisor cone lies in `\mathcal Q_N`. Define

\[
b_N(k):=kM(\tau_N(k)),
\qquad k\in\mathcal Q_N.
\tag{14}
\]

Then on the divisor-closed set `\mathcal Q_N`,

\[
A_N(k)=\sum_{d\mid k}b_N(d).
\tag{15}
\]

Ordinary divisor Möbius inversion applies without introducing any frequency outside `\mathcal Q_N`:

\[
b_N(k)=\sum_{d\mid k}\mu(k/d)A_N(d).
\tag{16}
\]

Dividing by `k` proves (4). Since `\tau_N` is a permutation, all coordinates `(M(r))_{r\in\mathcal Q_N}` are recovered.

For an arbitrary frequency `\ell>=1`, equation (13) expresses `A_N(\ell)` using only values

\[
M\!\left(\left\lfloor\frac Nd\right\rfloor\right),
\qquad d\le N,
\tag{17}
\]

and each index `floor(N/d)` lies in `\mathcal Q_N`. Hence all nonskeleton Fourier modes are reconstructed after (4). Alternatively, `FD-117` reconstructs `D_N(x)` pointwise from the same recovered source vector, so the whole infinite Fourier tail is algebraically redundant.

Notice that `A_N(k)` is real despite its Fourier notation: equation (13) is a real divisor sum. Thus the skeleton contains exactly one real measurement per positive frequency, not two hidden real coordinates per complex coefficient.

## 3. Exact rank and linear minimality

Order `\mathcal Q_N` increasingly and let `m=(M(r))_{r\in\mathcal Q_N}`. Let `P_{\tau}` be the permutation matrix for `r\mapsto\tau_N(r)`, let

\[
\Delta=\operatorname{diag}(k)_{k\in\mathcal Q_N},
\tag{18}
\]

and let `Z_{\mathcal Q}` be the ordinary divisor-zeta matrix restricted to `\mathcal Q_N`,

\[
(Z_{\mathcal Q})_{k,d}=\mathbf 1_{d\mid k}.
\tag{19}
\]

Divisor closure makes `Z_{\mathcal Q}` unit lower triangular in this ordering. Equations (14)--(15) are exactly

\[
A=Z_{\mathcal Q}\,\Delta\,P_{\tau}m.
\tag{20}
\]

Therefore

\[
\det(Z_{\mathcal Q}\Delta P_{\tau})
=
\pm\prod_{k\in\mathcal Q_N}k,
\tag{21}
\]

which proves (5). The formal source space has dimension `|\mathcal Q_N|`, and the skeleton supplies exactly that many real linear measurements. Rank-nullity then gives the stated minimality among real-linear measurement families required to recover an **arbitrary formal source vector** in `\mathbb R^{\mathcal Q_N}`.

That qualifier is essential. The actual arithmetic vector `(M(r))_{r\in\mathcal Q_N}` is not an arbitrary point of `\mathbb R^{\mathcal Q_N}`. Equation (21) does not exclude nonlinear compression exploiting additional theorems about the Mertens trajectory, does not assert uniqueness of this skeleton, and does not turn formal rank into an information-theoretic lower bound for the actual arithmetic sequence.

## 4. Skeleton size

Put `s=floor(sqrt(N))`. The standard hyperbola decomposition is

\[
\mathcal Q_N
=
\{1,\ldots,s\}
\cup
\left\{
\left\lfloor\frac Nj\right\rfloor:1\le j\le s
\right\}.
\tag{22}
\]

Indeed `m>s` contributes only a value at most `s`, while `m<=s` contributes the second set. Its values are distinct; the two pieces are either disjoint or meet only at `s`. Consequently

\[
|\mathcal Q_N|\in\{2s-1,2s\}.
\tag{23}
\]

Thus the exact linear carrier dimension of the formal quotient source is `2\sqrt N+O(1)`, while the `N`-mode inverse used in `FD-117` was intentionally nonminimal.

## 5. Exact checks and adversarial boundary

As a finite regression check independent of the proof, exact integer arithmetic verified both `\tau_N^2=1` on `\mathcal Q_N` and divisor closure for every `2<=N<2000`. The matrix in (20) was also constructed directly for `N=2,3,4,5,10,17,100`; in each case its determinant had absolute value exactly `prod_(k in Q_N) k`.

The main adversarial failure modes are scope errors rather than algebraic ones. The claim does **not** say that more Fourier modes are analytically useless: redundant measurements can make positivity, averaging, norm inequalities or cancellation easier to prove. It does **not** improve the Franel energy constant or any Mertens exponent; `FD-003` and `FD-004` already warn that generic GCD/hyperbola geometry does not automatically buy such an improvement. It also does not claim novelty for floor-quotient self-duality or its order structure. Lagarias--Richman study that structure explicitly, and earlier Mertens matrix work uses the same hyperbola-scale state compression. No external theorem is needed for (9), (12), or the Farey--Fourier inversion above.

The durable conclusion is narrower and useful: after `FD-117`, **the full spectral bandwidth is not another escape hatch**. An explicit divisor-closed set of only `2\sqrt N+O(1)` positive frequencies already carries the full formal arithmetic source. Any future spectral progress must therefore come from a quantitatively coercive property of this skeleton (or another reversible representation of the same source), not from the mere availability of additional Fourier coordinates.

## Prior-art boundary

The floor-quotient set and its associated order are established objects; see Jeffrey C. Lagarias and David Harry Richman, *The floor quotient partial order*, Advances in Applied Mathematics 153 (2024), 102615. Jean-Paul Cardinal's earlier Mertens-matrix work also uses floor-quotient compression. `FD-118` makes no novelty claim for those ingredients. The line-specific result is their exact splice with the Farey Fourier identity of `FD-001`/`FD-117`, producing the square Fourier carrier (4)--(5) and the resulting representation kill test.
