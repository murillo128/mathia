# PL-065 — Zero-free sampling forces late prime-log recurrence in the Weil boundary shell

## Claim

`PL-052` proves that the fixed-depth Weil boundary shell has arbitrarily late high-frequency states that coherently recover its atomic prime-power mass, while `PL-063` proves that every sufficiently low Dirichlet-frequency band collapses after the completed pole/prime centering. These two facts can be coupled quantitatively.

Fix `R>0`. Retain the centered cross-end boundary block

```text
D_(L,R)=H_(mu_(L,R))-P_R
```

from `PL-052`--`PL-063`, where

```text
mu_(L,R)
 = exp(-L)
   sum_(2L-2R<log n<2L)
      Lambda(n)/sqrt(n)
      delta_(2L-log n),
```

and

```text
d mu_R(delta)=exp(-delta/2) 1_[0,2R](delta) d delta,
P_R=H_(mu_R).
```

Put

```text
N_R=1-exp(-R),

tau_R(delta)=delta          for 0<=delta<=R,
             2R-delta       for R<=delta<=2R,

w_R(delta)=exp(-delta/2) tau_R(delta)/N_R.
```

For the `PL-052` modulated boundary profiles

```text
f_xi(a)=N_R^(-1/2) exp((-1/2+i xi)a),
g_xi(a)=N_R^(-1/2) exp((-1/2-i xi)a),
```

define the weighted atomic recurrence amplitude

```text
A_(L,R)(xi)
 = integral exp(i xi delta) w_R(delta) d mu_(L,R)(delta),

M_(L,R)
 = integral w_R(delta) d mu_(L,R)(delta).
```

The fixed-width PNT shell law gives

```text
M_(L,R) -> N_R.
```

There are constants `xi_R>0`, `c_R>0`, and `L_R` such that, for every `L>=L_R`, every `|xi|>=xi_R` satisfying the concrete coherence condition

```text
|A_(L,R)(xi)| >= (3/4) M_(L,R)
```

must obey

```text
boxed:
log(2+|xi|)
 [log log(exp(exp(1))+|xi|)]^2
 >= c_R L^(3/2).
```

Consequently, after changing `c_R`,

```text
boxed:
|xi|
 >= exp(c_R L^(3/2)/(log L)^2)
```

for all sufficiently large `L`.

Kronecker recurrence from `PL-052` guarantees arbitrarily large `xi` satisfying the coherence condition for each fixed `L`. The present theorem therefore does not remove recurrence; it proves an unconditional **lower bound on how early the `PL-052` coherent return can occur**. In particular, the recurrent norm-defect witnesses cannot live at polynomial, ordinary exponential, or any stretched-exponential boundary frequency `exp(L^alpha)` with `alpha<3/2`.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION`, and `DECISIVE-NEGATIVE` for the route

```text
PL-052 prime-log coherent recurrence
+ a boundary frequency below the zero-free sampling barrier
    -> order-one centered Weil defect
    -> mesoscopic RH-sensitive spectral limit.
```

The exponent `3/2` and logarithmic loss come from the same Vinogradov--Korobov zero-free sampling estimate as `PL-063`. They are sufficient barriers, not claimed sharp recurrence exponents and not intrinsic selectors of the Riemann critical line.

## The recurrence observable is exactly the `PL-052` matrix element

For a shell atom at deficit `delta`, `PL-052` computes

```text
<g_xi,H_delta f_xi>
 = exp(i xi delta)
   exp(-delta/2) tau_R(delta)/N_R.
```

Therefore

```text
<g_xi,H_(mu_(L,R)) f_xi>
 = A_(L,R)(xi).
```

For the continuum PNT model,

```text
<g_xi,P_R f_xi>
 = N_R^(-1)
   [ integral_0^R exp(-a) exp(i xi a) da ]^2,
