# AF-345 — prime-gap occupancy is the exact sign currency for nonnegative backgrounds

**Status:** `EXACT-DERIVED`, `ARITHMETIC-FIDELITY`, `ZERO-SENSITIVE-SOURCE`, `SOURCE-COMPLEXITY-CONSERVATION`, `CLASSICAL-INEQUALITY`, `NO-NOVELTY-CLAIM`

## Claim

AF-342 shows that a variable background can reduce the ordered sign variation of the prime-layer residual only by creating prime-scale exceptional behavior, AF-343 rules out fixed syndetic positive-composite support, and AF-344 exhibits the opposite extreme: a sparse perfect-power background can preserve the right-half-plane RH pole discriminator while making the residual sign variation sub-prime-scale by concentrating the background mass onto rare, high-amplitude sites.

For the entire nonnegative, sub-prime-height class there is an exact source-side classification of what the zero-deleted sign statistic actually sees.

Let

\[
a(n):=
\begin{cases}
\log p,&n=p\text{ prime},\\
0,&n\text{ composite},
\end{cases}
\qquad
h_b(n):=a(n)-b(n),
\tag{1}
\]

where `b(n)>=0`. Fix consecutive primes

\[
p_r<p_{r+1}<\cdots<p_s
\tag{2}
\]

and assume

\[
b(p_j)<\log p_j
\qquad(r\le j\le s).
\tag{3}
\]

For each consecutive-prime gap define its **composite background mass**

\[
m_j(b):=\sum_{p_j<n<p_{j+1}} b(n),
\qquad r\le j<s,
\tag{4}
\]

and let

\[
J_b(r,s):=\#\{j\in\{r,\ldots,s-1\}:m_j(b)>0\}.
\tag{5}
\]

Using the AF-216 convention that zero coefficients are deleted before ordered sign changes are counted, one has the exact identity

\[
\boxed{
V\bigl(h_b(p_r),h_b(p_r+1),\ldots,h_b(p_s)\bigr)
=2J_b(r,s).
}
\tag{6}
\]

Thus ordered sign variation does **not** measure the number of nonzero background sites, their description complexity, or their amplitudes. In this class it measures exactly one quotient statistic: **how many consecutive-prime gaps contain any positive composite background mass**.

This immediately yields a sharp concentration law. Put

\[
M:=\sum_{j=r}^{s-1}m_j,
\qquad
S_q:=\sum_{j=r}^{s-1}m_j^q,
\qquad q>1.
\tag{7}
\]

Then Holder's inequality on the occupied gaps gives

\[
M^q\le J_b^{\,q-1}S_q,
\tag{8}
\]

and therefore, by `(6)`,

\[
\boxed{
V^{q-1}S_q\ge 2^{q-1}M^q.
}
\tag{9}
\]

Equivalently, the `q`-effective number of gaps carrying the composite background mass,

\[
N_{\mathrm{eff},q}
:=\left(\frac{M^q}{S_q}\right)^{1/(q-1)},
\tag{10}
\]

satisfies

\[
\boxed{
N_{\mathrm{eff},q}\le J_b=\frac V2.
}
\tag{11}
\]

For `q=2` this becomes the particularly transparent participation-ratio law

\[
\boxed{
V\sum_j m_j^2\ge2M^2,
\qquad
\frac{M^2}{\sum_jm_j^2}\le\frac V2.
}
\tag{12}
\]

Equality in `(8)`--`(12)` holds exactly when all occupied prime gaps carry the same mass. Hence the inequality is not merely qualitative: for fixed total composite background mass and fixed sign budget, it gives the least possible gap-mass concentration.

There is also an exact bridge to the amplitude/support-gap currencies exposed by AF-344. Write

\[
d_j:=p_{j+1}-p_j,
\qquad
A:=\max_{\substack{p_r<n<p_s\\ n\ \mathrm{composite}}}b(n),
\tag{13}
\]

with `A=0` when there is no composite background mass. Since every integer strictly between consecutive primes is composite,

\[
m_j\le A(d_j-1).
\tag{14}
\]

Combining `(9)` with `(14)` yields, for every `q>1`,

\[
\boxed{
A^qV^{q-1}
\sum_{j=r}^{s-1}(d_j-1)^q
\ge
2^{q-1}M^q.
}
\tag{15}
\]

In particular,

\[
\boxed{
A^2V\sum_j(d_j-1)^2\ge2M^2.
}
\tag{16}
\]

If `G:=\max_j(d_j-1)`, then the still simpler estimate

\[
M\le J_bAG=\frac V2AG
\]

