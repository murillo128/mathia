# MC-152 — Canonical divisibility-split row norms remain blind to iterated Möbius parity

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue in the canonical number-state representation of `MC-149`–`MC-151`,

\[
\mathcal H=\ell^2(\mathbb N),
\qquad
S_p\varepsilon_k=\varepsilon_{pk},
\qquad
D_a\varepsilon_k=a_k\varepsilon_k,
\]

where `p` is prime and `a=(a_k)` is bounded. `MC-151` closed every **scalar** prime weight followed only by external `\ell^r` row boundedness, leaving genuinely state-dependent structure as the next obvious escape.

The most immediate source-forced state dependence is already present in the semigroup isometry itself. Put

\[
P_p:=S_pS_p^*,
\]

so in this representation

\[
P_p\varepsilon_k=\mathbf 1_{p\mid k}\varepsilon_k.
\tag{1}
\]

Split the raw commutator according to whether the input state is divisible by `p`:

\[
C_p^{(0)}(a):=[D_a,S_p](I-P_p),
\qquad
C_p^{(1)}(a):=[D_a,S_p]P_p.
\tag{2}
\]

For `1\le r\le\infty` and an arbitrary scalar prime weight `w=(w_p)_p`, form the two rows

\[
\mathcal R^{(j)}_{w,r}(a)\xi
:=\bigl(w_pC_p^{(j)}(a)\xi\bigr)_p
\in\ell^r(\mathbb P;\mathcal H),
\qquad j\in\{0,1\}.
\tag{3}
\]

For Möbius these rows have the exact norms

\[
\boxed{
\|\mathcal R^{(0)}_{w,r}(\mu)\|=2\|w\|_{\ell^r},
\qquad
\|\mathcal R^{(1)}_{w,r}(\mu)\|=\|w\|_{\ell^r}.
}
\tag{4}
\]

The split initially looks more selective than `MC-151`: for the support control `\mu^2` the corresponding pair is `(0,\|w\|_r)`, while for Liouville it is `(2\|w\|_r,2\|w\|_r)`.

But this apparent Möbius selectivity is killed by a stronger matched control. Define

\[
b(n):=\mu(n)^2-2\mathbf 1_{\mathbb P}(n),
\tag{5}
\]

that is,

\[
b(1)=1,
\qquad
b(p)=-1\text{ for primes }p,
\qquad
b(n)=1\text{ for squarefree composite }n,
\qquad
b(n)=0\text{ otherwise}.
\tag{6}
\]

Then `|b|=\mu^2`, and `b` agrees with `\mu` at `1` and at every prime, but it flattens all higher squarefree parity to `+1`. Nevertheless **every scalar-weighted divisibility-split row norm is exactly the same as for Möbius**:

\[
\boxed{
\|\mathcal R^{(0)}_{w,r}(b)\|
=2\|w\|_{\ell^r},
\qquad
\|\mathcal R^{(1)}_{w,r}(b)\|
=\|w\|_{\ell^r}
}
\tag{7}
\]

for every `1\le r\le\infty`, again with the extended-value convention when `w\notin\ell^r`.

Yet `b` has no Mertens-scale cancellation. If

\[
B(x):=\sum_{n\le x}b(n),
\qquad
Q(x):=\sum_{n\le x}\mu(n)^2,
\]

then exactly

\[
B(x)=Q(x)-2\pi(x),
\tag{8}
\]

and the classical squarefree-counting asymptotic together with the prime number theorem gives

\[
\boxed{
B(x)=\frac{6}{\pi^2}x+o(x).
}
\tag{9}
\]

Thus the first canonical state-dependent repair of the scalar-row obstruction still does not connect to global cancellation. The pair of divisibility-sector **operator norms** retains squarefree support and enough one-prime behavior to separate `\mu^2` and `\lambda`, but it forgets where the extremal transitions occur and therefore loses the iterated parity coherence across distinct prime factors that distinguishes Möbius from `(5)`.

Consequently a surviving transverse Bost--Connes route cannot consist only of source-forced divisibility splitting followed by separate row norms. It must retain a relational observable across input states, prime dilations, or successive prime additions that the norm supremum does not erase, and must still prove a cheaper transfer to anchored Mertens excursion.

## 1. The range projection is exactly the input-divisibility selector

Since `S_p` maps the basis isometrically onto

\[
\operatorname{span}\{\varepsilon_{pk}:k\ge1\},
\]

its range projection satisfies `(1)`. From the raw commutator formula of `MC-149`,

\[
[D_a,S_p]\varepsilon_k=(a_{pk}-a_k)\varepsilon_{pk},
\tag{10}
\]

we therefore obtain

\[
C_p^{(0)}(a)\varepsilon_k
=
\begin{cases}
(a_{pk}-a_k)\varepsilon_{pk},&p\nmid k,\\
0,&p\mid k,
\end{cases}
\tag{11}
\]

and

