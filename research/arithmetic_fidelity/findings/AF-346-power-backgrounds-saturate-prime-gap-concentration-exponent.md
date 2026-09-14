# AF-346 — cubic-and-higher power backgrounds saturate the prime-gap concentration exponent

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `ZERO-SENSITIVE-SOURCE`, `SOURCE-COMPLEXITY-CONSERVATION`, `SHARPNESS`, `NO-NOVELTY-CLAIM`

## Claim

AF-344 constructs, for every fixed integer `k>=2`, the prime-independent background

\[
b_k(n):=
\begin{cases}
 k m^{k-1},&n=m^k\text{ with }m>=2,\\
 0,&\text{otherwise},
\end{cases}
\tag{1}
\]

whose Dirichlet transform is

\[
B_k(s)=k\bigl(\zeta(ks-k+1)-1\bigr).
\tag{2}
\]

It has residue `1` at `s=1`, no poles at nontrivial zeta zeros, and therefore preserves the right-half-plane RH pole discriminator after subtraction from the prime layer. AF-345 then shows that for every nonnegative background below prime height, zero-deleted sign variation is exactly twice the number of consecutive-prime gaps carrying positive composite background mass, and that its gap-mass moments obey a sharp Holder lower bound.

For `k>=3`, the power-supported family realizes that lower-bound **exponent sharply**. The missing input is classical short-interval prime theory: Baker--Harman--Pintz imply that every sufficiently large interval between consecutive `k`-th powers contains a prime.

Fix an integer `k>=3`, a real `B>1`, and `q>1`. Let `M` tend to infinity and put

\[
L:=\lfloor B^{1/k}M\rfloor.
\tag{3}
\]

For sufficiently large `M`, choose primes

\[
p_-\in(M^k,(M+1)^k),
\qquad
p_+\in(L^k,(L+1)^k).
\tag{4}
\]

Consider the AF-344 residual

\[
h_k(n)=a(n)-b_k(n),
\qquad
a(p)=\log p,\quad a(n)=0\text{ on composites},
\tag{5}
\]

on the prime-endpoint block `[p_-,p_+]`. Then:

1. every support point `(M+1)^k,\ldots,L^k` lies in a **different** consecutive-prime gap;
2. these are exactly the occupied gaps in the block;
3. hence, with `V` denoting zero-deleted ordered sign variation,

\[
\boxed{V=2(L-M)}
\tag{6}
\]

and therefore

\[
\boxed{
V
=2\bigl(B^{1/k}-1\bigr)M+O(1)
=2\bigl(B^{1/k}-1\bigr)X^{1/k}+O(1),
}
\tag{7}
\]

where `X:=M^k`.

Let `\mu_j` be the AF-345 composite background mass in the occupied prime gaps, and define

\[
\mathcal M:=\sum_j\mu_j,
\qquad
S_q:=\sum_j\mu_j^q.
\tag{8}
\]

Because each occupied gap contains exactly one `k`-th power,

\[
\mu_j=k m^{k-1}
\tag{9}
\]

for a unique `m\in\{M+1,\ldots,L\}`. Consequently,

\[
\boxed{
\mathcal M
=(B-1)X+O_{k,B}\bigl(X^{1-1/k}\bigr),
}
\tag{10}
\]

while

\[
\boxed{
S_q
=C_{k,q,B}\,
X^{\,q-(q-1)/k}
+O_{k,q,B}\bigl(X^{q(1-1/k)}\bigr),
}
\tag{11}
\]

with

\[
C_{k,q,B}
:=
\frac{k^q}{q(k-1)+1}
\left(
B^{\frac{q(k-1)+1}{k}}-1
\right)>0.
\tag{12}
\]

Writing

\[
\theta:=\frac1k,
\qquad
\alpha_q:=q-\frac{q-1}{k},
\tag{13}
\]

the family therefore lies exactly on the AF-345 concentration line

\[
\boxed{
\alpha_q+(q-1)\theta=q.
}
\tag{14}
\]

Equivalently, if sign variation is of scale `X^theta`, then the gap-mass `q`-moment is of scale

\[
X^{q-(q-1)\theta},
\tag{15}
\]

which is precisely the exponent forced by

\[
V^{q-1}S_q\ge2^{q-1}\mathcal M^q
\tag{16}
\]

once `\mathcal M\asymp X`.

Thus AF-345's Holder tradeoff cannot be strengthened at the exponent level under only nonnegativity, sub-prime height, and order-`X` composite mass. The same simple backgrounds that preserve the RH pole discriminator and collapse sign density also realize the full prime-gap concentration bill predicted by that inequality.

## Derivation

### 1. Baker--Harman--Pintz separates consecutive `k`-th powers for `k>=3`