gives

\[
\boxed{AVG\ge2M.}
\tag{17}
\]

So a nonnegative background carrying substantial composite mass cannot simultaneously have small ordered sign variation, small amplitude, and mild prime-gap geometry. The sparse-background escape of AF-344 is therefore an instance of a general conservation law rather than an isolated construction: lowering the sign currency forces the retained composite mass into fewer prime gaps, and any pointwise realization of that concentration must pay through amplitude, available gap width, or both.

## Derivation

### 1. Consecutive-prime gaps are the exact sign blocks

Condition `(3)` gives

\[
h_b(p_j)=\log p_j-b(p_j)>0
\tag{18}
\]

at every prime in the block. If `p_j<n<p_{j+1}`, then `n` is composite, so

\[
h_b(n)=-b(n)\le0,
\tag{19}
\]

with strict negativity exactly when `b(n)>0`.

After zero coefficients are deleted, consider the portion of the sign sequence between the two consecutive positive prime entries at `p_j` and `p_{j+1}`.

If `m_j=0`, nonnegativity of `b` forces `b(n)=0` at every interior integer, so the two prime entries become adjacent signs `+,+` and contribute no sign change.

If `m_j>0`, at least one interior composite has `b(n)>0`; every nonzero interior residual is negative. After deleting interior zeros, the block has sign pattern

\[
+,-,\ldots,-,+,
\tag{20}
\]

and contributes exactly two sign changes.

The intervals `(p_j,p_{j+1})` are disjoint and exhaust the region between the endpoint primes. There are no other possible nonzero sign types. Summing the independent contributions proves `(6)`.

For an arbitrary integer window containing at least two primes, restricting to its first and last internal primes gives the same exact interior identity; the two exterior fragments can add at most one transition each. Thus the prime-endpoint formulation loses at most an `O(1)` boundary term in multiplicative-window asymptotics.

### 2. Gap-mass concentration is forced by a small sign budget

Only the `J_b` occupied gaps contribute to `M`. Holder's inequality gives

\[
\left(\sum_{m_j>0}m_j\right)^q
\le
J_b^{q-1}\sum_{m_j>0}m_j^q.
\tag{21}
\]

The left side is `M^q`, the final sum is `S_q`, and `(6)` gives `J_b=V/2`. This proves `(9)`--`(11)`.

For `q=2`, `(21)` is Cauchy--Schwarz and gives `(12)`. Equality in Holder occurs precisely when the positive `m_j` are equal, proving the sharpness statement.

The result can also be read in reverse. If the total mass `M` must remain of a fixed order while `V` is reduced, the effective number of mass-carrying prime gaps must fall at least proportionally. The sign saving is therefore exactly a **prime-gap mass-concentration operation**.

### 3. Pointwise amplitude and prime-gap width realize the concentration

There are exactly `d_j-1` integers in `(p_j,p_{j+1})`, all composite. Hence `(14)` follows immediately from the definition of `A`. Raising to the `q`-th power and summing gives

\[
S_q\le A^q\sum_j(d_j-1)^q.
\tag{22}
\]

Substitution into `(9)` proves `(15)` and its quadratic case `(16)`.

Alternatively, each occupied gap has mass at most `AG`, so

\[
M\le J_bAG=\frac V2AG,
\tag{23}
\]

which proves `(17)`.

These bounds deliberately separate three resources that sign count alone conflates: the number of occupied prime gaps, the mass placed in each occupied gap, and the geometric capacity of the gap to hold that mass at bounded amplitude.

## Relation to AF-342--AF-344

AF-342 uses prime sites and their immediate composite neighbors to prove that a low-sign residual needs a prime-scale exceptional set unless the baseline changes the local sign geometry. AF-345 identifies the exact quotient of that local geometry after zero deletion: immediate neighbors are not intrinsically special. What matters is whether **some** negative witness survives anywhere between each pair of consecutive positive prime landmarks.

AF-343's syndetic theorem is therefore a sufficient mechanism for forcing many occupied gaps. A syndetic positive-composite support cannot leave long sequences of consecutive prime gaps empty, so the exact occupancy identity immediately explains why its sign order remains prime-scale. The periodic case is one structured realization of the same principle.

AF-344 sits on the opposite side of the classification. For the perfect-`k`-power background, a prime gap is occupied only if it contains at least one perfect `k`-th power. Equation `(6)` sharpens the previous counting interpretation to

\[
V=2\times\#\{\text{prime gaps containing a perfect }k\text{-th power}\}
\tag{24}
\]

