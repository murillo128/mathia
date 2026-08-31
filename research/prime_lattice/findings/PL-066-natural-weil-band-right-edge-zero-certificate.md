# PL-066 — Natural Weil-band noncollapse gives a band-dependent rightmost-zero certificate

## Claim

The fixed-depth moving-band escape left after `PL-063`--`PL-065` is more rigid than the one-way Vinogradov--Korobov collapse estimate suggests. Before inserting any zero-free region, the `PL-063` proof already gives an **inverse zero-location certificate**: an order-one defect of the naturally `exp(-L)`-normalized completed Weil form forces a nontrivial zeta zero whose real part is quantitatively determined by the growth rate of the boundary band.

Fix `R>0`. Let `Pi_N` be the two-copy projection onto the first `N` Dirichlet sine modes of `L^2(0,R)`, and let `W_(L,R)` be the naturally `exp(-L)`-normalized completed Weil boundary form used in `PL-059`--`PL-065`. Put

```text
X=exp(2L).
```

For `T>=max(e^e,2N)`, define

```text
M(T)=max_{rho: |Im rho|<=T} X^(Re rho-1),
```

where the maximum is over nontrivial zeta zeros. The zero-sampling argument inside `PL-063`, *before* the Vinogradov--Korobov zero-free estimate is substituted, gives

```text
boxed:
||Pi_N W_(L,R) Pi_N||
 <= C_R [
      M(T) log(2+T)
      + N^2 log(2+T)/T
      + exp(-L)(1+log(1+N))
    ].
```

Consequently, fix `epsilon>0` and suppose `L_j->infinity`, `N_j->infinity`,

```text
log N_j = o(exp(L_j)),
```

and

```text
||Pi_(N_j) W_(L_j,R) Pi_(N_j)|| >= epsilon
```

for infinitely many `j`. Then for all sufficiently large such `j` there exists a nontrivial zero

```text
rho_j=beta_j+i gamma_j,
|gamma_j| <= N_j^3,
```

such that

```text
boxed:
1-beta_j
 <= [log(C_(R,epsilon) log(2+N_j))]/(2L_j).
```

This gives a useful scale dictionary. If

```text
log log N_j / L_j -> alpha,
0 <= alpha < 1,
```

then any order-one defect forces

```text
boxed:
liminf beta_j >= 1-alpha/2.
```

In particular, for every regime with `log log N=o(L)` it forces zeros with `beta->1`. As the band approaches the much larger scale `log N=exp((1-o(1))L)`, the certificate weakens continuously toward the critical-line threshold `beta>=1/2`; it should not be described as a near-`1` theorem in that extreme regime.

There is an immediate conditional corollary. Under RH,

```text
boxed:
log N(L)=o(exp(L)), N(L)->infinity
    =>
||Pi_(N(L)) W_(L,R) Pi_(N(L))|| -> 0.
```

So, assuming RH, the natural boundary normalization has no nontrivial fixed-depth Dirichlet-band limit anywhere below the scale at which the normalized archimedean logarithmic cost itself can become order one. This is a **negative topology statement**, not an RH proof mechanism.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION`, and `DECISIVE-NEGATIVE` for the route

```text
natural exp(-L) completed Weil boundary normalization
+ fixed boundary depth
+ moving Dirichlet band with log N=o(exp L)
    -> nontrivial RH-compatible order-one limit
    -> critical-line rigidity.
```

The theorem does not rule out amplitude renormalization, a different moving topology, frequencies at or beyond the archimedean scale, or a construction whose observable is not controlled by the `PL-063` Paley--Wiener zero-sampling estimate.

## The pre-zero-free estimate already contains the inverse statement

`PL-063` writes the centered cross-end prime block through the completed explicit formula as

```text
<g,D_(L,R)f>
 = - sum_rho
       X^(rho-1)
       A_f(rho-1/2)
       conjugate(A_g(conjugate(rho)-1/2))
   + O_R(X^(-3)) ||f|| ||g||,
```

with compact boundary Laplace transform

```text
A_f(z)=integral_0^R f(a) exp(-z a) da.
```

For every `f in L^2(0,R)` and `T>=3`, the same finding proves the sampling bound

```text
sum_(rho: |Im rho|<=T)
 |A_f(rho-1/2)|^2
 <= C_R log(2+T) ||f||_2^2.