Baker, Harman, and Pintz proved that for all sufficiently large `x`, an interval of length `x^{0.525}` adjacent to `x` contains a prime. Apply their theorem with

\[
x=(m+1)^k.
\tag{17}
\]

The gap between consecutive `k`-th powers satisfies

\[
(m+1)^k-m^k
\sim k m^{k-1}.
\tag{18}
\]

For `k>=3`,

\[
k-1>0.525k
\tag{19}
\]

because `0.475k>1`. Hence

\[
(m+1)^k-(m+1)^{0.525k}>m^k
\tag{20}
\]

for all sufficiently large `m`. The BHP prime in the short interval below `(m+1)^k` therefore lies strictly between `m^k` and `(m+1)^k`; the upper endpoint itself is composite.

So every sufficiently large pair of consecutive `k`-th powers with `k>=3` is separated by at least one prime.

It follows immediately that no consecutive-prime gap can contain two support points of `b_k`. With the endpoint primes chosen in `(4)`, the only `k`-th powers between them are

\[
(M+1)^k,(M+2)^k,\ldots,L^k,
\tag{21}
\]

and each occupies a distinct prime gap. There are `L-M` such gaps.

AF-345 applies because `b_k>=0` and `b_k(p)=0<\log p` at every prime. Its exact occupancy identity therefore gives `(6)`.

### 2. The total gap mass remains pole-normalized at scale `X`

Since occupied gaps contain exactly one support point,

\[
\mathcal M
=\sum_{m=M+1}^{L}k m^{k-1}.
\tag{22}
\]

The classical power-sum estimate gives

\[
\sum_{m=M+1}^{L}m^{k-1}
=\frac{L^k-M^k}{k}+O_k(M^{k-1}),
\tag{23}
\]

because `L\asymp_{k,B}M`. From `L=B^{1/k}M+O(1)`,

\[
L^k=BM^k+O_{k,B}(M^{k-1}).
\tag{24}
\]

Substituting into `(22)` proves `(10)`.

This is the finite-window source-side form of the residue-one normalization already visible analytically in `(2)`: reducing sign density has not reduced the leading background mass.

### 3. Prime-gap aggregation becomes the ordinary power moment

Again using one support point per occupied gap,

\[
S_q
=\sum_{m=M+1}^{L}\bigl(km^{k-1}\bigr)^q
=k^q\sum_{m=M+1}^{L}m^{q(k-1)}.
\tag{25}
\]

For the real exponent

\[
\beta:=q(k-1)>-1,
\tag{26}
\]

the standard integral/power-sum asymptotic gives

\[
\sum_{m=M+1}^{L}m^\beta
=
\frac{L^{\beta+1}-M^{\beta+1}}{\beta+1}
+O_{k,q,B}(M^\beta).
\tag{27}
\]

Because

\[
\frac{\beta+1}{k}
= q-\frac{q-1}{k},
\tag{28}
\]

and `X=M^k`, equations `(25)`--`(28)` prove `(11)`--`(12)`.

Combining `(7)`, `(10)`, and `(11)` proves the exponent identity `(14)`.

### 4. The AF-345 Holder law is genuinely sharp, not merely necessary

AF-345 gives

\[
V^{q-1}S_q\ge2^{q-1}\mathcal M^q.
\tag{29}
\]

The present family has

\[
V\asymp X^{1/k},
\quad
\mathcal M\asymp X,
\quad
S_q\asymp X^{q-(q-1)/k},
\tag{30}
\]

so both sides of `(29)` have order `X^q`. Therefore no universal replacement of `(29)` can force a strictly larger power of `X` for `S_q` from the same hypotheses and the same sign scale.

The asymptotic Holder ratio can also be read explicitly. Put

\[
R_{k,q,B}
:=
\frac{V^{q-1}S_q}{2^{q-1}\mathcal M^q}.
\tag{31}
\]

Then

\[
R_{k,q,B}\longrightarrow
\frac{
(B^{1/k}-1)^{q-1}
\,C_{k,q,B}
}{(B-1)^q}
\ge1.
\tag{32}
\]

The inequality is exactly Holder. Moreover, as the fixed multiplicative window becomes thin,

\[
\lim_{B\downarrow1}
\frac{
(B^{1/k}-1)^{q-1}
\,C_{k,q,B}
}{(B-1)^q}
=1.
\tag{33}
\]

So the family can approach not only exponent equality but also the sharp Holder constant locally in multiplicative scale: on a thin window the power weights are nearly equal across the occupied gaps.

## Relation to AF-344 and AF-345

AF-344 deliberately asserted only

\[
V=O(X^{1/k}),
\tag{34}
\]