\[
C_p^{(1)}(a)\varepsilon_k
=
\begin{cases}
0,&p\nmid k,\\
(a_{pk}-a_k)\varepsilon_{pk},&p\mid k.
\end{cases}
\tag{12}
\]

For each fixed `p`, the output basis vectors remain orthogonal as `k` varies, so each sector norm is the supremum of the corresponding restricted finite differences.

This split is not an externally chosen arithmetic mask: `P_p=S_pS_p^*` is forced by the canonical semigroup isometry. It is therefore the simplest state-dependent construction not covered literally by the scalar-weight theorem `MC-151`.

## 2. Möbius has exact sector amplitudes two and one

If `p\nmid k` and `k` is squarefree, multiplicativity gives

\[
\mu(pk)=-\mu(k),
\]

hence

\[
|\mu(pk)-\mu(k)|=2.
\tag{13}
\]

If `k` is not squarefree, both values vanish. Therefore

\[
\|C_p^{(0)}(\mu)\|=2.
\tag{14}
\]

If instead `p\mid k` and `k` is squarefree, then `pk` contains `p^2`, so

\[
\mu(pk)=0,
\qquad
|\mu(pk)-\mu(k)|=1.
\tag{15}
\]

For nonsquarefree `k`, again both values vanish. Hence

\[
\|C_p^{(1)}(\mu)\|=1.
\tag{16}
\]

The row upper bounds in `(4)` follow immediately from `(14)`–`(16)`.

They are sharp simultaneously across the prime coordinate. For the nondivisible sector, the anchored state `\varepsilon_1` gives

\[
C_p^{(0)}(\mu)\varepsilon_1=-2\varepsilon_p
\qquad\text{for every prime }p,
\tag{17}
\]

so the first row has norm at least `2\|w\|_r`.

For the divisible sector, let `F` be any finite set of primes and put

\[
k_F=\prod_{p\in F}p.
\]

Then `k_F` is squarefree and for every `p\in F`,

\[
\|C_p^{(1)}(\mu)\varepsilon_{k_F}\|=1,
\]

while the projection kills primes outside `F`. Taking the supremum over finite `F` recovers `\|w\|_r`; the `r=\infty` endpoint follows by a one-prime choice. This proves `(4)`.

## 3. The obvious controls are separated, but that is not enough

For `q_0=\mu^2`, if `p\nmid k`, multiplication by `p` preserves squarefreeness versus nonsquarefreeness, so

\[
C_p^{(0)}(q_0)=0.
\tag{18}
\]

On a squarefree `k` divisible by `p`, multiplication by `p` destroys squarefreeness, giving a unit difference. The same finite-prime-product argument as above yields

\[
\|\mathcal R^{(0)}_{w,r}(q_0)\|=0,
\qquad
\|\mathcal R^{(1)}_{w,r}(q_0)\|=\|w\|_r.
\tag{19}
\]

For Liouville, complete multiplicativity gives

\[
\lambda(pk)-\lambda(k)=-2\lambda(k)
\]

for every `p,k`. Restricting to either input sector therefore gives amplitude `2`, and finite products again allow simultaneous activation of any finite divisible prime set. Thus

\[
\|\mathcal R^{(0)}_{w,r}(\lambda)\|
=
\|\mathcal R^{(1)}_{w,r}(\lambda)\|
=2\|w\|_r.
\tag{20}
\]

So unlike the unsplit scalar rows of `MC-151`, the pair of sector norms distinguishes Möbius from both standard controls. That makes the split a legitimate refinement rather than a tautological repetition of the previous theorem.

The next matched control shows exactly what the refinement still misses.

## 4. A parity-flattened squarefree control has the identical split norm profile

Consider `b` from `(5)`–`(6)`. For `p\nmid k`, four cases exhaust the possibilities.

- If `k=1`, then `b(p)-b(1)=-2`.
- If `k=q` is a prime different from `p`, then `pq` is squarefree composite and `b(pq)-b(q)=1-(-1)=2`.
- If `k` is squarefree composite, then `pk` is squarefree composite and the difference is `0`.
- If `k` is nonsquarefree, so is `pk`, and the difference is `0`.

Hence

\[
\|C_p^{(0)}(b)\|=2,
\tag{21}
\]

and, more importantly, the single state `\varepsilon_1` again activates amplitude `2` for every prime at once. Therefore

\[
\|\mathcal R^{(0)}_{w,r}(b)\|=2\|w\|_r.
\tag{22}
\]

For the divisible sector, if `p\mid k` and `k=p`, then

\[
b(p^2)-b(p)=0-(-1)=1.
\tag{23}
\]

If `k` is squarefree composite and divisible by `p`, then `b(k)=1` while `pk` is nonsquarefree, so

\[
b(pk)-b(k)=-1.
\tag{24}
\]

For nonsquarefree `k`, both values vanish. Thus `\|C_p^{(1)}(b)\|=1`. Given any finite prime set `F`, the squarefree product `k_F` used above has unit divisible-sector difference for every `p\in F` (with the singleton case supplied by `(23)`). Consequently

