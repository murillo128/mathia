# FD-191 — Critical square-root dyadic Fourier bands remain null under squarefree prime fidelity

- **Date:** 2026-09-18
- **Status:** proved
- **Evidence:** EXACT-DERIVED / NEGATIVE-OBSTRUCTION
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** endpoint identifiability / dyadic quotient geometry / arithmetic-admissible nullspace
- **Depends on:** FD-117, FD-189, FD-190

## Claim

`FD-190` proves that every strict sub-square-root signed dyadic Farey band remains noninjective even after fixing all primes, all nonsquarefree coefficients and all Möbius signs, but its density argument loses all margin at the endpoint `alpha=1/2`. The endpoint is nevertheless still noninjective in the same coordinatewise Möbius-faithful class.

Let

\[
\mathcal Q_{1/2}
:=
\left\{
\left\lfloor\frac{2^m}{k}\right\rfloor:
 m\ge0,
 1\le k\le 2^{m/2}
\right\}
\tag{1}
\]

be the cumulative-source coordinates exposed by the complete critical signed band. Then for every sufficiently large dyadic scale `X=2^r` there are

\[
\gg \sqrt X
\tag{2}
\]

integers `n` in the terminal window

\[
X-\frac{\sqrt X}{4}\le n<X
\tag{3}
\]

such that

1. `n` is not in `Q_(1/2)`;
2. both `n` and `n+1` are composite squarefree integers.

Consequently the endpoint band operator has, in every sufficiently large terminal dyadic window, an `Omega(sqrt(X))`-dimensional exact kernel supported only on composite squarefree source coordinates while fixing every prime and every nonsquarefree coefficient. In particular, after any prescribed finite prefix and for every `0<epsilon<1`, one can choose such an `n` and define

\[
a_\varepsilon(t)
=
\begin{cases}
\mu(n)+\varepsilon,&t=n,\\
\mu(n+1)-\varepsilon,&t=n+1,\\
\mu(t),&\text{otherwise}.
\end{cases}
\tag{4}
\]

Then

\[
\boxed{
\mathcal F_{2^m}^{a_\varepsilon}(k)
=
\mathcal F_{2^m}^{\mu}(k)
\quad
\text{for every }m\ge0,
\quad 1\le k\le 2^{m/2},
}
\tag{5}
\]

although `a_epsilon != mu`. The perturbation preserves exact prime values, exact zero values on nonsquarefrees, the Möbius sign on every squarefree coordinate, bounded amplitudes, and an arbitrary fixed prefix.

Combined with the unrestricted tail-injectivity of `FD-189` for every `alpha>1/2`, this closes the power-law threshold for this coordinatewise Möbius-faithful squarefree class as well: the critical band is still on the noninjective side, while every fixed super-square-root band is tail-injective even without arithmetic restrictions.

This remains an identifiability theorem, not a stability estimate and not a Franel--Landau/RH bound.

## 1. A deterministic terminal family of endpoint holes

The key new fact is an exact near-power-of-two hole criterion.

Let

\[
X=2^r,
\qquad d\ge1\text{ odd},
\qquad d^2+d<X,
\qquad n=X-d.
\tag{6}
\]

Then

\[
\boxed{n\notin\mathcal Q_{1/2}.}
\tag{7}
\]

To prove this, suppose that for some dyadic horizon `H=2^m` and integer `k<=sqrt(H)` we had

\[
\left\lfloor\frac Hk\right\rfloor=n.
\tag{8}
\]

If `m<r`, then `H<=X/2<n`, so (8) is impossible. If `m>=2r`, then `sqrt(H)>=X`; since `k<=sqrt(H)`,

\[
\frac Hk\ge\sqrt H\ge X>n,
\tag{9}
\]

so (8) is again impossible.

It remains to treat

\[
r\le m<2r.
\tag{10}
\]

Write

\[
m=r+j,
\qquad 0\le j<r,
\qquad s=r-j\ge1.
\tag{11}
\]

Since `H=2^j X`, equation (8) is equivalent to

\[
\frac H{n+1}<k\le\frac Hn.
\tag{12}
\]

Put `k=2^j+t`. Substituting `n=X-d` gives

\[
\frac{(d-1)2^j}{X-d+1}
<t
\le
\frac{d2^j}{X-d}.
\tag{13}
\]

Let

\[
q=2^s,
\qquad
A=\left\lfloor\frac{d-1}{q}\right\rfloor.
\tag{14}
\]

Because `2^j/X=1/q`, the left endpoint in (13) is at least `(d-1)/q>=A`. On the other hand

\[
\frac{d2^j}{X-d}
=
\frac dq+\frac{d^2}{q(X-d)}.
\tag{15}
\]