```

so

```text
|<g_xi,P_R f_xi>| <= C_R (1+|xi|)^(-2).
```

Also, by weak convergence of the positive shell measure against the fixed continuous weight `w_R`,

```text
M_(L,R)
 -> integral_0^(2R)
      exp(-delta) tau_R(delta)/N_R d delta
 = N_R.
```

Choose `xi_R` so that the continuum matrix element has modulus at most `N_R/8` for `|xi|>=xi_R`. For all sufficiently large `L`, `M_(L,R)>=3N_R/4`. Hence the coherence condition implies

```text
boxed:
|<g_xi,D_(L,R) f_xi>| >= c_R >0.
```

This is the only place where a recurrence threshold is imposed. It is deliberately stated as a weighted shell coherence condition rather than requiring every active prime-power phase to lie in a prescribed arc. The exact Kronecker returns of `PL-052` are stronger and therefore satisfy it arbitrarily far out.

## Quantitative sine-band approximation of the recurrent profiles

The missing bridge noted explicitly in `PL-063` is that the `PL-052` witnesses are complex exponentials on `(0,R)`, whereas `PL-063` controls the first `N` Dirichlet sine modes. For these particular witnesses the bridge is elementary and quantitative.

Let

```text
kappa_k=k pi/R,
e_k(a)=sqrt(2/R) sin(kappa_k a),
lambda=-1/2+i xi.
```

Up to the fixed normalization factor `sqrt(2/R)/sqrt(N_R)`, the sine coefficient of `f_xi` is exactly

```text
integral_0^R exp(lambda a) sin(kappa_k a) da

 = kappa_k
   [1-(-1)^k exp(lambda R)]
   /(kappa_k^2+lambda^2).
```

If

```text
kappa_k >= 2 |lambda|,
```

then

```text
|kappa_k^2+lambda^2|
 >= kappa_k^2-|lambda|^2
 >= (3/4) kappa_k^2,
```

and therefore

```text
|<f_xi,e_k>| <= C_R/k.
```

The same estimate holds for `g_xi`. If `P_N` is the first-`N` sine projection and

```text
N >= K_R(1+|xi|)
```

for a fixed sufficiently large `K_R`, summing the coefficient tail gives

```text
boxed:
||(I-P_N)f_xi||_2
 + ||(I-P_N)g_xi||_2
 <= C_R N^(-1/2).
```

This estimate is exact elementary Fourier analysis; it does not use zeta or any unproved Diophantine information.

## Uniform boundedness lets the compression see the recurrence

For fixed `R`, the centered boundary blocks are uniformly bounded in `L`. Indeed, each atomic truncated-reflection block has norm at most its positive weight, and on the shell `n` is comparable to `exp(2L)`. Chebyshev's bound for `psi(x)` therefore gives

```text
sup_L ||H_(mu_(L,R))|| < infinity,
```

while `P_R` is fixed rank one. Thus

```text
sup_L ||D_(L,R)|| <= C_R.
```

Using the previous projection estimate,

```text
| <g_xi,D_(L,R)f_xi>
  -<P_N g_xi,D_(L,R)P_N f_xi> |
 <= C_R N^(-1/2).
```

Take

```text
N=ceil(K_R(1+|xi|)).
```

For a coherent return and sufficiently large `L`, the left matrix element is bounded below by the fixed positive constant from the first section. Hence

```text
c_R
 <= ||P_N D_(L,R) P_N|| + C_R N^(-1/2).
```

A coherent `PL-052` recurrence therefore forces a nontrivial finite-band compression at a band index linearly comparable to its modulation frequency.

## Insert the `PL-063` zero-free sampling estimate

The pre-archimedean estimate proved inside `PL-063` applies directly to this centered cross block. For every `T>=max(exp(exp(1)),2N)`,

```text
||P_N D_(L,R) P_N||

 <= C_R [
      log(2+T)
      exp( - c L /
            ((log T)^(2/3)(log log T)^(1/3)) )

      + N^2 log(2+T)/T
      + exp(-6L)
    ].
