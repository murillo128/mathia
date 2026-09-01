# PL-098 — Critical S1 rank floor has a classical prolate Nyquist threshold

## Claim

The finite-rank obstruction behind `PL-097` already becomes nontrivial at a **finite** observation-time ratio, and its onset is exactly the classical time-bandwidth/Nyquist threshold of the continuum comparator. Therefore a positive trace-class defect in the growing prime-power Gram cannot by itself be interpreted as arithmetic once the observation horizon crosses this threshold.

Keep the unweighted growing-depth shell notation of `PL-094`--`PL-097`:

```text
0<a<b<infinity,
A=log a,
B=log b,
Delta=B-A=log(b/a),
L=log X,
K=K(X)->infinity,
K=O(sqrt(L)),
Q_(X,>=K)={n=p^k : k>=K, aX<n<=bX},
N_X=|Q_(X,>=K)| -> infinity.
```

On

```text
H_T=L^2([0,T],dt/T),
nu_y(t)=exp(i t y),
P_y=|nu_y><nu_y|,
```

write

```text
A_(X,T)
 =(1/N_X) sum_(n in Q_(X,>=K)) P_(log(n/X)),

B_T
 =(1/Delta) integral_A^B P_y dy.
```

Thus `A_(X,T)` is the covariance realization of `G_(X,T)/N_X` from `PL-095`, while `B_T=C_T^(0)` is its log-uniform PNT continuum comparator. Both are positive trace-class operators of trace one, and `rank A_(X,T)=N_X`.

Let

```text
beta_1(T)>=beta_2(T)>=...>0
```

be the eigenvalues of `B_T`, and put

```text
S_N(T)=sum_(j=1)^N beta_j(T).
```

For **every** positive trace-one operator `R` of rank at most `N`, independently of any arithmetic structure,

```text
boxed:
||R-B_T||_(S_1) >= 2[1-S_N(T)].
```

Moreover this is the exact best possible rank-`N` trace-class error:

```text
boxed:
inf_{
 R>=0,
 Tr R=1,
 rank R<=N
}
||R-B_T||_(S_1)
 =2[1-S_N(T)].
```

The continuum operator is exactly the normalized prolate time-band limiting operator already identified in `PL-095`:

```text
B_T=(2 pi/(T Delta)) Q_(T Delta/4).
```

If `q_j(c)` are the standard prolate eigenvalues, then

```text
beta_j(T)=q_j(T Delta/4)/W_T,
W_T=T Delta/(2 pi),
```

where `W_T` is the classical time-bandwidth dimension. Landau--Pollak/Landau--Widom prolate eigenvalue concentration implies that only `O(log W_T)` eigenvalues lie in the transition between values asymptotically near `1` and values asymptotically near `0`. Consequently, for every finite ratio

```text
T_X/N_X -> tau in (0,infinity),
```

one has

```text
boxed:
S_(N_X)(T_X)
 -> min(1, 2 pi/(tau Delta)).
```

Therefore

```text
boxed:
liminf_(X->infinity)
||A_(X,T_X)-B_(T_X)||_(S_1)
 >=2(1-2 pi/(tau Delta))_+.
```

The same lower bound holds for the `ell^1` distance between the ordered eigenvalue lists of `G_(X,T_X)/N_X` and `B_(T_X)`.

Thus the raw `S_1` defect has a classical phase:

```text
tau <= 2 pi/Delta
    -> finite rank alone imposes no asymptotic S_1 defect;

tau > 2 pi/Delta
    -> every N_X-point covariance has a strictly positive
       universal rank floor;

tau -> infinity
    -> the floor tends to 2,
       recovering the maximal separation of PL-097.
```

The threshold is exactly the condition that the continuum time-bandwidth dimension

```text
W_T=T Delta/(2 pi)
```

exceed the available empirical rank `N_X`.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE` for the route

```text
growing prime-power shell
+ unweighted 1/N_X coherent covariance
+ finite critical ratio T_X/N_X -> tau > 2 pi/Delta
+ nonzero S_1 or ell^1 spectral defect from the continuum comparator
    -> rational-prime-specific or RH-sensitive information.
```

The lower bound does **not** say that the empirical prime-power covariance attains the optimal rank floor. Any excess above the floor may still depend on microscopic frequency spacing. What is ruled out is treating the existence or the universal minimum size of the trace-class discrepancy itself as arithmetic evidence.

## Exact rank-constrained trace-distance formula

Let `B>=0` be any trace-one compact operator with eigenvalues

```text
beta_1>=beta_2>=...>=0,
```

and let

```text
S_N=sum_(j=1)^N beta_j.
```

Take any positive trace-one `R` with `rank R<=N`, and let `P` be the support projection of `R`. Then

```text
rank P<=N,
PR=R.
```

The self-adjoint unitary

```text
Q=2P-I
```

has norm one, so trace-norm duality gives

```text
||R-B||_1
 >=|Tr Q(R-B)|.