\[
\|\mathcal R^{(1)}_{w,r}(b)\|=\|w\|_r.
\tag{25}
\]

Equations `(22)` and `(25)` prove `(7)`.

The control is deliberately stronger than `\mu^2` or `\lambda`: it has exactly the same squarefree support as Möbius and exactly the same value `-1` at every prime. What it removes is the parity accumulation across three or more distinct prime factors. The split norm sees extremal one-step transitions but not the location and consistency of those transitions along multiplicative paths.

## 5. The matched control has linear summatory bias

Because `b` differs from `\mu^2` only by changing every prime value from `+1` to `-1`, equation `(8)` is exact. The squarefree-counting estimate already anchored in `MC-S12` gives

\[
Q(x)=\frac{6}{\pi^2}x+O(\sqrt x)
\]

at more than enough precision here, while the classical prime number theorem (within the standard prime-distribution background anchored in `MC-S15`) gives `\pi(x)=o(x)`. Therefore `(9)` follows.

So equality of all split-row norm pairs does not merely coexist with a slightly worse cancellation exponent. It coexists with an order-`x` mean. Any implication from these norms alone to even qualitative `o(x)` cancellation is false.

This is a stronger falsification than comparing only the critical exponent of a weighted row: the source-forced state-dependent projection has recovered some local arithmetic selectivity, but the norm scalarization still admits a support- and prime-value-matched sequence with maximal-scale bias.

## 6. Prior-art and novelty assessment

The Bost--Connes semigroup/crossed-product framework and its canonical isometries are established prior art; `MC-149`–`MC-151` already audit the representation and nearby operator-algebra/spectral-triple literature. A targeted literature check for the canonical range projections/divisibility split, semigroup commutators, and Möbius did not locate an established theorem with the exact matched-control norm classification `(4)`–`(9)`. No novelty inference is drawn from that absence.

The operator-theoretic ingredients are elementary. `P_p=S_pS_p^*` is simply the range projection of an isometry, and `(11)`–`(12)` are basis calculations. The classical semigroup-crossed-product viewpoint for the Bost--Connes algebra goes back at least to Laca and Raeburn, *A Semigroup Crossed Product Arising in Number Theory*, Journal of the London Mathematical Society **59** (1999), 330–344, DOI `10.1112/S0024610798006620`. The arithmetic asymptotic in `(9)` uses only the already anchored classical squarefree and prime-counting estimates.

Accordingly this finding is stored as an exact **line-specific obstruction**, not as a novelty claim about range projections, semigroup crossed products, or squarefree counting.

## Boundaries and falsification tests

- **Norm scalarization is essential to the no-go.** The actual operators `C_p^{(j)}(\mu)` and `C_p^{(j)}(b)` are not equal. An observable retaining matrix coefficients, mixed products, correlations between several prime dilations, or the distribution of extremal input states may distinguish them.
- **The control is not multiplicative.** This is deliberate: the theorem falsifies claims based only on the represented divisibility split and its row norms. A mechanism that uses exact multiplicativity in an additional nontrivial way is outside the claim. Conversely, imposing squarefree support, the value `-1` on every prime, and full multiplicativity already determines Möbius on squarefree integers, so such an input must still demonstrate that it has reduced rather than merely restated the hard cancellation problem.
- **Scalar prime weights remain arbitrary.** The theorem covers every `w` and every external `\ell^r` exponent, but only after the state dependence is the canonical binary split `P_p/(I-P_p)`. More refined joint `(p,k)` weights or source-forced non-scalar kernels require separate analysis.
- **No statement about twisted commutators.** A cocycle, alternative Dirac operator, different representation, or genuinely crossed-product phase observable is not reduced to `(2)`.
- **The matched control is exact, not numerical.** Equality of the row norms follows from explicit basis states and finite prime products, while its linear mean follows from classical asymptotics. Larger computations cannot repair this norm-level implication.
- **No RH input is used.** There is no analytic continuation, contour shift, zero-free region, or Mertens estimate in the derivation.

## Consequence for the line

`MC-151` showed that scalar weighting plus Banach aggregation is entirely externally controlled. The canonical input-divisibility projections provide the first natural state-dependent refinement and genuinely separate the two standard controls `\mu^2` and `\lambda`.

That gain is still insufficient. The parity-flattened control `(5)` has the same squarefree support and prime values as Möbius, reproduces **all** of the split-row operator norms for arbitrary scalar weights and `\ell^r` aggregation, yet has a linear summatory main term. The missing datum is not another scalar decay exponent; it is the consistency of sign changes along successive additions of distinct prime factors.

Further Bost--Connes work should therefore move past separate norms of one-prime divisibility sectors. A plausible intermediate transverse category must retain cross-prime/path coherence or another relational statistic that rules out `(5)` without simply encoding the full Möbius recursion, and it must then connect that retained relation quantitatively to anchored Mertens excursion.