The hypothesis `d^2+d<X` gives `d^2<X-d`, hence the second term in (15) is strictly smaller than `1/q`. Since `d` is odd and `q=2^s>=2`, `q` does not divide `d`, and the distance from `d/q` to the next integer is at least `1/q`. Therefore

\[
\frac{d2^j}{X-d}
<
\left\lceil\frac dq\right\rceil
=
\left\lfloor\frac{d-1}{q}\right\rfloor+1
=A+1.
\tag{16}
\]

Thus any integer `t` satisfying (13) would obey

\[
A<t<A+1,
\tag{17}
\]

which is impossible. This proves (7) for every horizon simultaneously.

The Mersenne holes of `FD-189` are the special case `d=1`. The useful endpoint improvement is that the same obstruction actually fills a whole square-root-sized family of odd offsets below each sufficiently large power of two.

## 2. A positive fraction of those holes have two composite squarefree source coordinates

The deterministic hole family alone does not yet preserve the coordinatewise Möbius constraints: a null spike at cumulative coordinate `n` requires changing the two source increments at `n` and `n+1`. We therefore need both to be squarefree composites.

Set

\[
L=\left\lfloor\frac{\sqrt X}{4}\right\rfloor.
\tag{18}
\]

For all sufficiently large `X`, every `1<=d<=L` satisfies `d^2+d<X`. Restrict `d` further to one residue class modulo

\[
M=4\cdot9\cdot25=900
\tag{19}
\]

chosen by the Chinese remainder theorem so that

\[
d\equiv3\pmod4,
\qquad
d\equiv X-3\pmod9,
\qquad
d\equiv X-4\pmod{25}.
\tag{20}
\]

For `n=X-d`, these congruences force

\[
n\equiv1\pmod4,
\qquad n\equiv3\pmod9,
\qquad n\equiv4\pmod{25},
\tag{21}
\]

and

\[
n+1\equiv2\pmod4,
\qquad n+1\equiv4\pmod9,
\qquad n+1\equiv5\pmod{25}.
\tag{22}
\]

Hence neither `n` nor `n+1` has a square factor from `2,3,5`; moreover `3|n` and `5|(n+1)`, so both are composite once `X` is large.

There are

\[
T=\frac L{900}+O(1)\asymp\sqrt X
\tag{23}
\]

candidate offsets in (20). Parameterize them as `d=d_0+900t`. For any prime `p>=7`, the condition `p^2|n` removes at most one residue class of `t mod p^2`, and `p^2|(n+1)` removes at most one more. Thus the number of candidates spoiled by some prime square `p^2`, `p>=7`, is at most

\[
2T\sum_{p\ge7}\frac1{p^2}
+
2\pi(\sqrt{X+1}).
\tag{24}
\]

A deliberately crude bound is already enough:

\[
\sum_{p\ge7}\frac1{p^2}
\le
\sum_{m=7}^\infty\frac1{m^2}
\le
\frac1{49}+\int_7^\infty\frac{dt}{t^2}
=
\frac8{49}.
\tag{25}
\]

The prime number theorem gives

\[
\pi(\sqrt{X+1})=o(\sqrt X)=o(T).
\tag{26}
\]

Combining (24)--(26), at most

\[
\left(\frac{16}{49}+o(1)\right)T
\tag{27}
\]

candidates are spoiled. Therefore at least

\[
\left(\frac{33}{49}+o(1)\right)T
=\Omega(\sqrt X)
\tag{28}
\]

survive, and for every survivor both `n` and `n+1` are composite squarefree. By Section 1 every corresponding `n` is an exact endpoint hole.

No short-interval squarefree theorem is needed. The argument is only CRT plus a square-divisor union bound; PNT is used for the harmless `+1` cost accumulated over possible prime squares and is already a durable source anchor for this research line.

## 3. The critical band has a large arithmetic-admissible kernel

For each surviving offset `d`, let

\[
n_d=X-d
\tag{29}
\]

and define the increment perturbation

\[
h_d(t)
=
\begin{cases}
1,&t=n_d,\\
-1,&t=n_d+1,\\
0,&\text{otherwise}.
\end{cases}
\tag{30}
\]

Its cumulative perturbation is exactly

\[
H_d(u)=\sum_{t\le u}h_d(t)
=
\mathbf 1_{\{u=n_d\}}.
\tag{31}
\]

Section 1 gives `n_d notin Q_(1/2)`, so

\[
H_d\!\left(\left\lfloor\frac{2^m}{k}\right\rfloor\right)=0
\tag{32}
\]

for every dyadic horizon and every `k<=2^(m/2)`.

By the exact divisor-transform identity of `FD-117/FD-189`,

\[
\mathcal F_H^a(k)
=
\sum_{e\mid k}e\,A(\lfloor H/e\rfloor).
\tag{33}
\]