```

Therefore the contribution from zeros with `|Im rho|<=T` has operator norm at most

```text
C_R M(T) log(2+T).
```

On the first `N` Dirichlet modes, one integration by parts gives the high-zero tail

```text
C_R N^2 log(2+T)/T.
```

`PL-059` and `PL-061` control the remaining pole, same-end, scalar, and archimedean completion terms by

```text
C_R exp(-L)(1+log(1+N)).
```

Combining those three ingredients yields the displayed pre-zero-free bound for the **full completed compression**. The Vinogradov--Korobov region used in `PL-063` is only one possible upper bound for `M(T)`; it is not needed for the inverse argument.

## An order-one defect forces a band-dependent rightmost zero

Take

```text
T=N^3.
```

Then

```text
N^2 log T/T = O(log N/N).
```

Along a sequence satisfying

```text
N->infinity,
log N=o(exp L),
```

both the high-zero tail and the full completion remainder tend to zero:

```text
log N/N ->0,
exp(-L)(1+log N) ->0.
```

Hence, if the compressed completed norm is at least a fixed `epsilon>0`, then for all sufficiently large indices

```text
M(N^3)
 >= c_(R,epsilon)/log(2+N).
```

By definition of `M`, some zero `rho=beta+i gamma`, `|gamma|<=N^3`, satisfies

```text
exp(-2L(1-beta))
 >= c_(R,epsilon)/log(2+N).
```

Taking logarithms gives

```text
2L(1-beta)
 <= log(C_(R,epsilon) log(2+N)),
```

which is exactly the claimed certificate.

The useful parameter is therefore

```text
alpha_L = log log N / L.
```

Ignoring the lower-order `log C` term, noncollapse requires a zero with

```text
beta >= 1-alpha_L/2.
```

This makes the information geometry explicit:

```text
log log N=o(L)
    -> a surviving defect forces beta->1;

log log N ~ alpha L, 0<alpha<1
    -> it forces beta >= 1-alpha/2-o(1);

alpha ->1
    -> the forced threshold approaches beta>=1/2.
```

Thus the fixed-depth natural-scale band does not single out `1/2` internally. The critical value appears only when the band itself is pushed to the separate scale where `log N` is almost `exp(L)`.

## Under RH the natural band collapses almost to the archimedean scale

If RH holds, every nontrivial zero satisfies `Re rho=1/2`, so

```text
M(T)=X^(-1/2)=exp(-L)
```

for every `T` above the first zero. With `T=N^3`, the general bound becomes

```text
||Pi_N W_(L,R) Pi_N||
 <= C_R [
      exp(-L) log(2+N)
      + log(2+N)/N
      + exp(-L)(1+log(1+N))
    ].
```

Therefore every moving band with

```text
N(L)->infinity,
log N(L)=o(exp L)
```

collapses in norm under RH.

The scale `log N ~ exp(L)` is not being claimed as an intrinsic arithmetic transition. It is exactly where the already-audited normalized archimedean logarithmic multiplier `exp(-L) log N` can become order one. The result only says that **below that unrelated archimedean scale, critical-line zeros themselves are too strongly suppressed by the natural boundary normalization to sustain an order-one band defect**.

## Prime-lattice interpretation

The zero-sensitive cross-end shell is supported on prime-power exponent vectors `k e_p`. Its moving boundary phases are

```text
exp(-i xi log n)
 = exp(-i xi <v(n),(log p)_p>).
```

`PL-052` and `PL-065` show that these finite prime-log phases can recur coherently, but only at very late frequencies. The present inverse estimate says something complementary: if a controlled Dirichlet band carries an order-one completed defect, then its required zero location is determined quantitatively by how fast that band grows. Generic Kronecker recurrence alone does not supply this band-to-zero-real-part law; it enters through the completed explicit formula.

The fixed-depth topology therefore has the information flow

```text
prime-log band defect
    -> compact-boundary explicit formula
    -> large factor X^(beta-1)
    -> rightmost-zero certificate set by log log N / L.