```

Choose `T=N^3` and write

```text
u=log N.
```

Since `N` is linearly comparable to `1+|xi|`, `u=log(2+|xi|)+O_R(1)`. The compression and projection bounds give

```text
c_R
 <= C_R [
      u exp(-c_R L/(u^(2/3)(log u)^(1/3)))
      + u exp(-u)
      + exp(-u/2)
      + exp(-6L)
    ].
```

For large `L`, the last three terms are negligible at any coherent return beyond the fixed `xi_R`. Therefore the first term must remain bounded below. Taking logarithms yields

```text
c_R L
 <= u^(2/3) (log u)^(4/3)
```

and hence

```text
boxed:
u (log u)^2 >= c_R L^(3/2).
```

Replacing `u` by `log(2+|xi|)` gives the first displayed recurrence lower bound.

For the simpler corollary, if `u>=L^(3/2)` there is nothing to prove. Otherwise `log u=O(log L)`, so

```text
u >= c_R L^(3/2)/(log L)^2.
```

Exponentiating and absorbing the fixed comparison between `N` and `1+|xi|` proves

```text
|xi| >= exp(c_R L^(3/2)/(log L)^2).
```

## Exact prime-lattice meaning

Every shell atom has

```text
delta_n=2L-log n,
```

and therefore

```text
exp(i xi delta_n)
 = exp(i 2L xi)
   exp(-i xi log n)

 = exp(i 2L xi)
   exp(-i xi <v(n),(log p)_p>).
```

Because the von Mangoldt weight is supported on prime powers, the active exponent vectors here are axis rays `k e_p`. A Kronecker return simultaneously aligns the primitive coordinate phases `exp(-i xi log p)`, and hence all active powers. The theorem says that the completed explicit-formula geometry prevents that finite prime-coordinate flow from producing a strongly coherent boundary return until a frequency at least of the displayed zero-free scale.

This is more precise than the bare statement that `{log p}` are rationally independent. Rational independence guarantees recurrence but contains no useful first-return scale. Here the **distribution of the ordinary primes through the completed zeta explicit formula and its zero-free region supplies a quantitative delay**.

## Why this does not contradict Kronecker recurrence

`PL-045` and `PL-052` use Kronecker/Weyl only as an existence theorem: for every fixed finite prime set and every target neighborhood of the torus identity, arbitrarily late returns occur. That theorem gives no assertion that a return occurs before a particular height.

`PL-065` is a lower-bound theorem. It says that one concrete order-one recurrence observable attached to the growing Weil shell cannot return too early as `L` grows. Both statements are compatible:

```text
finite prime-log orbit
    -> return exists arbitrarily late                 (Kronecker)

completed zeta shell + zero-free sampling
    -> no strong weighted return below a large scale (this finding).