```

Since `Tr R=Tr B=1`,

```text
Tr Q(R-B)
 =2-2 Tr(PB).
```

Ky Fan's variational principle gives

```text
Tr(PB)<=S_N,
```

and therefore

```text
||R-B||_1>=2(1-S_N).
```

This lower bound is sharp. Let `P_N` be the spectral projection of `B` onto its top `N` eigenvectors and define

```text
R_N=S_N^(-1) P_N B P_N.
```

Then `R_N>=0`, `Tr R_N=1`, `rank R_N<=N`, and `R_N` commutes with `B`. Hence

```text
||R_N-B||_1
 =sum_(j<=N) beta_j(1/S_N-1)
  +sum_(j>N) beta_j

 =(1-S_N)+(1-S_N)
 =2(1-S_N).
```

Thus the rank floor is not a rough inequality. It is the exact distance from the diffuse continuum state to the entire set of positive trace-one states of rank at most `N`.

For ordered eigenvalue lists the same tail obstruction is immediate. If `alpha_j` are the eigenvalues of a positive rank-`N` trace-one operator, padded by zeros, then

```text
sum_j |alpha_j-beta_j|
 >=|sum_(j<=N)(alpha_j-beta_j)|
   +sum_(j>N) beta_j

 =2(1-S_N).
```

So the obstruction survives even after discarding all eigenvector information.

## Prolate concentration makes the finite-ratio phase explicit

`PL-095` gives the exact unitary equivalence

```text
B_T=(2 pi/(T Delta))Q_c,
c=T Delta/4,
```

where `Q_c` is the classical prolate concentration operator on `[-1,1]` with kernel

```text
sin(c(x-x'))/[pi(x-x')].
```

Its trace is

```text
Tr Q_c=2c/pi=W_T=T Delta/(2 pi).
```

Thus, if `q_j(c)` are its decreasing eigenvalues,

```text
beta_j(T)=q_j(c)/W_T.
```

Classical time-frequency limiting theory shows that the spectrum of `Q_c` has a sharp step at index `W_T`: for every fixed `epsilon in (0,1/2)`, all but `O(log W_T)` of the eigenvalues are outside `[epsilon,1-epsilon]`, with the count of order-one eigenvalues equal to `W_T+O(log W_T)`. Equivalently for the present coarse ratio calculation,

```text
sum_(j<=N) q_j(c)
 =min(N,W_T)+o(W_T+N)
```

whenever `N/W_T` tends to a positive finite limit.

Now suppose

```text
T_X/N_X->tau.
```

Then

```text
W_(T_X)/N_X
 ->tau Delta/(2 pi).
```

Dividing the preceding partial-sum asymptotic by `W_(T_X)` yields

```text
S_(N_X)(T_X)
 =1/W_(T_X)
   sum_(j<=N_X)q_j

 ->min(1, 2 pi/(tau Delta)).
```

Substitution into the exact rank-distance formula gives the claimed Nyquist phase.

This strengthens `PL-097` in a specific way. The earlier finding used only

```text
S_N(T)<=N||B_T||
 <=2 pi N/(T Delta)
```

and therefore emphasized the limit `T/N->infinity`, where the trace distance becomes maximally `2`. The prolate spectral concentration shows that the same rank mechanism already creates a nonzero asymptotic floor as soon as

```text
T Delta/(2 pi)>N
```

by a fixed proportion. The super-`N` limit is merely the far end of this ordinary Nyquist transition.

## A weighted corollary already narrows the von-Mangoldt envelope branch

For the shell-weighted comparator of `PL-095`--`PL-097`,

```text
B_T^(1)
 =(1/Delta) integral_A^B exp(-y)P_y dy,

m=Tr B_T^(1)
 =(1/Delta)(1/a-1/b),
```

and the empirical weighted covariance has trace tending to `m` and rank at most `N_X`. The elementary support-projection argument of `PL-097`, together with

```text
||B_T^(1)||<=2 pi/(T Delta a),
```

gives, whenever `T_X/N_X->tau`,

```text
liminf
||C_(mu_X,T_X)^(1)-B_(T_X)^(1)||_1
 >=