on prime-endpoint blocks. The upper bound `V=O(P^{1/k})` follows because there are only `O(P^{1/k})` such powers in a fixed multiplicative window. The large weights in AF-344 are then exactly the mechanism by which order-one total background mass can be transported through a much smaller set of occupied gaps.

The conceptual frontier is therefore sharper than “add an amplitude penalty.” A useful source certificate for the AF-338 observation route must prevent or price **prime-gap mass concentration**. Pointwise amplitude, local mass, support-gap geometry, and moment norms are candidate realizations of that same missing resource; `(9)`--`(17)` state the exact relations they must obey before any analytic observation theorem is applied.

## Exact controls and boundaries

### Nonnegativity is load-bearing

If `b` may be negative at composites, then `h_b=-b` can be positive there. Composite positive sites can merge prime-positive runs or create additional positive structure, and `m_j>0` no longer characterizes the existence of a negative witness. A signed-background theory needs separate positive and negative gap masses or a different state variable.

### Sub-prime height at the prime landmarks is load-bearing

Condition `(3)` keeps every prime residual strictly positive. If `b(p)>=log p`, a prime can vanish or become negative and the consecutive-prime landmarks themselves are altered. That is precisely the prime-site escape already isolated by `E_b` in AF-342; it is not hidden inside `(6)`.

### Composite gap mass is not total baseline mass

The quantity `M` excludes baseline mass placed at prime sites. Consequently, a pole-normalized analytic background does not automatically give `M\asymp P`; one must separately control how much source mass is carried on primes. The present theorem is finite-window and exact and makes no Tauberian assumption.

### Prime-gap occupancy is an audit coordinate, not a cheap retained mark

The partition into consecutive rational-prime gaps already uses the arithmetic source being audited. Equation `(6)` does not propose storing `J_b` or the vector `(m_j)` as an independent compression. It identifies the exact hidden resource consumed by the existing zero-deleted sign statistic so that a proposed source recoding can be tested against it.

### Small sign variation need not force large pointwise amplitude by itself

Equation `(17)` contains both `A` and `G`. A background may exploit unusually long gaps, uneven mass, or both. The stronger moment law `(9)` is the representation-independent statement at the prime-gap level; amplitude-only conclusions require additional information on gap geometry.

### No growing-order observation theorem is obtained

AF-345 is a source-side conservation law. It does not upgrade AF-338 from fixed-order sign regularity to a theorem whose admissible order grows with source complexity, and it does not prove that the gap-mass moments themselves are the right quantity for such an observation theorem. It identifies a precise resource that any such theorem can now try to consume or bypass.

## Prior art and novelty assessment

No novelty claim is made for the constituent mathematics.

- The partition of the integers by consecutive-prime gaps is elementary and standard.
- The exact sign identity `(6)` is a direct consequence of deleting zeros from a sequence that is positive at every prime landmark and nonpositive between landmarks.
- Inequalities `(8)`--`(12)` are Holder/Cauchy--Schwarz applied to the occupied-gap mass vector, and `(14)`--`(17)` are elementary support-size/amplitude estimates.
- Classical prime-gap literature studies the sizes and moments of `p_{j+1}-p_j`; those results can be inserted into `(15)` when a particular quantitative regime needs them, but no such external estimate is required for the present theorem.

A targeted literature search around sign changes indexed by consecutive-prime gaps and occupancy/moment bounds did not identify a standard theorem organized in this exact form. Search failure is not evidence of novelty, and the result is therefore classified as an exact Arithmetic Fidelity synthesis of elementary ingredients rather than as a new prime-gap theorem.

## Consequence for Arithmetic Fidelity

AF-344 showed that a fidelity-preserving recoding can move complexity out of ordered sign count and into sparse high-amplitude structure. AF-345 identifies the conservation law behind that phenomenon.

For nonnegative backgrounds that do not neutralize the primes themselves, the sign statistic has a complete factorization:

\[
\text{background}
\longmapsto
\{m_j>0\}_{\text{prime gaps}}
\longmapsto
V=2J_b.
\tag{25}
\]

Everything else about the background is invisible to this particular compression. When substantial composite mass survives, `(9)` then forces any reduction in `V` to reappear as concentration of the prime-gap mass profile. This turns the previous qualitative frontier — amplitude, support gaps, or local concentration — into one precise object: **the distribution of retained background mass across consecutive-prime gaps**.

The next viable source-to-observation bridge can therefore be tested sharply: either its downstream mechanism controls a norm or concentration functional of this gap-mass profile, or it must explain why that conserved source resource is irrelevant to the zero discriminator it claims to preserve.