```

The result also does not give a matching upper bound. Generic effective Kronecker theorems and linear-forms-in-logarithms methods provide quantitative tools for finite-frequency systems, but the active dimension here itself grows roughly like the number of primes below `exp(2L)`. A targeted novelty audit did not locate an existing theorem matching this particular completed-Weil weighted-shell lower bound. Search absence is not treated as novelty evidence.

## Beurling and matched-control audit

The recurrence-existence half is generic: any finite rationally independent family of primitive energies has the same Kronecker returns. The quantitative exclusion half uses exactly the arithmetic inputs inherited from `PL-063`:

```text
completed explicit-formula zero expansion
+ a zero-free envelope near Re(s)=1
+ local zero counting
+ compact-boundary Paley--Wiener sampling.
```

Accordingly, a generalized-prime system with analogous completed explicit formula, zero-free region, and local zero-count bounds would inherit an analogous recurrence-delay theorem. The scale is therefore **not by itself rational-prime RH rigidity**. It is useful because it couples the generic prime-torus recurrence mechanism to non-generic analytic information, but matched Beurling controls remain mandatory before interpreting any sharper transition as zeta-specific.

## Analytic-continuation audit

No Euler product is continued outside `Re(s)>1`.

For fixed `L` the shell is a finite von-Mangoldt sum. The recurrence step is finite-dimensional Kronecker theory. The quantitative exclusion uses the `PL-063` compressed estimate, which was derived from the already-continued completed von-Mangoldt/Weil explicit formula, the unconditional Vinogradov--Korobov zero-free region, and unconditional local zero counts. The sine-projection lemma and the passage from compression to the modulated witnesses are elementary Hilbert-space estimates.

Thus the only critical-strip input enters through an established global explicit formula, not through formal continuation of the prime Euler product.

## Prior-art and novelty audit

The ingredients are individually classical or already canonical in this line:

- `PL-045` and `PL-052` supply the exact prime-log Kronecker recurrence mechanism and the boundary witnesses;
- `PL-063`, anchored by the Weil explicit formula and the Bellotti/Johnston Vinogradov--Korobov zero-free/PNT literature recorded in `SOURCES.md`, supplies the finite-band exclusion estimate;
- Dirichlet sine projection of a truncated exponential is elementary Fourier analysis;
- quantitative Kronecker--Weyl theory and linear forms in logarithms are established subjects, so no novelty is claimed for seeking effective recurrence bounds in general.

The durable content is the exact **bridge between two already-persisted regimes**: the modulated norm witnesses from `PL-052` can be approximated in the Dirichlet basis at linear frequency cost, so the zero-sampled band collapse of `PL-063` becomes an explicit lower bound on their coherent return time. A targeted search around effective Kronecker--Weyl recurrence, logarithms of primes, and von-Mangoldt exponential sums did not locate this exact fixed-depth completed-Weil recurrence-delay statement. That search result does not establish originality.

## Falsification and boundary tests

The claim reduces to independently checkable steps:

1. the `PL-052` matrix-element formula for the modulated profiles is correct;
2. `M_(L,R)->N_R` under the fixed-width PNT shell law;
3. the continuum rank-one matrix element is `O_R(|xi|^-2)`;
4. the exact sine coefficient has the displayed rational form;
5. its tail gives `||(I-P_N)f_xi||+||(I-P_N)g_xi||=O_R(N^-1/2)` once `N>=K_R(1+|xi|)`;
6. `D_(L,R)` is uniformly bounded for fixed `R`;
7. the centered-prime compression estimate quoted from `PL-063` holds uniformly for the projected vectors;
8. the elementary logarithmic rearrangement of that estimate gives `u(log u)^2>=c_R L^(3/2)`.

Failure of any item invalidates the corresponding recurrence lower bound. The theorem does not rule out weaker partial coherence, different moving profiles whose Dirichlet approximation cost is much larger or smaller, a different boundary topology, or a recurrence observable that does not force an order-one matrix element of `D_(L,R)`.

## Consequence for the research line

The topology ledger now contains a direct bridge between the unrestricted recurrence obstruction and the moving-band no-go:

```text
fixed profiles
    -> completed boundary cancellation;

Dirichlet bands below zero-free sampling scale
    -> completed norm collapse;

PL-052 coherent prime-log return
    -> necessarily lies beyond
       exp(c_R L^(3/2)/(log L)^2) boundary frequency;

unrestricted frequency
    -> coherent returns still exist arbitrarily late.
```

Thus `CLUE-mesoscopic-weil-boundary-topology` is narrowed again. A candidate that tries merely to capture the known `PL-052` recurrence by letting the boundary cutoff grow more slowly than the displayed scale cannot work. The unresolved region begins only at genuinely enormous frequencies, or in a topology whose states evade the linear-cost Dirichlet approximation used here. Survival beyond this barrier would still not imply RH rigidity; a successful mechanism must additionally distinguish the ordinary rational-prime system from matched generalized-prime controls and produce a stable invariant rather than only a late recurrence.