because a matching lower bound requires knowing that distinct perfect powers do not collapse into the same prime gap. AF-346 supplies exactly that missing arithmetic input for every `k>=3` using BHP. The sign scale is then no longer an upper-bound artifact:

\[
V\sim2(B^{1/k}-1)X^{1/k}.
\tag{35}
\]

AF-345 identifies prime-gap occupancy as the exact sign currency and proves that low occupancy forces mass concentration. AF-346 shows that this concentration inequality describes an actually realizable, prime-independent, analytically faithful family. The source-complexity tradeoff is therefore not created by an adversarial background that encodes prime gaps; the background rule remains simply “weighted perfect `k`-th powers.”

This closes one possible escape from the AF-345 obstruction. The Holder exponent cannot be improved merely by exploiting the arithmetic placement of the gaps: cubic-and-higher power supports already attain it while remaining zero-pole-blind and pole-normalized.

## Exact controls and boundaries

### The theorem begins at `k=3` for a genuine arithmetic reason

For `k=2`, consecutive-square spacing is of order `x^{1/2}`, below the BHP exponent `0.525`. The argument above therefore does not show that consecutive squares are separated by primes. That is the classical Legendre-conjecture boundary.

AF-344 still gives the unconditional square-background upper bound `V=O(X^{1/2})`, and AF-345 still gives the universal concentration lower bound. What is not established here is the exact square-gap occupancy asymptotic or the corresponding exact `S_q` asymptotic after aggregation by prime gaps.

### Prime-gap separation is used only to prove sharpness

The analytic fidelity of `b_k`, its residue-one normalization, its sparse support, and the AF-344 sign upper bound need no short-interval prime theorem. BHP enters only to show that for `k>=3` the support points land in distinct prime gaps, turning the AF-345 lower-bound exponent into an attained exponent.

### No new short-interval prime theorem is claimed

The existence of a prime between all sufficiently large consecutive cubes is a standard corollary of classical prime-gap bounds, and higher integer powers are easier at this exponent scale. Equation `(20)` is only that corollary written in the coordinates needed for Arithmetic Fidelity.

### The result does not make gap moments sufficient for the downstream Euler observation

AF-346 prices one source resource exactly. It does not prove a growing-order extension of AF-338 whose constants consume `S_q`, nor does it show that a bound on one `q`-moment is the right regularity hypothesis for transporting the RH pole discriminator toward the critical strip.

The conclusion is narrower: **if a future observation theorem uses only the AF-345 sign/mass tradeoff, its exponent cannot beat this family without an additional source restriction.**

### Large `k` still means a family of different fixed backgrounds

As in AF-344, each integer `k` defines a different background. The points

\[
\left(\theta,\alpha_q\right)
=\left(\frac1k,q-\frac{q-1}{k}\right)
\tag{36}
\]

approach `(0,q)` as `k` grows, but this does not produce one fixed background with bounded sign variation.

## Prior art and novelty assessment

No novelty claim is made for the constituent number theory or asymptotics.

- R. C. Baker, G. Harman, and J. Pintz, **“The Difference Between Consecutive Primes, II,”** *Proceedings of the London Mathematical Society* 83(3) (2001), 532--562, DOI `10.1112/plms/83.3.532`, prove the classical short-interval exponent `0.525`. Their result is the only non-elementary input in the support-separation step.
- The corollary that sufficiently large consecutive cubes contain a prime is standard and has also been studied in explicit form. The present argument needs only eventual separation, not an effective threshold.
- Power-sum asymptotics and Holder's inequality are classical. The analytic identity `(2)` and its RH-pole-fidelity consequence were already established in AF-344.

A targeted literature check around prime gaps, consecutive powers, and perfect-power support found the established short-interval/consecutive-power theory but no need for a new theorem there. The Arithmetic Fidelity content is the synthesis: the classical separation theorem turns AF-344 into an exponent-sharp realization of AF-345's source concentration law. It should be read as a sharpness result for the line's resource accounting, not as a new theorem about prime gaps or perfect powers.

## Consequence for Arithmetic Fidelity

The current source-side picture is now quantitatively tight for a broad explicit escape family.

For the cubic-and-higher power backgrounds, three facts coexist:

\[
\text{RH pole discriminator retained},
\qquad
V\asymp X^{1/k},
\qquad
S_q\asymp X^{q-(q-1)/k}.
\tag{37}
\]

The sign saving is paid exactly at the prime-gap concentration exponent forced by AF-345. Therefore simply strengthening “low sign variation” to “low sign variation plus the corresponding unavoidable gap-mass moment” does not yet exclude these prime-independent recodings.

The next useful source certificate must either impose a strictly stronger normalized concentration/locality resource than `(29)`, or derive a growing-order observation theorem whose quantitative constants explicitly consume the concentration profile rather than treating sign count as the whole source complexity.