Every divisor `e|k` also satisfies `e<=sqrt(H)`, so every cumulative coordinate occurring in (33) belongs to `Q_(1/2)`. Equation (32) therefore makes `h_d` an exact null direction for the complete critical signed-band history.

Distinct admissible offsets in the fixed residue class (20) differ by at least `900`, so the supports `{n_d,n_d+1}` are disjoint. The corresponding `h_d` are linearly independent. Equation (28) therefore yields an

\[
\boxed{\Omega(\sqrt X)}
\tag{34}
\]

dimensional endpoint kernel supported wholly on composite squarefree coordinates inside the terminal window (3). Every sufficiently small vector in this subspace preserves the Möbius sign at every affected coordinate while fixing all primes and all nonsquarefree coefficients.

Taking one basis direction and multiplying it by `0<epsilon<1` gives (4)--(5). Since `X` can be arbitrarily large, the collision can be placed beyond any prescribed finite prefix. Its coefficient discrepancy is again finite and minimal in cardinality:

\[
D_{a_\varepsilon,q}(x)=2\varepsilon^q
\tag{35}
\]

once `x>=n+1`.

## Representation audit

No stronger source observable has been inserted. `FD-189` proves that the retained signed Fourier band is exactly equivalent, by divisor Möbius inversion, to the quotient samples `A(floor(H/k))` with the same cutoff. The set `Q_(1/2)` is therefore precisely the cumulative-coordinate coverage of the stated Farey observation family.

The new arithmetic restrictions are imposed only on the original increment source. The proof exploits the geometry of the unsampled quotient coordinates and then asks whether their two adjacent increments can both remain inside the squarefree composite fibre. The CRT/square-sieve step answers yes on `Omega(sqrt(X))` independent coordinates near every sufficiently large dyadic endpoint. Nothing in the argument assumes multiplicativity; that omitted cross-coordinate law remains exactly the distinction exposed by `FD-172--FD-190`.

## Prior-art and novelty boundary

The fixed-horizon floor-quotient set `{floor(X/k)}` and its cardinality are classical; Randell Heyman's 2019 work remains the nearest fixed-horizon boundary already recorded by `FD-189`. Classical work of Mirsky and successors establishes positive-density laws for fixed tuples of squarefree integers, including consecutive squarefree patterns. Those results are neighboring arithmetic prior art, but they are not needed here: the moving terminal window below `2^r` is handled directly by the elementary residue-class square sieve in Section 2.

A targeted search for dyadic multihorizon quotient coverage at the square-root cutoff, near-power-of-two hole criteria of the form (6)--(7), and squarefree/prime-faithful Farey-band nullspaces did not surface a theorem matching this endpoint statement. No global novelty claim is made. The exact new contribution claimed here is the Mathia-specific composition of the deterministic dyadic hole family with an arithmetic-admissible squarefree source kernel.

No new external theorem is load-bearing beyond PNT, already anchored in `SOURCES.md`, so `SOURCES.md` is unchanged.

## Boundary conditions and failure modes

The conclusion is specific to **signed coefficient data** through the initial critical band `k<=sqrt(H)` on the dyadic horizon schedule. It does not automatically transfer to arbitrary nonuniform frequency selections, to scalar Fourier energies, or to a different horizon family.

The construction is deliberately nonmultiplicative. It proves that squarefree support, correct prime values, correct Möbius signs, bounded amplitudes, finite coefficient error and even a large exact prefix do not repair endpoint injectivity. It does not contradict the multiplicative rigidity of `FD-172--FD-174`, where changing a composite independently of its prime factors is forbidden.

Finally, exact noninjectivity does not by itself give a lower bound for stable recovery under noise, nor does super-square-root injectivity give an RH-critical discrepancy estimate. The Franel--Landau destination still requires analytic cancellation, not merely source identifiability.

## Research consequence

`FD-190` left one precise loophole: perhaps coordinatewise Möbius fidelity improves the unrestricted threshold exactly at `alpha=1/2`, even though it cannot improve any strict sub-square-root power. The present result closes that loophole decisively.

The square-root power transition from `FD-189` is therefore stable under a very strong coordinatewise physicalization of the source. At the endpoint there is not merely one exceptional collision but an `Omega(sqrt(X))` family of independent composite-squarefree null directions near every sufficiently large dyadic scale. Any observation-side improvement below or at the square-root cutoff must therefore exploit **relations between source coordinates**—multiplicativity, divisor compatibility, prime-extension consistency—or alter the Farey observation family rather than impose more coordinatewise fidelity.

The next observation-side question should accordingly move away from endpoint coverage and toward relation-sensitive sampling: identify the thinnest Farey statistic that exposes the prime-extension/divisor-cube inconsistency without reconstructing the whole source.