```

This is genuine arithmetic information, but it does not independently select the self-dual line.

## Prior-art and novelty audit

The logical philosophy is classical rather than new. Turan's localization method links uniform bounds for prime-supported Dirichlet polynomials to zero-free regions of `zeta`; Michel J. G. Weber, “Local Suprema of Dirichlet Polynomials and Zerofree Regions of the Riemann Zeta-Function,” *Glasgow Mathematical Journal* **56**(3) (2014), 643--655, DOI `10.1017/S001708951400007X`, gives a modern explicit formulation of this prime-polynomial/zero-free connection and cites Turan's original localization criteria. In Weber's formulation, local bounds for sums with prime frequencies imply a semi-global zero-free region.

The exact inequality above is not taken from that literature. It is the line-specific contrapositive extracted from the already-persisted completed-Weil Paley--Wiener estimate of `PL-063`. No novelty is claimed for the general principle that anomalously large prime observables can certify nearby zeros.

The Vinogradov--Korobov and PNT anchors already recorded in `SOURCES.md` entries 59--60 explain the unconditional scale obtained by inserting a known zero-free envelope. Broucke's generalized-prime result in entry 61 remains the matched-control warning: zero-free contours and corresponding PNT-error scales can be reproduced in Beurling systems. Hence a boundary transition governed only by a rightmost-zero envelope is not rational-prime-specific RH rigidity.

A targeted literature search across Turan localization, prime Dirichlet-polynomial suprema, localized Weil operators, and Paley--Wiener sampling did not locate this exact fixed-depth operator-norm certificate. Search absence is not evidence of originality.

## Analytic-continuation audit

No Euler product is used outside `Re(s)>1`.

For fixed `L`, the prime shell is finite. The zero expansion is the already-continued completed Weil/von-Mangoldt explicit formula used and audited in `PL-063`. The sampling estimate is compact-support Paley--Wiener analysis, the high-zero bound is elementary integration by parts plus local zero counting, and the completion estimate comes from the pole and archimedean terms already isolated in `PL-059` and `PL-061`.

The inverse step is only the contrapositive of that established operator upper bound. It introduces no new continuation argument.

## Beurling and matched-control audit

The deduction

```text
large band defect
    -> a zero crossing a band-dependent rightmost threshold
```

is structural for any generalized-prime explicit formula with the same compact-boundary sampling and zero-count estimates. The threshold then depends on the generalized zeta zero-free geometry. This is exactly why the certificate is a negative guide for RH: its native scale is controlled by the location of the rightmost available zeros, not by an intrinsic prime-lattice mechanism selecting `1/2`.

To become specifically useful for the ordinary RH problem, a successor construction would need an additional rational-prime invariant that changes this information geometry rather than merely sharpening a right-edge zero-free estimate.

## Falsification and boundary tests

The result reduces to the following checkable steps:

1. the pre-Vinogradov--Korobov `PL-063` low-zero estimate is `C_R M(T) log(2+T)`;
2. the finite-band high-zero tail is `O_R(N^2 log(2+T)/T)`;
3. the remaining full completion terms are `O_R(exp(-L)(1+log(1+N)))`;
4. choosing `T=N^3` makes the tail `O(log N/N)`;
5. `log N=o(exp L)` makes the normalized archimedean/completion term vanish;
6. an order-one norm lower bound therefore forces `M(N^3)>=c/log N`;
7. `X=exp(2L)` converts that inequality into the displayed bound on `1-Re rho`;
8. the extra condition `log log N=o(L)`, not merely `log N=o(exp L)`, is what makes the forced zeros approach `Re(s)=1`;
9. under RH, `M(T)=exp(-L)`, yielding full band collapse whenever `log N=o(exp L)`.

Failure of any of the first three inherited estimates invalidates the certificate. The theorem does not address cutoffs whose basis has different high-zero approximation cost, unrestricted norm states, growing boundary depth, or the second amplitude scale obtained by multiplying the centered residual by `exp(L)`.

## Consequence for the research line

The accepted `CLUE-mesoscopic-weil-boundary-topology` should no longer treat the unresolved fixed-depth Dirichlet-band transition at the **natural** `exp(-L)` normalization as a plausible way to obtain an RH-compatible nonzero limit. Under RH the entire sub-archimedean band regime collapses; conversely, any order-one survival there certifies a zero to the right of a band-dependent threshold, approaching `Re(s)=1` whenever `log log N=o(L)`.

The surviving mesoscopic question therefore has to change one of the ingredients: use a further amplitude normalization that keeps square-root-scale zero terms visible, use a topology not controlled by compact-boundary zero sampling, couple to a genuinely global rational-prime invariant, or move to a regime where the archimedean and prime pieces interact nontrivially. Any `exp(L)` second normalization must in turn pass the prior-art test that it is not merely the classical explicit-formula zero series rewritten as a boundary operator.