[2m-4 pi/(tau Delta a)]_+.
```

This bound is not claimed sharp; the exact weighted threshold would require the corresponding Wiener--Hopf Ky Fan asymptotics. It is nevertheless enough to show that a finite-ratio universal rank floor also appears in the weighted envelope once `tau` is sufficiently large. Under the depth hypotheses of `PL-093`, its `S_1` equivalence transfers the same warning to the first `K^2`-renormalized von-Mangoldt Gram.

## Prior-art and novelty audit

The mechanism is classical at every structural level.

- H. J. Landau and H. O. Pollak, “Prolate spheroidal wave functions, Fourier analysis and uncertainty—III: The dimension of the space of essentially time- and band-limited signals,” *Bell System Technical Journal* **41** (1962), 1295–1336, established the time-bandwidth interpretation of the prolate spectrum.
- H. J. Landau and H. Widom, “Eigenvalue distribution of time and frequency limiting,” *Journal of Mathematical Analysis and Applications* **77**(2) (1980), 469–481, DOI `10.1016/0022-247X(80)90241-3`, gives the classical asymptotic eigenvalue distribution and logarithmic transition width used above.
- Ky Fan variational inequalities and best low-rank approximation in unitarily invariant norms are standard operator theory. The exact normalized-positive-state formula above is rederived directly rather than treated as a novelty claim.
- `PL-078` and `PL-080` already identified the same `2 pi` sampling constant in sharp logarithmic Gram systems, and `PL-095` identified `B_T` itself with the prolate operator. The present result is therefore a classicalization of the remaining `PL-097` trace-class window, not a new sampling theorem.

A targeted literature search for trace-norm/rank approximation of prolate time-frequency limiting operators and finite-rank covariance states returned the established low-rank/prolate operator setting rather than a prime-specific theorem. The result is stored because it gives a new line-specific boundary: **the raw trace-class discrepancy acquires a mandatory non-arithmetic component already at finite `T/N`, not only when `T/N->infinity`.**

The rational-prime discrimination control is decisive. The rank-distance formula holds for every `N`-point frequency cloud in `[A,B]`, and the comparator depends only on the macroscopic shell interval. Replacing the prime powers by any matched deterministic or random `N`-point set leaves the same Nyquist floor.

## Adversarial boundaries

1. **No `S_1` convergence is proved below Nyquist.** When `tau<=2 pi/Delta`, the rank floor tends to zero. The actual empirical covariance can still fail to converge in trace norm because of microscopic spacing or other structure.
2. **No exact empirical `S_1` limit is claimed above Nyquist.** The prime-power covariance may sit strictly farther from the continuum comparator than the optimal rank-`N` state. Only the mandatory universal component is identified.
3. **Arithmetic could survive in the excess over the rank floor.** A renormalized quantity subtracting `2(1-S_N)` or a target-relative observable is not covered by this no-go and would require a separate falsification control.
4. **The exact endpoint has a finer transition scale.** At `tau=2 pi/Delta` the coarse floor vanishes. The classical prolate transition has logarithmic width, so `T Delta/(2 pi)-N=O(log N)` is a separate edge regime not classified here.
5. **The weighted threshold above is only a sufficient rank obstruction.** No sharp Wiener--Hopf partial-eigenvalue asymptotic is asserted for `B_T^(1)` in this finding.
6. **The depth assumptions are inherited.** The unweighted rank statement itself only uses `N_X` distinct shell frequencies, but the interpretation as the growing prime-power/PNT envelope branch and the von-Mangoldt transfer use the regimes established in `PL-094`--`PL-097`.
7. **No analytic continuation or zero information enters.** The proof is finite Fourier/operator theory. It neither uses the Euler product beyond its convergence region nor constrains the Riemann zero divisor.

## Consequence for the surviving S1 branch

The hierarchy after `PL-095`--`PL-098` is now sharper:

```text
T_X * delta_X ->0
    -> S_1 transport to the PNT/prolate continuum (PL-095);

all T_X
    -> S_2 coherent spectral universality (PL-096);

T_X/N_X -> tau > 2 pi/Delta
    -> a positive S_1 defect is forced universally by
       time-bandwidth rank mismatch (PL-098);

T_X/N_X -> infinity
    -> that universal defect becomes maximal (PL-097).
```

Therefore the existence of a nonzero `S_1` discrepancy cannot be a rational-prime signal throughout the finite super-Nyquist phase. Any surviving arithmetic mechanism must either live on the **sub-/critical-Nyquist side**, use the excess over the universal rank floor, resolve microscopic prime-power spacing, or introduce a distinguished target/indefinite completed coupling that is not captured by positive covariance rank geometry.
